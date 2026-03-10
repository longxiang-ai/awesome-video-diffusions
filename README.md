# Awesome Video Diffusions [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Video Diffusion Models and Video Generation. Content is automatically updated daily.

> Last Update: 2026-03-10 02:02:57

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

- [3D-aware Video Generation](#3d-aware-video-generation) (25 papers) - Video generation with 3D awareness, multi-view consistency, and 4D content creation
- [Applications](#applications) (48 papers) - Domain-specific applications of video diffusion models
- [Architecture & Efficiency](#architecture-&-efficiency) (362 papers) - Architectural innovations (DiT, UNet), flow matching, and training/inference efficiency
- [Audio & Multi-modal](#audio-&-multi-modal) (33 papers) - Audio-driven and multi-modal conditioned video generation
- [Controllable Generation](#controllable-generation) (111 papers) - Controllable video generation with motion, camera, pose, or layout guidance
- [Human & Character Animation](#human-&-character-animation) (35 papers) - Human-centric video generation including talking heads, dance, and character animation
- [Image-to-Video Generation](#image-to-video-generation) (40 papers) - Methods for animating still images into videos
- [Long Video Generation](#long-video-generation) (125 papers) - Generating temporally consistent long-form videos beyond short clips
- [Personalization & Customization](#personalization-&-customization) (93 papers) - Personalized video generation with custom subjects, identities, or styles
- [Physical Understanding](#physical-understanding) (122 papers) - Physics-aware video generation and dynamics modeling
- [Surveys & Benchmarks](#surveys-&-benchmarks) (195 papers) - Survey papers, benchmarks, and evaluation metrics for video generation
- [Text-to-Video Generation](#text-to-video-generation) (74 papers) - Foundation models and methods for generating videos from text prompts
- [Video Editing](#video-editing) (37 papers) - Diffusion-based video editing, style transfer, and manipulation
- [Video Inpainting & Completion](#video-inpainting-&-completion) (6 papers) - Video inpainting, completion, outpainting, and temporal prediction
- [Video Super-Resolution & Enhancement](#video-super-resolution-&-enhancement) (55 papers) - Video quality improvement, upscaling, restoration, and frame interpolation
- [World Models & Simulation](#world-models-&-simulation) (97 papers) - Video generation as world simulators and interactive environment generation



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3D-aware Video Generation

- **[Transformer-Based Inpainting for Real-Time 3D Streaming in Sparse Multi-Camera Setups](https://arxiv.org/abs/2603.05507v1)**  
  Authors: Leif Van Holland, Domenic Zingsheim, Mana Takhsha, Hannah Dröge, Patrick Stotko, Markus Plack, Reinhard Klein  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05507v1.pdf)  
  Keywords: dit, streaming, novel view, architecture  
- **[Orthogonal Spatial-temporal Distributional Transfer for 4D Generation](https://arxiv.org/abs/2603.05081v1)**  
  Authors: Wei Liu, Shengqiong Wu, Bobo Li, Haoyu Zhao, Hao Fei, Mong-Li Lee, Wynne Hsu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05081v1.pdf)  
  Keywords: 4d generation, temporal consistency, diffusion model, video diffusion  
- **[ShareVerse: Multi-Agent Consistent Video Generation for Shared World Modeling](https://arxiv.org/abs/2603.02697v1)**  
  Authors: Jiayi Zhu, Jianing Zhang, Yiying Yang, Wei Cheng, Xiaoyun Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02697v1.pdf)  
  Keywords: world model, dit, simulation, multi-view video, interactive, video generation  
- **[HumanOrbit: 3D Human Reconstruction as 360° Orbit Generation](https://arxiv.org/abs/2602.24148v1)**  
  Authors: Keito Suzuki, Kunyao Chen, Lei Wang, Bang Du, Runfa Blark Li, Peng Liu, Ning Bi, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.24148v1.pdf)  
  Keywords: identity, novel view, diffusion model, video diffusion  
- **[BetterScene: 3D Scene Synthesis with Representation-Aligned Generative Model](https://arxiv.org/abs/2602.22596v1)**  
  Authors: Yuci Han, Charles Toth, John E. Anderson, William J. Shuart, Alper Yilmaz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.22596v1.pdf)  
  Keywords: dit, novel view, diffusion model, video diffusion  
- **[Geometry-as-context: Modulating Explicit 3D in Scene-consistent Video Generation to Geometry Context](https://arxiv.org/abs/2602.21929v1)**  
  Authors: JiaKui Hu, Jialun Liu, Liying Yang, Xinliang Zhang, Kaiwen Li, Shuang Zeng, Yuanwei Li, Haibin Huang, Chi Zhang, Yanye Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21929v1.pdf)  
  Keywords: autoregressive, trajectory, camera control, novel view, video generation  
- **[RAYNOVA: Scale-Temporal Autoregressive World Modeling in Ray Space](https://arxiv.org/abs/2602.20685v2)**  
  Authors: Yichen Xie, Chensheng Peng, Mazen Abdelfattah, Yihan Hu, Jiezhi Yang, Eric Higgins, Ryan Brigden, Masayoshi Tomizuka, Wei Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20685v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://raynova-ai.github.io)  
  Keywords: autoregressive, world model, dit, novel view, multi-view video, physical, video generation  
- **[A Single Image and Multimodality Is All You Need for Novel View Synthesis](https://arxiv.org/abs/2602.17909v1)**  
  Authors: Amirhosein Javadi, Chi-Shiang Gau, Konstantinos D. Polyzos, Tara Javidi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.17909v1.pdf)  
  Keywords: dit, video generation, novel view, efficient  
- **[VideoNeuMat: Neural Material Extraction from Generative Video Models](https://arxiv.org/abs/2602.07272v1)**  
  Authors: Bowen Xue, Saeed Hadadan, Zheng Zeng, Fabrice Rousselle, Zahra Montazeri, Milos Hasan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.07272v1.pdf)  
  Keywords: dit, novel view, diffusion model, video diffusion  
- **[CineScene: Implicit 3D as Effective Scene Representation for Cinematic Video Generation](https://arxiv.org/abs/2602.06959v1)**  
  Authors: Kaiyi Huang, Yukun Huang, Yu Li, Jianhong Bai, Xintao Wang, Zinan Lin, Xuefei Ning, Jiwen Yu, Pengfei Wan, Yu Wang, Xihui Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06959v1.pdf)  
  Keywords: text-to-video, trajectory, dit, video synthesis, 3d-aware, physical, video generation  

### Applications

- **[EduVQA: Benchmarking AI-Generated Video Quality Assessment for Education](https://arxiv.org/abs/2603.03066v1)**  
  Authors: Baoliang Chen, Xinlong Bu, Lingyu Zhu, Hanwei Zhu, Xiangjie Sui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.03066v1.pdf)  
  Keywords: evaluation, text-to-video, concept, benchmark, t2v, education  
- **[MicroVerse: A Preliminary Exploration Toward a Micro-World Simulation](https://arxiv.org/abs/2603.00585v1)**  
  Authors: Rongsheng Wang, Minghao Wu, Hongru Zhou, Zhihan Yu, Zhenyang Cai, Junying Chen, Benyou Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.00585v1.pdf) | [![GitHub](https://img.shields.io/github/stars/FreedomIntelligence/MicroVerse?style=social)](https://github.com/FreedomIntelligence/MicroVerse)  
  Keywords: evaluation, concept, simulation, medical, interactive, benchmark, physical, video generation, dynamics, education  
- **[HorizonForge: Driving Scene Editing with Any Trajectories and Any Vehicles](https://arxiv.org/abs/2602.21333v2)**  
  Authors: Yifan Wang, Francesco Pittaluga, Zaid Tasneem, Chenyu You, Manmohan Chandraker, Ziyu Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21333v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://horizonforge.github.io)  
  Keywords: evaluation, trajectory, temporal consistency, dit, simulation, autonomous driving, benchmark, controllable, video diffusion  
- **[GA-Drive: Geometry-Appearance Decoupled Modeling for Free-viewpoint Driving Scene Generatio](https://arxiv.org/abs/2602.20673v1)**  
  Authors: Hao Zhang, Lue Fan, Qitai Wang, Wenbo Li, Zehuan Wu, Lewei Lu, Zhaoxiang Zhang, Hongsheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20673v1.pdf)  
  Keywords: trajectory, dit, video-to-video, simulation, autonomous driving, video editing, diffusion model, video diffusion  
- **[3DSPA: A 3D Semantic Point Autoencoder for Evaluating Video Realism](https://arxiv.org/abs/2602.20354v1)**  
  Authors: Bhavik Chandna, Kelsey R. Allen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20354v1.pdf) | [![GitHub](https://img.shields.io/github/stars/TheProParadox/3dspa_code?style=social)](https://github.com/TheProParadox/3dspa_code)  
  Keywords: film, evaluation, robotics, trajectory, temporal consistency, benchmark, physical, video generation  
- **[PedaCo-Gen: Scaffolding Pedagogical Agency in Human-AI Collaborative Video Authoring](https://arxiv.org/abs/2602.19623v1)**  
  Authors: Injun Baek, Yearim Kim, Nojun Kwak  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.19623v1.pdf)  
  Keywords: text-to-video, dit, interactive, t2v, education  
- **[VideoSketcher: Video Models Prior Enable Versatile Sequential Sketch Generation](https://arxiv.org/abs/2602.15819v1)**  
  Authors: Hui Ren, Yuval Alaluf, Omer Bar Tal, Alexander Schwing, Antonio Torralba, Yael Vinker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.15819v1.pdf)  
  Keywords: style, text-to-video, autoregressive, dit, creative, interactive, efficient, diffusion model, video diffusion  
- **[Beyond End-to-End Video Models: An LLM-Based Multi-Agent System for Educational Video Generation](https://arxiv.org/abs/2602.11790v1)**  
  Authors: Lingyong Yan, Jiulong Wu, Dong Xie, Weixian Shi, Deguo Xia, Jizhou Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.11790v1.pdf)  
  Keywords: dit, video generation, education  
- **[Ctrl&Shift: High-Quality Geometry-Aware Object Manipulation in Visual Generation](https://arxiv.org/abs/2602.11440v1)**  
  Authors: Penghui Ruan, Bojia Zi, Xianbiao Qi, Youze Huang, Rong Xiao, Pichao Wang, Jiannong Cao, Yuhui Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.11440v1.pdf)  
  Keywords: film, dit, creative, controllable, identity  
- **[VideoWorld 2: Learning Transferable Knowledge from Real-world Videos](https://arxiv.org/abs/2602.10102v1)**  
  Authors: Zhongwei Ren, Yunchao Wei, Xiao Yu, Guixun Luo, Yao Zhao, Bingyi Kang, Jiashi Feng, Xiaojie Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.10102v1.pdf)  
  Keywords: autoregressive, robotics, video generation, dynamics, diffusion model, video diffusion  

### Architecture & Efficiency

*Showing the latest 50 out of 362 papers*

- **[Video2LoRA: Unified Semantic-Controlled Video Generation via Per-Reference-Video LoRA](https://arxiv.org/abs/2603.08210v1)**  
  Authors: Zexi Wu, Qinghe Wang, Jing Dai, Baolu Li, Yiming Zhang, Yue Ma, Xu Jia, Hongming Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08210v1.pdf)  
  Keywords: dit, video generation, style, efficient  
- **[MM-TS: Multi-Modal Temperature and Margin Schedules for Contrastive Learning with Long-Tail Data](https://arxiv.org/abs/2603.08202v1)**  
  Authors: Siarhei Sheludzko, Dhimitrios Duka, Bernt Schiele, Hilde Kuehne, Anna Kukleva  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08202v1.pdf)  
  Keywords: dit, multi-modal, concept  
- **[Controllable Complex Human Motion Video Generation via Text-to-Skeleton Cascades](https://arxiv.org/abs/2603.08028v1)**  
  Authors: Ashkan Taghipour, Morteza Ghahremani, Zinuo Li, Hamid Laga, Farid Boussaid, Mohammed Bennamoun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08028v1.pdf)  
  Keywords: autoregressive, temporal consistency, human motion, dit, benchmark, motion control, controllable, video generation, diffusion model, video diffusion  
- **[FastSTAR: Spatiotemporal Token Pruning for Efficient Autoregressive Video Synthesis](https://arxiv.org/abs/2603.07192v1)**  
  Authors: Sungwoong Yune, Suheon Jeong, Joo-Young Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.07192v1.pdf)  
  Keywords: autoregressive, video synthesis, acceleration, efficient, video generation  
- **[Two Frames Matter: A Temporal Attack for Text-to-Video Model Jailbreaking](https://arxiv.org/abs/2603.07028v1)**  
  Authors: Moyang Chen, Zonghao Ying, Wenzhuo Xu, Quancheng Zou, Deyue Zhang, Dongdong Yang, Xiangzheng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.07028v1.pdf)  
  Keywords: evaluation, text-to-video, trajectory, dit, t2v  
- **[Penguin-VL: Exploring the Efficiency Limits of VLM with LLM-based Vision Encoders](https://arxiv.org/abs/2603.06569v1)**  
  Authors: Boqiang Zhang, Lei Ke, Ruihan Yang, Qi Gao, Tianyuan Qu, Rossell Chen, Dong Yu, Leoweiliang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06569v1.pdf) | [![GitHub](https://img.shields.io/github/stars/tencent-ailab/Penguin-VL?style=social)](https://github.com/tencent-ailab/Penguin-VL)  
  Keywords: dit, architecture, benchmark, efficient  
- **[NEGATE: Constrained Semantic Guidance for Linguistic Negation in Text-to-Video Diffusion](https://arxiv.org/abs/2603.06533v1)**  
  Authors: Taewon Kang, Ming C. Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06533v1.pdf)  
  Keywords: evaluation, text-to-video, dit, benchmark, dynamics, video diffusion  
- **[Pinterest Canvas: Large-Scale Image Generation at Pinterest](https://arxiv.org/abs/2603.06453v1)**  
  Authors: Yu Wang, Eric Tzeng, Raymond Shiau, Jie Yang, Dmitry Kislyuk, Charles Rosenberg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06453v1.pdf)  
  Keywords: dit, image-to-video, video generation, diffusion model, outpainting  
- **[Place-it-R1: Unlocking Environment-aware Reasoning Potential of MLLM for Video Object Insertion](https://arxiv.org/abs/2603.06140v1)**  
  Authors: Bohai Gu, Taiyi Wu, Dazhao Du, Jian Liu, Shuai Yang, Xiaotong Zhao, Alan Zhao, Song Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06140v1.pdf)  
  Keywords: dit, video editing, physical, diffusion model, video diffusion  
- **[Cross-Resolution Distribution Matching for Diffusion Distillation](https://arxiv.org/abs/2603.06136v1)**  
  Authors: Feiyang Chen, Hongpeng Pan, Haonan Xu, Xinyu Duan, Yang Yang, Zhefeng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06136v1.pdf)  
  Keywords: dit, video generation, distillation, denoising  

### Audio & Multi-modal

- **[MM-TS: Multi-Modal Temperature and Margin Schedules for Contrastive Learning with Long-Tail Data](https://arxiv.org/abs/2603.08202v1)**  
  Authors: Siarhei Sheludzko, Dhimitrios Duka, Bernt Schiele, Hilde Kuehne, Anna Kukleva  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08202v1.pdf)  
  Keywords: dit, multi-modal, concept  
- **[StreamWise: Serving Multi-Modal Generation in Real-Time at Scale](https://arxiv.org/abs/2603.05800v1)**  
  Authors: Haoran Qiu, Gohar Irfan Chaudhry, Chaojie Zhang, Íñigo Goiri, Esha Choukse, Rodrigo Fonseca, Ricardo Bianchini  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05800v1.pdf)  
  Keywords: multi-modal, video generation, streaming, efficient  
- **[UniTalking: A Unified Audio-Video Framework for Talking Portrait Generation](https://arxiv.org/abs/2603.01418v1)**  
  Authors: Hebeizi Li, Zihao Liang, Benyuan Sun, Zihao Yin, Xiao Sha, Chenliang Wang, Yi Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01418v1.pdf)  
  Keywords: style, multi-modal, architecture, efficient, video generation  
- **[FlowPortrait: Reinforcement Learning for Audio-Driven Portrait Video Generation](https://arxiv.org/abs/2603.00159v1)**  
  Authors: Weiting Tan, Andy T. Liu, Ming Tu, Xinghua Qu, Philipp Koehn, Lu Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.00159v1.pdf)  
  Keywords: evaluation, autoregressive, audio-driven, temporal consistency, video generation, audio-to-video  
- **[SkyReels-V4: Multi-modal Video-Audio Generation, Inpainting and Editing model](https://arxiv.org/abs/2602.21818v2)**  
  Authors: Guibin Chen, Dixuan Lin, Jiangping Yang, Youqiang Zhang, Zhengcong Fei, Debang Li, Sheng Chen, Chaofeng Ao, Nuo Pang, Yiming Wang, Yikun Dou, Zheng Chen, Mingyuan Fan, Tuanhui Li, Mingshan Chang, Hao Zhang, Xiaopeng Sun, Jingtao Xu, Yuqiang Xie, Jiahua Wang, Zhiheng Xu, Weiming Xiong, Yuzhe Jin, Baoxuan Gu, Binjie Mao, Yunjie Yu, Jujie He, Yuhao Feng, Shiwen Tu, Chaojie Wang, Rui Yan, Wei Shen, Jingchen Wu, Peng Zhao, Xuanyue Zhong, Zhuangzhuang Liu, Kaifei Wang, Fuxiang Zhang, Weikai Xu, Wenyan Liu, Binglu Zhang, Yu Shen, Tianhui Xiong, Bin Peng, Liang Zeng, Xuchen Song, Haoxiang Guo, Peiyu Wang, Max W. Y. Lam, Chien-Hung Liu, Yahui Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21818v2.pdf)  
  Keywords: style, frame interpolation, sound, diffusion transformer, dit, multi-modal, image to video, architecture, video editing, super-resolution, video generation  
- **[JavisDiT++: Unified Modeling and Optimization for Joint Audio-Video Generation](https://arxiv.org/abs/2602.19163v1)**  
  Authors: Kai Liu, Yanhao Zheng, Kai Wang, Shengqiong Wu, Rongjunchen Zhang, Jiebo Luo, Dimitrios Hatzinakos, Ziwei Liu, Hao Fei, Tat-Seng Chua  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.19163v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://JavisVerse.github.io/JavisDiT2-page)  
  Keywords: evaluation, sound, dit, t2v, video generation  
- **[EchoTorrent: Towards Swift, Sustained, and Streaming Multi-Modal Video Generation](https://arxiv.org/abs/2602.13669v2)**  
  Authors: Rang Meng, Yingjie Yin, Yuming Li, Chenguang Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.13669v2.pdf)  
  Keywords: autoregressive, temporal consistency, multi-modal, architecture, video generation, streaming, identity  
- **[DreamID-Omni: Unified Framework for Controllable Human-Centric Audio-Video Generation](https://arxiv.org/abs/2602.12160v1)**  
  Authors: Xu Guo, Fulong Ye, Qichao Sun, Liyang Chen, Bingchuan Li, Pengze Zhang, Jiawei Liu, Songtao Zhao, Qian He, Xiangwang Hou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.12160v1.pdf)  
  Keywords: audio-driven, diffusion transformer, dit, video editing, controllable, video generation, identity  
- **[TiFRe: Text-guided Video Frame Reduction for Efficient Video Multi-modal Large Language Models](https://arxiv.org/abs/2602.08861v1)**  
  Authors: Xiangtian Zheng, Zishuo Wang, Yuxin Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.08861v1.pdf)  
  Keywords: style, multi-modal, efficient  
- **[VideoVeritas: AI-Generated Video Detection via Perception Pretext Reinforcement Learning](https://arxiv.org/abs/2602.08828v1)**  
  Authors: Hao Tan, Jun Lan, Senyuan Shi, Zichang Tan, Zijian Yu, Huijia Zhu, Weiqiang Wang, Jun Wan, Zhen Lei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.08828v1.pdf)  
  Keywords: evaluation, video generation, multi-modal, benchmark  

### Controllable Generation

*Showing the latest 50 out of 111 papers*

- **[Controllable Complex Human Motion Video Generation via Text-to-Skeleton Cascades](https://arxiv.org/abs/2603.08028v1)**  
  Authors: Ashkan Taghipour, Morteza Ghahremani, Zinuo Li, Hamid Laga, Farid Boussaid, Mohammed Bennamoun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08028v1.pdf)  
  Keywords: autoregressive, temporal consistency, human motion, dit, benchmark, motion control, controllable, video generation, diffusion model, video diffusion  
- **[TDM-R1: Reinforcing Few-Step Diffusion Models with Non-Differentiable Reward](https://arxiv.org/abs/2603.07700v1)**  
  Authors: Yihong Luo, Tianyang Hu, Weijian Luo, Jing Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.07700v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Luo-Yihong/TDM-R1?style=social)](https://github.com/Luo-Yihong/TDM-R1)  
  Keywords: video generation, trajectory, diffusion model  
- **[Two Frames Matter: A Temporal Attack for Text-to-Video Model Jailbreaking](https://arxiv.org/abs/2603.07028v1)**  
  Authors: Moyang Chen, Zonghao Ying, Wenzhuo Xu, Quancheng Zou, Deyue Zhang, Dongdong Yang, Xiangzheng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.07028v1.pdf)  
  Keywords: evaluation, text-to-video, trajectory, dit, t2v  
- **[FaceCam: Portrait Video Camera Control via Scale-Aware Conditioning](https://arxiv.org/abs/2603.05506v1)**  
  Authors: Weijie Lyu, Ming-Hsuan Yang, Zhixin Shu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05506v1.pdf)  
  Keywords: camera control, video generation, identity, dit  
- **[RealWonder: Real-Time Physical Action-Conditioned Video Generation](https://arxiv.org/abs/2603.05449v1)**  
  Authors: Wei Liu, Ziyu Chen, Zizhang Li, Yue Wang, Hong-Xing Yu, Jiajun Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05449v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://liuwei283.github.io/RealWonder)  
  Keywords: camera control, dit, simulation, action-conditioned, interactive, physical, video generation, physics  
- **[Frequency-Aware Error-Bounded Caching for Accelerating Diffusion Transformers](https://arxiv.org/abs/2603.05315v1)**  
  Authors: Guandong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05315v1.pdf)  
  Keywords: trajectory, diffusion transformer, dit, denoising, architecture, video generation, dynamics  
- **[FC-VFI: Faithful and Consistent Video Frame Interpolation for High-FPS Slow Motion Video Generation](https://arxiv.org/abs/2603.04899v1)**  
  Authors: Ganggui Ding, Hao Chen, Xiaogang Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.04899v1.pdf)  
  Keywords: frame interpolation, temporal consistency, motion control, video generation, diffusion model, video diffusion  
- **[TC-Padé: Trajectory-Consistent Padé Approximation for Diffusion Acceleration](https://arxiv.org/abs/2603.02943v1)**  
  Authors: Benlei Cui, Shaoxuan He, Bukun Huang, Zhizeng Ye, Yunyun Sun, Longtao Huang, Hui Xue, Yang Yang, Jingqun Tang, Zhou Zhao, Haiwen Hong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02943v1.pdf)  
  Keywords: trajectory, dit, denoising, acceleration, efficient, video generation, dynamics, diffusion model  
- **[LiftAvatar: Kinematic-Space Completion for Expression-Controlled 3D Gaussian Avatar Animation](https://arxiv.org/abs/2603.02129v1)**  
  Authors: Hualiang Wei, Shunran Jia, Jialun Liu, Wenhui Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02129v1.pdf)  
  Keywords: diffusion transformer, dit, efficient, controllable, distillation, avatar, video diffusion  
- **[WorldStereo: Bridging Camera-Guided Video Generation and Scene Reconstruction via 3D Geometric Memories](https://arxiv.org/abs/2603.02049v1)**  
  Authors: Yisu Zhang, Chenjie Cao, Tengfei Wang, Xuhui Zuo, Junta Wu, Jianke Zhu, Chunchao Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02049v1.pdf)  
  Keywords: world model, camera control, benchmark, video generation, diffusion model, video diffusion  

### Human & Character Animation

- **[Controllable Complex Human Motion Video Generation via Text-to-Skeleton Cascades](https://arxiv.org/abs/2603.08028v1)**  
  Authors: Ashkan Taghipour, Morteza Ghahremani, Zinuo Li, Hamid Laga, Farid Boussaid, Mohammed Bennamoun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08028v1.pdf)  
  Keywords: autoregressive, temporal consistency, human motion, dit, benchmark, motion control, controllable, video generation, diffusion model, video diffusion  
- **[ArtHOI: Articulated Human-Object Interaction Synthesis by 4D Reconstruction from Video Priors](https://arxiv.org/abs/2603.04338v1)**  
  Authors: Zihao Huang, Tianqi Liu, Zhaoxi Chen, Shaocong Xu, Saining Zhang, Lixing Xiao, Zhiguo Cao, Wei Li, Hao Zhao, Ziwei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.04338v1.pdf)  
  Keywords: human motion, dit, physical, diffusion model, video diffusion  
- **[Direct Reward Fine-Tuning on Poses for Single Image to 3D Human in the Wild](https://arxiv.org/abs/2603.02619v1)**  
  Authors: Seunguk Do, Minwoo Huh, Joonghyuk Shin, Jaesik Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02619v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://seunguk-do.github.io/drpose)  
  Keywords: evaluation, human motion, dit, benchmark, diffusion model  
- **[LiftAvatar: Kinematic-Space Completion for Expression-Controlled 3D Gaussian Avatar Animation](https://arxiv.org/abs/2603.02129v1)**  
  Authors: Hualiang Wei, Shunran Jia, Jialun Liu, Wenhui Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02129v1.pdf)  
  Keywords: diffusion transformer, dit, efficient, controllable, distillation, avatar, video diffusion  
- **[Non-verbal Real-time Human-AI Interaction in Constrained Robotic Environments](https://arxiv.org/abs/2603.01804v1)**  
  Authors: Dragos Costea, Alina Marcu, Cristina Lazar, Marius Leordeanu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01804v1.pdf)  
  Keywords: body motion, text-to-video, architecture  
- **[GeoDiff4D: Geometry-Aware Diffusion for 4D Head Avatar Reconstruction](https://arxiv.org/abs/2602.24161v1)**  
  Authors: Chao Xu, Xiaochen Zhao, Xiang Deng, Jingxiang Sun, Zhuo Su, Donglin Di, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.24161v1.pdf)  
  Keywords: video generation, identity, avatar, diffusion model  
- **[Spatio-Temporal Garment Reconstruction Using Diffusion Mapping via Pattern Coordinates](https://arxiv.org/abs/2602.24043v1)**  
  Authors: Yingxuan You, Ren Li, Corentin Dumery, Cong Cao, Hao Li, Pascal Fua  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.24043v1.pdf)  
  Keywords: temporal consistency, dit, virtual try-on, avatar, diffusion model  
- **[BigMaQ: A Big Macaque Motion and Animation Dataset Bridging Image and 3D Pose Representations](https://arxiv.org/abs/2602.19874v1)**  
  Authors: Lucas Martini, Alexander Lappe, Anna Bognár, Rufin Vogels, Martin A. Giese  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.19874v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://martinivis.github.io/BigMaQ)  
  Keywords: dynamics, avatar, benchmark  
- **[Ani3DHuman: Photorealistic 3D Human Animation with Self-guided Stochastic Sampling](https://arxiv.org/abs/2602.19089v1)**  
  Authors: Qi Sun, Can Wang, Jiaxiang Shang, Yingchun Liu, Jing Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.19089v1.pdf) | [![GitHub](https://img.shields.io/github/stars/qiisun/ani3dhuman?style=social)](https://github.com/qiisun/ani3dhuman)  
  Keywords: human animation, dynamics, identity, diffusion model, video diffusion  
- **[HairWeaver: Few-Shot Photorealistic Hair Motion Synthesis with Sim-to-Real Guided Video Diffusion](https://arxiv.org/abs/2602.11117v1)**  
  Authors: Di Chang, Ji Hou, Aljaz Bozic, Assaf Neuberger, Felix Juefei-Xu, Olivier Maury, Gene Wei-Chin Lin, Tuur Stuyck, Doug Roble, Mohammad Soleymani, Stephane Grabli  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.11117v1.pdf)  
  Keywords: evaluation, human motion, dit, dynamics, video diffusion  

### Image-to-Video Generation

- **[Pinterest Canvas: Large-Scale Image Generation at Pinterest](https://arxiv.org/abs/2603.06453v1)**  
  Authors: Yu Wang, Eric Tzeng, Raymond Shiau, Jie Yang, Dmitry Kislyuk, Charles Rosenberg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06453v1.pdf)  
  Keywords: dit, image-to-video, video generation, diffusion model, outpainting  
- **[Helios: Real Real-Time Long Video Generation Model](https://arxiv.org/abs/2603.04379v1)**  
  Authors: Shenghai Yuan, Yuanyang Yin, Zongjian Li, Xinwei Huang, Xiao Yang, Li Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.04379v1.pdf)  
  Keywords: autoregressive, i2v, long video, acceleration, t2v, video generation, diffusion model  
- **[FastLightGen: Fast and Light Video Generation with Fewer Steps and Parameters](https://arxiv.org/abs/2603.01685v2)**  
  Authors: Shitong Shao, Yufei Gu, Zeke Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01685v2.pdf)  
  Keywords: i2v, video generation, distillation, efficient  
- **[FREE-Edit: Using Editing-aware Injection in Rectified Flow Models for Zero-shot Image-Driven Video Editing](https://arxiv.org/abs/2603.01164v1)**  
  Authors: Maomao Li, Yunfei Liu, Yu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01164v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://free-edit.github.io/page)  
  Keywords: image-driven, layout, i2v, dit, denoising, rectified flow, video editing, image-to-video  
- **[Let Your Image Move with Your Motion! -- Implicit Multi-Object Multi-Motion Transfer](https://arxiv.org/abs/2603.01000v1)**  
  Authors: Yuze Li, Dong Gong, Xiao Cao, Junchao Yuan, Dongsheng Li, Lei Zhou, Yun Sing Koh, Cheng Yan, Xinyu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01000v1.pdf)  
  Keywords: i2v, image-to-video, efficient, controllable, video generation  
- **[SkyReels-V4: Multi-modal Video-Audio Generation, Inpainting and Editing model](https://arxiv.org/abs/2602.21818v2)**  
  Authors: Guibin Chen, Dixuan Lin, Jiangping Yang, Youqiang Zhang, Zhengcong Fei, Debang Li, Sheng Chen, Chaofeng Ao, Nuo Pang, Yiming Wang, Yikun Dou, Zheng Chen, Mingyuan Fan, Tuanhui Li, Mingshan Chang, Hao Zhang, Xiaopeng Sun, Jingtao Xu, Yuqiang Xie, Jiahua Wang, Zhiheng Xu, Weiming Xiong, Yuzhe Jin, Baoxuan Gu, Binjie Mao, Yunjie Yu, Jujie He, Yuhao Feng, Shiwen Tu, Chaojie Wang, Rui Yan, Wei Shen, Jingchen Wu, Peng Zhao, Xuanyue Zhong, Zhuangzhuang Liu, Kaifei Wang, Fuxiang Zhang, Weikai Xu, Wenyan Liu, Binglu Zhang, Yu Shen, Tianhui Xiong, Bin Peng, Liang Zeng, Xuchen Song, Haoxiang Guo, Peiyu Wang, Max W. Y. Lam, Chien-Hung Liu, Yahui Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21818v2.pdf)  
  Keywords: style, frame interpolation, sound, diffusion transformer, dit, multi-modal, image to video, architecture, video editing, super-resolution, video generation  
- **[MultiAnimate: Pose-Guided Image Animation Made Extensible](https://arxiv.org/abs/2602.21581v1)**  
  Authors: Yingcheng Hu, Haowen Gong, Chuanguang Yang, Zhulin An, Yongjun Xu, Songhua Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21581v1.pdf)  
  Keywords: diffusion transformer, dit, image animation, video generation, identity, pose-guided  
- **[Human Video Generation from a Single Image with 3D Pose and View Control](https://arxiv.org/abs/2602.21188v1)**  
  Authors: Tiantian Wang, Chun-Han Yao, Tao Hu, Mallikarjun Byrasandra Ramalinga Reddy, Ming-Hsuan Yang, Varun Jampani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21188v1.pdf)  
  Keywords: latent video, video synthesis, image-to-video, video generation, diffusion model, video diffusion  
- **[VII: Visual Instruction Injection for Jailbreaking Image-to-Video Generation Models](https://arxiv.org/abs/2602.20999v2)**  
  Authors: Bowen Zheng, Yongli Xiang, Ziming Hong, Zerong Lin, Chaojian Yu, Tongliang Liu, Xinge You  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20999v2.pdf)  
  Keywords: i2v, video generation, dit, image-to-video  
- **[AnimeAgent: Is the Multi-Agent via Image-to-Video models a Good Disney Storytelling Artist?](https://arxiv.org/abs/2602.20664v1)**  
  Authors: Hailong Yan, Shice Liu, Tao Wang, Xiangtao Zhang, Yijie Zhong, Jinwei Chen, Le Zhang, Bo Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20664v1.pdf)  
  Keywords: i2v, benchmark, diffusion model, image-to-video  

### Long Video Generation

*Showing the latest 50 out of 125 papers*

- **[Controllable Complex Human Motion Video Generation via Text-to-Skeleton Cascades](https://arxiv.org/abs/2603.08028v1)**  
  Authors: Ashkan Taghipour, Morteza Ghahremani, Zinuo Li, Hamid Laga, Farid Boussaid, Mohammed Bennamoun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08028v1.pdf)  
  Keywords: autoregressive, temporal consistency, human motion, dit, benchmark, motion control, controllable, video generation, diffusion model, video diffusion  
- **[Image Generation Models: A Technical History](https://arxiv.org/abs/2603.07455v1)**  
  Authors: Rouzbeh Shirvani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.07455v1.pdf)  
  Keywords: survey, video generation, autoregressive  
- **[FastSTAR: Spatiotemporal Token Pruning for Efficient Autoregressive Video Synthesis](https://arxiv.org/abs/2603.07192v1)**  
  Authors: Sungwoong Yune, Suheon Jeong, Joo-Young Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.07192v1.pdf)  
  Keywords: autoregressive, video synthesis, acceleration, efficient, video generation  
- **[StreamWise: Serving Multi-Modal Generation in Real-Time at Scale](https://arxiv.org/abs/2603.05800v1)**  
  Authors: Haoran Qiu, Gohar Irfan Chaudhry, Chaojie Zhang, Íñigo Goiri, Esha Choukse, Rodrigo Fonseca, Ricardo Bianchini  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05800v1.pdf)  
  Keywords: multi-modal, video generation, streaming, efficient  
- **[Transformer-Based Inpainting for Real-Time 3D Streaming in Sparse Multi-Camera Setups](https://arxiv.org/abs/2603.05507v1)**  
  Authors: Leif Van Holland, Domenic Zingsheim, Mana Takhsha, Hannah Dröge, Patrick Stotko, Markus Plack, Reinhard Klein  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05507v1.pdf)  
  Keywords: dit, streaming, novel view, architecture  
- **[Orthogonal Spatial-temporal Distributional Transfer for 4D Generation](https://arxiv.org/abs/2603.05081v1)**  
  Authors: Wei Liu, Shengqiong Wu, Bobo Li, Haoyu Zhao, Hao Fei, Mong-Li Lee, Wynne Hsu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05081v1.pdf)  
  Keywords: 4d generation, temporal consistency, diffusion model, video diffusion  
- **[FC-VFI: Faithful and Consistent Video Frame Interpolation for High-FPS Slow Motion Video Generation](https://arxiv.org/abs/2603.04899v1)**  
  Authors: Ganggui Ding, Hao Chen, Xiaogang Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.04899v1.pdf)  
  Keywords: frame interpolation, temporal consistency, motion control, video generation, diffusion model, video diffusion  
- **[Helios: Real Real-Time Long Video Generation Model](https://arxiv.org/abs/2603.04379v1)**  
  Authors: Shenghai Yuan, Yuanyang Yin, Zongjian Li, Xinwei Huang, Xiao Yang, Li Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.04379v1.pdf)  
  Keywords: autoregressive, i2v, long video, acceleration, t2v, video generation, diffusion model  
- **[CubeComposer: Spatio-Temporal Autoregressive 4K 360° Video Generation from Perspective Video](https://arxiv.org/abs/2603.04291v1)**  
  Authors: Lingen Li, Guangzhi Wang, Xiaoyu Li, Zhaoyang Zhang, Qi Dou, Jinwei Gu, Tianfan Xue, Ying Shan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.04291v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lg-li.github.io/project/cubecomposer)  
  Keywords: autoregressive, benchmark, super-resolution, video generation, diffusion model  
- **[InfinityStory: Unlimited Video Generation with World Consistency and Character-Aware Shot Transitions](https://arxiv.org/abs/2603.03646v1)**  
  Authors: Mohamed Elmoghany, Liangbing Zhao, Xiaoqian Shen, Subhojyoti Mukherjee, Yang Zhou, Gang Wu, Viet Dac Lai, Seunghyun Yoon, Ryan Rossi, Abdullah Rashwan, Puneet Mathur, Varun Manjunatha, Daksh Dangi, Chien Nguyen, Nedim Lipka, Trung Bui, Krishna Kumar Singh, Ruiyi Zhang, Xiaolei Huang, Jaemin Cho, Yu Wang, Namyong Park, Zhengzhong Tu, Hongjie Chen, Hoda Eldardiry, Nesreen Ahmed, Thien Nguyen, Dinesh Manocha, Mohamed Elhoseiny, Franck Dernoncourt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.03646v1.pdf)  
  Keywords: video synthesis, video generation, identity, long-form  

### Personalization & Customization

*Showing the latest 50 out of 93 papers*

- **[Video2LoRA: Unified Semantic-Controlled Video Generation via Per-Reference-Video LoRA](https://arxiv.org/abs/2603.08210v1)**  
  Authors: Zexi Wu, Qinghe Wang, Jing Dai, Baolu Li, Yiming Zhang, Yue Ma, Xu Jia, Hongming Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08210v1.pdf)  
  Keywords: dit, video generation, style, efficient  
- **[MM-TS: Multi-Modal Temperature and Margin Schedules for Contrastive Learning with Long-Tail Data](https://arxiv.org/abs/2603.08202v1)**  
  Authors: Siarhei Sheludzko, Dhimitrios Duka, Bernt Schiele, Hilde Kuehne, Anna Kukleva  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08202v1.pdf)  
  Keywords: dit, multi-modal, concept  
- **[GenHOI: Towards Object-Consistent Hand-Object Interaction with Temporally Balanced and Spatially Selective Object Injection](https://arxiv.org/abs/2603.06048v1)**  
  Authors: Xuan Huang, Mochu Xiang, Zhelun Shen, Jinbo Wu, Chenming Wu, Chen Zhao, Kaisiyuan Wang, Hang Zhou, Shanshan Liu, Haocheng Feng, Wei He, Jingdong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06048v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xuanhuang0.github.io/GenHOI)  
  Keywords: evaluation, dit, video synthesis, video editing, physical, video generation, identity  
- **[FaceCam: Portrait Video Camera Control via Scale-Aware Conditioning](https://arxiv.org/abs/2603.05506v1)**  
  Authors: Weijie Lyu, Ming-Hsuan Yang, Zhixin Shu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05506v1.pdf)  
  Keywords: camera control, video generation, identity, dit  
- **[InfinityStory: Unlimited Video Generation with World Consistency and Character-Aware Shot Transitions](https://arxiv.org/abs/2603.03646v1)**  
  Authors: Mohamed Elmoghany, Liangbing Zhao, Xiaoqian Shen, Subhojyoti Mukherjee, Yang Zhou, Gang Wu, Viet Dac Lai, Seunghyun Yoon, Ryan Rossi, Abdullah Rashwan, Puneet Mathur, Varun Manjunatha, Daksh Dangi, Chien Nguyen, Nedim Lipka, Trung Bui, Krishna Kumar Singh, Ruiyi Zhang, Xiaolei Huang, Jaemin Cho, Yu Wang, Namyong Park, Zhengzhong Tu, Hongjie Chen, Hoda Eldardiry, Nesreen Ahmed, Thien Nguyen, Dinesh Manocha, Mohamed Elhoseiny, Franck Dernoncourt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.03646v1.pdf)  
  Keywords: video synthesis, video generation, identity, long-form  
- **[EduVQA: Benchmarking AI-Generated Video Quality Assessment for Education](https://arxiv.org/abs/2603.03066v1)**  
  Authors: Baoliang Chen, Xinlong Bu, Lingyu Zhu, Hanwei Zhu, Xiangjie Sui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.03066v1.pdf)  
  Keywords: evaluation, text-to-video, concept, benchmark, t2v, education  
- **[Interpretable Motion-Attentive Maps: Spatio-Temporally Localizing Concepts in Video Diffusion Transformers](https://arxiv.org/abs/2603.02919v1)**  
  Authors: Youngjun Jun, Seil Kang, Woojung Han, Seong Jae Hwang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02919v1.pdf)  
  Keywords: dit, concept, diffusion transformer, video diffusion  
- **[Does Semantic Noise Initialization Transfer from Images to Videos? A Paired Diagnostic Study](https://arxiv.org/abs/2603.06672v1)**  
  Authors: Yixiao Jing, Chaoyu Zhang, Zixuan Zhong, Peizhou Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06672v1.pdf)  
  Keywords: style, evaluation, text-to-video, benchmark, t2v, diffusion model  
- **[UniTalking: A Unified Audio-Video Framework for Talking Portrait Generation](https://arxiv.org/abs/2603.01418v1)**  
  Authors: Hebeizi Li, Zihao Liang, Benyuan Sun, Zihao Yin, Xiao Sha, Chenliang Wang, Yi Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01418v1.pdf)  
  Keywords: style, multi-modal, architecture, efficient, video generation  
- **[Unified Vision-Language Modeling via Concept Space Alignment](https://arxiv.org/abs/2603.01096v1)**  
  Authors: Yifu Qiu, Paul-Ambroise Duquenne, Holger Schwenk  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01096v1.pdf)  
  Keywords: text-to-video, concept  

### Physical Understanding

*Showing the latest 50 out of 122 papers*

- **[NEGATE: Constrained Semantic Guidance for Linguistic Negation in Text-to-Video Diffusion](https://arxiv.org/abs/2603.06533v1)**  
  Authors: Taewon Kang, Ming C. Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06533v1.pdf)  
  Keywords: evaluation, text-to-video, dit, benchmark, dynamics, video diffusion  
- **[Physical Simulator In-the-Loop Video Generation](https://arxiv.org/abs/2603.06408v1)**  
  Authors: Lin Geng Foo, Mark He Huang, Alexandros Lattas, Stylianos Moschoglou, Thabo Beeler, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06408v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vcai.mpi-inf.mpg.de/projects/PSIVG)  
  Keywords: diffusion model, physical, video generation, dynamics, physics, video diffusion  
- **[Place-it-R1: Unlocking Environment-aware Reasoning Potential of MLLM for Video Object Insertion](https://arxiv.org/abs/2603.06140v1)**  
  Authors: Bohai Gu, Taiyi Wu, Dazhao Du, Jian Liu, Shuai Yang, Xiaotong Zhao, Alan Zhao, Song Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06140v1.pdf)  
  Keywords: dit, video editing, physical, diffusion model, video diffusion  
- **[GenHOI: Towards Object-Consistent Hand-Object Interaction with Temporally Balanced and Spatially Selective Object Injection](https://arxiv.org/abs/2603.06048v1)**  
  Authors: Xuan Huang, Mochu Xiang, Zhelun Shen, Jinbo Wu, Chenming Wu, Chen Zhao, Kaisiyuan Wang, Hang Zhou, Shanshan Liu, Haocheng Feng, Wei He, Jingdong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06048v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xuanhuang0.github.io/GenHOI)  
  Keywords: evaluation, dit, video synthesis, video editing, physical, video generation, identity  
- **[RealWonder: Real-Time Physical Action-Conditioned Video Generation](https://arxiv.org/abs/2603.05449v1)**  
  Authors: Wei Liu, Ziyu Chen, Zizhang Li, Yue Wang, Hong-Xing Yu, Jiajun Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05449v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://liuwei283.github.io/RealWonder)  
  Keywords: camera control, dit, simulation, action-conditioned, interactive, physical, video generation, physics  
- **[Frequency-Aware Error-Bounded Caching for Accelerating Diffusion Transformers](https://arxiv.org/abs/2603.05315v1)**  
  Authors: Guandong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05315v1.pdf)  
  Keywords: trajectory, diffusion transformer, dit, denoising, architecture, video generation, dynamics  
- **[ArtHOI: Articulated Human-Object Interaction Synthesis by 4D Reconstruction from Video Priors](https://arxiv.org/abs/2603.04338v1)**  
  Authors: Zihao Huang, Tianqi Liu, Zhaoxi Chen, Shaocong Xu, Saining Zhang, Lixing Xiao, Zhiguo Cao, Wei Li, Hao Zhao, Ziwei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.04338v1.pdf)  
  Keywords: human motion, dit, physical, diffusion model, video diffusion  
- **[PhyPrompt: RL-based Prompt Refinement for Physically Plausible Text-to-Video Generation](https://arxiv.org/abs/2603.03505v1)**  
  Authors: Shang Wu, Chenwei Xu, Zhuofan Xia, Weijian Li, Lie Lu, Pranav Maneriker, Fan Du, Manling Li, Han Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.03505v1.pdf)  
  Keywords: text-to-video, architecture, t2v, video generation, physics-aware, physical, physics  
- **[Phys4D: Fine-Grained Physics-Consistent 4D Modeling from Video Diffusion](https://arxiv.org/abs/2603.03485v2)**  
  Authors: Haoran Lu, Shang Wu, Jianshu Zhang, Maojiang Su, Guo Ye, Chenwei Xu, Lie Lu, Pranav Maneriker, Fan Du, Manling Li, Zhaoran Wang, Han Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.03485v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://sensational-brioche-7657e7.netlify.app/) | [![Demo](https://img.shields.io/badge/-Demo-brightgreen)](https://sensational-brioche-7657e7.netlify.app)  
  Keywords: evaluation, world model, simulation, physical, physics, dynamics, diffusion model, video diffusion  
- **[TC-Padé: Trajectory-Consistent Padé Approximation for Diffusion Acceleration](https://arxiv.org/abs/2603.02943v1)**  
  Authors: Benlei Cui, Shaoxuan He, Bukun Huang, Zhizeng Ye, Yunyun Sun, Longtao Huang, Hui Xue, Yang Yang, Jingqun Tang, Zhou Zhao, Haiwen Hong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02943v1.pdf)  
  Keywords: trajectory, dit, denoising, acceleration, efficient, video generation, dynamics, diffusion model  

### Surveys & Benchmarks

*Showing the latest 50 out of 195 papers*

- **[Controllable Complex Human Motion Video Generation via Text-to-Skeleton Cascades](https://arxiv.org/abs/2603.08028v1)**  
  Authors: Ashkan Taghipour, Morteza Ghahremani, Zinuo Li, Hamid Laga, Farid Boussaid, Mohammed Bennamoun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08028v1.pdf)  
  Keywords: autoregressive, temporal consistency, human motion, dit, benchmark, motion control, controllable, video generation, diffusion model, video diffusion  
- **[Image Generation Models: A Technical History](https://arxiv.org/abs/2603.07455v1)**  
  Authors: Rouzbeh Shirvani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.07455v1.pdf)  
  Keywords: survey, video generation, autoregressive  
- **[VIVECaption: A Split Approach to Caption Quality Improvement](https://arxiv.org/abs/2603.07401v1)**  
  Authors: Varun Ananth, Baqiao Liu, Haoran Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.07401v1.pdf)  
  Keywords: evaluation, text-to-video, t2v  
- **[Two Frames Matter: A Temporal Attack for Text-to-Video Model Jailbreaking](https://arxiv.org/abs/2603.07028v1)**  
  Authors: Moyang Chen, Zonghao Ying, Wenzhuo Xu, Quancheng Zou, Deyue Zhang, Dongdong Yang, Xiangzheng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.07028v1.pdf)  
  Keywords: evaluation, text-to-video, trajectory, dit, t2v  
- **[Penguin-VL: Exploring the Efficiency Limits of VLM with LLM-based Vision Encoders](https://arxiv.org/abs/2603.06569v1)**  
  Authors: Boqiang Zhang, Lei Ke, Ruihan Yang, Qi Gao, Tianyuan Qu, Rossell Chen, Dong Yu, Leoweiliang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06569v1.pdf) | [![GitHub](https://img.shields.io/github/stars/tencent-ailab/Penguin-VL?style=social)](https://github.com/tencent-ailab/Penguin-VL)  
  Keywords: dit, architecture, benchmark, efficient  
- **[NEGATE: Constrained Semantic Guidance for Linguistic Negation in Text-to-Video Diffusion](https://arxiv.org/abs/2603.06533v1)**  
  Authors: Taewon Kang, Ming C. Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06533v1.pdf)  
  Keywords: evaluation, text-to-video, dit, benchmark, dynamics, video diffusion  
- **[GenHOI: Towards Object-Consistent Hand-Object Interaction with Temporally Balanced and Spatially Selective Object Injection](https://arxiv.org/abs/2603.06048v1)**  
  Authors: Xuan Huang, Mochu Xiang, Zhelun Shen, Jinbo Wu, Chenming Wu, Chen Zhao, Kaisiyuan Wang, Hang Zhou, Shanshan Liu, Haocheng Feng, Wei He, Jingdong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06048v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xuanhuang0.github.io/GenHOI)  
  Keywords: evaluation, dit, video synthesis, video editing, physical, video generation, identity  
- **[MultiHaystack: Benchmarking Multimodal Retrieval and Reasoning over 40K Images, Videos, and Documents](https://arxiv.org/abs/2603.05697v1)**  
  Authors: Dannong Xu, Zhongyu Yang, Jun Chen, Yingfang Yuan, Ming Hu, Lei Sun, Luc Van Gool, Danda Pani Paudel, Chun-Mei Feng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05697v1.pdf)  
  Keywords: dit, evaluation, benchmark  
- **[UniM: A Unified Any-to-Any Interleaved Multimodal Benchmark](https://arxiv.org/abs/2603.05075v1)**  
  Authors: Yanlin Li, Minghui Guo, Kaiwen Zhang, Shize Zhang, Yiran Zhao, Haodong Li, Congyue Zhou, Weijie Zheng, Yushen Yan, Shengqiong Wu, Wei Ji, Lei Cui, Furu Wei, Hao Fei, Mong-Li Lee, Wynne Hsu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05075v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://any2any-mllm.github.io/unim)  
  Keywords: dit, evaluation, benchmark  
- **[CubeComposer: Spatio-Temporal Autoregressive 4K 360° Video Generation from Perspective Video](https://arxiv.org/abs/2603.04291v1)**  
  Authors: Lingen Li, Guangzhi Wang, Xiaoyu Li, Zhaoyang Zhang, Qi Dou, Jinwei Gu, Tianfan Xue, Ying Shan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.04291v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lg-li.github.io/project/cubecomposer)  
  Keywords: autoregressive, benchmark, super-resolution, video generation, diffusion model  

### Text-to-Video Generation

*Showing the latest 50 out of 74 papers*

- **[VIVECaption: A Split Approach to Caption Quality Improvement](https://arxiv.org/abs/2603.07401v1)**  
  Authors: Varun Ananth, Baqiao Liu, Haoran Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.07401v1.pdf)  
  Keywords: evaluation, text-to-video, t2v  
- **[Two Frames Matter: A Temporal Attack for Text-to-Video Model Jailbreaking](https://arxiv.org/abs/2603.07028v1)**  
  Authors: Moyang Chen, Zonghao Ying, Wenzhuo Xu, Quancheng Zou, Deyue Zhang, Dongdong Yang, Xiangzheng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.07028v1.pdf)  
  Keywords: evaluation, text-to-video, trajectory, dit, t2v  
- **[NEGATE: Constrained Semantic Guidance for Linguistic Negation in Text-to-Video Diffusion](https://arxiv.org/abs/2603.06533v1)**  
  Authors: Taewon Kang, Ming C. Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06533v1.pdf)  
  Keywords: evaluation, text-to-video, dit, benchmark, dynamics, video diffusion  
- **[Accelerating Text-to-Video Generation with Calibrated Sparse Attention](https://arxiv.org/abs/2603.05503v1)**  
  Authors: Shai Yehezkel, Shahar Yadin, Noam Elata, Yaron Ostrovsky-Berman, Bahjat Kawar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05503v1.pdf)  
  Keywords: video generation, text-to-video, diffusion model, efficient  
- **[Helios: Real Real-Time Long Video Generation Model](https://arxiv.org/abs/2603.04379v1)**  
  Authors: Shenghai Yuan, Yuanyang Yin, Zongjian Li, Xinwei Huang, Xiao Yang, Li Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.04379v1.pdf)  
  Keywords: autoregressive, i2v, long video, acceleration, t2v, video generation, diffusion model  
- **[PhyPrompt: RL-based Prompt Refinement for Physically Plausible Text-to-Video Generation](https://arxiv.org/abs/2603.03505v1)**  
  Authors: Shang Wu, Chenwei Xu, Zhuofan Xia, Weijian Li, Lie Lu, Pranav Maneriker, Fan Du, Manling Li, Han Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.03505v1.pdf)  
  Keywords: text-to-video, architecture, t2v, video generation, physics-aware, physical, physics  
- **[EduVQA: Benchmarking AI-Generated Video Quality Assessment for Education](https://arxiv.org/abs/2603.03066v1)**  
  Authors: Baoliang Chen, Xinlong Bu, Lingyu Zhu, Hanwei Zhu, Xiangjie Sui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.03066v1.pdf)  
  Keywords: evaluation, text-to-video, concept, benchmark, t2v, education  
- **[BrandFusion: A Multi-Agent Framework for Seamless Brand Integration in Text-to-Video Generation](https://arxiv.org/abs/2603.02816v1)**  
  Authors: Zihao Zhu, Ruotong Wang, Siwei Lyu, Min Zhang, Baoyuan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02816v1.pdf)  
  Keywords: evaluation, video generation, text-to-video, t2v  
- **[Does Semantic Noise Initialization Transfer from Images to Videos? A Paired Diagnostic Study](https://arxiv.org/abs/2603.06672v1)**  
  Authors: Yixiao Jing, Chaoyu Zhang, Zixuan Zhong, Peizhou Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06672v1.pdf)  
  Keywords: style, evaluation, text-to-video, benchmark, t2v, diffusion model  
- **[Non-verbal Real-time Human-AI Interaction in Constrained Robotic Environments](https://arxiv.org/abs/2603.01804v1)**  
  Authors: Dragos Costea, Alina Marcu, Cristina Lazar, Marius Leordeanu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01804v1.pdf)  
  Keywords: body motion, text-to-video, architecture  

### Video Editing

- **[Place-it-R1: Unlocking Environment-aware Reasoning Potential of MLLM for Video Object Insertion](https://arxiv.org/abs/2603.06140v1)**  
  Authors: Bohai Gu, Taiyi Wu, Dazhao Du, Jian Liu, Shuai Yang, Xiaotong Zhao, Alan Zhao, Song Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06140v1.pdf)  
  Keywords: dit, video editing, physical, diffusion model, video diffusion  
- **[GenHOI: Towards Object-Consistent Hand-Object Interaction with Temporally Balanced and Spatially Selective Object Injection](https://arxiv.org/abs/2603.06048v1)**  
  Authors: Xuan Huang, Mochu Xiang, Zhelun Shen, Jinbo Wu, Chenming Wu, Chen Zhao, Kaisiyuan Wang, Hang Zhou, Shanshan Liu, Haocheng Feng, Wei He, Jingdong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06048v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xuanhuang0.github.io/GenHOI)  
  Keywords: evaluation, dit, video synthesis, video editing, physical, video generation, identity  
- **[Training-free Latent Inter-Frame Pruning with Attention Recovery](https://arxiv.org/abs/2603.05811v1)**  
  Authors: Dennis Menn, Yuedong Yang, Bokun Wang, Xiwen Wei, Mustafa Munir, Feng Liang, Radu Marculescu, Chenfeng Xu, Diana Marculescu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05811v1.pdf)  
  Keywords: dit, video generation, video editing  
- **[FREE-Edit: Using Editing-aware Injection in Rectified Flow Models for Zero-shot Image-Driven Video Editing](https://arxiv.org/abs/2603.01164v1)**  
  Authors: Maomao Li, Yunfei Liu, Yu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01164v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://free-edit.github.io/page)  
  Keywords: image-driven, layout, i2v, dit, denoising, rectified flow, video editing, image-to-video  
- **[UniVBench: Towards Unified Evaluation for Video Foundation Models](https://arxiv.org/abs/2602.21835v2)**  
  Authors: Jianhui Wei, Xiaotian Zhang, Yichen Li, Yuan Wang, Yan Zhang, Ziyi Chen, Zhihang Tang, Wei Xu, Zuozhu Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21835v2.pdf)  
  Keywords: evaluation, dit, video editing, benchmark, video generation  
- **[SkyReels-V4: Multi-modal Video-Audio Generation, Inpainting and Editing model](https://arxiv.org/abs/2602.21818v2)**  
  Authors: Guibin Chen, Dixuan Lin, Jiangping Yang, Youqiang Zhang, Zhengcong Fei, Debang Li, Sheng Chen, Chaofeng Ao, Nuo Pang, Yiming Wang, Yikun Dou, Zheng Chen, Mingyuan Fan, Tuanhui Li, Mingshan Chang, Hao Zhang, Xiaopeng Sun, Jingtao Xu, Yuqiang Xie, Jiahua Wang, Zhiheng Xu, Weiming Xiong, Yuzhe Jin, Baoxuan Gu, Binjie Mao, Yunjie Yu, Jujie He, Yuhao Feng, Shiwen Tu, Chaojie Wang, Rui Yan, Wei Shen, Jingchen Wu, Peng Zhao, Xuanyue Zhong, Zhuangzhuang Liu, Kaifei Wang, Fuxiang Zhang, Weikai Xu, Wenyan Liu, Binglu Zhang, Yu Shen, Tianhui Xiong, Bin Peng, Liang Zeng, Xuchen Song, Haoxiang Guo, Peiyu Wang, Max W. Y. Lam, Chien-Hung Liu, Yahui Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21818v2.pdf)  
  Keywords: style, frame interpolation, sound, diffusion transformer, dit, multi-modal, image to video, architecture, video editing, super-resolution, video generation  
- **[GA-Drive: Geometry-Appearance Decoupled Modeling for Free-viewpoint Driving Scene Generatio](https://arxiv.org/abs/2602.20673v1)**  
  Authors: Hao Zhang, Lue Fan, Qitai Wang, Wenbo Li, Zehuan Wu, Lewei Lu, Zhaoxiang Zhang, Hongsheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20673v1.pdf)  
  Keywords: trajectory, dit, video-to-video, simulation, autonomous driving, video editing, diffusion model, video diffusion  
- **[PropFly: Learning to Propagate via On-the-Fly Supervision from Pre-trained Video Diffusion Models](https://arxiv.org/abs/2602.20583v1)**  
  Authors: Wonyong Seo, Jaeho Moon, Jaehyup Lee, Soo Ye Kim, Munchurl Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20583v1.pdf)  
  Keywords: flow matching, dit, video editing, diffusion model, video diffusion  
- **[RoboCurate: Harnessing Diversity with Action-Verified Neural Trajectory for Robot Learning](https://arxiv.org/abs/2602.18742v1)**  
  Authors: Seungku Kim, Suhyeok Jang, Byungjun Yoon, Dongyoung Kim, John Won, Jinwoo Shin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.18742v1.pdf)  
  Keywords: trajectory, dit, video-to-video, simulation, physical  
- **[When Test-Time Guidance Is Enough: Fast Image and Video Editing with Diffusion Guidance](https://arxiv.org/abs/2602.14157v1)**  
  Authors: Ahmed Ghorbel, Badr Moufad, Navid Bagheri Shouraki, Alain Oliviero Durmus, Thomas Hirtz, Eric Moulines, Jimmy Olsson, Yazid Janati  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.14157v1.pdf)  
  Keywords: video editing, evaluation, dit, benchmark  

### Video Inpainting & Completion

- **[Pinterest Canvas: Large-Scale Image Generation at Pinterest](https://arxiv.org/abs/2603.06453v1)**  
  Authors: Yu Wang, Eric Tzeng, Raymond Shiau, Jie Yang, Dmitry Kislyuk, Charles Rosenberg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06453v1.pdf)  
  Keywords: dit, image-to-video, video generation, diffusion model, outpainting  
- **[Learning Physics-Grounded 4D Dynamics with Neural Gaussian Force Fields](https://arxiv.org/abs/2602.00148v2)**  
  Authors: Shiqian Li, Ruihong Shen, Junfeng Ni, Chang Pan, Chi Zhang, Yixin Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.00148v2.pdf)  
  Keywords: evaluation, video prediction, world model, simulation, interactive, physical, video generation, dynamics, physics  
- **[DriveLaW:Unifying Planning and Video Generation in a Latent Driving World](https://arxiv.org/abs/2512.23421v2)**  
  Authors: Tianze Xia, Yongkang Li, Lijun Zhou, Jingfeng Yao, Kaixin Xiong, Haiyang Sun, Bing Wang, Kun Ma, Guang Chen, Hangjun Ye, Wenyu Liu, Xinggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.23421v2.pdf)  
  Keywords: video prediction, trajectory, world model, architecture, autonomous driving, benchmark, video generation  
- **[Autoregressive Flow Matching for Motion Prediction](https://arxiv.org/abs/2512.22688v1)**  
  Authors: Johnathan Xie, Stefan Stojanov, Cristobal Eyzaguirre, Daniel L. K. Yamins, Jiajun Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.22688v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Johnathan-Xie/arfm-motion-prediction?style=social)](https://github.com/Johnathan-Xie/arfm-motion-prediction)  
  Keywords: autoregressive, video prediction, flow matching, human motion, robotics, dit, benchmark, video generation  
- **[Over++: Generative Video Compositing for Layer Interaction Effects](https://arxiv.org/abs/2512.19661v1)**  
  Authors: Luchao Qi, Jiaye Wu, Jun Myeong Choi, Cary Phillips, Roni Sengupta, Dan B Goldman  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.19661v1.pdf)  
  Keywords: dit, video inpainting  
- **[Vidarc: Embodied Video Diffusion Model for Closed-loop Control](https://arxiv.org/abs/2512.17661v1)**  
  Authors: Yao Feng, Chendong Xiang, Xinyi Mao, Hengkai Tan, Zuyue Zhang, Shuhe Huang, Kaiwen Zheng, Haitian Liu, Hang Su, Jun Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.17661v1.pdf)  
  Keywords: autoregressive, video prediction, physical, dynamics, diffusion model, video diffusion  

### Video Super-Resolution & Enhancement

*Showing the latest 50 out of 55 papers*

- **[Cross-Resolution Distribution Matching for Diffusion Distillation](https://arxiv.org/abs/2603.06136v1)**  
  Authors: Feiyang Chen, Hongpeng Pan, Haonan Xu, Xinyu Duan, Yang Yang, Zhefeng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06136v1.pdf)  
  Keywords: dit, video generation, distillation, denoising  
- **[Frequency-Aware Error-Bounded Caching for Accelerating Diffusion Transformers](https://arxiv.org/abs/2603.05315v1)**  
  Authors: Guandong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05315v1.pdf)  
  Keywords: trajectory, diffusion transformer, dit, denoising, architecture, video generation, dynamics  
- **[FC-VFI: Faithful and Consistent Video Frame Interpolation for High-FPS Slow Motion Video Generation](https://arxiv.org/abs/2603.04899v1)**  
  Authors: Ganggui Ding, Hao Chen, Xiaogang Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.04899v1.pdf)  
  Keywords: frame interpolation, temporal consistency, motion control, video generation, diffusion model, video diffusion  
- **[CubeComposer: Spatio-Temporal Autoregressive 4K 360° Video Generation from Perspective Video](https://arxiv.org/abs/2603.04291v1)**  
  Authors: Lingen Li, Guangzhi Wang, Xiaoyu Li, Zhaoyang Zhang, Qi Dou, Jinwei Gu, Tianfan Xue, Ying Shan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.04291v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lg-li.github.io/project/cubecomposer)  
  Keywords: autoregressive, benchmark, super-resolution, video generation, diffusion model  
- **[TC-Padé: Trajectory-Consistent Padé Approximation for Diffusion Acceleration](https://arxiv.org/abs/2603.02943v1)**  
  Authors: Benlei Cui, Shaoxuan He, Bukun Huang, Zhizeng Ye, Yunyun Sun, Longtao Huang, Hui Xue, Yang Yang, Jingqun Tang, Zhou Zhao, Haiwen Hong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02943v1.pdf)  
  Keywords: trajectory, dit, denoising, acceleration, efficient, video generation, dynamics, diffusion model  
- **[Retrieval, Refinement, and Ranking for Text-to-Video Generation via Prompt Optimization and Test-Time Scaling](https://arxiv.org/abs/2603.01509v1)**  
  Authors: Zillur Rahman, Alex Sheng, Cristian Meo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01509v1.pdf)  
  Keywords: text-to-video, frame interpolation, dit, efficient, t2v, video generation, diffusion model  
- **[FREE-Edit: Using Editing-aware Injection in Rectified Flow Models for Zero-shot Image-Driven Video Editing](https://arxiv.org/abs/2603.01164v1)**  
  Authors: Maomao Li, Yunfei Liu, Yu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01164v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://free-edit.github.io/page)  
  Keywords: image-driven, layout, i2v, dit, denoising, rectified flow, video editing, image-to-video  
- **[SenCache: Accelerating Diffusion Model Inference via Sensitivity-Aware Caching](https://arxiv.org/abs/2602.24208v1)**  
  Authors: Yasaman Haghighi, Alexandre Alahi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.24208v1.pdf)  
  Keywords: acceleration, video generation, denoising, diffusion model  
- **[Denoising as Path Planning: Training-Free Acceleration of Diffusion Models with DPCache](https://arxiv.org/abs/2602.22654v2)**  
  Authors: Bowen Cui, Yuanbin Wang, Huajiang Xu, Biaolong Chen, Aixi Zhang, Hao Jiang, Zhengzheng Jin, Xu Liu, Pipei Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.22654v2.pdf) | [![GitHub](https://img.shields.io/github/stars/argsss/DPCache?style=social)](https://github.com/argsss/DPCache)  
  Keywords: trajectory, dit, denoising, acceleration, efficient, video generation, diffusion model  
- **[SkyReels-V4: Multi-modal Video-Audio Generation, Inpainting and Editing model](https://arxiv.org/abs/2602.21818v2)**  
  Authors: Guibin Chen, Dixuan Lin, Jiangping Yang, Youqiang Zhang, Zhengcong Fei, Debang Li, Sheng Chen, Chaofeng Ao, Nuo Pang, Yiming Wang, Yikun Dou, Zheng Chen, Mingyuan Fan, Tuanhui Li, Mingshan Chang, Hao Zhang, Xiaopeng Sun, Jingtao Xu, Yuqiang Xie, Jiahua Wang, Zhiheng Xu, Weiming Xiong, Yuzhe Jin, Baoxuan Gu, Binjie Mao, Yunjie Yu, Jujie He, Yuhao Feng, Shiwen Tu, Chaojie Wang, Rui Yan, Wei Shen, Jingchen Wu, Peng Zhao, Xuanyue Zhong, Zhuangzhuang Liu, Kaifei Wang, Fuxiang Zhang, Weikai Xu, Wenyan Liu, Binglu Zhang, Yu Shen, Tianhui Xiong, Bin Peng, Liang Zeng, Xuchen Song, Haoxiang Guo, Peiyu Wang, Max W. Y. Lam, Chien-Hung Liu, Yahui Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21818v2.pdf)  
  Keywords: style, frame interpolation, sound, diffusion transformer, dit, multi-modal, image to video, architecture, video editing, super-resolution, video generation  

### World Models & Simulation

*Showing the latest 50 out of 97 papers*

- **[RealWonder: Real-Time Physical Action-Conditioned Video Generation](https://arxiv.org/abs/2603.05449v1)**  
  Authors: Wei Liu, Ziyu Chen, Zizhang Li, Yue Wang, Hong-Xing Yu, Jiajun Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05449v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://liuwei283.github.io/RealWonder)  
  Keywords: camera control, dit, simulation, action-conditioned, interactive, physical, video generation, physics  
- **[Phys4D: Fine-Grained Physics-Consistent 4D Modeling from Video Diffusion](https://arxiv.org/abs/2603.03485v2)**  
  Authors: Haoran Lu, Shang Wu, Jianshu Zhang, Maojiang Su, Guo Ye, Chenwei Xu, Lie Lu, Pranav Maneriker, Fan Du, Manling Li, Zhaoran Wang, Han Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.03485v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://sensational-brioche-7657e7.netlify.app/) | [![Demo](https://img.shields.io/badge/-Demo-brightgreen)](https://sensational-brioche-7657e7.netlify.app)  
  Keywords: evaluation, world model, simulation, physical, physics, dynamics, diffusion model, video diffusion  
- **[ShareVerse: Multi-Agent Consistent Video Generation for Shared World Modeling](https://arxiv.org/abs/2603.02697v1)**  
  Authors: Jiayi Zhu, Jianing Zhang, Yiying Yang, Wei Cheng, Xiaoyun Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02697v1.pdf)  
  Keywords: world model, dit, simulation, multi-view video, interactive, video generation  
- **[WorldStereo: Bridging Camera-Guided Video Generation and Scene Reconstruction via 3D Geometric Memories](https://arxiv.org/abs/2603.02049v1)**  
  Authors: Yisu Zhang, Chenjie Cao, Tengfei Wang, Xuhui Zuo, Junta Wu, Jianke Zhu, Chunchao Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02049v1.pdf)  
  Keywords: world model, camera control, benchmark, video generation, diffusion model, video diffusion  
- **[Accelerating Video Generation Inference with Sequential-Parallel 3D Positional Encoding Using a Global Time Index](https://arxiv.org/abs/2603.06664v1)**  
  Authors: Chao Yuan, Pan Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06664v1.pdf)  
  Keywords: autoregressive, diffusion transformer, long video, dit, video synthesis, interactive, video generation  
- **[COMBAT: Conditional World Models for Behavioral Agent Training](https://arxiv.org/abs/2603.00825v1)**  
  Authors: Anmol Agarwal, Pranay Meshram, Sumer Singh, Saurav Suman, Andrew Lapp, Shahbuland Matiana, Louis Castricato, Spencer Frazier  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.00825v1.pdf)  
  Keywords: evaluation, diffusion transformer, world model, dit, interactive, benchmark, controllable, video generation, distillation, diffusion model  
- **[MicroVerse: A Preliminary Exploration Toward a Micro-World Simulation](https://arxiv.org/abs/2603.00585v1)**  
  Authors: Rongsheng Wang, Minghao Wu, Hongru Zhou, Zhihan Yu, Zhenyang Cai, Junying Chen, Benyou Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.00585v1.pdf) | [![GitHub](https://img.shields.io/github/stars/FreedomIntelligence/MicroVerse?style=social)](https://github.com/FreedomIntelligence/MicroVerse)  
  Keywords: evaluation, concept, simulation, medical, interactive, benchmark, physical, video generation, dynamics, education  
- **[DreamWorld: Unified World Modeling in Video Generation](https://arxiv.org/abs/2603.00466v1)**  
  Authors: Boming Tan, Xiangdong Zhang, Ning Liao, Yuqing Zhang, Shaofeng Zhang, Xue Yang, Qi Fan, Yanyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.00466v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ABU121111/DreamWorld?style=social)](https://github.com/ABU121111/DreamWorld)  
  Keywords: evaluation, temporal consistency, world model, dit, physical, video generation, dynamics  
- **[MSVBench: Towards Human-Level Evaluation of Multi-Shot Video Generation](https://arxiv.org/abs/2602.23969v1)**  
  Authors: Haoyuan Shi, Yunxin Li, Nanhao Deng, Zhenran Xu, Xinyu Chen, Longyue Wang, Baotian Hu, Min Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.23969v1.pdf)  
  Keywords: evaluation, world model, benchmark, video generation, long-form  
- **[U-Mind: A Unified Framework for Real-Time Multimodal Interaction with Audiovisual Generation](https://arxiv.org/abs/2602.23739v1)**  
  Authors: Xiang Deng, Feng Gao, Yong Zhang, Youxin Pang, Xu Xiaoming, Zhuoliang Kang, Xiaoming Wei, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.23739v1.pdf)  
  Keywords: video synthesis, interactive, dit  



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
