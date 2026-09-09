# Awesome Video Diffusions [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Video Diffusion Models and Video Generation. Content is automatically updated daily.

> Last Update: 2026-09-09 03:23:16

## 📰 Latest Updates

🔧 **[2026-08-08] Resilient Scheduled Updates**
- Temporary arXiv rate limits, server errors, and timeouts now preserve the latest valid data and finish with a warning
- Added stable search exit codes, atomic publication, strict JSON validation, and fallback to any valid historical snapshot

🔎 **[2026-08-08] Broader and More Accurate Video Indexing**
- Expanded coverage to 1,000 relevant papers across diffusion, flow matching, autoregressive generation, world models, editing, enhancement, and audio-video generation
- Added broader arXiv domains, local relevance filtering, and boundary-aware category matching for acronyms such as DiT, T2V, I2V, and V2V

🚀 **[2026-02] Project Launched — v1.0**
- Adapted from [awesome-gaussians](https://github.com/longxiang-ai/awesome-gaussians) framework for tracking video diffusion research
- **Unified CLI**: Single entry point `python main.py` with subcommands: `init`, `search`, `suggest`, `export-bib`, `readme`
- **Interactive Configuration Wizard**: Run `python main.py init` to set up keywords, domains, time range, and API keys step-by-step
- **Custom Time Range Filtering**: Support relative periods (`6m`, `1y`, `2y`) and absolute date ranges
- **Smart Link Extraction**: Automatically extracts and classifies GitHub, project page, dataset, video, demo, and HuggingFace links from paper abstracts
- **BibTeX Export**: Fetch BibTeX from arXiv and export to `.bib` files with category/date filters
- **LLM Keyword Suggestion**: Paste a few paper titles or arXiv IDs, and an LLM automatically generates optimized search keywords
- **arXiv Domain Filtering**: Restrict searches to specific arXiv categories (e.g., `cs.CV`, `cs.AI`, `cs.MM`)
- **16 Research Categories**: Comprehensive taxonomy covering T2V, I2V, video editing, controllable generation, world models, and more

- View detailed updates: [News.md](News.md) 📋

---

## Categories

- [3D-aware Video Generation](#3d-aware-video-generation) (53 papers) - Video generation with 3D awareness, multi-view consistency, and 4D content creation
- [Applications](#applications) (211 papers) - Domain-specific applications of video diffusion models
- [Architecture & Efficiency](#architecture-&-efficiency) (395 papers) - Architectural innovations (DiT, UNet), flow matching, and training/inference efficiency
- [Audio & Multi-modal](#audio-&-multi-modal) (72 papers) - Audio-driven and multi-modal conditioned video generation
- [Controllable Generation](#controllable-generation) (328 papers) - Controllable video generation with motion, camera, pose, or layout guidance
- [Human & Character Animation](#human-&-character-animation) (65 papers) - Human-centric video generation including talking heads, dance, and character animation
- [Image-to-Video Generation](#image-to-video-generation) (95 papers) - Methods for animating still images into videos
- [Long Video Generation](#long-video-generation) (270 papers) - Generating temporally consistent long-form videos beyond short clips
- [Personalization & Customization](#personalization-&-customization) (183 papers) - Personalized video generation with custom subjects, identities, or styles
- [Physical Understanding](#physical-understanding) (310 papers) - Physics-aware video generation and dynamics modeling
- [Surveys & Benchmarks](#surveys-&-benchmarks) (313 papers) - Survey papers, benchmarks, and evaluation metrics for video generation
- [Text-to-Video Generation](#text-to-video-generation) (140 papers) - Foundation models and methods for generating videos from text prompts
- [Video Editing](#video-editing) (102 papers) - Diffusion-based video editing, style transfer, and manipulation
- [Video Inpainting & Completion](#video-inpainting-&-completion) (24 papers) - Video inpainting, completion, outpainting, and temporal prediction
- [Video Super-Resolution & Enhancement](#video-super-resolution-&-enhancement) (163 papers) - Video quality improvement, upscaling, restoration, and frame interpolation
- [World Models & Simulation](#world-models-&-simulation) (257 papers) - Video generation as world simulators and interactive environment generation



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3D-aware Video Generation

*Showing the latest 50 out of 53 papers*

- **[Rethinking 3D Noise: Learning 3D-Aware Video Priors via Optimization-Free Morphological Perturbations](https://arxiv.org/abs/2609.03657v1)**  
  Authors: Onat Şahin, Mohammad Altillawi, George Eskandar, Carlos Carbone, Ziyuan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.03657v1.pdf)  
  Keywords: 3d-aware, robotics, video diffusion  
- **[Stabilizing Camera-Controlled Novel View Synthesis at Inference Time](https://arxiv.org/abs/2609.03639v1)**  
  Authors: Prajwal Singh, Arjun Badola, Seema Kumari, Hajime Nagahara, Shanmuganathan Raman  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.03639v1.pdf)  
  Keywords: autoregressive, camera motion, efficient, novel view, video diffusion  
- **[Building Pretraining Data for World Models: An Unreal Engine-Based Pipeline for Action-Conditioned Video Generation](https://arxiv.org/abs/2609.03557v1)**  
  Authors: Haoyu Wang, Songchun Zhang, Haoran Li, Haoyang Huang, Zeyue Xue, Nan Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.03557v1.pdf)  
  Keywords: action-conditioned, architecture, multi-view video, physics, trajectory, video generation, world model  
- **[RoGe: Novel View Synthesis via End-to-End Implicit Reconstruction and Generation](https://arxiv.org/abs/2609.02847v2)**  
  Authors: Xiaolei Lang, Ze Kang, Zehao Huang, Naiyan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.02847v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jerry-locker.github.io/roge)  
  Keywords: camera trajectory, diffusion model, novel view, temporal consistency, trajectory, video diffusion  
- **[Spatially Aware World Action Model via Geometric Latent Diffusion](https://arxiv.org/abs/2609.02531v1)**  
  Authors: Javier Alejandro Lopetegui Gonzalez, Paul Pacaud, Cordelia Schmid  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.02531v1.pdf)  
  Keywords: 3d-aware, evaluation, physical, video diffusion, world model  
- **[Streaming4D: Accelerate 4D World Models via Block-wise Video Generation and Incremental Reconstruction](https://arxiv.org/abs/2609.00610v1)**  
  Authors: Xiaoyan Liu, Jiaxin Liu, Kangrui Li, Sifan Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.00610v1.pdf)  
  Keywords: 4d generation, autoregressive, autoregressive video, interactive, style, video generation  
- **[4DStreamCtrl: Interactive Video Generation with Online 4D Control](https://arxiv.org/abs/2608.25479v2)**  
  Authors: Shiqian Li, Chenguo Lin, Zhiguang Liu, Yu Tang, Jiarong Ou, Rui Chen, Yixin Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.25479v2.pdf)  
  Keywords: 3d consistent, camera motion, controllable, denoising, diffusion model, efficient, embodied, interactive, long video, motion control, motion transfer, streaming, trajectory, video diffusion, video generation  
- **[FixAnything: 3D-Consistent Rendering Refinement via Video Generative Priors](https://arxiv.org/abs/2608.23549v1)**  
  Authors: Khiem Vuong, Deva Ramanan, Srinivasa Narasimhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.23549v1.pdf)  
  Keywords: 3d consistent, camera motion, video to video, video translation, video-to-video  
- **[GaussVid: Sparse-View Gaussian Splatting with 3D-Aware Video Diffusion Priors](https://arxiv.org/abs/2608.21849v1)**  
  Authors: Xinhui Liu, Can Wang, Wei Jiang, Wei Wang, Dong Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.21849v1.pdf)  
  Keywords: 3d-aware, camera-conditioned, novel view, video diffusion, video generation, video restoration  
- **[Grounded-Exo2Ego: Structured Semantic Grounding for Robust Exocentric-to-Egocentric Video Generation](https://arxiv.org/abs/2608.20534v1)**  
  Authors: Shengze Wang, Michael Stengel, Tianye Li, Seonwook Park, Amrita Mazumdar, Koki Nagano, Alex Trevithick, Shalini De Mello  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.20534v1.pdf)  
  Keywords: diffusion model, evaluation, novel view, physical, video diffusion, video generation  

### Applications

*Showing the latest 50 out of 211 papers*

- **[Beyond Coherence: Benchmarking Professional Editing-Technique Execution in Multi-Shot Audio-Video Generation](https://arxiv.org/abs/2609.08275v1)**  
  Authors: Tianyi Zeng, Junchao Liao, Yujie Wei, Ziying Zhang, Litao Li, Tianyi Wang, Zhichao Wei, Shuyao Xu, Wenwen Qiang, Siyu Zhu, Zhenghao Zhang, Long Qin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.08275v1.pdf) | [![GitHub](https://img.shields.io/github/stars/AlibabaResearch/cut-craft-bench?style=social)](https://github.com/AlibabaResearch/cut-craft-bench)  
  Keywords: audio-video generation, benchmark, cinematic, evaluation, physical, physical plausibility, video generation  
- **[PhysFlow: Physics-Aware Optical Flow for Motion Controllable Video Generation](https://arxiv.org/abs/2609.08215v1)**  
  Authors: Cong Wang, Hanxin Zhu, Yonglin Tian, Jiayi Luo, Ruiqi Song, Boyi Sun, Long Chen, Zhibo Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.08215v1.pdf)  
  Keywords: controllable, driving, dynamics, physical, physical plausibility, physics, physics-aware, video generation  
- **[Geodesic-informed Generative Diffusion Model For Topology-preserved Image Video Generation](https://arxiv.org/abs/2609.08153v1)**  
  Authors: Nian Wu, Nivetha Jayakumar, Jiarui Xing, Miaomiao Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.08153v1.pdf) | [![GitHub](https://img.shields.io/github/stars/nellie689/IGG?style=social)](https://github.com/nellie689/IGG)  
  Keywords: diffusion model, dynamics, robotics, video generation  
- **[VI-Bench: Benchmarking Prompt Inversion from AIGC Videos](https://arxiv.org/abs/2609.08079v1)**  
  Authors: Wulin Xie, Rui Zhao, Kecen Li, Xiujin Liu, Bokang Zhang, Zheng Liu, Xinwen Hou, Chen Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.08079v1.pdf)  
  Keywords: benchmark, creative, style, video generation  
- **[Better Call CineCrew: Consistent Ultra-Long Narrative-to-Film Generation](https://arxiv.org/abs/2609.07720v1)**  
  Authors: Jiaben Chen, Sixun Dong, Qinhong Zhou, Raine Ma, Zhiyang Dou, Wojciech Matusik, Chuang Gan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.07720v1.pdf)  
  Keywords: cinematic, film, film generation, identity, long-form, style, video generation  
- **[PRG-Fusion: Orchestrating Generative Priors with Reconstruction Evidence for Driving View Synthesis](https://arxiv.org/abs/2609.06948v1)**  
  Authors: Sipeng He, Jialei Chen, Zhen Fang, Dongchun Ren, Feng Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.06948v1.pdf)  
  Keywords: driving, simulation, trajectory, video synthesis  
- **[PAI-Actor: Cinematic Multi-Character Replacement in Dynamic Scenes](https://arxiv.org/abs/2609.05918v1)**  
  Authors: Bangxun Tang, Heyuan Gao, Yiren Song, Guian Fang, Zijian He, Jie Yang, Mike Zheng Shou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.05918v1.pdf)  
  Keywords: autoregressive, autoregressive video, camera motion, character animation, cinematic, diffusion transformer, distillation, dynamics, efficient, film, long-form, video generation, video to video, video-to-video  
- **[Rethinking 3D Noise: Learning 3D-Aware Video Priors via Optimization-Free Morphological Perturbations](https://arxiv.org/abs/2609.03657v1)**  
  Authors: Onat Şahin, Mohammad Altillawi, George Eskandar, Carlos Carbone, Ziyuan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.03657v1.pdf)  
  Keywords: 3d-aware, robotics, video diffusion  
- **[CAER: Causal Action Effect Reweighting for World Model Training](https://arxiv.org/abs/2608.30897v1)**  
  Authors: Jianjie Fang, Xvyuan Liu, Ziyou Wang, Rongze Tang, Zhaolu Wang, Zhuohang Li, Xin Zhang, Haisheng Su, Chen Gao, Wei Wu, Xinlei Chen, Yong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.30897v1.pdf)  
  Keywords: action-conditioned, controllable, dynamics, embodied, physical, physical consistency, video generation, world model  
- **[Matrix-Game 3.5: Enhancing Real-Time Streaming Interactive World Models with Patch Memory](https://arxiv.org/abs/2608.29910v1)**  
  Authors: Runjia Qian, Zile Wang, Jihai Zhang, Kai Zou, Wei Yu, Jiaxing Li, Zexiang Liu, Yaokun Li, Fei Kang, Kaichen Huang, Mengyin An, Haobo Zhang, Biao Jiang, Jiahua Wang, Haofeng Sun, Yang Liu, Yangguang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.29910v1.pdf)  
  Keywords: autoregressive, camera control, diffusion model, distillation, embodied, flow matching, game, identity, interactive, minute-long, robotics, simulation, streaming, video generation  

### Architecture & Efficiency

*Showing the latest 50 out of 395 papers*

- **[SignRefine: Adapting Foundational Video Models for Sign Language Generation](https://arxiv.org/abs/2609.08496v1)**  
  Authors: Anton Pelykh, Edward Fish, Ozge Mercanoglu Sincan, Richard Bowden  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.08496v1.pdf)  
  Keywords: diffusion transformer, video diffusion, video diffusion transformer, video generation  
- **[Generalist Open-World Temporal Perception](https://arxiv.org/abs/2609.06823v1)**  
  Authors: Cristian Sminchisescu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.06823v1.pdf)  
  Keywords: architecture, controllable, identity, physical, simulation, world model  
- **[RoLA: Rotary-Positioned Low-Rank Linear Attention for Efficient Diffusion Transformers](https://arxiv.org/abs/2609.06712v1)**  
  Authors: Zekun Zhang, Yixiang Cai, Yuxi Liu, Tengxu Sun, Tianle Liu, Zhoutong Wu, Haoyu Li, Baole Ai, Ang Wang, Jiamang Wang, Lin Qu, Kun Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.06712v1.pdf)  
  Keywords: efficient, video generation  
- **[MVWeaver: A Hierarchical Music Video Generation Agent with a Learned Song-to-Visual Bridge](https://arxiv.org/abs/2609.06478v1)**  
  Authors: Sifei Li, Minyan Luo, Xu Li, Guodong Qi, Xincan Wang, Hanwen Wang, Chen Zhang, Pengfei Wan, Oliver Deussen, Weiming Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.06478v1.pdf)  
  Keywords: architecture, long-form, music video, video generation  
- **[TBDub: Production-Oriented Visual Dubbing](https://arxiv.org/abs/2609.06144v1)**  
  Authors: Bihan Li, Xinyang Li, Zeran Xu, Meiguang Jin, Junfeng Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.06144v1.pdf) | [![GitHub](https://img.shields.io/github/stars/TaoLiveAIGC/TBDub?style=social)](https://github.com/TaoLiveAIGC/TBDub) | [![Project](https://img.shields.io/badge/-Project-blue)](https://huggingface.co/TaoLiveAIGC/TBDub.) | [![HuggingFace](https://img.shields.io/badge/-HuggingFace-yellow)](https://huggingface.co/TaoLiveAIGC/TBDub)  
  Keywords: distillation, dit, evaluation, identity, temporal consistency, video dit, video editing  
- **[PAI-Actor: Cinematic Multi-Character Replacement in Dynamic Scenes](https://arxiv.org/abs/2609.05918v1)**  
  Authors: Bangxun Tang, Heyuan Gao, Yiren Song, Guian Fang, Zijian He, Jie Yang, Mike Zheng Shou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.05918v1.pdf)  
  Keywords: autoregressive, autoregressive video, camera motion, character animation, cinematic, diffusion transformer, distillation, dynamics, efficient, film, long-form, video generation, video to video, video-to-video  
- **[ReaDiT Guidance: Control for Image and Video Generation using Diffusion Transformer Features](https://arxiv.org/abs/2609.04649v1)**  
  Authors: Jay Mahajan, Chang Liu, Rauf Makharov, Viraj Shah, Alexander Schwing, Svetlana Lazebnik  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.04649v1.pdf)  
  Keywords: diffusion transformer, dit, motion control, text to video, text-to-video, video generation  
- **[DSAQuant: Denoising-Stage-Aligned Quantization-Aware Training for Video Generation](https://arxiv.org/abs/2609.04031v1)**  
  Authors: Shuaiting Li, Zelin Gao, Haibin Shen, Yujun Shen, Haotong Qin, Yinghao Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.04031v1.pdf)  
  Keywords: denoising, distillation, layout, text to video, text-to-video, video denoising, video diffusion, video generation  
- **[Stabilizing Camera-Controlled Novel View Synthesis at Inference Time](https://arxiv.org/abs/2609.03639v1)**  
  Authors: Prajwal Singh, Arjun Badola, Seema Kumari, Hajime Nagahara, Shanmuganathan Raman  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.03639v1.pdf)  
  Keywords: autoregressive, camera motion, efficient, novel view, video diffusion  
- **[EraseSAE: Surgical Concept Erasure in Text-to-Video Diffusion Models via Sparse Autoencoders](https://arxiv.org/abs/2609.03629v2)**  
  Authors: Xinghao Wang, Dong Li, Wei Yu, Yingwei Pan, Tao Gong, Qi Chu, Nenghai Yu, Ting Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.03629v2.pdf) | [![GitHub](https://img.shields.io/github/stars/HiDream-ai/EraseSAE?style=social)](https://github.com/HiDream-ai/EraseSAE)  
  Keywords: concept, dit, t2v, text to video, text-to-video, video diffusion  

### Audio & Multi-modal

*Showing the latest 50 out of 72 papers*

- **[Beyond Coherence: Benchmarking Professional Editing-Technique Execution in Multi-Shot Audio-Video Generation](https://arxiv.org/abs/2609.08275v1)**  
  Authors: Tianyi Zeng, Junchao Liao, Yujie Wei, Ziying Zhang, Litao Li, Tianyi Wang, Zhichao Wei, Shuyao Xu, Wenwen Qiang, Siyu Zhu, Zhenghao Zhang, Long Qin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.08275v1.pdf) | [![GitHub](https://img.shields.io/github/stars/AlibabaResearch/cut-craft-bench?style=social)](https://github.com/AlibabaResearch/cut-craft-bench)  
  Keywords: audio-video generation, benchmark, cinematic, evaluation, physical, physical plausibility, video generation  
- **[AV-SafetyBench: A Safety Benchmark for Text-to-Audio-Video Generation](https://arxiv.org/abs/2609.06991v1)**  
  Authors: Suah Choi, Tae-Young Lee, Gyeong-Moon Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.06991v1.pdf)  
  Keywords: audio-video generation, benchmark, evaluation, sound, video generation  
- **[MVWeaver: A Hierarchical Music Video Generation Agent with a Learned Song-to-Visual Bridge](https://arxiv.org/abs/2609.06478v1)**  
  Authors: Sifei Li, Minyan Luo, Xu Li, Guodong Qi, Xincan Wang, Hanwen Wang, Chen Zhang, Pengfei Wan, Oliver Deussen, Weiming Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.06478v1.pdf)  
  Keywords: architecture, long-form, music video, video generation  
- **[PRISM-Bench: An Audio-Centric Diagnostic Benchmark for Text-to-Audio-Video Generation](https://arxiv.org/abs/2609.04867v1)**  
  Authors: Yuchen Sun, Qian Yang, Jun Wang, Detai Xin, Guoqiao Yu, Guanglu Wan, Qi Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.04867v1.pdf)  
  Keywords: audio-video generation, benchmark, evaluation, sound, video generation  
- **[The Attention Triangle in Audio-Video Models](https://arxiv.org/abs/2609.03586v1)**  
  Authors: Sagi Polaczek, Noa Kraicer, Gal Metzer, Zhuo Ning, Ali Mahdavi-Amiri, Daniel Cohen-Or, Raja Giryes  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.03586v1.pdf)  
  Keywords: dynamics, sound, video diffusion, video generation  
- **[The Missing Temporal Link: Temporal Context Routing for Script-Driven Audio-Video Generation](https://arxiv.org/abs/2609.02367v1)**  
  Authors: Yichen Liu, Quanwei Zhang, Haozhe Wang, Donghao Zhou, Xiaojie Li, Yang Shi, Jiaming Liu, Ruihua Huang, Yingtian Zou, Daquan Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.02367v1.pdf)  
  Keywords: audio-video generation, joint audio-video, video generation  
- **[DreamX-Creator: Democratizing Native Audio-Video Generation at 2K Resolution](https://arxiv.org/abs/2608.31106v1)**  
  Authors: Jiashu Zhu, Yanhao Zheng, Ruitian Tian, Rujing Dang, Shen Zhang, Bingze Song, Jiachen Lei, Ruimin Lin, Jiahong Wu, Xiangxiang Chu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.31106v1.pdf)  
  Keywords: audio-video generation, autoregressive, denoising, dynamics, evaluation, joint audio-video, video generation  
- **[Encore: Infinite Audio-Video Generation with Adaptive Signal Routing](https://arxiv.org/abs/2609.04249v1)**  
  Authors: Shaohua Pan, Junbao Chen, Shengyi He, Jingfeng Xue, Wen Tao, Haocheng Feng, Siming Fan, Dongwei Pan, Yi Yang, Wei He, Hang Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.04249v1.pdf) | [![GitHub](https://img.shields.io/github/stars/shaohua-pan/Encore?style=social)](https://github.com/shaohua-pan/Encore)  
  Keywords: audio-to-video, audio-video generation, denoising, evaluation, joint audio-video, long video, long-form, video generation, video-to-audio  
- **[Multi2AV-Safety: Benchmarking Safety in Multimodal-to-Audio-Video Generation](https://arxiv.org/abs/2608.26535v1)**  
  Authors: Kaichao Jiang, Changtao Miao, Baiqi Wu, Zhiyuan Lu, Kang Yang, Peiwei Zhao, Junchi Chen, Yunfeng Diao, He Liu, Qi Chu, Tao Gong, Nenghai Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.26535v1.pdf)  
  Keywords: audio-video generation, benchmark, evaluation, video generation  
- **[StreamAV-Bench: A Comprehensive Benchmark for Streaming Audio-Video Generation](https://arxiv.org/abs/2608.26336v1)**  
  Authors: Kaiqi Liu, Haoxuan Zeng, Jingqi Liu, Jiacong Fang, Ziqi Cai, Yunyao Mao, Henglin Liu, Yu Sheng, Shuchen Weng, Boxin Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.26336v1.pdf)  
  Keywords: audio-video generation, benchmark, evaluation, interactive, joint audio-video, streaming, video generation  

### Controllable Generation

*Showing the latest 50 out of 328 papers*

- **[Temporal State Transport in Video Generation: Diagnosing and Correcting Spectral Imbalance](https://arxiv.org/abs/2609.08505v1)**  
  Authors: Luyao Tang, Bingjun Luo, Dong Yi, Jialin Guo, Haoning Xi, Cheng Chen, Yizhou Yu, Chaoqi Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.08505v1.pdf) | [![GitHub](https://img.shields.io/github/stars/lytang63/temporal-state-transport?style=social)](https://github.com/lytang63/temporal-state-transport)  
  Keywords: identity, layout, temporal consistency, video generation  
- **[PhysFlow: Physics-Aware Optical Flow for Motion Controllable Video Generation](https://arxiv.org/abs/2609.08215v1)**  
  Authors: Cong Wang, Hanxin Zhu, Yonglin Tian, Jiayi Luo, Ruiqi Song, Boyi Sun, Long Chen, Zhibo Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.08215v1.pdf)  
  Keywords: controllable, driving, dynamics, physical, physical plausibility, physics, physics-aware, video generation  
- **[The Price of Consistency: Exploiting Visual Anchors for Multimodal Jailbreaking in Video Generation](https://arxiv.org/abs/2609.07216v1)**  
  Authors: Peng Li, Qianqian Xu, Yangbangyan Jiang, Zhipeng Yu, Qingming Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.07216v1.pdf)  
  Keywords: benchmark, controllable, video generation  
- **[PRG-Fusion: Orchestrating Generative Priors with Reconstruction Evidence for Driving View Synthesis](https://arxiv.org/abs/2609.06948v1)**  
  Authors: Sipeng He, Jialei Chen, Zhen Fang, Dongchun Ren, Feng Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.06948v1.pdf)  
  Keywords: driving, simulation, trajectory, video synthesis  
- **[Generalist Open-World Temporal Perception](https://arxiv.org/abs/2609.06823v1)**  
  Authors: Cristian Sminchisescu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.06823v1.pdf)  
  Keywords: architecture, controllable, identity, physical, simulation, world model  
- **[PAI-Actor: Cinematic Multi-Character Replacement in Dynamic Scenes](https://arxiv.org/abs/2609.05918v1)**  
  Authors: Bangxun Tang, Heyuan Gao, Yiren Song, Guian Fang, Zijian He, Jie Yang, Mike Zheng Shou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.05918v1.pdf)  
  Keywords: autoregressive, autoregressive video, camera motion, character animation, cinematic, diffusion transformer, distillation, dynamics, efficient, film, long-form, video generation, video to video, video-to-video  
- **[TourPhysics: Bringing Physics to World Models for Exploration and Manipulation from a Single Image](https://arxiv.org/abs/2609.04911v2)**  
  Authors: Xin Zhang, Yabo Chen, Zixuan Duan, Haibin Huang, Chi Zhang, Feng Xu, Xuelong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.04911v2.pdf)  
  Keywords: camera motion, camera trajectory, interactive, physical, physics, simulation, trajectory, video generation, video synthesis  
- **[ReaDiT Guidance: Control for Image and Video Generation using Diffusion Transformer Features](https://arxiv.org/abs/2609.04649v1)**  
  Authors: Jay Mahajan, Chang Liu, Rauf Makharov, Viraj Shah, Alexander Schwing, Svetlana Lazebnik  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.04649v1.pdf)  
  Keywords: diffusion transformer, dit, motion control, text to video, text-to-video, video generation  
- **[One Editor, Many Edits: A Unified Training-Free Framework for Diverse Video Editing](https://arxiv.org/abs/2609.04190v1)**  
  Authors: Adheesh Sunil Juvekar, Onkar Kishor Susladkar, Kiet A. Nguyen, Muntasir Wahed, Nabeel Bashir, Xiaona Zhou, Tianjiao Yu, Vedant Shah, Ismini Lourentzou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.04190v1.pdf)  
  Keywords: identity, instruction-guided, reference-guided, style, video editing  
- **[BooM-VVT: Boosting Mask-Free Video Virtual Try-On with Image-Level Pseudo Data](https://arxiv.org/abs/2609.04120v1)**  
  Authors: Wei Zhang, Xin Li, Peishu Shi, Jialin Gao, Xuekang Peng, Zhichao Lian, Yeying Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.04120v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://boomvvt.github.io/boomvvt)  
  Keywords: keyframe, temporal consistency, video generation, virtual try-on  

### Human & Character Animation

*Showing the latest 50 out of 65 papers*

- **[PAI-Actor: Cinematic Multi-Character Replacement in Dynamic Scenes](https://arxiv.org/abs/2609.05918v1)**  
  Authors: Bangxun Tang, Heyuan Gao, Yiren Song, Guian Fang, Zijian He, Jie Yang, Mike Zheng Shou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.05918v1.pdf)  
  Keywords: autoregressive, autoregressive video, camera motion, character animation, cinematic, diffusion transformer, distillation, dynamics, efficient, film, long-form, video generation, video to video, video-to-video  
- **[BooM-VVT: Boosting Mask-Free Video Virtual Try-On with Image-Level Pseudo Data](https://arxiv.org/abs/2609.04120v1)**  
  Authors: Wei Zhang, Xin Li, Peishu Shi, Jialin Gao, Xuekang Peng, Zhichao Lian, Yeying Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.04120v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://boomvvt.github.io/boomvvt)  
  Keywords: keyframe, temporal consistency, video generation, virtual try-on  
- **[4DStreamCtrl: Interactive Video Generation with Online 4D Control](https://arxiv.org/abs/2608.25479v2)**  
  Authors: Shiqian Li, Chenguo Lin, Zhiguang Liu, Yu Tang, Jiarong Ou, Rui Chen, Yixin Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.25479v2.pdf)  
  Keywords: 3d consistent, camera motion, controllable, denoising, diffusion model, efficient, embodied, interactive, long video, motion control, motion transfer, streaming, trajectory, video diffusion, video generation  
- **[AvatarDynamizer: From Static to Dynamic Human Avatars via Generative Dynamic Textures](https://arxiv.org/abs/2608.19900v1)**  
  Authors: Guoxing Sun, Heming Zhu, Linjie Lyu, Pascal Fua, Christian Theobalt, Marc Habermann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.19900v1.pdf)  
  Keywords: avatar, controllable, dynamics, video diffusion, view-consistent  
- **[SingDance: Compositional Zero-Shot Singing-and-Dancing Video Generation with Role-Aware Audio Conditioning](https://arxiv.org/abs/2608.16220v1)**  
  Authors: Tao Feng, Xu Li, Xiangyang Luo, Ming Wen, Huadai Liu, Chen Zhang, Wei Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.16220v1.pdf)  
  Keywords: body motion, controllable, speech-driven, video diffusion, video generation  
- **[AnyTalk: Speech Animation for Arbitrary Characters Leveraging a Video Generation Model](https://arxiv.org/abs/2608.16143v1)**  
  Authors: Kwan Yun, Serin Yoon, Sunjin Jung, Jung Eun Yoo, Inyup Lee, Junyong Noh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.16143v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://serin-yoon.github.io/projects/anytalk)  
  Keywords: audio-driven, diffusion model, talking head, video diffusion, video generation  
- **[FlowDance: Music-Driven Dance Video Generation with Parallel Pose and RGB Streams](https://arxiv.org/abs/2608.15818v1)**  
  Authors: Genying Li, Boda Lin, Jiachen Li, Zijian Jia, Haojie Zheng, Yiming Wang, Shuchen Weng, Si Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.15818v1.pdf)  
  Keywords: body motion, denoising, human animation, identity, identity-preserving, long video, video generation, video synthesis  
- **[Avatar-Forever: Decoupled Parallel Training for High-Quality Real-Time Infinite Avatars](https://arxiv.org/abs/2608.12107v1)**  
  Authors: Ruibin Li, Tao Yang, Zhiyuan Ma, Fangzhou Ai, Shilei Wen, Lei Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.12107v1.pdf)  
  Keywords: audio-driven, audio-driven avatar, autoregressive, avatar, distillation, efficient, identity, interactive, long video, streaming, video foundation model, video generation  
- **[LiveAnimate: Stable Long-Form Streaming Human Animation in Real-Time](https://arxiv.org/abs/2608.11745v2)**  
  Authors: Yuxuan Zhang, Haozhong Xiong, Yubo Huang, Jiayi Song, Jinpeng Yu, Haofan Wang, Jiaming Liu, Ruihua Huang, Liwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.11745v2.pdf)  
  Keywords: autoregressive, benchmark, diffusion transformer, distillation, dit, driving, human animation, identity, interactive, long-form, streaming, video diffusion, video diffusion transformer  
- **[Omni-LiveAvatar: Minute-Level Real-Time Streaming Joint Audio-Video Avatar Generation](https://arxiv.org/abs/2608.13602v2)**  
  Authors: Lunjie Zhu, Xingtong Ge, Fangyu Lin, Yi Zhang, Zhening Liu, Mengfei Li, Yumeng Zhang, Guanglu Song, Yu Liu, Jun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.13602v2.pdf) | [![GitHub](https://img.shields.io/github/stars/Aoko955/Omni-LiveAvatar?style=social)](https://github.com/Aoko955/Omni-LiveAvatar)  
  Keywords: autoregressive, avatar, denoising, diffusion model, digital human, distillation, interactive, joint audio-video, streaming, video diffusion  

### Image-to-Video Generation

*Showing the latest 50 out of 95 papers*

- **[DF26: We Cannot Tell Fake From Real Anymore](https://arxiv.org/abs/2609.07369v1)**  
  Authors: Severyn Shykula, Andrii Yermakov, Ivan Samarskyi, Dmytro Mishkin, Jan Cech, Anastasiia Mishchuk  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.07369v1.pdf)  
  Keywords: benchmark, evaluation, image to video, image-to-video, text to video, text-to-video  
- **[PhysWeep: Does a Video Generator Realize the Physics You Ask For?](https://arxiv.org/abs/2609.06207v1)**  
  Authors: Rasul Khanbayov, Hasan Kurban  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.06207v1.pdf)  
  Keywords: benchmark, dynamics, image to video, image-to-video, physical, physics  
- **[EditaLive! Unified Character Video Editing for Live Streaming](https://arxiv.org/abs/2608.27123v1)**  
  Authors: Zhiyuan Li, Chi-Man Pun, Peng-Tao Jiang, Bo Li, Xiaodong Cun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.27123v1.pdf)  
  Keywords: distillation, image animation, sparse attention, streaming, video editing  
- **[TempJail: Temporal Jailbreak Attacks against Image-to-Video Generation Models](https://arxiv.org/abs/2608.26971v2)**  
  Authors: Qi Lu, Zehui Guo, David Yuanda Gan, Zijing Li, Hengda Zhang, Weijun Xu, Qiankun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.26971v2.pdf) | [![GitHub](https://img.shields.io/github/stars/luqi-glory/TempJail?style=social)](https://github.com/luqi-glory/TempJail)  
  Keywords: evaluation, human evaluation, i2v, image to video, image-to-video, video generation, video synthesis  
- **[Direct, Parallel, or Sequential? A Comparative Study of Training-Free Multi-Subject Image-to-Video Generation](https://arxiv.org/abs/2608.22819v1)**  
  Authors: Yanliang Qi, Kexi Chen, Muchao Ye, Haomiao Ni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.22819v1.pdf)  
  Keywords: controllable, i2v, image to video, image-to-video, temporal consistency, video generation  
- **[CaliBench: Are the Stochastic Dynamics of Video World Models Physically Calibrated?](https://arxiv.org/abs/2608.16829v2)**  
  Authors: Jonathan Sadeghi, Jenny Seidenschwarz, Jesse Allardice, Sirish Srinivasan, Benjamin Graham, Jeffrey Hawke  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.16829v2.pdf)  
  Keywords: dynamics, image to video, image-to-video, physical  
- **[EditStream: A Unified Autoregressive Framework for Interactive Video Generation and Editing](https://arxiv.org/abs/2608.21424v1)**  
  Authors: Yuqian Zhou, Zhenghong Zhou, Zongze Wu, Cameron Smith, Richard Zhang, Jiebo Luo, Eli Shechtman, Zhe Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.21424v1.pdf)  
  Keywords: autoregressive, autoregressive video, creative, distillation, dit, efficient, image to video, image-to-video, interactive, reference-guided, streaming, text to video, text-to-video, video editing, video generation, video to video, video-to-video  
- **[HPSD: Hybrid-Policy Self-Distillation for Text-Image-to-Video Diffusion Models](https://arxiv.org/abs/2608.13205v1)**  
  Authors: Jiazi Bu, Pengyang Ling, Yujie Zhou, Yibin Wang, Yuhang Zang, Xuanlang Dai, Shengyuan Ding, Tianyi Wei, Xiaohang Zhan, Jiaqi Wang, Tong Wu, Dahua Lin, Xingang Pan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.13205v1.pdf)  
  Keywords: architecture, distillation, i2v, image to video, image-to-video, t2v, text to video, text-to-video, trajectory, video diffusion  
- **[Beyond Trial-and-Error: Agentic Optimization for Image-to-Video Adherence](https://arxiv.org/abs/2608.12290v1)**  
  Authors: Aman Tyagi, Hemanth Boinpally, Jonathan Chen, Douglas Gebert, Steven Hickson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.12290v1.pdf)  
  Keywords: i2v, image to video, image-to-video, video generation, video synthesis  
- **[SparSTAR: Sparse Attention for SpaceTime AutoRegressive Video Synthesis](https://arxiv.org/abs/2608.10519v2)**  
  Authors: Jongbeom Lee, Hyunwoo Yu, Jincheol Yang, Jaemin Choi, Suk-Ju Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.10519v2.pdf)  
  Keywords: autoregressive, autoregressive video, image to video, image-to-video, sparse attention, text to video, text-to-video, video generation, video synthesis  

### Long Video Generation

*Showing the latest 50 out of 270 papers*

- **[Temporal State Transport in Video Generation: Diagnosing and Correcting Spectral Imbalance](https://arxiv.org/abs/2609.08505v1)**  
  Authors: Luyao Tang, Bingjun Luo, Dong Yi, Jialin Guo, Haoning Xi, Cheng Chen, Yizhou Yu, Chaoqi Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.08505v1.pdf) | [![GitHub](https://img.shields.io/github/stars/lytang63/temporal-state-transport?style=social)](https://github.com/lytang63/temporal-state-transport)  
  Keywords: identity, layout, temporal consistency, video generation  
- **[Better Call CineCrew: Consistent Ultra-Long Narrative-to-Film Generation](https://arxiv.org/abs/2609.07720v1)**  
  Authors: Jiaben Chen, Sixun Dong, Qinhong Zhou, Raine Ma, Zhiyang Dou, Wojciech Matusik, Chuang Gan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.07720v1.pdf)  
  Keywords: cinematic, film, film generation, identity, long-form, style, video generation  
- **[MVWeaver: A Hierarchical Music Video Generation Agent with a Learned Song-to-Visual Bridge](https://arxiv.org/abs/2609.06478v1)**  
  Authors: Sifei Li, Minyan Luo, Xu Li, Guodong Qi, Xincan Wang, Hanwen Wang, Chen Zhang, Pengfei Wan, Oliver Deussen, Weiming Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.06478v1.pdf)  
  Keywords: architecture, long-form, music video, video generation  
- **[Multi-Grid Post-Training for Long-Form Multi-Shot Video Generation](https://arxiv.org/abs/2609.06373v1)**  
  Authors: Jiawei Mao, Haoqin Tu, Hardy Chen, Yuhan Wang, Keyang Xu, Jieru Mei, Hongliang Fei, Ruogu Fang, Wei Shao, Cihang Xie, Yuyin Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.06373v1.pdf)  
  Keywords: benchmark, denoising, long video, long-form, video generation  
- **[TBDub: Production-Oriented Visual Dubbing](https://arxiv.org/abs/2609.06144v1)**  
  Authors: Bihan Li, Xinyang Li, Zeran Xu, Meiguang Jin, Junfeng Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.06144v1.pdf) | [![GitHub](https://img.shields.io/github/stars/TaoLiveAIGC/TBDub?style=social)](https://github.com/TaoLiveAIGC/TBDub) | [![Project](https://img.shields.io/badge/-Project-blue)](https://huggingface.co/TaoLiveAIGC/TBDub.) | [![HuggingFace](https://img.shields.io/badge/-HuggingFace-yellow)](https://huggingface.co/TaoLiveAIGC/TBDub)  
  Keywords: distillation, dit, evaluation, identity, temporal consistency, video dit, video editing  
- **[PAI-Actor: Cinematic Multi-Character Replacement in Dynamic Scenes](https://arxiv.org/abs/2609.05918v1)**  
  Authors: Bangxun Tang, Heyuan Gao, Yiren Song, Guian Fang, Zijian He, Jie Yang, Mike Zheng Shou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.05918v1.pdf)  
  Keywords: autoregressive, autoregressive video, camera motion, character animation, cinematic, diffusion transformer, distillation, dynamics, efficient, film, long-form, video generation, video to video, video-to-video  
- **[BooM-VVT: Boosting Mask-Free Video Virtual Try-On with Image-Level Pseudo Data](https://arxiv.org/abs/2609.04120v1)**  
  Authors: Wei Zhang, Xin Li, Peishu Shi, Jialin Gao, Xuekang Peng, Zhichao Lian, Yeying Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.04120v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://boomvvt.github.io/boomvvt)  
  Keywords: keyframe, temporal consistency, video generation, virtual try-on  
- **[OctWorld: Long-Range World-Consistent Video Generation with Octree-Based 3D Mapping](https://arxiv.org/abs/2609.03919v1)**  
  Authors: Zelong Lv, Sicheng Xu, Jianfeng Xiang, Ruicheng Wang, Yue Dong, Yu Deng, Guangzhong Sun, Jiaolong Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.03919v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://maxtirerror.github.io/octworldpage)  
  Keywords: autoregressive, video diffusion, video generation  
- **[Stabilizing Camera-Controlled Novel View Synthesis at Inference Time](https://arxiv.org/abs/2609.03639v1)**  
  Authors: Prajwal Singh, Arjun Badola, Seema Kumari, Hajime Nagahara, Shanmuganathan Raman  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.03639v1.pdf)  
  Keywords: autoregressive, camera motion, efficient, novel view, video diffusion  
- **[RoGe: Novel View Synthesis via End-to-End Implicit Reconstruction and Generation](https://arxiv.org/abs/2609.02847v2)**  
  Authors: Xiaolei Lang, Ze Kang, Zehao Huang, Naiyan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.02847v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jerry-locker.github.io/roge)  
  Keywords: camera trajectory, diffusion model, novel view, temporal consistency, trajectory, video diffusion  

### Personalization & Customization

*Showing the latest 50 out of 183 papers*

- **[Temporal State Transport in Video Generation: Diagnosing and Correcting Spectral Imbalance](https://arxiv.org/abs/2609.08505v1)**  
  Authors: Luyao Tang, Bingjun Luo, Dong Yi, Jialin Guo, Haoning Xi, Cheng Chen, Yizhou Yu, Chaoqi Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.08505v1.pdf) | [![GitHub](https://img.shields.io/github/stars/lytang63/temporal-state-transport?style=social)](https://github.com/lytang63/temporal-state-transport)  
  Keywords: identity, layout, temporal consistency, video generation  
- **[VI-Bench: Benchmarking Prompt Inversion from AIGC Videos](https://arxiv.org/abs/2609.08079v1)**  
  Authors: Wulin Xie, Rui Zhao, Kecen Li, Xiujin Liu, Bokang Zhang, Zheng Liu, Xinwen Hou, Chen Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.08079v1.pdf)  
  Keywords: benchmark, creative, style, video generation  
- **[Better Call CineCrew: Consistent Ultra-Long Narrative-to-Film Generation](https://arxiv.org/abs/2609.07720v1)**  
  Authors: Jiaben Chen, Sixun Dong, Qinhong Zhou, Raine Ma, Zhiyang Dou, Wojciech Matusik, Chuang Gan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.07720v1.pdf)  
  Keywords: cinematic, film, film generation, identity, long-form, style, video generation  
- **[Generalist Open-World Temporal Perception](https://arxiv.org/abs/2609.06823v1)**  
  Authors: Cristian Sminchisescu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.06823v1.pdf)  
  Keywords: architecture, controllable, identity, physical, simulation, world model  
- **[Adapting Vision Foundation Models to Acoustics for Pose-Free 3D Sonar Reconstruction](https://arxiv.org/abs/2609.06261v1)**  
  Authors: Kevin Zhang, Jingxi Chen, Mohamad Qadri, Russell Shomberg, Michael Kaess, Jia-Bin Huang, Adithya Pediredla, Christopher Metzler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.06261v1.pdf)  
  Keywords: few-shot, physics, text to video, text-to-video, video generation  
- **[TBDub: Production-Oriented Visual Dubbing](https://arxiv.org/abs/2609.06144v1)**  
  Authors: Bihan Li, Xinyang Li, Zeran Xu, Meiguang Jin, Junfeng Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.06144v1.pdf) | [![GitHub](https://img.shields.io/github/stars/TaoLiveAIGC/TBDub?style=social)](https://github.com/TaoLiveAIGC/TBDub) | [![Project](https://img.shields.io/badge/-Project-blue)](https://huggingface.co/TaoLiveAIGC/TBDub.) | [![HuggingFace](https://img.shields.io/badge/-HuggingFace-yellow)](https://huggingface.co/TaoLiveAIGC/TBDub)  
  Keywords: distillation, dit, evaluation, identity, temporal consistency, video dit, video editing  
- **[One Editor, Many Edits: A Unified Training-Free Framework for Diverse Video Editing](https://arxiv.org/abs/2609.04190v1)**  
  Authors: Adheesh Sunil Juvekar, Onkar Kishor Susladkar, Kiet A. Nguyen, Muntasir Wahed, Nabeel Bashir, Xiaona Zhou, Tianjiao Yu, Vedant Shah, Ismini Lourentzou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.04190v1.pdf)  
  Keywords: identity, instruction-guided, reference-guided, style, video editing  
- **[EraseSAE: Surgical Concept Erasure in Text-to-Video Diffusion Models via Sparse Autoencoders](https://arxiv.org/abs/2609.03629v2)**  
  Authors: Xinghao Wang, Dong Li, Wei Yu, Yingwei Pan, Tao Gong, Qi Chu, Nenghai Yu, Ting Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.03629v2.pdf) | [![GitHub](https://img.shields.io/github/stars/HiDream-ai/EraseSAE?style=social)](https://github.com/HiDream-ai/EraseSAE)  
  Keywords: concept, dit, t2v, text to video, text-to-video, video diffusion  
- **[Thinking in Pictures: A Systematic Benchmark for Reasoning-driven Image Generation](https://arxiv.org/abs/2609.02864v1)**  
  Authors: Yutong Liu, Nan Huang, Xu Cao, James M. Rehg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.02864v1.pdf)  
  Keywords: benchmark, concept, video generation  
- **[CameraEditor: Camera-Controlled Image Editing via Video-Prior Sequential Modeling](https://arxiv.org/abs/2609.01479v1)**  
  Authors: Xin Shen, Chengyou Jia, Keshuo Xing, Zifeng Zhu, Changliang Xia, Bowen Ping, Zhuohang Dang, Hangwei Qian, Minnan Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.01479v1.pdf)  
  Keywords: camera control, evaluation, identity, video diffusion  

### Physical Understanding

*Showing the latest 50 out of 310 papers*

- **[Kairos: A Dataset for Fine-Grained Video-Language Modeling over Space, Time, and Dynamics](https://arxiv.org/abs/2609.08755v1)**  
  Authors: Ruibo Ming, Lei Sun, Deheng Zhang, He Zhang, Jialu Li, Jian Wang, Zhendong Li, Mengshun Hu, Danda Pani Paudel, Luc Van Gool, Jinjin Gu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.08755v1.pdf)  
  Keywords: dynamics, evaluation, video generation  
- **[Beyond Coherence: Benchmarking Professional Editing-Technique Execution in Multi-Shot Audio-Video Generation](https://arxiv.org/abs/2609.08275v1)**  
  Authors: Tianyi Zeng, Junchao Liao, Yujie Wei, Ziying Zhang, Litao Li, Tianyi Wang, Zhichao Wei, Shuyao Xu, Wenwen Qiang, Siyu Zhu, Zhenghao Zhang, Long Qin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.08275v1.pdf) | [![GitHub](https://img.shields.io/github/stars/AlibabaResearch/cut-craft-bench?style=social)](https://github.com/AlibabaResearch/cut-craft-bench)  
  Keywords: audio-video generation, benchmark, cinematic, evaluation, physical, physical plausibility, video generation  
- **[PhysFlow: Physics-Aware Optical Flow for Motion Controllable Video Generation](https://arxiv.org/abs/2609.08215v1)**  
  Authors: Cong Wang, Hanxin Zhu, Yonglin Tian, Jiayi Luo, Ruiqi Song, Boyi Sun, Long Chen, Zhibo Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.08215v1.pdf)  
  Keywords: controllable, driving, dynamics, physical, physical plausibility, physics, physics-aware, video generation  
- **[Geodesic-informed Generative Diffusion Model For Topology-preserved Image Video Generation](https://arxiv.org/abs/2609.08153v1)**  
  Authors: Nian Wu, Nivetha Jayakumar, Jiarui Xing, Miaomiao Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.08153v1.pdf) | [![GitHub](https://img.shields.io/github/stars/nellie689/IGG?style=social)](https://github.com/nellie689/IGG)  
  Keywords: diffusion model, dynamics, robotics, video generation  
- **[Generalist Open-World Temporal Perception](https://arxiv.org/abs/2609.06823v1)**  
  Authors: Cristian Sminchisescu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.06823v1.pdf)  
  Keywords: architecture, controllable, identity, physical, simulation, world model  
- **[Adapting Vision Foundation Models to Acoustics for Pose-Free 3D Sonar Reconstruction](https://arxiv.org/abs/2609.06261v1)**  
  Authors: Kevin Zhang, Jingxi Chen, Mohamad Qadri, Russell Shomberg, Michael Kaess, Jia-Bin Huang, Adithya Pediredla, Christopher Metzler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.06261v1.pdf)  
  Keywords: few-shot, physics, text to video, text-to-video, video generation  
- **[PhysWeep: Does a Video Generator Realize the Physics You Ask For?](https://arxiv.org/abs/2609.06207v1)**  
  Authors: Rasul Khanbayov, Hasan Kurban  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.06207v1.pdf)  
  Keywords: benchmark, dynamics, image to video, image-to-video, physical, physics  
- **[PAI-Actor: Cinematic Multi-Character Replacement in Dynamic Scenes](https://arxiv.org/abs/2609.05918v1)**  
  Authors: Bangxun Tang, Heyuan Gao, Yiren Song, Guian Fang, Zijian He, Jie Yang, Mike Zheng Shou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.05918v1.pdf)  
  Keywords: autoregressive, autoregressive video, camera motion, character animation, cinematic, diffusion transformer, distillation, dynamics, efficient, film, long-form, video generation, video to video, video-to-video  
- **[TourPhysics: Bringing Physics to World Models for Exploration and Manipulation from a Single Image](https://arxiv.org/abs/2609.04911v2)**  
  Authors: Xin Zhang, Yabo Chen, Zixuan Duan, Haibin Huang, Chi Zhang, Feng Xu, Xuelong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.04911v2.pdf)  
  Keywords: camera motion, camera trajectory, interactive, physical, physics, simulation, trajectory, video generation, video synthesis  
- **[The Attention Triangle in Audio-Video Models](https://arxiv.org/abs/2609.03586v1)**  
  Authors: Sagi Polaczek, Noa Kraicer, Gal Metzer, Zhuo Ning, Ali Mahdavi-Amiri, Daniel Cohen-Or, Raja Giryes  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.03586v1.pdf)  
  Keywords: dynamics, sound, video diffusion, video generation  

### Surveys & Benchmarks

*Showing the latest 50 out of 313 papers*

- **[Kairos: A Dataset for Fine-Grained Video-Language Modeling over Space, Time, and Dynamics](https://arxiv.org/abs/2609.08755v1)**  
  Authors: Ruibo Ming, Lei Sun, Deheng Zhang, He Zhang, Jialu Li, Jian Wang, Zhendong Li, Mengshun Hu, Danda Pani Paudel, Luc Van Gool, Jinjin Gu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.08755v1.pdf)  
  Keywords: dynamics, evaluation, video generation  
- **[Beyond Coherence: Benchmarking Professional Editing-Technique Execution in Multi-Shot Audio-Video Generation](https://arxiv.org/abs/2609.08275v1)**  
  Authors: Tianyi Zeng, Junchao Liao, Yujie Wei, Ziying Zhang, Litao Li, Tianyi Wang, Zhichao Wei, Shuyao Xu, Wenwen Qiang, Siyu Zhu, Zhenghao Zhang, Long Qin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.08275v1.pdf) | [![GitHub](https://img.shields.io/github/stars/AlibabaResearch/cut-craft-bench?style=social)](https://github.com/AlibabaResearch/cut-craft-bench)  
  Keywords: audio-video generation, benchmark, cinematic, evaluation, physical, physical plausibility, video generation  
- **[VI-Bench: Benchmarking Prompt Inversion from AIGC Videos](https://arxiv.org/abs/2609.08079v1)**  
  Authors: Wulin Xie, Rui Zhao, Kecen Li, Xiujin Liu, Bokang Zhang, Zheng Liu, Xinwen Hou, Chen Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.08079v1.pdf)  
  Keywords: benchmark, creative, style, video generation  
- **[DF26: We Cannot Tell Fake From Real Anymore](https://arxiv.org/abs/2609.07369v1)**  
  Authors: Severyn Shykula, Andrii Yermakov, Ivan Samarskyi, Dmytro Mishkin, Jan Cech, Anastasiia Mishchuk  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.07369v1.pdf)  
  Keywords: benchmark, evaluation, image to video, image-to-video, text to video, text-to-video  
- **[The Price of Consistency: Exploiting Visual Anchors for Multimodal Jailbreaking in Video Generation](https://arxiv.org/abs/2609.07216v1)**  
  Authors: Peng Li, Qianqian Xu, Yangbangyan Jiang, Zhipeng Yu, Qingming Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.07216v1.pdf)  
  Keywords: benchmark, controllable, video generation  
- **[AV-SafetyBench: A Safety Benchmark for Text-to-Audio-Video Generation](https://arxiv.org/abs/2609.06991v1)**  
  Authors: Suah Choi, Tae-Young Lee, Gyeong-Moon Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.06991v1.pdf)  
  Keywords: audio-video generation, benchmark, evaluation, sound, video generation  
- **[Multi-Grid Post-Training for Long-Form Multi-Shot Video Generation](https://arxiv.org/abs/2609.06373v1)**  
  Authors: Jiawei Mao, Haoqin Tu, Hardy Chen, Yuhan Wang, Keyang Xu, Jieru Mei, Hongliang Fei, Ruogu Fang, Wei Shao, Cihang Xie, Yuyin Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.06373v1.pdf)  
  Keywords: benchmark, denoising, long video, long-form, video generation  
- **[PhysWeep: Does a Video Generator Realize the Physics You Ask For?](https://arxiv.org/abs/2609.06207v1)**  
  Authors: Rasul Khanbayov, Hasan Kurban  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.06207v1.pdf)  
  Keywords: benchmark, dynamics, image to video, image-to-video, physical, physics  
- **[TBDub: Production-Oriented Visual Dubbing](https://arxiv.org/abs/2609.06144v1)**  
  Authors: Bihan Li, Xinyang Li, Zeran Xu, Meiguang Jin, Junfeng Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.06144v1.pdf) | [![GitHub](https://img.shields.io/github/stars/TaoLiveAIGC/TBDub?style=social)](https://github.com/TaoLiveAIGC/TBDub) | [![Project](https://img.shields.io/badge/-Project-blue)](https://huggingface.co/TaoLiveAIGC/TBDub.) | [![HuggingFace](https://img.shields.io/badge/-HuggingFace-yellow)](https://huggingface.co/TaoLiveAIGC/TBDub)  
  Keywords: distillation, dit, evaluation, identity, temporal consistency, video dit, video editing  
- **[PRISM-Bench: An Audio-Centric Diagnostic Benchmark for Text-to-Audio-Video Generation](https://arxiv.org/abs/2609.04867v1)**  
  Authors: Yuchen Sun, Qian Yang, Jun Wang, Detai Xin, Guoqiao Yu, Guanglu Wan, Qi Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.04867v1.pdf)  
  Keywords: audio-video generation, benchmark, evaluation, sound, video generation  

### Text-to-Video Generation

*Showing the latest 50 out of 140 papers*

- **[DF26: We Cannot Tell Fake From Real Anymore](https://arxiv.org/abs/2609.07369v1)**  
  Authors: Severyn Shykula, Andrii Yermakov, Ivan Samarskyi, Dmytro Mishkin, Jan Cech, Anastasiia Mishchuk  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.07369v1.pdf)  
  Keywords: benchmark, evaluation, image to video, image-to-video, text to video, text-to-video  
- **[Adapting Vision Foundation Models to Acoustics for Pose-Free 3D Sonar Reconstruction](https://arxiv.org/abs/2609.06261v1)**  
  Authors: Kevin Zhang, Jingxi Chen, Mohamad Qadri, Russell Shomberg, Michael Kaess, Jia-Bin Huang, Adithya Pediredla, Christopher Metzler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.06261v1.pdf)  
  Keywords: few-shot, physics, text to video, text-to-video, video generation  
- **[ReaDiT Guidance: Control for Image and Video Generation using Diffusion Transformer Features](https://arxiv.org/abs/2609.04649v1)**  
  Authors: Jay Mahajan, Chang Liu, Rauf Makharov, Viraj Shah, Alexander Schwing, Svetlana Lazebnik  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.04649v1.pdf)  
  Keywords: diffusion transformer, dit, motion control, text to video, text-to-video, video generation  
- **[DSAQuant: Denoising-Stage-Aligned Quantization-Aware Training for Video Generation](https://arxiv.org/abs/2609.04031v1)**  
  Authors: Shuaiting Li, Zelin Gao, Haibin Shen, Yujun Shen, Haotong Qin, Yinghao Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.04031v1.pdf)  
  Keywords: denoising, distillation, layout, text to video, text-to-video, video denoising, video diffusion, video generation  
- **[EraseSAE: Surgical Concept Erasure in Text-to-Video Diffusion Models via Sparse Autoencoders](https://arxiv.org/abs/2609.03629v2)**  
  Authors: Xinghao Wang, Dong Li, Wei Yu, Yingwei Pan, Tao Gong, Qi Chu, Nenghai Yu, Ting Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.03629v2.pdf) | [![GitHub](https://img.shields.io/github/stars/HiDream-ai/EraseSAE?style=social)](https://github.com/HiDream-ai/EraseSAE)  
  Keywords: concept, dit, t2v, text to video, text-to-video, video diffusion  
- **[Step Back to Move Forward: Reflection-Aware Preference Optimization for Visual Generation](https://arxiv.org/abs/2609.04282v1)**  
  Authors: Junlong Wu, Jiuzhou Lin, Jia Sun, Boheng Zhang, Huaiqing Wang, Dewen Fan, Houde Liu, Qianqian Gan, Fan Yang, Tingting Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.04282v1.pdf)  
  Keywords: architecture, t2v, text to video, text-to-video  
- **[NoisEasier: Test-Time Noise Optimization for Text-to-Video Generation](https://arxiv.org/abs/2608.30194v1)**  
  Authors: Yujiang Pu, Yu Kong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.30194v1.pdf)  
  Keywords: controllable, efficient, t2v, text to video, text-to-video, trajectory, video generation  
- **[On the Resilience of Text-to-Video Diffusion Models to Hardware Faults](https://arxiv.org/abs/2608.29598v1)**  
  Authors: Zachary Coalson, A M Aahad, Stella Doehring, Zane Ma, Sanghyun Hong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.29598v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ztcoalson/T2V-Resilience?style=social)](https://github.com/ztcoalson/T2V-Resilience)  
  Keywords: benchmark, denoising, t2v, text to video, text-to-video, video diffusion, video generation  
- **[ClusterAttention: A training-free speedup of bidirectional attention](https://arxiv.org/abs/2608.26965v1)**  
  Authors: Kasper Nordenram, Amelie Dittmann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.26965v1.pdf)  
  Keywords: sparse attention, t2v, video generation  
- **[TurboT2VA: Fast Large-Scale Text-to-Video-Audio Generation via Score-Regularized Consistency Distillation](https://arxiv.org/abs/2608.24674v2)**  
  Authors: Xiaoda Yang, Yuxiang Liu, Kaiwen Zheng, Yuan Liu, Yibo Lai, Shengpeng Ji, Kai Jiang, Jianfei Chen, Shan Yang, Xiaobin Hu, Shuicheng Yan, Jintao Zhang, Jun Zhu, Zhou Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.24674v2.pdf) | [![GitHub](https://img.shields.io/github/stars/thu-ml/TurboDiffusion?style=social)](https://github.com/thu-ml/TurboDiffusion)  
  Keywords: architecture, consistency distillation, distillation, evaluation, sparse attention, text to video, text-to-video, trajectory  

### Video Editing

*Showing the latest 50 out of 102 papers*

- **[Agentic Visual Generation: From Generative Models to Agentic Control](https://arxiv.org/abs/2609.06758v1)**  
  Authors: Yinming Huang, Shuyuan Tu, Xi Yan, Jiahao Zhan, Zihan Yang, Zhen Xing, Hui Zhang, Tiehua Zhang, Yu-Gang Jiang, Zuxuan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.06758v1.pdf)  
  Keywords: video editing  
- **[TBDub: Production-Oriented Visual Dubbing](https://arxiv.org/abs/2609.06144v1)**  
  Authors: Bihan Li, Xinyang Li, Zeran Xu, Meiguang Jin, Junfeng Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.06144v1.pdf) | [![GitHub](https://img.shields.io/github/stars/TaoLiveAIGC/TBDub?style=social)](https://github.com/TaoLiveAIGC/TBDub) | [![Project](https://img.shields.io/badge/-Project-blue)](https://huggingface.co/TaoLiveAIGC/TBDub.) | [![HuggingFace](https://img.shields.io/badge/-HuggingFace-yellow)](https://huggingface.co/TaoLiveAIGC/TBDub)  
  Keywords: distillation, dit, evaluation, identity, temporal consistency, video dit, video editing  
- **[PAI-Actor: Cinematic Multi-Character Replacement in Dynamic Scenes](https://arxiv.org/abs/2609.05918v1)**  
  Authors: Bangxun Tang, Heyuan Gao, Yiren Song, Guian Fang, Zijian He, Jie Yang, Mike Zheng Shou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.05918v1.pdf)  
  Keywords: autoregressive, autoregressive video, camera motion, character animation, cinematic, diffusion transformer, distillation, dynamics, efficient, film, long-form, video generation, video to video, video-to-video  
- **[One Editor, Many Edits: A Unified Training-Free Framework for Diverse Video Editing](https://arxiv.org/abs/2609.04190v1)**  
  Authors: Adheesh Sunil Juvekar, Onkar Kishor Susladkar, Kiet A. Nguyen, Muntasir Wahed, Nabeel Bashir, Xiaona Zhou, Tianjiao Yu, Vedant Shah, Ismini Lourentzou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.04190v1.pdf)  
  Keywords: identity, instruction-guided, reference-guided, style, video editing  
- **[AVENUE: Audio-Video EditiNg Understanding and Evaluation](https://arxiv.org/abs/2609.04253v1)**  
  Authors: Hayeon Kim, Yoojin Jang, Jaejun Yoo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.04253v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://huggingface.co/datasets/AVENUE-dataset/AVENUE.) | [![Dataset](https://img.shields.io/badge/-Dataset-orange)](https://huggingface.co/datasets/AVENUE-dataset/AVENUE)  
  Keywords: benchmark, controllable, evaluation, video editing  
- **[EditaLive! Unified Character Video Editing for Live Streaming](https://arxiv.org/abs/2608.27123v1)**  
  Authors: Zhiyuan Li, Chi-Man Pun, Peng-Tao Jiang, Bo Li, Xiaodong Cun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.27123v1.pdf)  
  Keywords: distillation, image animation, sparse attention, streaming, video editing  
- **[Thinking on Shots: Consistent Multi-Shot Video Editing with Agentic Reasoning](https://arxiv.org/abs/2608.26809v1)**  
  Authors: Chenyang Wu, Fuchen Long, Binyuan Huang, Xinlong Sun, Xi Chen, Chun-Le Guo, Chongyi Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.26809v1.pdf)  
  Keywords: dynamics, evaluation, long video, video editing  
- **[RefVideo-6M: A Reliable Reference-Based Dataset for Instructional Video Editing](https://arxiv.org/abs/2608.26101v1)**  
  Authors: Bojia Zi, Xiaoyan Yang, Yu Zhou, Ruijie Sun, Lihan Zhang, Bin Liang, Kam-Fai Wong, Haibin Huang, Chi Zhang, Xuelong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.26101v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://huggingface.co/datasets/RefVideo6M/RefVideo6M.) | [![Dataset](https://img.shields.io/badge/-Dataset-orange)](https://huggingface.co/datasets/RefVideo6M/RefVideo6M)  
  Keywords: controllable, identity, identity-preserving, reference-guided, video editing  
- **[Plans You Can Check: Verifier-Grounded Learning of an Open-Weight Planner for Executable Video-Editing](https://arxiv.org/abs/2608.25622v1)**  
  Authors: Haoyu Wang, Cheng Feng, Liuyang Bian, Ruiyang Huang, Lei Wei, Yafei Wen, Xiaoxin Chen, Xiaoying Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.25622v1.pdf)  
  Keywords: distillation, video editing  
- **[Game2World Engine: Unlocking In-the-Wild Gameplay Videos for World Model Training](https://arxiv.org/abs/2608.24680v1)**  
  Authors: Wenxuan Shen, Dongna Jin, Dongping Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.24680v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Dongping-Chen/Game2World?style=social)](https://github.com/Dongping-Chen/Game2World)  
  Keywords: dynamics, evaluation, game, video editing, world model  

### Video Inpainting & Completion

- **[Stream4D: 4D-Consistency for Streaming Autoregressive Diffusion Video Models](https://arxiv.org/abs/2608.19556v1)**  
  Authors: Yuanhao Ban, Jiaqi Feng, Hengguang Zhou, Xiaohuan Pei, Justin Cui, Cho-Jui Hsieh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.19556v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://banyuanhao.github.io/Stream4D)  
  Keywords: autoregressive, autoregressive video, dynamics, frame prediction, streaming, video generation  
- **[V-RAE: Rethinking Video Latent Spaces for Generation](https://arxiv.org/abs/2608.13556v1)**  
  Authors: Minghui Guo, Shengqiong Wu, Hao Fei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.13556v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://v-rae.github.io)  
  Keywords: latent video, video autoencoder, video generation, video prediction, video tokenizer  
- **[GeoRoute: Geometry-Aware Hybrid Inference for Traffic Future-Frame Prediction](https://arxiv.org/abs/2608.09493v1)**  
  Authors: Khang Minh Le, Hieu Dinh Trung Pham, Luu Thanh Danh, Nam-Tien Le, Hieu Anh Ngo, Phuong Huu Vu Tran, Son Nguyen Minh Le, Nguyen Trong Nghia, Tu Tran Thi Cam, Huy Minh Nhat Nguyen, Cuong Tuan Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.09493v1.pdf)  
  Keywords: architecture, autonomous driving, benchmark, driving, frame prediction, future frame prediction, latent video, latent video diffusion, video diffusion  
- **[SimWAM: A Simple World Action Model for End-to-End Autonomous Driving](https://arxiv.org/abs/2608.07468v4)**  
  Authors: Zongchuang Zhao, Xin Zhou, Tianyang Xu, Zhengyang Sun, Kaixuan Zhou, Yu Wu, Honglin Li, Dingkang Liang, Xiang Bai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.07468v4.pdf) | [![GitHub](https://img.shields.io/github/stars/H-EmbodVis/SimWAM?style=social)](https://github.com/H-EmbodVis/SimWAM)  
  Keywords: autonomous driving, driving, dynamics, efficient, flow matching, trajectory, video generation, video prediction  
- **[MirrorWorld: Taming Video Diffusion Models for Mirror Reflection Generation](https://arxiv.org/abs/2608.07463v1)**  
  Authors: Youjun Zhao, Alex Warren, Gary K. L. Tam, Rynson W. H. Lau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.07463v1.pdf)  
  Keywords: benchmark, distillation, video diffusion, video inpainting, video synthesis  
- **[UniVVT: A Unified End-to-End Framework for High-Fidelity Video Virtual Try-on](https://arxiv.org/abs/2608.05745v2)**  
  Authors: Yushe Cao, Shikun Feng, Fei Shen, Haikuo Peng, Jianqiang Xia, Yiheng Zhu, Dianxi Shi, Chun Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05745v2.pdf)  
  Keywords: dynamics, identity, video generation, video inpainting, virtual try-on  
- **[CrossScope: A Role-Asymmetric World Model for Joint Dual-Scope Surgical Video Prediction](https://arxiv.org/abs/2608.03211v1)**  
  Authors: Wanhao Liu, Jinsong Lin, Rulin Zhou, Chi Kit Ng, Wenbin Pan, Zhiqing Tang, Dongyue Li, Liwei Luo, Yanshen Wu, Panshuo Li, Zhiyong Xiong, Huxin Gao, Tamas Haidegger, Hongliang Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.03211v1.pdf)  
  Keywords: benchmark, dynamics, video generation, video prediction, world model  
- **[CameraAnything: Refilming Videos with Arbitrary Camera Control](https://arxiv.org/abs/2607.24591v1)**  
  Authors: Yixuan Li, Yanhong Zeng, Ka Leong Cheng, Jiayi Zhu, Hanlin Wang, Wen Wang, Yihao Meng, Hao Ouyang, Qiuyu Wang, Yue Yu, ZiDong Wang, Yiyuan Zhang, Yujun Shen, Dahua Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.24591v1.pdf)  
  Keywords: camera control, cinematic, outpainting, video editing  
- **[The Seriality Gap in Video Diffusion Models](https://arxiv.org/abs/2607.13031v1)**  
  Authors: Jorge Diaz Chao, Konpat Preechakul, Yuxi Liu, Yutong Bai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.13031v1.pdf)  
  Keywords: autoregressive, denoising, dynamics, simulation, video diffusion, video prediction  
- **[Video Generation Models Are Inherent Lighting Estimators](https://arxiv.org/abs/2607.04674v1)**  
  Authors: Ziqi Cai, Shuchen Weng, Kaiqi Liu, Zifeng Wang, Zhiquan Zhang, Minggui Teng, Han Jiang, Boxin Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.04674v1.pdf)  
  Keywords: efficient, physical, video diffusion, video generation, video inpainting  

### Video Super-Resolution & Enhancement

*Showing the latest 50 out of 163 papers*

- **[Multi-Grid Post-Training for Long-Form Multi-Shot Video Generation](https://arxiv.org/abs/2609.06373v1)**  
  Authors: Jiawei Mao, Haoqin Tu, Hardy Chen, Yuhan Wang, Keyang Xu, Jieru Mei, Hongliang Fei, Ruogu Fang, Wei Shao, Cihang Xie, Yuyin Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.06373v1.pdf)  
  Keywords: benchmark, denoising, long video, long-form, video generation  
- **[DSAQuant: Denoising-Stage-Aligned Quantization-Aware Training for Video Generation](https://arxiv.org/abs/2609.04031v1)**  
  Authors: Shuaiting Li, Zelin Gao, Haibin Shen, Yujun Shen, Haotong Qin, Yinghao Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.04031v1.pdf)  
  Keywords: denoising, distillation, layout, text to video, text-to-video, video denoising, video diffusion, video generation  
- **[Physically Plausible Video Generation via Visual-Semantic Chain-of-Events Conditioning](https://arxiv.org/abs/2609.00656v1)**  
  Authors: Zixuan Wang, Yixin Hu, Wen Li, Feng Chen, Yan Liu, Duo Peng, Yinjie Lei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.00656v1.pdf)  
  Keywords: denoising, dynamics, keyframe, physical, physical plausibility, physics, physics-informed, video generation  
- **[DreamX-Creator: Democratizing Native Audio-Video Generation at 2K Resolution](https://arxiv.org/abs/2608.31106v1)**  
  Authors: Jiashu Zhu, Yanhao Zheng, Ruitian Tian, Rujing Dang, Shen Zhang, Bingze Song, Jiachen Lei, Ruimin Lin, Jiahong Wu, Xiangxiang Chu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.31106v1.pdf)  
  Keywords: audio-video generation, autoregressive, denoising, dynamics, evaluation, joint audio-video, video generation  
- **[On the Resilience of Text-to-Video Diffusion Models to Hardware Faults](https://arxiv.org/abs/2608.29598v1)**  
  Authors: Zachary Coalson, A M Aahad, Stella Doehring, Zane Ma, Sanghyun Hong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.29598v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ztcoalson/T2V-Resilience?style=social)](https://github.com/ztcoalson/T2V-Resilience)  
  Keywords: benchmark, denoising, t2v, text to video, text-to-video, video diffusion, video generation  
- **[Test-Time Scaling for Video Diffusion Models via Diagnosis-Guided Candidate Recycling](https://arxiv.org/abs/2608.29322v1)**  
  Authors: Hangzhou He, Lunhao Duan, Shanshan Zhao, Kaiwen Li, Qing-Guo Chen, Weihua Luo, Yanye Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.29322v1.pdf)  
  Keywords: denoising, evaluation, layout, video diffusion  
- **[Encore: Infinite Audio-Video Generation with Adaptive Signal Routing](https://arxiv.org/abs/2609.04249v1)**  
  Authors: Shaohua Pan, Junbao Chen, Shengyi He, Jingfeng Xue, Wen Tao, Haocheng Feng, Siming Fan, Dongwei Pan, Yi Yang, Wei He, Hang Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.04249v1.pdf) | [![GitHub](https://img.shields.io/github/stars/shaohua-pan/Encore?style=social)](https://github.com/shaohua-pan/Encore)  
  Keywords: audio-to-video, audio-video generation, denoising, evaluation, joint audio-video, long video, long-form, video generation, video-to-audio  
- **[4DStreamCtrl: Interactive Video Generation with Online 4D Control](https://arxiv.org/abs/2608.25479v2)**  
  Authors: Shiqian Li, Chenguo Lin, Zhiguang Liu, Yu Tang, Jiarong Ou, Rui Chen, Yixin Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.25479v2.pdf)  
  Keywords: 3d consistent, camera motion, controllable, denoising, diffusion model, efficient, embodied, interactive, long video, motion control, motion transfer, streaming, trajectory, video diffusion, video generation  
- **[Generalization, memorization, and overfitting for diffusion models trained in the lazy high-dimensional regime](https://arxiv.org/abs/2608.23938v1)**  
  Authors: Hugo Latourelle-Vigeant, Sinho Chewi, Aram-Alexandre Pooladian, John Sous, Theodor Misiakiewicz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.23938v1.pdf)  
  Keywords: denoising, video synthesis  
- **[Scaling Reinforcement Learning for Diffusion Models via Velocity Matching](https://arxiv.org/abs/2608.23664v1)**  
  Authors: Jaemoo Choi, Wei Guo, Yuchen Zhu, Arash Vahdat, Molei Tao, Julius Berner, Yongxin Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.23664v1.pdf)  
  Keywords: autoregressive, denoising, trajectory, video generation  

### World Models & Simulation

*Showing the latest 50 out of 257 papers*

- **[PRG-Fusion: Orchestrating Generative Priors with Reconstruction Evidence for Driving View Synthesis](https://arxiv.org/abs/2609.06948v1)**  
  Authors: Sipeng He, Jialei Chen, Zhen Fang, Dongchun Ren, Feng Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.06948v1.pdf)  
  Keywords: driving, simulation, trajectory, video synthesis  
- **[Generalist Open-World Temporal Perception](https://arxiv.org/abs/2609.06823v1)**  
  Authors: Cristian Sminchisescu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.06823v1.pdf)  
  Keywords: architecture, controllable, identity, physical, simulation, world model  
- **[TourPhysics: Bringing Physics to World Models for Exploration and Manipulation from a Single Image](https://arxiv.org/abs/2609.04911v2)**  
  Authors: Xin Zhang, Yabo Chen, Zixuan Duan, Haibin Huang, Chi Zhang, Feng Xu, Xuelong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.04911v2.pdf)  
  Keywords: camera motion, camera trajectory, interactive, physical, physics, simulation, trajectory, video generation, video synthesis  
- **[Building Pretraining Data for World Models: An Unreal Engine-Based Pipeline for Action-Conditioned Video Generation](https://arxiv.org/abs/2609.03557v1)**  
  Authors: Haoyu Wang, Songchun Zhang, Haoran Li, Haoyang Huang, Zeyue Xue, Nan Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.03557v1.pdf)  
  Keywords: action-conditioned, architecture, multi-view video, physics, trajectory, video generation, world model  
- **[Spatially Aware World Action Model via Geometric Latent Diffusion](https://arxiv.org/abs/2609.02531v1)**  
  Authors: Javier Alejandro Lopetegui Gonzalez, Paul Pacaud, Cordelia Schmid  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.02531v1.pdf)  
  Keywords: 3d-aware, evaluation, physical, video diffusion, world model  
- **[VirSqueezer: Generating Realistic Deformations and Squeezing Dynamics in VR from Fine-Grained Squeezing Controls](https://arxiv.org/abs/2609.01698v1)**  
  Authors: Qian Zhang, Xiaoming Chen, Xiaorui Ma, Haisheng Li, Weidong Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.01698v1.pdf)  
  Keywords: dynamics, evaluation, physical, simulation, video generation  
- **[Solaris: Towards Interfaces That Are Generated, Not Coded](https://arxiv.org/abs/2609.00776v1)**  
  Authors: Yuval Alaluf, Omri Avrahami, Guy Bukchin Leshem, Michal Geyer, Kfir Goldberg, Elad Richardson, Diego Alarcón, Alejandro Alvarez, Cole Garry, Anastasis Germanidis, Tenaya Goldsen, Corina Gurau, Robin Kahlow, Joel Kwartler, Kathleen Lewis, Alejandro Matamala Ortiz, Eugene McMahon, Thon Prom, Sarah Saltonstall-Wurm, Jamie Umpherson, Hudson Yeo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.00776v1.pdf)  
  Keywords: autoregressive, distillation, interactive, visual world model, world model  
- **[Streaming4D: Accelerate 4D World Models via Block-wise Video Generation and Incremental Reconstruction](https://arxiv.org/abs/2609.00610v1)**  
  Authors: Xiaoyan Liu, Jiaxin Liu, Kangrui Li, Sifan Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.00610v1.pdf)  
  Keywords: 4d generation, autoregressive, autoregressive video, interactive, style, video generation  
- **[CAER: Causal Action Effect Reweighting for World Model Training](https://arxiv.org/abs/2608.30897v1)**  
  Authors: Jianjie Fang, Xvyuan Liu, Ziyou Wang, Rongze Tang, Zhaolu Wang, Zhuohang Li, Xin Zhang, Haisheng Su, Chen Gao, Wei Wu, Xinlei Chen, Yong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.30897v1.pdf)  
  Keywords: action-conditioned, controllable, dynamics, embodied, physical, physical consistency, video generation, world model  
- **[Matrix-Game 3.5: Enhancing Real-Time Streaming Interactive World Models with Patch Memory](https://arxiv.org/abs/2608.29910v1)**  
  Authors: Runjia Qian, Zile Wang, Jihai Zhang, Kai Zou, Wei Yu, Jiaxing Li, Zexiang Liu, Yaokun Li, Fei Kang, Kaichen Huang, Mengyin An, Haobo Zhang, Biao Jiang, Jiahua Wang, Haofeng Sun, Yang Liu, Yangguang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.29910v1.pdf)  
  Keywords: autoregressive, camera control, diffusion model, distillation, embodied, flow matching, game, identity, interactive, minute-long, robotics, simulation, streaming, video generation  



## Classic Papers
- **[Video Diffusion Models](https://arxiv.org/abs/2204.03458)** (NeurIPS 2022)  
  Authors: Jonathan Ho, Tim Salimans, Alexey Gritsenko, William Chan, Mohammad Norouzi, David J. Fleet  
  Keywords: Video Diffusion, Generative Model, Unconditional Video Generation

- **[Align your Latents: High-Resolution Video Synthesis with Latent Diffusion Models](https://arxiv.org/abs/2304.08818)** (CVPR 2023)  
  Authors: Andreas Blattmann, Robin Rombach, Huan Ling, Tim Dockhorn, Seung Wook Kim, Sanja Fidler, Karsten Kreis  
  Keywords: Latent Video Diffusion, Text-to-Video, High-Resolution

- **[Stable Video Diffusion: Scaling Latent Video Diffusion Models to Large Datasets](https://arxiv.org/abs/2311.15127)** (2023)  
  Authors: Andreas Blattmann, Tim Dockhorn, Sumith Kulal, Daniel Menber, Maciej Kilian, Dominik Lorenz, et al.  
  Code: 🔗 [GitHub](https://github.com/Stability-AI/generative-models)  
  Keywords: Image-to-Video, Latent Video Diffusion, Large-Scale Training

- **[Sora: Video Generation Models as World Simulators](https://openai.com/research/video-generation-models-as-world-simulators)** (OpenAI, 2024)  
  Authors: OpenAI  
  Keywords: Text-to-Video, World Simulator, Diffusion Transformer, Long Video

- **[CogVideoX: Text-to-Video Diffusion Models with An Expert Transformer](https://arxiv.org/abs/2408.06072)** (2024)  
  Authors: Zhuoyi Yang, Jiayan Teng, Wendi Zheng, Ming Ding, Shiyu Huang, et al.  
  Code: 🔗 [GitHub](https://github.com/THUDM/CogVideo)  
  Keywords: Text-to-Video, Diffusion Transformer, Expert Transformer

## Open Source Projects
- [CogVideo](https://github.com/THUDM/CogVideo) - Text-to-video generation with CogVideoX series models (Tsinghua & Zhipu AI)
- [Open-Sora](https://github.com/hpcaitech/Open-Sora) - Open-source Sora-like video generation framework
- [Open-Sora-Plan](https://github.com/PKU-YuanGroup/Open-Sora-Plan) - Reproducing Sora with an open-source plan
- [HunyuanVideo](https://github.com/Tencent/HunyuanVideo) - Tencent's large-scale video generation model
- [Wan2.1](https://github.com/Wan-Video/Wan2.1) - Alibaba's open-source video generation model
- [AnimateDiff](https://github.com/guoyww/AnimateDiff) - Animate personalized text-to-image models without specific tuning
- [Stable Video Diffusion](https://github.com/Stability-AI/generative-models) - Stability AI's video generation models
- [ModelScope Text-to-Video](https://github.com/modelscope/modelscope) - ModelScope text-to-video synthesis

## Tutorials & Blogs
- [Video Generation Models as World Simulators](https://openai.com/research/video-generation-models-as-world-simulators) - OpenAI's Sora technical report
- [A Survey on Video Diffusion Models](https://arxiv.org/abs/2310.10647) - Comprehensive survey on video diffusion
- [Diffusion Models: A Comprehensive Survey](https://arxiv.org/abs/2209.00796) - Foundation knowledge on diffusion models

## 📋 Project Features

### 🛠️ Core Features
- **Unified CLI** (`main.py`): Single entry point with `init`, `search`, `suggest`, `export-bib`, `readme` subcommands
- **Interactive Config Wizard**: Guided setup for keywords, domains, time range, and API keys via `python main.py init`
- **Custom Search Keywords**: Configure keywords for title, abstract, or both; with arXiv domain filtering (`cs.CV`, `cs.AI`, `cs.MM`, etc.)
- **Time Range Filtering**: Relative periods (`30d`, `6m`, `1y`, `2y`) or absolute date ranges (`YYYY-MM-DD` to `YYYY-MM-DD`)
- **Smart Link Extraction**: Auto-classifies URLs from abstracts into GitHub, project page, dataset, video, demo, HuggingFace links
- **BibTeX Export**: Fetch BibTeX from arXiv official API; export to `.bib` files with category and date filters
- **LLM Keyword Suggestion**: Input paper titles or arXiv IDs to auto-generate optimized search keywords via OpenAI-compatible API
- **Automated Paper Collection**: Daily automatic crawling with GitHub Actions
- **Intelligent Classification**: Auto-categorize papers into 16 topics (T2V, I2V, Video Editing, Controllable Generation, World Models, etc.)

### 🛠️ Technical Features
- **Robust Error Handling**: Multi-layer retry and fallback strategies ensure stable operation
- **GitHub Actions Integration**: Automated CI/CD workflows for daily updates
- **Multi-type Link Badges**: README entries display PDF, GitHub (with stars), Project, Dataset, Video, Demo, HuggingFace, and Citation badges
- **Detailed Logging**: Comprehensive logging for debugging and monitoring
- **Cross-Platform**: Support for Windows/Linux/macOS

### 📚 Data Output
- **Paper JSON files** (`data/papers_YYYY-MM-DD.json`): Full paper metadata with title, authors, abstract, links, keywords, BibTeX
- **BibTeX files** (`output/*.bib`): Ready-to-use bibliography files for LaTeX
- **Auto-generated README**: Categorized and formatted paper listings

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Interactive Setup (Recommended)

```bash
python main.py init
```

This wizard walks you through:
- Setting search keywords (for title, abstract, or both)
- Selecting arXiv domains (e.g., `cs.CV`, `cs.AI`, `cs.MM`)
- Configuring time range (relative like `6m`/`1y`, or absolute dates)
- Setting max results
- Optionally configuring an OpenAI-compatible API key for keyword suggestion

### 3. Search Papers

```bash
# Search with settings from user_config.json
python main.py search

# Override: fetch 200 papers from the last 6 months, include BibTeX
python main.py search --max-results 200 --recent 6m --bibtex

# Search with absolute date range
python main.py search --date-from 2024-01-01 --date-to 2025-01-01

# Include citation counts from Semantic Scholar
python main.py search --citations
```

### 4. Export BibTeX

```bash
# Export all papers from the latest data file
python main.py export-bib --output output/references.bib

# Export only "Text-to-Video Generation" papers
python main.py export-bib --category "Text-to-Video Generation" --output output/t2v.bib

# Export papers from a specific date range
python main.py export-bib --date-from 2024-06-01 --date-to 2025-01-01 --output output/recent.bib
```

### 5. LLM Keyword Suggestion

```bash
# Generate keywords from paper titles
python main.py suggest --titles "Video Diffusion Models" "Stable Video Diffusion"

# Generate from arXiv IDs (auto-fetches titles)
python main.py suggest --arxiv-ids 2204.03458 2311.15127

# Auto-write suggested keywords to config
python main.py suggest --titles "Sora" "CogVideoX" --apply

# Use a custom API endpoint (e.g., DeepSeek)
python main.py suggest --titles "Paper Title" --base-url https://api.deepseek.com/v1 --api-key sk-xxx --model deepseek-chat
```

### 6. Generate README

```bash
# Basic README
python main.py readme

# Include latest papers section and abstracts
python main.py readme --show-latest --show-abstracts
```

### Configuration File

All settings are stored in `data/user_config.json`:

```json
{
  "search": {
    "keywords": {
      "both_abstract_and_title": ["video diffusion", "video generation", "text-to-video", "video-to-video"],
      "abstract_only": ["diffusion-based video generation", "flow-based video generation"],
      "title_only": ["world foundation model", "world simulator", "video tokenizer"]
    },
    "domains": ["cs.CV", "cs.AI", "cs.MM", "cs.LG", "cs.RO", "cs.GR", "eess.IV"],
    "time_range": {
      "mode": "relative",
      "relative": "1y"
    },
    "max_results": 1000
  },
  "api_keys": {
    "openai_api_key": "",
    "openai_base_url": "https://api.openai.com/v1",
    "openai_model": "gpt-4o-mini"
  }
}
```

## Contribution Guidelines
Feel free to submit Pull Requests to improve this list! Please follow these formats:
- Paper entry format: `**[Paper Title](link)** - Brief description`
- Project entry format: `[Project Name](link) - Project description`

## License
[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/) 
