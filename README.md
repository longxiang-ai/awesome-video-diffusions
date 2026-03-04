# Awesome Video Diffusions [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Video Diffusion Models and Video Generation. Content is automatically updated daily.

> Last Update: 2026-03-04 02:04:38

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

- [3D-aware Video Generation](#3d-aware-video-generation) (28 papers) - Video generation with 3D awareness, multi-view consistency, and 4D content creation
- [Applications](#applications) (53 papers) - Domain-specific applications of video diffusion models
- [Architecture & Efficiency](#architecture-&-efficiency) (364 papers) - Architectural innovations (DiT, UNet), flow matching, and training/inference efficiency
- [Audio & Multi-modal](#audio-&-multi-modal) (34 papers) - Audio-driven and multi-modal conditioned video generation
- [Controllable Generation](#controllable-generation) (115 papers) - Controllable video generation with motion, camera, pose, or layout guidance
- [Human & Character Animation](#human-&-character-animation) (35 papers) - Human-centric video generation including talking heads, dance, and character animation
- [Image-to-Video Generation](#image-to-video-generation) (44 papers) - Methods for animating still images into videos
- [Long Video Generation](#long-video-generation) (129 papers) - Generating temporally consistent long-form videos beyond short clips
- [Personalization & Customization](#personalization-&-customization) (94 papers) - Personalized video generation with custom subjects, identities, or styles
- [Physical Understanding](#physical-understanding) (122 papers) - Physics-aware video generation and dynamics modeling
- [Surveys & Benchmarks](#surveys-&-benchmarks) (195 papers) - Survey papers, benchmarks, and evaluation metrics for video generation
- [Text-to-Video Generation](#text-to-video-generation) (76 papers) - Foundation models and methods for generating videos from text prompts
- [Video Editing](#video-editing) (36 papers) - Diffusion-based video editing, style transfer, and manipulation
- [Video Inpainting & Completion](#video-inpainting-&-completion) (6 papers) - Video inpainting, completion, outpainting, and temporal prediction
- [Video Super-Resolution & Enhancement](#video-super-resolution-&-enhancement) (58 papers) - Video quality improvement, upscaling, restoration, and frame interpolation
- [World Models & Simulation](#world-models-&-simulation) (102 papers) - Video generation as world simulators and interactive environment generation



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3D-aware Video Generation

- **[ShareVerse: Multi-Agent Consistent Video Generation for Shared World Modeling](https://arxiv.org/abs/2603.02697v1)**  
  Authors: Jiayi Zhu, Jianing Zhang, Yiying Yang, Wei Cheng, Xiaoyun Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02697v1.pdf)  
  Keywords: dit, video generation, multi-view video, world model, simulation, interactive  
- **[HumanOrbit: 3D Human Reconstruction as 360° Orbit Generation](https://arxiv.org/abs/2602.24148v1)**  
  Authors: Keito Suzuki, Kunyao Chen, Lei Wang, Bang Du, Runfa Blark Li, Peng Liu, Ning Bi, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.24148v1.pdf)  
  Keywords: novel view, diffusion model, identity, video diffusion  
- **[BetterScene: 3D Scene Synthesis with Representation-Aligned Generative Model](https://arxiv.org/abs/2602.22596v1)**  
  Authors: Yuci Han, Charles Toth, John E. Anderson, William J. Shuart, Alper Yilmaz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.22596v1.pdf)  
  Keywords: novel view, dit, diffusion model, video diffusion  
- **[Geometry-as-context: Modulating Explicit 3D in Scene-consistent Video Generation to Geometry Context](https://arxiv.org/abs/2602.21929v1)**  
  Authors: JiaKui Hu, Jialun Liu, Liying Yang, Xinliang Zhang, Kaiwen Li, Shuang Zeng, Yuanwei Li, Haibin Huang, Chi Zhang, Yanye Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21929v1.pdf)  
  Keywords: autoregressive, video generation, trajectory, novel view, camera control  
- **[RAYNOVA: Scale-Temporal Autoregressive World Modeling in Ray Space](https://arxiv.org/abs/2602.20685v2)**  
  Authors: Yichen Xie, Chensheng Peng, Mazen Abdelfattah, Yihan Hu, Jiezhi Yang, Eric Higgins, Ryan Brigden, Masayoshi Tomizuka, Wei Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20685v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://raynova-ai.github.io)  
  Keywords: dit, autoregressive, video generation, multi-view video, physical, world model, novel view  
- **[A Single Image and Multimodality Is All You Need for Novel View Synthesis](https://arxiv.org/abs/2602.17909v1)**  
  Authors: Amirhosein Javadi, Chi-Shiang Gau, Konstantinos D. Polyzos, Tara Javidi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.17909v1.pdf)  
  Keywords: video generation, dit, efficient, novel view  
- **[VideoNeuMat: Neural Material Extraction from Generative Video Models](https://arxiv.org/abs/2602.07272v1)**  
  Authors: Bowen Xue, Saeed Hadadan, Zheng Zeng, Fabrice Rousselle, Zahra Montazeri, Milos Hasan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.07272v1.pdf)  
  Keywords: novel view, dit, diffusion model, video diffusion  
- **[CineScene: Implicit 3D as Effective Scene Representation for Cinematic Video Generation](https://arxiv.org/abs/2602.06959v1)**  
  Authors: Kaiyi Huang, Yukun Huang, Yu Li, Jianhong Bai, Xintao Wang, Zinan Lin, Xuefei Ning, Jiwen Yu, Pengfei Wan, Yu Wang, Xihui Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06959v1.pdf)  
  Keywords: dit, video generation, physical, trajectory, video synthesis, text-to-video, 3d-aware  
- **[SkeletonGaussian: Editable 4D Generation through Gaussian Skeletonization](https://arxiv.org/abs/2602.04271v1)**  
  Authors: Lifan Wu, Ruijie Zhu, Yubo Ai, Tianzhu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.04271v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wusar.github.io/projects/skeletongaussian)  
  Keywords: dit, 4d generation  
- **[3D-Aware Implicit Motion Control for View-Adaptive Human Video Generation](https://arxiv.org/abs/2602.03796v2)**  
  Authors: Zhixue Fang, Xu He, Songlin Tang, Haoxian Zhang, Qingfeng Li, Xiaoqiang Liu, Pengfei Wan, Kun Gai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03796v2.pdf)  
  Keywords: dit, dynamics, video generation, human motion, motion control, camera control, 3d-aware  

### Applications

*Showing the latest 50 out of 53 papers*

- **[EduVQA: Benchmarking AI-Generated Video Quality Assessment for Education](https://arxiv.org/abs/2603.03066v1)**  
  Authors: Baoliang Chen, Xinlong Bu, Lingyu Zhu, Hanwei Zhu, Xiangjie Sui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.03066v1.pdf)  
  Keywords: evaluation, education, benchmark, concept, text-to-video, t2v  
- **[MicroVerse: A Preliminary Exploration Toward a Micro-World Simulation](https://arxiv.org/abs/2603.00585v1)**  
  Authors: Rongsheng Wang, Minghao Wu, Hongru Zhou, Zhihan Yu, Zhenyang Cai, Junying Chen, Benyou Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.00585v1.pdf) | [![GitHub](https://img.shields.io/github/stars/FreedomIntelligence/MicroVerse?style=social)](https://github.com/FreedomIntelligence/MicroVerse)  
  Keywords: medical, evaluation, dynamics, video generation, physical, simulation, education, benchmark, concept, interactive  
- **[HorizonForge: Driving Scene Editing with Any Trajectories and Any Vehicles](https://arxiv.org/abs/2602.21333v2)**  
  Authors: Yifan Wang, Francesco Pittaluga, Zaid Tasneem, Chenyu You, Manmohan Chandraker, Ziyu Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21333v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://horizonforge.github.io)  
  Keywords: dit, evaluation, trajectory, controllable, simulation, temporal consistency, benchmark, autonomous driving, video diffusion  
- **[GA-Drive: Geometry-Appearance Decoupled Modeling for Free-viewpoint Driving Scene Generatio](https://arxiv.org/abs/2602.20673v1)**  
  Authors: Hao Zhang, Lue Fan, Qitai Wang, Wenbo Li, Zehuan Wu, Lewei Lu, Zhaoxiang Zhang, Hongsheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20673v1.pdf)  
  Keywords: dit, video-to-video, video editing, trajectory, simulation, diffusion model, autonomous driving, video diffusion  
- **[3DSPA: A 3D Semantic Point Autoencoder for Evaluating Video Realism](https://arxiv.org/abs/2602.20354v1)**  
  Authors: Bhavik Chandna, Kelsey R. Allen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20354v1.pdf) | [![GitHub](https://img.shields.io/github/stars/TheProParadox/3dspa_code?style=social)](https://github.com/TheProParadox/3dspa_code)  
  Keywords: evaluation, video generation, physical, film, trajectory, robotics, temporal consistency, benchmark  
- **[PedaCo-Gen: Scaffolding Pedagogical Agency in Human-AI Collaborative Video Authoring](https://arxiv.org/abs/2602.19623v1)**  
  Authors: Injun Baek, Yearim Kim, Nojun Kwak  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.19623v1.pdf)  
  Keywords: dit, t2v, education, text-to-video, interactive  
- **[VideoSketcher: Video Models Prior Enable Versatile Sequential Sketch Generation](https://arxiv.org/abs/2602.15819v1)**  
  Authors: Hui Ren, Yuval Alaluf, Omer Bar Tal, Alexander Schwing, Antonio Torralba, Yael Vinker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.15819v1.pdf)  
  Keywords: dit, autoregressive, video diffusion, creative, efficient, style, diffusion model, text-to-video, interactive  
- **[Beyond End-to-End Video Models: An LLM-Based Multi-Agent System for Educational Video Generation](https://arxiv.org/abs/2602.11790v1)**  
  Authors: Lingyong Yan, Jiulong Wu, Dong Xie, Weixian Shi, Deguo Xia, Jizhou Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.11790v1.pdf)  
  Keywords: video generation, dit, education  
- **[Ctrl&Shift: High-Quality Geometry-Aware Object Manipulation in Visual Generation](https://arxiv.org/abs/2602.11440v1)**  
  Authors: Penghui Ruan, Bojia Zi, Xianbiao Qi, Youze Huang, Rong Xiao, Pichao Wang, Jiannong Cao, Yuhui Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.11440v1.pdf)  
  Keywords: dit, identity, film, controllable, creative  
- **[VideoWorld 2: Learning Transferable Knowledge from Real-world Videos](https://arxiv.org/abs/2602.10102v1)**  
  Authors: Zhongwei Ren, Yunchao Wei, Xiao Yu, Guixun Luo, Yao Zhao, Bingyi Kang, Jiashi Feng, Xiaojie Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.10102v1.pdf)  
  Keywords: dynamics, autoregressive, video generation, robotics, diffusion model, video diffusion  

### Architecture & Efficiency

*Showing the latest 50 out of 364 papers*

- **[TC-Padé: Trajectory-Consistent Padé Approximation for Diffusion Acceleration](https://arxiv.org/abs/2603.02943v1)**  
  Authors: Benlei Cui, Shaoxuan He, Bukun Huang, Zhizeng Ye, Yunyun Sun, Longtao Huang, Hui Xue, Yang Yang, Jingqun Tang, Zhou Zhao, Haiwen Hong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02943v1.pdf)  
  Keywords: dit, denoising, dynamics, video generation, trajectory, efficient, acceleration, diffusion model  
- **[Interpretable Motion-Attentive Maps: Spatio-Temporally Localizing Concepts in Video Diffusion Transformers](https://arxiv.org/abs/2603.02919v1)**  
  Authors: Youngjun Jun, Seil Kang, Woojung Han, Seong Jae Hwang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02919v1.pdf)  
  Keywords: dit, diffusion transformer, concept, video diffusion  
- **[SemanticDialect: Semantic-Aware Mixed-Format Quantization for Video Diffusion Transformers](https://arxiv.org/abs/2603.02883v1)**  
  Authors: Wonsuk Jang, Thierry Tambe  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02883v1.pdf)  
  Keywords: dit, diffusion transformer, video generation, efficient, video diffusion  
- **[ShareVerse: Multi-Agent Consistent Video Generation for Shared World Modeling](https://arxiv.org/abs/2603.02697v1)**  
  Authors: Jiayi Zhu, Jianing Zhang, Yiying Yang, Wei Cheng, Xiaoyun Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02697v1.pdf)  
  Keywords: dit, video generation, multi-view video, world model, simulation, interactive  
- **[Direct Reward Fine-Tuning on Poses for Single Image to 3D Human in the Wild](https://arxiv.org/abs/2603.02619v1)**  
  Authors: Seunguk Do, Minwoo Huh, Joonghyuk Shin, Jaesik Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02619v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://seunguk-do.github.io/drpose)  
  Keywords: dit, evaluation, human motion, benchmark, diffusion model  
- **[Deep Learning Based Wildfire Detection for Peatland Fires Using Transfer Learning](https://arxiv.org/abs/2603.02465v1)**  
  Authors: Emadeldeen Hamdan, Ahmad Faiz Tharima, Mohd Zahirasri Mohd Tohir, Dayang Nur Sakinah Musa, Erdem Koyuncu, Adam J. Watts, Ahmet Enis Cetin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02465v1.pdf)  
  Keywords: physical, dit  
- **[LiftAvatar: Kinematic-Space Completion for Expression-Controlled 3D Gaussian Avatar Animation](https://arxiv.org/abs/2603.02129v1)**  
  Authors: Hualiang Wei, Shunran Jia, Jialun Liu, Wenhui Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02129v1.pdf)  
  Keywords: dit, diffusion transformer, distillation, controllable, efficient, avatar, video diffusion  
- **[Non-verbal Real-time Human-AI Interaction in Constrained Robotic Environments](https://arxiv.org/abs/2603.01804v1)**  
  Authors: Dragos Costea, Alina Marcu, Cristina Lazar, Marius Leordeanu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01804v1.pdf)  
  Keywords: architecture, body motion, text-to-video  
- **[StepVAR: Structure-Texture Guided Pruning for Visual Autoregressive Models](https://arxiv.org/abs/2603.01757v1)**  
  Authors: Keli Liu, Zhendong Wang, Wengang Zhou, Houqiang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01757v1.pdf)  
  Keywords: architecture, evaluation, autoregressive, efficient, layout, acceleration, text-to-video  
- **[FastLightGen: Fast and Light Video Generation with Fewer Steps and Parameters](https://arxiv.org/abs/2603.01685v1)**  
  Authors: Shao Shitong, Gu Yufei, Xie Zeke  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01685v1.pdf)  
  Keywords: video generation, distillation, efficient, i2v  

### Audio & Multi-modal

- **[UniTalking: A Unified Audio-Video Framework for Talking Portrait Generation](https://arxiv.org/abs/2603.01418v1)**  
  Authors: Hebeizi Li, Zihao Liang, Benyuan Sun, Zihao Yin, Xiao Sha, Chenliang Wang, Yi Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01418v1.pdf)  
  Keywords: architecture, video generation, multi-modal, efficient, style  
- **[FlowPortrait: Reinforcement Learning for Audio-Driven Portrait Video Generation](https://arxiv.org/abs/2603.00159v1)**  
  Authors: Weiting Tan, Andy T. Liu, Ming Tu, Xinghua Qu, Philipp Koehn, Lu Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.00159v1.pdf)  
  Keywords: evaluation, autoregressive, audio-to-video, video generation, audio-driven, temporal consistency  
- **[SkyReels-V4: Multi-modal Video-Audio Generation, Inpainting and Editing model](https://arxiv.org/abs/2602.21818v2)**  
  Authors: Guibin Chen, Dixuan Lin, Jiangping Yang, Youqiang Zhang, Zhengcong Fei, Debang Li, Sheng Chen, Chaofeng Ao, Nuo Pang, Yiming Wang, Yikun Dou, Zheng Chen, Mingyuan Fan, Tuanhui Li, Mingshan Chang, Hao Zhang, Xiaopeng Sun, Jingtao Xu, Yuqiang Xie, Jiahua Wang, Zhiheng Xu, Weiming Xiong, Yuzhe Jin, Baoxuan Gu, Binjie Mao, Yunjie Yu, Jujie He, Yuhao Feng, Shiwen Tu, Chaojie Wang, Rui Yan, Wei Shen, Jingchen Wu, Peng Zhao, Xuanyue Zhong, Zhuangzhuang Liu, Kaifei Wang, Fuxiang Zhang, Weikai Xu, Wenyan Liu, Binglu Zhang, Yu Shen, Tianhui Xiong, Bin Peng, Liang Zeng, Xuchen Song, Haoxiang Guo, Peiyu Wang, Max W. Y. Lam, Chien-Hung Liu, Yahui Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21818v2.pdf)  
  Keywords: architecture, dit, diffusion transformer, video editing, video generation, super-resolution, frame interpolation, image to video, style, multi-modal, sound  
- **[JavisDiT++: Unified Modeling and Optimization for Joint Audio-Video Generation](https://arxiv.org/abs/2602.19163v1)**  
  Authors: Kai Liu, Yanhao Zheng, Kai Wang, Shengqiong Wu, Rongjunchen Zhang, Jiebo Luo, Dimitrios Hatzinakos, Ziwei Liu, Hao Fei, Tat-Seng Chua  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.19163v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://JavisVerse.github.io/JavisDiT2-page)  
  Keywords: dit, evaluation, video generation, sound, t2v  
- **[EchoTorrent: Towards Swift, Sustained, and Streaming Multi-Modal Video Generation](https://arxiv.org/abs/2602.13669v2)**  
  Authors: Rang Meng, Yingjie Yin, Yuming Li, Chenguang Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.13669v2.pdf)  
  Keywords: architecture, identity, streaming, autoregressive, video generation, multi-modal, temporal consistency  
- **[DreamID-Omni: Unified Framework for Controllable Human-Centric Audio-Video Generation](https://arxiv.org/abs/2602.12160v1)**  
  Authors: Xu Guo, Fulong Ye, Qichao Sun, Liyang Chen, Bingchuan Li, Pengze Zhang, Jiawei Liu, Songtao Zhao, Qian He, Xiangwang Hou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.12160v1.pdf)  
  Keywords: dit, diffusion transformer, identity, video editing, video generation, controllable, audio-driven  
- **[TiFRe: Text-guided Video Frame Reduction for Efficient Video Multi-modal Large Language Models](https://arxiv.org/abs/2602.08861v1)**  
  Authors: Xiangtian Zheng, Zishuo Wang, Yuxin Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.08861v1.pdf)  
  Keywords: style, multi-modal, efficient  
- **[VideoVeritas: AI-Generated Video Detection via Perception Pretext Reinforcement Learning](https://arxiv.org/abs/2602.08828v1)**  
  Authors: Hao Tan, Jun Lan, Senyuan Shi, Zichang Tan, Zijian Yu, Huijia Zhu, Weiqiang Wang, Jun Wan, Zhen Lei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.08828v1.pdf)  
  Keywords: video generation, benchmark, multi-modal, evaluation  
- **[MOVA: Towards Scalable and Synchronized Video-Audio Generation](https://arxiv.org/abs/2602.08794v2)**  
  Authors: SII-OpenMOSS Team, :, Donghua Yu, Mingshu Chen, Qi Chen, Qi Luo, Qianyi Wu, Qinyuan Cheng, Ruixiao Li, Tianyi Liang, Wenbo Zhang, Wenming Tu, Xiangyu Peng, Yang Gao, Yanru Huo, Ying Zhu, Yinze Luo, Yiyang Zhang, Yuerong Song, Zhe Xu, Zhiyu Zhang, Chenchen Yang, Cheng Chang, Chushu Zhou, Hanfu Chen, Hongnan Ma, Jiaxi Li, Jingqi Tong, Junxi Liu, Ke Chen, Shimin Li, Shiqi Jiang, Songlin Wang, Wei Jiang, Zhaoye Fei, Zhiyuan Ning, Chunguo Li, Chenhui Li, Ziwei He, Zengfeng Huang, Xie Chen, Xipeng Qiu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.08794v2.pdf)  
  Keywords: architecture, text to video, efficient, sound, t2v  
- **[T2VTree: User-Centered Visual Analytics for Agent-Assisted Thought-to-Video Authoring](https://arxiv.org/abs/2602.08368v1)**  
  Authors: Zhuoyun Zheng, Yu Dong, Gaorong Liang, Guan Li, Guihua Shan, Shiyu Cheng, Dong Tian, Jianlong Zhou, Jie Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.08368v1.pdf) | [![GitHub](https://img.shields.io/github/stars/tezuka0210/T2VTree?style=social)](https://github.com/tezuka0210/T2VTree)  
  Keywords: video generation, dit, multi-modal, t2v  

### Controllable Generation

*Showing the latest 50 out of 115 papers*

- **[TC-Padé: Trajectory-Consistent Padé Approximation for Diffusion Acceleration](https://arxiv.org/abs/2603.02943v1)**  
  Authors: Benlei Cui, Shaoxuan He, Bukun Huang, Zhizeng Ye, Yunyun Sun, Longtao Huang, Hui Xue, Yang Yang, Jingqun Tang, Zhou Zhao, Haiwen Hong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02943v1.pdf)  
  Keywords: dit, denoising, dynamics, video generation, trajectory, efficient, acceleration, diffusion model  
- **[LiftAvatar: Kinematic-Space Completion for Expression-Controlled 3D Gaussian Avatar Animation](https://arxiv.org/abs/2603.02129v1)**  
  Authors: Hualiang Wei, Shunran Jia, Jialun Liu, Wenhui Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02129v1.pdf)  
  Keywords: dit, diffusion transformer, distillation, controllable, efficient, avatar, video diffusion  
- **[WorldStereo: Bridging Camera-Guided Video Generation and Scene Reconstruction via 3D Geometric Memories](https://arxiv.org/abs/2603.02049v1)**  
  Authors: Yisu Zhang, Chenjie Cao, Tengfei Wang, Xuhui Zuo, Junta Wu, Jianke Zhu, Chunchao Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02049v1.pdf)  
  Keywords: video generation, camera control, world model, benchmark, diffusion model, video diffusion  
- **[StepVAR: Structure-Texture Guided Pruning for Visual Autoregressive Models](https://arxiv.org/abs/2603.01757v1)**  
  Authors: Keli Liu, Zhendong Wang, Wengang Zhou, Houqiang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01757v1.pdf)  
  Keywords: architecture, evaluation, autoregressive, efficient, layout, acceleration, text-to-video  
- **[FREE-Edit: Using Editing-aware Injection in Rectified Flow Models for Zero-shot Image-Driven Video Editing](https://arxiv.org/abs/2603.01164v1)**  
  Authors: Maomao Li, Yunfei Liu, Yu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01164v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://free-edit.github.io/page)  
  Keywords: dit, denoising, image-driven, video editing, rectified flow, i2v, image-to-video, layout  
- **[Let Your Image Move with Your Motion! -- Implicit Multi-Object Multi-Motion Transfer](https://arxiv.org/abs/2603.01000v1)**  
  Authors: Yuze Li, Dong Gong, Xiao Cao, Junchao Yuan, Dongsheng Li, Lei Zhou, Yun Sing Koh, Cheng Yan, Xinyu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01000v1.pdf)  
  Keywords: video generation, controllable, i2v, image-to-video, efficient  
- **[COMBAT: Conditional World Models for Behavioral Agent Training](https://arxiv.org/abs/2603.00825v1)**  
  Authors: Anmol Agarwal, Pranay Meshram, Sumer Singh, Saurav Suman, Andrew Lapp, Shahbuland Matiana, Louis Castricato, Spencer Frazier  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.00825v1.pdf)  
  Keywords: dit, diffusion transformer, evaluation, distillation, video generation, controllable, world model, benchmark, diffusion model, interactive  
- **[CamDirector: Towards Long-Term Coherent Video Trajectory Editing](https://arxiv.org/abs/2603.02256v1)**  
  Authors: Zhihao Shi, Kejia Yin, Weilin Wan, Yuhongze Zhou, Yuanhao Yu, Xinxin Zuo, Qiang Sun, Juwei Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02256v1.pdf)  
  Keywords: dit, autoregressive, trajectory, camera control, style, benchmark, diffusion model, video diffusion  
- **[ColoDiff: Integrating Dynamic Consistency With Content Awareness for Colonoscopy Video Generation](https://arxiv.org/abs/2602.23203v1)**  
  Authors: Junhu Fu, Shuyu Liang, Wutong Li, Chen Ma, Peng Huang, Kehao Wang, Ke Chen, Shengli Lin, Pinghong Zhou, Zeju Li, Yuanyuan Wang, Yi Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.23203v1.pdf)  
  Keywords: dit, dynamics, video generation, controllable, temporal consistency, diffusion model  
- **[The Trinity of Consistency as a Defining Principle for General World Models](https://arxiv.org/abs/2602.23152v1)**  
  Authors: Jingxuan Wei, Siyuan Li, Yuhang Xu, Zheng Sun, Junjie Jiang, Hexuan Jin, Caijun Jia, Honghao He, Xinglong Xu, Xi bai, Chang Yu, Yumou Liu, Junnan Zhu, Xuanhe Zhou, Jintao Chen, Xiaobin Hu, Shancheng Pang, Bihui Yu, Ran He, Zhen Lei, Stan Z. Li, Conghui He, Shuicheng Yan, Cheng Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.23152v1.pdf)  
  Keywords: world simulator, architecture, evaluation, dynamics, video generation, physical, trajectory, world model, temporal consistency, benchmark, concept  

### Human & Character Animation

- **[Direct Reward Fine-Tuning on Poses for Single Image to 3D Human in the Wild](https://arxiv.org/abs/2603.02619v1)**  
  Authors: Seunguk Do, Minwoo Huh, Joonghyuk Shin, Jaesik Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02619v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://seunguk-do.github.io/drpose)  
  Keywords: dit, evaluation, human motion, benchmark, diffusion model  
- **[LiftAvatar: Kinematic-Space Completion for Expression-Controlled 3D Gaussian Avatar Animation](https://arxiv.org/abs/2603.02129v1)**  
  Authors: Hualiang Wei, Shunran Jia, Jialun Liu, Wenhui Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02129v1.pdf)  
  Keywords: dit, diffusion transformer, distillation, controllable, efficient, avatar, video diffusion  
- **[Non-verbal Real-time Human-AI Interaction in Constrained Robotic Environments](https://arxiv.org/abs/2603.01804v1)**  
  Authors: Dragos Costea, Alina Marcu, Cristina Lazar, Marius Leordeanu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01804v1.pdf)  
  Keywords: architecture, body motion, text-to-video  
- **[GeoDiff4D: Geometry-Aware Diffusion for 4D Head Avatar Reconstruction](https://arxiv.org/abs/2602.24161v1)**  
  Authors: Chao Xu, Xiaochen Zhao, Xiang Deng, Jingxiang Sun, Zhuo Su, Donglin Di, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.24161v1.pdf)  
  Keywords: video generation, diffusion model, identity, avatar  
- **[Spatio-Temporal Garment Reconstruction Using Diffusion Mapping via Pattern Coordinates](https://arxiv.org/abs/2602.24043v1)**  
  Authors: Yingxuan You, Ren Li, Corentin Dumery, Cong Cao, Hao Li, Pascal Fua  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.24043v1.pdf)  
  Keywords: dit, virtual try-on, temporal consistency, diffusion model, avatar  
- **[BigMaQ: A Big Macaque Motion and Animation Dataset Bridging Image and 3D Pose Representations](https://arxiv.org/abs/2602.19874v1)**  
  Authors: Lucas Martini, Alexander Lappe, Anna Bognár, Rufin Vogels, Martin A. Giese  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.19874v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://martinivis.github.io/BigMaQ)  
  Keywords: benchmark, avatar, dynamics  
- **[Ani3DHuman: Photorealistic 3D Human Animation with Self-guided Stochastic Sampling](https://arxiv.org/abs/2602.19089v1)**  
  Authors: Qi Sun, Can Wang, Jiaxiang Shang, Yingchun Liu, Jing Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.19089v1.pdf) | [![GitHub](https://img.shields.io/github/stars/qiisun/ani3dhuman?style=social)](https://github.com/qiisun/ani3dhuman)  
  Keywords: identity, dynamics, human animation, diffusion model, video diffusion  
- **[HairWeaver: Few-Shot Photorealistic Hair Motion Synthesis with Sim-to-Real Guided Video Diffusion](https://arxiv.org/abs/2602.11117v1)**  
  Authors: Di Chang, Ji Hou, Aljaz Bozic, Assaf Neuberger, Felix Juefei-Xu, Olivier Maury, Gene Wei-Chin Lin, Tuur Stuyck, Doug Roble, Mohammad Soleymani, Stephane Grabli  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.11117v1.pdf)  
  Keywords: dit, evaluation, dynamics, human motion, video diffusion  
- **[Hand2World: Autoregressive Egocentric Interaction Generation via Free-Space Hand Gestures](https://arxiv.org/abs/2602.09600v2)**  
  Authors: Yuxi Wang, Wenqi Ouyang, Tianyi Wei, Yi Dong, Zhiqi Shen, Xingang Pan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.09600v2.pdf)  
  Keywords: dit, gesture, dynamics, autoregressive, video generation, camera control, world model, benchmark, diffusion model, interactive  
- **[AUHead: Realistic Emotional Talking Head Generation via Action Units Control](https://arxiv.org/abs/2602.09534v1)**  
  Authors: Jiayi Lyu, Leigang Qu, Wenjing Zhang, Hanyu Jiang, Kai Liu, Zhenglin Zhou, Xiaobo Xia, Jian Xue, Tat-Seng Chua  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.09534v1.pdf) | [![GitHub](https://img.shields.io/github/stars/laura990501/AUHead_ICLR?style=social)](https://github.com/laura990501/AUHead_ICLR)  
  Keywords: dit, identity, video generation, film, controllable, talking head, motion control, benchmark, diffusion model, avatar, interactive  

### Image-to-Video Generation

- **[FastLightGen: Fast and Light Video Generation with Fewer Steps and Parameters](https://arxiv.org/abs/2603.01685v1)**  
  Authors: Shao Shitong, Gu Yufei, Xie Zeke  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01685v1.pdf)  
  Keywords: video generation, distillation, efficient, i2v  
- **[FREE-Edit: Using Editing-aware Injection in Rectified Flow Models for Zero-shot Image-Driven Video Editing](https://arxiv.org/abs/2603.01164v1)**  
  Authors: Maomao Li, Yunfei Liu, Yu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01164v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://free-edit.github.io/page)  
  Keywords: dit, denoising, image-driven, video editing, rectified flow, i2v, image-to-video, layout  
- **[Let Your Image Move with Your Motion! -- Implicit Multi-Object Multi-Motion Transfer](https://arxiv.org/abs/2603.01000v1)**  
  Authors: Yuze Li, Dong Gong, Xiao Cao, Junchao Yuan, Dongsheng Li, Lei Zhou, Yun Sing Koh, Cheng Yan, Xinyu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01000v1.pdf)  
  Keywords: video generation, controllable, i2v, image-to-video, efficient  
- **[SkyReels-V4: Multi-modal Video-Audio Generation, Inpainting and Editing model](https://arxiv.org/abs/2602.21818v2)**  
  Authors: Guibin Chen, Dixuan Lin, Jiangping Yang, Youqiang Zhang, Zhengcong Fei, Debang Li, Sheng Chen, Chaofeng Ao, Nuo Pang, Yiming Wang, Yikun Dou, Zheng Chen, Mingyuan Fan, Tuanhui Li, Mingshan Chang, Hao Zhang, Xiaopeng Sun, Jingtao Xu, Yuqiang Xie, Jiahua Wang, Zhiheng Xu, Weiming Xiong, Yuzhe Jin, Baoxuan Gu, Binjie Mao, Yunjie Yu, Jujie He, Yuhao Feng, Shiwen Tu, Chaojie Wang, Rui Yan, Wei Shen, Jingchen Wu, Peng Zhao, Xuanyue Zhong, Zhuangzhuang Liu, Kaifei Wang, Fuxiang Zhang, Weikai Xu, Wenyan Liu, Binglu Zhang, Yu Shen, Tianhui Xiong, Bin Peng, Liang Zeng, Xuchen Song, Haoxiang Guo, Peiyu Wang, Max W. Y. Lam, Chien-Hung Liu, Yahui Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21818v2.pdf)  
  Keywords: architecture, dit, diffusion transformer, video editing, video generation, super-resolution, frame interpolation, image to video, style, multi-modal, sound  
- **[MultiAnimate: Pose-Guided Image Animation Made Extensible](https://arxiv.org/abs/2602.21581v1)**  
  Authors: Yingcheng Hu, Haowen Gong, Chuanguang Yang, Zhulin An, Yongjun Xu, Songhua Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21581v1.pdf)  
  Keywords: image animation, dit, diffusion transformer, identity, video generation, pose-guided  
- **[Human Video Generation from a Single Image with 3D Pose and View Control](https://arxiv.org/abs/2602.21188v1)**  
  Authors: Tiantian Wang, Chun-Han Yao, Tao Hu, Mallikarjun Byrasandra Ramalinga Reddy, Ming-Hsuan Yang, Varun Jampani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21188v1.pdf)  
  Keywords: video generation, image-to-video, latent video, diffusion model, video synthesis, video diffusion  
- **[VII: Visual Instruction Injection for Jailbreaking Image-to-Video Generation Models](https://arxiv.org/abs/2602.20999v2)**  
  Authors: Bowen Zheng, Yongli Xiang, Ziming Hong, Zerong Lin, Chaojian Yu, Tongliang Liu, Xinge You  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20999v2.pdf)  
  Keywords: video generation, image-to-video, dit, i2v  
- **[AnimeAgent: Is the Multi-Agent via Image-to-Video models a Good Disney Storytelling Artist?](https://arxiv.org/abs/2602.20664v1)**  
  Authors: Hailong Yan, Shice Liu, Tao Wang, Xiangtao Zhang, Yijie Zhong, Jinwei Chen, Le Zhang, Bo Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20664v1.pdf)  
  Keywords: benchmark, diffusion model, image-to-video, i2v  
- **[Frame2Freq: Spectral Adapters for Fine-Grained Video Understanding](https://arxiv.org/abs/2602.18977v1)**  
  Authors: Thinesh Thiyakesan Ponbagavathi, Constantin Seibold, Alina Roitberg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.18977v1.pdf) | [![GitHub](https://img.shields.io/github/stars/th-nesh/Frame2Freq?style=social)](https://github.com/th-nesh/Frame2Freq)  
  Keywords: image-to-video, dynamics  
- **[FlexAM: Flexible Appearance-Motion Decomposition for Versatile Video Generation Control](https://arxiv.org/abs/2602.13185v1)**  
  Authors: Mingzhi Sheng, Zekai Gu, Peng Li, Cheng Lin, Hao-Xiang Guo, Ying-Cong Chen, Yuan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.13185v1.pdf)  
  Keywords: dit, dynamics, video generation, i2v, camera control  

### Long Video Generation

*Showing the latest 50 out of 129 papers*

- **[StepVAR: Structure-Texture Guided Pruning for Visual Autoregressive Models](https://arxiv.org/abs/2603.01757v1)**  
  Authors: Keli Liu, Zhendong Wang, Wengang Zhou, Houqiang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01757v1.pdf)  
  Keywords: architecture, evaluation, autoregressive, efficient, layout, acceleration, text-to-video  
- **[EraseAnything++: Enabling Concept Erasure in Rectified Flow Transformers Leveraging Multi-Object Optimization](https://arxiv.org/abs/2603.00978v1)**  
  Authors: Zhaoxin Fan, Nanxiang Jiang, Daiheng Gao, Shiji Zhou, Wenjun Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.00978v1.pdf)  
  Keywords: architecture, video generation, rectified flow, video diffusion, temporal consistency, efficient, benchmark, diffusion model, concept, text-to-video, t2v  
- **[DreamWorld: Unified World Modeling in Video Generation](https://arxiv.org/abs/2603.00466v1)**  
  Authors: Boming Tan, Xiangdong Zhang, Ning Liao, Yuqing Zhang, Shaofeng Zhang, Xue Yang, Qi Fan, Yanyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.00466v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ABU121111/DreamWorld?style=social)](https://github.com/ABU121111/DreamWorld)  
  Keywords: dit, evaluation, dynamics, video generation, physical, world model, temporal consistency  
- **[CamDirector: Towards Long-Term Coherent Video Trajectory Editing](https://arxiv.org/abs/2603.02256v1)**  
  Authors: Zhihao Shi, Kejia Yin, Weilin Wan, Yuhongze Zhou, Yuanhao Yu, Xinxin Zuo, Qiang Sun, Juwei Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02256v1.pdf)  
  Keywords: dit, autoregressive, trajectory, camera control, style, benchmark, diffusion model, video diffusion  
- **[Mode Seeking meets Mean Seeking for Fast Long Video Generation](https://arxiv.org/abs/2602.24289v1)**  
  Authors: Shengqu Cai, Weili Nie, Chao Liu, Julius Berner, Lvmin Zhang, Nanye Ma, Hansheng Chen, Maneesh Agrawala, Leonidas Guibas, Gordon Wetzstein, Arash Vahdat  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.24289v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://primecai.github.io/mmm)  
  Keywords: diffusion transformer, flow matching, evaluation, video generation, long-form, long video  
- **[Spatio-Temporal Garment Reconstruction Using Diffusion Mapping via Pattern Coordinates](https://arxiv.org/abs/2602.24043v1)**  
  Authors: Yingxuan You, Ren Li, Corentin Dumery, Cong Cao, Hao Li, Pascal Fua  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.24043v1.pdf)  
  Keywords: dit, virtual try-on, temporal consistency, diffusion model, avatar  
- **[MSVBench: Towards Human-Level Evaluation of Multi-Shot Video Generation](https://arxiv.org/abs/2602.23969v1)**  
  Authors: Haoyuan Shi, Yunxin Li, Nanhao Deng, Zhenran Xu, Xinyu Chen, Longyue Wang, Baotian Hu, Min Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.23969v1.pdf)  
  Keywords: evaluation, video generation, world model, long-form, benchmark  
- **[SwitchCraft: Training-Free Multi-Event Video Generation with Attention Controls](https://arxiv.org/abs/2602.23956v1)**  
  Authors: Qianxun Xu, Chenxi Song, Yujun Cai, Chi Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.23956v1.pdf)  
  Keywords: video generation, video diffusion, temporal consistency, diffusion model, text-to-video  
- **[ColoDiff: Integrating Dynamic Consistency With Content Awareness for Colonoscopy Video Generation](https://arxiv.org/abs/2602.23203v1)**  
  Authors: Junhu Fu, Shuyu Liang, Wutong Li, Chen Ma, Peng Huang, Kehao Wang, Ke Chen, Shengli Lin, Pinghong Zhou, Zeju Li, Yuanyuan Wang, Yi Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.23203v1.pdf)  
  Keywords: dit, dynamics, video generation, controllable, temporal consistency, diffusion model  
- **[Uni-Animator: Towards Unified Visual Colorization](https://arxiv.org/abs/2602.23191v2)**  
  Authors: Xinyuan Chen, Yao Xu, Shaowen Wang, Pengjie Song, Bowen Deng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.23191v2.pdf)  
  Keywords: physical, temporal consistency, diffusion transformer, dit  

### Personalization & Customization

*Showing the latest 50 out of 94 papers*

- **[EduVQA: Benchmarking AI-Generated Video Quality Assessment for Education](https://arxiv.org/abs/2603.03066v1)**  
  Authors: Baoliang Chen, Xinlong Bu, Lingyu Zhu, Hanwei Zhu, Xiangjie Sui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.03066v1.pdf)  
  Keywords: evaluation, education, benchmark, concept, text-to-video, t2v  
- **[Interpretable Motion-Attentive Maps: Spatio-Temporally Localizing Concepts in Video Diffusion Transformers](https://arxiv.org/abs/2603.02919v1)**  
  Authors: Youngjun Jun, Seil Kang, Woojung Han, Seong Jae Hwang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02919v1.pdf)  
  Keywords: dit, diffusion transformer, concept, video diffusion  
- **[UniTalking: A Unified Audio-Video Framework for Talking Portrait Generation](https://arxiv.org/abs/2603.01418v1)**  
  Authors: Hebeizi Li, Zihao Liang, Benyuan Sun, Zihao Yin, Xiao Sha, Chenliang Wang, Yi Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01418v1.pdf)  
  Keywords: architecture, video generation, multi-modal, efficient, style  
- **[Unified Vision-Language Modeling via Concept Space Alignment](https://arxiv.org/abs/2603.01096v1)**  
  Authors: Yifu Qiu, Paul-Ambroise Duquenne, Holger Schwenk  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01096v1.pdf)  
  Keywords: concept, text-to-video  
- **[EraseAnything++: Enabling Concept Erasure in Rectified Flow Transformers Leveraging Multi-Object Optimization](https://arxiv.org/abs/2603.00978v1)**  
  Authors: Zhaoxin Fan, Nanxiang Jiang, Daiheng Gao, Shiji Zhou, Wenjun Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.00978v1.pdf)  
  Keywords: architecture, video generation, rectified flow, video diffusion, temporal consistency, efficient, benchmark, diffusion model, concept, text-to-video, t2v  
- **[WildActor: Unconstrained Identity-Preserving Video Generation](https://arxiv.org/abs/2603.00586v1)**  
  Authors: Qin Guo, Tianyu Yang, Xuanhua He, Fei Shen, Yong Zhang, Zhuoliang Kang, Xiaoming Wei, Dan Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.00586v1.pdf)  
  Keywords: video generation, dit, identity  
- **[MicroVerse: A Preliminary Exploration Toward a Micro-World Simulation](https://arxiv.org/abs/2603.00585v1)**  
  Authors: Rongsheng Wang, Minghao Wu, Hongru Zhou, Zhihan Yu, Zhenyang Cai, Junying Chen, Benyou Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.00585v1.pdf) | [![GitHub](https://img.shields.io/github/stars/FreedomIntelligence/MicroVerse?style=social)](https://github.com/FreedomIntelligence/MicroVerse)  
  Keywords: medical, evaluation, dynamics, video generation, physical, simulation, education, benchmark, concept, interactive  
- **[CamDirector: Towards Long-Term Coherent Video Trajectory Editing](https://arxiv.org/abs/2603.02256v1)**  
  Authors: Zhihao Shi, Kejia Yin, Weilin Wan, Yuhongze Zhou, Yuanhao Yu, Xinxin Zuo, Qiang Sun, Juwei Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02256v1.pdf)  
  Keywords: dit, autoregressive, trajectory, camera control, style, benchmark, diffusion model, video diffusion  
- **[GeoDiff4D: Geometry-Aware Diffusion for 4D Head Avatar Reconstruction](https://arxiv.org/abs/2602.24161v1)**  
  Authors: Chao Xu, Xiaochen Zhao, Xiang Deng, Jingxiang Sun, Zhuo Su, Donglin Di, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.24161v1.pdf)  
  Keywords: video generation, diffusion model, identity, avatar  
- **[HumanOrbit: 3D Human Reconstruction as 360° Orbit Generation](https://arxiv.org/abs/2602.24148v1)**  
  Authors: Keito Suzuki, Kunyao Chen, Lei Wang, Bang Du, Runfa Blark Li, Peng Liu, Ning Bi, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.24148v1.pdf)  
  Keywords: novel view, diffusion model, identity, video diffusion  

### Physical Understanding

*Showing the latest 50 out of 122 papers*

- **[TC-Padé: Trajectory-Consistent Padé Approximation for Diffusion Acceleration](https://arxiv.org/abs/2603.02943v1)**  
  Authors: Benlei Cui, Shaoxuan He, Bukun Huang, Zhizeng Ye, Yunyun Sun, Longtao Huang, Hui Xue, Yang Yang, Jingqun Tang, Zhou Zhao, Haiwen Hong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02943v1.pdf)  
  Keywords: dit, denoising, dynamics, video generation, trajectory, efficient, acceleration, diffusion model  
- **[Deep Learning Based Wildfire Detection for Peatland Fires Using Transfer Learning](https://arxiv.org/abs/2603.02465v1)**  
  Authors: Emadeldeen Hamdan, Ahmad Faiz Tharima, Mohd Zahirasri Mohd Tohir, Dayang Nur Sakinah Musa, Erdem Koyuncu, Adam J. Watts, Ahmet Enis Cetin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02465v1.pdf)  
  Keywords: physical, dit  
- **[MicroVerse: A Preliminary Exploration Toward a Micro-World Simulation](https://arxiv.org/abs/2603.00585v1)**  
  Authors: Rongsheng Wang, Minghao Wu, Hongru Zhou, Zhihan Yu, Zhenyang Cai, Junying Chen, Benyou Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.00585v1.pdf) | [![GitHub](https://img.shields.io/github/stars/FreedomIntelligence/MicroVerse?style=social)](https://github.com/FreedomIntelligence/MicroVerse)  
  Keywords: medical, evaluation, dynamics, video generation, physical, simulation, education, benchmark, concept, interactive  
- **[DreamWorld: Unified World Modeling in Video Generation](https://arxiv.org/abs/2603.00466v1)**  
  Authors: Boming Tan, Xiangdong Zhang, Ning Liao, Yuqing Zhang, Shaofeng Zhang, Xue Yang, Qi Fan, Yanyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.00466v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ABU121111/DreamWorld?style=social)](https://github.com/ABU121111/DreamWorld)  
  Keywords: dit, evaluation, dynamics, video generation, physical, world model, temporal consistency  
- **[ColoDiff: Integrating Dynamic Consistency With Content Awareness for Colonoscopy Video Generation](https://arxiv.org/abs/2602.23203v1)**  
  Authors: Junhu Fu, Shuyu Liang, Wutong Li, Chen Ma, Peng Huang, Kehao Wang, Ke Chen, Shengli Lin, Pinghong Zhou, Zeju Li, Yuanyuan Wang, Yi Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.23203v1.pdf)  
  Keywords: dit, dynamics, video generation, controllable, temporal consistency, diffusion model  
- **[Uni-Animator: Towards Unified Visual Colorization](https://arxiv.org/abs/2602.23191v2)**  
  Authors: Xinyuan Chen, Yao Xu, Shaowen Wang, Pengjie Song, Bowen Deng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.23191v2.pdf)  
  Keywords: physical, temporal consistency, diffusion transformer, dit  
- **[The Trinity of Consistency as a Defining Principle for General World Models](https://arxiv.org/abs/2602.23152v1)**  
  Authors: Jingxuan Wei, Siyuan Li, Yuhang Xu, Zheng Sun, Junjie Jiang, Hexuan Jin, Caijun Jia, Honghao He, Xinglong Xu, Xi bai, Chang Yu, Yumou Liu, Junnan Zhu, Xuanhe Zhou, Jintao Chen, Xiaobin Hu, Shancheng Pang, Bihui Yu, Ran He, Zhen Lei, Stan Z. Li, Conghui He, Shuicheng Yan, Cheng Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.23152v1.pdf)  
  Keywords: world simulator, architecture, evaluation, dynamics, video generation, physical, trajectory, world model, temporal consistency, benchmark, concept  
- **[Hierarchic-EEG2Text: Assessing EEG-To-Text Decoding across Hierarchical Abstraction Levels](https://arxiv.org/abs/2602.20932v1)**  
  Authors: Anupam Sharma, Harish Katti, Prajwal Singh, Shanmuganathan Raman, Krishna Miyapuram  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20932v1.pdf)  
  Keywords: architecture, concept, dynamics  
- **[RAYNOVA: Scale-Temporal Autoregressive World Modeling in Ray Space](https://arxiv.org/abs/2602.20685v2)**  
  Authors: Yichen Xie, Chensheng Peng, Mazen Abdelfattah, Yihan Hu, Jiezhi Yang, Eric Higgins, Ryan Brigden, Masayoshi Tomizuka, Wei Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20685v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://raynova-ai.github.io)  
  Keywords: dit, autoregressive, video generation, multi-view video, physical, world model, novel view  
- **[LESA: Learnable Stage-Aware Predictors for Diffusion Model Acceleration](https://arxiv.org/abs/2602.20497v1)**  
  Authors: Peiliang Cai, Jiacheng Liu, Haowen Xu, Xinyu Wang, Chang Zou, Linfeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20497v1.pdf)  
  Keywords: architecture, dit, diffusion transformer, denoising, dynamics, video generation, acceleration, diffusion model, video synthesis, text-to-video  

### Surveys & Benchmarks

*Showing the latest 50 out of 195 papers*

- **[EduVQA: Benchmarking AI-Generated Video Quality Assessment for Education](https://arxiv.org/abs/2603.03066v1)**  
  Authors: Baoliang Chen, Xinlong Bu, Lingyu Zhu, Hanwei Zhu, Xiangjie Sui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.03066v1.pdf)  
  Keywords: evaluation, education, benchmark, concept, text-to-video, t2v  
- **[BrandFusion: A Multi-Agent Framework for Seamless Brand Integration in Text-to-Video Generation](https://arxiv.org/abs/2603.02816v1)**  
  Authors: Zihao Zhu, Ruotong Wang, Siwei Lyu, Min Zhang, Baoyuan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02816v1.pdf)  
  Keywords: video generation, evaluation, text-to-video, t2v  
- **[Direct Reward Fine-Tuning on Poses for Single Image to 3D Human in the Wild](https://arxiv.org/abs/2603.02619v1)**  
  Authors: Seunguk Do, Minwoo Huh, Joonghyuk Shin, Jaesik Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02619v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://seunguk-do.github.io/drpose)  
  Keywords: dit, evaluation, human motion, benchmark, diffusion model  
- **[MUSE: A Run-Centric Platform for Multimodal Unified Safety Evaluation of Large Language Models](https://arxiv.org/abs/2603.02482v1)**  
  Authors: Zhongxi Wang, Yueqian Lin, Jingyang Zhang, Hai Helen Li, Yiran Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02482v1.pdf)  
  Keywords: evaluation  
- **[HAMMER: Harnessing MLLM via Cross-Modal Integration for Intention-Driven 3D Affordance Grounding](https://arxiv.org/abs/2603.02329v1)**  
  Authors: Lei Yao, Yong Chen, Yuejiao Su, Yi Wang, Moyun Liu, Lap-Pui Chau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02329v1.pdf)  
  Keywords: benchmark  
- **[WorldStereo: Bridging Camera-Guided Video Generation and Scene Reconstruction via 3D Geometric Memories](https://arxiv.org/abs/2603.02049v1)**  
  Authors: Yisu Zhang, Chenjie Cao, Tengfei Wang, Xuhui Zuo, Junta Wu, Jianke Zhu, Chunchao Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02049v1.pdf)  
  Keywords: video generation, camera control, world model, benchmark, diffusion model, video diffusion  
- **[StepVAR: Structure-Texture Guided Pruning for Visual Autoregressive Models](https://arxiv.org/abs/2603.01757v1)**  
  Authors: Keli Liu, Zhendong Wang, Wengang Zhou, Houqiang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01757v1.pdf)  
  Keywords: architecture, evaluation, autoregressive, efficient, layout, acceleration, text-to-video  
- **[Adaptive Spectral Feature Forecasting for Diffusion Sampling Acceleration](https://arxiv.org/abs/2603.01623v1)**  
  Authors: Jiaqi Han, Juntong Shi, Puheng Li, Haotian Ye, Qiushan Guo, Stefano Ermon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01623v1.pdf)  
  Keywords: diffusion transformer, evaluation, video generation, efficient, acceleration, diffusion model, video diffusion  
- **[EraseAnything++: Enabling Concept Erasure in Rectified Flow Transformers Leveraging Multi-Object Optimization](https://arxiv.org/abs/2603.00978v1)**  
  Authors: Zhaoxin Fan, Nanxiang Jiang, Daiheng Gao, Shiji Zhou, Wenjun Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.00978v1.pdf)  
  Keywords: architecture, video generation, rectified flow, video diffusion, temporal consistency, efficient, benchmark, diffusion model, concept, text-to-video, t2v  
- **[COMBAT: Conditional World Models for Behavioral Agent Training](https://arxiv.org/abs/2603.00825v1)**  
  Authors: Anmol Agarwal, Pranay Meshram, Sumer Singh, Saurav Suman, Andrew Lapp, Shahbuland Matiana, Louis Castricato, Spencer Frazier  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.00825v1.pdf)  
  Keywords: dit, diffusion transformer, evaluation, distillation, video generation, controllable, world model, benchmark, diffusion model, interactive  

### Text-to-Video Generation

*Showing the latest 50 out of 76 papers*

- **[EduVQA: Benchmarking AI-Generated Video Quality Assessment for Education](https://arxiv.org/abs/2603.03066v1)**  
  Authors: Baoliang Chen, Xinlong Bu, Lingyu Zhu, Hanwei Zhu, Xiangjie Sui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.03066v1.pdf)  
  Keywords: evaluation, education, benchmark, concept, text-to-video, t2v  
- **[BrandFusion: A Multi-Agent Framework for Seamless Brand Integration in Text-to-Video Generation](https://arxiv.org/abs/2603.02816v1)**  
  Authors: Zihao Zhu, Ruotong Wang, Siwei Lyu, Min Zhang, Baoyuan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02816v1.pdf)  
  Keywords: video generation, evaluation, text-to-video, t2v  
- **[Non-verbal Real-time Human-AI Interaction in Constrained Robotic Environments](https://arxiv.org/abs/2603.01804v1)**  
  Authors: Dragos Costea, Alina Marcu, Cristina Lazar, Marius Leordeanu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01804v1.pdf)  
  Keywords: architecture, body motion, text-to-video  
- **[StepVAR: Structure-Texture Guided Pruning for Visual Autoregressive Models](https://arxiv.org/abs/2603.01757v1)**  
  Authors: Keli Liu, Zhendong Wang, Wengang Zhou, Houqiang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01757v1.pdf)  
  Keywords: architecture, evaluation, autoregressive, efficient, layout, acceleration, text-to-video  
- **[Retrieval, Refinement, and Ranking for Text-to-Video Generation via Prompt Optimization and Test-Time Scaling](https://arxiv.org/abs/2603.01509v1)**  
  Authors: Zillur Rahman, Alex Sheng, Cristian Meo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01509v1.pdf)  
  Keywords: dit, video generation, frame interpolation, efficient, diffusion model, text-to-video, t2v  
- **[Unified Vision-Language Modeling via Concept Space Alignment](https://arxiv.org/abs/2603.01096v1)**  
  Authors: Yifu Qiu, Paul-Ambroise Duquenne, Holger Schwenk  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01096v1.pdf)  
  Keywords: concept, text-to-video  
- **[EraseAnything++: Enabling Concept Erasure in Rectified Flow Transformers Leveraging Multi-Object Optimization](https://arxiv.org/abs/2603.00978v1)**  
  Authors: Zhaoxin Fan, Nanxiang Jiang, Daiheng Gao, Shiji Zhou, Wenjun Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.00978v1.pdf)  
  Keywords: architecture, video generation, rectified flow, video diffusion, temporal consistency, efficient, benchmark, diffusion model, concept, text-to-video, t2v  
- **[SwitchCraft: Training-Free Multi-Event Video Generation with Attention Controls](https://arxiv.org/abs/2602.23956v1)**  
  Authors: Qianxun Xu, Chenxi Song, Yujun Cai, Chi Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.23956v1.pdf)  
  Keywords: video generation, video diffusion, temporal consistency, diffusion model, text-to-video  
- **[SKeDA: A Generative Watermarking Framework for Text-to-video Diffusion Models](https://arxiv.org/abs/2603.00194v1)**  
  Authors: Yang Yang, Xinze Zou, Zehua Ma, Han Fang, Weiming Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.00194v1.pdf)  
  Keywords: video generation, diffusion model, text-to-video, video diffusion  
- **[SPATIALALIGN: Aligning Dynamic Spatial Relationships in Video Generation](https://arxiv.org/abs/2602.22745v2)**  
  Authors: Fengming Liu, Tat-Jen Cham, Chuanxia Zheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.22745v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://fengming001ntu.github.io/SpatialAlign)  
  Keywords: video generation, evaluation, text-to-video, t2v  

### Video Editing

- **[FREE-Edit: Using Editing-aware Injection in Rectified Flow Models for Zero-shot Image-Driven Video Editing](https://arxiv.org/abs/2603.01164v1)**  
  Authors: Maomao Li, Yunfei Liu, Yu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01164v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://free-edit.github.io/page)  
  Keywords: dit, denoising, image-driven, video editing, rectified flow, i2v, image-to-video, layout  
- **[UniVBench: Towards Unified Evaluation for Video Foundation Models](https://arxiv.org/abs/2602.21835v1)**  
  Authors: Jianhui Wei, Xiaotian Zhang, Yichen Li, Yuan Wang, Yan Zhang, Ziyi Chen, Zhihang Tang, Wei Xu, Zuozhu Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21835v1.pdf)  
  Keywords: dit, evaluation, video editing, video generation, benchmark  
- **[SkyReels-V4: Multi-modal Video-Audio Generation, Inpainting and Editing model](https://arxiv.org/abs/2602.21818v2)**  
  Authors: Guibin Chen, Dixuan Lin, Jiangping Yang, Youqiang Zhang, Zhengcong Fei, Debang Li, Sheng Chen, Chaofeng Ao, Nuo Pang, Yiming Wang, Yikun Dou, Zheng Chen, Mingyuan Fan, Tuanhui Li, Mingshan Chang, Hao Zhang, Xiaopeng Sun, Jingtao Xu, Yuqiang Xie, Jiahua Wang, Zhiheng Xu, Weiming Xiong, Yuzhe Jin, Baoxuan Gu, Binjie Mao, Yunjie Yu, Jujie He, Yuhao Feng, Shiwen Tu, Chaojie Wang, Rui Yan, Wei Shen, Jingchen Wu, Peng Zhao, Xuanyue Zhong, Zhuangzhuang Liu, Kaifei Wang, Fuxiang Zhang, Weikai Xu, Wenyan Liu, Binglu Zhang, Yu Shen, Tianhui Xiong, Bin Peng, Liang Zeng, Xuchen Song, Haoxiang Guo, Peiyu Wang, Max W. Y. Lam, Chien-Hung Liu, Yahui Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21818v2.pdf)  
  Keywords: architecture, dit, diffusion transformer, video editing, video generation, super-resolution, frame interpolation, image to video, style, multi-modal, sound  
- **[GA-Drive: Geometry-Appearance Decoupled Modeling for Free-viewpoint Driving Scene Generatio](https://arxiv.org/abs/2602.20673v1)**  
  Authors: Hao Zhang, Lue Fan, Qitai Wang, Wenbo Li, Zehuan Wu, Lewei Lu, Zhaoxiang Zhang, Hongsheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20673v1.pdf)  
  Keywords: dit, video-to-video, video editing, trajectory, simulation, diffusion model, autonomous driving, video diffusion  
- **[PropFly: Learning to Propagate via On-the-Fly Supervision from Pre-trained Video Diffusion Models](https://arxiv.org/abs/2602.20583v1)**  
  Authors: Wonyong Seo, Jaeho Moon, Jaehyup Lee, Soo Ye Kim, Munchurl Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20583v1.pdf)  
  Keywords: dit, flow matching, video editing, diffusion model, video diffusion  
- **[RoboCurate: Harnessing Diversity with Action-Verified Neural Trajectory for Robot Learning](https://arxiv.org/abs/2602.18742v1)**  
  Authors: Seungku Kim, Suhyeok Jang, Byungjun Yoon, Dongyoung Kim, John Won, Jinwoo Shin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.18742v1.pdf)  
  Keywords: dit, video-to-video, physical, trajectory, simulation  
- **[When Test-Time Guidance Is Enough: Fast Image and Video Editing with Diffusion Guidance](https://arxiv.org/abs/2602.14157v1)**  
  Authors: Ahmed Ghorbel, Badr Moufad, Navid Bagheri Shouraki, Alain Oliviero Durmus, Thomas Hirtz, Eric Moulines, Jimmy Olsson, Yazid Janati  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.14157v1.pdf)  
  Keywords: benchmark, dit, evaluation, video editing  
- **[DreamID-Omni: Unified Framework for Controllable Human-Centric Audio-Video Generation](https://arxiv.org/abs/2602.12160v1)**  
  Authors: Xu Guo, Fulong Ye, Qichao Sun, Liyang Chen, Bingchuan Li, Pengze Zhang, Jiawei Liu, Songtao Zhao, Qian He, Xiangwang Hou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.12160v1.pdf)  
  Keywords: dit, diffusion transformer, identity, video editing, video generation, controllable, audio-driven  
- **[Tele-Omni: a Unified Multimodal Framework for Video Generation and Editing](https://arxiv.org/abs/2602.09609v2)**  
  Authors: Jialun Liu, Tian Li, Xiao Cao, Yukuo Ma, Gonghu Shang, Haibin Huang, Chi Zhang, Xiangzhen Chang, Zhiyong Huang, Jiakui Hu, Zuoxin Li, Yuanzhi Liang, Cong Liu, Junqi Liu, Robby T. Tan, Haitong Tang, Qizhen Weng, Yifan Xu, Liying Yang, Xiaoyan Yang, Peng Yu, Shiwen Zhang, Xuelong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.09609v2.pdf)  
  Keywords: dit, video editing, video generation, image-to-video, video synthesis, text-to-video  
- **[Omni-Video 2: Scaling MLLM-Conditioned Diffusion for Unified Video Generation and Editing](https://arxiv.org/abs/2602.08820v1)**  
  Authors: Hao Yang, Zhiyu Tan, Jia Gong, Luozheng Qin, Hesen Chen, Xiaomeng Yang, Yuqing Sun, Yuetan Lin, Mengping Yang, Hao Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.08820v1.pdf)  
  Keywords: dit, video editing, video generation, video diffusion, efficient, benchmark, diffusion model, text-to-video  

### Video Inpainting & Completion

- **[Learning Physics-Grounded 4D Dynamics with Neural Gaussian Force Fields](https://arxiv.org/abs/2602.00148v2)**  
  Authors: Shiqian Li, Ruihong Shen, Junfeng Ni, Chang Pan, Chi Zhang, Yixin Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.00148v2.pdf)  
  Keywords: physics, evaluation, dynamics, video generation, physical, video prediction, world model, simulation, interactive  
- **[DriveLaW:Unifying Planning and Video Generation in a Latent Driving World](https://arxiv.org/abs/2512.23421v2)**  
  Authors: Tianze Xia, Yongkang Li, Lijun Zhou, Jingfeng Yao, Kaixin Xiong, Haiyang Sun, Bing Wang, Kun Ma, Guang Chen, Hangjun Ye, Wenyu Liu, Xinggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.23421v2.pdf)  
  Keywords: architecture, video generation, trajectory, video prediction, world model, benchmark, autonomous driving  
- **[Autoregressive Flow Matching for Motion Prediction](https://arxiv.org/abs/2512.22688v1)**  
  Authors: Johnathan Xie, Stefan Stojanov, Cristobal Eyzaguirre, Daniel L. K. Yamins, Jiajun Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.22688v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Johnathan-Xie/arfm-motion-prediction?style=social)](https://github.com/Johnathan-Xie/arfm-motion-prediction)  
  Keywords: dit, flow matching, autoregressive, video generation, human motion, video prediction, robotics, benchmark  
- **[Over++: Generative Video Compositing for Layer Interaction Effects](https://arxiv.org/abs/2512.19661v1)**  
  Authors: Luchao Qi, Jiaye Wu, Jun Myeong Choi, Cary Phillips, Roni Sengupta, Dan B Goldman  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.19661v1.pdf)  
  Keywords: video inpainting, dit  
- **[Vidarc: Embodied Video Diffusion Model for Closed-loop Control](https://arxiv.org/abs/2512.17661v1)**  
  Authors: Yao Feng, Chendong Xiang, Xinyi Mao, Hengkai Tan, Zuyue Zhang, Shuhe Huang, Kaiwen Zheng, Haitian Liu, Hang Su, Jun Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.17661v1.pdf)  
  Keywords: dynamics, autoregressive, physical, video prediction, diffusion model, video diffusion  
- **[Flowception: Temporally Expansive Flow Matching for Video Generation](https://arxiv.org/abs/2512.11438v1)**  
  Authors: Tariq Berrada Ifriqi, John Nguyen, Karteek Alahari, Jakob Verbeek, Ricky T. Q. Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.11438v1.pdf)  
  Keywords: flow matching, denoising, autoregressive, video generation, image-to-video, efficient, video interpolation  

### Video Super-Resolution & Enhancement

*Showing the latest 50 out of 58 papers*

- **[TC-Padé: Trajectory-Consistent Padé Approximation for Diffusion Acceleration](https://arxiv.org/abs/2603.02943v1)**  
  Authors: Benlei Cui, Shaoxuan He, Bukun Huang, Zhizeng Ye, Yunyun Sun, Longtao Huang, Hui Xue, Yang Yang, Jingqun Tang, Zhou Zhao, Haiwen Hong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02943v1.pdf)  
  Keywords: dit, denoising, dynamics, video generation, trajectory, efficient, acceleration, diffusion model  
- **[Retrieval, Refinement, and Ranking for Text-to-Video Generation via Prompt Optimization and Test-Time Scaling](https://arxiv.org/abs/2603.01509v1)**  
  Authors: Zillur Rahman, Alex Sheng, Cristian Meo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01509v1.pdf)  
  Keywords: dit, video generation, frame interpolation, efficient, diffusion model, text-to-video, t2v  
- **[FREE-Edit: Using Editing-aware Injection in Rectified Flow Models for Zero-shot Image-Driven Video Editing](https://arxiv.org/abs/2603.01164v1)**  
  Authors: Maomao Li, Yunfei Liu, Yu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01164v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://free-edit.github.io/page)  
  Keywords: dit, denoising, image-driven, video editing, rectified flow, i2v, image-to-video, layout  
- **[SenCache: Accelerating Diffusion Model Inference via Sensitivity-Aware Caching](https://arxiv.org/abs/2602.24208v1)**  
  Authors: Yasaman Haghighi, Alexandre Alahi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.24208v1.pdf)  
  Keywords: video generation, acceleration, diffusion model, denoising  
- **[Denoising as Path Planning: Training-Free Acceleration of Diffusion Models with DPCache](https://arxiv.org/abs/2602.22654v1)**  
  Authors: Bowen Cui, Yuanbin Wang, Huajiang Xu, Biaolong Chen, Aixi Zhang, Hao Jiang, Zhengzheng Jin, Xu Liu, Pipei Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.22654v1.pdf) | [![GitHub](https://img.shields.io/github/stars/argsss/DPCache?style=social)](https://github.com/argsss/DPCache)  
  Keywords: dit, denoising, video generation, trajectory, efficient, acceleration, diffusion model  
- **[SkyReels-V4: Multi-modal Video-Audio Generation, Inpainting and Editing model](https://arxiv.org/abs/2602.21818v2)**  
  Authors: Guibin Chen, Dixuan Lin, Jiangping Yang, Youqiang Zhang, Zhengcong Fei, Debang Li, Sheng Chen, Chaofeng Ao, Nuo Pang, Yiming Wang, Yikun Dou, Zheng Chen, Mingyuan Fan, Tuanhui Li, Mingshan Chang, Hao Zhang, Xiaopeng Sun, Jingtao Xu, Yuqiang Xie, Jiahua Wang, Zhiheng Xu, Weiming Xiong, Yuzhe Jin, Baoxuan Gu, Binjie Mao, Yunjie Yu, Jujie He, Yuhao Feng, Shiwen Tu, Chaojie Wang, Rui Yan, Wei Shen, Jingchen Wu, Peng Zhao, Xuanyue Zhong, Zhuangzhuang Liu, Kaifei Wang, Fuxiang Zhang, Weikai Xu, Wenyan Liu, Binglu Zhang, Yu Shen, Tianhui Xiong, Bin Peng, Liang Zeng, Xuchen Song, Haoxiang Guo, Peiyu Wang, Max W. Y. Lam, Chien-Hung Liu, Yahui Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21818v2.pdf)  
  Keywords: architecture, dit, diffusion transformer, video editing, video generation, super-resolution, frame interpolation, image to video, style, multi-modal, sound  
- **[LESA: Learnable Stage-Aware Predictors for Diffusion Model Acceleration](https://arxiv.org/abs/2602.20497v1)**  
  Authors: Peiliang Cai, Jiacheng Liu, Haowen Xu, Xinyu Wang, Chang Zou, Linfeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20497v1.pdf)  
  Keywords: architecture, dit, diffusion transformer, denoising, dynamics, video generation, acceleration, diffusion model, video synthesis, text-to-video  
- **[UniE2F: A Unified Diffusion Framework for Event-to-Frame Reconstruction with Video Foundation Models](https://arxiv.org/abs/2602.19202v1)**  
  Authors: Gang Xu, Zhiyu Zhu, Junhui Hou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.19202v1.pdf) | [![GitHub](https://img.shields.io/github/stars/CS-GangXu/UniE2F?style=social)](https://github.com/CS-GangXu/UniE2F)  
  Keywords: dit, physical, frame interpolation, diffusion model, video diffusion  
- **[Predict to Skip: Linear Multistep Feature Forecasting for Efficient Diffusion Transformers](https://arxiv.org/abs/2602.18093v1)**  
  Authors: Hanshuai Cui, Zhiqing Tang, Qianli Ma, Zhi Yao, Weijia Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.18093v1.pdf)  
  Keywords: dit, diffusion transformer, denoising, dynamics, video generation, trajectory, efficient, acceleration  
- **[DDiT: Dynamic Patch Scheduling for Efficient Diffusion Transformers](https://arxiv.org/abs/2602.16968v1)**  
  Authors: Dahye Kim, Deepti Ghadiyaram, Raghudeep Gadde  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.16968v1.pdf)  
  Keywords: dit, diffusion transformer, denoising, video generation, efficient  

### World Models & Simulation

*Showing the latest 50 out of 102 papers*

- **[ShareVerse: Multi-Agent Consistent Video Generation for Shared World Modeling](https://arxiv.org/abs/2603.02697v1)**  
  Authors: Jiayi Zhu, Jianing Zhang, Yiying Yang, Wei Cheng, Xiaoyun Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02697v1.pdf)  
  Keywords: dit, video generation, multi-view video, world model, simulation, interactive  
- **[WorldStereo: Bridging Camera-Guided Video Generation and Scene Reconstruction via 3D Geometric Memories](https://arxiv.org/abs/2603.02049v1)**  
  Authors: Yisu Zhang, Chenjie Cao, Tengfei Wang, Xuhui Zuo, Junta Wu, Jianke Zhu, Chunchao Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02049v1.pdf)  
  Keywords: video generation, camera control, world model, benchmark, diffusion model, video diffusion  
- **[COMBAT: Conditional World Models for Behavioral Agent Training](https://arxiv.org/abs/2603.00825v1)**  
  Authors: Anmol Agarwal, Pranay Meshram, Sumer Singh, Saurav Suman, Andrew Lapp, Shahbuland Matiana, Louis Castricato, Spencer Frazier  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.00825v1.pdf)  
  Keywords: dit, diffusion transformer, evaluation, distillation, video generation, controllable, world model, benchmark, diffusion model, interactive  
- **[MicroVerse: A Preliminary Exploration Toward a Micro-World Simulation](https://arxiv.org/abs/2603.00585v1)**  
  Authors: Rongsheng Wang, Minghao Wu, Hongru Zhou, Zhihan Yu, Zhenyang Cai, Junying Chen, Benyou Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.00585v1.pdf) | [![GitHub](https://img.shields.io/github/stars/FreedomIntelligence/MicroVerse?style=social)](https://github.com/FreedomIntelligence/MicroVerse)  
  Keywords: medical, evaluation, dynamics, video generation, physical, simulation, education, benchmark, concept, interactive  
- **[DreamWorld: Unified World Modeling in Video Generation](https://arxiv.org/abs/2603.00466v1)**  
  Authors: Boming Tan, Xiangdong Zhang, Ning Liao, Yuqing Zhang, Shaofeng Zhang, Xue Yang, Qi Fan, Yanyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.00466v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ABU121111/DreamWorld?style=social)](https://github.com/ABU121111/DreamWorld)  
  Keywords: dit, evaluation, dynamics, video generation, physical, world model, temporal consistency  
- **[MSVBench: Towards Human-Level Evaluation of Multi-Shot Video Generation](https://arxiv.org/abs/2602.23969v1)**  
  Authors: Haoyuan Shi, Yunxin Li, Nanhao Deng, Zhenran Xu, Xinyu Chen, Longyue Wang, Baotian Hu, Min Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.23969v1.pdf)  
  Keywords: evaluation, video generation, world model, long-form, benchmark  
- **[U-Mind: A Unified Framework for Real-Time Multimodal Interaction with Audiovisual Generation](https://arxiv.org/abs/2602.23739v1)**  
  Authors: Xiang Deng, Feng Gao, Yong Zhang, Youxin Pang, Xu Xiaoming, Zhuoliang Kang, Xiaoming Wei, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.23739v1.pdf)  
  Keywords: dit, video synthesis, interactive  
- **[The Trinity of Consistency as a Defining Principle for General World Models](https://arxiv.org/abs/2602.23152v1)**  
  Authors: Jingxuan Wei, Siyuan Li, Yuhang Xu, Zheng Sun, Junjie Jiang, Hexuan Jin, Caijun Jia, Honghao He, Xinglong Xu, Xi bai, Chang Yu, Yumou Liu, Junnan Zhu, Xuanhe Zhou, Jintao Chen, Xiaobin Hu, Shancheng Pang, Bihui Yu, Ran He, Zhen Lei, Stan Z. Li, Conghui He, Shuicheng Yan, Cheng Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.23152v1.pdf)  
  Keywords: world simulator, architecture, evaluation, dynamics, video generation, physical, trajectory, world model, temporal consistency, benchmark, concept  
- **[UCM: Unifying Camera Control and Memory with Time-aware Positional Encoding Warping for World Models](https://arxiv.org/abs/2602.22960v1)**  
  Authors: Tianxing Xu, Zixuan Wang, Guangyuan Wang, Li Hu, Zhongyi Zhang, Peng Zhang, Bang Zhang, Song-Hai Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.22960v1.pdf)  
  Keywords: diffusion transformer, video generation, camera control, world model, efficient, benchmark, interactive  
- **[Flow Matching is Adaptive to Manifold Structures](https://arxiv.org/abs/2602.22486v1)**  
  Authors: Shivam Kumar, Yixin Wang, Lizhen Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.22486v1.pdf)  
  Keywords: video generation, flow matching, simulation  



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
