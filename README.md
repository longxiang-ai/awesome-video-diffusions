# Awesome Video Diffusions [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Video Diffusion Models and Video Generation. Content is automatically updated daily.

🗺️ **[Explore the Paper Atlas](https://longxiang-ai.github.io/awesome-video-diffusions/)**: an interactive paper map, monthly trends, topic network, co-author network and author rankings of every tracked paper.

> Last Update: 2026-11-08 04:44:52

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

- [3D-aware Video Generation](#3d-aware-video-generation) (52 papers) - Video generation with 3D awareness, multi-view consistency, and 4D content creation
- [Applications](#applications) (193 papers) - Domain-specific applications of video diffusion models
- [Architecture & Efficiency](#architecture-&-efficiency) (393 papers) - Architectural innovations (DiT, UNet), flow matching, and training/inference efficiency
- [Audio & Multi-modal](#audio-&-multi-modal) (64 papers) - Audio-driven and multi-modal conditioned video generation
- [Controllable Generation](#controllable-generation) (314 papers) - Controllable video generation with motion, camera, pose, or layout guidance
- [Human & Character Animation](#human-&-character-animation) (53 papers) - Human-centric video generation including talking heads, dance, and character animation
- [Image-to-Video Generation](#image-to-video-generation) (92 papers) - Methods for animating still images into videos
- [Long Video Generation](#long-video-generation) (242 papers) - Generating temporally consistent long-form videos beyond short clips
- [Personalization & Customization](#personalization-&-customization) (153 papers) - Personalized video generation with custom subjects, identities, or styles
- [Physical Understanding](#physical-understanding) (282 papers) - Physics-aware video generation and dynamics modeling
- [Surveys & Benchmarks](#surveys-&-benchmarks) (323 papers) - Survey papers, benchmarks, and evaluation metrics for video generation
- [Text-to-Video Generation](#text-to-video-generation) (138 papers) - Foundation models and methods for generating videos from text prompts
- [Video Editing](#video-editing) (90 papers) - Diffusion-based video editing, style transfer, and manipulation
- [Video Inpainting & Completion](#video-inpainting-&-completion) (26 papers) - Video inpainting, completion, outpainting, and temporal prediction
- [Video Super-Resolution & Enhancement](#video-super-resolution-&-enhancement) (180 papers) - Video quality improvement, upscaling, restoration, and frame interpolation
- [World Models & Simulation](#world-models-&-simulation) (233 papers) - Video generation as world simulators and interactive environment generation



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3D-aware Video Generation

*Showing the latest 50 out of 52 papers*

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

*Showing the latest 50 out of 193 papers*

- **[GuidedWAM: Training-Free Energy Guidance for World Action Models in Autonomous Driving](https://arxiv.org/abs/2611.07912v1)**  
  Authors: Xiyan Su, Finn Rasmus Schäfer, Hojun Lim, Frank Diermeyer, Johannes Betz, Markus Lienkamp  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.07912v1.pdf)  
  Keywords: autonomous driving, driving, visual world model, world model  
- **[ReactWorld: Structuring Interaction Responses for Embodied Video Generation](https://arxiv.org/abs/2611.06120v1)**  
  Authors: Hanwei Liu, Huijia Zhang, Hanzhang Wang, Guangyu Liu, Hanbei Zhan, Linjie Hu, Bin Xiao, Xuan Zhou, Dong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.06120v1.pdf)  
  Keywords: dynamics, embodied, video generation  
- **[HIVE-Diff: High Frame Rate HDR Video Reconstruction from a Single LDR Frame and Events](https://arxiv.org/abs/2611.03465v1)**  
  Authors: Caixin Wang, Qingrui Wang, Jie Zhang, Ralph Etienne-Cummings  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.03465v1.pdf)  
  Keywords: autonomous driving, distillation, driving, video diffusion  
- **[Synthetic Realities: Evaluating Human Ability to Distinguish AIGenerated Videos from Real Footage](https://arxiv.org/abs/2611.01990v1)**  
  Authors: Danyal Sarfraz, Raja Mubashar Karim, KwanMyung Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.01990v1.pdf)  
  Keywords: evaluation, film, image to video, image-to-video, outpainting, text to video, text-to-video, video outpainting, video synthesis  
- **[FilmTogether: Cinematic Video Generation from Low-Cost Inputs](https://arxiv.org/abs/2611.00899v1)**  
  Authors: Shiying Zhang, Xiaobin Hu, Qianchi Zhang, Jiaqi Zhao, Xiaoda Yang, Bo Yin, Shuicheng Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.00899v1.pdf)  
  Keywords: cinematic, identity, layout, video editing, video generation  
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

### Architecture & Efficiency

*Showing the latest 50 out of 393 papers*

- **[Towards Practical 20 kbps Generative Video Compression via Adaptive Tokenization and Entropy Modeling](https://arxiv.org/abs/2611.08099v1)**  
  Authors: Jiancheng Zhao, Jixiang Luo, Haibin Huang, Chi Zhang, Xuelong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.08099v1.pdf)  
  Keywords: autoregressive, video tokenizer  
- **[Training-Free Predictive Spatio-Temporal Token Pruning for Few-Step Autoregressive Video Diffusion](https://arxiv.org/abs/2611.07551v1)**  
  Authors: Jia Li, Xurui Peng, Xing Wang, Hayden Kwok-Hay So  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.07551v1.pdf)  
  Keywords: autoregressive, autoregressive video, denoising, distillation, efficient, trajectory, video diffusion, video generation  
- **[Householder Motion Embedding: Noise Modulation for Motion-Controllable Video Generation](https://arxiv.org/abs/2611.07294v1)**  
  Authors: Tao Jun Lin, Jinhong Ni, Ruyi Zha, Yifu Wang, Xibin Song, Pan Ji, Hongdong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.07294v1.pdf)  
  Keywords: architecture, controllable, efficient, motion control, video diffusion, video generation  
- **[VA-TDM: A Unified View for Improving Few-Step Diffusion Models by Velocity Adversarial Distillation](https://arxiv.org/abs/2611.06796v1)**  
  Authors: Yihong Luo, Tianyu Pang, Tianyang Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.06796v1.pdf)  
  Keywords: denoising, distillation, efficient, flow matching, text to video, text-to-video, trajectory, video generation  
- **[NextGAN: Towards Simple and Scalable GAN Training for Image and Video Generation](https://arxiv.org/abs/2611.06270v1)**  
  Authors: Xinhao Lou, Dongye Xie, Peng Sun, Chenyi Zhuang, Kaicheng Yu, Tao Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.06270v1.pdf) | [![GitHub](https://img.shields.io/github/stars/LINs-lab/NextGAN.git?style=social)](https://github.com/LINs-lab/NextGAN.git)  
  Keywords: dit, text to video, text-to-video, video generation  
- **[TouchéWorld tech report : Towards Online Unified Camera--Hand Exploration in Generative Worlds](https://arxiv.org/abs/2611.06061v1)**  
  Authors: Jiaao Yu, Yanjian Zhang, Haoyang Jiang, Guillaume Wisniewski, Nadi Tomeh, Shijie Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.06061v1.pdf)  
  Keywords: distillation, efficient, gesture, video world model, world model  
- **[DecoupAttn: Decoupled Sparse Attention for Training-Free Acceleration of Video Diffusion](https://arxiv.org/abs/2611.05917v1)**  
  Authors: Yanjin Li, Bingbing Qiu, Qiang Huang, Rui Qian, Yanfeng Li, Jian Wang, Xiaoying Tang, Mingda Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.05917v1.pdf)  
  Keywords: acceleration, denoising, sparse attention, video diffusion  
- **[DualCast: Dual-Image Conditioned Diffusion Transformers for Digital Human E-Commerce Video Generation](https://arxiv.org/abs/2611.05825v1)**  
  Authors: Lifan Jiang, Yibo Zhao, Senlin Cheng, Bolei Xu, Xiaobo Li, Can Ye, Dehai Zhao, Deng Cai, Boxi Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.05825v1.pdf)  
  Keywords: digital human, dit, identity, style, video generation  
- **[DreamX: Video Diffusion Model is a Universal Latent Action Learner](https://arxiv.org/abs/2611.05377v1)**  
  Authors: Jisoo Kim, Chaehyun Kim, Junsu Kim, Jiho Park, Seongchan Kim, Eunbeen Hong, Soowon Son, Fu-En Yang, Seungryong Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.05377v1.pdf)  
  Keywords: diffusion model, dynamics, latent video, video diffusion  
- **[Behind Video Generation: Observations and Insights on Multimodal Understanding from Kling](https://arxiv.org/abs/2611.04916v1)**  
  Authors: Kling Team, Dong Chen, Jialu Chen, Xinlong Chen, Yifan Dai, Haotian Dong, Binzong Geng, Yushuo Guan, Minghui Guo, Guanlin He, Guanxiao He, Jingyun Hua, Yanwei Huang, Yiyan Ji, Xueping Jia, Yizhuo Jia, Bozhou Li, Jiaze Li, Min Li, Shihao Li, Shujie Li, Shengyi Liao, Weihong Lin, Shiyuan Liu, Xinyu Liu, Siyang Mao, Xiaoru Qu, Dianmo Sheng, Yang Shi, Jiafu Tang, Longxiang Tang, Yuqi Tang, Chengzhuo Tong, Kuo Wang, Qixun Wang, Rui Wang, Tianduo Wang, Yuran Wang, Zekun Wang, Zihao Wang, Boyang Xia, Yifan Xu, Liu Yang, Zhenlong Yuan, Bohan Zeng, Mujin Zhang, Yuanxing Zhang, Zhicheng Zhang, Zhuoran Zhang, Yuanhong Zheng, Kun Gai, Chengru Song, Pengfei Wan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.04916v1.pdf)  
  Keywords: controllable, dit, evaluation, video generation  

### Audio & Multi-modal

*Showing the latest 50 out of 64 papers*

- **[TaoMate-HD: Progressive-Resolution Autoregressive Audio-Video Generation](https://arxiv.org/abs/2611.03394v1)**  
  Authors: Qijun Gan, Chenwei Zhang, Xinyang Li, Meiguang Jin, Junfeng Ma, Shen Qiu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.03394v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://taoliveaigc.github.io/TaoMate-HD)  
  Keywords: audio-video generation, autoregressive, denoising, distillation, streaming, trajectory, video generation  
- **[OmniOPD: Stable On-Policy Distillation for Joint Audio-Video Generation](https://arxiv.org/abs/2611.02803v1)**  
  Authors: Zihao Fan, Xin Lu, Jie Huang, Hexin Zhang, Xueyang Fu, Zheng-Jun Zha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.02803v1.pdf)  
  Keywords: audio-video generation, distillation, joint audio-video, video generation  
- **[CAST-Bench: Tracing Every Sound to Its Source in Multi-Shot Audio-Video Generation](https://arxiv.org/abs/2611.05422v1)**  
  Authors: Yucong Liu, Qi Tian, Shuyuan Tu, Kaihang Pan, Weijie Kong, Chao Pan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.05422v1.pdf) | [![GitHub](https://img.shields.io/github/stars/yucong-liu/CAST-Bench-public?style=social)](https://github.com/yucong-liu/CAST-Bench-public)  
  Keywords: audio-video generation, benchmark, evaluation, identity, sound, video generation  
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

### Controllable Generation

*Showing the latest 50 out of 314 papers*

- **[EgoGeneralist: Unifying Egocentric Action-Video Tasks through Video-Native Modeling](https://arxiv.org/abs/2611.08477v1)**  
  Authors: Yanlin Jin, Bowen Yang, Cheng Zhang, Yifan Yang, Zhe Li, Jianfei Cai, Kai Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.08477v1.pdf)  
  Keywords: action-conditioned, dynamics, human motion, video generation  
- **[Training-Free Predictive Spatio-Temporal Token Pruning for Few-Step Autoregressive Video Diffusion](https://arxiv.org/abs/2611.07551v1)**  
  Authors: Jia Li, Xurui Peng, Xing Wang, Hayden Kwok-Hay So  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.07551v1.pdf)  
  Keywords: autoregressive, autoregressive video, denoising, distillation, efficient, trajectory, video diffusion, video generation  
- **[Householder Motion Embedding: Noise Modulation for Motion-Controllable Video Generation](https://arxiv.org/abs/2611.07294v1)**  
  Authors: Tao Jun Lin, Jinhong Ni, Ruyi Zha, Yifu Wang, Xibin Song, Pan Ji, Hongdong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.07294v1.pdf)  
  Keywords: architecture, controllable, efficient, motion control, video diffusion, video generation  
- **[VA-TDM: A Unified View for Improving Few-Step Diffusion Models by Velocity Adversarial Distillation](https://arxiv.org/abs/2611.06796v1)**  
  Authors: Yihong Luo, Tianyu Pang, Tianyang Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.06796v1.pdf)  
  Keywords: denoising, distillation, efficient, flow matching, text to video, text-to-video, trajectory, video generation  
- **[Chronos: Sequential Identity-Preserving Video Generation by Temporal Anchoring](https://arxiv.org/abs/2611.05893v1)**  
  Authors: Mengqi Huang, Wenchuan Wang, Zhendong Mao, Yijing Tu, Zhike Liu, Luoni Wang, Ning Tong, Xiaoxiao Sheng, Tianyu Huang, Xuecheng Qi, Yongdong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.05893v1.pdf)  
  Keywords: evaluation, identity, identity-preserving, keyframe, reference-guided, video generation  
- **[Route Anything: A Study of Model and Policy Routing for General-Purpose AI Systems](https://arxiv.org/abs/2611.05275v1)**  
  Authors: Pengfei Zhou, Yixing Ma, Hexin Wang, Weidong Tang, Zhenglin Wan, Wangbo Zhao, Yang You  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.05275v1.pdf)  
  Keywords: trajectory, video generation  
- **[Behind Video Generation: Observations and Insights on Multimodal Understanding from Kling](https://arxiv.org/abs/2611.04916v1)**  
  Authors: Kling Team, Dong Chen, Jialu Chen, Xinlong Chen, Yifan Dai, Haotian Dong, Binzong Geng, Yushuo Guan, Minghui Guo, Guanlin He, Guanxiao He, Jingyun Hua, Yanwei Huang, Yiyan Ji, Xueping Jia, Yizhuo Jia, Bozhou Li, Jiaze Li, Min Li, Shihao Li, Shujie Li, Shengyi Liao, Weihong Lin, Shiyuan Liu, Xinyu Liu, Siyang Mao, Xiaoru Qu, Dianmo Sheng, Yang Shi, Jiafu Tang, Longxiang Tang, Yuqi Tang, Chengzhuo Tong, Kuo Wang, Qixun Wang, Rui Wang, Tianduo Wang, Yuran Wang, Zekun Wang, Zihao Wang, Boyang Xia, Yifan Xu, Liu Yang, Zhenlong Yuan, Bohan Zeng, Mujin Zhang, Yuanxing Zhang, Zhicheng Zhang, Zhuoran Zhang, Yuanhong Zheng, Kun Gai, Chengru Song, Pengfei Wan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.04916v1.pdf)  
  Keywords: controllable, dit, evaluation, video generation  
- **[CounterSketch: Physics-Grounded Counterfactual Reasoning for Sketch-to-Video Generation](https://arxiv.org/abs/2611.04244v1)**  
  Authors: Hien Trinh, Tan-Hiep To, Dinh-Khoi Vo, Tam V. Nguyen, Minh-Triet Tran, Trung-Nghia Le  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.04244v1.pdf)  
  Keywords: physical, physics, trajectory, video generation, video synthesis  
- **[TaoMate-HD: Progressive-Resolution Autoregressive Audio-Video Generation](https://arxiv.org/abs/2611.03394v1)**  
  Authors: Qijun Gan, Chenwei Zhang, Xinyang Li, Meiguang Jin, Junfeng Ma, Shen Qiu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.03394v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://taoliveaigc.github.io/TaoMate-HD)  
  Keywords: audio-video generation, autoregressive, denoising, distillation, streaming, trajectory, video generation  
- **[Generative diffusion in long-range correlated landscapes: Speciation cascade and the foam structure of the score](https://arxiv.org/abs/2611.02955v1)**  
  Authors: Jerome Garnier-Brun, Giulio Biroli, Marc Mézard, Jean-Philippe Bouchaud  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.02955v1.pdf)  
  Keywords: autoregressive, denoising, trajectory, video generation  

### Human & Character Animation

*Showing the latest 50 out of 53 papers*

- **[EgoGeneralist: Unifying Egocentric Action-Video Tasks through Video-Native Modeling](https://arxiv.org/abs/2611.08477v1)**  
  Authors: Yanlin Jin, Bowen Yang, Cheng Zhang, Yifan Yang, Zhe Li, Jianfei Cai, Kai Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.08477v1.pdf)  
  Keywords: action-conditioned, dynamics, human motion, video generation  
- **[EmoReward: Self-Evolving Reward Calibration for Emotional Video Generation RL](https://arxiv.org/abs/2611.06518v1)**  
  Authors: Mingzhe Zheng, Yue Wu, Jing Tan, Chang Zou, Dengyang Jiang, Zeyue Tian, Xuanhua He, Ryan Xu, Yunyang Ge, Sihui Ji, Yunlong Lin, Kaihang Pan, Hongru Yan, Sixiang Chen, Dianyi Wang, Julian Zhang, Weijie Kong, Changlin Li, Lanqing Guo, Zhao Zhong, Qifeng Chen, Harry Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.06518v1.pdf)  
  Keywords: body motion, evaluation, video generation  
- **[TouchéWorld tech report : Towards Online Unified Camera--Hand Exploration in Generative Worlds](https://arxiv.org/abs/2611.06061v1)**  
  Authors: Jiaao Yu, Yanjian Zhang, Haoyang Jiang, Guillaume Wisniewski, Nadi Tomeh, Shijie Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.06061v1.pdf)  
  Keywords: distillation, efficient, gesture, video world model, world model  
- **[DualCast: Dual-Image Conditioned Diffusion Transformers for Digital Human E-Commerce Video Generation](https://arxiv.org/abs/2611.05825v1)**  
  Authors: Lifan Jiang, Yibo Zhao, Senlin Cheng, Bolei Xu, Xiaobo Li, Can Ye, Dehai Zhao, Deng Cai, Boxi Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.05825v1.pdf)  
  Keywords: digital human, dit, identity, style, video generation  
- **[Synthesizing Dexterous Robot Demonstrations from Human Videos via Virtual Try-On](https://arxiv.org/abs/2611.05163v3)**  
  Authors: Seungyong Lee, Suhyeok Jang, Minyoung Kim, Jinwoo Shin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.05163v3.pdf)  
  Keywords: dynamics, video synthesis, virtual try-on  
- **[TaoMate-FVSR: Audio-Guided Facial Video Restoration](https://arxiv.org/abs/2611.03393v2)**  
  Authors: Xinyang Li, Zeran Xu, Jingna Sun, Qijun Gan, Chenwei Zhang, Meiguang Jin, Junfeng Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.03393v2.pdf)  
  Keywords: diffusion transformer, identity, talking head, temporal consistency, video diffusion, video diffusion transformer, video restoration  
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

### Image-to-Video Generation

*Showing the latest 50 out of 92 papers*

- **[PathoS2VD: From 2D Histopathology to Pseudo Z-Stack Representations](https://arxiv.org/abs/2611.05974v1)**  
  Authors: Jiamu Wang, Keunho Byeon, Ji-Uk Kim, Jin Tae Kwak, Heounjeong Go  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.05974v1.pdf) | [![GitHub](https://img.shields.io/github/stars/QuIIL/PathoS2VD?style=social)](https://github.com/QuIIL/PathoS2VD)  
  Keywords: diffusion model, i2v, image to video, image-to-video, physical  
- **[Synthetic Realities: Evaluating Human Ability to Distinguish AIGenerated Videos from Real Footage](https://arxiv.org/abs/2611.01990v1)**  
  Authors: Danyal Sarfraz, Raja Mubashar Karim, KwanMyung Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.01990v1.pdf)  
  Keywords: evaluation, film, image to video, image-to-video, outpainting, text to video, text-to-video, video outpainting, video synthesis  
- **[IMPACT: Image-Conditioned Motion with Physics-Aware Collision and Trajectory Guidance for Video Generation](https://arxiv.org/abs/2611.01372v1)**  
  Authors: Shiwei Yang, Yunlong Yu, Zhao Wang, Jungong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.01372v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://weiweiwiewei.github.io/impact)  
  Keywords: controllable, dynamics, image to video, image-to-video, physical, physical plausibility, physics, physics-aware, trajectory, video generation  
- **[GeoFlip Preview: Benchmarking Geometry-Sensitive Physics in Video Generation](https://arxiv.org/abs/2610.42002v2)**  
  Authors: Yuqi Li, Junming Liu, Bowen Hu, Ruize Niu, Huiran Duan, Ming-Hsuan Yang, Yingli Tian, Hao Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.42002v2.pdf)  
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
- **[AEON: Unifying Video and 3D World Models](https://arxiv.org/abs/2610.28631v2)**  
  Authors: Weiqi Zhang, Wenyuan Zhang, Yu-Shen Liu, Junsheng Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.28631v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://weiqi-zhang.github.io/AEON)  
  Keywords: distillation, dynamics, image-conditioned video, simulation, world simulation  
- **[Latent Bridge: From Video Latents to 3D Geometry via Feature Alignment](https://arxiv.org/abs/2610.28521v1)**  
  Authors: Shuai Zhang, Zhanpeng Ouyang, Zhengqing Chen, Ruohong Mei, Shaoyu Chen, Weiqiang Ren, Hui Sun, Qian Zhang, Wenyu Liu, Xinggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.28521v1.pdf) | [![GitHub](https://img.shields.io/github/stars/hustvl/Latent-Bridge?style=social)](https://github.com/hustvl/Latent-Bridge)  
  Keywords: distillation, efficient, image to video, image-to-video, text to video, text-to-video, video generation  
- **[Code2Video-Compass: A Comprehensive Benchmark for General-Purpose Code-Based Video Generation across T2V, I2V, and V2V](https://arxiv.org/abs/2610.28416v1)**  
  Authors: Zhenghan Chen, Zekai Shao, Xin Lin, Leting Cheng, Siming Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.28416v1.pdf)  
  Keywords: benchmark, controllable, creative, evaluation, i2v, image to video, image-to-video, t2v, text to video, text-to-video, v2v, video generation, video to video, video-to-video  

### Long Video Generation

*Showing the latest 50 out of 242 papers*

- **[ManimCode: Learning Visual Self-Correction for Educational Animation](https://arxiv.org/abs/2611.08294v1)**  
  Authors: Zhengyang Liang, Lizi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.08294v1.pdf)  
  Keywords: long-form, video generation  
- **[Towards Practical 20 kbps Generative Video Compression via Adaptive Tokenization and Entropy Modeling](https://arxiv.org/abs/2611.08099v1)**  
  Authors: Jiancheng Zhao, Jixiang Luo, Haibin Huang, Chi Zhang, Xuelong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.08099v1.pdf)  
  Keywords: autoregressive, video tokenizer  
- **[Training-Free Predictive Spatio-Temporal Token Pruning for Few-Step Autoregressive Video Diffusion](https://arxiv.org/abs/2611.07551v1)**  
  Authors: Jia Li, Xurui Peng, Xing Wang, Hayden Kwok-Hay So  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.07551v1.pdf)  
  Keywords: autoregressive, autoregressive video, denoising, distillation, efficient, trajectory, video diffusion, video generation  
- **[EvoWorld: Towards Out-of-Sight World Evolution in Generative Video Models](https://arxiv.org/abs/2611.06748v2)**  
  Authors: Yequan Bie, Dengyang Jiang, Zhixuan Chen, Xiaozhuan Liang, Haoxuan Che, Quande Liu, Xi Chen, Hao Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.06748v2.pdf)  
  Keywords: autoregressive, autoregressive video  
- **[NanoKV: High-Ratio KV Cache Compression for Autoregressive Video Generation](https://arxiv.org/abs/2611.06377v1)**  
  Authors: Jiacheng Lu, Haoyi Zhu, Sipei Yi, Enze Xie, Cheng Zhuo, Yu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.06377v1.pdf)  
  Keywords: autoregressive, autoregressive video, video generation  
- **[What Remains in Sight? Autoregressive Video Decoding as Representation-Guided Context Rewriting](https://arxiv.org/abs/2611.04164v1)**  
  Authors: Lixuan He, Jihyeon Je, Yang You, Leonidas Guibas  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.04164v1.pdf)  
  Keywords: autoregressive, autoregressive video, long video, text to video, text-to-video, video generation  
- **[TaoMate-HD: Progressive-Resolution Autoregressive Audio-Video Generation](https://arxiv.org/abs/2611.03394v1)**  
  Authors: Qijun Gan, Chenwei Zhang, Xinyang Li, Meiguang Jin, Junfeng Ma, Shen Qiu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.03394v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://taoliveaigc.github.io/TaoMate-HD)  
  Keywords: audio-video generation, autoregressive, denoising, distillation, streaming, trajectory, video generation  
- **[TaoMate-FVSR: Audio-Guided Facial Video Restoration](https://arxiv.org/abs/2611.03393v2)**  
  Authors: Xinyang Li, Zeran Xu, Jingna Sun, Qijun Gan, Chenwei Zhang, Meiguang Jin, Junfeng Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.03393v2.pdf)  
  Keywords: diffusion transformer, identity, talking head, temporal consistency, video diffusion, video diffusion transformer, video restoration  
- **[Generative diffusion in long-range correlated landscapes: Speciation cascade and the foam structure of the score](https://arxiv.org/abs/2611.02955v1)**  
  Authors: Jerome Garnier-Brun, Giulio Biroli, Marc Mézard, Jean-Philippe Bouchaud  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.02955v1.pdf)  
  Keywords: autoregressive, denoising, trajectory, video generation  
- **[Disen-Forcing: Disentangling Semantic Anchoring from Motion for Autoregressive Video Diffusion](https://arxiv.org/abs/2611.02822v1)**  
  Authors: Zhengyang Yu, Akio Hayakawa, Masato Ishii, Qingtao Yu, Xuesong Li, Takashi Shibuya, Yuki Mitsufuji, Jing Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.02822v1.pdf)  
  Keywords: autoregressive, autoregressive video, distillation, dynamics, style, video diffusion, video generation  

### Personalization & Customization

*Showing the latest 50 out of 153 papers*

- **[Guidance Is a Field, Not a Scalar: Interval-Integrated Classifier-Free Guidance for One-Step Video Generation](https://arxiv.org/abs/2611.07566v1)**  
  Authors: Zijie Meng, Xixin Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.07566v1.pdf) | [![GitHub](https://img.shields.io/github/stars/YMlinfeng/AGAVE?style=social)](https://github.com/YMlinfeng/AGAVE)  
  Keywords: evaluation, identity, video generation  
- **[Chronos: Sequential Identity-Preserving Video Generation by Temporal Anchoring](https://arxiv.org/abs/2611.05893v1)**  
  Authors: Mengqi Huang, Wenchuan Wang, Zhendong Mao, Yijing Tu, Zhike Liu, Luoni Wang, Ning Tong, Xiaoxiao Sheng, Tianyu Huang, Xuecheng Qi, Yongdong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.05893v1.pdf)  
  Keywords: evaluation, identity, identity-preserving, keyframe, reference-guided, video generation  
- **[DualCast: Dual-Image Conditioned Diffusion Transformers for Digital Human E-Commerce Video Generation](https://arxiv.org/abs/2611.05825v1)**  
  Authors: Lifan Jiang, Yibo Zhao, Senlin Cheng, Bolei Xu, Xiaobo Li, Can Ye, Dehai Zhao, Deng Cai, Boxi Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.05825v1.pdf)  
  Keywords: digital human, dit, identity, style, video generation  
- **[TaoMate-FVSR: Audio-Guided Facial Video Restoration](https://arxiv.org/abs/2611.03393v2)**  
  Authors: Xinyang Li, Zeran Xu, Jingna Sun, Qijun Gan, Chenwei Zhang, Meiguang Jin, Junfeng Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.03393v2.pdf)  
  Keywords: diffusion transformer, identity, talking head, temporal consistency, video diffusion, video diffusion transformer, video restoration  
- **[One Image Is Enough: Self-Generated Supervision for Personalizing Human Video Diffusion at Test Time](https://arxiv.org/abs/2611.02964v1)**  
  Authors: Sadman Rakib Pinon, Adamo Orsini, Yanis Falaki, Linlian Jiang, Jacob Kingi, Yang Wang, Xinxin Zuo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.02964v1.pdf) | [![GitHub](https://img.shields.io/github/stars/SadmanPinon/one-image-is-enough?style=social)](https://github.com/SadmanPinon/one-image-is-enough)  
  Keywords: identity, personalization, video diffusion  
- **[Disen-Forcing: Disentangling Semantic Anchoring from Motion for Autoregressive Video Diffusion](https://arxiv.org/abs/2611.02822v1)**  
  Authors: Zhengyang Yu, Akio Hayakawa, Masato Ishii, Qingtao Yu, Xuesong Li, Takashi Shibuya, Yuki Mitsufuji, Jing Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.02822v1.pdf)  
  Keywords: autoregressive, autoregressive video, distillation, dynamics, style, video diffusion, video generation  
- **[CAST-Bench: Tracing Every Sound to Its Source in Multi-Shot Audio-Video Generation](https://arxiv.org/abs/2611.05422v1)**  
  Authors: Yucong Liu, Qi Tian, Shuyuan Tu, Kaihang Pan, Weijie Kong, Chao Pan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.05422v1.pdf) | [![GitHub](https://img.shields.io/github/stars/yucong-liu/CAST-Bench-public?style=social)](https://github.com/yucong-liu/CAST-Bench-public)  
  Keywords: audio-video generation, benchmark, evaluation, identity, sound, video generation  
- **[FilmTogether: Cinematic Video Generation from Low-Cost Inputs](https://arxiv.org/abs/2611.00899v1)**  
  Authors: Shiying Zhang, Xiaobin Hu, Qianchi Zhang, Jiaqi Zhao, Xiaoda Yang, Bo Yin, Shuicheng Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.00899v1.pdf)  
  Keywords: cinematic, identity, layout, video editing, video generation  
- **[TADP: Dual-Branch Temporally Adaptive Differential Privacy for Expression-Aware Video Anonymization](https://arxiv.org/abs/2610.41642v1)**  
  Authors: Feng Xu, Xun Li, Lars Petersson, Yulei Sui, David Ahmedt-Aristizabal, Dadong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.41642v1.pdf)  
  Keywords: identity, video generation  
- **[MorphSIG: Subject-Driven Image Generation via Decoupled Anchoring and Feature Transport](https://arxiv.org/abs/2610.39530v1)**  
  Authors: Hailong Yan, Yongrui Zhang, Xiangtao Zhang, Le Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.39530v1.pdf)  
  Keywords: benchmark, denoising, identity, image to video, image-to-video, subject-driven  

### Physical Understanding

*Showing the latest 50 out of 282 papers*

- **[EgoGeneralist: Unifying Egocentric Action-Video Tasks through Video-Native Modeling](https://arxiv.org/abs/2611.08477v1)**  
  Authors: Yanlin Jin, Bowen Yang, Cheng Zhang, Yifan Yang, Zhe Li, Jianfei Cai, Kai Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.08477v1.pdf)  
  Keywords: action-conditioned, dynamics, human motion, video generation  
- **[CoGenRec: A Unified Generative Framework for Complementary Vision Reconstruction](https://arxiv.org/abs/2611.07665v1)**  
  Authors: Yapeng Meng, Yuguo Chen, Xiangru Chen, Shaojun Xu, Xuezhen Wang, Lijian Wang, Zheyu Yang, Yihan Lin, Luping Shi, Rong Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.07665v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://cogenrec.github.io)  
  Keywords: diffusion model, frame interpolation, physical, video deblurring, video diffusion  
- **[ReactWorld: Structuring Interaction Responses for Embodied Video Generation](https://arxiv.org/abs/2611.06120v1)**  
  Authors: Hanwei Liu, Huijia Zhang, Hanzhang Wang, Guangyu Liu, Hanbei Zhan, Linjie Hu, Bin Xiao, Xuan Zhou, Dong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.06120v1.pdf)  
  Keywords: dynamics, embodied, video generation  
- **[PathoS2VD: From 2D Histopathology to Pseudo Z-Stack Representations](https://arxiv.org/abs/2611.05974v1)**  
  Authors: Jiamu Wang, Keunho Byeon, Ji-Uk Kim, Jin Tae Kwak, Heounjeong Go  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.05974v1.pdf) | [![GitHub](https://img.shields.io/github/stars/QuIIL/PathoS2VD?style=social)](https://github.com/QuIIL/PathoS2VD)  
  Keywords: diffusion model, i2v, image to video, image-to-video, physical  
- **[DreamX: Video Diffusion Model is a Universal Latent Action Learner](https://arxiv.org/abs/2611.05377v1)**  
  Authors: Jisoo Kim, Chaehyun Kim, Junsu Kim, Jiho Park, Seongchan Kim, Eunbeen Hong, Soowon Son, Fu-En Yang, Seungryong Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.05377v1.pdf)  
  Keywords: diffusion model, dynamics, latent video, video diffusion  
- **[Synthesizing Dexterous Robot Demonstrations from Human Videos via Virtual Try-On](https://arxiv.org/abs/2611.05163v3)**  
  Authors: Seungyong Lee, Suhyeok Jang, Minyoung Kim, Jinwoo Shin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.05163v3.pdf)  
  Keywords: dynamics, video synthesis, virtual try-on  
- **[CounterSketch: Physics-Grounded Counterfactual Reasoning for Sketch-to-Video Generation](https://arxiv.org/abs/2611.04244v1)**  
  Authors: Hien Trinh, Tan-Hiep To, Dinh-Khoi Vo, Tam V. Nguyen, Minh-Triet Tran, Trung-Nghia Le  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.04244v1.pdf)  
  Keywords: physical, physics, trajectory, video generation, video synthesis  
- **[Compression Forcing: Hierarchical History Tokenization Enables Flexible World Models](https://arxiv.org/abs/2611.04028v1)**  
  Authors: Siqiao Huang, Partha Kaushik, Michael Chen, Hengkai Pan, Kaiwen Geng, Omar Chehab, Fernando Moreno-Pino, Max Simchowitz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.04028v1.pdf)  
  Keywords: dynamics, dynamics-aware, physical, video generation, world model  
- **[Disen-Forcing: Disentangling Semantic Anchoring from Motion for Autoregressive Video Diffusion](https://arxiv.org/abs/2611.02822v1)**  
  Authors: Zhengyang Yu, Akio Hayakawa, Masato Ishii, Qingtao Yu, Xuesong Li, Takashi Shibuya, Yuki Mitsufuji, Jing Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.02822v1.pdf)  
  Keywords: autoregressive, autoregressive video, distillation, dynamics, style, video diffusion, video generation  
- **[IMPACT: Image-Conditioned Motion with Physics-Aware Collision and Trajectory Guidance for Video Generation](https://arxiv.org/abs/2611.01372v1)**  
  Authors: Shiwei Yang, Yunlong Yu, Zhao Wang, Jungong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.01372v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://weiweiwiewei.github.io/impact)  
  Keywords: controllable, dynamics, image to video, image-to-video, physical, physical plausibility, physics, physics-aware, trajectory, video generation  

### Surveys & Benchmarks

*Showing the latest 50 out of 323 papers*

- **[Guidance Is a Field, Not a Scalar: Interval-Integrated Classifier-Free Guidance for One-Step Video Generation](https://arxiv.org/abs/2611.07566v1)**  
  Authors: Zijie Meng, Xixin Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.07566v1.pdf) | [![GitHub](https://img.shields.io/github/stars/YMlinfeng/AGAVE?style=social)](https://github.com/YMlinfeng/AGAVE)  
  Keywords: evaluation, identity, video generation  
- **[EmoReward: Self-Evolving Reward Calibration for Emotional Video Generation RL](https://arxiv.org/abs/2611.06518v1)**  
  Authors: Mingzhe Zheng, Yue Wu, Jing Tan, Chang Zou, Dengyang Jiang, Zeyue Tian, Xuanhua He, Ryan Xu, Yunyang Ge, Sihui Ji, Yunlong Lin, Kaihang Pan, Hongru Yan, Sixiang Chen, Dianyi Wang, Julian Zhang, Weijie Kong, Changlin Li, Lanqing Guo, Zhao Zhong, Qifeng Chen, Harry Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.06518v1.pdf)  
  Keywords: body motion, evaluation, video generation  
- **[Grounding in the Dark: Text-Only Training for Zero-Shot Video Temporal Localization](https://arxiv.org/abs/2611.06149v2)**  
  Authors: Divyanshu Mishra, Sabine Sternig, Rakshith Shetty, Erhan Gundogdu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.06149v2.pdf)  
  Keywords: benchmark, text to video, text-to-video  
- **[Chronos: Sequential Identity-Preserving Video Generation by Temporal Anchoring](https://arxiv.org/abs/2611.05893v1)**  
  Authors: Mengqi Huang, Wenchuan Wang, Zhendong Mao, Yijing Tu, Zhike Liu, Luoni Wang, Ning Tong, Xiaoxiao Sheng, Tianyu Huang, Xuecheng Qi, Yongdong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.05893v1.pdf)  
  Keywords: evaluation, identity, identity-preserving, keyframe, reference-guided, video generation  
- **[Behind Video Generation: Observations and Insights on Multimodal Understanding from Kling](https://arxiv.org/abs/2611.04916v1)**  
  Authors: Kling Team, Dong Chen, Jialu Chen, Xinlong Chen, Yifan Dai, Haotian Dong, Binzong Geng, Yushuo Guan, Minghui Guo, Guanlin He, Guanxiao He, Jingyun Hua, Yanwei Huang, Yiyan Ji, Xueping Jia, Yizhuo Jia, Bozhou Li, Jiaze Li, Min Li, Shihao Li, Shujie Li, Shengyi Liao, Weihong Lin, Shiyuan Liu, Xinyu Liu, Siyang Mao, Xiaoru Qu, Dianmo Sheng, Yang Shi, Jiafu Tang, Longxiang Tang, Yuqi Tang, Chengzhuo Tong, Kuo Wang, Qixun Wang, Rui Wang, Tianduo Wang, Yuran Wang, Zekun Wang, Zihao Wang, Boyang Xia, Yifan Xu, Liu Yang, Zhenlong Yuan, Bohan Zeng, Mujin Zhang, Yuanxing Zhang, Zhicheng Zhang, Zhuoran Zhang, Yuanhong Zheng, Kun Gai, Chengru Song, Pengfei Wan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.04916v1.pdf)  
  Keywords: controllable, dit, evaluation, video generation  
- **[Omni-Life: Benchmarking Omnimodal Real-Time AI Assistants in People's Daily Lives](https://arxiv.org/abs/2611.02835v1)**  
  Authors: Mengze Hong, Ziwei Shang, Di Liang, Zijian Li, Liang Zhu, Hongyu Shan, Robin Zhou, Minlong Peng, Zhiqiang Kou, Jia Wang, Di Jiang, Chen Jason Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.02835v1.pdf)  
  Keywords: benchmark, video synthesis  
- **[CAST-Bench: Tracing Every Sound to Its Source in Multi-Shot Audio-Video Generation](https://arxiv.org/abs/2611.05422v1)**  
  Authors: Yucong Liu, Qi Tian, Shuyuan Tu, Kaihang Pan, Weijie Kong, Chao Pan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.05422v1.pdf) | [![GitHub](https://img.shields.io/github/stars/yucong-liu/CAST-Bench-public?style=social)](https://github.com/yucong-liu/CAST-Bench-public)  
  Keywords: audio-video generation, benchmark, evaluation, identity, sound, video generation  
- **[MoviEdit: Long-form Multi-Shot Video Editing Made Easy](https://arxiv.org/abs/2611.02737v1)**  
  Authors: Suhyeon Lee, Zhengang Li, Soo Ye Kim, Peihao Zhu, Jong Chul Ye, Chun-Hao Paul Huang, Duygu Ceylan, Yan Kang, Hyeonho Jeong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.02737v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://multi-shot-edit.github.io)  
  Keywords: autoregressive, benchmark, evaluation, long-form, video editing  
- **[Synthetic Realities: Evaluating Human Ability to Distinguish AIGenerated Videos from Real Footage](https://arxiv.org/abs/2611.01990v1)**  
  Authors: Danyal Sarfraz, Raja Mubashar Karim, KwanMyung Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.01990v1.pdf)  
  Keywords: evaluation, film, image to video, image-to-video, outpainting, text to video, text-to-video, video outpainting, video synthesis  
- **[Recoverability-Aware Evaluation of Diffusion Video Inpainting and Object Removal](https://arxiv.org/abs/2611.01578v1)**  
  Authors: Yanliang Qi, Jiacheng Ding, Cong Guo, Peihua Mai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.01578v1.pdf)  
  Keywords: evaluation, video diffusion, video inpainting  

### Text-to-Video Generation

*Showing the latest 50 out of 138 papers*

- **[VA-TDM: A Unified View for Improving Few-Step Diffusion Models by Velocity Adversarial Distillation](https://arxiv.org/abs/2611.06796v1)**  
  Authors: Yihong Luo, Tianyu Pang, Tianyang Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.06796v1.pdf)  
  Keywords: denoising, distillation, efficient, flow matching, text to video, text-to-video, trajectory, video generation  
- **[NextGAN: Towards Simple and Scalable GAN Training for Image and Video Generation](https://arxiv.org/abs/2611.06270v1)**  
  Authors: Xinhao Lou, Dongye Xie, Peng Sun, Chenyi Zhuang, Kaicheng Yu, Tao Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.06270v1.pdf) | [![GitHub](https://img.shields.io/github/stars/LINs-lab/NextGAN.git?style=social)](https://github.com/LINs-lab/NextGAN.git)  
  Keywords: dit, text to video, text-to-video, video generation  
- **[Grounding in the Dark: Text-Only Training for Zero-Shot Video Temporal Localization](https://arxiv.org/abs/2611.06149v2)**  
  Authors: Divyanshu Mishra, Sabine Sternig, Rakshith Shetty, Erhan Gundogdu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.06149v2.pdf)  
  Keywords: benchmark, text to video, text-to-video  
- **[What Remains in Sight? Autoregressive Video Decoding as Representation-Guided Context Rewriting](https://arxiv.org/abs/2611.04164v1)**  
  Authors: Lixuan He, Jihyeon Je, Yang You, Leonidas Guibas  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.04164v1.pdf)  
  Keywords: autoregressive, autoregressive video, long video, text to video, text-to-video, video generation  
- **[Synthetic Realities: Evaluating Human Ability to Distinguish AIGenerated Videos from Real Footage](https://arxiv.org/abs/2611.01990v1)**  
  Authors: Danyal Sarfraz, Raja Mubashar Karim, KwanMyung Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.01990v1.pdf)  
  Keywords: evaluation, film, image to video, image-to-video, outpainting, text to video, text-to-video, video outpainting, video synthesis  
- **[Wave Forcing: Towards Speed-of-Light Streaming Video Generation](https://arxiv.org/abs/2611.00859v1)**  
  Authors: Yijie Jin, Yuxuan Liu, Jiajun Xu, Ye Huang, Chuzhi Wang, Jiayang Li, Ruiyang Chen, Chenling Hong, Xu Wang, Zhijie Deng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.00859v1.pdf)  
  Keywords: autoregressive, denoising, dit, long video, streaming, streaming video generation, t2v, video generation  
- **[Running a 20B Video Diffusion Transformer on Consumer Hardware: A Deployment and Measurement Report for MiniMax H3 on Apple Silicon](https://arxiv.org/abs/2611.00843v2)**  
  Authors: Zhenzhou, Shi, Yizhe, Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.00843v2.pdf)  
  Keywords: diffusion transformer, dit, temporal consistency, text to video, text-to-video, video diffusion, video diffusion transformer  
- **[UniCaMo: Unified Camera and Motion Control for Video Diffusion Models](https://arxiv.org/abs/2611.00810v1)**  
  Authors: Long Vu, Tan Ngo, Animesh Karnewar, Amir Habibian, Binh-Son Hua, Hung Bui, Minh Hoai Nguyen, Phong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.00810v1.pdf)  
  Keywords: camera trajectory, controllable, motion control, text to video, text-to-video, trajectory, video diffusion, video generation  
- **[A Better Critic Matters for Distribution Matching Distillation](https://arxiv.org/abs/2610.42135v1)**  
  Authors: Zongze Wu, Xianbang Wang, Zhengyang Geng, Mingdeng Cao, Zhoutong Zhang, Richard Zhang, Eli Shechtman, Ruiming Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.42135v1.pdf)  
  Keywords: distillation, text to video, text-to-video, video generation  
- **[MEV: A Multi-Event Video Dataset for Long-Take Generation](https://arxiv.org/abs/2610.38241v1)**  
  Authors: Peiyuan Zhu, Shaoan Xie, Yifan Shen, Wen Tian, Zijian Li, Guangyi Chen, Kun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.38241v1.pdf)  
  Keywords: evaluation, text to video, text-to-video, video generation  

### Video Editing

*Showing the latest 50 out of 90 papers*

- **[VideoEditor-MoE: Scaling Complex Video Editing with Mixture of Experts](https://arxiv.org/abs/2611.03043v1)**  
  Authors: Xiao Cao, Fuchen Long, Yansong Qu, Wen Xiao, Xin Zhang, Xinlong Sun, Xi Chen, Zhiyong Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.03043v1.pdf)  
  Keywords: video editing  
- **[MoviEdit: Long-form Multi-Shot Video Editing Made Easy](https://arxiv.org/abs/2611.02737v1)**  
  Authors: Suhyeon Lee, Zhengang Li, Soo Ye Kim, Peihao Zhu, Jong Chul Ye, Chun-Hao Paul Huang, Duygu Ceylan, Yan Kang, Hyeonho Jeong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.02737v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://multi-shot-edit.github.io)  
  Keywords: autoregressive, benchmark, evaluation, long-form, video editing  
- **[FilmTogether: Cinematic Video Generation from Low-Cost Inputs](https://arxiv.org/abs/2611.00899v1)**  
  Authors: Shiying Zhang, Xiaobin Hu, Qianchi Zhang, Jiaqi Zhao, Xiaoda Yang, Bo Yin, Shuicheng Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.00899v1.pdf)  
  Keywords: cinematic, identity, layout, video editing, video generation  
- **[Multimodal Concert Video Editing: System Design and Exploratory Evaluation](https://arxiv.org/abs/2610.35816v1)**  
  Authors: Lennart Schiweck, Adrian Kempf, Michelle Retig, Moritz Feucht, Tim Mangliers, Benjamin Himpel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.35816v1.pdf)  
  Keywords: architecture, evaluation, video editing  
- **[VidEdit3D: Flexible 3D Gaussian Editing with Video Diffusion](https://arxiv.org/abs/2610.35756v1)**  
  Authors: Yanming Yang, Chenxi Song, Tong Zhao, Juntao Xu, Wenhao Rao, Yiwen Chen, Yiwei Wang, Chi Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.35756v1.pdf)  
  Keywords: dynamics, trajectory, video diffusion, video editing  
- **[Demystifying Prompt Stealing Attacks against Synthetic Video](https://arxiv.org/abs/2611.00102v1)**  
  Authors: Junyan Huang, Sanskar Agmain, Chen Gong, Yan Pang, FNU Suya  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.00102v1.pdf)  
  Keywords: benchmark, customization, layout, trajectory, video to video, video-to-video  
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

### Video Inpainting & Completion

- **[FloMo: 3D Scene Flow as a World Action Model Intermediate for Learning from Human Video](https://arxiv.org/abs/2611.05062v2)**  
  Authors: Jeremy Collins, Namra Patel, Ayush Agarwal, Shitij Govil, Animesh Garg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.05062v2.pdf)  
  Keywords: video generation, video prediction  
- **[Future Representation Distillation for Imagination-free World Action Models](https://arxiv.org/abs/2611.04527v2)**  
  Authors: Jaehyeong Jo, Sangwon Jang, Sihyun Yu, Seonghyeon Ye, Yekyung Nah, Hojung Jung, Kimin Lee, Sung Ju Hwang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.04527v2.pdf)  
  Keywords: denoising, diffusion model, distillation, video denoising, video diffusion, video prediction  
- **[Synthetic Realities: Evaluating Human Ability to Distinguish AIGenerated Videos from Real Footage](https://arxiv.org/abs/2611.01990v1)**  
  Authors: Danyal Sarfraz, Raja Mubashar Karim, KwanMyung Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.01990v1.pdf)  
  Keywords: evaluation, film, image to video, image-to-video, outpainting, text to video, text-to-video, video outpainting, video synthesis  
- **[Recoverability-Aware Evaluation of Diffusion Video Inpainting and Object Removal](https://arxiv.org/abs/2611.01578v1)**  
  Authors: Yanliang Qi, Jiacheng Ding, Cong Guo, Peihua Mai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.01578v1.pdf)  
  Keywords: evaluation, video diffusion, video inpainting  
- **[RynnWorld-Latent: A Cross-Embodiment World Model Conditioned on Universal Latent Actions](https://arxiv.org/abs/2610.36791v1)**  
  Authors: Haoyu Zhao, Yinzhou Tang, Zixuan Wang, Minghao Zhu, Dongchi Huang, Xingyue Zhao, Qin Zhao, Kehan Li, Siteng Huang, Xin Li, Zhenyu Zeng, Mingxiu Chen, Deli Zhao, Zhongyu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.36791v1.pdf)  
  Keywords: controllable, dynamics, identity, simulation, video prediction, video world model, world model  
- **[What Does World Modeling Actually Improve in Robot Action Learning?](https://arxiv.org/abs/2610.34593v2)**  
  Authors: Hanwen Cui, Yuanyuan Li, Qing Guo, Zhida Zhang, Chao Chen, Xi Chen, Jie Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.34593v2.pdf)  
  Keywords: architecture, diffusion transformer, dit, trajectory, video diffusion, video diffusion transformer, video prediction  
- **[TrackTok: Object-Centric Video Tokenization with Semantically Persistent Tokens](https://arxiv.org/abs/2610.33857v2)**  
  Authors: Nhi Pham, Christopher Wewer, Bernt Schiele, Jonas Fischer, Jan Eric Lenssen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.33857v2.pdf) | [![GitHub](https://img.shields.io/github/stars/phamleyennhi/tracktok?style=social)](https://github.com/phamleyennhi/tracktok)  
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

### Video Super-Resolution & Enhancement

*Showing the latest 50 out of 180 papers*

- **[CoGenRec: A Unified Generative Framework for Complementary Vision Reconstruction](https://arxiv.org/abs/2611.07665v1)**  
  Authors: Yapeng Meng, Yuguo Chen, Xiangru Chen, Shaojun Xu, Xuezhen Wang, Lijian Wang, Zheyu Yang, Yihan Lin, Luping Shi, Rong Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.07665v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://cogenrec.github.io)  
  Keywords: diffusion model, frame interpolation, physical, video deblurring, video diffusion  
- **[Training-Free Predictive Spatio-Temporal Token Pruning for Few-Step Autoregressive Video Diffusion](https://arxiv.org/abs/2611.07551v1)**  
  Authors: Jia Li, Xurui Peng, Xing Wang, Hayden Kwok-Hay So  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.07551v1.pdf)  
  Keywords: autoregressive, autoregressive video, denoising, distillation, efficient, trajectory, video diffusion, video generation  
- **[VA-TDM: A Unified View for Improving Few-Step Diffusion Models by Velocity Adversarial Distillation](https://arxiv.org/abs/2611.06796v1)**  
  Authors: Yihong Luo, Tianyu Pang, Tianyang Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.06796v1.pdf)  
  Keywords: denoising, distillation, efficient, flow matching, text to video, text-to-video, trajectory, video generation  
- **[DecoupAttn: Decoupled Sparse Attention for Training-Free Acceleration of Video Diffusion](https://arxiv.org/abs/2611.05917v1)**  
  Authors: Yanjin Li, Bingbing Qiu, Qiang Huang, Rui Qian, Yanfeng Li, Jian Wang, Xiaoying Tang, Mingda Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.05917v1.pdf)  
  Keywords: acceleration, denoising, sparse attention, video diffusion  
- **[Future Representation Distillation for Imagination-free World Action Models](https://arxiv.org/abs/2611.04527v2)**  
  Authors: Jaehyeong Jo, Sangwon Jang, Sihyun Yu, Seonghyeon Ye, Yekyung Nah, Hojung Jung, Kimin Lee, Sung Ju Hwang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.04527v2.pdf)  
  Keywords: denoising, diffusion model, distillation, video denoising, video diffusion, video prediction  
- **[TaoMate-HD: Progressive-Resolution Autoregressive Audio-Video Generation](https://arxiv.org/abs/2611.03394v1)**  
  Authors: Qijun Gan, Chenwei Zhang, Xinyang Li, Meiguang Jin, Junfeng Ma, Shen Qiu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.03394v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://taoliveaigc.github.io/TaoMate-HD)  
  Keywords: audio-video generation, autoregressive, denoising, distillation, streaming, trajectory, video generation  
- **[TaoMate-FVSR: Audio-Guided Facial Video Restoration](https://arxiv.org/abs/2611.03393v2)**  
  Authors: Xinyang Li, Zeran Xu, Jingna Sun, Qijun Gan, Chenwei Zhang, Meiguang Jin, Junfeng Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.03393v2.pdf)  
  Keywords: diffusion transformer, identity, talking head, temporal consistency, video diffusion, video diffusion transformer, video restoration  
- **[Generative diffusion in long-range correlated landscapes: Speciation cascade and the foam structure of the score](https://arxiv.org/abs/2611.02955v1)**  
  Authors: Jerome Garnier-Brun, Giulio Biroli, Marc Mézard, Jean-Philippe Bouchaud  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.02955v1.pdf)  
  Keywords: autoregressive, denoising, trajectory, video generation  
- **[W2A: Distilling World Priors into Action Models for Real-Time Robotic Control](https://arxiv.org/abs/2611.02600v1)**  
  Authors: Xiaopeng Zhang, Yongjin Mu, Yueyang Weng, Chengzhi Zhao, Yanjie Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.02600v1.pdf)  
  Keywords: denoising, diffusion model, distillation, simulation, video diffusion  
- **[What Helps Denoising Can Hurt Memory: Rethinking History in Long Video Generation](https://arxiv.org/abs/2611.00937v1)**  
  Authors: Yubin Jing, Ziyang Zhang, Meng Chen, Yuyao Li, Haofan Wang, Yichen Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.00937v1.pdf)  
  Keywords: autoregressive, autoregressive video, denoising, long video, temporal consistency, video generation  

### World Models & Simulation

*Showing the latest 50 out of 233 papers*

- **[EgoGeneralist: Unifying Egocentric Action-Video Tasks through Video-Native Modeling](https://arxiv.org/abs/2611.08477v1)**  
  Authors: Yanlin Jin, Bowen Yang, Cheng Zhang, Yifan Yang, Zhe Li, Jianfei Cai, Kai Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.08477v1.pdf)  
  Keywords: action-conditioned, dynamics, human motion, video generation  
- **[GuidedWAM: Training-Free Energy Guidance for World Action Models in Autonomous Driving](https://arxiv.org/abs/2611.07912v1)**  
  Authors: Xiyan Su, Finn Rasmus Schäfer, Hojun Lim, Frank Diermeyer, Johannes Betz, Markus Lienkamp  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.07912v1.pdf)  
  Keywords: autonomous driving, driving, visual world model, world model  
- **[TouchéWorld tech report : Towards Online Unified Camera--Hand Exploration in Generative Worlds](https://arxiv.org/abs/2611.06061v1)**  
  Authors: Jiaao Yu, Yanjian Zhang, Haoyang Jiang, Guillaume Wisniewski, Nadi Tomeh, Shijie Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.06061v1.pdf)  
  Keywords: distillation, efficient, gesture, video world model, world model  
- **[Compression Forcing: Hierarchical History Tokenization Enables Flexible World Models](https://arxiv.org/abs/2611.04028v1)**  
  Authors: Siqiao Huang, Partha Kaushik, Michael Chen, Hengkai Pan, Kaiwen Geng, Omar Chehab, Fernando Moreno-Pino, Max Simchowitz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.04028v1.pdf)  
  Keywords: dynamics, dynamics-aware, physical, video generation, world model  
- **[W2A: Distilling World Priors into Action Models for Real-Time Robotic Control](https://arxiv.org/abs/2611.02600v1)**  
  Authors: Xiaopeng Zhang, Yongjin Mu, Yueyang Weng, Chengzhi Zhao, Yanjie Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.02600v1.pdf)  
  Keywords: denoising, diffusion model, distillation, simulation, video diffusion  
- **[AgiWorld: An Agentic Video World Model for Building Persistent Worlds](https://arxiv.org/abs/2611.02341v1)**  
  Authors: Shaoheng Fang, Yiqun Mei, Hanwen Jiang, Xin Sun, Haitian Zheng, Hao Tan, Kalyan Sunkavalli, Georgios Pavlakos, Qixing Huang, Yiwei Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2611.02341v1.pdf)  
  Keywords: camera motion, interactive, minute-long, video world model, world model  
- **[GeoFlip Preview: Benchmarking Geometry-Sensitive Physics in Video Generation](https://arxiv.org/abs/2610.42002v2)**  
  Authors: Yuqi Li, Junming Liu, Bowen Hu, Ruize Niu, Huiran Duan, Ming-Hsuan Yang, Yingli Tian, Hao Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.42002v2.pdf)  
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
