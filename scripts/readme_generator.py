import json
import datetime
import sys
import os
import tempfile
from pathlib import Path
from typing import List, Dict, Optional
import re
from utils.logger import setup_logger
from collections import defaultdict
import argparse
from paper_data import find_latest_valid_snapshot, load_papers_file, validate_papers
from text_matching import contains_phrase

class ReadmeGenerator:
    def __init__(self, data_dir: Path = Path("data"),
                 template_path: Path = Path("README_template.md"),
                 readme_path: Path = Path("README.md")):
        self.logger = setup_logger("readme_generator")
        self.data_dir = Path(data_dir)
        self.template_path = Path(template_path)
        self.readme_path = Path(readme_path)

        # Check necessary directories and files
        if not self.data_dir.exists():
            self.logger.error(f"Data directory not found: {self.data_dir}")
            raise FileNotFoundError(f"Data directory not found: {self.data_dir}")

        if not self.template_path.exists():
            self.logger.error(f"Template file not found: {self.template_path}")
            raise FileNotFoundError(f"Template file not found: {self.template_path}")

        # Read template file
        try:
            with open(self.template_path, "r", encoding="utf-8") as f:
                self.template_content = f.read()
                self.logger.info(f"Successfully read template file, size: {len(self.template_content)} bytes")
        except Exception as e:
            self.logger.error(f"Failed to read template file: {e}")
            raise

        # Load keyword categories and common keywords from JSON
        try:
            keywords_path = self.data_dir / "keywords.json"
            if not keywords_path.exists():
                self.logger.error(f"Keywords file not found: {keywords_path}")
                raise FileNotFoundError(f"Keywords file not found: {keywords_path}")

            with open(keywords_path, "r", encoding="utf-8") as f:
                keywords_data = json.load(f)
                self.keyword_categories = keywords_data["categories"]
                self.common_keywords = keywords_data["common_keywords"]["keywords"]
                self.logger.info(f"Successfully loaded {len(self.keyword_categories)} keyword categories")
                self.logger.info(f"Successfully loaded {len(self.common_keywords)} common keywords")
        except Exception as e:
            self.logger.error(f"Failed to load keywords data: {e}")
            raise

        # Add configuration options
        self.show_latest_papers = False  # Default to not show latest papers section
        self.show_abstracts = False  # Default to not show abstracts

    def load_latest_papers(self, input_path: Optional[Path] = None) -> List[Dict]:
        """Load an explicit snapshot or the latest valid date-named snapshot."""
        if input_path is not None:
            selected_path = Path(input_path)
            papers = load_papers_file(selected_path)
        else:
            snapshot = find_latest_valid_snapshot(self.data_dir)
            if snapshot is None:
                self.logger.warning("No valid paper snapshot found")
                return []
            selected_path = snapshot.path
            papers = snapshot.papers

        self.logger.info("Loaded %s papers from %s", len(papers), selected_path)
        return papers

    def group_papers_by_month(self, papers: List[Dict]) -> Dict[str, List[Dict]]:
        """Group papers by month"""
        papers_by_month = {}
        for paper in papers:
            date = datetime.datetime.strptime(paper["published_date"], "%Y-%m-%d")
            month_key = date.strftime("%B %Y")  # Format: "February 2024"
            if month_key not in papers_by_month:
                papers_by_month[month_key] = []
            papers_by_month[month_key].append(paper)
        return papers_by_month

    def _extract_keywords(self, abstract: str, title: str) -> List[str]:
        """Extract boundary-aware keywords from abstract and title."""
        keywords = []
        text = abstract + " " + title

        # Check each common keyword
        for keyword in self.common_keywords:
            if contains_phrase(text, keyword):
                keywords.append(keyword)

        return keywords

    def format_paper_entry(self, paper: Dict) -> str:
        """Format a single paper entry"""
        try:
            arxiv_id = paper["arxiv_url"].split("/")[-1]

            # Basic information
            entry = f'- **[{paper["title"]}](https://arxiv.org/abs/{arxiv_id})**  \n'

            # Add authors
            authors = paper["authors"]
            entry += f'  Authors: {", ".join(authors)}  \n'

            # Add links with different styles
            link_badges = []
            # Always add arXiv PDF link
            link_badges.append(f'[![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/{arxiv_id}.pdf)')

            # Use the structured links field if available, otherwise fall back to old logic
            paper_links = paper.get("links", {})

            # GitHub link
            github_url = paper_links.get("github") or paper.get("github_url", "")
            if github_url:
                parts = github_url.split('github.com/')[-1].split('/')
                if len(parts) >= 2:
                    owner, repo = parts[0], parts[1]
                    link_badges.append(f'[![GitHub](https://img.shields.io/github/stars/{owner}/{repo}?style=social)]({github_url})')

            # Project page link
            project_url = paper_links.get("project")
            if not project_url and paper.get("abstract"):
                # Fallback: extract from abstract
                urls = re.findall(r'https?://[^\s<>"]+|www\.[^\s<>"]+', paper["abstract"])
                for url in urls:
                    if not url.startswith('http'):
                        url = 'https://' + url
                    if 'arxiv.org' not in url and 'github.com' not in url:
                        project_url = url
                        break
            if project_url:
                link_badges.append(f'[![Project](https://img.shields.io/badge/-Project-blue)]({project_url})')

            # Dataset link
            dataset_url = paper_links.get("dataset")
            if dataset_url:
                link_badges.append(f'[![Dataset](https://img.shields.io/badge/-Dataset-orange)]({dataset_url})')

            # Video link
            video_url = paper_links.get("video")
            if video_url:
                link_badges.append(f'[![Video](https://img.shields.io/badge/-Video-red)]({video_url})')

            # Demo link
            demo_url = paper_links.get("demo")
            if demo_url:
                link_badges.append(f'[![Demo](https://img.shields.io/badge/-Demo-brightgreen)]({demo_url})')

            # HuggingFace link
            hf_url = paper_links.get("huggingface")
            if hf_url:
                link_badges.append(f'[![HuggingFace](https://img.shields.io/badge/-HuggingFace-yellow)]({hf_url})')

            # Handle Semantic Scholar citations
            if paper.get("semantic_url"):
                link_badges.append(f'[![Citations](https://img.shields.io/badge/Citations-{paper.get("citations", 0)}-green)]({paper["semantic_url"]})')

            entry += f'  Links: {" | ".join(link_badges)}  \n'

            # Only add abstract if enabled
            if self.show_abstracts:
                abstract = paper["abstract"]
                words = abstract.split()
                if len(words) > 150:
                    abstract = ' '.join(words[:150]) + "..."
                entry += f'  <details><summary>Abstract</summary>\n\n  {abstract}\n  </details>  \n'

            # Add keywords (use existing keywords or extract from abstract/title)
            if paper.get("keywords"):
                keywords = paper["keywords"]
            else:
                keywords = self._extract_keywords(paper["abstract"], paper["title"])
            if keywords:
                entry += f'  Keywords: {", ".join(keywords)}  \n'

            return entry
        except Exception as e:
            self.logger.error(f"Error formatting paper entry: {e}")
            raise

    def categorize_paper(self, paper: Dict) -> List[str]:
        """Categorize paper based on its keywords and title"""
        categories = set()

        title = paper["title"]
        keyword_text = " ".join(paper["keywords"] or [])

        # Check each category's keywords
        for category, category_info in self.keyword_categories.items():
            category_keywords = category_info["keywords"]
            for keyword in category_keywords:
                if contains_phrase(title, keyword) or contains_phrase(
                    keyword_text, keyword
                ):
                    categories.add(category)

        return list(categories)

    def generate_navigation(self, categorized_papers: Dict[str, List[Dict]]) -> str:
        """Generate navigation section with descriptions"""
        nav = "## Categories\n\n"
        for category in sorted(categorized_papers.keys()):
            if categorized_papers[category]:  # Only show categories with papers
                paper_count = len(categorized_papers[category])
                description = self.keyword_categories[category]["description"]
                nav += f"- [{category}](#{category.lower().replace(' ', '-')}) ({paper_count} papers) - {description}\n"
        return nav + "\n"

    def generate_categorized_sections(self, categorized_papers: Dict[str, List[Dict]]) -> str:
        """Generate sections for each category"""
        sections = "## Categorized Papers\n\n"

        # Sort papers by date in each category
        for category in sorted(categorized_papers.keys()):
            if categorized_papers[category]:  # Only show categories with papers
                # Sort papers by date (newest first)
                sorted_papers = sorted(
                    categorized_papers[category],
                    key=lambda x: x["published_date"],
                    reverse=True
                )

                # Only show the latest 10 papers in each category
                papers_to_show = sorted_papers[:10]
                total_papers = len(sorted_papers)

                sections += f"### {category}\n\n"
                if total_papers > 50:
                    sections += f"*Showing the latest 50 out of {total_papers} papers*\n\n"

                for paper in papers_to_show:
                    sections += self.format_paper_entry(paper)
                sections += "\n"
        return sections

    def render_readme(
        self,
        papers: List[Dict],
        updated_at: Optional[datetime.datetime] = None,
    ) -> str:
        """Render README content without modifying the working tree."""
        papers = validate_papers(papers)
        papers_by_month = self.group_papers_by_month(papers)
        self.logger.info("Grouped by months: %s", list(papers_by_month.keys()))

        categorized_papers = defaultdict(list)
        for paper in papers:
            categories = self.categorize_paper(paper)
            for category in categories:
                categorized_papers[category].append(paper)

        navigation = self.generate_navigation(categorized_papers)
        latest_papers_section = ""
        if self.show_latest_papers:
            latest_papers_section = "## Latest Papers\n> 🔄 Updated Daily\n\n"
            for month, month_papers in sorted(papers_by_month.items(), reverse=True):
                self.logger.info("Processing %s papers for %s", len(month_papers), month)
                latest_papers_section += f"### {month}\n"
                for paper in month_papers:
                    latest_papers_section += self.format_paper_entry(paper)
                latest_papers_section += "\n"

        categorized_sections = self.generate_categorized_sections(categorized_papers)
        toc = "## Table of Contents\n\n"
        if self.show_latest_papers:
            toc += "- [Latest Papers](#latest-papers)\n"
        toc += "- [Categorized Papers](#categorized-papers)\n"
        toc += "- [Classic Papers](#classic-papers)\n"
        toc += "- [Open Source Projects](#open-source-projects)\n"
        toc += "- [Applications](#applications)\n"
        toc += "- [Tutorials & Blogs](#tutorials--blogs)\n\n"

        if updated_at is None:
            updated_at = datetime.datetime.now()
        readme_content = self.template_content
        readme_content = readme_content.replace("{{NAVIGATION}}", navigation)
        readme_content = readme_content.replace("{{TABLE_OF_CONTENTS}}", toc)
        readme_content = readme_content.replace("{{LATEST_PAPERS}}", latest_papers_section)
        readme_content = readme_content.replace("{{CATEGORIZED_PAPERS}}", categorized_sections)
        return readme_content.replace(
            "{{LAST_UPDATE}}", updated_at.strftime("%Y-%m-%d %H:%M:%S")
        )

    def generate_readme(
        self,
        input_path: Optional[Path] = None,
        output_path: Optional[Path] = None,
        papers: Optional[List[Dict]] = None,
        updated_at: Optional[datetime.datetime] = None,
    ) -> Path:
        """Generate README atomically from an explicit or latest valid snapshot."""
        self.logger.info("Starting README generation...")
        if papers is None:
            papers = self.load_latest_papers(input_path)
        papers = validate_papers(papers)
        readme_content = self.render_readme(papers, updated_at=updated_at)

        target_path = Path(output_path) if output_path is not None else self.readme_path
        target_path.parent.mkdir(parents=True, exist_ok=True)
        temporary_path = None
        try:
            with tempfile.NamedTemporaryFile(
                "w",
                encoding="utf-8",
                dir=target_path.parent,
                prefix=f".{target_path.name}.",
                suffix=".tmp",
                delete=False,
            ) as handle:
                temporary_path = Path(handle.name)
                handle.write(readme_content)
            os.replace(temporary_path, target_path)
            self.logger.info(
                "README generated at %s, size: %s bytes",
                target_path,
                target_path.stat().st_size,
            )
            return target_path
        finally:
            if temporary_path is not None and temporary_path.exists():
                temporary_path.unlink()

def main():
    parser = argparse.ArgumentParser(description='README Generator')
    parser.add_argument('--input', type=Path, default=None,
                      help='Explicit papers JSON file')
    parser.add_argument('--output', type=Path, default=None,
                      help='README output path')
    parser.add_argument('--show-latest', action='store_true',
                      help='Show latest papers section in chronological order')
    parser.add_argument('--show-abstracts', action='store_true',
                      help='Include paper abstracts in the output')
    args = parser.parse_args()

    try:
        generator = ReadmeGenerator()
        generator.show_latest_papers = args.show_latest
        generator.show_abstracts = args.show_abstracts
        generator.generate_readme(input_path=args.input, output_path=args.output)
    except Exception as e:
        print(f"README generator failed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
