# Awesome Video Diffusions [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Video Diffusion Models and Video Generation. Content is automatically updated daily.

🗺️ **[Explore the Paper Atlas](https://longxiang-ai.github.io/awesome-video-diffusions/)**: an interactive paper map, monthly trends, topic network, co-author network and author rankings of every tracked paper.

> Last Update: 2026-10-18 03:17:50

## 📰 Latest Updates

🗺️ **[2026-09-30] Paper Atlas on GitHub Pages**
- New [interactive site](https://longxiang-ai.github.io/awesome-video-diffusions/) built from all daily snapshots, rebuilt after every update

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

- [3D-aware Video Generation](#3d-aware-video-generation) (49 papers) - Video generation with 3D awareness, multi-view consistency, and 4D content creation
- [Applications](#applications) (203 papers) - Domain-specific applications of video diffusion models
- [Architecture & Efficiency](#architecture-&-efficiency) (392 papers) - Architectural innovations (DiT, UNet), flow matching, and training/inference efficiency
- [Audio & Multi-modal](#audio-&-multi-modal) (68 papers) - Audio-driven and multi-modal conditioned video generation
- [Controllable Generation](#controllable-generation) (322 papers) - Controllable video generation with motion, camera, pose, or layout guidance
- [Human & Character Animation](#human-&-character-animation) (53 papers) - Human-centric video generation including talking heads, dance, and character animation
- [Image-to-Video Generation](#image-to-video-generation) (94 papers) - Methods for animating still images into videos
- [Long Video Generation](#long-video-generation) (247 papers) - Generating temporally consistent long-form videos beyond short clips
- [Personalization & Customization](#personalization-&-customization) (154 papers) - Personalized video generation with custom subjects, identities, or styles
- [Physical Understanding](#physical-understanding) (302 papers) - Physics-aware video generation and dynamics modeling
- [Surveys & Benchmarks](#surveys-&-benchmarks) (322 papers) - Survey papers, benchmarks, and evaluation metrics for video generation
- [Text-to-Video Generation](#text-to-video-generation) (144 papers) - Foundation models and methods for generating videos from text prompts
- [Video Editing](#video-editing) (89 papers) - Diffusion-based video editing, style transfer, and manipulation
- [Video Inpainting & Completion](#video-inpainting-&-completion) (21 papers) - Video inpainting, completion, outpainting, and temporal prediction
- [Video Super-Resolution & Enhancement](#video-super-resolution-&-enhancement) (172 papers) - Video quality improvement, upscaling, restoration, and frame interpolation
- [World Models & Simulation](#world-models-&-simulation) (247 papers) - Video generation as world simulators and interactive environment generation



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3D-aware Video Generation

- **[CoWorld Reasoner: Agentic Multimodal Reasoning with the Evolving Video World Model-Driven Harness](https://arxiv.org/abs/2610.21910v1)**  
  Authors: Dongjie Cheng, Ruifeng Yuan, Ran Wei, Ning Song, Yongqi Li, Wenjie Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.21910v1.pdf)  
  Keywords: novel view, video world model, world model  
- **[4LC: 4D Latent Cache for Efficient Conditioning in Dynamic World Modeling](https://arxiv.org/abs/2610.17625v1)**  
  Authors: Jianhui Zhang, Zuyao Lin, Pengxin Xu, Jingdong Wang, Xingyu Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.17625v1.pdf)  
  Keywords: camera control, efficient, novel view, video generation  
- **[CineRecon: Benchmarking Frontier Models for Agentic Cinematic Reconstruction](https://arxiv.org/abs/2610.16577v1)**  
  Authors: Jialei Wang, Zehan Wang, XiaoYang Wu, Ziang Zhang, Siyu Chen, Jiaer Huang, Yujia Zhang, Tianyu Pang, Hengshuang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.16577v1.pdf)  
  Keywords: benchmark, cinematic, controllable, dynamic 3d, dynamics, evaluation, film, layout, video generation  
- **[VGGA: Geometry-Grounded Autoencoder for Video Generation](https://arxiv.org/abs/2610.16204v1)**  
  Authors: Chaofan Gan, Yian Zhao, Shijie Li, Tieyuan Chen, Zicheng Zhao, Mehrtash Harandi, Weiyao Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.16204v1.pdf)  
  Keywords: dynamic 3d, human motion, latent video, video autoencoder, video generation  
- **[Demiurge: Forging Navigable 4D Worlds via Autoregressive Video Rerendering](https://arxiv.org/abs/2610.14685v1)**  
  Authors: Hanxin Zhu, Jianqi Ma, Cong Wang, Zhihao Hu, Junyao Gao, Tianyu He, Junyan Lin, Jiayin Xiao, Jiateng Shou, Sen Liang, Weidong Zhang, Zhibo Chen, Jun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.14685v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hanxinzhu-lab.github.io/demiurge_project_page)  
  Keywords: autoregressive, autoregressive video, diffusion model, embodied, novel view, simulation, trajectory, video diffusion, video synthesis  
- **[GeoFix: Geometry Fixing for 4D Consistent Generation](https://arxiv.org/abs/2610.14293v1)**  
  Authors: Yeobin Hong, Hyojun Go, Dohun Lee, Jeongjae Lee, Sunghwan Hong, Federico Tombari, Zhaochong An, Jong Chul Ye, Konrad Schindler, Dominik Narnhofer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.14293v1.pdf)  
  Keywords: 4d generation, video diffusion  
- **[LEGO: A Lifting-Free Approach for Exocentric-to-Egocentric Video Generation](https://arxiv.org/abs/2610.12442v1)**  
  Authors: Suhwan Cho, Yonwoo Choi, Soongjin Kim, Jicheol Park, Taegyu Lim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.12442v1.pdf)  
  Keywords: denoising, diffusion model, layout, novel view, style, video diffusion, video generation  
- **[SymRegFlow: Symmetry-Regularized Flow Matching for Video World Models](https://arxiv.org/abs/2610.02726v1)**  
  Authors: Xi Ye, Yuzhu Wang, Xiaoyang Liu, Jiayi Wang, Yangyang Xu, Ruyu Wang, Wenlin Chen, Duo Su, Jun Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.02726v1.pdf)  
  Keywords: autonomous driving, denoising, driving, flow matching, novel view, video generation, view-consistent  
- **[4Director: Controlling Video World Models with Rigid 3D Geometry](https://arxiv.org/abs/2610.02160v1)**  
  Authors: Wei Cao, Hao Zhang, Vikram Voleti, Yuqun Wu, Mallikarjun B R, Shimon Vainer, Mark Boss, Yaoyao Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.02160v1.pdf)  
  Keywords: dynamics, identity, video world model, view-consistent, world model  
- **[PartiCam: Camera Controlled Video Generation with Reward Guidance](https://arxiv.org/abs/2609.39504v1)**  
  Authors: Amine Ouasfi, Runjia Li, Junlin Han, Eric Marchand, Philip H. S. Torr, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.39504v1.pdf)  
  Keywords: camera control, camera motion, camera trajectory, camera-conditioned, trajectory, video diffusion, video generation  

### Applications

*Showing the latest 50 out of 203 papers*

- **[RIGen: Beyond Action Following with Reciprocal Interaction in Generative Gameplay](https://arxiv.org/abs/2610.20811v1)**  
  Authors: Mengfei Li, Yi Zhang, Xingtong Ge, Lunjie Zhu, Fangyu Lin, Peng Li, Guanglu Song, Yu Liu, Wei Xue, Wenhan Luo, Yike Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.20811v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://murphylmf.github.io/RIGen)  
  Keywords: action-conditioned, dynamics, game, interactive, video generation  
- **[Any Time, Any Space: A World-State-Centric Framework for Agentic Video Generation](https://arxiv.org/abs/2610.20571v1)**  
  Authors: Weijie Wang, Haomin Zhang, Ye Li, Akide Liu, Zeyu Zhang, Haoyu Zhao, Yefei He, Donny Y. Chen, Feng Chen, Bohan Zhuang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.20571v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lhmd.top/atas)  
  Keywords: benchmark, film, long-form, video generation  
- **[FPV-CRASH: A Dataset for Offline Crash Moment Localization in Drone First-Person-View Videos](https://arxiv.org/abs/2610.19785v1)**  
  Authors: Jifan Zhang, Tingyu Wang, Qian Liu, Zhedong Zheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.19785v1.pdf)  
  Keywords: evaluation, physical, robotics, text to video, text-to-video  
- **[GreenWAM: A World Foundation Model for Robotics](https://arxiv.org/abs/2610.18774v1)**  
  Authors: Gennady Sidorov, Valerii Kornilov, Denis Grankin, Polina Fedotova, Aleksey Postnikov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.18774v1.pdf)  
  Keywords: action-conditioned, leaderboard, robotics, trajectory, world foundation model, world model  
- **[Data-Free Continual Learning for World Action Model with Rectified Generative Replay](https://arxiv.org/abs/2610.18038v2)**  
  Authors: Kaipeng Fang, Hangxu Liu, Chaojian Shi, Yunsong Zhou, Hongzi Zhu, Minyi Guo, Jingkuan Song, Lianli Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.18038v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kaipengfang.github.io/r2-wam)  
  Keywords: dynamics, robotics, video generation  
- **[Hierarchical Curriculum Learning for Surgical Video Generation: Focusing on Bilateral Axillo-Breast Approach Robotic Thyroidectomy Datasets](https://arxiv.org/abs/2610.17684v1)**  
  Authors: Youngbin Kong, Seungho Lee, Jae Kyung Shin, Jong-hyuk Ahn, Hyoun-Joong Kong, Kyu Eun Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.17684v1.pdf)  
  Keywords: benchmark, diffusion model, education, simulation, text to video, text-to-video, video diffusion, video generation  
- **[From Pixels to Executable Physics: Behavior-Grounded World Models for Embodied Action Consequence Prediction](https://arxiv.org/abs/2610.17630v1)**  
  Authors: Ruo Chen, Jiahua Pang, Yingjie Niu, Hongyi Lin, Jun Tian, Yang Zhu, Chao Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.17630v1.pdf)  
  Keywords: dynamics, embodied, evaluation, physical, physics, simulation, video world model, world model  
- **[CineRecon: Benchmarking Frontier Models for Agentic Cinematic Reconstruction](https://arxiv.org/abs/2610.16577v1)**  
  Authors: Jialei Wang, Zehan Wang, XiaoYang Wu, Ziang Zhang, Siyu Chen, Jiaer Huang, Yujia Zhang, Tianyu Pang, Hengshuang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.16577v1.pdf)  
  Keywords: benchmark, cinematic, controllable, dynamic 3d, dynamics, evaluation, film, layout, video generation  
- **[RAP-WAM: Learning World-Action Models through Predictive Rehearsal and Action Perturbations](https://arxiv.org/abs/2610.16443v2)**  
  Authors: Yuanpeng He, Ceyao Zhang, Fangjing Li, Kefei Zhu, Lijian Li, Yueheng Li, Tianjia He, Wenpin Jiao, Zhi Jin, Yaodong Yang, Yuanpei Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.16443v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rapwam.github.io)  
  Keywords: embodied, simulation, video generation  
- **[PINT: A Unified Model with Shared Predictive Intent for Robot Manipulation](https://arxiv.org/abs/2610.16355v1)**  
  Authors: Xinyu Guo, Chao Jing, Li Yi, Xingyu Chen, Zhengxing Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.16355v1.pdf)  
  Keywords: dynamics, embodied, video generation, video prediction  

### Architecture & Efficiency

*Showing the latest 50 out of 392 papers*

- **[Perceive, Predict, and Plan: a Unified World Action Model for Egocentric Dexterous Manipulation](https://arxiv.org/abs/2610.22363v1)**  
  Authors: Zirui Wu, Chen Guo, Tianjian Jiang, Zeren Jiang, Zeming Li, Lingchen Yang, Longteng Duan, Ying Xue, Handi Yin, Shenyuan Gao, Martin R. Oswald, Jun Zhang, Ping Tan, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.22363v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://p3-wam.pages.dev)  
  Keywords: action-conditioned, architecture, diffusion transformer, evaluation, video diffusion, video diffusion transformer, video generation, video prediction  
- **[Speculative Forcing for Efficient Autoregressive Video Generation](https://arxiv.org/abs/2610.22347v1)**  
  Authors: Hyunwook Choi, Seungryong Kim, Dongyoon Han, Sangdoo Yun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.22347v1.pdf)  
  Keywords: autoregressive, autoregressive video, camera motion, denoising, efficient, long video, streaming, video generation  
- **[Velox: Spatial Memory Makes World Models Efficient](https://arxiv.org/abs/2610.22311v1)**  
  Authors: Qiuhong Shen, Shizun Wang, Xinchao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.22311v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://velox-world.com/velox)  
  Keywords: camera motion, denoising, efficient, interactive, simulation, streaming, style, video diffusion  
- **[Sparse Attention for Video Generation Acceleration via Growing Sparsity and Reduced Search](https://arxiv.org/abs/2610.21129v1)**  
  Authors: Yun Dai, Yuyun Chen, Jiarui Wen, Huiping Zhuang, Cen Chen, Ziqian Zeng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.21129v1.pdf)  
  Keywords: acceleration, denoising, dynamics, evaluation, sparse attention, video generation  
- **[Temporal Specification Guidance for Text-to-Video Generation](https://arxiv.org/abs/2610.20822v1)**  
  Authors: Avishree Khare, Hideki Okamoto, Bardh Hoxha, Georgios Fainekos, Rajeev Alur  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.20822v1.pdf)  
  Keywords: benchmark, concept, denoising, efficient, text to video, text-to-video, video generation  
- **[Glance Forcing: Making Bidirectional Diffusion Autoregressive at a Glance](https://arxiv.org/abs/2610.20220v1)**  
  Authors: Zhuobai Dong, Junchao Yi, Hu Jian Guo, Linjie Li, Rui Zhao, Alex Jinpeng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.20220v1.pdf)  
  Keywords: autoregressive, denoising, diffusion model, distillation, efficient, layout, trajectory, video synthesis  
- **[StreamErase: Towards Ultra-Fast Streaming Video Erasing](https://arxiv.org/abs/2610.20137v1)**  
  Authors: Zhuobai Dong, Xiaobing Tu, Xiantao Zhang, Jinkui Ren, Yinggui Wang, Yue Ma, Linfeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.20137v1.pdf)  
  Keywords: benchmark, efficient, fast inference, interactive, long video, streaming, text to video, text-to-video  
- **[RepForcing: Representation-Space Initialization for Autoregressive Video Distillation](https://arxiv.org/abs/2610.20111v1)**  
  Authors: Siming Fu, Zheming Fu, Lianrui Mu, Haoyang Huang, Chaojie Gu, Ruizhe He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.20111v1.pdf)  
  Keywords: autoregressive, autoregressive video, diffusion transformer, distillation, trajectory, video diffusion, video diffusion transformer  
- **[StateCraft: Augmenting Video World Models with Abstract-State Reasoning](https://arxiv.org/abs/2610.19795v1)**  
  Authors: Lorenzo Venturoli, Nedko Savov, Xi Wang, Marc Pollefeys, Luc Van Gool  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.19795v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://insait-institute.github.io/StateCraft)  
  Keywords: architecture, benchmark, concept, diffusion model, dynamics, evaluation, video diffusion  
- **[SonoWorld: Towards Interactive Pose-Controllable Ultrasound World Models](https://arxiv.org/abs/2610.19327v1)**  
  Authors: Zefan Yang, Zheyuan Zhang, Boris Maihe, Yikang Liu, Hang Yu, Ankush Mukherjee, Xiao Chen, Pingkun Yan, Terrence Chen, Shanhui Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.19327v1.pdf)  
  Keywords: action-conditioned, autoregressive, controllable, diffusion model, distillation, dynamics, evaluation, interactive, simulation, video diffusion, world model  

### Audio & Multi-modal

*Showing the latest 50 out of 68 papers*

- **[AVC-Reward: Event-Centric Audio-Video Consistency Evaluation](https://arxiv.org/abs/2610.22321v1)**  
  Authors: Yuruo Wu, Kaihang Pan, Kai Shen, Jiacheng Li, Shuyuan Tu, Jisheng Dang, Li Tuoyu, Juncheng Li, Siliang Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.22321v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://tsuki0512.github.io/AVC-Reward.github.io)  
  Keywords: audio-video generation, benchmark, evaluation, joint audio-video, video generation  
- **[Kandinsky S2V 1.0: Audio-Driven Avatar Video Generation](https://arxiv.org/abs/2610.19290v1)**  
  Authors: Nikolay Semenov, Artem Riabinin, Sergey Bassenko, Anna Averchenkova, Julia Agafonova, Anastasia Aliaskina, Kirill Kozlov, Lev Novitskiy, Nikita Samsonov, Nikolai Gerasimenko, Denis Dimitrov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.19290v1.pdf)  
  Keywords: architecture, audio-driven, audio-driven avatar, avatar, benchmark, controllable, evaluation, gesture, human animation, human evaluation, long-form, speech-to-video, video generation  
- **[Simplifying and Improving On-Policy Distillation for Few-Step Diffusion](https://arxiv.org/abs/2610.18472v1)**  
  Authors: Jiawei Zhang, Ziyu Wan, Nanye Ma, Long Zhao, Dong Chen, Hongyu Liu, Qifeng Chen, Dongdong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.18472v1.pdf)  
  Keywords: audio-video generation, distillation, joint audio-video, video generation, video synthesis  
- **[Structured Stateful Relational Scripts with a High-Quality Dataset for Multi-Shot Audio-Visual Video Generation](https://arxiv.org/abs/2610.15512v1)**  
  Authors: Chen Zhao, Lehan Shen, Qilong Huang, Hongyu Li, Zhuoliang Kang, Xiaoming Wei, Jian Yang, Ying Tai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.15512v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://huggingface.co/datasets/shenlehan/MSAV-Script-100K}{MSAV-Script-100K}.) | [![Dataset](https://img.shields.io/badge/-Dataset-orange)](https://huggingface.co/datasets/shenlehan/MSAV-Script-100K)  
  Keywords: audio-visual generation, identity, sound, video generation  
- **[CatPortrait: Taming Video Generative Models for Portrait Animation via In-context Conditioning](https://arxiv.org/abs/2610.14957v1)**  
  Authors: Ziqi Ni, Zhou Fang, Shijian Wang, Rui Li, Yi Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.14957v1.pdf)  
  Keywords: audio-driven, controllable, image to video, image-to-video, portrait animation, video generation  
- **[PAGE: Parts-Aware Guidance for Co-Speech Gesture Portrait Video Generation](https://arxiv.org/abs/2610.13301v1)**  
  Authors: Yabiao Wang, Jiafu Wu, Yicheng Xu, Teng Hu, Shengzhe Zhou, Yanxiao Sun, Jiangning Zhang, Ying Tai, Yong Liu, Ming-Hsuan Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13301v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://aigc-explorer.github.io/PAGE)  
  Keywords: audio-driven, benchmark, body motion, denoising, efficient, evaluation, gesture, trajectory, video generation  
- **[AV-FlowEdit: Training-Free Prompt-Driven Audio-Visual Editing with Event-Aware Spectral Trajectory Preservation](https://arxiv.org/abs/2610.13072v1)**  
  Authors: Shaohua Pan, Xiao Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13072v1.pdf)  
  Keywords: joint audio-video, temporal consistency, trajectory, video diffusion, video editing  
- **[Real-Time Joint Audio-Video Generation by Parallel Adapter Composition](https://arxiv.org/abs/2610.10343v2)**  
  Authors: Jingyu Li, Xiaoxiao Xiang, Yiwen Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.10343v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pac-demo-2027.github.io/demo/) | [![Demo](https://img.shields.io/badge/-Demo-brightgreen)](https://pac-demo-2027.github.io/demo)  
  Keywords: audio-video generation, autoregressive, diffusion transformer, interactive, joint audio-video, streaming, video diffusion, video diffusion transformer, video generation  
- **[Kandinsky 6.0 Video: Foundation Models for Synchronized Video and Audio Generation](https://arxiv.org/abs/2610.05608v1)**  
  Authors: Team Kandinsky, Julia Agafonova, Bulat Akhmatov, Mikhail Aksyutin, Grigorii Alekseenko, Anastasia Aliaskina, Olga Androsova, Vladimir Arkhipkin, Anna Averchenkova, Alexander Belykh, Serafima Bocharova, Sofiya Bogakovskaya, Anton Bukashkin, Mark Bulygin, Kirill Buzygin, Irina Cheremnykh, Kirill Chernyshev, Mikhail Chernyshov, Vladimir Chernyy, David Chikovani, Georgy Daniltsev, Denis Dimitrov, Anna Dmitrienko, Vladimir Dokholyan, Sergey Emelyanov, Dmitry Ermilov, Georgii Fedorov, Polina Gavrilova, Nikolai Gerasimenko, Aleksandr Gordeev, Andrey Inozemtsev, Andrei Ivaniuta, Alexander Ivanov, Mikhail Karaev, Anastasiia Kargapoltseva, Ivan Kirillov, Nikita Kiselev, Valeria Kobenko, Yury Kolabushin, Denis Koposov, Anatoly Korobov, Vladimir Korviakov, Kirill Kozlov, Denis Krzhivokolskiy, Konstantin Kuklev, Alexander Kunitsyn, Sergey Kuzin, Vladislav Lakhtionov, Alexey Letunovskiy, Maxim Litvinov, Alexander Lyulkov, Georgy Makarov, Kirill Malakhov, Egor Malykh, Mikhail Mamaev, Dmitrii Mikhailov, Polina Mikhailova, Ivan Mikheev, Elizaveta Muromtseva, Nikolai Nazarkin, Tatiana Nikulina, Lev Novitskiy, Stanislav Onuchin, Nikita Osterov, Denis Parkhomenko, Anatoliy Parpara, Vladimir Polovnikov, Konstantin Reznikov, Azat Saginbaev, Nikita Samsonov, Alexander Sentsov, Nikita Shaimov, Artem Sherstyuk, Andrey Shutkin, Egor Silvestrov, Bulat Suleimanov, Matvey Suprunov, Sergey Taranov, Irina Tolstykh, Tatiana Trofimuk, Ilya Trushkin, Aleksandra Tsybina, Olga Varlashina, Viacheslav Vasilev, Ilya Vasiliev, Eugeny Vilisov, Sergey Yakubson, Konstantin Zakharov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.05608v1.pdf)  
  Keywords: architecture, audio-video generation, distillation, evaluation, human evaluation, super-resolution, video generation  
- **[DMAD: Distribution Matching as Adversarial Distillation for Fast Visual Generation](https://arxiv.org/abs/2610.02188v2)**  
  Authors: Zhengming Yu, Junkun Yuan, Haotian Yang, Gordon Guocheng Qian, Yizhi Wang, Angtian Wang, Yiding Yang, Bo Liu, Xin Li, Wenping Wang, Chongyang Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.02188v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yzmblog.github.io/projects/DMAD)  
  Keywords: audio-video generation, diffusion model, distillation, identity, joint audio-video, t2v, video generation  

### Controllable Generation

*Showing the latest 50 out of 322 papers*

- **[Perceive, Predict, and Plan: a Unified World Action Model for Egocentric Dexterous Manipulation](https://arxiv.org/abs/2610.22363v1)**  
  Authors: Zirui Wu, Chen Guo, Tianjian Jiang, Zeren Jiang, Zeming Li, Lingchen Yang, Longteng Duan, Ying Xue, Handi Yin, Shenyuan Gao, Martin R. Oswald, Jun Zhang, Ping Tan, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.22363v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://p3-wam.pages.dev)  
  Keywords: action-conditioned, architecture, diffusion transformer, evaluation, video diffusion, video diffusion transformer, video generation, video prediction  
- **[Speculative Forcing for Efficient Autoregressive Video Generation](https://arxiv.org/abs/2610.22347v1)**  
  Authors: Hyunwook Choi, Seungryong Kim, Dongyoon Han, Sangdoo Yun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.22347v1.pdf)  
  Keywords: autoregressive, autoregressive video, camera motion, denoising, efficient, long video, streaming, video generation  
- **[Velox: Spatial Memory Makes World Models Efficient](https://arxiv.org/abs/2610.22311v1)**  
  Authors: Qiuhong Shen, Shizun Wang, Xinchao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.22311v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://velox-world.com/velox)  
  Keywords: camera motion, denoising, efficient, interactive, simulation, streaming, style, video diffusion  
- **[Routing Policy Optimization for Online Diffusion Reinforcement Learning](https://arxiv.org/abs/2610.22282v1)**  
  Authors: Qiuhong Shen, Yiding Yang, Yuxin Zhang, Xinwei Huang, Minxuan Lin, Bo Liu, Hao Kang, Haotian Yang, Yizhi Wang, Chongyang Ma, Xinchao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.22282v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://velox-world.com/rpo)  
  Keywords: denoising, style, text to video, text-to-video, trajectory, video generation  
- **[RIGen: Beyond Action Following with Reciprocal Interaction in Generative Gameplay](https://arxiv.org/abs/2610.20811v1)**  
  Authors: Mengfei Li, Yi Zhang, Xingtong Ge, Lunjie Zhu, Fangyu Lin, Peng Li, Guanglu Song, Yu Liu, Wei Xue, Wenhan Luo, Yike Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.20811v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://murphylmf.github.io/RIGen)  
  Keywords: action-conditioned, dynamics, game, interactive, video generation  
- **[KinoGen: Customizable Humanoid Loco-Manipulation References via Kinematically Grounded Video Generation](https://arxiv.org/abs/2610.20552v1)**  
  Authors: Qi Wu, Lulu Zhao, Sanghyun Hahn, Rishi Yennu, Emmy Yang, Dingqi Zhang, Tao Pang, Jiuguang Wang, Kuan Fang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.20552v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kinogen-humanoid.github.io)  
  Keywords: keyframe, video generation  
- **[Glance Forcing: Making Bidirectional Diffusion Autoregressive at a Glance](https://arxiv.org/abs/2610.20220v1)**  
  Authors: Zhuobai Dong, Junchao Yi, Hu Jian Guo, Linjie Li, Rui Zhao, Alex Jinpeng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.20220v1.pdf)  
  Keywords: autoregressive, denoising, diffusion model, distillation, efficient, layout, trajectory, video synthesis  
- **[RepForcing: Representation-Space Initialization for Autoregressive Video Distillation](https://arxiv.org/abs/2610.20111v1)**  
  Authors: Siming Fu, Zheming Fu, Lianrui Mu, Haoyang Huang, Chaojie Gu, Ruizhe He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.20111v1.pdf)  
  Keywords: autoregressive, autoregressive video, diffusion transformer, distillation, trajectory, video diffusion, video diffusion transformer  
- **[SonoWorld: Towards Interactive Pose-Controllable Ultrasound World Models](https://arxiv.org/abs/2610.19327v1)**  
  Authors: Zefan Yang, Zheyuan Zhang, Boris Maihe, Yikang Liu, Hang Yu, Ankush Mukherjee, Xiao Chen, Pingkun Yan, Terrence Chen, Shanhui Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.19327v1.pdf)  
  Keywords: action-conditioned, autoregressive, controllable, diffusion model, distillation, dynamics, evaluation, interactive, simulation, video diffusion, world model  
- **[Kandinsky S2V 1.0: Audio-Driven Avatar Video Generation](https://arxiv.org/abs/2610.19290v1)**  
  Authors: Nikolay Semenov, Artem Riabinin, Sergey Bassenko, Anna Averchenkova, Julia Agafonova, Anastasia Aliaskina, Kirill Kozlov, Lev Novitskiy, Nikita Samsonov, Nikolai Gerasimenko, Denis Dimitrov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.19290v1.pdf)  
  Keywords: architecture, audio-driven, audio-driven avatar, avatar, benchmark, controllable, evaluation, gesture, human animation, human evaluation, long-form, speech-to-video, video generation  

### Human & Character Animation

*Showing the latest 50 out of 53 papers*

- **[DreamHMR: From Video Generation to Human Motion Modeling via Structural Focusing](https://arxiv.org/abs/2610.20124v1)**  
  Authors: Zhengjie Xu, Ruihao Gong, Xianglong Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.20124v1.pdf)  
  Keywords: body motion, evaluation, human motion, video generation  
- **[Kandinsky S2V 1.0: Audio-Driven Avatar Video Generation](https://arxiv.org/abs/2610.19290v1)**  
  Authors: Nikolay Semenov, Artem Riabinin, Sergey Bassenko, Anna Averchenkova, Julia Agafonova, Anastasia Aliaskina, Kirill Kozlov, Lev Novitskiy, Nikita Samsonov, Nikolai Gerasimenko, Denis Dimitrov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.19290v1.pdf)  
  Keywords: architecture, audio-driven, audio-driven avatar, avatar, benchmark, controllable, evaluation, gesture, human animation, human evaluation, long-form, speech-to-video, video generation  
- **[VGGA: Geometry-Grounded Autoencoder for Video Generation](https://arxiv.org/abs/2610.16204v1)**  
  Authors: Chaofan Gan, Yian Zhao, Shijie Li, Tieyuan Chen, Zicheng Zhao, Mehrtash Harandi, Weiyao Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.16204v1.pdf)  
  Keywords: dynamic 3d, human motion, latent video, video autoencoder, video generation  
- **[CatPortrait: Taming Video Generative Models for Portrait Animation via In-context Conditioning](https://arxiv.org/abs/2610.14957v1)**  
  Authors: Ziqi Ni, Zhou Fang, Shijian Wang, Rui Li, Yi Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.14957v1.pdf)  
  Keywords: audio-driven, controllable, image to video, image-to-video, portrait animation, video generation  
- **[PAGE: Parts-Aware Guidance for Co-Speech Gesture Portrait Video Generation](https://arxiv.org/abs/2610.13301v1)**  
  Authors: Yabiao Wang, Jiafu Wu, Yicheng Xu, Teng Hu, Shengzhe Zhou, Yanxiao Sun, Jiangning Zhang, Ying Tai, Yong Liu, Ming-Hsuan Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13301v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://aigc-explorer.github.io/PAGE)  
  Keywords: audio-driven, benchmark, body motion, denoising, efficient, evaluation, gesture, trajectory, video generation  
- **[PVSync: A Unified Lip-Sync Expert for Timing and Articulation](https://arxiv.org/abs/2610.09223v1)**  
  Authors: Kevin Stephen, Varun Menon, Timo Mertens, Nikita Drobyshev  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.09223v1.pdf)  
  Keywords: benchmark, talking head, video generation  
- **[PixReenact: Pixel-Conditioned Causal Video Diffusion for Streaming Head-Avatar Reenactment](https://arxiv.org/abs/2610.05233v1)**  
  Authors: Gavriel Habib, Dvir Samuel, Or Shimshi, Rami Ben-Ari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.05233v1.pdf)  
  Keywords: autoregressive, avatar, benchmark, denoising, distillation, driving, identity, motion transfer, streaming, video diffusion  
- **[Parasitic Co-Denoising: Unlocking 3D Human Motion Generation in a Frozen Video Diffusion Model](https://arxiv.org/abs/2610.03047v1)**  
  Authors: Yunjiao Zhou, Junlang Qian, Lihua Xie, Jianfei Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.03047v1.pdf)  
  Keywords: denoising, diffusion model, efficient, flow matching, human motion, text to video, text-to-video, video diffusion  
- **[GLARE: Generating Listening Heads with Appropriate Reactions](https://arxiv.org/abs/2609.40317v1)**  
  Authors: Zikai Liao, Yumin Suh, Yi Ouyang, Yi-Lun Lee, Yi-Hsuan Tsai, Zhaozheng Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.40317v1.pdf)  
  Keywords: audio-driven, evaluation, flow matching, talking head, video generation  
- **[TexTailor: Texture-Preserving Video Virtual Try-On via Adaptive Garment Conditioning](https://arxiv.org/abs/2609.39335v1)**  
  Authors: Zijing Qin, Jun Zhou, Ruicheng Zhang, Jiaqi Hou, Zunnan Xu, Ronghui Li, Zhenyu Xie, Xiu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.39335v1.pdf)  
  Keywords: denoising, diffusion transformer, temporal consistency, video diffusion, video diffusion transformer, virtual try-on  

### Image-to-Video Generation

*Showing the latest 50 out of 94 papers*

- **[Gen Through the Lens: Camera-Controllable Video Generation via Cross-Coordinate Conditioning Fusion](https://arxiv.org/abs/2610.15900v1)**  
  Authors: Shuai Li, Jinxu Xiang, Xinyuan Li, Hanlei Guo, Xiyang Tan, Alan Zhao, Xiaotong Zhao, Ran Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.15900v1.pdf)  
  Keywords: camera motion, controllable, image to video, image-to-video, video generation  
- **[A Plausible Future Is Not a Causal Future: Can Video Models Generate How the World Unfolds?](https://arxiv.org/abs/2610.15562v1)**  
  Authors: Jialiang Li, Zhengning Xu, Zongyang Ma, Shaobo Cui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.15562v1.pdf) | [![GitHub](https://img.shields.io/github/stars/SJTU-DeepDeltaLab/CausalCascade?style=social)](https://github.com/SJTU-DeepDeltaLab/CausalCascade)  
  Keywords: benchmark, dynamics, evaluation, image to video, image-to-video, physical, physical plausibility, video generation  
- **[CatPortrait: Taming Video Generative Models for Portrait Animation via In-context Conditioning](https://arxiv.org/abs/2610.14957v1)**  
  Authors: Ziqi Ni, Zhou Fang, Shijian Wang, Rui Li, Yi Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.14957v1.pdf)  
  Keywords: audio-driven, controllable, image to video, image-to-video, portrait animation, video generation  
- **[Images Talk Back: Guiding MMDiTs by Suppressing Image-to-Text Feedback](https://arxiv.org/abs/2610.13941v2)**  
  Authors: Yucheng Yang, Xiaoxiao Sun, Shusheng Yang, Jiakang Chen, Serena Yeung-Levy  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13941v2.pdf) | [![GitHub](https://img.shields.io/github/stars/yyc1215lll-creator/SFG?style=social)](https://github.com/yyc1215lll-creator/SFG)  
  Keywords: image to video, image-to-video, text to video, text-to-video, video generation  
- **[TrajCFG: Token-Wise Classifier-Free Guidance via Denoising Trajectory Feedback](https://arxiv.org/abs/2610.14153v1)**  
  Authors: Jingyu Liu, Hao Jiang, Yikang Ding, Huafeng Shi, Xu Yang, Xiaoqiang Liu, Guoxin Zhang, Pengfei Wan, Kun Gai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.14153v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jyliu-98.github.io/trajcfg-project-page)  
  Keywords: denoising, flow matching, image to video, image-to-video, text to video, text-to-video, trajectory, video generation  
- **[LETHE: Defending against Unauthorized Image-to-Video Generation via Value Diversity Collapse](https://arxiv.org/abs/2610.13333v1)**  
  Authors: Boheng Li, Yueming Xing, Yiming Li, Jie Zhang, Tianwei Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13333v1.pdf)  
  Keywords: efficient, i2v, image to video, image-to-video, video generation  
- **[Golden Anchor for Video Generation](https://arxiv.org/abs/2610.13217v2)**  
  Authors: Jinyuan Xu, Shitong Shao, Lichen Bai, Zikai Zhou, Guoxi Huang, Nantheera Anantrasirichai, Zeke Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13217v2.pdf)  
  Keywords: game, i2v, identity, image to video, image-to-video, interactive, style, video generation  
- **[Destination-Conditioned Adaptation with Semantic-Geometric Alignment for Generative Inbetweening](https://arxiv.org/abs/2610.13187v1)**  
  Authors: Zhiyu Xu, Wei Shang, Yushen Xu, Wenwen Li, Zhiyan Xu, Pengfei Zhu, Dongwei Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13187v1.pdf)  
  Keywords: dynamics, flow matching, image to video, image-to-video, latent video, latent video diffusion, trajectory, video diffusion  
- **[WorldAlign: Decoupled 4D Reward for World-Consistent Video Generation](https://arxiv.org/abs/2610.12382v1)**  
  Authors: Jing He, Kaixin Ding, Xingye Tian, Guibao Shen, Wenhang Ge, Xin Tao, Pengfei Wan, Ying-Cong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.12382v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://worldalign.github.io)  
  Keywords: camera motion, evaluation, image to video, image-to-video, physical, physical plausibility, simulation, video generation, world simulation  
- **[Towards Unified Evaluation of Prompt Enhancers for Video Generation](https://arxiv.org/abs/2610.11736v1)**  
  Authors: Yawen Shao, Yubo Zhu, Ziyun Dai, Zixun Fang, Kai Zhu, Zeyinzi Jiang, Yufeng Ai, Siyang Sun, Haolan Xue, Yu Shang, Yuxiang Bao, Zoubin Bi, Jingming Luo, Jie Xiao, Chaojie Mao, Zhehan Kan, Hongchen Luo, Yu Liu, Sheng Zhong, Wei Tong, Xueyang Fu, Yang Cao, Wei Zhai, Zheng-Jun Zha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11736v1.pdf)  
  Keywords: benchmark, cinematic, evaluation, image to video, image-to-video, text to video, text-to-video, video generation  

### Long Video Generation

*Showing the latest 50 out of 247 papers*

- **[Speculative Forcing for Efficient Autoregressive Video Generation](https://arxiv.org/abs/2610.22347v1)**  
  Authors: Hyunwook Choi, Seungryong Kim, Dongyoon Han, Sangdoo Yun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.22347v1.pdf)  
  Keywords: autoregressive, autoregressive video, camera motion, denoising, efficient, long video, streaming, video generation  
- **[Velox: Spatial Memory Makes World Models Efficient](https://arxiv.org/abs/2610.22311v1)**  
  Authors: Qiuhong Shen, Shizun Wang, Xinchao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.22311v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://velox-world.com/velox)  
  Keywords: camera motion, denoising, efficient, interactive, simulation, streaming, style, video diffusion  
- **[Where, How, and When: Query-Guided Grounding for Video Understanding](https://arxiv.org/abs/2610.21422v1)**  
  Authors: Yogesh Kumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.21422v1.pdf)  
  Keywords: few-shot, one-shot, temporal consistency, text to video, text-to-video, video to video, video-to-video  
- **[Tokenized Joint Source-Network Coding for Loss-Resilient Video Streaming](https://arxiv.org/abs/2610.21166v1)**  
  Authors: Ke Yang, Sixian Wang, Kailin Tan, Guo Lu, Jincheng Dai, Wenjun Zhang, Ping Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.21166v1.pdf)  
  Keywords: physical, streaming  
- **[Any Time, Any Space: A World-State-Centric Framework for Agentic Video Generation](https://arxiv.org/abs/2610.20571v1)**  
  Authors: Weijie Wang, Haomin Zhang, Ye Li, Akide Liu, Zeyu Zhang, Haoyu Zhao, Yefei He, Donny Y. Chen, Feng Chen, Bohan Zhuang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.20571v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lhmd.top/atas)  
  Keywords: benchmark, film, long-form, video generation  
- **[Speculative Sampling in Interactive Video Generation](https://arxiv.org/abs/2610.20556v1)**  
  Authors: Yubo Huang, Yuxuan Zhang, Jiaming Liu, Sirui Zhao, Enhong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.20556v1.pdf)  
  Keywords: interactive, streaming, video generation  
- **[Glance Forcing: Making Bidirectional Diffusion Autoregressive at a Glance](https://arxiv.org/abs/2610.20220v1)**  
  Authors: Zhuobai Dong, Junchao Yi, Hu Jian Guo, Linjie Li, Rui Zhao, Alex Jinpeng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.20220v1.pdf)  
  Keywords: autoregressive, denoising, diffusion model, distillation, efficient, layout, trajectory, video synthesis  
- **[StreamErase: Towards Ultra-Fast Streaming Video Erasing](https://arxiv.org/abs/2610.20137v1)**  
  Authors: Zhuobai Dong, Xiaobing Tu, Xiantao Zhang, Jinkui Ren, Yinggui Wang, Yue Ma, Linfeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.20137v1.pdf)  
  Keywords: benchmark, efficient, fast inference, interactive, long video, streaming, text to video, text-to-video  
- **[RepForcing: Representation-Space Initialization for Autoregressive Video Distillation](https://arxiv.org/abs/2610.20111v1)**  
  Authors: Siming Fu, Zheming Fu, Lianrui Mu, Haoyang Huang, Chaojie Gu, Ruizhe He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.20111v1.pdf)  
  Keywords: autoregressive, autoregressive video, diffusion transformer, distillation, trajectory, video diffusion, video diffusion transformer  
- **[SonoWorld: Towards Interactive Pose-Controllable Ultrasound World Models](https://arxiv.org/abs/2610.19327v1)**  
  Authors: Zefan Yang, Zheyuan Zhang, Boris Maihe, Yikang Liu, Hang Yu, Ankush Mukherjee, Xiao Chen, Pingkun Yan, Terrence Chen, Shanhui Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.19327v1.pdf)  
  Keywords: action-conditioned, autoregressive, controllable, diffusion model, distillation, dynamics, evaluation, interactive, simulation, video diffusion, world model  

### Personalization & Customization

*Showing the latest 50 out of 154 papers*

- **[Velox: Spatial Memory Makes World Models Efficient](https://arxiv.org/abs/2610.22311v1)**  
  Authors: Qiuhong Shen, Shizun Wang, Xinchao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.22311v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://velox-world.com/velox)  
  Keywords: camera motion, denoising, efficient, interactive, simulation, streaming, style, video diffusion  
- **[Routing Policy Optimization for Online Diffusion Reinforcement Learning](https://arxiv.org/abs/2610.22282v1)**  
  Authors: Qiuhong Shen, Yiding Yang, Yuxin Zhang, Xinwei Huang, Minxuan Lin, Bo Liu, Hao Kang, Haotian Yang, Yizhi Wang, Chongyang Ma, Xinchao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.22282v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://velox-world.com/rpo)  
  Keywords: denoising, style, text to video, text-to-video, trajectory, video generation  
- **[Where, How, and When: Query-Guided Grounding for Video Understanding](https://arxiv.org/abs/2610.21422v1)**  
  Authors: Yogesh Kumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.21422v1.pdf)  
  Keywords: few-shot, one-shot, temporal consistency, text to video, text-to-video, video to video, video-to-video  
- **[Temporal Specification Guidance for Text-to-Video Generation](https://arxiv.org/abs/2610.20822v1)**  
  Authors: Avishree Khare, Hideki Okamoto, Bardh Hoxha, Georgios Fainekos, Rajeev Alur  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.20822v1.pdf)  
  Keywords: benchmark, concept, denoising, efficient, text to video, text-to-video, video generation  
- **[StateCraft: Augmenting Video World Models with Abstract-State Reasoning](https://arxiv.org/abs/2610.19795v1)**  
  Authors: Lorenzo Venturoli, Nedko Savov, Xi Wang, Marc Pollefeys, Luc Van Gool  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.19795v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://insait-institute.github.io/StateCraft)  
  Keywords: architecture, benchmark, concept, diffusion model, dynamics, evaluation, video diffusion  
- **[LongForcing: Scaling Temporal Manifold Matching for Long-Horizon World Rollout](https://arxiv.org/abs/2610.18289v1)**  
  Authors: Ziyu Zhu, Zhaoxu Sun, Fan Jiang, Mengchao Wang, Junfeng Ni, Ting-Bing Xu, Zhicheng Liu, Mu Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.18289v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Fantasy-AMAP/LongForcing?style=social)](https://github.com/Fantasy-AMAP/LongForcing)  
  Keywords: action-conditioned, architecture, autoregressive, autoregressive video, distillation, identity, interactive, text to video, text-to-video, video diffusion, video generation  
- **[QK-Edit: Revisiting Attention-based Injection in MM-DiT for Image and Video Editing](https://arxiv.org/abs/2610.17829v2)**  
  Authors: Tiancheng Shen, Zilong Huang, Xiangtai Li, Zhijie Lin, Jiyang Liu, Yitong Wang, Jiashi Feng, Ming-Hsuan Yang, Jun Hao Liew  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.17829v2.pdf)  
  Keywords: dit, dynamics, style, video editing  
- **[IsoVRBench: Video Reward Modeling Without Human Feedback](https://arxiv.org/abs/2610.17234v1)**  
  Authors: Shuyue Stella Li, Jacqueline He, Jiahui Chen, Sreya Dutta Roy, Yulia Tsvetkov, Luke Zettlemoyer, Marjan Ghazvininejad, Xiaochuang Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.17234v1.pdf)  
  Keywords: benchmark, identity, video generation  
- **[REEL: Learning to Retrieve, Evaluate, and Evolve Visual Memory for Any Long-Horizon Multi-Shot Video Generation](https://arxiv.org/abs/2610.16632v1)**  
  Authors: Hang Xu, Guohui Zhang, Xiaoxiao Ma, Hu Yu, Jie Huang, Jiayin Xiao, Lin Song, Haoyang Huang, Nan Duan, Feng Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.16632v1.pdf)  
  Keywords: identity, long video, video generation  
- **[Tikhonov-Stabilized Bezier Representation Forecasting for Training-free Diffusion Acceleration](https://arxiv.org/abs/2610.16448v1)**  
  Authors: Lei Zhu, Mujie Lin, Ruochong Zheng, Guangyi Wang, Hao Li, Peng Jin, Chang Liu, Jie Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.16448v1.pdf)  
  Keywords: acceleration, denoising, style, trajectory, video diffusion, video generation  

### Physical Understanding

*Showing the latest 50 out of 302 papers*

- **[Tokenized Joint Source-Network Coding for Loss-Resilient Video Streaming](https://arxiv.org/abs/2610.21166v1)**  
  Authors: Ke Yang, Sixian Wang, Kailin Tan, Guo Lu, Jincheng Dai, Wenjun Zhang, Ping Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.21166v1.pdf)  
  Keywords: physical, streaming  
- **[Sparse Attention for Video Generation Acceleration via Growing Sparsity and Reduced Search](https://arxiv.org/abs/2610.21129v1)**  
  Authors: Yun Dai, Yuyun Chen, Jiarui Wen, Huiping Zhuang, Cen Chen, Ziqian Zeng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.21129v1.pdf)  
  Keywords: acceleration, denoising, dynamics, evaluation, sparse attention, video generation  
- **[RIGen: Beyond Action Following with Reciprocal Interaction in Generative Gameplay](https://arxiv.org/abs/2610.20811v1)**  
  Authors: Mengfei Li, Yi Zhang, Xingtong Ge, Lunjie Zhu, Fangyu Lin, Peng Li, Guanglu Song, Yu Liu, Wei Xue, Wenhan Luo, Yike Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.20811v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://murphylmf.github.io/RIGen)  
  Keywords: action-conditioned, dynamics, game, interactive, video generation  
- **[PhyMetric: Diagnosing Physical Plausibility in Text-to-Video Generation via Scene-Level QA](https://arxiv.org/abs/2610.19823v1)**  
  Authors: Siwei Meng, Xuerou Cai, Rui Hu, Ping Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.19823v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://mengsiwei.github.io/PhyMetric)  
  Keywords: benchmark, evaluation, physical, physical plausibility, t2v, text to video, text-to-video, video generation  
- **[StateCraft: Augmenting Video World Models with Abstract-State Reasoning](https://arxiv.org/abs/2610.19795v1)**  
  Authors: Lorenzo Venturoli, Nedko Savov, Xi Wang, Marc Pollefeys, Luc Van Gool  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.19795v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://insait-institute.github.io/StateCraft)  
  Keywords: architecture, benchmark, concept, diffusion model, dynamics, evaluation, video diffusion  
- **[FPV-CRASH: A Dataset for Offline Crash Moment Localization in Drone First-Person-View Videos](https://arxiv.org/abs/2610.19785v1)**  
  Authors: Jifan Zhang, Tingyu Wang, Qian Liu, Zhedong Zheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.19785v1.pdf)  
  Keywords: evaluation, physical, robotics, text to video, text-to-video  
- **[Integrating Simulation and Chain-of-thought Reasoning in Multimodal-Language Models For Physical Reasoning](https://arxiv.org/abs/2610.19441v1)**  
  Authors: YingQiao Wang, Eric Bigelow, Tomer Ullman, Yujin Tang, Sebastian Risi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.19441v1.pdf)  
  Keywords: dynamics, physical, physics, simulation  
- **[SonoWorld: Towards Interactive Pose-Controllable Ultrasound World Models](https://arxiv.org/abs/2610.19327v1)**  
  Authors: Zefan Yang, Zheyuan Zhang, Boris Maihe, Yikang Liu, Hang Yu, Ankush Mukherjee, Xiao Chen, Pingkun Yan, Terrence Chen, Shanhui Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.19327v1.pdf)  
  Keywords: action-conditioned, autoregressive, controllable, diffusion model, distillation, dynamics, evaluation, interactive, simulation, video diffusion, world model  
- **[Data-Free Continual Learning for World Action Model with Rectified Generative Replay](https://arxiv.org/abs/2610.18038v2)**  
  Authors: Kaipeng Fang, Hangxu Liu, Chaojian Shi, Yunsong Zhou, Hongzi Zhu, Minyi Guo, Jingkuan Song, Lianli Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.18038v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kaipengfang.github.io/r2-wam)  
  Keywords: dynamics, robotics, video generation  
- **[QK-Edit: Revisiting Attention-based Injection in MM-DiT for Image and Video Editing](https://arxiv.org/abs/2610.17829v2)**  
  Authors: Tiancheng Shen, Zilong Huang, Xiangtai Li, Zhijie Lin, Jiyang Liu, Yitong Wang, Jiashi Feng, Ming-Hsuan Yang, Jun Hao Liew  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.17829v2.pdf)  
  Keywords: dit, dynamics, style, video editing  

### Surveys & Benchmarks

*Showing the latest 50 out of 322 papers*

- **[Perceive, Predict, and Plan: a Unified World Action Model for Egocentric Dexterous Manipulation](https://arxiv.org/abs/2610.22363v1)**  
  Authors: Zirui Wu, Chen Guo, Tianjian Jiang, Zeren Jiang, Zeming Li, Lingchen Yang, Longteng Duan, Ying Xue, Handi Yin, Shenyuan Gao, Martin R. Oswald, Jun Zhang, Ping Tan, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.22363v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://p3-wam.pages.dev)  
  Keywords: action-conditioned, architecture, diffusion transformer, evaluation, video diffusion, video diffusion transformer, video generation, video prediction  
- **[AVC-Reward: Event-Centric Audio-Video Consistency Evaluation](https://arxiv.org/abs/2610.22321v1)**  
  Authors: Yuruo Wu, Kaihang Pan, Kai Shen, Jiacheng Li, Shuyuan Tu, Jisheng Dang, Li Tuoyu, Juncheng Li, Siliang Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.22321v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://tsuki0512.github.io/AVC-Reward.github.io)  
  Keywords: audio-video generation, benchmark, evaluation, joint audio-video, video generation  
- **[Sparse Attention for Video Generation Acceleration via Growing Sparsity and Reduced Search](https://arxiv.org/abs/2610.21129v1)**  
  Authors: Yun Dai, Yuyun Chen, Jiarui Wen, Huiping Zhuang, Cen Chen, Ziqian Zeng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.21129v1.pdf)  
  Keywords: acceleration, denoising, dynamics, evaluation, sparse attention, video generation  
- **[Temporal Specification Guidance for Text-to-Video Generation](https://arxiv.org/abs/2610.20822v1)**  
  Authors: Avishree Khare, Hideki Okamoto, Bardh Hoxha, Georgios Fainekos, Rajeev Alur  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.20822v1.pdf)  
  Keywords: benchmark, concept, denoising, efficient, text to video, text-to-video, video generation  
- **[Any Time, Any Space: A World-State-Centric Framework for Agentic Video Generation](https://arxiv.org/abs/2610.20571v1)**  
  Authors: Weijie Wang, Haomin Zhang, Ye Li, Akide Liu, Zeyu Zhang, Haoyu Zhao, Yefei He, Donny Y. Chen, Feng Chen, Bohan Zhuang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.20571v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lhmd.top/atas)  
  Keywords: benchmark, film, long-form, video generation  
- **[StreamErase: Towards Ultra-Fast Streaming Video Erasing](https://arxiv.org/abs/2610.20137v1)**  
  Authors: Zhuobai Dong, Xiaobing Tu, Xiantao Zhang, Jinkui Ren, Yinggui Wang, Yue Ma, Linfeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.20137v1.pdf)  
  Keywords: benchmark, efficient, fast inference, interactive, long video, streaming, text to video, text-to-video  
- **[DreamHMR: From Video Generation to Human Motion Modeling via Structural Focusing](https://arxiv.org/abs/2610.20124v1)**  
  Authors: Zhengjie Xu, Ruihao Gong, Xianglong Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.20124v1.pdf)  
  Keywords: body motion, evaluation, human motion, video generation  
- **[PhyMetric: Diagnosing Physical Plausibility in Text-to-Video Generation via Scene-Level QA](https://arxiv.org/abs/2610.19823v1)**  
  Authors: Siwei Meng, Xuerou Cai, Rui Hu, Ping Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.19823v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://mengsiwei.github.io/PhyMetric)  
  Keywords: benchmark, evaluation, physical, physical plausibility, t2v, text to video, text-to-video, video generation  
- **[StateCraft: Augmenting Video World Models with Abstract-State Reasoning](https://arxiv.org/abs/2610.19795v1)**  
  Authors: Lorenzo Venturoli, Nedko Savov, Xi Wang, Marc Pollefeys, Luc Van Gool  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.19795v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://insait-institute.github.io/StateCraft)  
  Keywords: architecture, benchmark, concept, diffusion model, dynamics, evaluation, video diffusion  
- **[FPV-CRASH: A Dataset for Offline Crash Moment Localization in Drone First-Person-View Videos](https://arxiv.org/abs/2610.19785v1)**  
  Authors: Jifan Zhang, Tingyu Wang, Qian Liu, Zhedong Zheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.19785v1.pdf)  
  Keywords: evaluation, physical, robotics, text to video, text-to-video  

### Text-to-Video Generation

*Showing the latest 50 out of 144 papers*

- **[Routing Policy Optimization for Online Diffusion Reinforcement Learning](https://arxiv.org/abs/2610.22282v1)**  
  Authors: Qiuhong Shen, Yiding Yang, Yuxin Zhang, Xinwei Huang, Minxuan Lin, Bo Liu, Hao Kang, Haotian Yang, Yizhi Wang, Chongyang Ma, Xinchao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.22282v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://velox-world.com/rpo)  
  Keywords: denoising, style, text to video, text-to-video, trajectory, video generation  
- **[Where, How, and When: Query-Guided Grounding for Video Understanding](https://arxiv.org/abs/2610.21422v1)**  
  Authors: Yogesh Kumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.21422v1.pdf)  
  Keywords: few-shot, one-shot, temporal consistency, text to video, text-to-video, video to video, video-to-video  
- **[Temporal Specification Guidance for Text-to-Video Generation](https://arxiv.org/abs/2610.20822v1)**  
  Authors: Avishree Khare, Hideki Okamoto, Bardh Hoxha, Georgios Fainekos, Rajeev Alur  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.20822v1.pdf)  
  Keywords: benchmark, concept, denoising, efficient, text to video, text-to-video, video generation  
- **[StreamErase: Towards Ultra-Fast Streaming Video Erasing](https://arxiv.org/abs/2610.20137v1)**  
  Authors: Zhuobai Dong, Xiaobing Tu, Xiantao Zhang, Jinkui Ren, Yinggui Wang, Yue Ma, Linfeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.20137v1.pdf)  
  Keywords: benchmark, efficient, fast inference, interactive, long video, streaming, text to video, text-to-video  
- **[PhyMetric: Diagnosing Physical Plausibility in Text-to-Video Generation via Scene-Level QA](https://arxiv.org/abs/2610.19823v1)**  
  Authors: Siwei Meng, Xuerou Cai, Rui Hu, Ping Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.19823v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://mengsiwei.github.io/PhyMetric)  
  Keywords: benchmark, evaluation, physical, physical plausibility, t2v, text to video, text-to-video, video generation  
- **[FPV-CRASH: A Dataset for Offline Crash Moment Localization in Drone First-Person-View Videos](https://arxiv.org/abs/2610.19785v1)**  
  Authors: Jifan Zhang, Tingyu Wang, Qian Liu, Zhedong Zheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.19785v1.pdf)  
  Keywords: evaluation, physical, robotics, text to video, text-to-video  
- **[LongForcing: Scaling Temporal Manifold Matching for Long-Horizon World Rollout](https://arxiv.org/abs/2610.18289v1)**  
  Authors: Ziyu Zhu, Zhaoxu Sun, Fan Jiang, Mengchao Wang, Junfeng Ni, Ting-Bing Xu, Zhicheng Liu, Mu Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.18289v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Fantasy-AMAP/LongForcing?style=social)](https://github.com/Fantasy-AMAP/LongForcing)  
  Keywords: action-conditioned, architecture, autoregressive, autoregressive video, distillation, identity, interactive, text to video, text-to-video, video diffusion, video generation  
- **[VARI: Robust Text-to-Video Generation via Group-Structured Intent Alignment](https://arxiv.org/abs/2610.18189v1)**  
  Authors: Mingxuan Zhu, Hohei Chan, Shiyuan Liu, Yuanxing Zhang, Lu Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.18189v1.pdf)  
  Keywords: distillation, evaluation, human evaluation, t2v, text to video, text-to-video, video generation  
- **[FlowCred: Hierarchical Credit Assignment and Functional Coordination for Joint Text-to-Video Post-Training](https://arxiv.org/abs/2610.18142v1)**  
  Authors: Mingxuan Zhu, Yanwei Huang, Shiyuan Liu, Xinzhi Zhang, Shujie Li, Yuanxing Zhang, Lu Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.18142v1.pdf)  
  Keywords: evaluation, human evaluation, t2v, text to video, text-to-video  
- **[Hierarchical Curriculum Learning for Surgical Video Generation: Focusing on Bilateral Axillo-Breast Approach Robotic Thyroidectomy Datasets](https://arxiv.org/abs/2610.17684v1)**  
  Authors: Youngbin Kong, Seungho Lee, Jae Kyung Shin, Jong-hyuk Ahn, Hyoun-Joong Kong, Kyu Eun Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.17684v1.pdf)  
  Keywords: benchmark, diffusion model, education, simulation, text to video, text-to-video, video diffusion, video generation  

### Video Editing

*Showing the latest 50 out of 89 papers*

- **[Where, How, and When: Query-Guided Grounding for Video Understanding](https://arxiv.org/abs/2610.21422v1)**  
  Authors: Yogesh Kumar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.21422v1.pdf)  
  Keywords: few-shot, one-shot, temporal consistency, text to video, text-to-video, video to video, video-to-video  
- **[QK-Edit: Revisiting Attention-based Injection in MM-DiT for Image and Video Editing](https://arxiv.org/abs/2610.17829v2)**  
  Authors: Tiancheng Shen, Zilong Huang, Xiangtai Li, Zhijie Lin, Jiyang Liu, Yitong Wang, Jiashi Feng, Ming-Hsuan Yang, Jun Hao Liew  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.17829v2.pdf)  
  Keywords: dit, dynamics, style, video editing  
- **[AV-FlowEdit: Training-Free Prompt-Driven Audio-Visual Editing with Event-Aware Spectral Trajectory Preservation](https://arxiv.org/abs/2610.13072v1)**  
  Authors: Shaohua Pan, Xiao Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13072v1.pdf)  
  Keywords: joint audio-video, temporal consistency, trajectory, video diffusion, video editing  
- **[MotionCoach: Constructing Multimodal Guidance for Video Professional Motion Editing](https://arxiv.org/abs/2610.12963v1)**  
  Authors: Siyi Qian, Hanqing Yang, Weihuang Lin, Zihao Yang, Yichen Lu, Yuanhong Zheng, Sheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.12963v1.pdf)  
  Keywords: evaluation, motion editing, video editing  
- **[VINCIE-NExT: Unlocking Video Editing from Images via In-Context Modeling](https://arxiv.org/abs/2610.12104v1)**  
  Authors: Leigang Qu, Feng Cheng, Ziyan Yang, Bangbang Yang, Zhaoyang Huang, Wei Chow, Yicong Li, Wenjie Wang, Tat-Seng Chua, Yan Zeng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.12104v1.pdf)  
  Keywords: video editing  
- **[From Video Clips to Creation Trajectory: Sora100K for AI-Native Video Creation](https://arxiv.org/abs/2610.11770v1)**  
  Authors: Sicong Yang, Ruihuan Yang, Jian Lu, Jianfei Yuan, Xiaodong Cun, Xiuli Bi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11770v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://huggingface.co/datasets/ysicong/Sora100K.) | [![Dataset](https://img.shields.io/badge/-Dataset-orange)](https://huggingface.co/datasets/ysicong/Sora100K)  
  Keywords: evaluation, text to video, text-to-video, trajectory, video editing, video generation  
- **[Transforming Image Editors into Video Editors](https://arxiv.org/abs/2610.11037v1)**  
  Authors: Feng Wang, Zijie Li, Ceyuan Yang, Alan Yuille, Peng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11037v1.pdf) | [![GitHub](https://img.shields.io/github/stars/wangf3014/AVE?style=social)](https://github.com/wangf3014/AVE)  
  Keywords: diffusion model, image to video, image-to-video, temporal consistency, video diffusion, video editing  
- **[SoccerNet-FoulRet: Retrieving Semantically Similar Soccer Foul Videos](https://arxiv.org/abs/2610.09742v2)**  
  Authors: Jacobus Arthur, Ahmad Sait, Batool Hani, Merey Ramazanova, Jan Held, Marc Van Droogenbroeck, Bernard Ghanem, Anthony Cioppa, Silvio Giancola  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.09742v2.pdf) | [![GitHub](https://img.shields.io/github/stars/SoccerNet/sn-foulret?style=social)](https://github.com/SoccerNet/sn-foulret)  
  Keywords: benchmark, video to video, video-to-video  
- **[ALIVE: Interaction-Aligned Object Insertion for First-Frame-Guided Video Editing](https://arxiv.org/abs/2610.08779v1)**  
  Authors: Zhenghong Zhou, Zhe Lin, Jiebo Luo, Yuqian Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.08779v1.pdf)  
  Keywords: benchmark, video editing  
- **[Robotizing Human Videos with Physically Consistent Interactions](https://arxiv.org/abs/2610.06137v1)**  
  Authors: Ching-Lam Cheng, Shengfeng He, Bin Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.06137v1.pdf)  
  Keywords: physical, video editing  

### Video Inpainting & Completion

- **[Perceive, Predict, and Plan: a Unified World Action Model for Egocentric Dexterous Manipulation](https://arxiv.org/abs/2610.22363v1)**  
  Authors: Zirui Wu, Chen Guo, Tianjian Jiang, Zeren Jiang, Zeming Li, Lingchen Yang, Longteng Duan, Ying Xue, Handi Yin, Shenyuan Gao, Martin R. Oswald, Jun Zhang, Ping Tan, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.22363v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://p3-wam.pages.dev)  
  Keywords: action-conditioned, architecture, diffusion transformer, evaluation, video diffusion, video diffusion transformer, video generation, video prediction  
- **[PINT: A Unified Model with Shared Predictive Intent for Robot Manipulation](https://arxiv.org/abs/2610.16355v1)**  
  Authors: Xinyu Guo, Chao Jing, Li Yi, Xingyu Chen, Zhengxing Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.16355v1.pdf)  
  Keywords: dynamics, embodied, video generation, video prediction  
- **[SurgCast: Action-Conditioned Future Skeletons for Controllable Surgical World Models](https://arxiv.org/abs/2610.15645v1)**  
  Authors: Wanhao Liu, Rulin Zhou, Liangjing Shao, Zhaocheng Lin, Dongyue Li, Jinsong Lin, Guoheng Ma, Hangheng Yang, Zhiqing Tang, Jing Chen, Panshuo Li, Hongliang Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.15645v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://surgcast.netlify.app/.) | [![Demo](https://img.shields.io/badge/-Demo-brightgreen)](https://surgcast.netlify.app)  
  Keywords: action-conditioned, controllable, video generation, video prediction  
- **[ProAR: Learning Prospective Reasoning with Autoregressive Video Models](https://arxiv.org/abs/2610.03664v1)**  
  Authors: Linghui Shen, Tinghui Zhu, Sheng Zhang, Muhao Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.03664v1.pdf)  
  Keywords: autoregressive, autoregressive video, dynamics, efficient, embodied, frame prediction, video generation  
- **[Dexterous Tactile World Model](https://arxiv.org/abs/2609.34286v1)**  
  Authors: Ziyao Zeng, Xiatao Sun, Hao Wang, Yueyang Pan, Zhengxiang Yu, Fengyu Yang, Tianyu Liu, Zhiwen Fan, Daniel Rakita  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.34286v1.pdf)  
  Keywords: architecture, diffusion transformer, frame prediction, future frame prediction, video diffusion, video diffusion transformer, video world model, world model  
- **[WorldWeave: Growing Persistent Geometric Worlds for Video Generation](https://arxiv.org/abs/2609.34221v2)**  
  Authors: Yifan Huang, Lifan Jiang, Qingyue Hao, Cheng Chen, Boxi Wu, Xiaoxue Ren, Xiaofei He, Dehai Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.34221v2.pdf)  
  Keywords: outpainting, video generation, video synthesis  
- **[MT-WAM: Reorienting the One-Pass Predictive Representation Toward Action Generation](https://arxiv.org/abs/2609.21474v1)**  
  Authors: Yiguang Yang, Jiankun Peng, Xiaoming Wang, Yiran Zhang, Zhibo Fang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.21474v1.pdf)  
  Keywords: diffusion transformer, dynamics, embodied, video diffusion, video diffusion transformer, video prediction  
- **[StrucPhysVideo: Learning Physical Dynamics from Structured Captions and Robot Actions](https://arxiv.org/abs/2609.18430v1)**  
  Authors: Awomo-WM Team, :, Enhui Ma, Kaiwen Guo, Tingrui Zhang, Wei Song, Yingshui Tan, Jianhua Xu, Tong Zhang, Kaicheng Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.18430v1.pdf)  
  Keywords: action-conditioned, autoregressive, camera motion, denoising, distillation, dynamics, embodied, image to video, image-to-video, interactive, physical, physics, video prediction, video world model, world model  
- **[GeoLAM: Learning Geometry-Grounded Latent Actions from Unlabeled Human Videos](https://arxiv.org/abs/2609.17099v1)**  
  Authors: Yifan Xie, Hekun Tian, Jinkun Liu, YuAn Wang, Qiao Sun, Wenbo Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.17099v1.pdf)  
  Keywords: benchmark, trajectory, video generation, video prediction  
- **[Stream4D: 4D-Consistency for Streaming Autoregressive Diffusion Video Models](https://arxiv.org/abs/2608.19556v1)**  
  Authors: Yuanhao Ban, Jiaqi Feng, Hengguang Zhou, Xiaohuan Pei, Justin Cui, Cho-Jui Hsieh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.19556v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://banyuanhao.github.io/Stream4D)  
  Keywords: autoregressive, autoregressive video, dynamics, frame prediction, streaming, video generation  

### Video Super-Resolution & Enhancement

*Showing the latest 50 out of 172 papers*

- **[Speculative Forcing for Efficient Autoregressive Video Generation](https://arxiv.org/abs/2610.22347v1)**  
  Authors: Hyunwook Choi, Seungryong Kim, Dongyoon Han, Sangdoo Yun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.22347v1.pdf)  
  Keywords: autoregressive, autoregressive video, camera motion, denoising, efficient, long video, streaming, video generation  
- **[Velox: Spatial Memory Makes World Models Efficient](https://arxiv.org/abs/2610.22311v1)**  
  Authors: Qiuhong Shen, Shizun Wang, Xinchao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.22311v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://velox-world.com/velox)  
  Keywords: camera motion, denoising, efficient, interactive, simulation, streaming, style, video diffusion  
- **[Routing Policy Optimization for Online Diffusion Reinforcement Learning](https://arxiv.org/abs/2610.22282v1)**  
  Authors: Qiuhong Shen, Yiding Yang, Yuxin Zhang, Xinwei Huang, Minxuan Lin, Bo Liu, Hao Kang, Haotian Yang, Yizhi Wang, Chongyang Ma, Xinchao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.22282v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://velox-world.com/rpo)  
  Keywords: denoising, style, text to video, text-to-video, trajectory, video generation  
- **[Sparse Attention for Video Generation Acceleration via Growing Sparsity and Reduced Search](https://arxiv.org/abs/2610.21129v1)**  
  Authors: Yun Dai, Yuyun Chen, Jiarui Wen, Huiping Zhuang, Cen Chen, Ziqian Zeng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.21129v1.pdf)  
  Keywords: acceleration, denoising, dynamics, evaluation, sparse attention, video generation  
- **[Temporal Specification Guidance for Text-to-Video Generation](https://arxiv.org/abs/2610.20822v1)**  
  Authors: Avishree Khare, Hideki Okamoto, Bardh Hoxha, Georgios Fainekos, Rajeev Alur  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.20822v1.pdf)  
  Keywords: benchmark, concept, denoising, efficient, text to video, text-to-video, video generation  
- **[Glance Forcing: Making Bidirectional Diffusion Autoregressive at a Glance](https://arxiv.org/abs/2610.20220v1)**  
  Authors: Zhuobai Dong, Junchao Yi, Hu Jian Guo, Linjie Li, Rui Zhao, Alex Jinpeng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.20220v1.pdf)  
  Keywords: autoregressive, denoising, diffusion model, distillation, efficient, layout, trajectory, video synthesis  
- **[Complementary Future Token Pruning for World Action Models](https://arxiv.org/abs/2610.19957v1)**  
  Authors: Baekseung Kim, Junhoo Lee, Sohyeon Hong, Suhyun Jeon, Minkyu Kim, Seungyeon Kim, Donghoon Han, Nojun Kwak  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.19957v1.pdf)  
  Keywords: denoising, simulation, video synthesis  
- **[Heuristics are Not Enough: Calibrated and Corrected Caching for Video Diffusion Acceleration](https://arxiv.org/abs/2610.16545v1)**  
  Authors: Jiyue Jiang, Zhiyu Huo, Yuhan Chen, Yanruisheng Shao, Gong Zhang, Lei Deng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.16545v1.pdf) | [![GitHub](https://img.shields.io/github/stars/jiangjyjy/AlignCache?style=social)](https://github.com/jiangjyjy/AlignCache)  
  Keywords: acceleration, denoising, dynamics, trajectory, video diffusion, video generation  
- **[Tikhonov-Stabilized Bezier Representation Forecasting for Training-free Diffusion Acceleration](https://arxiv.org/abs/2610.16448v1)**  
  Authors: Lei Zhu, Mujie Lin, Ruochong Zheng, Guangyi Wang, Hao Li, Peng Jin, Chang Liu, Jie Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.16448v1.pdf)  
  Keywords: acceleration, denoising, style, trajectory, video diffusion, video generation  
- **[Competition Domains Matter: Selective Head Globalization for Training-Free Sparse Attention in Video Diffusion Transformers](https://arxiv.org/abs/2610.14672v1)**  
  Authors: Tiantian Liu, Meng Wan, Zhiqiang Liang, Jue Wang, Ningming Nie, Yangang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.14672v1.pdf)  
  Keywords: denoising, diffusion transformer, efficient, sparse attention, video diffusion, video diffusion transformer  

### World Models & Simulation

*Showing the latest 50 out of 247 papers*

- **[Perceive, Predict, and Plan: a Unified World Action Model for Egocentric Dexterous Manipulation](https://arxiv.org/abs/2610.22363v1)**  
  Authors: Zirui Wu, Chen Guo, Tianjian Jiang, Zeren Jiang, Zeming Li, Lingchen Yang, Longteng Duan, Ying Xue, Handi Yin, Shenyuan Gao, Martin R. Oswald, Jun Zhang, Ping Tan, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.22363v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://p3-wam.pages.dev)  
  Keywords: action-conditioned, architecture, diffusion transformer, evaluation, video diffusion, video diffusion transformer, video generation, video prediction  
- **[Velox: Spatial Memory Makes World Models Efficient](https://arxiv.org/abs/2610.22311v1)**  
  Authors: Qiuhong Shen, Shizun Wang, Xinchao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.22311v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://velox-world.com/velox)  
  Keywords: camera motion, denoising, efficient, interactive, simulation, streaming, style, video diffusion  
- **[CoWorld Reasoner: Agentic Multimodal Reasoning with the Evolving Video World Model-Driven Harness](https://arxiv.org/abs/2610.21910v1)**  
  Authors: Dongjie Cheng, Ruifeng Yuan, Ran Wei, Ning Song, Yongqi Li, Wenjie Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.21910v1.pdf)  
  Keywords: novel view, video world model, world model  
- **[RIGen: Beyond Action Following with Reciprocal Interaction in Generative Gameplay](https://arxiv.org/abs/2610.20811v1)**  
  Authors: Mengfei Li, Yi Zhang, Xingtong Ge, Lunjie Zhu, Fangyu Lin, Peng Li, Guanglu Song, Yu Liu, Wei Xue, Wenhan Luo, Yike Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.20811v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://murphylmf.github.io/RIGen)  
  Keywords: action-conditioned, dynamics, game, interactive, video generation  
- **[Speculative Sampling in Interactive Video Generation](https://arxiv.org/abs/2610.20556v1)**  
  Authors: Yubo Huang, Yuxuan Zhang, Jiaming Liu, Sirui Zhao, Enhong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.20556v1.pdf)  
  Keywords: interactive, streaming, video generation  
- **[StreamErase: Towards Ultra-Fast Streaming Video Erasing](https://arxiv.org/abs/2610.20137v1)**  
  Authors: Zhuobai Dong, Xiaobing Tu, Xiantao Zhang, Jinkui Ren, Yinggui Wang, Yue Ma, Linfeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.20137v1.pdf)  
  Keywords: benchmark, efficient, fast inference, interactive, long video, streaming, text to video, text-to-video  
- **[Complementary Future Token Pruning for World Action Models](https://arxiv.org/abs/2610.19957v1)**  
  Authors: Baekseung Kim, Junhoo Lee, Sohyeon Hong, Suhyun Jeon, Minkyu Kim, Seungyeon Kim, Donghoon Han, Nojun Kwak  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.19957v1.pdf)  
  Keywords: denoising, simulation, video synthesis  
- **[Integrating Simulation and Chain-of-thought Reasoning in Multimodal-Language Models For Physical Reasoning](https://arxiv.org/abs/2610.19441v1)**  
  Authors: YingQiao Wang, Eric Bigelow, Tomer Ullman, Yujin Tang, Sebastian Risi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.19441v1.pdf)  
  Keywords: dynamics, physical, physics, simulation  
- **[SonoWorld: Towards Interactive Pose-Controllable Ultrasound World Models](https://arxiv.org/abs/2610.19327v1)**  
  Authors: Zefan Yang, Zheyuan Zhang, Boris Maihe, Yikang Liu, Hang Yu, Ankush Mukherjee, Xiao Chen, Pingkun Yan, Terrence Chen, Shanhui Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.19327v1.pdf)  
  Keywords: action-conditioned, autoregressive, controllable, diffusion model, distillation, dynamics, evaluation, interactive, simulation, video diffusion, world model  
- **[GAD: Geometry Attention Distillation for Consistent Video Generation](https://arxiv.org/abs/2610.18779v1)**  
  Authors: Junfeng Ni, Ziyu Zhu, Fan Jiang, Yu Liu, Chiyu Wang, Jiawei Zhang, Zhaoxu Sun, Mu Xu, Siyuan Huang, Yixin Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.18779v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://fantasy-amap.github.io/GAD)  
  Keywords: distillation, efficient, simulation, temporal consistency, video diffusion, video generation, world simulation  



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
