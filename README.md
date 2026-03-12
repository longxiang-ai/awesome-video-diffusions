# Awesome Video Diffusions [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Video Diffusion Models and Video Generation. Content is automatically updated daily.

> Last Update: 2026-03-12 02:08:58

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

- [3D-aware Video Generation](#3d-aware-video-generation) (24 papers) - Video generation with 3D awareness, multi-view consistency, and 4D content creation
- [Applications](#applications) (48 papers) - Domain-specific applications of video diffusion models
- [Architecture & Efficiency](#architecture-&-efficiency) (362 papers) - Architectural innovations (DiT, UNet), flow matching, and training/inference efficiency
- [Audio & Multi-modal](#audio-&-multi-modal) (32 papers) - Audio-driven and multi-modal conditioned video generation
- [Controllable Generation](#controllable-generation) (110 papers) - Controllable video generation with motion, camera, pose, or layout guidance
- [Human & Character Animation](#human-&-character-animation) (35 papers) - Human-centric video generation including talking heads, dance, and character animation
- [Image-to-Video Generation](#image-to-video-generation) (41 papers) - Methods for animating still images into videos
- [Long Video Generation](#long-video-generation) (120 papers) - Generating temporally consistent long-form videos beyond short clips
- [Personalization & Customization](#personalization-&-customization) (93 papers) - Personalized video generation with custom subjects, identities, or styles
- [Physical Understanding](#physical-understanding) (129 papers) - Physics-aware video generation and dynamics modeling
- [Surveys & Benchmarks](#surveys-&-benchmarks) (197 papers) - Survey papers, benchmarks, and evaluation metrics for video generation
- [Text-to-Video Generation](#text-to-video-generation) (72 papers) - Foundation models and methods for generating videos from text prompts
- [Video Editing](#video-editing) (38 papers) - Diffusion-based video editing, style transfer, and manipulation
- [Video Inpainting & Completion](#video-inpainting-&-completion) (7 papers) - Video inpainting, completion, outpainting, and temporal prediction
- [Video Super-Resolution & Enhancement](#video-super-resolution-&-enhancement) (58 papers) - Video quality improvement, upscaling, restoration, and frame interpolation
- [World Models & Simulation](#world-models-&-simulation) (93 papers) - Video generation as world simulators and interactive environment generation



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3D-aware Video Generation

- **[ConfCtrl: Enabling Precise Camera Control in Video Diffusion via Confidence-Aware Interpolation](https://arxiv.org/abs/2603.09819v1)**  
  Authors: Liudi Yang, George Eskandar, Fengyi Shen, Mohammad Altillawi, Yang Bai, Chi Zhang, Ziyuan Liu, Abhinav Valada  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09819v1.pdf)  
  Keywords: novel view, diffusion model, camera control, video diffusion, dit, video interpolation  
- **[Transformer-Based Inpainting for Real-Time 3D Streaming in Sparse Multi-Camera Setups](https://arxiv.org/abs/2603.05507v1)**  
  Authors: Leif Van Holland, Domenic Zingsheim, Mana Takhsha, Hannah Dröge, Patrick Stotko, Markus Plack, Reinhard Klein  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05507v1.pdf)  
  Keywords: architecture, novel view, streaming, dit  
- **[Orthogonal Spatial-temporal Distributional Transfer for 4D Generation](https://arxiv.org/abs/2603.05081v1)**  
  Authors: Wei Liu, Shengqiong Wu, Bobo Li, Haoyu Zhao, Hao Fei, Mong-Li Lee, Wynne Hsu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05081v1.pdf)  
  Keywords: diffusion model, temporal consistency, 4d generation, video diffusion  
- **[ShareVerse: Multi-Agent Consistent Video Generation for Shared World Modeling](https://arxiv.org/abs/2603.02697v1)**  
  Authors: Jiayi Zhu, Jianing Zhang, Yiying Yang, Wei Cheng, Xiaoyun Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02697v1.pdf)  
  Keywords: world model, simulation, video generation, multi-view video, dit, interactive  
- **[HumanOrbit: 3D Human Reconstruction as 360° Orbit Generation](https://arxiv.org/abs/2602.24148v1)**  
  Authors: Keito Suzuki, Kunyao Chen, Lei Wang, Bang Du, Runfa Blark Li, Peng Liu, Ning Bi, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.24148v1.pdf)  
  Keywords: identity, diffusion model, novel view, video diffusion  
- **[BetterScene: 3D Scene Synthesis with Representation-Aligned Generative Model](https://arxiv.org/abs/2602.22596v1)**  
  Authors: Yuci Han, Charles Toth, John E. Anderson, William J. Shuart, Alper Yilmaz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.22596v1.pdf)  
  Keywords: diffusion model, novel view, video diffusion, dit  
- **[Geometry-as-context: Modulating Explicit 3D in Scene-consistent Video Generation to Geometry Context](https://arxiv.org/abs/2602.21929v1)**  
  Authors: JiaKui Hu, Jialun Liu, Liying Yang, Xinliang Zhang, Kaiwen Li, Shuang Zeng, Yuanwei Li, Haibin Huang, Chi Zhang, Yanye Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21929v1.pdf)  
  Keywords: novel view, camera control, trajectory, video generation, autoregressive  
- **[RAYNOVA: Scale-Temporal Autoregressive World Modeling in Ray Space](https://arxiv.org/abs/2602.20685v2)**  
  Authors: Yichen Xie, Chensheng Peng, Mazen Abdelfattah, Yihan Hu, Jiezhi Yang, Eric Higgins, Ryan Brigden, Masayoshi Tomizuka, Wei Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20685v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://raynova-ai.github.io)  
  Keywords: novel view, world model, video generation, autoregressive, multi-view video, physical, dit  
- **[A Single Image and Multimodality Is All You Need for Novel View Synthesis](https://arxiv.org/abs/2602.17909v1)**  
  Authors: Amirhosein Javadi, Chi-Shiang Gau, Konstantinos D. Polyzos, Tara Javidi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.17909v1.pdf)  
  Keywords: video generation, novel view, dit, efficient  
- **[VideoNeuMat: Neural Material Extraction from Generative Video Models](https://arxiv.org/abs/2602.07272v1)**  
  Authors: Bowen Xue, Saeed Hadadan, Zheng Zeng, Fabrice Rousselle, Zahra Montazeri, Milos Hasan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.07272v1.pdf)  
  Keywords: diffusion model, novel view, video diffusion, dit  

### Applications

- **[Motion Forcing: A Decoupled Framework for Robust Video Generation in Motion Dynamics](https://arxiv.org/abs/2603.10408v1)**  
  Authors: Tianshuo Xu, Zhifei Chen, Leyi Wu, Hao Lu, Ying-cong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.10408v1.pdf)  
  Keywords: autonomous driving, dynamics, robotics, evaluation, video generation, benchmark, physics, physical  
- **[EduVQA: Benchmarking AI-Generated Video Quality Assessment for Education](https://arxiv.org/abs/2603.03066v1)**  
  Authors: Baoliang Chen, Xinlong Bu, Lingyu Zhu, Hanwei Zhu, Xiangjie Sui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.03066v1.pdf)  
  Keywords: t2v, evaluation, education, benchmark, concept, text-to-video  
- **[MicroVerse: A Preliminary Exploration Toward a Micro-World Simulation](https://arxiv.org/abs/2603.00585v1)**  
  Authors: Rongsheng Wang, Minghao Wu, Hongru Zhou, Zhihan Yu, Zhenyang Cai, Junying Chen, Benyou Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.00585v1.pdf) | [![GitHub](https://img.shields.io/github/stars/FreedomIntelligence/MicroVerse?style=social)](https://github.com/FreedomIntelligence/MicroVerse)  
  Keywords: dynamics, evaluation, education, simulation, video generation, benchmark, medical, concept, physical, interactive  
- **[HorizonForge: Driving Scene Editing with Any Trajectories and Any Vehicles](https://arxiv.org/abs/2602.21333v2)**  
  Authors: Yifan Wang, Francesco Pittaluga, Zaid Tasneem, Chenyu You, Manmohan Chandraker, Ziyu Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21333v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://horizonforge.github.io)  
  Keywords: temporal consistency, autonomous driving, dit, trajectory, evaluation, video diffusion, simulation, benchmark, controllable  
- **[GA-Drive: Geometry-Appearance Decoupled Modeling for Free-viewpoint Driving Scene Generatio](https://arxiv.org/abs/2602.20673v1)**  
  Authors: Hao Zhang, Lue Fan, Qitai Wang, Wenbo Li, Zehuan Wu, Lewei Lu, Zhaoxiang Zhang, Hongsheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20673v1.pdf)  
  Keywords: autonomous driving, diffusion model, dit, trajectory, video diffusion, simulation, video-to-video, video editing  
- **[3DSPA: A 3D Semantic Point Autoencoder for Evaluating Video Realism](https://arxiv.org/abs/2602.20354v1)**  
  Authors: Bhavik Chandna, Kelsey R. Allen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20354v1.pdf) | [![GitHub](https://img.shields.io/github/stars/TheProParadox/3dspa_code?style=social)](https://github.com/TheProParadox/3dspa_code)  
  Keywords: temporal consistency, robotics, trajectory, evaluation, film, video generation, benchmark, physical  
- **[PedaCo-Gen: Scaffolding Pedagogical Agency in Human-AI Collaborative Video Authoring](https://arxiv.org/abs/2602.19623v1)**  
  Authors: Injun Baek, Yearim Kim, Nojun Kwak  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.19623v1.pdf)  
  Keywords: t2v, text-to-video, education, dit, interactive  
- **[VideoSketcher: Video Models Prior Enable Versatile Sequential Sketch Generation](https://arxiv.org/abs/2602.15819v1)**  
  Authors: Hui Ren, Yuval Alaluf, Omer Bar Tal, Alexander Schwing, Antonio Torralba, Yael Vinker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.15819v1.pdf)  
  Keywords: creative, diffusion model, dit, video diffusion, style, autoregressive, efficient, text-to-video, interactive  
- **[Beyond End-to-End Video Models: An LLM-Based Multi-Agent System for Educational Video Generation](https://arxiv.org/abs/2602.11790v1)**  
  Authors: Lingyong Yan, Jiulong Wu, Dong Xie, Weixian Shi, Deguo Xia, Jizhou Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.11790v1.pdf)  
  Keywords: video generation, education, dit  
- **[Ctrl&Shift: High-Quality Geometry-Aware Object Manipulation in Visual Generation](https://arxiv.org/abs/2602.11440v1)**  
  Authors: Penghui Ruan, Bojia Zi, Xianbiao Qi, Youze Huang, Rong Xiao, Pichao Wang, Jiannong Cao, Yuhui Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.11440v1.pdf)  
  Keywords: creative, film, controllable, identity, dit  

### Architecture & Efficiency

*Showing the latest 50 out of 362 papers*

- **[Fuel Gauge: Estimating Chain-of-Thought Length Ahead of Time in Large Multimodal Models](https://arxiv.org/abs/2603.10335v1)**  
  Authors: Yuedong Yang, Xiwen Wei, Mustafa Munir, Radu Marculescu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.10335v1.pdf)  
  Keywords: multi-modal, benchmark, efficient  
- **[ID-LoRA: Identity-Driven Audio-Video Personalization with In-Context LoRA](https://arxiv.org/abs/2603.10256v1)**  
  Authors: Aviad Dahan, Moran Yanuka, Noa Kraicer, Lior Wolf, Raja Giryes  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.10256v1.pdf)  
  Keywords: denoising, personalization, video diffusion, style, identity, efficient, physical, sound, dit  
- **[DISPLAY: Directable Human-Object Interaction Video Generation via Sparse Motion Guidance and Multi-Task Auxiliary](https://arxiv.org/abs/2603.09883v1)**  
  Authors: Jiazhi Guan, Quanwei Yang, Luying Huang, Junhao Liang, Borong Liang, Haocheng Feng, Wei He, Kaisiyuan Wang, Hang Zhou, Jingdong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09883v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://mumuwei.github.io/DISPLAY)  
  Keywords: video generation, dit, controllable, physical  
- **[ConfCtrl: Enabling Precise Camera Control in Video Diffusion via Confidence-Aware Interpolation](https://arxiv.org/abs/2603.09819v1)**  
  Authors: Liudi Yang, George Eskandar, Fengyi Shen, Mohammad Altillawi, Yang Bai, Chi Zhang, Ziyuan Liu, Abhinav Valada  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09819v1.pdf)  
  Keywords: novel view, diffusion model, camera control, video diffusion, dit, video interpolation  
- **[FetalAgents: A Multi-Agent System for Fetal Ultrasound Image and Video Analysis](https://arxiv.org/abs/2603.09733v1)**  
  Authors: Xiaotian Hu, Junwei Huang, Mingxuan Liu, Kasidit Anmahapong, Yifei Chen, Yitong Luo, Yiming Huang, Xuguang Bai, Zihan Li, Yi Liao, Haibo Qu, Qiyuan Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09733v1.pdf)  
  Keywords: sound, evaluation, dit  
- **[FrameDiT: Diffusion Transformer with Frame-Level Matrix Attention for Efficient Video Generation](https://arxiv.org/abs/2603.09721v1)**  
  Authors: Minh Khoa Le, Kien Do, Duc Thanh Nguyen, Truyen Tran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09721v1.pdf)  
  Keywords: diffusion model, dynamics, video diffusion, architecture, diffusion transformer, video generation, benchmark, efficient, dit  
- **[When to Lock Attention: Training-Free KV Control in Video Diffusion](https://arxiv.org/abs/2603.09657v1)**  
  Authors: Tianyi Zeng, Jincheng Gao, Tianyi Wang, Zijie Meng, Miao Zhang, Jun Yin, Haoyuan Sun, Junfeng Jiao, Christian Claudel, Junbo Tan, Xueqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09657v1.pdf)  
  Keywords: video editing, denoising, diffusion model, video diffusion, dit  
- **[Streaming Autoregressive Video Generation via Diagonal Distillation](https://arxiv.org/abs/2603.09488v2)**  
  Authors: Jinxiu Liu, Xuanming Liu, Kangfu Mei, Yandong Wen, Ming-Hsuan Yang, Weiyang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09488v2.pdf)  
  Keywords: denoising, streaming, diffusion model, distillation, video generation, autoregressive, efficient, video synthesis, dit  
- **[Prune Redundancy, Preserve Essence: Vision Token Compression in VLMs via Synergistic Importance-Diversity](https://arxiv.org/abs/2603.09480v2)**  
  Authors: Zhengyao Fang, Pengyuan Lyu, Chengquan Zhang, Guangming Lu, Jun Yu, Wenjie Pei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09480v2.pdf) | [![GitHub](https://img.shields.io/github/stars/ZhengyaoFang/PruneSID?style=social)](https://github.com/ZhengyaoFang/PruneSID)  
  Keywords: concept, dit  
- **[Training-free Motion Factorization for Compositional Video Generation](https://arxiv.org/abs/2603.09104v1)**  
  Authors: Zixuan Wang, Ziqin Zhou, Feng Chen, Duo Peng, Yixin Hu, Changsheng Li, Yinjie Lei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09104v1.pdf)  
  Keywords: diffusion model, architecture, video generation, benchmark, dit  

### Audio & Multi-modal

- **[Fuel Gauge: Estimating Chain-of-Thought Length Ahead of Time in Large Multimodal Models](https://arxiv.org/abs/2603.10335v1)**  
  Authors: Yuedong Yang, Xiwen Wei, Mustafa Munir, Radu Marculescu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.10335v1.pdf)  
  Keywords: multi-modal, benchmark, efficient  
- **[ID-LoRA: Identity-Driven Audio-Video Personalization with In-Context LoRA](https://arxiv.org/abs/2603.10256v1)**  
  Authors: Aviad Dahan, Moran Yanuka, Noa Kraicer, Lior Wolf, Raja Giryes  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.10256v1.pdf)  
  Keywords: denoising, personalization, video diffusion, style, identity, efficient, physical, sound, dit  
- **[FetalAgents: A Multi-Agent System for Fetal Ultrasound Image and Video Analysis](https://arxiv.org/abs/2603.09733v1)**  
  Authors: Xiaotian Hu, Junwei Huang, Mingxuan Liu, Kasidit Anmahapong, Yifei Chen, Yitong Luo, Yiming Huang, Xuguang Bai, Zihan Li, Yi Liao, Haibo Qu, Qiyuan Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09733v1.pdf)  
  Keywords: sound, evaluation, dit  
- **[MM-TS: Multi-Modal Temperature and Margin Schedules for Contrastive Learning with Long-Tail Data](https://arxiv.org/abs/2603.08202v1)**  
  Authors: Siarhei Sheludzko, Dhimitrios Duka, Bernt Schiele, Hilde Kuehne, Anna Kukleva  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08202v1.pdf)  
  Keywords: concept, multi-modal, dit  
- **[StreamWise: Serving Multi-Modal Generation in Real-Time at Scale](https://arxiv.org/abs/2603.05800v1)**  
  Authors: Haoran Qiu, Gohar Irfan Chaudhry, Chaojie Zhang, Íñigo Goiri, Esha Choukse, Rodrigo Fonseca, Ricardo Bianchini  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05800v1.pdf)  
  Keywords: multi-modal, video generation, streaming, efficient  
- **[UniTalking: A Unified Audio-Video Framework for Talking Portrait Generation](https://arxiv.org/abs/2603.01418v1)**  
  Authors: Hebeizi Li, Zihao Liang, Benyuan Sun, Zihao Yin, Xiao Sha, Chenliang Wang, Yi Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01418v1.pdf)  
  Keywords: multi-modal, style, architecture, video generation, efficient  
- **[FlowPortrait: Reinforcement Learning for Audio-Driven Portrait Video Generation](https://arxiv.org/abs/2603.00159v1)**  
  Authors: Weiting Tan, Andy T. Liu, Ming Tu, Xinghua Qu, Philipp Koehn, Lu Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.00159v1.pdf)  
  Keywords: temporal consistency, evaluation, audio-driven, video generation, autoregressive, audio-to-video  
- **[SkyReels-V4: Multi-modal Video-Audio Generation, Inpainting and Editing model](https://arxiv.org/abs/2602.21818v2)**  
  Authors: Guibin Chen, Dixuan Lin, Jiangping Yang, Youqiang Zhang, Zhengcong Fei, Debang Li, Sheng Chen, Chaofeng Ao, Nuo Pang, Yiming Wang, Yikun Dou, Zheng Chen, Mingyuan Fan, Tuanhui Li, Mingshan Chang, Hao Zhang, Xiaopeng Sun, Jingtao Xu, Yuqiang Xie, Jiahua Wang, Zhiheng Xu, Weiming Xiong, Yuzhe Jin, Baoxuan Gu, Binjie Mao, Yunjie Yu, Jujie He, Yuhao Feng, Shiwen Tu, Chaojie Wang, Rui Yan, Wei Shen, Jingchen Wu, Peng Zhao, Xuanyue Zhong, Zhuangzhuang Liu, Kaifei Wang, Fuxiang Zhang, Weikai Xu, Wenyan Liu, Binglu Zhang, Yu Shen, Tianhui Xiong, Bin Peng, Liang Zeng, Xuchen Song, Haoxiang Guo, Peiyu Wang, Max W. Y. Lam, Chien-Hung Liu, Yahui Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21818v2.pdf)  
  Keywords: dit, multi-modal, image to video, super-resolution, frame interpolation, style, architecture, diffusion transformer, video generation, sound, video editing  
- **[JavisDiT++: Unified Modeling and Optimization for Joint Audio-Video Generation](https://arxiv.org/abs/2602.19163v1)**  
  Authors: Kai Liu, Yanhao Zheng, Kai Wang, Shengqiong Wu, Rongjunchen Zhang, Jiebo Luo, Dimitrios Hatzinakos, Ziwei Liu, Hao Fei, Tat-Seng Chua  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.19163v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://JavisVerse.github.io/JavisDiT2-page)  
  Keywords: t2v, evaluation, video generation, sound, dit  
- **[EchoTorrent: Towards Swift, Sustained, and Streaming Multi-Modal Video Generation](https://arxiv.org/abs/2602.13669v2)**  
  Authors: Rang Meng, Yingjie Yin, Yuming Li, Chenguang Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.13669v2.pdf)  
  Keywords: temporal consistency, streaming, multi-modal, architecture, video generation, autoregressive, identity  

### Controllable Generation

*Showing the latest 50 out of 110 papers*

- **[DISPLAY: Directable Human-Object Interaction Video Generation via Sparse Motion Guidance and Multi-Task Auxiliary](https://arxiv.org/abs/2603.09883v1)**  
  Authors: Jiazhi Guan, Quanwei Yang, Luying Huang, Junhao Liang, Borong Liang, Haocheng Feng, Wei He, Kaisiyuan Wang, Hang Zhou, Jingdong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09883v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://mumuwei.github.io/DISPLAY)  
  Keywords: video generation, dit, controllable, physical  
- **[ConfCtrl: Enabling Precise Camera Control in Video Diffusion via Confidence-Aware Interpolation](https://arxiv.org/abs/2603.09819v1)**  
  Authors: Liudi Yang, George Eskandar, Fengyi Shen, Mohammad Altillawi, Yang Bai, Chi Zhang, Ziyuan Liu, Abhinav Valada  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09819v1.pdf)  
  Keywords: novel view, diffusion model, camera control, video diffusion, dit, video interpolation  
- **[HECTOR: Hybrid Editable Compositional Object References for Video Generation](https://arxiv.org/abs/2603.08850v1)**  
  Authors: Guofeng Zhang, Angtian Wang, Jacob Zhiyuan Fang, Liming Jiang, Haotian Yang, Alan Yuille, Chongyang Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08850v1.pdf)  
  Keywords: trajectory, motion control, video generation, physical, dit  
- **[SPIRAL: A Closed-Loop Framework for Self-Improving Action World Models via Reflective Planning Agents](https://arxiv.org/abs/2603.08403v2)**  
  Authors: Yu Yang, Yue Liao, Jianbiao Mei, Baisen Wang, Xuemeng Yang, Licheng Wen, Jiangning Zhang, Xiangtai Li, Hanlin Chen, Botian Shi, Yong Liu, Shuicheng Yan, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08403v2.pdf)  
  Keywords: temporal consistency, i2v, dit, world model, evaluation, video generation, benchmark, controllable  
- **[Controllable Complex Human Motion Video Generation via Text-to-Skeleton Cascades](https://arxiv.org/abs/2603.08028v1)**  
  Authors: Ashkan Taghipour, Morteza Ghahremani, Zinuo Li, Hamid Laga, Farid Boussaid, Mohammed Bennamoun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08028v1.pdf)  
  Keywords: temporal consistency, diffusion model, dit, video diffusion, motion control, video generation, autoregressive, benchmark, human motion, controllable  
- **[TDM-R1: Reinforcing Few-Step Diffusion Models with Non-Differentiable Reward](https://arxiv.org/abs/2603.07700v1)**  
  Authors: Yihong Luo, Tianyang Hu, Weijian Luo, Jing Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.07700v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Luo-Yihong/TDM-R1?style=social)](https://github.com/Luo-Yihong/TDM-R1)  
  Keywords: video generation, trajectory, diffusion model  
- **[Two Frames Matter: A Temporal Attack for Text-to-Video Model Jailbreaking](https://arxiv.org/abs/2603.07028v1)**  
  Authors: Moyang Chen, Zonghao Ying, Wenzhuo Xu, Quancheng Zou, Deyue Zhang, Dongdong Yang, Xiangzheng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.07028v1.pdf)  
  Keywords: t2v, text-to-video, evaluation, trajectory, dit  
- **[FaceCam: Portrait Video Camera Control via Scale-Aware Conditioning](https://arxiv.org/abs/2603.05506v1)**  
  Authors: Weijie Lyu, Ming-Hsuan Yang, Zhixin Shu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05506v1.pdf)  
  Keywords: identity, video generation, camera control, dit  
- **[RealWonder: Real-Time Physical Action-Conditioned Video Generation](https://arxiv.org/abs/2603.05449v1)**  
  Authors: Wei Liu, Ziyu Chen, Zizhang Li, Yue Wang, Hong-Xing Yu, Jiajun Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05449v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://liuwei283.github.io/RealWonder)  
  Keywords: action-conditioned, camera control, simulation, video generation, physical, physics, dit, interactive  
- **[Frequency-Aware Error-Bounded Caching for Accelerating Diffusion Transformers](https://arxiv.org/abs/2603.05315v1)**  
  Authors: Guandong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05315v1.pdf)  
  Keywords: denoising, dynamics, trajectory, architecture, diffusion transformer, video generation, dit  

### Human & Character Animation

- **[Controllable Complex Human Motion Video Generation via Text-to-Skeleton Cascades](https://arxiv.org/abs/2603.08028v1)**  
  Authors: Ashkan Taghipour, Morteza Ghahremani, Zinuo Li, Hamid Laga, Farid Boussaid, Mohammed Bennamoun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08028v1.pdf)  
  Keywords: temporal consistency, diffusion model, dit, video diffusion, motion control, video generation, autoregressive, benchmark, human motion, controllable  
- **[ArtHOI: Articulated Human-Object Interaction Synthesis by 4D Reconstruction from Video Priors](https://arxiv.org/abs/2603.04338v1)**  
  Authors: Zihao Huang, Tianqi Liu, Zhaoxi Chen, Shaocong Xu, Saining Zhang, Lixing Xiao, Zhiguo Cao, Wei Li, Hao Zhao, Ziwei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.04338v1.pdf)  
  Keywords: diffusion model, video diffusion, physical, human motion, dit  
- **[Direct Reward Fine-Tuning on Poses for Single Image to 3D Human in the Wild](https://arxiv.org/abs/2603.02619v1)**  
  Authors: Seunguk Do, Minwoo Huh, Joonghyuk Shin, Jaesik Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02619v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://seunguk-do.github.io/drpose)  
  Keywords: diffusion model, evaluation, benchmark, human motion, dit  
- **[LiftAvatar: Kinematic-Space Completion for Expression-Controlled 3D Gaussian Avatar Animation](https://arxiv.org/abs/2603.02129v1)**  
  Authors: Hualiang Wei, Shunran Jia, Jialun Liu, Wenhui Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02129v1.pdf)  
  Keywords: avatar, dit, distillation, video diffusion, diffusion transformer, efficient, controllable  
- **[Non-verbal Real-time Human-AI Interaction in Constrained Robotic Environments](https://arxiv.org/abs/2603.01804v1)**  
  Authors: Dragos Costea, Alina Marcu, Cristina Lazar, Marius Leordeanu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01804v1.pdf)  
  Keywords: architecture, body motion, text-to-video  
- **[GeoDiff4D: Geometry-Aware Diffusion for 4D Head Avatar Reconstruction](https://arxiv.org/abs/2602.24161v1)**  
  Authors: Chao Xu, Xiaochen Zhao, Xiang Deng, Jingxiang Sun, Zhuo Su, Donglin Di, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.24161v1.pdf)  
  Keywords: avatar, video generation, identity, diffusion model  
- **[Spatio-Temporal Garment Reconstruction Using Diffusion Mapping via Pattern Coordinates](https://arxiv.org/abs/2602.24043v1)**  
  Authors: Yingxuan You, Ren Li, Corentin Dumery, Cong Cao, Hao Li, Pascal Fua  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.24043v1.pdf)  
  Keywords: temporal consistency, avatar, diffusion model, virtual try-on, dit  
- **[BigMaQ: A Big Macaque Motion and Animation Dataset Bridging Image and 3D Pose Representations](https://arxiv.org/abs/2602.19874v1)**  
  Authors: Lucas Martini, Alexander Lappe, Anna Bognár, Rufin Vogels, Martin A. Giese  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.19874v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://martinivis.github.io/BigMaQ)  
  Keywords: avatar, benchmark, dynamics  
- **[Ani3DHuman: Photorealistic 3D Human Animation with Self-guided Stochastic Sampling](https://arxiv.org/abs/2602.19089v1)**  
  Authors: Qi Sun, Can Wang, Jiaxiang Shang, Yingchun Liu, Jing Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.19089v1.pdf) | [![GitHub](https://img.shields.io/github/stars/qiisun/ani3dhuman?style=social)](https://github.com/qiisun/ani3dhuman)  
  Keywords: diffusion model, dynamics, video diffusion, human animation, identity  
- **[HairWeaver: Few-Shot Photorealistic Hair Motion Synthesis with Sim-to-Real Guided Video Diffusion](https://arxiv.org/abs/2602.11117v1)**  
  Authors: Di Chang, Ji Hou, Aljaz Bozic, Assaf Neuberger, Felix Juefei-Xu, Olivier Maury, Gene Wei-Chin Lin, Tuur Stuyck, Doug Roble, Mohammad Soleymani, Stephane Grabli  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.11117v1.pdf)  
  Keywords: dynamics, evaluation, video diffusion, human motion, dit  

### Image-to-Video Generation

- **[SPIRAL: A Closed-Loop Framework for Self-Improving Action World Models via Reflective Planning Agents](https://arxiv.org/abs/2603.08403v2)**  
  Authors: Yu Yang, Yue Liao, Jianbiao Mei, Baisen Wang, Xuemeng Yang, Licheng Wen, Jiangning Zhang, Xiangtai Li, Hanlin Chen, Botian Shi, Yong Liu, Shuicheng Yan, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08403v2.pdf)  
  Keywords: temporal consistency, i2v, dit, world model, evaluation, video generation, benchmark, controllable  
- **[Pinterest Canvas: Large-Scale Image Generation at Pinterest](https://arxiv.org/abs/2603.06453v1)**  
  Authors: Yu Wang, Eric Tzeng, Raymond Shiau, Jie Yang, Dmitry Kislyuk, Charles Rosenberg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06453v1.pdf)  
  Keywords: diffusion model, image-to-video, video generation, outpainting, dit  
- **[Helios: Real Real-Time Long Video Generation Model](https://arxiv.org/abs/2603.04379v1)**  
  Authors: Shenghai Yuan, Yuanyang Yin, Zongjian Li, Xinwei Huang, Xiao Yang, Li Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.04379v1.pdf)  
  Keywords: diffusion model, t2v, long video, video generation, autoregressive, acceleration, i2v  
- **[FastLightGen: Fast and Light Video Generation with Fewer Steps and Parameters](https://arxiv.org/abs/2603.01685v2)**  
  Authors: Shitong Shao, Yufei Gu, Zeke Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01685v2.pdf)  
  Keywords: video generation, distillation, efficient, i2v  
- **[FREE-Edit: Using Editing-aware Injection in Rectified Flow Models for Zero-shot Image-Driven Video Editing](https://arxiv.org/abs/2603.01164v1)**  
  Authors: Maomao Li, Yunfei Liu, Yu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01164v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://free-edit.github.io/page)  
  Keywords: denoising, i2v, layout, image-to-video, dit, image-driven, rectified flow, video editing  
- **[Let Your Image Move with Your Motion! -- Implicit Multi-Object Multi-Motion Transfer](https://arxiv.org/abs/2603.01000v1)**  
  Authors: Yuze Li, Dong Gong, Xiao Cao, Junchao Yuan, Dongsheng Li, Lei Zhou, Yun Sing Koh, Cheng Yan, Xinyu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01000v1.pdf)  
  Keywords: i2v, image-to-video, video generation, efficient, controllable  
- **[SkyReels-V4: Multi-modal Video-Audio Generation, Inpainting and Editing model](https://arxiv.org/abs/2602.21818v2)**  
  Authors: Guibin Chen, Dixuan Lin, Jiangping Yang, Youqiang Zhang, Zhengcong Fei, Debang Li, Sheng Chen, Chaofeng Ao, Nuo Pang, Yiming Wang, Yikun Dou, Zheng Chen, Mingyuan Fan, Tuanhui Li, Mingshan Chang, Hao Zhang, Xiaopeng Sun, Jingtao Xu, Yuqiang Xie, Jiahua Wang, Zhiheng Xu, Weiming Xiong, Yuzhe Jin, Baoxuan Gu, Binjie Mao, Yunjie Yu, Jujie He, Yuhao Feng, Shiwen Tu, Chaojie Wang, Rui Yan, Wei Shen, Jingchen Wu, Peng Zhao, Xuanyue Zhong, Zhuangzhuang Liu, Kaifei Wang, Fuxiang Zhang, Weikai Xu, Wenyan Liu, Binglu Zhang, Yu Shen, Tianhui Xiong, Bin Peng, Liang Zeng, Xuchen Song, Haoxiang Guo, Peiyu Wang, Max W. Y. Lam, Chien-Hung Liu, Yahui Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21818v2.pdf)  
  Keywords: dit, multi-modal, image to video, super-resolution, frame interpolation, style, architecture, diffusion transformer, video generation, sound, video editing  
- **[MultiAnimate: Pose-Guided Image Animation Made Extensible](https://arxiv.org/abs/2602.21581v1)**  
  Authors: Yingcheng Hu, Haowen Gong, Chuanguang Yang, Zhulin An, Yongjun Xu, Songhua Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21581v1.pdf)  
  Keywords: pose-guided, diffusion transformer, video generation, identity, dit, image animation  
- **[Human Video Generation from a Single Image with 3D Pose and View Control](https://arxiv.org/abs/2602.21188v1)**  
  Authors: Tiantian Wang, Chun-Han Yao, Tao Hu, Mallikarjun Byrasandra Ramalinga Reddy, Ming-Hsuan Yang, Varun Jampani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21188v1.pdf)  
  Keywords: diffusion model, image-to-video, video diffusion, video generation, latent video, video synthesis  
- **[VII: Visual Instruction Injection for Jailbreaking Image-to-Video Generation Models](https://arxiv.org/abs/2602.20999v2)**  
  Authors: Bowen Zheng, Yongli Xiang, Ziming Hong, Zerong Lin, Chaojian Yu, Tongliang Liu, Xinge You  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20999v2.pdf)  
  Keywords: video generation, dit, i2v, image-to-video  

### Long Video Generation

*Showing the latest 50 out of 120 papers*

- **[Streaming Autoregressive Video Generation via Diagonal Distillation](https://arxiv.org/abs/2603.09488v2)**  
  Authors: Jinxiu Liu, Xuanming Liu, Kangfu Mei, Yandong Wen, Ming-Hsuan Yang, Weiyang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09488v2.pdf)  
  Keywords: denoising, streaming, diffusion model, distillation, video generation, autoregressive, efficient, video synthesis, dit  
- **[HiAR: Efficient Autoregressive Long Video Generation via Hierarchical Denoising](https://arxiv.org/abs/2603.08703v1)**  
  Authors: Kai Zou, Dian Zheng, Hongbo Liu, Tiankai Hang, Bin Liu, Nenghai Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08703v1.pdf)  
  Keywords: temporal consistency, denoising, diffusion model, long video, distillation, video generation, autoregressive, efficient, dit  
- **[CAST: Modeling Visual State Transitions for Consistent Video Retrieval](https://arxiv.org/abs/2603.08648v1)**  
  Authors: Yanqing Liu, Yingcheng Liu, Fanghong Dong, Budianto Budianto, Cihang Xie, Yan Jiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08648v1.pdf)  
  Keywords: long-form, video generation, benchmark, identity, dit  
- **[SPIRAL: A Closed-Loop Framework for Self-Improving Action World Models via Reflective Planning Agents](https://arxiv.org/abs/2603.08403v2)**  
  Authors: Yu Yang, Yue Liao, Jianbiao Mei, Baisen Wang, Xuemeng Yang, Licheng Wen, Jiangning Zhang, Xiangtai Li, Hanlin Chen, Botian Shi, Yong Liu, Shuicheng Yan, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08403v2.pdf)  
  Keywords: temporal consistency, i2v, dit, world model, evaluation, video generation, benchmark, controllable  
- **[Controllable Complex Human Motion Video Generation via Text-to-Skeleton Cascades](https://arxiv.org/abs/2603.08028v1)**  
  Authors: Ashkan Taghipour, Morteza Ghahremani, Zinuo Li, Hamid Laga, Farid Boussaid, Mohammed Bennamoun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08028v1.pdf)  
  Keywords: temporal consistency, diffusion model, dit, video diffusion, motion control, video generation, autoregressive, benchmark, human motion, controllable  
- **[Image Generation Models: A Technical History](https://arxiv.org/abs/2603.07455v1)**  
  Authors: Rouzbeh Shirvani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.07455v1.pdf)  
  Keywords: video generation, survey, autoregressive  
- **[FastSTAR: Spatiotemporal Token Pruning for Efficient Autoregressive Video Synthesis](https://arxiv.org/abs/2603.07192v1)**  
  Authors: Sungwoong Yune, Suheon Jeong, Joo-Young Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.07192v1.pdf)  
  Keywords: video generation, autoregressive, efficient, acceleration, video synthesis  
- **[StreamWise: Serving Multi-Modal Generation in Real-Time at Scale](https://arxiv.org/abs/2603.05800v1)**  
  Authors: Haoran Qiu, Gohar Irfan Chaudhry, Chaojie Zhang, Íñigo Goiri, Esha Choukse, Rodrigo Fonseca, Ricardo Bianchini  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05800v1.pdf)  
  Keywords: multi-modal, video generation, streaming, efficient  
- **[Transformer-Based Inpainting for Real-Time 3D Streaming in Sparse Multi-Camera Setups](https://arxiv.org/abs/2603.05507v1)**  
  Authors: Leif Van Holland, Domenic Zingsheim, Mana Takhsha, Hannah Dröge, Patrick Stotko, Markus Plack, Reinhard Klein  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05507v1.pdf)  
  Keywords: architecture, novel view, streaming, dit  
- **[Orthogonal Spatial-temporal Distributional Transfer for 4D Generation](https://arxiv.org/abs/2603.05081v1)**  
  Authors: Wei Liu, Shengqiong Wu, Bobo Li, Haoyu Zhao, Hao Fei, Mong-Li Lee, Wynne Hsu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05081v1.pdf)  
  Keywords: diffusion model, temporal consistency, 4d generation, video diffusion  

### Personalization & Customization

*Showing the latest 50 out of 93 papers*

- **[ID-LoRA: Identity-Driven Audio-Video Personalization with In-Context LoRA](https://arxiv.org/abs/2603.10256v1)**  
  Authors: Aviad Dahan, Moran Yanuka, Noa Kraicer, Lior Wolf, Raja Giryes  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.10256v1.pdf)  
  Keywords: denoising, personalization, video diffusion, style, identity, efficient, physical, sound, dit  
- **[Prune Redundancy, Preserve Essence: Vision Token Compression in VLMs via Synergistic Importance-Diversity](https://arxiv.org/abs/2603.09480v2)**  
  Authors: Zhengyao Fang, Pengyuan Lyu, Chengquan Zhang, Guangming Lu, Jun Yu, Wenjie Pei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09480v2.pdf) | [![GitHub](https://img.shields.io/github/stars/ZhengyaoFang/PruneSID?style=social)](https://github.com/ZhengyaoFang/PruneSID)  
  Keywords: concept, dit  
- **[Chain of Event-Centric Causal Thought for Physically Plausible Video Generation](https://arxiv.org/abs/2603.09094v1)**  
  Authors: Zixuan Wang, Yixin Hu, Haolan Wang, Feng Chen, Yan Liu, Wen Li, Yinjie Lei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09094v1.pdf)  
  Keywords: diffusion model, physics, video diffusion, video generation, benchmark, physical, concept, dit, interactive  
- **[CAST: Modeling Visual State Transitions for Consistent Video Retrieval](https://arxiv.org/abs/2603.08648v1)**  
  Authors: Yanqing Liu, Yingcheng Liu, Fanghong Dong, Budianto Budianto, Cihang Xie, Yan Jiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08648v1.pdf)  
  Keywords: long-form, video generation, benchmark, identity, dit  
- **[Video2LoRA: Unified Semantic-Controlled Video Generation via Per-Reference-Video LoRA](https://arxiv.org/abs/2603.08210v2)**  
  Authors: Zexi Wu, Qinghe Wang, Jing Dai, Baolu Li, Yiming Zhang, Yue Ma, Xu Jia, Hongming Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08210v2.pdf)  
  Keywords: video generation, dit, efficient, style  
- **[MM-TS: Multi-Modal Temperature and Margin Schedules for Contrastive Learning with Long-Tail Data](https://arxiv.org/abs/2603.08202v1)**  
  Authors: Siarhei Sheludzko, Dhimitrios Duka, Bernt Schiele, Hilde Kuehne, Anna Kukleva  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08202v1.pdf)  
  Keywords: concept, multi-modal, dit  
- **[GenHOI: Towards Object-Consistent Hand-Object Interaction with Temporally Balanced and Spatially Selective Object Injection](https://arxiv.org/abs/2603.06048v1)**  
  Authors: Xuan Huang, Mochu Xiang, Zhelun Shen, Jinbo Wu, Chenming Wu, Chen Zhao, Kaisiyuan Wang, Hang Zhou, Shanshan Liu, Haocheng Feng, Wei He, Jingdong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06048v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xuanhuang0.github.io/GenHOI)  
  Keywords: video editing, evaluation, video generation, physical, identity, video synthesis, dit  
- **[FaceCam: Portrait Video Camera Control via Scale-Aware Conditioning](https://arxiv.org/abs/2603.05506v1)**  
  Authors: Weijie Lyu, Ming-Hsuan Yang, Zhixin Shu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05506v1.pdf)  
  Keywords: identity, video generation, camera control, dit  
- **[InfinityStory: Unlimited Video Generation with World Consistency and Character-Aware Shot Transitions](https://arxiv.org/abs/2603.03646v1)**  
  Authors: Mohamed Elmoghany, Liangbing Zhao, Xiaoqian Shen, Subhojyoti Mukherjee, Yang Zhou, Gang Wu, Viet Dac Lai, Seunghyun Yoon, Ryan Rossi, Abdullah Rashwan, Puneet Mathur, Varun Manjunatha, Daksh Dangi, Chien Nguyen, Nedim Lipka, Trung Bui, Krishna Kumar Singh, Ruiyi Zhang, Xiaolei Huang, Jaemin Cho, Yu Wang, Namyong Park, Zhengzhong Tu, Hongjie Chen, Hoda Eldardiry, Nesreen Ahmed, Thien Nguyen, Dinesh Manocha, Mohamed Elhoseiny, Franck Dernoncourt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.03646v1.pdf)  
  Keywords: video synthesis, video generation, long-form, identity  
- **[EduVQA: Benchmarking AI-Generated Video Quality Assessment for Education](https://arxiv.org/abs/2603.03066v1)**  
  Authors: Baoliang Chen, Xinlong Bu, Lingyu Zhu, Hanwei Zhu, Xiangjie Sui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.03066v1.pdf)  
  Keywords: t2v, evaluation, education, benchmark, concept, text-to-video  

### Physical Understanding

*Showing the latest 50 out of 129 papers*

- **[World2Act: Latent Action Post-Training via Skill-Compositional World Models](https://arxiv.org/abs/2603.10422v1)**  
  Authors: An Dinh Vuong, Tuan Van Vo, Abdullah Sohail, Haoran Ding, Liang Ma, Xiaodan Liang, Anqing Duan, Ivan Laptev, Ian Reid  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.10422v1.pdf)  
  Keywords: world model, video generation, dynamics  
- **[Motion Forcing: A Decoupled Framework for Robust Video Generation in Motion Dynamics](https://arxiv.org/abs/2603.10408v1)**  
  Authors: Tianshuo Xu, Zhifei Chen, Leyi Wu, Hao Lu, Ying-cong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.10408v1.pdf)  
  Keywords: autonomous driving, dynamics, robotics, evaluation, video generation, benchmark, physics, physical  
- **[ID-LoRA: Identity-Driven Audio-Video Personalization with In-Context LoRA](https://arxiv.org/abs/2603.10256v1)**  
  Authors: Aviad Dahan, Moran Yanuka, Noa Kraicer, Lior Wolf, Raja Giryes  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.10256v1.pdf)  
  Keywords: denoising, personalization, video diffusion, style, identity, efficient, physical, sound, dit  
- **[DISPLAY: Directable Human-Object Interaction Video Generation via Sparse Motion Guidance and Multi-Task Auxiliary](https://arxiv.org/abs/2603.09883v1)**  
  Authors: Jiazhi Guan, Quanwei Yang, Luying Huang, Junhao Liang, Borong Liang, Haocheng Feng, Wei He, Kaisiyuan Wang, Hang Zhou, Jingdong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09883v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://mumuwei.github.io/DISPLAY)  
  Keywords: video generation, dit, controllable, physical  
- **[FrameDiT: Diffusion Transformer with Frame-Level Matrix Attention for Efficient Video Generation](https://arxiv.org/abs/2603.09721v1)**  
  Authors: Minh Khoa Le, Kien Do, Duc Thanh Nguyen, Truyen Tran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09721v1.pdf)  
  Keywords: diffusion model, dynamics, video diffusion, architecture, diffusion transformer, video generation, benchmark, efficient, dit  
- **[Chain of Event-Centric Causal Thought for Physically Plausible Video Generation](https://arxiv.org/abs/2603.09094v1)**  
  Authors: Zixuan Wang, Yixin Hu, Haolan Wang, Feng Chen, Yan Liu, Wen Li, Yinjie Lei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09094v1.pdf)  
  Keywords: diffusion model, physics, video diffusion, video generation, benchmark, physical, concept, dit, interactive  
- **[HECTOR: Hybrid Editable Compositional Object References for Video Generation](https://arxiv.org/abs/2603.08850v1)**  
  Authors: Guofeng Zhang, Angtian Wang, Jacob Zhiyuan Fang, Liming Jiang, Haotian Yang, Alan Yuille, Chongyang Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08850v1.pdf)  
  Keywords: trajectory, motion control, video generation, physical, dit  
- **[NEGATE: Constrained Semantic Guidance for Linguistic Negation in Text-to-Video Diffusion](https://arxiv.org/abs/2603.06533v1)**  
  Authors: Taewon Kang, Ming C. Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06533v1.pdf)  
  Keywords: dynamics, text-to-video, evaluation, video diffusion, benchmark, dit  
- **[Physical Simulator In-the-Loop Video Generation](https://arxiv.org/abs/2603.06408v1)**  
  Authors: Lin Geng Foo, Mark He Huang, Alexandros Lattas, Stylianos Moschoglou, Thabo Beeler, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06408v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vcai.mpi-inf.mpg.de/projects/PSIVG)  
  Keywords: diffusion model, dynamics, video diffusion, video generation, physics, physical  
- **[Place-it-R1: Unlocking Environment-aware Reasoning Potential of MLLM for Video Object Insertion](https://arxiv.org/abs/2603.06140v1)**  
  Authors: Bohai Gu, Taiyi Wu, Dazhao Du, Jian Liu, Shuai Yang, Xiaotong Zhao, Alan Zhao, Song Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06140v1.pdf)  
  Keywords: video editing, diffusion model, video diffusion, physical, dit  

### Surveys & Benchmarks

*Showing the latest 50 out of 197 papers*

- **[COMIC: Agentic Sketch Comedy Generation](https://arxiv.org/abs/2603.11048v1)**  
  Authors: Susung Hong, Brian Curless, Ira Kemelmacher-Shlizerman, Steve Seitz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.11048v1.pdf)  
  Keywords: video generation, evaluation  
- **[Motion Forcing: A Decoupled Framework for Robust Video Generation in Motion Dynamics](https://arxiv.org/abs/2603.10408v1)**  
  Authors: Tianshuo Xu, Zhifei Chen, Leyi Wu, Hao Lu, Ying-cong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.10408v1.pdf)  
  Keywords: autonomous driving, dynamics, robotics, evaluation, video generation, benchmark, physics, physical  
- **[Fuel Gauge: Estimating Chain-of-Thought Length Ahead of Time in Large Multimodal Models](https://arxiv.org/abs/2603.10335v1)**  
  Authors: Yuedong Yang, Xiwen Wei, Mustafa Munir, Radu Marculescu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.10335v1.pdf)  
  Keywords: multi-modal, benchmark, efficient  
- **[FetalAgents: A Multi-Agent System for Fetal Ultrasound Image and Video Analysis](https://arxiv.org/abs/2603.09733v1)**  
  Authors: Xiaotian Hu, Junwei Huang, Mingxuan Liu, Kasidit Anmahapong, Yifei Chen, Yitong Luo, Yiming Huang, Xuguang Bai, Zihan Li, Yi Liao, Haibo Qu, Qiyuan Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09733v1.pdf)  
  Keywords: sound, evaluation, dit  
- **[FrameDiT: Diffusion Transformer with Frame-Level Matrix Attention for Efficient Video Generation](https://arxiv.org/abs/2603.09721v1)**  
  Authors: Minh Khoa Le, Kien Do, Duc Thanh Nguyen, Truyen Tran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09721v1.pdf)  
  Keywords: diffusion model, dynamics, video diffusion, architecture, diffusion transformer, video generation, benchmark, efficient, dit  
- **[Training-free Motion Factorization for Compositional Video Generation](https://arxiv.org/abs/2603.09104v1)**  
  Authors: Zixuan Wang, Ziqin Zhou, Feng Chen, Duo Peng, Yixin Hu, Changsheng Li, Yinjie Lei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09104v1.pdf)  
  Keywords: diffusion model, architecture, video generation, benchmark, dit  
- **[Chain of Event-Centric Causal Thought for Physically Plausible Video Generation](https://arxiv.org/abs/2603.09094v1)**  
  Authors: Zixuan Wang, Yixin Hu, Haolan Wang, Feng Chen, Yan Liu, Wen Li, Yinjie Lei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09094v1.pdf)  
  Keywords: diffusion model, physics, video diffusion, video generation, benchmark, physical, concept, dit, interactive  
- **[CAST: Modeling Visual State Transitions for Consistent Video Retrieval](https://arxiv.org/abs/2603.08648v1)**  
  Authors: Yanqing Liu, Yingcheng Liu, Fanghong Dong, Budianto Budianto, Cihang Xie, Yan Jiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08648v1.pdf)  
  Keywords: long-form, video generation, benchmark, identity, dit  
- **[SWIFT: Sliding Window Reconstruction for Few-Shot Training-Free Generated Video Attribution](https://arxiv.org/abs/2603.08536v1)**  
  Authors: Chao Wang, Zijin Yang, Yaofei Wang, Yuang Qi, Weiming Zhang, Nenghai Yu, Kejiang Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08536v1.pdf) | [![GitHub](https://img.shields.io/github/stars/wangchao0708/SWIFT?style=social)](https://github.com/wangchao0708/SWIFT)  
  Keywords: video generation, evaluation, dit  
- **[SPIRAL: A Closed-Loop Framework for Self-Improving Action World Models via Reflective Planning Agents](https://arxiv.org/abs/2603.08403v2)**  
  Authors: Yu Yang, Yue Liao, Jianbiao Mei, Baisen Wang, Xuemeng Yang, Licheng Wen, Jiangning Zhang, Xiangtai Li, Hanlin Chen, Botian Shi, Yong Liu, Shuicheng Yan, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08403v2.pdf)  
  Keywords: temporal consistency, i2v, dit, world model, evaluation, video generation, benchmark, controllable  

### Text-to-Video Generation

*Showing the latest 50 out of 72 papers*

- **[VIVECaption: A Split Approach to Caption Quality Improvement](https://arxiv.org/abs/2603.07401v1)**  
  Authors: Varun Ananth, Baqiao Liu, Haoran Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.07401v1.pdf)  
  Keywords: t2v, evaluation, text-to-video  
- **[Two Frames Matter: A Temporal Attack for Text-to-Video Model Jailbreaking](https://arxiv.org/abs/2603.07028v1)**  
  Authors: Moyang Chen, Zonghao Ying, Wenzhuo Xu, Quancheng Zou, Deyue Zhang, Dongdong Yang, Xiangzheng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.07028v1.pdf)  
  Keywords: t2v, text-to-video, evaluation, trajectory, dit  
- **[NEGATE: Constrained Semantic Guidance for Linguistic Negation in Text-to-Video Diffusion](https://arxiv.org/abs/2603.06533v1)**  
  Authors: Taewon Kang, Ming C. Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06533v1.pdf)  
  Keywords: dynamics, text-to-video, evaluation, video diffusion, benchmark, dit  
- **[Accelerating Text-to-Video Generation with Calibrated Sparse Attention](https://arxiv.org/abs/2603.05503v1)**  
  Authors: Shai Yehezkel, Shahar Yadin, Noam Elata, Yaron Ostrovsky-Berman, Bahjat Kawar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05503v1.pdf)  
  Keywords: video generation, efficient, diffusion model, text-to-video  
- **[Helios: Real Real-Time Long Video Generation Model](https://arxiv.org/abs/2603.04379v1)**  
  Authors: Shenghai Yuan, Yuanyang Yin, Zongjian Li, Xinwei Huang, Xiao Yang, Li Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.04379v1.pdf)  
  Keywords: diffusion model, t2v, long video, video generation, autoregressive, acceleration, i2v  
- **[PhyPrompt: RL-based Prompt Refinement for Physically Plausible Text-to-Video Generation](https://arxiv.org/abs/2603.03505v1)**  
  Authors: Shang Wu, Chenwei Xu, Zhuofan Xia, Weijian Li, Lie Lu, Pranav Maneriker, Fan Du, Manling Li, Han Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.03505v1.pdf)  
  Keywords: t2v, architecture, video generation, physics-aware, physical, physics, text-to-video  
- **[EduVQA: Benchmarking AI-Generated Video Quality Assessment for Education](https://arxiv.org/abs/2603.03066v1)**  
  Authors: Baoliang Chen, Xinlong Bu, Lingyu Zhu, Hanwei Zhu, Xiangjie Sui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.03066v1.pdf)  
  Keywords: t2v, evaluation, education, benchmark, concept, text-to-video  
- **[BrandFusion: A Multi-Agent Framework for Seamless Brand Integration in Text-to-Video Generation](https://arxiv.org/abs/2603.02816v2)**  
  Authors: Zihao Zhu, Ruotong Wang, Siwei Lyu, Min Zhang, Baoyuan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02816v2.pdf)  
  Keywords: t2v, video generation, evaluation, text-to-video  
- **[Does Semantic Noise Initialization Transfer from Images to Videos? A Paired Diagnostic Study](https://arxiv.org/abs/2603.06672v1)**  
  Authors: Yixiao Jing, Chaoyu Zhang, Zixuan Zhong, Peizhou Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06672v1.pdf)  
  Keywords: diffusion model, t2v, evaluation, style, benchmark, text-to-video  
- **[Non-verbal Real-time Human-AI Interaction in Constrained Robotic Environments](https://arxiv.org/abs/2603.01804v1)**  
  Authors: Dragos Costea, Alina Marcu, Cristina Lazar, Marius Leordeanu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01804v1.pdf)  
  Keywords: architecture, body motion, text-to-video  

### Video Editing

- **[When to Lock Attention: Training-Free KV Control in Video Diffusion](https://arxiv.org/abs/2603.09657v1)**  
  Authors: Tianyi Zeng, Jincheng Gao, Tianyi Wang, Zijie Meng, Miao Zhang, Jun Yin, Haoyuan Sun, Junfeng Jiao, Christian Claudel, Junbo Tan, Xueqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09657v1.pdf)  
  Keywords: video editing, denoising, diffusion model, video diffusion, dit  
- **[Place-it-R1: Unlocking Environment-aware Reasoning Potential of MLLM for Video Object Insertion](https://arxiv.org/abs/2603.06140v1)**  
  Authors: Bohai Gu, Taiyi Wu, Dazhao Du, Jian Liu, Shuai Yang, Xiaotong Zhao, Alan Zhao, Song Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06140v1.pdf)  
  Keywords: video editing, diffusion model, video diffusion, physical, dit  
- **[GenHOI: Towards Object-Consistent Hand-Object Interaction with Temporally Balanced and Spatially Selective Object Injection](https://arxiv.org/abs/2603.06048v1)**  
  Authors: Xuan Huang, Mochu Xiang, Zhelun Shen, Jinbo Wu, Chenming Wu, Chen Zhao, Kaisiyuan Wang, Hang Zhou, Shanshan Liu, Haocheng Feng, Wei He, Jingdong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06048v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xuanhuang0.github.io/GenHOI)  
  Keywords: video editing, evaluation, video generation, physical, identity, video synthesis, dit  
- **[Training-free Latent Inter-Frame Pruning with Attention Recovery](https://arxiv.org/abs/2603.05811v1)**  
  Authors: Dennis Menn, Yuedong Yang, Bokun Wang, Xiwen Wei, Mustafa Munir, Feng Liang, Radu Marculescu, Chenfeng Xu, Diana Marculescu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05811v1.pdf)  
  Keywords: video generation, dit, video editing  
- **[FREE-Edit: Using Editing-aware Injection in Rectified Flow Models for Zero-shot Image-Driven Video Editing](https://arxiv.org/abs/2603.01164v1)**  
  Authors: Maomao Li, Yunfei Liu, Yu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01164v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://free-edit.github.io/page)  
  Keywords: denoising, i2v, layout, image-to-video, dit, image-driven, rectified flow, video editing  
- **[UniVBench: Towards Unified Evaluation for Video Foundation Models](https://arxiv.org/abs/2602.21835v2)**  
  Authors: Jianhui Wei, Xiaotian Zhang, Yichen Li, Yuan Wang, Yan Zhang, Ziyi Chen, Zhihang Tang, Wei Xu, Zuozhu Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21835v2.pdf)  
  Keywords: video editing, evaluation, video generation, benchmark, dit  
- **[SkyReels-V4: Multi-modal Video-Audio Generation, Inpainting and Editing model](https://arxiv.org/abs/2602.21818v2)**  
  Authors: Guibin Chen, Dixuan Lin, Jiangping Yang, Youqiang Zhang, Zhengcong Fei, Debang Li, Sheng Chen, Chaofeng Ao, Nuo Pang, Yiming Wang, Yikun Dou, Zheng Chen, Mingyuan Fan, Tuanhui Li, Mingshan Chang, Hao Zhang, Xiaopeng Sun, Jingtao Xu, Yuqiang Xie, Jiahua Wang, Zhiheng Xu, Weiming Xiong, Yuzhe Jin, Baoxuan Gu, Binjie Mao, Yunjie Yu, Jujie He, Yuhao Feng, Shiwen Tu, Chaojie Wang, Rui Yan, Wei Shen, Jingchen Wu, Peng Zhao, Xuanyue Zhong, Zhuangzhuang Liu, Kaifei Wang, Fuxiang Zhang, Weikai Xu, Wenyan Liu, Binglu Zhang, Yu Shen, Tianhui Xiong, Bin Peng, Liang Zeng, Xuchen Song, Haoxiang Guo, Peiyu Wang, Max W. Y. Lam, Chien-Hung Liu, Yahui Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21818v2.pdf)  
  Keywords: dit, multi-modal, image to video, super-resolution, frame interpolation, style, architecture, diffusion transformer, video generation, sound, video editing  
- **[GA-Drive: Geometry-Appearance Decoupled Modeling for Free-viewpoint Driving Scene Generatio](https://arxiv.org/abs/2602.20673v1)**  
  Authors: Hao Zhang, Lue Fan, Qitai Wang, Wenbo Li, Zehuan Wu, Lewei Lu, Zhaoxiang Zhang, Hongsheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20673v1.pdf)  
  Keywords: autonomous driving, diffusion model, dit, trajectory, video diffusion, simulation, video-to-video, video editing  
- **[PropFly: Learning to Propagate via On-the-Fly Supervision from Pre-trained Video Diffusion Models](https://arxiv.org/abs/2602.20583v1)**  
  Authors: Wonyong Seo, Jaeho Moon, Jaehyup Lee, Soo Ye Kim, Munchurl Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20583v1.pdf)  
  Keywords: video editing, diffusion model, flow matching, video diffusion, dit  
- **[RoboCurate: Harnessing Diversity with Action-Verified Neural Trajectory for Robot Learning](https://arxiv.org/abs/2602.18742v1)**  
  Authors: Seungku Kim, Suhyeok Jang, Byungjun Yoon, Dongyoung Kim, John Won, Jinwoo Shin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.18742v1.pdf)  
  Keywords: trajectory, simulation, physical, video-to-video, dit  

### Video Inpainting & Completion

- **[ConfCtrl: Enabling Precise Camera Control in Video Diffusion via Confidence-Aware Interpolation](https://arxiv.org/abs/2603.09819v1)**  
  Authors: Liudi Yang, George Eskandar, Fengyi Shen, Mohammad Altillawi, Yang Bai, Chi Zhang, Ziyuan Liu, Abhinav Valada  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09819v1.pdf)  
  Keywords: novel view, diffusion model, camera control, video diffusion, dit, video interpolation  
- **[Pinterest Canvas: Large-Scale Image Generation at Pinterest](https://arxiv.org/abs/2603.06453v1)**  
  Authors: Yu Wang, Eric Tzeng, Raymond Shiau, Jie Yang, Dmitry Kislyuk, Charles Rosenberg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06453v1.pdf)  
  Keywords: diffusion model, image-to-video, video generation, outpainting, dit  
- **[Learning Physics-Grounded 4D Dynamics with Neural Gaussian Force Fields](https://arxiv.org/abs/2602.00148v2)**  
  Authors: Shiqian Li, Ruihong Shen, Junfeng Ni, Chang Pan, Chi Zhang, Yixin Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.00148v2.pdf)  
  Keywords: dynamics, world model, evaluation, simulation, video generation, physics, video prediction, physical, interactive  
- **[DriveLaW:Unifying Planning and Video Generation in a Latent Driving World](https://arxiv.org/abs/2512.23421v2)**  
  Authors: Tianze Xia, Yongkang Li, Lijun Zhou, Jingfeng Yao, Kaixin Xiong, Haiyang Sun, Bing Wang, Kun Ma, Guang Chen, Hangjun Ye, Wenyu Liu, Xinggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.23421v2.pdf)  
  Keywords: autonomous driving, world model, trajectory, architecture, video generation, benchmark, video prediction  
- **[Autoregressive Flow Matching for Motion Prediction](https://arxiv.org/abs/2512.22688v1)**  
  Authors: Johnathan Xie, Stefan Stojanov, Cristobal Eyzaguirre, Daniel L. K. Yamins, Jiajun Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.22688v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Johnathan-Xie/arfm-motion-prediction?style=social)](https://github.com/Johnathan-Xie/arfm-motion-prediction)  
  Keywords: robotics, flow matching, video generation, autoregressive, benchmark, human motion, video prediction, dit  
- **[Over++: Generative Video Compositing for Layer Interaction Effects](https://arxiv.org/abs/2512.19661v1)**  
  Authors: Luchao Qi, Jiaye Wu, Jun Myeong Choi, Cary Phillips, Roni Sengupta, Dan B Goldman  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.19661v1.pdf)  
  Keywords: video inpainting, dit  
- **[Vidarc: Embodied Video Diffusion Model for Closed-loop Control](https://arxiv.org/abs/2512.17661v1)**  
  Authors: Yao Feng, Chendong Xiang, Xinyi Mao, Hengkai Tan, Zuyue Zhang, Shuhe Huang, Kaiwen Zheng, Haitian Liu, Hang Su, Jun Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.17661v1.pdf)  
  Keywords: diffusion model, dynamics, video diffusion, autoregressive, video prediction, physical  

### Video Super-Resolution & Enhancement

*Showing the latest 50 out of 58 papers*

- **[ID-LoRA: Identity-Driven Audio-Video Personalization with In-Context LoRA](https://arxiv.org/abs/2603.10256v1)**  
  Authors: Aviad Dahan, Moran Yanuka, Noa Kraicer, Lior Wolf, Raja Giryes  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.10256v1.pdf)  
  Keywords: denoising, personalization, video diffusion, style, identity, efficient, physical, sound, dit  
- **[When to Lock Attention: Training-Free KV Control in Video Diffusion](https://arxiv.org/abs/2603.09657v1)**  
  Authors: Tianyi Zeng, Jincheng Gao, Tianyi Wang, Zijie Meng, Miao Zhang, Jun Yin, Haoyuan Sun, Junfeng Jiao, Christian Claudel, Junbo Tan, Xueqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09657v1.pdf)  
  Keywords: video editing, denoising, diffusion model, video diffusion, dit  
- **[Streaming Autoregressive Video Generation via Diagonal Distillation](https://arxiv.org/abs/2603.09488v2)**  
  Authors: Jinxiu Liu, Xuanming Liu, Kangfu Mei, Yandong Wen, Ming-Hsuan Yang, Weiyang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09488v2.pdf)  
  Keywords: denoising, streaming, diffusion model, distillation, video generation, autoregressive, efficient, video synthesis, dit  
- **[HiAR: Efficient Autoregressive Long Video Generation via Hierarchical Denoising](https://arxiv.org/abs/2603.08703v1)**  
  Authors: Kai Zou, Dian Zheng, Hongbo Liu, Tiankai Hang, Bin Liu, Nenghai Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08703v1.pdf)  
  Keywords: temporal consistency, denoising, diffusion model, long video, distillation, video generation, autoregressive, efficient, dit  
- **[Cross-Resolution Distribution Matching for Diffusion Distillation](https://arxiv.org/abs/2603.06136v1)**  
  Authors: Feiyang Chen, Hongpeng Pan, Haonan Xu, Xinyu Duan, Yang Yang, Zhefeng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06136v1.pdf)  
  Keywords: video generation, distillation, denoising, dit  
- **[Frequency-Aware Error-Bounded Caching for Accelerating Diffusion Transformers](https://arxiv.org/abs/2603.05315v1)**  
  Authors: Guandong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05315v1.pdf)  
  Keywords: denoising, dynamics, trajectory, architecture, diffusion transformer, video generation, dit  
- **[FC-VFI: Faithful and Consistent Video Frame Interpolation for High-FPS Slow Motion Video Generation](https://arxiv.org/abs/2603.04899v1)**  
  Authors: Ganggui Ding, Hao Chen, Xiaogang Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.04899v1.pdf)  
  Keywords: temporal consistency, diffusion model, frame interpolation, video diffusion, motion control, video generation  
- **[CubeComposer: Spatio-Temporal Autoregressive 4K 360° Video Generation from Perspective Video](https://arxiv.org/abs/2603.04291v1)**  
  Authors: Lingen Li, Guangzhi Wang, Xiaoyu Li, Zhaoyang Zhang, Qi Dou, Jinwei Gu, Tianfan Xue, Ying Shan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.04291v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lg-li.github.io/project/cubecomposer)  
  Keywords: diffusion model, super-resolution, video generation, autoregressive, benchmark  
- **[TC-Padé: Trajectory-Consistent Padé Approximation for Diffusion Acceleration](https://arxiv.org/abs/2603.02943v1)**  
  Authors: Benlei Cui, Shaoxuan He, Bukun Huang, Zhizeng Ye, Yunyun Sun, Longtao Huang, Hui Xue, Yang Yang, Jingqun Tang, Zhou Zhao, Haiwen Hong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02943v1.pdf)  
  Keywords: denoising, diffusion model, dynamics, trajectory, video generation, efficient, acceleration, dit  
- **[Retrieval, Refinement, and Ranking for Text-to-Video Generation via Prompt Optimization and Test-Time Scaling](https://arxiv.org/abs/2603.01509v1)**  
  Authors: Zillur Rahman, Alex Sheng, Cristian Meo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01509v1.pdf)  
  Keywords: diffusion model, t2v, dit, frame interpolation, video generation, efficient, text-to-video  

### World Models & Simulation

*Showing the latest 50 out of 93 papers*

- **[World2Act: Latent Action Post-Training via Skill-Compositional World Models](https://arxiv.org/abs/2603.10422v1)**  
  Authors: An Dinh Vuong, Tuan Van Vo, Abdullah Sohail, Haoran Ding, Liang Ma, Xiaodan Liang, Anqing Duan, Ivan Laptev, Ian Reid  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.10422v1.pdf)  
  Keywords: world model, video generation, dynamics  
- **[Chain of Event-Centric Causal Thought for Physically Plausible Video Generation](https://arxiv.org/abs/2603.09094v1)**  
  Authors: Zixuan Wang, Yixin Hu, Haolan Wang, Feng Chen, Yan Liu, Wen Li, Yinjie Lei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09094v1.pdf)  
  Keywords: diffusion model, physics, video diffusion, video generation, benchmark, physical, concept, dit, interactive  
- **[SPIRAL: A Closed-Loop Framework for Self-Improving Action World Models via Reflective Planning Agents](https://arxiv.org/abs/2603.08403v2)**  
  Authors: Yu Yang, Yue Liao, Jianbiao Mei, Baisen Wang, Xuemeng Yang, Licheng Wen, Jiangning Zhang, Xiangtai Li, Hanlin Chen, Botian Shi, Yong Liu, Shuicheng Yan, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08403v2.pdf)  
  Keywords: temporal consistency, i2v, dit, world model, evaluation, video generation, benchmark, controllable  
- **[RealWonder: Real-Time Physical Action-Conditioned Video Generation](https://arxiv.org/abs/2603.05449v1)**  
  Authors: Wei Liu, Ziyu Chen, Zizhang Li, Yue Wang, Hong-Xing Yu, Jiajun Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05449v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://liuwei283.github.io/RealWonder)  
  Keywords: action-conditioned, camera control, simulation, video generation, physical, physics, dit, interactive  
- **[Phys4D: Fine-Grained Physics-Consistent 4D Modeling from Video Diffusion](https://arxiv.org/abs/2603.03485v2)**  
  Authors: Haoran Lu, Shang Wu, Jianshu Zhang, Maojiang Su, Guo Ye, Chenwei Xu, Lie Lu, Pranav Maneriker, Fan Du, Manling Li, Zhaoran Wang, Han Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.03485v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://sensational-brioche-7657e7.netlify.app/) | [![Demo](https://img.shields.io/badge/-Demo-brightgreen)](https://sensational-brioche-7657e7.netlify.app)  
  Keywords: diffusion model, dynamics, world model, evaluation, video diffusion, simulation, physics, physical  
- **[ShareVerse: Multi-Agent Consistent Video Generation for Shared World Modeling](https://arxiv.org/abs/2603.02697v1)**  
  Authors: Jiayi Zhu, Jianing Zhang, Yiying Yang, Wei Cheng, Xiaoyun Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02697v1.pdf)  
  Keywords: world model, simulation, video generation, multi-view video, dit, interactive  
- **[WorldStereo: Bridging Camera-Guided Video Generation and Scene Reconstruction via 3D Geometric Memories](https://arxiv.org/abs/2603.02049v1)**  
  Authors: Yisu Zhang, Chenjie Cao, Tengfei Wang, Xuhui Zuo, Junta Wu, Jianke Zhu, Chunchao Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02049v1.pdf)  
  Keywords: diffusion model, world model, camera control, video diffusion, video generation, benchmark  
- **[Accelerating Video Generation Inference with Sequential-Parallel 3D Positional Encoding Using a Global Time Index](https://arxiv.org/abs/2603.06664v1)**  
  Authors: Chao Yuan, Pan Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06664v1.pdf)  
  Keywords: long video, diffusion transformer, video generation, autoregressive, video synthesis, dit, interactive  
- **[COMBAT: Conditional World Models for Behavioral Agent Training](https://arxiv.org/abs/2603.00825v1)**  
  Authors: Anmol Agarwal, Pranay Meshram, Sumer Singh, Saurav Suman, Andrew Lapp, Shahbuland Matiana, Louis Castricato, Spencer Frazier  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.00825v1.pdf)  
  Keywords: diffusion model, dit, world model, evaluation, distillation, diffusion transformer, video generation, benchmark, controllable, interactive  
- **[MicroVerse: A Preliminary Exploration Toward a Micro-World Simulation](https://arxiv.org/abs/2603.00585v1)**  
  Authors: Rongsheng Wang, Minghao Wu, Hongru Zhou, Zhihan Yu, Zhenyang Cai, Junying Chen, Benyou Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.00585v1.pdf) | [![GitHub](https://img.shields.io/github/stars/FreedomIntelligence/MicroVerse?style=social)](https://github.com/FreedomIntelligence/MicroVerse)  
  Keywords: dynamics, evaluation, education, simulation, video generation, benchmark, medical, concept, physical, interactive  



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
