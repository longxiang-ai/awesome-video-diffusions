# Awesome Video Diffusions [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Video Diffusion Models and Video Generation. Content is automatically updated daily.

> Last Update: 2026-08-05 02:29:59

## 📰 Latest Updates

🚀 **[2026-02] Project Launched — v1.0**
- Adapted from [awesome-gaussians](https://github.com/limingwei/awesome-gaussians) framework for tracking video diffusion research
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

- [3D-aware Video Generation](#3d-aware-video-generation) (21 papers) - Video generation with 3D awareness, multi-view consistency, and 4D content creation
- [Applications](#applications) (50 papers) - Domain-specific applications of video diffusion models
- [Architecture & Efficiency](#architecture-&-efficiency) (358 papers) - Architectural innovations (DiT, UNet), flow matching, and training/inference efficiency
- [Audio & Multi-modal](#audio-&-multi-modal) (20 papers) - Audio-driven and multi-modal conditioned video generation
- [Controllable Generation](#controllable-generation) (137 papers) - Controllable video generation with motion, camera, pose, or layout guidance
- [Human & Character Animation](#human-&-character-animation) (26 papers) - Human-centric video generation including talking heads, dance, and character animation
- [Image-to-Video Generation](#image-to-video-generation) (55 papers) - Methods for animating still images into videos
- [Long Video Generation](#long-video-generation) (127 papers) - Generating temporally consistent long-form videos beyond short clips
- [Personalization & Customization](#personalization-&-customization) (93 papers) - Personalized video generation with custom subjects, identities, or styles
- [Physical Understanding](#physical-understanding) (153 papers) - Physics-aware video generation and dynamics modeling
- [Surveys & Benchmarks](#surveys-&-benchmarks) (226 papers) - Survey papers, benchmarks, and evaluation metrics for video generation
- [Text-to-Video Generation](#text-to-video-generation) (78 papers) - Foundation models and methods for generating videos from text prompts
- [Video Editing](#video-editing) (23 papers) - Diffusion-based video editing, style transfer, and manipulation
- [Video Inpainting & Completion](#video-inpainting-&-completion) (8 papers) - Video inpainting, completion, outpainting, and temporal prediction
- [Video Super-Resolution & Enhancement](#video-super-resolution-&-enhancement) (71 papers) - Video quality improvement, upscaling, restoration, and frame interpolation
- [World Models & Simulation](#world-models-&-simulation) (128 papers) - Video generation as world simulators and interactive environment generation



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3D-aware Video Generation

- **[AniGS: Bridging Rendering and Diffusion Prior for 3D Scene Animation](https://arxiv.org/abs/2607.18539v1)**  
  Authors: Yen-Chi Cheng, Chen Gao, Chuhan Chen, Tuotuo Li, Rajvi Shah, Ayush Saraf, Changil Kim, Liangyan Gui, Alexander Schwing, Johannes Kopf, Hung-Yu Tseng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.18539v1.pdf)  
  Keywords: diffusion model, video-to-video, novel view, video diffusion, dynamics, dit  
- **[Delving into the Temporal Challenges of Unified Video Protection Against Image-to-Video and Fine-Tuning-based Customization](https://arxiv.org/abs/2607.13336v1)**  
  Authors: Yuxin Huang, Ziming Hong, Mingming Gong, Wanyu Wang, Jing Zhang, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.13336v1.pdf)  
  Keywords: customization, video generation, diffusion model, image-to-video, video diffusion, 3d video, identity, dit  
- **[4D Human-Scene Reconstruction from Low-Overlap Captures](https://arxiv.org/abs/2607.09125v1)**  
  Authors: Minhyuk Hwang, Sangmin Kim, Seunguk Do, Daneul Kim, Jaesik Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.09125v1.pdf)  
  Keywords: trajectory, diffusion model, novel view, video diffusion, identity  
- **[SoccerNet 2026 Challenges Results](https://arxiv.org/abs/2607.07320v1)**  
  Authors: Anthony Cioppa, Silvio Giancola, Håkan Ardö, Mohamad Dalal, Jan Held, Jérémie Ochin, Jiayuan Rao, Karen Sanchez, Renaud Vandeghen, Artur Xarles, Olivier Barnich, Albert Clapés, Mathieu Delvaux, Sergio Escalera, Bernard Ghanem, Cédric Hons, Antoine Houet, Sotiris Manitsaris, Tom Michel, Pierre Miralles, Thomas B. Moeslund, Mikael Nilsson, Bogdan Stanciulescu, Marc Van Droogenbroeck, Yanfeng Wang, Weidi Xie, Faisal Altawijri, Mohamed Atef, Semen Budennyy, Vasiliy Chelpanov, Puhua Chen, Yixin Chen, Lechao Cheng, Jianling Chu, Ju-Seong Do, Oleg Durygin, Omar Fetouh, Mirco Fuchs, Youssef Ghallab, Falguni Ghosh, Wonjun Heo, Yufeng Hu, Weixuan Huang, Phuong-Linh Huynh-Ha, Matvey Isupov, Yangguang Ji, Siyuan Jiang, Zhenxiang Jiang, Wonyong Jo, Ho-Young Jung, SeongHeon Kang, MinJae Kim, Youngseon Kim, Jakub Komosa, Artem Konshin, Trung-Hoang Le, Jongmin Lee, Lingling Li, Litao Li, Vadim Linkov, Fang Liu, Haoxuan Ma, Shun Makino, Ismail Mathkour, Konstantin Mitin, Mikhail Moiseev, Takumi Nagaya, Yuki Nakamura, Thanh-Khoi Nguyen, Hoang-Phuc Nguyen, Trong-Thuan Nguyen, Christian Orduz, Kwanyong Park, Fabian Perez, Parthsarthi Rawat, SuHyun Rim, Hoover Rueda-Chacón, Atom Scott, Minori Sugimura, Yuyang Sun, Shengeng Tang, Minh-Triet Tran, Ikuma Uchida, Juan Vanegas, Thanh-Nhan Vo, Jiangtao Wang, Yaxiong Wang, Xiaogang Wang, Ruifeng Wang, Rio Watanabe, Jiali Wen, Yongliang Wu, Di Yang, Xu Yang, Zhuo Yang, Xinyu Ye, Yibo Yu, Zihan Zhai, Yu Zhang, Zhenyu Zhao, Zhun Zhong, Yixi Zhou, Xingyu Zhu, Wenbo Zhu, Julian Ziegler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.07320v1.pdf)  
  Keywords: benchmark, evaluation, dit, novel view  
- **[MV-Forcing: Long Multi-View Video Generation via 4D-Grounded Spatio-Temporal Self-Forcing](https://arxiv.org/abs/2607.05376v1)**  
  Authors: Gal Fiebelman, Hadar Averbuch-Elor, Sagie Benaim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.05376v1.pdf)  
  Keywords: autoregressive, distillation, video generation, diffusion model, multi-view video, denoising, video diffusion  
- **[HandsOnWorld: Unconstrained Egocentric Video Generation with Camera-Disentangled Hand Control](https://arxiv.org/abs/2607.02075v1)**  
  Authors: Yushuo Chen, Xiaoyu Shi, Xiaoshi Wu, Xintao Wang, Pengfei Wan, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.02075v1.pdf)  
  Keywords: 3d-aware, video generation  
- **[NeoMap: Training-free Novel-View Synthesis from Single Images and Videos](https://arxiv.org/abs/2607.01962v1)**  
  Authors: Jinxi Li, Tianyi Zhang, Yafei Yang, Zihui Zhang, Peng Huang, Koon Wing Macgyver Lin, Bo Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.01962v1.pdf)  
  Keywords: denoising, novel view, video synthesis, benchmark, dit  
- **[RayPE: Ray-Space Positional Encoding for 3D-Aware Video Generation](https://arxiv.org/abs/2606.27345v2)**  
  Authors: Minghao Yin, Jiahao Lu, Wenbo Hu, Wang Zhao, Shan Ying, Kai Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.27345v2.pdf)  
  Keywords: diffusion transformer, video generation, 3d-aware, video diffusion, camera control, identity, dit  
- **[Follow Your Track: Precise Skeleton Animation Controlled by 3D Trajectories](https://arxiv.org/abs/2606.25344v1)**  
  Authors: Yueting Liu, Yanqin Jiang, Nian Liu, Jingmen Zhou, Zhengjun Zha, Weiming Hu, Jin Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.25344v1.pdf)  
  Keywords: trajectory, 4d generation, body motion, efficient, temporal consistency, dit  
- **[OmniDrive: An LLM-Choreographed Multi-Agent World Model with Unified Latent Co-Compression for Multi-View Driving Video Generation](https://arxiv.org/abs/2606.17536v1)**  
  Authors: Zijie Meng, Yufei Liu, Chengqian Ma, Zhiyu Li, Jiyuan Liu, Wenhua Nie, Bingcai Wei, Shuqin Chen, Weichen Xu, Jiquan Yuan, Miao Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.17536v1.pdf)  
  Keywords: autonomous driving, video generation, controllable, multi-view video, world model, layout, dit  

### Applications

- **[RealWeather: Realistic and Scene-Faithful Weather Translation with Driving World Models](https://arxiv.org/abs/2608.02953v1)**  
  Authors: Yuwei Ning, Liangzhi Wang, Yi Xiao, Zhenhua Wu, Yun Pang, Mingkun Chan, Jichang Li, Guanbin Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.02953v1.pdf)  
  Keywords: autonomous driving, world model, dynamics, dit, style  
- **[Mitigating Compounding Error via Video Representation Regularization](https://arxiv.org/abs/2607.27036v1)**  
  Authors: Taiye Chen, Qi Zhang, Yisen Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.27036v1.pdf)  
  Keywords: autonomous driving, autoregressive, robotics, video generation, simulation, world model, video diffusion, long video, dynamics  
- **[CG-World: A Large-Scale World-State Dataset and Protocol for World Models](https://arxiv.org/abs/2607.26452v1)**  
  Authors: Yiming Cai, Fangjie Yu, Meiqing Yu, Ziyue Shi, Pengfei Yuan, Yong Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.26452v1.pdf)  
  Keywords: robotics, video generation, simulation, world model, physical, dynamics, physics, dit  
- **[FilmBench: A Film-Grade Benchmark for Cinematic Video Generation](https://arxiv.org/abs/2607.24241v2)**  
  Authors: Shengyi Wang, Niantong Li, Guangzheng Hu, Hong Qi, Fei Ding, Weixu Qiao, Jinlin Wang, Xiaotong Lv, Peng Han, Zimeng Li, Fanshu Ding, Yushu Wang, Han Wu, Jingjing Chen, Chongxiao Wang, Yanhao Wu, Chenglong Huang, Xiaoqian Zhu, Jie Tian, Hua Li, Jingjing Fan, Mingshuang Tang, Zhong Li, Hengxia Qiang, Weibin Chen, Jinyang Zhen, Bing Zhao, Lin Qu, Jing Li, Hu Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.24241v2.pdf)  
  Keywords: t2v, video generation, text-to-video, evaluation, film, benchmark, dit, style  
- **[HALLELUAI: A Hallucination-Aware AI System for Ultra-Realistic Image-to-Video Generation at Scale](https://arxiv.org/abs/2607.22959v1)**  
  Authors: Aniket Sakpal, Yang Jiang, Rouzbeh Davoudi, Shayan Hassantabar, Mani Najmabadi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.22959v1.pdf)  
  Keywords: creative, evaluation, video generation, image-to-video  
- **[ID-V2V: Identity-Preserving Video Restylization](https://arxiv.org/abs/2607.22830v1)**  
  Authors: Yuancheng Xu, Mingming He, Pablo Salamanca, Li Ma, Yash Kant, Emmett Steven, Paul Debevec, Ning Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.22830v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Eyeline-Labs/ID-V2V?style=social)](https://github.com/Eyeline-Labs/ID-V2V)  
  Keywords: creative, video-to-video, identity, video synthesis, dit, style  
- **[SafeGen: Goal-Conditioned Video Diffusion of Safety-Critical Scenarios for VLM-Based Autonomous Driving](https://arxiv.org/abs/2607.19701v1)**  
  Authors: Jiangfan Liu, Zexuan Cui, Tianyuan Zhang, Zonglei Jing, Zonghao Ying, Yaoyuan Zhang, Jiakai Wang, Xiaoqi Jiang, Aishan Liu, Xianglong Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.19701v1.pdf)  
  Keywords: autonomous driving, evaluation, physical, video diffusion, dynamics, dit  
- **[D3VL: Understanding Driving Scenes from 3D Time Series Data and Video with Language Models](https://arxiv.org/abs/2607.19528v1)**  
  Authors: Heesang Han, A. Lynn Abbott, Abhijit Sarkar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.19528v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://automotivesafety-lvlm.github.io)  
  Keywords: autonomous driving, architecture, dit  
- **[FilmWorld: Agentic Novel-to-Film Generation through Dynamic Cinematic World Modeling](https://arxiv.org/abs/2607.19038v1)**  
  Authors: Jialong Zuo, Haotong Zuo, Shiwei Zhang, Xiang Wang, Chen Li, Nong Sang, Changxin Gao, Xiang Bai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.19038v1.pdf)  
  Keywords: video generation, evaluation, world model, long-form, film, benchmark  
- **[SGA: Plug&Play Geometric Verification for Educational Video Synthesis](https://arxiv.org/abs/2607.18116v1)**  
  Authors: Lopez Jhon, Hinojosa Carlos, Ghanem Bernard  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.18116v1.pdf)  
  Keywords: benchmark, education, video synthesis  

### Architecture & Efficiency

*Showing the latest 50 out of 358 papers*

- **[SPADE: An Input-Adaptive Sparse Attention Engine for Fast Video Diffusion Models Inference](https://arxiv.org/abs/2608.03335v1)**  
  Authors: Shanghao Liu, Renze Chen, Size Zheng, Yuanqiang Liu, Yun, Liang, Hailong Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.03335v1.pdf) | [![GitHub](https://img.shields.io/github/stars/6somehow/DAC-SPADE?style=social)](https://github.com/6somehow/DAC-SPADE)  
  Keywords: diffusion transformer, video generation, text-to-video, diffusion model, video diffusion, image-to-video, dit  
- **[Adaptive Two-Stage Visual Token Pruning for Efficient Inference in Video-Language Models](https://arxiv.org/abs/2608.03112v1)**  
  Authors: Paribesh Regmi, Qingshuang Chen, Chi Zhang, Heba Aly, Yelin Kim, Hongda Mao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.03112v1.pdf)  
  Keywords: efficient, benchmark, dit  
- **[CAPE-T2V: Captioner-Anchored Prompt Enhancement toward Two-Sided Conditioning Alignment in Text-to-Video Generation](https://arxiv.org/abs/2608.03046v1)**  
  Authors: Yizhuo Jia, Jingyun Hua, Yuanxing Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.03046v1.pdf) | [![GitHub](https://img.shields.io/github/stars/yizzz927/CAPE-T2V?style=social)](https://github.com/yizzz927/CAPE-T2V)  
  Keywords: t2v, diffusion transformer, video generation, text-to-video, dit  
- **[Qwen-3D: A Generalist 3D Vision-Language Model for Spatial Understanding](https://arxiv.org/abs/2608.02980v1)**  
  Authors: Lucy Lin, Ayush Jain, Yifan Liu, Katerina Fragkiadaki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.02980v1.pdf)  
  Keywords: efficient, long video, benchmark  
- **[RealWeather: Realistic and Scene-Faithful Weather Translation with Driving World Models](https://arxiv.org/abs/2608.02953v1)**  
  Authors: Yuwei Ning, Liangzhi Wang, Yi Xiao, Zhenhua Wu, Yun Pang, Mingkun Chan, Jichang Li, Guanbin Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.02953v1.pdf)  
  Keywords: autonomous driving, world model, dynamics, dit, style  
- **[WorldExam: Benchmarking World Models from Apparent Appearance to Inherent Reactivity](https://arxiv.org/abs/2608.02603v1)**  
  Authors: Yuxue Yang, Shuyao Shang, Jiahe Wang, Zitong Zhou, Liang Tan, Junhan Zeng, Ruizhi Li, Junyan Li, Yu Liu, Xiao Yang, Yong Li, Jun Zhu, Hongsheng Li, Tieniu Tan, Lue Fan, Zhaoxiang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.02603v1.pdf)  
  Keywords: video generation, controllable, evaluation, world model, camera control, benchmark, dit  
- **[Estimating SSIM from MSE for DCT-Based Compressed Images](https://arxiv.org/abs/2608.02549v1)**  
  Authors: Luc Trudeau, Maria G. Martini  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.02549v1.pdf)  
  Keywords: efficient, streaming  
- **[Token Radius Attention for Efficient Video Generation](https://arxiv.org/abs/2608.02504v1)**  
  Authors: Jiayu Chen, Zhikun Jiang, Maoliang Li, Jiayi Luo, Jiawei Yang, Zihao Zheng, Hengyi Zhang, Guojie Luo, Xiang Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.02504v1.pdf) | [![GitHub](https://img.shields.io/github/stars/IF-LAB-PKU/Token-Radius-Attention?style=social)](https://github.com/IF-LAB-PKU/Token-Radius-Attention)  
  Keywords: t2v, diffusion transformer, video generation, video diffusion, efficient, dit, i2v  
- **[EchoCache: Energy-Guided Cross-Modal Caching for Efficient Audio-Driven Video Generation](https://arxiv.org/abs/2608.02474v1)**  
  Authors: Jiayu Chen, Xiaoyu Wu, Rongshan Gao, Maoliang Li, Zihao Zheng, Xinhao Sun, Hailong Zou, Guojie Luo, Xiang Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.02474v1.pdf) | [![GitHub](https://img.shields.io/github/stars/IF-LAB-PKU/EchoCache?style=social)](https://github.com/IF-LAB-PKU/EchoCache)  
  Keywords: video generation, audio-driven, diffusion model, denoising, efficient, benchmark  
- **[HiResNets: Native Full-HD Video Recognition with Foveal Residual Streams](https://arxiv.org/abs/2608.02140v2)**  
  Authors: Shivani Mall, Swarnim Jain, Joao F. Henriques  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.02140v2.pdf)  
  Keywords: architecture  

### Audio & Multi-modal

- **[EchoCache: Energy-Guided Cross-Modal Caching for Efficient Audio-Driven Video Generation](https://arxiv.org/abs/2608.02474v1)**  
  Authors: Jiayu Chen, Xiaoyu Wu, Rongshan Gao, Maoliang Li, Zihao Zheng, Xinhao Sun, Hailong Zou, Guojie Luo, Xiang Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.02474v1.pdf) | [![GitHub](https://img.shields.io/github/stars/IF-LAB-PKU/EchoCache?style=social)](https://github.com/IF-LAB-PKU/EchoCache)  
  Keywords: video generation, audio-driven, diffusion model, denoising, efficient, benchmark  
- **[AcoustiTrace: When Plausible Sound Violates Physics](https://arxiv.org/abs/2608.02035v1)**  
  Authors: Shiyang Li, Yuewen Cao, Yihao Liu, Yuandong Pu, Baochang Zhang, Xiaofei Li, Changqing Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.02035v1.pdf)  
  Keywords: video generation, evaluation, physical, sound, benchmark, physics  
- **[LeapTalk: Breaking the Latency-Quality Trade-off in Talking Head Generation](https://arxiv.org/abs/2608.00079v1)**  
  Authors: Rongxiang Zhang, Songhua Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.00079v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zhangrongxiang.github.io/leaptalk-page)  
  Keywords: autoregressive, distillation, video generation, audio-driven, long-form, long video, efficient, identity, streaming, talking head  
- **[AptAvatar: Fast and Vivid Long-Form Audio-Driven Video Generation for Production-Ready Avatars](https://arxiv.org/abs/2607.24013v2)**  
  Authors: Hengyuan Zhang, Jingna Sun, Meiguang Jin, Junfeng Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.24013v2.pdf) | [![GitHub](https://img.shields.io/github/stars/TaoLiveAIGC/AptAvatar?style=social)](https://github.com/TaoLiveAIGC/AptAvatar)  
  Keywords: trajectory, distillation, video generation, audio-driven, long-form, efficient, identity, acceleration, avatar, dit  
- **[Bring Music The Horizon: Music-Driven 360$^\circ$ Video Generation](https://arxiv.org/abs/2607.13471v1)**  
  Authors: Kai Hsu Tsai, Yong Wei Fu, Hung I Yang, Yu-Chih Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.13471v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://etoile-et-toi-mp3.github.io/BMTH_Project_Page)  
  Keywords: trajectory, video generation, image-to-video, sound, dynamics, dit, music video  
- **[HumanForge: A Human-Centric Deepfake Video Benchmark with Multi-Agent Forgery Rationales](https://arxiv.org/abs/2607.08705v1)**  
  Authors: Wenbo Xu, Zhimin Chen, Xiaojie Liang, Hengrui Liu, Wei Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.08705v1.pdf)  
  Keywords: text-to-video, diffusion model, video diffusion, video synthesis, multi-modal, benchmark, dit  
- **[AVTok: 1D Unified Tokenization for Holistic Audio-Video Generation](https://arxiv.org/abs/2606.30811v1)**  
  Authors: Kien T. Pham, I Chieh Chen, Qifeng Chen, Long Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30811v1.pdf)  
  Keywords: video generation, efficient, architecture, audio-to-video, sound, dit  
- **[TRUST: Efficient Abdominal Trauma Recognition via Image-to-Ultrasound-Video Transfer Learning](https://arxiv.org/abs/2606.27777v1)**  
  Authors: Enguang Wang, Hao Zhou, Shuo Gao, Tuo Liu, Guangquan Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.27777v1.pdf)  
  Keywords: image-to-video, efficient, dynamics, sound, dit  
- **[PhyEditBench: A Real-World Multi-Stage Benchmark for Physics-Aware Image Editing](https://arxiv.org/abs/2606.26551v2)**  
  Authors: Shengbin Guo, Shaokang He, Chaoyue Meng, Shengpeng Xiao, Xunzhi Xiang, Shaofeng Zhang, Qi Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.26551v2.pdf) | [![GitHub](https://img.shields.io/github/stars/Previsior/PhyEditBench?style=social)](https://github.com/Previsior/PhyEditBench)  
  Keywords: video generation, evaluation, physical, dynamics, multi-modal, physics-aware, benchmark, physics, dit  
- **[Wan-Streamer v0.1: End-to-end Real-time Interactive Foundation Models](https://arxiv.org/abs/2606.25041v3)**  
  Authors: Lianghua Huang, Zhi-Fan Wu, Wei Wang, Yupeng Shi, Mengyang Feng, Junjie He, Chen-Wei Xie, Yu Liu, Jingren Zhou, Ang Wang, Bang Zhang, Baole Ai, Chen Liang, Cheng Yu, Chongyang Zhong, Jinwei Qi, Kai Zhu, Pandeng Li, Peng Zhang, Wenyuan Zhang, Xinhua Cheng, Yitong Huang, Yun Zheng, Yuzheng Wang, Zoubin Bi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.25041v3.pdf)  
  Keywords: streaming, avatar, interactive, audio-driven  

### Controllable Generation

*Showing the latest 50 out of 137 papers*

- **[GVCCTurbo: Rate-Compute Quality Scheduling for Codebook Driven Generative Compression](https://arxiv.org/abs/2608.03517v1)**  
  Authors: Ziyue Zeng, Dingjie Peng, Xun Su, Hiroshi Watanabe  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.03517v1.pdf)  
  Keywords: trajectory, evaluation, style, controllable  
- **[SUV: Future Scene Understanding as Video Generation for End-to-End Driving](https://arxiv.org/abs/2608.03084v1)**  
  Authors: Yibo Yuan, Jiacheng Fu, Jiangtong Zhu, Yi Li, Jianhua Han, Meng Tian, Zhuohan Liu, Zhiwei Xiong, Hang Xu, Jianwu Fang, Jianru Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.03084v1.pdf)  
  Keywords: trajectory, benchmark, video generation, dynamics  
- **[WorldExam: Benchmarking World Models from Apparent Appearance to Inherent Reactivity](https://arxiv.org/abs/2608.02603v1)**  
  Authors: Yuxue Yang, Shuyao Shang, Jiahe Wang, Zitong Zhou, Liang Tan, Junhan Zeng, Ruizhi Li, Junyan Li, Yu Liu, Xiao Yang, Yong Li, Jun Zhu, Hongsheng Li, Tieniu Tan, Lue Fan, Zhaoxiang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.02603v1.pdf)  
  Keywords: video generation, controllable, evaluation, world model, camera control, benchmark, dit  
- **[UniMoCa: Unifying Motion and Camera Controls as Visual Proxies for Faithful Human Video Generation](https://arxiv.org/abs/2608.01944v1)**  
  Authors: Liming Tan, Ye Chen, Hao Zhang, Lirong Qian, Feifei Li, Bingbing Ni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01944v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://tanliming-daniel.github.io/UniMoCa)  
  Keywords: trajectory, video generation, body motion, dit, camera control, identity, temporal consistency, human motion, motion control, i2v  
- **[DreamTraj: Generating 6-DoF Object Trajectories by Reading Unrendered Video Diffusion Latents](https://arxiv.org/abs/2608.00486v1)**  
  Authors: Tongsheng Ding, Zhen Luo, Yixuan Yang, Boyu Wang, Luyang Xie, Jinyu Yang, Feng Zheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.00486v1.pdf)  
  Keywords: trajectory, diffusion model, denoising, image-to-video, video diffusion  
- **[BWM: A Low-Cost High-Fidelity World Simulator for Robot Learning](https://arxiv.org/abs/2607.29302v1)**  
  Authors: BWM Team  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.29302v1.pdf)  
  Keywords: trajectory, autoregressive, action-conditioned, evaluation, world model, physical, world simulator, benchmark, physics, dit  
- **[Video Models as Native 4D Renderers: World-Grounded Conditioning from Animated Mesh](https://arxiv.org/abs/2608.00094v2)**  
  Authors: Junhao Chen, Mingjin Chen, Henghaofan Zhang, Minglin Chen, Liaoyuan Fan, Boran Zhang, Saining Zhang, Mingze Sun, Hao Zhao, Ruqi Huang, Zhihao Li, Yufei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.00094v2.pdf)  
  Keywords: trajectory, diffusion model, image-to-video, camera control, video diffusion, benchmark, dit  
- **[EgoGenesis: Egocentric World-Action Modeling with Online Anchored Projective Memory and Action-3D RoPE](https://arxiv.org/abs/2607.28243v1)**  
  Authors: Zexuan Yan, Yuzhou Wu, Yue Ma, Zonghang He, Kaibo Yin, Xiaobing Tu, Yinggui Wang, Jinkui Ren, Xiantao Zhang, Shijian Wang, Jinghong Liu, Linfeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.28243v1.pdf)  
  Keywords: autoregressive, dit, video generation, controllable  
- **[VideoCoCo: Code-as-CoT for Physically-Consistent Video Generation via an Agentic Dual-Engine System](https://arxiv.org/abs/2607.27380v1)**  
  Authors: Haodong Li, Tianfei Ren, Xiaoxiao Ma, Chunmei Qing, Zhen Fang, Sipeng He, Ziyu Guo, Haoyu Wu, Juanxi Tian, Yihang Zou, Ruichuan An, Dongzhi Jiang, Boxue Yang, Ji Xie, Xu Huang, Wenhao Yan, Jialv Zou, Zhengrong Yue, Yaxin Luo, Xiaotong Li, Yuzhu Wang, Junyan Ye, Jinjing Zhao, Zehui Chen, Lin Chen, Renye Yan, Feng Zhao, Pheng-Ann Heng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.27380v1.pdf)  
  Keywords: video generation, controllable, text-to-video, simulation, physical, dynamics, benchmark, dit  
- **[TPD: Temporal Prior Decoupling for Text-to-Video Diffusion Models](https://arxiv.org/abs/2607.26706v1)**  
  Authors: Taewon Kang, Matthias Zwicker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.26706v1.pdf)  
  Keywords: concept, trajectory, text-to-video, diffusion model, video diffusion, dit  

### Human & Character Animation

- **[UniMoCa: Unifying Motion and Camera Controls as Visual Proxies for Faithful Human Video Generation](https://arxiv.org/abs/2608.01944v1)**  
  Authors: Liming Tan, Ye Chen, Hao Zhang, Lirong Qian, Feifei Li, Bingbing Ni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01944v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://tanliming-daniel.github.io/UniMoCa)  
  Keywords: trajectory, video generation, body motion, dit, camera control, identity, temporal consistency, human motion, motion control, i2v  
- **[InteracVid: Building a Real Interactive Audio-Visual Response Dataset from Live-Chat Videos](https://arxiv.org/abs/2608.01157v1)**  
  Authors: Chi Zhang, Haoyang Shi, Yueyi Liu, Zhaokun Yan, Yishu Yin, Yuhang Wu, Miao Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01157v1.pdf)  
  Keywords: benchmark, evaluation, interactive, avatar  
- **[LeapTalk: Breaking the Latency-Quality Trade-off in Talking Head Generation](https://arxiv.org/abs/2608.00079v1)**  
  Authors: Rongxiang Zhang, Songhua Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.00079v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zhangrongxiang.github.io/leaptalk-page)  
  Keywords: autoregressive, distillation, video generation, audio-driven, long-form, long video, efficient, identity, streaming, talking head  
- **[AptAvatar: Fast and Vivid Long-Form Audio-Driven Video Generation for Production-Ready Avatars](https://arxiv.org/abs/2607.24013v2)**  
  Authors: Hengyuan Zhang, Jingna Sun, Meiguang Jin, Junfeng Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.24013v2.pdf) | [![GitHub](https://img.shields.io/github/stars/TaoLiveAIGC/AptAvatar?style=social)](https://github.com/TaoLiveAIGC/AptAvatar)  
  Keywords: trajectory, distillation, video generation, audio-driven, long-form, efficient, identity, acceleration, avatar, dit  
- **[Robot Learning to Communicate through Projected Visual Abstractions](https://arxiv.org/abs/2607.22434v1)**  
  Authors: Danyang Yan, Boyuan Wang, Jiaxun Liu, Boyuan Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.22434v1.pdf)  
  Keywords: simulation, physical, gesture  
- **[Learning Explicit Physical Parameter Control and Benchmarking for Video Generation](https://arxiv.org/abs/2607.18924v1)**  
  Authors: Yanxun Li, Hao Wen, Bingze Song, Jiashu Zhu, Aiming Hao, Chubin Chen, Jintao Chen, Jiahong Wu, Xiangxiang Chu, Miao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.18924v1.pdf)  
  Keywords: video generation, controllable, diffusion model, simulation, body motion, physical, image-to-video, video diffusion, dynamics, benchmark, physics, dit  
- **[DeforM: Reasoning-Guided Physics-Aware Video Generation via Spatial-Temporal Masking](https://arxiv.org/abs/2607.18664v1)**  
  Authors: Yunyi Li, Yu Qiao, Yaohui Wang, Xinyuan Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.18664v1.pdf)  
  Keywords: video generation, body motion, physical, image-to-video, dynamics, physics-aware, physics  
- **[Wan-Dancer: A Hierarchical Framework for Minute-scale Coherent Music-to-Dance Generation](https://arxiv.org/abs/2607.09581v3)**  
  Authors: Mingyang Huang, Peng Zhang, Li Hu, Guangyuan Wang, Ruoshi Zhang, Yi Lu, Gang Cheng, Bang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.09581v3.pdf)  
  Keywords: dance generation, diffusion model, long-form, identity, video synthesis, dit  
- **[Behavior Foundations for Quadruped Robots: ABot-C0 Technical Report](https://arxiv.org/abs/2607.07370v2)**  
  Authors: Xufeng Zhao, Fuzhi Yang, Jianhui Chen, Li Gao, Zhang Meng, Jie Gao, Yao Zheng, Congyang Zhao, Tianxiong Lv, Menglin Yang, Minqi Gu, Yaru Zhao, Wenyu Liu, Honglin Han, Shihui Su, Zixiao Tang, Liu Liu, Mu Xu, Yang Cai, Wenbin Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.07370v2.pdf)  
  Keywords: dit, physical, efficient, human motion, motion control, style  
- **[ProxyPose: 6-DoF Pose Tracking via Video-to-Video Translation](https://arxiv.org/abs/2607.06555v1)**  
  Authors: Ruihang Zhang, Felix Taubner, Pooja Ravi, Kiriakos N. Kutulakos, David B. Lindell  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.06555v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ruihangzhang97.github.io/proxypose)  
  Keywords: trajectory, diffusion model, video-to-video, body motion, video diffusion, video translation, identity, dit  

### Image-to-Video Generation

*Showing the latest 50 out of 55 papers*

- **[SPADE: An Input-Adaptive Sparse Attention Engine for Fast Video Diffusion Models Inference](https://arxiv.org/abs/2608.03335v1)**  
  Authors: Shanghao Liu, Renze Chen, Size Zheng, Yuanqiang Liu, Yun, Liang, Hailong Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.03335v1.pdf) | [![GitHub](https://img.shields.io/github/stars/6somehow/DAC-SPADE?style=social)](https://github.com/6somehow/DAC-SPADE)  
  Keywords: diffusion transformer, video generation, text-to-video, diffusion model, video diffusion, image-to-video, dit  
- **[FakeI2V-Bench: Benchmarking the Applicability of Image-level Deepfake Detectors for Deepfake Video Detection](https://arxiv.org/abs/2608.03096v1)**  
  Authors: Pei Li, Sihan Chen, Delong Ran, Tianshuo Cong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.03096v1.pdf) | [![GitHub](https://img.shields.io/github/stars/CryptoAILab/FakeI2V-Bench?style=social)](https://github.com/CryptoAILab/FakeI2V-Bench)  
  Keywords: benchmark, evaluation, video generation, i2v  
- **[Token Radius Attention for Efficient Video Generation](https://arxiv.org/abs/2608.02504v1)**  
  Authors: Jiayu Chen, Zhikun Jiang, Maoliang Li, Jiayi Luo, Jiawei Yang, Zihao Zheng, Hengyi Zhang, Guojie Luo, Xiang Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.02504v1.pdf) | [![GitHub](https://img.shields.io/github/stars/IF-LAB-PKU/Token-Radius-Attention?style=social)](https://github.com/IF-LAB-PKU/Token-Radius-Attention)  
  Keywords: t2v, diffusion transformer, video generation, video diffusion, efficient, dit, i2v  
- **[UniMoCa: Unifying Motion and Camera Controls as Visual Proxies for Faithful Human Video Generation](https://arxiv.org/abs/2608.01944v1)**  
  Authors: Liming Tan, Ye Chen, Hao Zhang, Lirong Qian, Feifei Li, Bingbing Ni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01944v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://tanliming-daniel.github.io/UniMoCa)  
  Keywords: trajectory, video generation, body motion, dit, camera control, identity, temporal consistency, human motion, motion control, i2v  
- **[DreamTraj: Generating 6-DoF Object Trajectories by Reading Unrendered Video Diffusion Latents](https://arxiv.org/abs/2608.00486v1)**  
  Authors: Tongsheng Ding, Zhen Luo, Yixuan Yang, Boyu Wang, Luyang Xie, Jinyu Yang, Feng Zheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.00486v1.pdf)  
  Keywords: trajectory, diffusion model, denoising, image-to-video, video diffusion  
- **[Video Models as Native 4D Renderers: World-Grounded Conditioning from Animated Mesh](https://arxiv.org/abs/2608.00094v2)**  
  Authors: Junhao Chen, Mingjin Chen, Henghaofan Zhang, Minglin Chen, Liaoyuan Fan, Boran Zhang, Saining Zhang, Mingze Sun, Hao Zhao, Ruqi Huang, Zhihao Li, Yufei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.00094v2.pdf)  
  Keywords: trajectory, diffusion model, image-to-video, camera control, video diffusion, benchmark, dit  
- **[Visko Orbis 1.0: A Live Model for Real-Time Interactive Long Video Generation](https://arxiv.org/abs/2607.26694v1)**  
  Authors: Xiangbo Gao, Siyuan Yang, Ping He, Mingyang Wu, Yuheng Wu, Yushen Zuo, Jiongze Yu, Ryan Cui, Hongyuan Hua, Devin Ma, Xiao Jin, Yubo Yuan, Qing Yin, Jie Yang, Zhengzhong Tu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.26694v1.pdf)  
  Keywords: video generation, text-to-video, long-form, image-to-video, long video, interactive, streaming, style  
- **[Wonder: Video World Model Done Better](https://arxiv.org/abs/2607.26037v1)**  
  Authors: Jiacong Xu, Hanwen Jiang, Zhixin Shu, Kalyan Sunkavalli, Vishal M. Patel, Yiqun Mei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.26037v1.pdf)  
  Keywords: distillation, video generation, controllable, world model, image-to-video, efficient, interactive, dynamics, dit, style  
- **[I2VShield: An Efficient Proactive Defense Framework against DiT-based Image-to-Video Models](https://arxiv.org/abs/2607.25522v2)**  
  Authors: Yimao Guo, Zuomin Qu, Wei Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.25522v2.pdf)  
  Keywords: diffusion transformer, video generation, image-to-video, efficient, dit, i2v  
- **[Physics-Grounded Fluid Video Generation with a Simulation Dataset and Dual-Stream Optical-Flow Supervision](https://arxiv.org/abs/2607.25321v1)**  
  Authors: Ruijie Su, Yuanzhi Liang, Xiaohua Xie, Jianhuang Lai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.25321v1.pdf)  
  Keywords: video generation, diffusion model, evaluation, simulation, physical, video diffusion, image-to-video, architecture, dynamics, benchmark, physics  

### Long Video Generation

*Showing the latest 50 out of 127 papers*

- **[Qwen-3D: A Generalist 3D Vision-Language Model for Spatial Understanding](https://arxiv.org/abs/2608.02980v1)**  
  Authors: Lucy Lin, Ayush Jain, Yifan Liu, Katerina Fragkiadaki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.02980v1.pdf)  
  Keywords: efficient, long video, benchmark  
- **[Estimating SSIM from MSE for DCT-Based Compressed Images](https://arxiv.org/abs/2608.02549v1)**  
  Authors: Luc Trudeau, Maria G. Martini  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.02549v1.pdf)  
  Keywords: efficient, streaming  
- **[UniMoCa: Unifying Motion and Camera Controls as Visual Proxies for Faithful Human Video Generation](https://arxiv.org/abs/2608.01944v1)**  
  Authors: Liming Tan, Ye Chen, Hao Zhang, Lirong Qian, Feifei Li, Bingbing Ni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01944v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://tanliming-daniel.github.io/UniMoCa)  
  Keywords: trajectory, video generation, body motion, dit, camera control, identity, temporal consistency, human motion, motion control, i2v  
- **[MiniWorld: Democratizing the Training of Video World Models from Scratch](https://arxiv.org/abs/2608.01127v2)**  
  Authors: Yian Zhao, Ruochong Zheng, Hongcan Guo, Yu Yan, Jian Zhang, Jie Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01127v2.pdf)  
  Keywords: diffusion transformer, autoregressive, flow matching, distillation, video generation, simulation, denoising, world model, video diffusion, efficient, interactive, dynamics, streaming, dit  
- **[BWM: A Low-Cost High-Fidelity World Simulator for Robot Learning](https://arxiv.org/abs/2607.29302v1)**  
  Authors: BWM Team  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.29302v1.pdf)  
  Keywords: trajectory, autoregressive, action-conditioned, evaluation, world model, physical, world simulator, benchmark, physics, dit  
- **[ReToken: One Token to Improve Vision-Language Models for Visual Retrieval](https://arxiv.org/abs/2607.28627v1)**  
  Authors: Yao Xiao, Reuben Tan, Zhen Zhu, Yuqun Wu, Jianfeng Gao, Derek Hoiem  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.28627v1.pdf) | [![GitHub](https://img.shields.io/github/stars/avaxiao/ReToken?style=social)](https://github.com/avaxiao/ReToken)  
  Keywords: long video, benchmark  
- **[Chimera: Designing and Chinchilla-Scaling Hybrid Visual Diffusion Transformers](https://arxiv.org/abs/2607.28611v1)**  
  Authors: Chongjian Ge, Hanwen Jiang, Tianyu Wang, Jiuxiang Gu, Yiran Xu, Ziwen Chen, Shaoteng Liu, Jing Shi, Yicong Hong, Zefan Cai, Hailin Jin, Hao Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.28611v1.pdf)  
  Keywords: diffusion transformer, efficient, architecture, long video, style  
- **[EgoGenesis: Egocentric World-Action Modeling with Online Anchored Projective Memory and Action-3D RoPE](https://arxiv.org/abs/2607.28243v1)**  
  Authors: Zexuan Yan, Yuzhou Wu, Yue Ma, Zonghang He, Kaibo Yin, Xiaobing Tu, Yinggui Wang, Jinkui Ren, Xiantao Zhang, Shijian Wang, Jinghong Liu, Linfeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.28243v1.pdf)  
  Keywords: autoregressive, dit, video generation, controllable  
- **[FreqForcing: Autoregressive Long Video Generation via Spectral Self-Anchoring](https://arxiv.org/abs/2607.27110v2)**  
  Authors: Jiatong Li, Leo Liang, Linghe Kong, Yulun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.27110v2.pdf)  
  Keywords: autoregressive, video generation, diffusion model, video diffusion, long video, streaming  
- **[Mitigating Compounding Error via Video Representation Regularization](https://arxiv.org/abs/2607.27036v1)**  
  Authors: Taiye Chen, Qi Zhang, Yisen Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.27036v1.pdf)  
  Keywords: autonomous driving, autoregressive, robotics, video generation, simulation, world model, video diffusion, long video, dynamics  

### Personalization & Customization

*Showing the latest 50 out of 93 papers*

- **[GVCCTurbo: Rate-Compute Quality Scheduling for Codebook Driven Generative Compression](https://arxiv.org/abs/2608.03517v1)**  
  Authors: Ziyue Zeng, Dingjie Peng, Xun Su, Hiroshi Watanabe  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.03517v1.pdf)  
  Keywords: trajectory, evaluation, style, controllable  
- **[RealWeather: Realistic and Scene-Faithful Weather Translation with Driving World Models](https://arxiv.org/abs/2608.02953v1)**  
  Authors: Yuwei Ning, Liangzhi Wang, Yi Xiao, Zhenhua Wu, Yun Pang, Mingkun Chan, Jichang Li, Guanbin Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.02953v1.pdf)  
  Keywords: autonomous driving, world model, dynamics, dit, style  
- **[UniMoCa: Unifying Motion and Camera Controls as Visual Proxies for Faithful Human Video Generation](https://arxiv.org/abs/2608.01944v1)**  
  Authors: Liming Tan, Ye Chen, Hao Zhang, Lirong Qian, Feifei Li, Bingbing Ni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01944v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://tanliming-daniel.github.io/UniMoCa)  
  Keywords: trajectory, video generation, body motion, dit, camera control, identity, temporal consistency, human motion, motion control, i2v  
- **[Chimera: Designing and Chinchilla-Scaling Hybrid Visual Diffusion Transformers](https://arxiv.org/abs/2607.28611v1)**  
  Authors: Chongjian Ge, Hanwen Jiang, Tianyu Wang, Jiuxiang Gu, Yiran Xu, Ziwen Chen, Shaoteng Liu, Jing Shi, Yicong Hong, Zefan Cai, Hailin Jin, Hao Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.28611v1.pdf)  
  Keywords: diffusion transformer, efficient, architecture, long video, style  
- **[Collaborative Feature Aggregation for Face Super-Resolution and Robust Re-Identification](https://arxiv.org/abs/2607.28130v1)**  
  Authors: Juheon Hwang, Taewan Kim, Jiwoo Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.28130v1.pdf)  
  Keywords: identity, super-resolution, dit  
- **[LeapTalk: Breaking the Latency-Quality Trade-off in Talking Head Generation](https://arxiv.org/abs/2608.00079v1)**  
  Authors: Rongxiang Zhang, Songhua Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.00079v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zhangrongxiang.github.io/leaptalk-page)  
  Keywords: autoregressive, distillation, video generation, audio-driven, long-form, long video, efficient, identity, streaming, talking head  
- **[TPD: Temporal Prior Decoupling for Text-to-Video Diffusion Models](https://arxiv.org/abs/2607.26706v1)**  
  Authors: Taewon Kang, Matthias Zwicker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.26706v1.pdf)  
  Keywords: concept, trajectory, text-to-video, diffusion model, video diffusion, dit  
- **[Visko Orbis 1.0: A Live Model for Real-Time Interactive Long Video Generation](https://arxiv.org/abs/2607.26694v1)**  
  Authors: Xiangbo Gao, Siyuan Yang, Ping He, Mingyang Wu, Yuheng Wu, Yushen Zuo, Jiongze Yu, Ryan Cui, Hongyuan Hua, Devin Ma, Xiao Jin, Yubo Yuan, Qing Yin, Jie Yang, Zhengzhong Tu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.26694v1.pdf)  
  Keywords: video generation, text-to-video, long-form, image-to-video, long video, interactive, streaming, style  
- **[CineWeaver: Training-Free Reference-Controllable Multi-Shot Long Video Generation for Cinematic Storytelling](https://arxiv.org/abs/2607.26529v1)**  
  Authors: Yuyang Huang, Yabo Chen, Wenrui Dai, Ziyang Zheng, Haibin Huang, Chi Zhang, Junni Zou, Hongkai Xiong, Xuelong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.26529v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://cineweaver.github.io)  
  Keywords: customization, video generation, controllable, text-to-video, diffusion model, video diffusion, long-form, long video, dit  
- **[Wonder: Video World Model Done Better](https://arxiv.org/abs/2607.26037v1)**  
  Authors: Jiacong Xu, Hanwen Jiang, Zhixin Shu, Kalyan Sunkavalli, Vishal M. Patel, Yiqun Mei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.26037v1.pdf)  
  Keywords: distillation, video generation, controllable, world model, image-to-video, efficient, interactive, dynamics, dit, style  

### Physical Understanding

*Showing the latest 50 out of 153 papers*

- **[CrossScope: A Role-Asymmetric World Model for Joint Dual-Scope Surgical Video Prediction](https://arxiv.org/abs/2608.03211v1)**  
  Authors: Wanhao Liu, Jinsong Lin, Rulin Zhou, Chi Kit Ng, Wenbin Pan, Zhiqing Tang, Dongyue Li, Liwei Luo, Yanshen Wu, Panshuo Li, Zhiyong Xiong, Huxin Gao, Tamas Haidegger, Hongliang Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.03211v1.pdf)  
  Keywords: video generation, evaluation, video prediction, world model, dynamics, benchmark  
- **[SUV: Future Scene Understanding as Video Generation for End-to-End Driving](https://arxiv.org/abs/2608.03084v1)**  
  Authors: Yibo Yuan, Jiacheng Fu, Jiangtong Zhu, Yi Li, Jianhua Han, Meng Tian, Zhuohan Liu, Zhiwei Xiong, Hang Xu, Jianwu Fang, Jianru Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.03084v1.pdf)  
  Keywords: trajectory, benchmark, video generation, dynamics  
- **[RealWeather: Realistic and Scene-Faithful Weather Translation with Driving World Models](https://arxiv.org/abs/2608.02953v1)**  
  Authors: Yuwei Ning, Liangzhi Wang, Yi Xiao, Zhenhua Wu, Yun Pang, Mingkun Chan, Jichang Li, Guanbin Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.02953v1.pdf)  
  Keywords: autonomous driving, world model, dynamics, dit, style  
- **[AcoustiTrace: When Plausible Sound Violates Physics](https://arxiv.org/abs/2608.02035v1)**  
  Authors: Shiyang Li, Yuewen Cao, Yihao Liu, Yuandong Pu, Baochang Zhang, Xiaofei Li, Changqing Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.02035v1.pdf)  
  Keywords: video generation, evaluation, physical, sound, benchmark, physics  
- **[CultureVidBench: Benchmarking Cultural Understanding in Text-to-Video Generation](https://arxiv.org/abs/2608.01942v1)**  
  Authors: Xianjing Han, Yuhan Su, Yang Deng, Dong Ma, Wee Peng Tay, Bin Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01942v1.pdf)  
  Keywords: t2v, video generation, text-to-video, physical, benchmark  
- **[MoCRA: Mixture of Compositional Rank-1 Atoms for 4K All-in-One Video Restoration](https://arxiv.org/abs/2608.01829v1)**  
  Authors: Yongcong Wang, Pu Wang, Hingchin Chen, Runci Bai, Yucheng Xin, Chen Wu, Chengchao Shen, Guangwei Gao, Siyuan Yao, Pengwen Dai, Zhuoran Zheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01829v1.pdf)  
  Keywords: video restoration, benchmark, dit, physical  
- **[MiniWorld: Democratizing the Training of Video World Models from Scratch](https://arxiv.org/abs/2608.01127v2)**  
  Authors: Yian Zhao, Ruochong Zheng, Hongcan Guo, Yu Yan, Jian Zhang, Jie Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01127v2.pdf)  
  Keywords: diffusion transformer, autoregressive, flow matching, distillation, video generation, simulation, denoising, world model, video diffusion, efficient, interactive, dynamics, streaming, dit  
- **[Diagnosing Under-Development of Irreversible Processes in Video Generation](https://arxiv.org/abs/2608.00617v1)**  
  Authors: Jian Xu, Yanning Wu, Delu Zeng, John Paisley, Qibin Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.00617v1.pdf)  
  Keywords: text-to-video, physical, video generation  
- **[BWM: A Low-Cost High-Fidelity World Simulator for Robot Learning](https://arxiv.org/abs/2607.29302v1)**  
  Authors: BWM Team  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.29302v1.pdf)  
  Keywords: trajectory, autoregressive, action-conditioned, evaluation, world model, physical, world simulator, benchmark, physics, dit  
- **[Mirror Learning](https://arxiv.org/abs/2607.28737v1)**  
  Authors: Yunpeng Liu, Matthew Niedoba, Oluwanifemi A. Adekanye, Jason Yoo, Yingchen He, Berend Zwartsenberg, Frank Wood  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.28737v1.pdf)  
  Keywords: diffusion model, world model, dynamics, video diffusion  

### Surveys & Benchmarks

*Showing the latest 50 out of 226 papers*

- **[GVCCTurbo: Rate-Compute Quality Scheduling for Codebook Driven Generative Compression](https://arxiv.org/abs/2608.03517v1)**  
  Authors: Ziyue Zeng, Dingjie Peng, Xun Su, Hiroshi Watanabe  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.03517v1.pdf)  
  Keywords: trajectory, evaluation, style, controllable  
- **[CrossScope: A Role-Asymmetric World Model for Joint Dual-Scope Surgical Video Prediction](https://arxiv.org/abs/2608.03211v1)**  
  Authors: Wanhao Liu, Jinsong Lin, Rulin Zhou, Chi Kit Ng, Wenbin Pan, Zhiqing Tang, Dongyue Li, Liwei Luo, Yanshen Wu, Panshuo Li, Zhiyong Xiong, Huxin Gao, Tamas Haidegger, Hongliang Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.03211v1.pdf)  
  Keywords: video generation, evaluation, video prediction, world model, dynamics, benchmark  
- **[Adaptive Two-Stage Visual Token Pruning for Efficient Inference in Video-Language Models](https://arxiv.org/abs/2608.03112v1)**  
  Authors: Paribesh Regmi, Qingshuang Chen, Chi Zhang, Heba Aly, Yelin Kim, Hongda Mao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.03112v1.pdf)  
  Keywords: efficient, benchmark, dit  
- **[FakeI2V-Bench: Benchmarking the Applicability of Image-level Deepfake Detectors for Deepfake Video Detection](https://arxiv.org/abs/2608.03096v1)**  
  Authors: Pei Li, Sihan Chen, Delong Ran, Tianshuo Cong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.03096v1.pdf) | [![GitHub](https://img.shields.io/github/stars/CryptoAILab/FakeI2V-Bench?style=social)](https://github.com/CryptoAILab/FakeI2V-Bench)  
  Keywords: benchmark, evaluation, video generation, i2v  
- **[SUV: Future Scene Understanding as Video Generation for End-to-End Driving](https://arxiv.org/abs/2608.03084v1)**  
  Authors: Yibo Yuan, Jiacheng Fu, Jiangtong Zhu, Yi Li, Jianhua Han, Meng Tian, Zhuohan Liu, Zhiwei Xiong, Hang Xu, Jianwu Fang, Jianru Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.03084v1.pdf)  
  Keywords: trajectory, benchmark, video generation, dynamics  
- **[Qwen-3D: A Generalist 3D Vision-Language Model for Spatial Understanding](https://arxiv.org/abs/2608.02980v1)**  
  Authors: Lucy Lin, Ayush Jain, Yifan Liu, Katerina Fragkiadaki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.02980v1.pdf)  
  Keywords: efficient, long video, benchmark  
- **[WorldExam: Benchmarking World Models from Apparent Appearance to Inherent Reactivity](https://arxiv.org/abs/2608.02603v1)**  
  Authors: Yuxue Yang, Shuyao Shang, Jiahe Wang, Zitong Zhou, Liang Tan, Junhan Zeng, Ruizhi Li, Junyan Li, Yu Liu, Xiao Yang, Yong Li, Jun Zhu, Hongsheng Li, Tieniu Tan, Lue Fan, Zhaoxiang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.02603v1.pdf)  
  Keywords: video generation, controllable, evaluation, world model, camera control, benchmark, dit  
- **[EchoCache: Energy-Guided Cross-Modal Caching for Efficient Audio-Driven Video Generation](https://arxiv.org/abs/2608.02474v1)**  
  Authors: Jiayu Chen, Xiaoyu Wu, Rongshan Gao, Maoliang Li, Zihao Zheng, Xinhao Sun, Hailong Zou, Guojie Luo, Xiang Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.02474v1.pdf) | [![GitHub](https://img.shields.io/github/stars/IF-LAB-PKU/EchoCache?style=social)](https://github.com/IF-LAB-PKU/EchoCache)  
  Keywords: video generation, audio-driven, diffusion model, denoising, efficient, benchmark  
- **[AcoustiTrace: When Plausible Sound Violates Physics](https://arxiv.org/abs/2608.02035v1)**  
  Authors: Shiyang Li, Yuewen Cao, Yihao Liu, Yuandong Pu, Baochang Zhang, Xiaofei Li, Changqing Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.02035v1.pdf)  
  Keywords: video generation, evaluation, physical, sound, benchmark, physics  
- **[CultureVidBench: Benchmarking Cultural Understanding in Text-to-Video Generation](https://arxiv.org/abs/2608.01942v1)**  
  Authors: Xianjing Han, Yuhan Su, Yang Deng, Dong Ma, Wee Peng Tay, Bin Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01942v1.pdf)  
  Keywords: t2v, video generation, text-to-video, physical, benchmark  

### Text-to-Video Generation

*Showing the latest 50 out of 78 papers*

- **[SPADE: An Input-Adaptive Sparse Attention Engine for Fast Video Diffusion Models Inference](https://arxiv.org/abs/2608.03335v1)**  
  Authors: Shanghao Liu, Renze Chen, Size Zheng, Yuanqiang Liu, Yun, Liang, Hailong Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.03335v1.pdf) | [![GitHub](https://img.shields.io/github/stars/6somehow/DAC-SPADE?style=social)](https://github.com/6somehow/DAC-SPADE)  
  Keywords: diffusion transformer, video generation, text-to-video, diffusion model, video diffusion, image-to-video, dit  
- **[CAPE-T2V: Captioner-Anchored Prompt Enhancement toward Two-Sided Conditioning Alignment in Text-to-Video Generation](https://arxiv.org/abs/2608.03046v1)**  
  Authors: Yizhuo Jia, Jingyun Hua, Yuanxing Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.03046v1.pdf) | [![GitHub](https://img.shields.io/github/stars/yizzz927/CAPE-T2V?style=social)](https://github.com/yizzz927/CAPE-T2V)  
  Keywords: t2v, diffusion transformer, video generation, text-to-video, dit  
- **[Token Radius Attention for Efficient Video Generation](https://arxiv.org/abs/2608.02504v1)**  
  Authors: Jiayu Chen, Zhikun Jiang, Maoliang Li, Jiayi Luo, Jiawei Yang, Zihao Zheng, Hengyi Zhang, Guojie Luo, Xiang Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.02504v1.pdf) | [![GitHub](https://img.shields.io/github/stars/IF-LAB-PKU/Token-Radius-Attention?style=social)](https://github.com/IF-LAB-PKU/Token-Radius-Attention)  
  Keywords: t2v, diffusion transformer, video generation, video diffusion, efficient, dit, i2v  
- **[CultureVidBench: Benchmarking Cultural Understanding in Text-to-Video Generation](https://arxiv.org/abs/2608.01942v1)**  
  Authors: Xianjing Han, Yuhan Su, Yang Deng, Dong Ma, Wee Peng Tay, Bin Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01942v1.pdf)  
  Keywords: t2v, video generation, text-to-video, physical, benchmark  
- **[Diagnosing Under-Development of Irreversible Processes in Video Generation](https://arxiv.org/abs/2608.00617v1)**  
  Authors: Jian Xu, Yanning Wu, Delu Zeng, John Paisley, Qibin Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.00617v1.pdf)  
  Keywords: text-to-video, physical, video generation  
- **[Temporal Concentration from Rollout Errors: Implicit Preference Optimization for Text-to-Video Diffusion](https://arxiv.org/abs/2607.28058v1)**  
  Authors: Henglin Liu, Fangyuan Kong, Jing Wang, Yizhou Lin, Nisha Huang, Chang Liu, Xintao Wang, Pengfei Wan, Kun Gai, Xiu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.28058v1.pdf)  
  Keywords: video generation, text-to-video, diffusion model, denoising, video diffusion, dynamics, dit  
- **[VideoCoCo: Code-as-CoT for Physically-Consistent Video Generation via an Agentic Dual-Engine System](https://arxiv.org/abs/2607.27380v1)**  
  Authors: Haodong Li, Tianfei Ren, Xiaoxiao Ma, Chunmei Qing, Zhen Fang, Sipeng He, Ziyu Guo, Haoyu Wu, Juanxi Tian, Yihang Zou, Ruichuan An, Dongzhi Jiang, Boxue Yang, Ji Xie, Xu Huang, Wenhao Yan, Jialv Zou, Zhengrong Yue, Yaxin Luo, Xiaotong Li, Yuzhu Wang, Junyan Ye, Jinjing Zhao, Zehui Chen, Lin Chen, Renye Yan, Feng Zhao, Pheng-Ann Heng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.27380v1.pdf)  
  Keywords: video generation, controllable, text-to-video, simulation, physical, dynamics, benchmark, dit  
- **[TPD: Temporal Prior Decoupling for Text-to-Video Diffusion Models](https://arxiv.org/abs/2607.26706v1)**  
  Authors: Taewon Kang, Matthias Zwicker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.26706v1.pdf)  
  Keywords: concept, trajectory, text-to-video, diffusion model, video diffusion, dit  
- **[Visko Orbis 1.0: A Live Model for Real-Time Interactive Long Video Generation](https://arxiv.org/abs/2607.26694v1)**  
  Authors: Xiangbo Gao, Siyuan Yang, Ping He, Mingyang Wu, Yuheng Wu, Yushen Zuo, Jiongze Yu, Ryan Cui, Hongyuan Hua, Devin Ma, Xiao Jin, Yubo Yuan, Qing Yin, Jie Yang, Zhengzhong Tu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.26694v1.pdf)  
  Keywords: video generation, text-to-video, long-form, image-to-video, long video, interactive, streaming, style  
- **[CineWeaver: Training-Free Reference-Controllable Multi-Shot Long Video Generation for Cinematic Storytelling](https://arxiv.org/abs/2607.26529v1)**  
  Authors: Yuyang Huang, Yabo Chen, Wenrui Dai, Ziyang Zheng, Haibin Huang, Chi Zhang, Junni Zou, Hongkai Xiong, Xuelong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.26529v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://cineweaver.github.io)  
  Keywords: customization, video generation, controllable, text-to-video, diffusion model, video diffusion, long-form, long video, dit  

### Video Editing

- **[EgoPlay: Event-Triggered Video Editing for Egocentric Streams](https://arxiv.org/abs/2607.24560v1)**  
  Authors: Jinjie Mai, Gordon Guocheng Qian, Willi Menapace, Arpit Sahni, Chaoyang Wang, Ashkan Mirzaei, Runjia Li, Sergey Tulyakov, Bernard Ghanem, Peter Wonka, Rameen Abdal  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.24560v1.pdf)  
  Keywords: diffusion transformer, evaluation, video-to-video, video diffusion, video editing, benchmark, dit  
- **[ID-V2V: Identity-Preserving Video Restylization](https://arxiv.org/abs/2607.22830v1)**  
  Authors: Yuancheng Xu, Mingming He, Pablo Salamanca, Li Ma, Yash Kant, Emmett Steven, Paul Debevec, Ning Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.22830v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Eyeline-Labs/ID-V2V?style=social)](https://github.com/Eyeline-Labs/ID-V2V)  
  Keywords: creative, video-to-video, identity, video synthesis, dit, style  
- **[OSVE: One Step Video Editing with One Step Diffusion Models](https://arxiv.org/abs/2607.19895v1)**  
  Authors: Habin Lim, Gyeong-Moon Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.19895v1.pdf) | [![GitHub](https://img.shields.io/github/stars/KU-VGI/OSVE?style=social)](https://github.com/KU-VGI/OSVE)  
  Keywords: diffusion model, long video, temporal consistency, video editing, dit  
- **[AniGS: Bridging Rendering and Diffusion Prior for 3D Scene Animation](https://arxiv.org/abs/2607.18539v1)**  
  Authors: Yen-Chi Cheng, Chen Gao, Chuhan Chen, Tuotuo Li, Rajvi Shah, Ayush Saraf, Changil Kim, Liangyan Gui, Alexander Schwing, Johannes Kopf, Hung-Yu Tseng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.18539v1.pdf)  
  Keywords: diffusion model, video-to-video, novel view, video diffusion, dynamics, dit  
- **[PE-Field 4D: Video Generation Models as Canvas](https://arxiv.org/abs/2607.15667v1)**  
  Authors: Yunpeng Bai, Haoxiang Li, Qixing Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.15667v1.pdf) | [![GitHub](https://img.shields.io/github/stars/MTLab/PE-Field?style=social)](https://github.com/MTLab/PE-Field)  
  Keywords: diffusion transformer, trajectory, video generation, controllable, diffusion model, denoising, video diffusion, video editing, video synthesis, dit  
- **[From Draft to Draft-Free: One-Step Video Object Removal via Privileged Distillation and Fast Planting](https://arxiv.org/abs/2607.14976v1)**  
  Authors: Zizhao Chen, Ping Wei, Guang Dai, Jingdong Wang, Mengmeng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.14976v1.pdf)  
  Keywords: distillation, video generation, denoising, video editing, dit  
- **[ReBind: Multi-Reference Video Editing via Structured Instructions with Explicit Reference Relationships](https://arxiv.org/abs/2607.14681v1)**  
  Authors: Xinyu Liu, Shihao Li, Weihong Lin, Xinlong Chen, Yang Shi, Yujin Han, Yiyang Cai, Yanghao Wang, Ruibin Yuan, Yuanxing Zhang, Pengfei Wan, Wenhan Luo, Yike Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.14681v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rebind-mrv2v.github.io)  
  Keywords: text-to-video, dit, video generation, video editing  
- **[LightCrafter: PBR-Conditioned Video Diffusion Refinement for Controllable and Consistent Relighting](https://arxiv.org/abs/2607.08016v2)**  
  Authors: Zixin Guo, Yehonathan Litman, Yifeng He, John Miller, Chuhan Chen, Deva Ramanan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.08016v2.pdf)  
  Keywords: concept, video generation, controllable, diffusion model, video-to-video, physical, video diffusion, long-form, video translation, temporal consistency, benchmark, dit  
- **[ProxyPose: 6-DoF Pose Tracking via Video-to-Video Translation](https://arxiv.org/abs/2607.06555v1)**  
  Authors: Ruihang Zhang, Felix Taubner, Pooja Ravi, Kiriakos N. Kutulakos, David B. Lindell  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.06555v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ruihangzhang97.github.io/proxypose)  
  Keywords: trajectory, diffusion model, video-to-video, body motion, video diffusion, video translation, identity, dit  
- **[Consistent and Editable: A Balanced Framework for Text-Guided Video Editing](https://arxiv.org/abs/2607.05056v1)**  
  Authors: Tao Jin, Li Xiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.05056v1.pdf)  
  Keywords: diffusion model, temporal consistency, dit, video editing  

### Video Inpainting & Completion

- **[CrossScope: A Role-Asymmetric World Model for Joint Dual-Scope Surgical Video Prediction](https://arxiv.org/abs/2608.03211v1)**  
  Authors: Wanhao Liu, Jinsong Lin, Rulin Zhou, Chi Kit Ng, Wenbin Pan, Zhiqing Tang, Dongyue Li, Liwei Luo, Yanshen Wu, Panshuo Li, Zhiyong Xiong, Huxin Gao, Tamas Haidegger, Hongliang Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.03211v1.pdf)  
  Keywords: video generation, evaluation, video prediction, world model, dynamics, benchmark  
- **[Schrödinger's Cat: Probabilistic Representation and Prediction of Potential Scene Kinematics](https://arxiv.org/abs/2607.25984v1)**  
  Authors: Timy Phan, Jannik Wiese, Björn Ommer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.25984v1.pdf)  
  Keywords: trajectory, video generation, video prediction, efficient, interactive, dit  
- **[The Seriality Gap in Video Diffusion Models](https://arxiv.org/abs/2607.13031v1)**  
  Authors: Jorge Diaz Chao, Konpat Preechakul, Yuxi Liu, Yutong Bai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.13031v1.pdf)  
  Keywords: autoregressive, simulation, diffusion model, denoising, video prediction, video diffusion, dynamics  
- **[Video Generation Models Are Inherent Lighting Estimators](https://arxiv.org/abs/2607.04674v1)**  
  Authors: Ziqi Cai, Shuchen Weng, Kaiqi Liu, Zifeng Wang, Zhiquan Zhang, Minggui Teng, Han Jiang, Boxin Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.04674v1.pdf)  
  Keywords: video generation, diffusion model, physical, video diffusion, efficient, video inpainting  
- **[ImageWAM: Do World Action Models Really Need Video Generation, or Just Image Editing?](https://arxiv.org/abs/2606.19531v1)**  
  Authors: Yuyang Zhang, Wenyao Zhang, Zekun Qi, He Zhang, Haitao Lin, Jingbo Zhang, Yao Mu, Xiaokang Yang, Wenjun Zeng, Xin Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.19531v1.pdf)  
  Keywords: video generation, denoising, video prediction, world model, dit  
- **[R2RDreamer: 3D-aware Data Augmentation for Spatially-generalized 2D Manipulation Policies](https://arxiv.org/abs/2606.17040v1)**  
  Authors: Xiuwei Xu, Haowen Sun, Angyuan Ma, Yiwei Zhang, Zhenyu Wu, Xiaofeng Wang, Bingyao Yu, Zheng Zhu, Jie Zhou, Jiwen Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.17040v1.pdf)  
  Keywords: controllable, 3d-aware, simulation, image-to-video, video completion, dit, style  
- **[PointAction: 3D Points as Universal Action Representations for Robot Control](https://arxiv.org/abs/2606.03943v1)**  
  Authors: Mutian Tong, Han Jiang, Qiao Feng, Lingjie Liu, Jiatao Gu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.03943v1.pdf)  
  Keywords: 4d generation, video generation, simulation, diffusion model, video prediction, video diffusion, dynamics  
- **[World Models: A Comprehensive Survey of Architectures, Methodologies, Reasoning Paradigms, and Applications](https://arxiv.org/abs/2606.00133v1)**  
  Authors: Arif Hassan Zidan, Yi Pan, Hanqi Jiang, Ruiyu Yan, Wei Ruan, Zihao Wu, Lifeng Chen, Weihang You, Xinliang Li, Bowen Chen, Huawen Hu, Peilong Wang, Sizhuang Liu, Jing Zhang, Siyuan Li, Zhengliang Liu, Yu Bao, Lin Zhao, Lichao Sun, Dajiang Zhu, Xiang Li, Jinglei Lv, Quanzheng Li, Wei Liu, Tianming Liu, Wei Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.00133v1.pdf)  
  Keywords: autonomous driving, robotics, video generation, evaluation, video prediction, survey, world model, architecture, education, interactive, dynamics, medical, benchmark, physics  

### Video Super-Resolution & Enhancement

*Showing the latest 50 out of 71 papers*

- **[EchoCache: Energy-Guided Cross-Modal Caching for Efficient Audio-Driven Video Generation](https://arxiv.org/abs/2608.02474v1)**  
  Authors: Jiayu Chen, Xiaoyu Wu, Rongshan Gao, Maoliang Li, Zihao Zheng, Xinhao Sun, Hailong Zou, Guojie Luo, Xiang Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.02474v1.pdf) | [![GitHub](https://img.shields.io/github/stars/IF-LAB-PKU/EchoCache?style=social)](https://github.com/IF-LAB-PKU/EchoCache)  
  Keywords: video generation, audio-driven, diffusion model, denoising, efficient, benchmark  
- **[MoCRA: Mixture of Compositional Rank-1 Atoms for 4K All-in-One Video Restoration](https://arxiv.org/abs/2608.01829v1)**  
  Authors: Yongcong Wang, Pu Wang, Hingchin Chen, Runci Bai, Yucheng Xin, Chen Wu, Chengchao Shen, Guangwei Gao, Siyuan Yao, Pengwen Dai, Zhuoran Zheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01829v1.pdf)  
  Keywords: video restoration, benchmark, dit, physical  
- **[MiniWorld: Democratizing the Training of Video World Models from Scratch](https://arxiv.org/abs/2608.01127v2)**  
  Authors: Yian Zhao, Ruochong Zheng, Hongcan Guo, Yu Yan, Jian Zhang, Jie Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01127v2.pdf)  
  Keywords: diffusion transformer, autoregressive, flow matching, distillation, video generation, simulation, denoising, world model, video diffusion, efficient, interactive, dynamics, streaming, dit  
- **[DreamTraj: Generating 6-DoF Object Trajectories by Reading Unrendered Video Diffusion Latents](https://arxiv.org/abs/2608.00486v1)**  
  Authors: Tongsheng Ding, Zhen Luo, Yixuan Yang, Boyu Wang, Luyang Xie, Jinyu Yang, Feng Zheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.00486v1.pdf)  
  Keywords: trajectory, diffusion model, denoising, image-to-video, video diffusion  
- **[Collaborative Feature Aggregation for Face Super-Resolution and Robust Re-Identification](https://arxiv.org/abs/2607.28130v1)**  
  Authors: Juheon Hwang, Taewan Kim, Jiwoo Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.28130v1.pdf)  
  Keywords: identity, super-resolution, dit  
- **[Temporal Concentration from Rollout Errors: Implicit Preference Optimization for Text-to-Video Diffusion](https://arxiv.org/abs/2607.28058v1)**  
  Authors: Henglin Liu, Fangyuan Kong, Jing Wang, Yizhou Lin, Nisha Huang, Chang Liu, Xintao Wang, Pengfei Wan, Kun Gai, Xiu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.28058v1.pdf)  
  Keywords: video generation, text-to-video, diffusion model, denoising, video diffusion, dynamics, dit  
- **[FeatFix: Reuse What You Verify through Local Exact-Feature Correction for Faster Cached Diffusion Inference](https://arxiv.org/abs/2607.27842v1)**  
  Authors: Hanshuai Cui, Zhiqing Tang, Zhi Yao, Qianli Ma, Fanshuai Meng, Weijia Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.27842v1.pdf)  
  Keywords: diffusion model, denoising  
- **[Genie Sim PanoWorld: An Infinite Indoor 3D World Generation Pipeline via Panoramic Scene Modeling and Simulation](https://arxiv.org/abs/2607.26646v1)**  
  Authors: Yongxin Su, Linjie Hou, Feng Wang, Jialin Tang, Zhijun Li, Qian Wang, Maoqing Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.26646v1.pdf)  
  Keywords: trajectory, video generation, controllable, diffusion model, simulation, denoising, video diffusion, latent video, dit  
- **[Parallel Decoding Distillation for Fast Image and Video Generation](https://arxiv.org/abs/2607.26004v1)**  
  Authors: Neta Shaul, Chao Liu, Arash Vahdat, Julius Berner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.26004v1.pdf)  
  Keywords: concept, trajectory, flow matching, distillation, video generation, text-to-video, evaluation, diffusion model, denoising, video diffusion, architecture, acceleration, fast inference  
- **[TaoMate: Anchor-Guided Memory Bridging Evolving and Reference States for Real-Time Audio-Video Digital Human Generation](https://arxiv.org/abs/2607.24359v1)**  
  Authors: Qijun Gan, Chenwei Zhang, Meiguang Jin, Junfeng Ma, Qiu Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.24359v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://taoliveaigc.github.io/TaoMate)  
  Keywords: autoregressive, distillation, video generation, denoising, long-form, dit  

### World Models & Simulation

*Showing the latest 50 out of 128 papers*

- **[CrossScope: A Role-Asymmetric World Model for Joint Dual-Scope Surgical Video Prediction](https://arxiv.org/abs/2608.03211v1)**  
  Authors: Wanhao Liu, Jinsong Lin, Rulin Zhou, Chi Kit Ng, Wenbin Pan, Zhiqing Tang, Dongyue Li, Liwei Luo, Yanshen Wu, Panshuo Li, Zhiyong Xiong, Huxin Gao, Tamas Haidegger, Hongliang Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.03211v1.pdf)  
  Keywords: video generation, evaluation, video prediction, world model, dynamics, benchmark  
- **[RealWeather: Realistic and Scene-Faithful Weather Translation with Driving World Models](https://arxiv.org/abs/2608.02953v1)**  
  Authors: Yuwei Ning, Liangzhi Wang, Yi Xiao, Zhenhua Wu, Yun Pang, Mingkun Chan, Jichang Li, Guanbin Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.02953v1.pdf)  
  Keywords: autonomous driving, world model, dynamics, dit, style  
- **[WorldExam: Benchmarking World Models from Apparent Appearance to Inherent Reactivity](https://arxiv.org/abs/2608.02603v1)**  
  Authors: Yuxue Yang, Shuyao Shang, Jiahe Wang, Zitong Zhou, Liang Tan, Junhan Zeng, Ruizhi Li, Junyan Li, Yu Liu, Xiao Yang, Yong Li, Jun Zhu, Hongsheng Li, Tieniu Tan, Lue Fan, Zhaoxiang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.02603v1.pdf)  
  Keywords: video generation, controllable, evaluation, world model, camera control, benchmark, dit  
- **[InteracVid: Building a Real Interactive Audio-Visual Response Dataset from Live-Chat Videos](https://arxiv.org/abs/2608.01157v1)**  
  Authors: Chi Zhang, Haoyang Shi, Yueyi Liu, Zhaokun Yan, Yishu Yin, Yuhang Wu, Miao Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01157v1.pdf)  
  Keywords: benchmark, evaluation, interactive, avatar  
- **[MiniWorld: Democratizing the Training of Video World Models from Scratch](https://arxiv.org/abs/2608.01127v2)**  
  Authors: Yian Zhao, Ruochong Zheng, Hongcan Guo, Yu Yan, Jian Zhang, Jie Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01127v2.pdf)  
  Keywords: diffusion transformer, autoregressive, flow matching, distillation, video generation, simulation, denoising, world model, video diffusion, efficient, interactive, dynamics, streaming, dit  
- **[BWM: A Low-Cost High-Fidelity World Simulator for Robot Learning](https://arxiv.org/abs/2607.29302v1)**  
  Authors: BWM Team  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.29302v1.pdf)  
  Keywords: trajectory, autoregressive, action-conditioned, evaluation, world model, physical, world simulator, benchmark, physics, dit  
- **[Mirror Learning](https://arxiv.org/abs/2607.28737v1)**  
  Authors: Yunpeng Liu, Matthew Niedoba, Oluwanifemi A. Adekanye, Jason Yoo, Yingchen He, Berend Zwartsenberg, Frank Wood  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.28737v1.pdf)  
  Keywords: diffusion model, world model, dynamics, video diffusion  
- **[ODEWorld: A Continuous Predictive Architecture via Physical-Time Flow](https://arxiv.org/abs/2607.27924v1)**  
  Authors: Dongxiu Liu, Haoyi Niu, Peng Cheng, Yuan Gao, Xirui Kang, Sangli Teng, Koushil Sreenath, Xianyuan Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.27924v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://dstate.github.io/odeworld_website)  
  Keywords: video generation, world model, physical, efficient, architecture, dynamics  
- **[Articulated Object Reconstruction from Rest-State Observation](https://arxiv.org/abs/2607.27749v1)**  
  Authors: Daeun Lee, Jaeah Lee, Woosung Kim, Haebeom Jung, Jaesik Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.27749v1.pdf)  
  Keywords: diffusion model, physical, interactive, video diffusion  
- **[VideoCoCo: Code-as-CoT for Physically-Consistent Video Generation via an Agentic Dual-Engine System](https://arxiv.org/abs/2607.27380v1)**  
  Authors: Haodong Li, Tianfei Ren, Xiaoxiao Ma, Chunmei Qing, Zhen Fang, Sipeng He, Ziyu Guo, Haoyu Wu, Juanxi Tian, Yihang Zou, Ruichuan An, Dongzhi Jiang, Boxue Yang, Ji Xie, Xu Huang, Wenhao Yan, Jialv Zou, Zhengrong Yue, Yaxin Luo, Xiaotong Li, Yuzhu Wang, Junyan Ye, Jinjing Zhao, Zehui Chen, Lin Chen, Renye Yan, Feng Zhao, Pheng-Ann Heng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.27380v1.pdf)  
  Keywords: video generation, controllable, text-to-video, simulation, physical, dynamics, benchmark, dit  



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
      "both_abstract_and_title": ["video diffusion", "video generation", "text-to-video"],
      "abstract_only": ["diffusion model video generation"],
      "title_only": ["video generation", "video diffusion"]
    },
    "domains": ["cs.CV", "cs.AI", "cs.MM"],
    "time_range": {
      "mode": "relative",
      "relative": "1y"
    },
    "max_results": 500
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
