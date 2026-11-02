# Awesome Video Diffusions [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Video Diffusion Models and Video Generation. Content is automatically updated daily.

🗺️ **[Explore the Paper Atlas](https://longxiang-ai.github.io/awesome-video-diffusions/)**: an interactive paper map, monthly trends, topic network, co-author network and author rankings of every tracked paper.

> Last Update: 2026-11-02 04:43:27

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

- [3D-aware Video Generation](#3d-aware-video-generation) (55 papers) - Video generation with 3D awareness, multi-view consistency, and 4D content creation
- [Applications](#applications) (201 papers) - Domain-specific applications of video diffusion models
- [Architecture & Efficiency](#architecture-&-efficiency) (393 papers) - Architectural innovations (DiT, UNet), flow matching, and training/inference efficiency
- [Audio & Multi-modal](#audio-&-multi-modal) (63 papers) - Audio-driven and multi-modal conditioned video generation
- [Controllable Generation](#controllable-generation) (320 papers) - Controllable video generation with motion, camera, pose, or layout guidance
- [Human & Character Animation](#human-&-character-animation) (53 papers) - Human-centric video generation including talking heads, dance, and character animation
- [Image-to-Video Generation](#image-to-video-generation) (94 papers) - Methods for animating still images into videos
- [Long Video Generation](#long-video-generation) (245 papers) - Generating temporally consistent long-form videos beyond short clips
- [Personalization & Customization](#personalization-&-customization) (152 papers) - Personalized video generation with custom subjects, identities, or styles
- [Physical Understanding](#physical-understanding) (288 papers) - Physics-aware video generation and dynamics modeling
- [Surveys & Benchmarks](#surveys-&-benchmarks) (319 papers) - Survey papers, benchmarks, and evaluation metrics for video generation
- [Text-to-Video Generation](#text-to-video-generation) (140 papers) - Foundation models and methods for generating videos from text prompts
- [Video Editing](#video-editing) (90 papers) - Diffusion-based video editing, style transfer, and manipulation
- [Video Inpainting & Completion](#video-inpainting-&-completion) (23 papers) - Video inpainting, completion, outpainting, and temporal prediction
- [Video Super-Resolution & Enhancement](#video-super-resolution-&-enhancement) (181 papers) - Video quality improvement, upscaling, restoration, and frame interpolation
- [World Models & Simulation](#world-models-&-simulation) (241 papers) - Video generation as world simulators and interactive environment generation



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3D-aware Video Generation

*Showing the latest 50 out of 55 papers*

- **[LucidLyra: Feed-Forward Generative 3D Scene Reconstruction and Joint Understanding via Multi-Task Distillation](https://arxiv.org/abs/2610.40495v1)**  
  Authors: Oliver Hahn, Rodrigo Marcuzzi, Sangeetha Grama Srinivasan, Alessandro Burzio, Sherwin Bahmani, Jiahui Huang, Stefan Roth, Shengyu Huang, Qunjie Zhou, Laura Leal-Taixé  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.40495v1.pdf)  
  Keywords: diffusion model, distillation, dynamic 3d, novel view, physical, robotics, simulation, video diffusion  
- **[Hierarchical Diffusion for Camera-controlled Autoregressive Video Generation](https://arxiv.org/abs/2610.37983v1)**  
  Authors: Kaihua Chen, Yiming Gong, Deva Ramanan, Tarasha Khurana  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.37983v1.pdf)  
  Keywords: autoregressive, autoregressive video, camera control, denoising, long video, novel view, video generation  
- **[GroundControl: Satellite-Conditioned Multi-View Diffusion for Reconstruction-Free Novel View Synthesis](https://arxiv.org/abs/2610.37545v1)**  
  Authors: Akshay Krishnan, Matias Turkulainen, Jamie Wynn, Zawar Qureshi, Mohamed Sayed, Guillermo Garcia-Hernando, Sara Vicente, James Hays, Michael Firman, Daniyar Turmukhambetov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.37545v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://nianticspatial.github.io/groundcontrol)  
  Keywords: diffusion model, layout, novel view, video diffusion  
- **[SyncVid: World-Equivariant Diffusion for Synchronized Video Generation](https://arxiv.org/abs/2610.31765v1)**  
  Authors: Farhad G. Zanjani, Animesh Karnewar, Fatih Porikli, Amirhossein Habibian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.31765v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://qualcomm-ai-research.github.io/SyncVid-Webpage)  
  Keywords: camera control, diffusion model, video diffusion, video generation, view-consistent  
- **[AudioLift: Audio-Driven Single Image to Full-Head Gaussian Avatar via Multi-view Video Generation](https://arxiv.org/abs/2610.31747v1)**  
  Authors: Zhuoyuan Jiang, Weijie Lyu, Xiaoyuan Wang, Tiancheng Shen, Ming-Hsuan Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.31747v1.pdf)  
  Keywords: audio-driven, audio-driven avatar, avatar, multi-view video, multi-view video generation, talking avatar, video generation  
- **[Learning the 4D World through Point Trajectory Forecasting](https://arxiv.org/abs/2610.28594v1)**  
  Authors: Byungwoo Jeon, Sunghwan Hong, Dohyeon Kim, Jonghoon Lee, Jungwoo Park, Inhee Lee, Doosan Baek, Jinil Kim, Taehyun Lim, Hanbyul Joo, Marc Pollefeys, Saining Xie, Jinwoo Shin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.28594v1.pdf)  
  Keywords: 3d-aware, 4d generation, benchmark, camera-conditioned, evaluation, multi-view video, physical, point trajectory, simulation, trajectory, video generation, world model  
- **[Mise-en-Video: Fine-Grained 3D Control for Multi-Shot Video Generation](https://arxiv.org/abs/2610.26801v1)**  
  Authors: Yingshuang Zou, Xiaoyu Shi, Yawen Luo, Ziang Li, Qinghe Wang, Mengfei Li, Chengfeng Zhao, Xintao Wang, Pengfei Wan, Kun Gai, Yuan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.26801v1.pdf)  
  Keywords: 3d-aware, controllable, evaluation, layout, text to video, text-to-video, video generation  
- **[HORIA: 4D Human and Object Reconstruction from a Monocular Video with Interaction-Aware Re-Rendering](https://arxiv.org/abs/2610.25960v2)**  
  Authors: Hyeongjin Nam, Taeryung Lee, Daniel Sungho Jung, Kyoung Mu Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.25960v2.pdf)  
  Keywords: novel view, text to video, text-to-video, video diffusion  
- **[Holo4D: Holistic 4D Reconstruction as Geometric Control for Video Diffusion](https://arxiv.org/abs/2610.25276v1)**  
  Authors: Yushi Lan, Zeren Jiang, Koichi Namekata, Xingang Pan, Chuanxia Zheng, Andrea Vedaldi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.25276v1.pdf)  
  Keywords: camera control, camera trajectory, diffusion model, novel view, trajectory, video diffusion  
- **[GeoART: Geometry-Aware Refinement via Test-Time Scaling for Camera-Conditioned Video Diffusion](https://arxiv.org/abs/2610.25273v1)**  
  Authors: Liudi Yang, Ziyuan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.25273v1.pdf)  
  Keywords: camera control, camera-conditioned, denoising, diffusion model, trajectory, video diffusion  

### Applications

*Showing the latest 50 out of 201 papers*

- **[MotorSense: A Video-EMG Dataset of Motoric Representations for Action Understanding](https://arxiv.org/abs/2610.41127v1)**  
  Authors: Eadom Dessalene, Michael Maynord, Amir-Hossein Shahidzadeh, Botao He, Yasamin Tabatabaee, Ruoshi Liu, Ruohan Gao, Paul Pu Liang, Yiannis Aloimonos  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.41127v1.pdf)  
  Keywords: diffusion model, embodied, video diffusion  
- **[LucidLyra: Feed-Forward Generative 3D Scene Reconstruction and Joint Understanding via Multi-Task Distillation](https://arxiv.org/abs/2610.40495v1)**  
  Authors: Oliver Hahn, Rodrigo Marcuzzi, Sangeetha Grama Srinivasan, Alessandro Burzio, Sherwin Bahmani, Jiahui Huang, Stefan Roth, Shengyu Huang, Qunjie Zhou, Laura Leal-Taixé  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.40495v1.pdf)  
  Keywords: diffusion model, distillation, dynamic 3d, novel view, physical, robotics, simulation, video diffusion  
- **[Wizard: Manipulate Any World in Real Time via Agentic Control](https://arxiv.org/abs/2610.40339v1)**  
  Authors: Yuzhe Wu, Zijun Lin, Yeying Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.40339v1.pdf)  
  Keywords: controllable, game, interactive, simulation, video generation, world model, world simulation  
- **[Video Generation Meets Agent Harness: Agentic Video Generation, Agentic World Modeling and Recursive Self-Improvement](https://arxiv.org/abs/2610.40191v1)**  
  Authors: Liaoyuan Fan, Yuhao Zheng, Dongxing Mao, Hangyu Ran, Siyuan Hu, Weijia Mao, Rui Zhao, Weijia Wu, Guian Fang, Yanzhe Chen, Zeyu Zhu, Yuxin Jiang, Yiren Song, Yuchao Gu, Junchao Yi, Qi Hu, Dan Kong, Alex Jinpeng Wang, Kevin Qinghong Lin, Mike Zheng Shou, Wei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.40191v1.pdf)  
  Keywords: action-conditioned, controllable, evaluation, game, interactive, video generation  
- **[Seeing and Imagining as One: Unified Video Generation and 4D Perception for Embodied World Modeling](https://arxiv.org/abs/2610.39232v2)**  
  Authors: Haitang Feng, Zhuoman Liu, Zhennan Wang, Sheng Wang, Juelin Li, Chengzhi Zhao, Hexiang Wei, Lin Shao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.39232v2.pdf)  
  Keywords: architecture, diffusion transformer, dit, embodied, embodied world model, video diffusion, video diffusion transformer, video generation, world model  
- **[StreamStudio: Exploring Video Authoring with Streaming Autoregressive Generation](https://arxiv.org/abs/2610.38467v1)**  
  Authors: Boyu Li, Zhe Lin, Eli Shechtman, Ding Li, Hongbo Fu, Yuqian Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.38467v1.pdf)  
  Keywords: autoregressive, controllable, creative, streaming, streaming video generation, video generation  
- **[PDRVLA: A Vision-Language-Action Model with Physical Dynamics Representations](https://arxiv.org/abs/2610.37381v2)**  
  Authors: Hanqing Wang, Zhaotian Cai, Ruichuan An, Bohan Zeng, Tao Zhang, Yilin Chen, Xu Jiang, Kaiquan Chen, Chongyang Wu, Haoran Li, Fan Yang, Mingan Lin, Wentao Zhang, Zenan Zhou, Youzheng Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.37381v2.pdf)  
  Keywords: dynamics, embodied, physical, simulation, video generation, video world model, world model  
- **[VibeVideoBench: Evaluating Multimodal Agents on Code-Driven Video Generation](https://arxiv.org/abs/2610.35864v2)**  
  Authors: Muxi Diao, Wenbin Xu, Lele Yang, Xuyang Ma, Yuzhe Chen, Jiankang Chen, Kaiyu Jiang, Changyi Liu, Haoyu Zhang, Hongyi Fu, Jianxiong Wang, Tianke Zhang, Haonan Fan, Yingxin Li, Bingyi Li, Xu Wang, Xuanyu Zheng, Bin Wen, Tingting Gao, Han Li, Wentao Zhang, Weiran Xu, Kongming Liang, Zhanyu Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.35864v2.pdf)  
  Keywords: benchmark, evaluation, game, sound, video generation  
- **[WorldCast: World-Consistent Character Video Generation with Large-Angle Camera Control](https://arxiv.org/abs/2610.33135v1)**  
  Authors: Lei Cao, Yu Liu, Wenhua Liao, Peng Zhang, Fei Wang, Hao Zhang, Jiajun Le, Daiguo Zhou, Jian Luan, Jiayi Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.33135v1.pdf)  
  Keywords: benchmark, camera control, camera trajectory, cinematic, evaluation, identity, trajectory, video generation  
- **[AnyGameRenderer: Entity-Consistent Generative Rendering Across Games and an Entity-Level Benchmark](https://arxiv.org/abs/2610.31466v3)**  
  Authors: Ruicong Liu, Liangyang Ouyang, Fengbo Lan, Zhixiang Wang, Kaipeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.31466v3.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://alaya-lab.github.io/AnyGameRenderer)  
  Keywords: benchmark, game, layout, video generation, video to video, video-to-video  

### Architecture & Efficiency

*Showing the latest 50 out of 393 papers*

- **[A Better Critic Matters for Distribution Matching Distillation](https://arxiv.org/abs/2610.42135v1)**  
  Authors: Zongze Wu, Xianbang Wang, Zhengyang Geng, Mingdeng Cao, Zhoutong Zhang, Richard Zhang, Eli Shechtman, Ruiming Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.42135v1.pdf)  
  Keywords: distillation, text to video, text-to-video, video generation  
- **[Any Forcing: Any-Step Generality and One-Step Stability for Autoregressive Video Generation](https://arxiv.org/abs/2610.42031v1)**  
  Authors: Jiahua Xu, Yijie Fang, Nannan Wang, Xunhao Lin, Li Cao, Lei Hao, Mingrui Zhu, Fei Gao, Xinbo Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.42031v1.pdf)  
  Keywords: autoregressive, autoregressive video, efficient, long video, streaming, video generation  
- **[L3G-World: Real-Time Infinite World Generation with Latent 3D Gaussian Memory](https://arxiv.org/abs/2610.40614v1)**  
  Authors: Jinhyeok Choi, JoungBin Lee, Jongmin Lee, Minkyeong Jeon, Jiyoung Kim, Kaeun Han, Yoonjin Yoon, Seungryong Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.40614v1.pdf)  
  Keywords: diffusion transformer, dit, efficient, interactive, latent video, video diffusion, video diffusion transformer  
- **[LucidLyra: Feed-Forward Generative 3D Scene Reconstruction and Joint Understanding via Multi-Task Distillation](https://arxiv.org/abs/2610.40495v1)**  
  Authors: Oliver Hahn, Rodrigo Marcuzzi, Sangeetha Grama Srinivasan, Alessandro Burzio, Sherwin Bahmani, Jiahui Huang, Stefan Roth, Shengyu Huang, Qunjie Zhou, Laura Leal-Taixé  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.40495v1.pdf)  
  Keywords: diffusion model, distillation, dynamic 3d, novel view, physical, robotics, simulation, video diffusion  
- **[AB-Attention: Accurate Block Attention for Accelerating Video Diffusion Transformers](https://arxiv.org/abs/2610.39663v1)**  
  Authors: Bin Xu, Mo Zhang, Zhengfeiyang Zhang, Xinfeng Yang, Yixing Ma, Wei Wang, HeXin Wang, Pengfei Zhou, Wangbo Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.39663v1.pdf) | [![GitHub](https://img.shields.io/github/stars/InfRec-Cardinal/AB-Attention?style=social)](https://github.com/InfRec-Cardinal/AB-Attention)  
  Keywords: sparse attention, video diffusion  
- **[Regional Anchor Routing for Multi-Object Motion Transfer](https://arxiv.org/abs/2610.39478v1)**  
  Authors: Yuze Li, Fuchen Long, Xinlong Sun, Cheng Yan, Xinyu Zhang, Xi Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.39478v1.pdf)  
  Keywords: denoising, diffusion transformer, efficient, motion transfer, video diffusion, video diffusion transformer  
- **[Seeing and Imagining as One: Unified Video Generation and 4D Perception for Embodied World Modeling](https://arxiv.org/abs/2610.39232v2)**  
  Authors: Haitang Feng, Zhuoman Liu, Zhennan Wang, Sheng Wang, Juelin Li, Chengzhi Zhao, Hexiang Wei, Lin Shao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.39232v2.pdf)  
  Keywords: architecture, diffusion transformer, dit, embodied, embodied world model, video diffusion, video diffusion transformer, video generation, world model  
- **[Repurposing Video Diffusion Transformers for Cross-View Temporal Object Correspondence](https://arxiv.org/abs/2610.37633v1)**  
  Authors: Siyoon Jin, Dahyun Chung, Honggyu An, Sangbeom Lim, Wonjin Nam, Jaewoo Jung, WonJun Moon, Seungryong Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.37633v1.pdf)  
  Keywords: dit, identity, temporal consistency, video diffusion, video dit  
- **[A First-Step Bias Restores Lost Diversity in Diffusion Model Distillation](https://arxiv.org/abs/2610.37110v1)**  
  Authors: Wenwu Tang, Dong Wang, Yun Cheng, Olga Saukh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.37110v1.pdf)  
  Keywords: denoising, diffusion model, distillation, efficient, t2v, text to video, text-to-video, trajectory  
- **[TAPESTRY: A Single Backbone for Video Generation and Robot Control](https://arxiv.org/abs/2610.36823v1)**  
  Authors: Jeremy A. Collins, Seungjae Lee, Rachanon Wachakorn, Krishnan Srinivasan, Animesh Garg, Vitor Campagnolo Guizilini, Paarth Shah  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.36823v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://tapestry-wam.github.io)  
  Keywords: diffusion transformer, dynamics, physical, simulation, video diffusion, video diffusion transformer, video generation  

### Audio & Multi-modal

*Showing the latest 50 out of 63 papers*

- **[VibeVideoBench: Evaluating Multimodal Agents on Code-Driven Video Generation](https://arxiv.org/abs/2610.35864v2)**  
  Authors: Muxi Diao, Wenbin Xu, Lele Yang, Xuyang Ma, Yuzhe Chen, Jiankang Chen, Kaiyu Jiang, Changyi Liu, Haoyu Zhang, Hongyi Fu, Jianxiong Wang, Tianke Zhang, Haonan Fan, Yingxin Li, Bingyi Li, Xu Wang, Xuanyu Zheng, Bin Wen, Tingting Gao, Han Li, Wentao Zhang, Weiran Xu, Kongming Liang, Zhanyu Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.35864v2.pdf)  
  Keywords: benchmark, evaluation, game, sound, video generation  
- **[AudioLift: Audio-Driven Single Image to Full-Head Gaussian Avatar via Multi-view Video Generation](https://arxiv.org/abs/2610.31747v1)**  
  Authors: Zhuoyuan Jiang, Weijie Lyu, Xiaoyuan Wang, Tiancheng Shen, Ming-Hsuan Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.31747v1.pdf)  
  Keywords: audio-driven, audio-driven avatar, avatar, multi-view video, multi-view video generation, talking avatar, video generation  
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

### Controllable Generation

*Showing the latest 50 out of 320 papers*

- **[Wizard: Manipulate Any World in Real Time via Agentic Control](https://arxiv.org/abs/2610.40339v1)**  
  Authors: Yuzhe Wu, Zijun Lin, Yeying Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.40339v1.pdf)  
  Keywords: controllable, game, interactive, simulation, video generation, world model, world simulation  
- **[Video Generation Meets Agent Harness: Agentic Video Generation, Agentic World Modeling and Recursive Self-Improvement](https://arxiv.org/abs/2610.40191v1)**  
  Authors: Liaoyuan Fan, Yuhao Zheng, Dongxing Mao, Hangyu Ran, Siyuan Hu, Weijia Mao, Rui Zhao, Weijia Wu, Guian Fang, Yanzhe Chen, Zeyu Zhu, Yuxin Jiang, Yiren Song, Yuchao Gu, Junchao Yi, Qi Hu, Dan Kong, Alex Jinpeng Wang, Kevin Qinghong Lin, Mike Zheng Shou, Wei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.40191v1.pdf)  
  Keywords: action-conditioned, controllable, evaluation, game, interactive, video generation  
- **[FutureWorld: A Plug-and-Play Causal Next-State Predictor for Interactive Video World Exploration](https://arxiv.org/abs/2610.39619v1)**  
  Authors: Guangyuan Li, Kelu Yao, Shuolin Xu, Xinlei Yu, Wei Xing, Lei Zhao, Peng-Tao Jiang, Xiaogang Xu, Xiaobin Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.39619v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://GuangYuanKK.github.io/futureworld)  
  Keywords: action-conditioned, interactive, long video, video generation  
- **[Edited Endpoints as Partial Goals for Image-to-Video Generation](https://arxiv.org/abs/2610.39179v1)**  
  Authors: Sihyun Kim, Sanghyun Jo, Kyungsu Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.39179v1.pdf) | [![GitHub](https://img.shields.io/github/stars/wannagetacat/Edited-Endpoints-I2V?style=social)](https://github.com/wannagetacat/Edited-Endpoints-I2V)  
  Keywords: i2v, image to video, image-to-video, layout, video generation  
- **[StreamStudio: Exploring Video Authoring with Streaming Autoregressive Generation](https://arxiv.org/abs/2610.38467v1)**  
  Authors: Boyu Li, Zhe Lin, Eli Shechtman, Ding Li, Hongbo Fu, Yuqian Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.38467v1.pdf)  
  Keywords: autoregressive, controllable, creative, streaming, streaming video generation, video generation  
- **[Hierarchical Diffusion for Camera-controlled Autoregressive Video Generation](https://arxiv.org/abs/2610.37983v1)**  
  Authors: Kaihua Chen, Yiming Gong, Deva Ramanan, Tarasha Khurana  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.37983v1.pdf)  
  Keywords: autoregressive, autoregressive video, camera control, denoising, long video, novel view, video generation  
- **[GroundControl: Satellite-Conditioned Multi-View Diffusion for Reconstruction-Free Novel View Synthesis](https://arxiv.org/abs/2610.37545v1)**  
  Authors: Akshay Krishnan, Matias Turkulainen, Jamie Wynn, Zawar Qureshi, Mohamed Sayed, Guillermo Garcia-Hernando, Sara Vicente, James Hays, Michael Firman, Daniyar Turmukhambetov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.37545v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://nianticspatial.github.io/groundcontrol)  
  Keywords: diffusion model, layout, novel view, video diffusion  
- **[Taming Noise Initialization for Zero-shot Video Restoration with Image Diffusion Priors](https://arxiv.org/abs/2610.37290v1)**  
  Authors: Chong Wang, Zixuan Fu, Hao Cheng, Siyuan Yang, Alex C. Kot, Bihan Wen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.37290v1.pdf)  
  Keywords: diffusion model, temporal consistency, trajectory, video diffusion, video restoration  
- **[A First-Step Bias Restores Lost Diversity in Diffusion Model Distillation](https://arxiv.org/abs/2610.37110v1)**  
  Authors: Wenwu Tang, Dong Wang, Yun Cheng, Olga Saukh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.37110v1.pdf)  
  Keywords: denoising, diffusion model, distillation, efficient, t2v, text to video, text-to-video, trajectory  
- **[GAWM: A Compact Latent World-Action Model for Multi-Task Robot Manipulation](https://arxiv.org/abs/2610.37091v1)**  
  Authors: Yang Liu, Xiaoli Liu, Liuzhao Li, Yuduo Song, Muyuan Liu, Xiang Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.37091v1.pdf) | [![GitHub](https://img.shields.io/github/stars/gaoxiang12/ga-wm?style=social)](https://github.com/gaoxiang12/ga-wm)  
  Keywords: layout, video generation, world model  

### Human & Character Animation

*Showing the latest 50 out of 53 papers*

- **[Regional Anchor Routing for Multi-Object Motion Transfer](https://arxiv.org/abs/2610.39478v1)**  
  Authors: Yuze Li, Fuchen Long, Xinlong Sun, Cheng Yan, Xinyu Zhang, Xi Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.39478v1.pdf)  
  Keywords: denoising, diffusion transformer, efficient, motion transfer, video diffusion, video diffusion transformer  
- **[ViT-H: Generative Video-To-Humanoid Control with Motion Tracking Feedback](https://arxiv.org/abs/2610.32966v1)**  
  Authors: Zimo He, Tianyi Bian, Zizhong Yang, Hongjie Li, Nan Jiang, Jieming Cui, Baoxiong Jia, Yizhou Wang, Siyuan Huang, Yixin Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.32966v1.pdf)  
  Keywords: autoregressive, diffusion model, human motion  
- **[AudioLift: Audio-Driven Single Image to Full-Head Gaussian Avatar via Multi-view Video Generation](https://arxiv.org/abs/2610.31747v1)**  
  Authors: Zhuoyuan Jiang, Weijie Lyu, Xiaoyuan Wang, Tiancheng Shen, Ming-Hsuan Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.31747v1.pdf)  
  Keywords: audio-driven, audio-driven avatar, avatar, multi-view video, multi-view video generation, talking avatar, video generation  
- **[StreamEval: Evaluating Interactive Streaming Video Generation Models](https://arxiv.org/abs/2610.28402v3)**  
  Authors: StreamEval Team  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.28402v3.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://streameval.ai)  
  Keywords: avatar, benchmark, evaluation, identity, interactive, leaderboard, streaming, streaming video generation, video generation  
- **[Decoupling Action from Egocentric Observation for World Simulation](https://arxiv.org/abs/2610.27946v1)**  
  Authors: Yue Ma, Pengjie Song, Xinyu Wang, Yi He, Zeqian Long, Fangneng Zhan, Kaichen Zhou, Hongyu Liu, Hongfa Wang, Peihao Li, Haoyang Huang, Nan Duan, Qifeng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.27946v1.pdf)  
  Keywords: benchmark, denoising, dynamics, embodied, layout, motion transfer, simulation, video diffusion, video generation, world simulation  
- **[MotionShift: Environment-Compatible Motion Transfer via Planner-Evaluator Synergistic Adaptation](https://arxiv.org/abs/2610.25290v1)**  
  Authors: Yanchen Liu, Junyao Gao, Yanan Sun, Wensheng Chen, Guangming Lu, Wenjie Pei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.25290v1.pdf)  
  Keywords: i2v, image to video, image-to-video, motion transfer, physical, trajectory  
- **[DreamHMR: From Video Generation to Human Motion Modeling via Structural Focusing](https://arxiv.org/abs/2610.20124v1)**  
  Authors: Zhengjie Xu, Ruihao Gong, Xianglong Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.20124v1.pdf)  
  Keywords: body motion, evaluation, human motion, video generation  
- **[Time-JEPA: Grounding Video World Models with Physical Time Series](https://arxiv.org/abs/2610.23982v1)**  
  Authors: Shenyi Li, Ziyang Zhang, Wen Wu, Ming Liu, Chao Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.23982v1.pdf)  
  Keywords: autonomous driving, driving, human motion, physical, video world model, world model  
- **[Kandinsky S2V 1.0: Audio-Driven Avatar Video Generation](https://arxiv.org/abs/2610.19290v1)**  
  Authors: Nikolay Semenov, Artem Riabinin, Sergey Bassenko, Anna Averchenkova, Julia Agafonova, Anastasia Aliaskina, Kirill Kozlov, Lev Novitskiy, Nikita Samsonov, Nikolai Gerasimenko, Denis Dimitrov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.19290v1.pdf)  
  Keywords: architecture, audio-driven, audio-driven avatar, avatar, benchmark, controllable, evaluation, gesture, human animation, human evaluation, long-form, speech-to-video, video generation  
- **[VGGA: Geometry-Grounded Autoencoder for Video Generation](https://arxiv.org/abs/2610.16204v1)**  
  Authors: Chaofan Gan, Yian Zhao, Shijie Li, Tieyuan Chen, Zicheng Zhao, Mehrtash Harandi, Weiyao Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.16204v1.pdf)  
  Keywords: dynamic 3d, human motion, latent video, video autoencoder, video generation  

### Image-to-Video Generation

*Showing the latest 50 out of 94 papers*

- **[GeoFlip: Benchmarking Geometry-Sensitive Physics in Video Generation](https://arxiv.org/abs/2610.42002v1)**  
  Authors: Yuqi Li, Junming Liu, Bowen Hu, Ruize Niu, Huiran Duan, Yingli Tian, Hao Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.42002v1.pdf)  
  Keywords: benchmark, evaluation, image to video, image-to-video, physical, physical consistency, physics, simulation, video generation  
- **[MorphSIG: Subject-Driven Image Generation via Decoupled Anchoring and Feature Transport](https://arxiv.org/abs/2610.39530v1)**  
  Authors: Hailong Yan, Yongrui Zhang, Xiangtao Zhang, Le Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.39530v1.pdf)  
  Keywords: benchmark, denoising, identity, image to video, image-to-video, subject-driven  
- **[Edited Endpoints as Partial Goals for Image-to-Video Generation](https://arxiv.org/abs/2610.39179v1)**  
  Authors: Sihyun Kim, Sanghyun Jo, Kyungsu Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.39179v1.pdf) | [![GitHub](https://img.shields.io/github/stars/wannagetacat/Edited-Endpoints-I2V?style=social)](https://github.com/wannagetacat/Edited-Endpoints-I2V)  
  Keywords: i2v, image to video, image-to-video, layout, video generation  
- **[Mix Forcing: Causal Pre-Training via Mixture Attention for Interactive World Models](https://arxiv.org/abs/2610.33589v1)**  
  Authors: Zelin Gao, Hao Ouyang, Jiapeng Zhu, Qiuyu Wang, Jingye Chen, Zichen Liu, Xing Zhu, Yujun Shen, Yinghao Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.33589v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zelingao98.github.io/mixforcing)  
  Keywords: autoregressive, benchmark, camera control, diffusion model, distillation, image to video, image-to-video, interactive, video diffusion  
- **[AEON: Unifying Video and 3D World Models](https://arxiv.org/abs/2610.28631v1)**  
  Authors: Weiqi Zhang, Wenyuan Zhang, Yu-Shen Liu, Junsheng Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.28631v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://weiqi-zhang.github.io/AEON)  
  Keywords: distillation, dynamics, image-conditioned video, simulation, world simulation  
- **[Latent Bridge: From Video Latents to 3D Geometry via Feature Alignment](https://arxiv.org/abs/2610.28521v1)**  
  Authors: Shuai Zhang, Zhanpeng Ouyang, Zhengqing Chen, Ruohong Mei, Shaoyu Chen, Weiqiang Ren, Hui Sun, Qian Zhang, Wenyu Liu, Xinggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.28521v1.pdf) | [![GitHub](https://img.shields.io/github/stars/hustvl/Latent-Bridge?style=social)](https://github.com/hustvl/Latent-Bridge)  
  Keywords: distillation, efficient, image to video, image-to-video, text to video, text-to-video, video generation  
- **[Code2Video-Compass: A Comprehensive Benchmark for General-Purpose Code-Based Video Generation across T2V, I2V, and V2V](https://arxiv.org/abs/2610.28416v1)**  
  Authors: Zhenghan Chen, Zekai Shao, Xin Lin, Leting Cheng, Siming Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.28416v1.pdf)  
  Keywords: benchmark, controllable, creative, evaluation, i2v, image to video, image-to-video, t2v, text to video, text-to-video, v2v, video generation, video to video, video-to-video  
- **[PhaseBreak: Proactive Temporal Protection against Unauthorized Image-to-Video Animation](https://arxiv.org/abs/2610.33070v1)**  
  Authors: Jiashu Zhang, Xuanyou Li, Qixin Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.33070v1.pdf)  
  Keywords: customization, dynamics, i2v, image to video, image-to-video, video diffusion  
- **[PVBench: Quantifying Physical Plausibility in Video Generation with Object-Level Physical Measurements](https://arxiv.org/abs/2610.26711v1)**  
  Authors: Kaiwei Chen, Moran Li, Zhenye Gan, Yabiao Wang, Chengjie Wang, Kexin Zhang, Yong Liu, Jiangning Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.26711v1.pdf)  
  Keywords: benchmark, dynamics, embodied, evaluation, human evaluation, image to video, image-to-video, physical, physical plausibility, text to video, text-to-video, video generation  
- **[Wan-Alpha++: Animating a Single RGBA Asset into Controllable Transparent Video Effects](https://arxiv.org/abs/2610.26189v1)**  
  Authors: Haotian Dong, Xin Wang, Wenjing Wang, Chen Li, Jing Lyu, Yan Tina Luximon, Ping Li, Wanchao Su, Ke Xu, Di Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.26189v1.pdf)  
  Keywords: controllable, game, image to video, image-to-video, video diffusion, video generation  

### Long Video Generation

*Showing the latest 50 out of 245 papers*

- **[Any Forcing: Any-Step Generality and One-Step Stability for Autoregressive Video Generation](https://arxiv.org/abs/2610.42031v1)**  
  Authors: Jiahua Xu, Yijie Fang, Nannan Wang, Xunhao Lin, Li Cao, Lei Hao, Mingrui Zhu, Fei Gao, Xinbo Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.42031v1.pdf)  
  Keywords: autoregressive, autoregressive video, efficient, long video, streaming, video generation  
- **[FutureWorld: A Plug-and-Play Causal Next-State Predictor for Interactive Video World Exploration](https://arxiv.org/abs/2610.39619v1)**  
  Authors: Guangyuan Li, Kelu Yao, Shuolin Xu, Xinlei Yu, Wei Xing, Lei Zhao, Peng-Tao Jiang, Xiaogang Xu, Xiaobin Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.39619v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://GuangYuanKK.github.io/futureworld)  
  Keywords: action-conditioned, interactive, long video, video generation  
- **[StreamStudio: Exploring Video Authoring with Streaming Autoregressive Generation](https://arxiv.org/abs/2610.38467v1)**  
  Authors: Boyu Li, Zhe Lin, Eli Shechtman, Ding Li, Hongbo Fu, Yuqian Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.38467v1.pdf)  
  Keywords: autoregressive, controllable, creative, streaming, streaming video generation, video generation  
- **[Hierarchical Diffusion for Camera-controlled Autoregressive Video Generation](https://arxiv.org/abs/2610.37983v1)**  
  Authors: Kaihua Chen, Yiming Gong, Deva Ramanan, Tarasha Khurana  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.37983v1.pdf)  
  Keywords: autoregressive, autoregressive video, camera control, denoising, long video, novel view, video generation  
- **[Repurposing Video Diffusion Transformers for Cross-View Temporal Object Correspondence](https://arxiv.org/abs/2610.37633v1)**  
  Authors: Siyoon Jin, Dahyun Chung, Honggyu An, Sangbeom Lim, Wonjin Nam, Jaewoo Jung, WonJun Moon, Seungryong Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.37633v1.pdf)  
  Keywords: dit, identity, temporal consistency, video diffusion, video dit  
- **[ReferStream: Interactive Subject Injection for Streaming Video Generation](https://arxiv.org/abs/2610.37566v1)**  
  Authors: Shuolin Xu, Guanyuan Li, Boyu Li, Kelu Yao, Xiaogang Xu, Hongchuan Yu, Shuicheng Yan, Xiaobin Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.37566v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xushuolin.github.io/ReferStream)  
  Keywords: benchmark, evaluation, interactive, streaming, streaming video generation, video generation  
- **[Taming Noise Initialization for Zero-shot Video Restoration with Image Diffusion Priors](https://arxiv.org/abs/2610.37290v1)**  
  Authors: Chong Wang, Zixuan Fu, Hao Cheng, Siyuan Yang, Alex C. Kot, Bihan Wen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.37290v1.pdf)  
  Keywords: diffusion model, temporal consistency, trajectory, video diffusion, video restoration  
- **[More Memory, Better Videos? A Controlled Study of Visual Memory in Long-Video Generation](https://arxiv.org/abs/2610.35001v1)**  
  Authors: Yuzhuo Chen, Huafeng Shi, Xinyu Wang, Yulong Xu, Yucheng Wang, Haoqin Hong, Guoxin Zhang, Zehua Ma, Weiming Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.35001v1.pdf)  
  Keywords: identity, long video, video generation  
- **[Learning the Autoregressive: Direct Score-Difference Estimation with Amortized Future Credit for Video Distillation](https://arxiv.org/abs/2610.34092v1)**  
  Authors: Zixuan Duan, Yabo Chen, Xunzhi Xiang, Xin Zhang, Haibin Huang, Yin Chen, Chi Zhang, Qi Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.34092v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://scdzx.github.io/Leta)  
  Keywords: autoregressive, denoising, distillation, video generation  
- **[Mix Forcing: Causal Pre-Training via Mixture Attention for Interactive World Models](https://arxiv.org/abs/2610.33589v1)**  
  Authors: Zelin Gao, Hao Ouyang, Jiapeng Zhu, Qiuyu Wang, Jingye Chen, Zichen Liu, Xing Zhu, Yujun Shen, Yinghao Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.33589v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zelingao98.github.io/mixforcing)  
  Keywords: autoregressive, benchmark, camera control, diffusion model, distillation, image to video, image-to-video, interactive, video diffusion  

### Personalization & Customization

*Showing the latest 50 out of 152 papers*

- **[TADP: Dual-Branch Temporally Adaptive Differential Privacy for Expression-Aware Video Anonymization](https://arxiv.org/abs/2610.41642v1)**  
  Authors: Feng Xu, Xun Li, Lars Petersson, Yulei Sui, David Ahmedt-Aristizabal, Dadong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.41642v1.pdf)  
  Keywords: identity, video generation  
- **[MorphSIG: Subject-Driven Image Generation via Decoupled Anchoring and Feature Transport](https://arxiv.org/abs/2610.39530v1)**  
  Authors: Hailong Yan, Yongrui Zhang, Xiangtao Zhang, Le Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.39530v1.pdf)  
  Keywords: benchmark, denoising, identity, image to video, image-to-video, subject-driven  
- **[Repurposing Video Diffusion Transformers for Cross-View Temporal Object Correspondence](https://arxiv.org/abs/2610.37633v1)**  
  Authors: Siyoon Jin, Dahyun Chung, Honggyu An, Sangbeom Lim, Wonjin Nam, Jaewoo Jung, WonJun Moon, Seungryong Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.37633v1.pdf)  
  Keywords: dit, identity, temporal consistency, video diffusion, video dit  
- **[RynnWorld-Latent: A Cross-Embodiment World Model Conditioned on Universal Latent Actions](https://arxiv.org/abs/2610.36791v1)**  
  Authors: Haoyu Zhao, Yinzhou Tang, Zixuan Wang, Minghao Zhu, Dongchi Huang, Xingyue Zhao, Qin Zhao, Kehan Li, Siteng Huang, Xin Li, Zhenyu Zeng, Mingxiu Chen, Deli Zhao, Zhongyu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.36791v1.pdf)  
  Keywords: controllable, dynamics, identity, simulation, video prediction, video world model, world model  
- **[OmniShowcase: Omnidirectional Subject-Consistent Video Generation from Multi-View Images](https://arxiv.org/abs/2610.35684v1)**  
  Authors: Junyeong Ahn, Geonwoo Kim, Kinam Kim, Gihwi Kim, Hoonjin Jung, Hyojin Jang, Jaegul Choo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.35684v1.pdf)  
  Keywords: evaluation, identity, trajectory, video generation  
- **[More Memory, Better Videos? A Controlled Study of Visual Memory in Long-Video Generation](https://arxiv.org/abs/2610.35001v1)**  
  Authors: Yuzhuo Chen, Huafeng Shi, Xinyu Wang, Yulong Xu, Yucheng Wang, Haoqin Hong, Guoxin Zhang, Zehua Ma, Weiming Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.35001v1.pdf)  
  Keywords: identity, long video, video generation  
- **[FlockWorld: Toward Population-Scale Multi-Agent Video World Models through Artificial Life Simulation](https://arxiv.org/abs/2610.34564v1)**  
  Authors: Meryem Koksal, Yunzhe Wang, Volkan Ustun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.34564v1.pdf)  
  Keywords: action-conditioned, diffusion transformer, flow matching, identity, simulation, video generation  
- **[WorldCast: World-Consistent Character Video Generation with Large-Angle Camera Control](https://arxiv.org/abs/2610.33135v1)**  
  Authors: Lei Cao, Yu Liu, Wenhua Liao, Peng Zhang, Fei Wang, Hao Zhang, Jiajun Le, Daiguo Zhou, Jian Luan, Jiayi Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.33135v1.pdf)  
  Keywords: benchmark, camera control, camera trajectory, cinematic, evaluation, identity, trajectory, video generation  
- **[Copyright Leakage Detection in AI Generated Videos](https://arxiv.org/abs/2610.28524v1)**  
  Authors: Shaif Chowdhury, Moshiur Rahman Tonmoy  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.28524v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Shaif95/video-cp-Leakage?style=social)](https://github.com/Shaif95/video-cp-Leakage) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zenodo.org/records/21386117)  
  Keywords: benchmark, concept, video generation  
- **[PhaseBreak: Proactive Temporal Protection against Unauthorized Image-to-Video Animation](https://arxiv.org/abs/2610.33070v1)**  
  Authors: Jiashu Zhang, Xuanyou Li, Qixin Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.33070v1.pdf)  
  Keywords: customization, dynamics, i2v, image to video, image-to-video, video diffusion  

### Physical Understanding

*Showing the latest 50 out of 288 papers*

- **[GeoFlip: Benchmarking Geometry-Sensitive Physics in Video Generation](https://arxiv.org/abs/2610.42002v1)**  
  Authors: Yuqi Li, Junming Liu, Bowen Hu, Ruize Niu, Huiran Duan, Yingli Tian, Hao Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.42002v1.pdf)  
  Keywords: benchmark, evaluation, image to video, image-to-video, physical, physical consistency, physics, simulation, video generation  
- **[GenDSR: Transferring Representations from Video Generation Models for Dynamic Spatial Reasoning](https://arxiv.org/abs/2610.41314v1)**  
  Authors: Ke Yang, Zhenyu Zhang, Jun Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.41314v1.pdf)  
  Keywords: dynamics, video generation  
- **[LucidLyra: Feed-Forward Generative 3D Scene Reconstruction and Joint Understanding via Multi-Task Distillation](https://arxiv.org/abs/2610.40495v1)**  
  Authors: Oliver Hahn, Rodrigo Marcuzzi, Sangeetha Grama Srinivasan, Alessandro Burzio, Sherwin Bahmani, Jiahui Huang, Stefan Roth, Shengyu Huang, Qunjie Zhou, Laura Leal-Taixé  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.40495v1.pdf)  
  Keywords: diffusion model, distillation, dynamic 3d, novel view, physical, robotics, simulation, video diffusion  
- **[Utility-WAM: Correcting Future-Induced Action Changes](https://arxiv.org/abs/2610.39367v1)**  
  Authors: Feihong Zhang, Xi Lin, Yulong Shi, Zuxing Lu, Yanghong Mei, Zhaopeng Gu, Tingyu Yuan, Zihao Liang, Yinuo Wang, Zhaowen Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.39367v1.pdf)  
  Keywords: benchmark, physical, video generation  
- **[PDRVLA: A Vision-Language-Action Model with Physical Dynamics Representations](https://arxiv.org/abs/2610.37381v2)**  
  Authors: Hanqing Wang, Zhaotian Cai, Ruichuan An, Bohan Zeng, Tao Zhang, Yilin Chen, Xu Jiang, Kaiquan Chen, Chongyang Wu, Haoran Li, Fan Yang, Mingan Lin, Wentao Zhang, Zenan Zhou, Youzheng Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.37381v2.pdf)  
  Keywords: dynamics, embodied, physical, simulation, video generation, video world model, world model  
- **[TAPESTRY: A Single Backbone for Video Generation and Robot Control](https://arxiv.org/abs/2610.36823v1)**  
  Authors: Jeremy A. Collins, Seungjae Lee, Rachanon Wachakorn, Krishnan Srinivasan, Animesh Garg, Vitor Campagnolo Guizilini, Paarth Shah  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.36823v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://tapestry-wam.github.io)  
  Keywords: diffusion transformer, dynamics, physical, simulation, video diffusion, video diffusion transformer, video generation  
- **[RynnWorld-Latent: A Cross-Embodiment World Model Conditioned on Universal Latent Actions](https://arxiv.org/abs/2610.36791v1)**  
  Authors: Haoyu Zhao, Yinzhou Tang, Zixuan Wang, Minghao Zhu, Dongchi Huang, Xingyue Zhao, Qin Zhao, Kehan Li, Siteng Huang, Xin Li, Zhenyu Zeng, Mingxiu Chen, Deli Zhao, Zhongyu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.36791v1.pdf)  
  Keywords: controllable, dynamics, identity, simulation, video prediction, video world model, world model  
- **[VidEdit3D: Flexible 3D Gaussian Editing with Video Diffusion](https://arxiv.org/abs/2610.35756v1)**  
  Authors: Yanming Yang, Chenxi Song, Tong Zhao, Juntao Xu, Wenhao Rao, Yiwen Chen, Yiwei Wang, Chi Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.35756v1.pdf)  
  Keywords: dynamics, trajectory, video diffusion, video editing  
- **[Beyond Distribution Matching: Self-Supervised Representation Forcing for Few-Step Video Generation](https://arxiv.org/abs/2610.35594v1)**  
  Authors: Junyi Chen, Haiyu Zhang, Zhoujie Fu, Tengfei Wang, Chunchao Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.35594v1.pdf)  
  Keywords: architecture, distillation, dynamics, video diffusion, video generation  
- **[Video World Models Need Predictable Latents](https://arxiv.org/abs/2610.34663v1)**  
  Authors: Mattia Scardecchia, Sherry Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.34663v1.pdf)  
  Keywords: architecture, dynamics, evaluation, physical  

### Surveys & Benchmarks

*Showing the latest 50 out of 319 papers*

- **[GeoFlip: Benchmarking Geometry-Sensitive Physics in Video Generation](https://arxiv.org/abs/2610.42002v1)**  
  Authors: Yuqi Li, Junming Liu, Bowen Hu, Ruize Niu, Huiran Duan, Yingli Tian, Hao Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.42002v1.pdf)  
  Keywords: benchmark, evaluation, image to video, image-to-video, physical, physical consistency, physics, simulation, video generation  
- **[Video Generation Meets Agent Harness: Agentic Video Generation, Agentic World Modeling and Recursive Self-Improvement](https://arxiv.org/abs/2610.40191v1)**  
  Authors: Liaoyuan Fan, Yuhao Zheng, Dongxing Mao, Hangyu Ran, Siyuan Hu, Weijia Mao, Rui Zhao, Weijia Wu, Guian Fang, Yanzhe Chen, Zeyu Zhu, Yuxin Jiang, Yiren Song, Yuchao Gu, Junchao Yi, Qi Hu, Dan Kong, Alex Jinpeng Wang, Kevin Qinghong Lin, Mike Zheng Shou, Wei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.40191v1.pdf)  
  Keywords: action-conditioned, controllable, evaluation, game, interactive, video generation  
- **[MorphSIG: Subject-Driven Image Generation via Decoupled Anchoring and Feature Transport](https://arxiv.org/abs/2610.39530v1)**  
  Authors: Hailong Yan, Yongrui Zhang, Xiangtao Zhang, Le Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.39530v1.pdf)  
  Keywords: benchmark, denoising, identity, image to video, image-to-video, subject-driven  
- **[Utility-WAM: Correcting Future-Induced Action Changes](https://arxiv.org/abs/2610.39367v1)**  
  Authors: Feihong Zhang, Xi Lin, Yulong Shi, Zuxing Lu, Yanghong Mei, Zhaopeng Gu, Tingyu Yuan, Zihao Liang, Yinuo Wang, Zhaowen Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.39367v1.pdf)  
  Keywords: benchmark, physical, video generation  
- **[MEV: A Multi-Event Video Dataset for Long-Take Generation](https://arxiv.org/abs/2610.38241v1)**  
  Authors: Peiyuan Zhu, Shaoan Xie, Yifan Shen, Wen Tian, Zijian Li, Guangyi Chen, Kun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.38241v1.pdf)  
  Keywords: evaluation, text to video, text-to-video, video generation  
- **[ReferStream: Interactive Subject Injection for Streaming Video Generation](https://arxiv.org/abs/2610.37566v1)**  
  Authors: Shuolin Xu, Guanyuan Li, Boyu Li, Kelu Yao, Xiaogang Xu, Hongchuan Yu, Shuicheng Yan, Xiaobin Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.37566v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xushuolin.github.io/ReferStream)  
  Keywords: benchmark, evaluation, interactive, streaming, streaming video generation, video generation  
- **[Hy-Nomas: Towards Free-form Interactive World Generation](https://arxiv.org/abs/2610.36729v1)**  
  Authors: Qiaoling Chen, Jiaxiang Cheng, Xueqing Deng, Tiankai Hang, Ji Hou, Jiaqi Li, Yifan Liu, Tao Lu, Junshu Tang, Yu Tang, Yao Teng, Yu Tian, Heng Wang, Weizhi Wang, Xiyao Wang, Xilun Wu, Mingyu Yang, Yangbin Yu, Rui Zhao, Longjun Cao, Linghao Chen, Haoyi Duan, Jiaming Han, Mingji Han, Enhua Jiang, Shunkai Li, Yanzhe Liang, Qinwei Ma, Cong Wang, Lei Wang, Bing Wu, Ke Xing, Ray Ying, Zhentao Yu, Key Zhang, Yuan Zhou, Zhengguang Zhou, Kai Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.36729v1.pdf)  
  Keywords: camera control, diffusion distillation, distillation, evaluation, human evaluation, interactive, video world model, world model  
- **[Adapting Video Models for Robot Control via Motion-guided Asymmetric Prediction](https://arxiv.org/abs/2610.36624v1)**  
  Authors: Taeyoung Kim, Junyoung Sung, Heeseung Kwon, Minseop Kim, Jinwoo Shin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.36624v1.pdf)  
  Keywords: benchmark, video diffusion  
- **[VibeVideoBench: Evaluating Multimodal Agents on Code-Driven Video Generation](https://arxiv.org/abs/2610.35864v2)**  
  Authors: Muxi Diao, Wenbin Xu, Lele Yang, Xuyang Ma, Yuzhe Chen, Jiankang Chen, Kaiyu Jiang, Changyi Liu, Haoyu Zhang, Hongyi Fu, Jianxiong Wang, Tianke Zhang, Haonan Fan, Yingxin Li, Bingyi Li, Xu Wang, Xuanyu Zheng, Bin Wen, Tingting Gao, Han Li, Wentao Zhang, Weiran Xu, Kongming Liang, Zhanyu Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.35864v2.pdf)  
  Keywords: benchmark, evaluation, game, sound, video generation  
- **[Multimodal Concert Video Editing: System Design and Exploratory Evaluation](https://arxiv.org/abs/2610.35816v1)**  
  Authors: Lennart Schiweck, Adrian Kempf, Michelle Retig, Moritz Feucht, Tim Mangliers, Benjamin Himpel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.35816v1.pdf)  
  Keywords: architecture, evaluation, video editing  

### Text-to-Video Generation

*Showing the latest 50 out of 140 papers*

- **[A Better Critic Matters for Distribution Matching Distillation](https://arxiv.org/abs/2610.42135v1)**  
  Authors: Zongze Wu, Xianbang Wang, Zhengyang Geng, Mingdeng Cao, Zhoutong Zhang, Richard Zhang, Eli Shechtman, Ruiming Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.42135v1.pdf)  
  Keywords: distillation, text to video, text-to-video, video generation  
- **[MEV: A Multi-Event Video Dataset for Long-Take Generation](https://arxiv.org/abs/2610.38241v1)**  
  Authors: Peiyuan Zhu, Shaoan Xie, Yifan Shen, Wen Tian, Zijian Li, Guangyi Chen, Kun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.38241v1.pdf)  
  Keywords: evaluation, text to video, text-to-video, video generation  
- **[A First-Step Bias Restores Lost Diversity in Diffusion Model Distillation](https://arxiv.org/abs/2610.37110v1)**  
  Authors: Wenwu Tang, Dong Wang, Yun Cheng, Olga Saukh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.37110v1.pdf)  
  Keywords: denoising, diffusion model, distillation, efficient, t2v, text to video, text-to-video, trajectory  
- **[Direct Forcing: Single-Stage Training with Representation-Space Supervision for Few-Step Autoregressive Video Generation](https://arxiv.org/abs/2610.30861v2)**  
  Authors: Haojun Xu, Jie Huang, Chuyang Zhao, Xin Lu, Mingchen Zhong, Zihao Fan, Haoyang Huang, Linjiang Huang, Si Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.30861v2.pdf)  
  Keywords: autoregressive, autoregressive video, streaming, text to video, text-to-video, video generation  
- **[PhyEvolve: Multi-Agent State-Evolution Planning for Physics-Aware Video Generation](https://arxiv.org/abs/2610.30717v1)**  
  Authors: Yang-Hao Zhou, Lixing Tan, Zhiqi Li, Guang Yang, Xiao Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.30717v1.pdf)  
  Keywords: physical, physical consistency, physics, physics-aware, text to video, text-to-video, video generation  
- **[Rethinking Video Autoencoders for Interactive World Models](https://arxiv.org/abs/2610.30129v1)**  
  Authors: Adrien Ramanana Rahary, Yutong Bai, Nicolas Dufour, Patrick Pérez, David Picard  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.30129v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kyutai.org/blog/2026-10-21-cadre)  
  Keywords: interactive, text to video, text-to-video, video autoencoder, world model  
- **[Latent Bridge: From Video Latents to 3D Geometry via Feature Alignment](https://arxiv.org/abs/2610.28521v1)**  
  Authors: Shuai Zhang, Zhanpeng Ouyang, Zhengqing Chen, Ruohong Mei, Shaoyu Chen, Weiqiang Ren, Hui Sun, Qian Zhang, Wenyu Liu, Xinggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.28521v1.pdf) | [![GitHub](https://img.shields.io/github/stars/hustvl/Latent-Bridge?style=social)](https://github.com/hustvl/Latent-Bridge)  
  Keywords: distillation, efficient, image to video, image-to-video, text to video, text-to-video, video generation  
- **[Code2Video-Compass: A Comprehensive Benchmark for General-Purpose Code-Based Video Generation across T2V, I2V, and V2V](https://arxiv.org/abs/2610.28416v1)**  
  Authors: Zhenghan Chen, Zekai Shao, Xin Lin, Leting Cheng, Siming Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.28416v1.pdf)  
  Keywords: benchmark, controllable, creative, evaluation, i2v, image to video, image-to-video, t2v, text to video, text-to-video, v2v, video generation, video to video, video-to-video  
- **[Mise-en-Video: Fine-Grained 3D Control for Multi-Shot Video Generation](https://arxiv.org/abs/2610.26801v1)**  
  Authors: Yingshuang Zou, Xiaoyu Shi, Yawen Luo, Ziang Li, Qinghe Wang, Mengfei Li, Chengfeng Zhao, Xintao Wang, Pengfei Wan, Kun Gai, Yuan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.26801v1.pdf)  
  Keywords: 3d-aware, controllable, evaluation, layout, text to video, text-to-video, video generation  
- **[PVBench: Quantifying Physical Plausibility in Video Generation with Object-Level Physical Measurements](https://arxiv.org/abs/2610.26711v1)**  
  Authors: Kaiwei Chen, Moran Li, Zhenye Gan, Yabiao Wang, Chengjie Wang, Kexin Zhang, Yong Liu, Jiangning Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.26711v1.pdf)  
  Keywords: benchmark, dynamics, embodied, evaluation, human evaluation, image to video, image-to-video, physical, physical plausibility, text to video, text-to-video, video generation  

### Video Editing

*Showing the latest 50 out of 90 papers*

- **[Multimodal Concert Video Editing: System Design and Exploratory Evaluation](https://arxiv.org/abs/2610.35816v1)**  
  Authors: Lennart Schiweck, Adrian Kempf, Michelle Retig, Moritz Feucht, Tim Mangliers, Benjamin Himpel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.35816v1.pdf)  
  Keywords: architecture, evaluation, video editing  
- **[VidEdit3D: Flexible 3D Gaussian Editing with Video Diffusion](https://arxiv.org/abs/2610.35756v1)**  
  Authors: Yanming Yang, Chenxi Song, Tong Zhao, Juntao Xu, Wenhao Rao, Yiwen Chen, Yiwei Wang, Chi Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.35756v1.pdf)  
  Keywords: dynamics, trajectory, video diffusion, video editing  
- **[When Fine-Grained Credit Assignment Helps and Hurts: Multimodal Agentic Reinforcement Learning through Video Editing](https://arxiv.org/abs/2610.35497v1)**  
  Authors: Lei Zhao, Zongheng Cao, Xinyu Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.35497v1.pdf)  
  Keywords: distillation, video editing  
- **[EditDistill: Is It Possible to Guide Video Editing with Image Editing?](https://arxiv.org/abs/2610.34303v1)**  
  Authors: Guojun Lei, Hong Li, Hongbing Yang, Lixue Gong, Chi Wang, Zheng Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.34303v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yu-shaonian.github.io/EditDistill-Web)  
  Keywords: controllable, denoising, diffusion model, flow matching, layout, trajectory, video diffusion, video editing  
- **[AnyGameRenderer: Entity-Consistent Generative Rendering Across Games and an Entity-Level Benchmark](https://arxiv.org/abs/2610.31466v3)**  
  Authors: Ruicong Liu, Liangyang Ouyang, Fengbo Lan, Zhixiang Wang, Kaipeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.31466v3.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://alaya-lab.github.io/AnyGameRenderer)  
  Keywords: benchmark, game, layout, video generation, video to video, video-to-video  
- **[NeuralSRender: G-Buffer Guided Video Diffusion for Sim-to-Real Rendering](https://arxiv.org/abs/2610.29200v1)**  
  Authors: Yipeng Lu, Youqi Liao, Zhenyu Wang, Yuning Peng, Zhen Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.29200v1.pdf) | [![GitHub](https://img.shields.io/github/stars/WHU-USI3DV/NeuralSRender?style=social)](https://github.com/WHU-USI3DV/NeuralSRender)  
  Keywords: autonomous driving, diffusion transformer, dit, driving, efficient, evaluation, video diffusion, video diffusion transformer, video translation  
- **[HorizonComposer: Spatiotemporally Consistent Driving Video Editing with Enriched Traffic Semantics](https://arxiv.org/abs/2610.28829v1)**  
  Authors: Mauricio Soroco, Yuqiu Liu, Zaid Tasneem, Francesco Pittaluga, Abhishek Aich, Wuyang Chen, Manmohan Chandraker, Ziyu Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.28829v1.pdf)  
  Keywords: autonomous driving, driving, dynamics, instruction-guided, temporal consistency, video editing  
- **[Code2Video-Compass: A Comprehensive Benchmark for General-Purpose Code-Based Video Generation across T2V, I2V, and V2V](https://arxiv.org/abs/2610.28416v1)**  
  Authors: Zhenghan Chen, Zekai Shao, Xin Lin, Leting Cheng, Siming Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.28416v1.pdf)  
  Keywords: benchmark, controllable, creative, evaluation, i2v, image to video, image-to-video, t2v, text to video, text-to-video, v2v, video generation, video to video, video-to-video  
- **[Auto-Director: Leveraging Multi-Agent Collaboration for Autonomous Video Editing](https://arxiv.org/abs/2610.28346v2)**  
  Authors: Yuxia Chen, Wenbo Zhu, Yangguang Ji, Zhenxiang Jiang, Teng Zhong, Yu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.28346v2.pdf)  
  Keywords: benchmark, creative, evaluation, human evaluation, video editing  
- **[VitronEdit: Universal Visual Editing across Images, Videos, and 3D Scenes](https://arxiv.org/abs/2610.27049v2)**  
  Authors: Jing Wang, Yanlin Li, Mong-Li Lee, Wynne Hsu, Shengqiong Wu, Hao Fei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.27049v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vitron-llm.github.io/VitronEdit)  
  Keywords: video editing  

### Video Inpainting & Completion

- **[RynnWorld-Latent: A Cross-Embodiment World Model Conditioned on Universal Latent Actions](https://arxiv.org/abs/2610.36791v1)**  
  Authors: Haoyu Zhao, Yinzhou Tang, Zixuan Wang, Minghao Zhu, Dongchi Huang, Xingyue Zhao, Qin Zhao, Kehan Li, Siteng Huang, Xin Li, Zhenyu Zeng, Mingxiu Chen, Deli Zhao, Zhongyu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.36791v1.pdf)  
  Keywords: controllable, dynamics, identity, simulation, video prediction, video world model, world model  
- **[What Does World Modeling Actually Improve in Robot Action Learning?](https://arxiv.org/abs/2610.34593v2)**  
  Authors: Hanwen Cui, Yuanyuan Li, Qing Guo, Zhida Zhang, Chao Chen, Xi Chen, Jie Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.34593v2.pdf)  
  Keywords: architecture, diffusion transformer, dit, trajectory, video diffusion, video diffusion transformer, video prediction  
- **[TrackTok: Object-Centric Video Tokenization with Semantically Persistent Tokens](https://arxiv.org/abs/2610.33857v1)**  
  Authors: Nhi Pham, Christopher Wewer, Bernt Schiele, Jonas Fischer, Jan Eric Lenssen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.33857v1.pdf) | [![GitHub](https://img.shields.io/github/stars/phamleyennhi/tracktok?style=social)](https://github.com/phamleyennhi/tracktok)  
  Keywords: efficient, frame prediction, latent video, video generation  
- **[Learning to Correct Geometry in Generated Videos](https://arxiv.org/abs/2610.23856v1)**  
  Authors: Weijie Lyu, Tiancheng Shen, Jason Li, Yujing Wang, Xiaoyuan Wang, Haobo Yuan, Yizhou Zhao, Ming-Hsuan Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.23856v1.pdf)  
  Keywords: camera motion, image to video, image-to-video, trajectory, video inpainting, video to video, video-to-video  
- **[Perceive, Predict, and Plan: a Unified World Action Model for Egocentric Dexterous Manipulation](https://arxiv.org/abs/2610.22363v2)**  
  Authors: Zirui Wu, Chen Guo, Tianjian Jiang, Zeren Jiang, Zeming Li, Lingchen Yang, Longteng Duan, Ying Xue, Handi Yin, Shenyuan Gao, Martin R. Oswald, Jun Zhang, Ping Tan, Jie Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.22363v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://p3-wam.pages.dev)  
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

### Video Super-Resolution & Enhancement

*Showing the latest 50 out of 181 papers*

- **[Optimizing Stochastic Policy Geometry for Few-Step Flow Reinforcement Learning](https://arxiv.org/abs/2610.41949v1)**  
  Authors: Zhuguanyu Wu, Congjia Chen, Ruihao Gong, Yang Yong, Shiqiao Gu, Yi Xu, Xianglong Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.41949v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ModelTC/LightX2V?style=social)](https://github.com/ModelTC/LightX2V)  
  Keywords: denoising, video generation  
- **[MorphSIG: Subject-Driven Image Generation via Decoupled Anchoring and Feature Transport](https://arxiv.org/abs/2610.39530v1)**  
  Authors: Hailong Yan, Yongrui Zhang, Xiangtao Zhang, Le Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.39530v1.pdf)  
  Keywords: benchmark, denoising, identity, image to video, image-to-video, subject-driven  
- **[Regional Anchor Routing for Multi-Object Motion Transfer](https://arxiv.org/abs/2610.39478v1)**  
  Authors: Yuze Li, Fuchen Long, Xinlong Sun, Cheng Yan, Xinyu Zhang, Xi Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.39478v1.pdf)  
  Keywords: denoising, diffusion transformer, efficient, motion transfer, video diffusion, video diffusion transformer  
- **[Hierarchical Diffusion for Camera-controlled Autoregressive Video Generation](https://arxiv.org/abs/2610.37983v1)**  
  Authors: Kaihua Chen, Yiming Gong, Deva Ramanan, Tarasha Khurana  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.37983v1.pdf)  
  Keywords: autoregressive, autoregressive video, camera control, denoising, long video, novel view, video generation  
- **[Taming Noise Initialization for Zero-shot Video Restoration with Image Diffusion Priors](https://arxiv.org/abs/2610.37290v1)**  
  Authors: Chong Wang, Zixuan Fu, Hao Cheng, Siyuan Yang, Alex C. Kot, Bihan Wen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.37290v1.pdf)  
  Keywords: diffusion model, temporal consistency, trajectory, video diffusion, video restoration  
- **[A First-Step Bias Restores Lost Diversity in Diffusion Model Distillation](https://arxiv.org/abs/2610.37110v1)**  
  Authors: Wenwu Tang, Dong Wang, Yun Cheng, Olga Saukh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.37110v1.pdf)  
  Keywords: denoising, diffusion model, distillation, efficient, t2v, text to video, text-to-video, trajectory  
- **[EditDistill: Is It Possible to Guide Video Editing with Image Editing?](https://arxiv.org/abs/2610.34303v1)**  
  Authors: Guojun Lei, Hong Li, Hongbing Yang, Lixue Gong, Chi Wang, Zheng Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.34303v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yu-shaonian.github.io/EditDistill-Web)  
  Keywords: controllable, denoising, diffusion model, flow matching, layout, trajectory, video diffusion, video editing  
- **[Learning the Autoregressive: Direct Score-Difference Estimation with Amortized Future Credit for Video Distillation](https://arxiv.org/abs/2610.34092v1)**  
  Authors: Zixuan Duan, Yabo Chen, Xunzhi Xiang, Xin Zhang, Haibin Huang, Yin Chen, Chi Zhang, Qi Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.34092v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://scdzx.github.io/Leta)  
  Keywords: autoregressive, denoising, distillation, video generation  
- **[TurboWAM: Learning What Matters for Fast World Action Models](https://arxiv.org/abs/2610.33941v1)**  
  Authors: Guile Wu, Shuangzhi Li, Xingxin Chen, Chengjie Huang, Sam Hosseini, Tongtong Cao, Yingxue Zhang, Dongfeng Bai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.33941v1.pdf)  
  Keywords: denoising, video world model, world model  
- **[WorldForge V2: Eliciting Camera-Trajectory Alignment in Video Diffusion Models](https://arxiv.org/abs/2610.31640v1)**  
  Authors: Chenxi Song, Yanming Yang, Tong Zhao, Ruibo Li, Joey Tianyi Zhou, Chi Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.31640v1.pdf)  
  Keywords: camera control, camera motion, camera trajectory, denoising, dynamics, evaluation, motion control, trajectory, video diffusion, video generation  

### World Models & Simulation

*Showing the latest 50 out of 241 papers*

- **[GeoFlip: Benchmarking Geometry-Sensitive Physics in Video Generation](https://arxiv.org/abs/2610.42002v1)**  
  Authors: Yuqi Li, Junming Liu, Bowen Hu, Ruize Niu, Huiran Duan, Yingli Tian, Hao Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.42002v1.pdf)  
  Keywords: benchmark, evaluation, image to video, image-to-video, physical, physical consistency, physics, simulation, video generation  
- **[L3G-World: Real-Time Infinite World Generation with Latent 3D Gaussian Memory](https://arxiv.org/abs/2610.40614v1)**  
  Authors: Jinhyeok Choi, JoungBin Lee, Jongmin Lee, Minkyeong Jeon, Jiyoung Kim, Kaeun Han, Yoonjin Yoon, Seungryong Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.40614v1.pdf)  
  Keywords: diffusion transformer, dit, efficient, interactive, latent video, video diffusion, video diffusion transformer  
- **[LucidLyra: Feed-Forward Generative 3D Scene Reconstruction and Joint Understanding via Multi-Task Distillation](https://arxiv.org/abs/2610.40495v1)**  
  Authors: Oliver Hahn, Rodrigo Marcuzzi, Sangeetha Grama Srinivasan, Alessandro Burzio, Sherwin Bahmani, Jiahui Huang, Stefan Roth, Shengyu Huang, Qunjie Zhou, Laura Leal-Taixé  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.40495v1.pdf)  
  Keywords: diffusion model, distillation, dynamic 3d, novel view, physical, robotics, simulation, video diffusion  
- **[Wizard: Manipulate Any World in Real Time via Agentic Control](https://arxiv.org/abs/2610.40339v1)**  
  Authors: Yuzhe Wu, Zijun Lin, Yeying Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.40339v1.pdf)  
  Keywords: controllable, game, interactive, simulation, video generation, world model, world simulation  
- **[Video Generation Meets Agent Harness: Agentic Video Generation, Agentic World Modeling and Recursive Self-Improvement](https://arxiv.org/abs/2610.40191v1)**  
  Authors: Liaoyuan Fan, Yuhao Zheng, Dongxing Mao, Hangyu Ran, Siyuan Hu, Weijia Mao, Rui Zhao, Weijia Wu, Guian Fang, Yanzhe Chen, Zeyu Zhu, Yuxin Jiang, Yiren Song, Yuchao Gu, Junchao Yi, Qi Hu, Dan Kong, Alex Jinpeng Wang, Kevin Qinghong Lin, Mike Zheng Shou, Wei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.40191v1.pdf)  
  Keywords: action-conditioned, controllable, evaluation, game, interactive, video generation  
- **[FutureWorld: A Plug-and-Play Causal Next-State Predictor for Interactive Video World Exploration](https://arxiv.org/abs/2610.39619v1)**  
  Authors: Guangyuan Li, Kelu Yao, Shuolin Xu, Xinlei Yu, Wei Xing, Lei Zhao, Peng-Tao Jiang, Xiaogang Xu, Xiaobin Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.39619v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://GuangYuanKK.github.io/futureworld)  
  Keywords: action-conditioned, interactive, long video, video generation  
- **[Seeing and Imagining as One: Unified Video Generation and 4D Perception for Embodied World Modeling](https://arxiv.org/abs/2610.39232v2)**  
  Authors: Haitang Feng, Zhuoman Liu, Zhennan Wang, Sheng Wang, Juelin Li, Chengzhi Zhao, Hexiang Wei, Lin Shao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.39232v2.pdf)  
  Keywords: architecture, diffusion transformer, dit, embodied, embodied world model, video diffusion, video diffusion transformer, video generation, world model  
- **[ReferStream: Interactive Subject Injection for Streaming Video Generation](https://arxiv.org/abs/2610.37566v1)**  
  Authors: Shuolin Xu, Guanyuan Li, Boyu Li, Kelu Yao, Xiaogang Xu, Hongchuan Yu, Shuicheng Yan, Xiaobin Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.37566v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xushuolin.github.io/ReferStream)  
  Keywords: benchmark, evaluation, interactive, streaming, streaming video generation, video generation  
- **[PDRVLA: A Vision-Language-Action Model with Physical Dynamics Representations](https://arxiv.org/abs/2610.37381v2)**  
  Authors: Hanqing Wang, Zhaotian Cai, Ruichuan An, Bohan Zeng, Tao Zhang, Yilin Chen, Xu Jiang, Kaiquan Chen, Chongyang Wu, Haoran Li, Fan Yang, Mingan Lin, Wentao Zhang, Zenan Zhou, Youzheng Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.37381v2.pdf)  
  Keywords: dynamics, embodied, physical, simulation, video generation, video world model, world model  
- **[GAWM: A Compact Latent World-Action Model for Multi-Task Robot Manipulation](https://arxiv.org/abs/2610.37091v1)**  
  Authors: Yang Liu, Xiaoli Liu, Liuzhao Li, Yuduo Song, Muyuan Liu, Xiang Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.37091v1.pdf) | [![GitHub](https://img.shields.io/github/stars/gaoxiang12/ga-wm?style=social)](https://github.com/gaoxiang12/ga-wm)  
  Keywords: layout, video generation, world model  



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
