# News & Changelog

## [2026-08-08] Resilient Updates and Broader Video Indexing

### Reliable scheduled updates

- Standardized arXiv requests on `https://export.arxiv.org/api/query` with a project User-Agent.
- Added bounded retries for `429`, `5xx`, and network timeouts using `Retry-After` or 10/30/60-second backoff.
- Temporary arXiv failures and valid empty results preserve the latest valid snapshot, skip README generation and commits, and finish the scheduled workflow with a warning.
- Removed the three-day stale-data failure threshold; historical data is preserved regardless of age when the upstream failure is temporary.
- Configuration, XML parsing, validation, and programming errors remain hard failures.
- Added stable CLI exit codes, atomic data/README publication, strict JSON validation, and detailed Job Summary reporting.

### Expanded and more accurate indexing

- Increased the effective paper limit from 500 to 1,000 relevant papers.
- Moved date constraints into the arXiv query and continued pagination until the relevant-paper limit or the result set is exhausted.
- Expanded search coverage for video-to-video, flow matching, autoregressive video generation, video tokenizers, world foundation models, world simulators, and audio-video generation.
- Added `cs.RO`, `cs.GR`, `cs.CL`, `cs.HC`, `cs.SD`, `eess.IV`, and `eess.AS` to the searched arXiv domains.
- Added a local relevance filter that retains broad generative-video work while removing video understanding, VLM, recognition, compression, and image-quality false positives.
- Replaced substring keyword matching with boundary-aware matching, so short acronyms such as `DiT`, `T2V`, `I2V`, and `V2V` no longer match ordinary words.
- Expanded all 16 category vocabularies for newer architectures and tasks.

## [2026-02-09] Project Launched — v1.0

- 🚀 **awesome-video-diffusions** created, adapted from the [awesome-gaussians](https://github.com/longxiang-ai/awesome-gaussians) framework
- Configured 16 research categories covering the full spectrum of video diffusion research:
  - Surveys & Benchmarks, Text-to-Video Generation, Image-to-Video Generation, Video Editing
  - Controllable Generation, Long Video Generation, Human & Character Animation, World Models & Simulation
  - Video Super-Resolution & Enhancement, Architecture & Efficiency, 3D-aware Video Generation
  - Audio & Multi-modal, Personalization & Customization, Physical Understanding
  - Video Inpainting & Completion, Applications
- Set up arXiv search keywords for video diffusion, video generation, text-to-video, image-to-video, and related terms
- Inherited all features from awesome-gaussians framework:
  - Unified CLI with `init`, `search`, `suggest`, `export-bib`, `readme` subcommands
  - Interactive configuration wizard
  - Custom time range filtering
  - Smart link extraction
  - BibTeX export
  - LLM keyword suggestion
  - GitHub Actions daily automation
