import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from readme_generator import ReadmeGenerator  # noqa: E402
from text_matching import contains_phrase  # noqa: E402


class BoundaryMatchingTests(unittest.TestCase):
    def test_hyphens_and_spaces_are_equivalent_but_substrings_do_not_match(self):
        self.assertTrue(contains_phrase("A text-to-video model", "text to video"))
        self.assertTrue(contains_phrase("A T2V model", "t2v"))
        self.assertFalse(contains_phrase("additional editing", "dit"))

    def test_readme_categories_use_boundary_matching(self):
        with tempfile.TemporaryDirectory() as temporary_dir:
            root = Path(temporary_dir)
            data_dir = root / "data"
            data_dir.mkdir()
            (data_dir / "keywords.json").write_text(
                json.dumps({
                    "common_keywords": {"keywords": ["video generation"]},
                    "categories": {
                        "Architecture & Efficiency": {
                            "description": "Architecture",
                            "keywords": ["dit"],
                        }
                    },
                }),
                encoding="utf-8",
            )
            template = root / "README_template.md"
            template.write_text("{{CATEGORIZED_PAPERS}}", encoding="utf-8")
            generator = ReadmeGenerator(
                data_dir=data_dir,
                template_path=template,
                readme_path=root / "README.md",
            )

            false_categories = generator.categorize_paper({
                "title": "Additional editing improvements",
                "keywords": ["editing"],
            })
            true_categories = generator.categorize_paper({
                "title": "A Video DiT Architecture",
                "keywords": ["dit"],
            })

            self.assertEqual([], false_categories)
            self.assertEqual(["Architecture & Efficiency"], true_categories)


if __name__ == "__main__":
    unittest.main()
