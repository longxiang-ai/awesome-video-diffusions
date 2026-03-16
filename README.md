# Awesome Video Diffusions [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Video Diffusion Models and Video Generation. Content is automatically updated daily.

> Last Update: 2026-03-16 02:30:18

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

- [3D-aware Video Generation](#3d-aware-video-generation) (23 papers) - Video generation with 3D awareness, multi-view consistency, and 4D content creation
- [Applications](#applications) (50 papers) - Domain-specific applications of video diffusion models
- [Architecture & Efficiency](#architecture-&-efficiency) (361 papers) - Architectural innovations (DiT, UNet), flow matching, and training/inference efficiency
- [Audio & Multi-modal](#audio-&-multi-modal) (31 papers) - Audio-driven and multi-modal conditioned video generation
- [Controllable Generation](#controllable-generation) (110 papers) - Controllable video generation with motion, camera, pose, or layout guidance
- [Human & Character Animation](#human-&-character-animation) (35 papers) - Human-centric video generation including talking heads, dance, and character animation
- [Image-to-Video Generation](#image-to-video-generation) (40 papers) - Methods for animating still images into videos
- [Long Video Generation](#long-video-generation) (125 papers) - Generating temporally consistent long-form videos beyond short clips
- [Personalization & Customization](#personalization-&-customization) (91 papers) - Personalized video generation with custom subjects, identities, or styles
- [Physical Understanding](#physical-understanding) (134 papers) - Physics-aware video generation and dynamics modeling
- [Surveys & Benchmarks](#surveys-&-benchmarks) (201 papers) - Survey papers, benchmarks, and evaluation metrics for video generation
- [Text-to-Video Generation](#text-to-video-generation) (71 papers) - Foundation models and methods for generating videos from text prompts
- [Video Editing](#video-editing) (35 papers) - Diffusion-based video editing, style transfer, and manipulation
- [Video Inpainting & Completion](#video-inpainting-&-completion) (7 papers) - Video inpainting, completion, outpainting, and temporal prediction
- [Video Super-Resolution & Enhancement](#video-super-resolution-&-enhancement) (53 papers) - Video quality improvement, upscaling, restoration, and frame interpolation
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
  Keywords: video interpolation, camera control, dit, diffusion model, novel view, video diffusion  
- **[Transformer-Based Inpainting for Real-Time 3D Streaming in Sparse Multi-Camera Setups](https://arxiv.org/abs/2603.05507v1)**  
  Authors: Leif Van Holland, Domenic Zingsheim, Mana Takhsha, Hannah Dröge, Patrick Stotko, Markus Plack, Reinhard Klein  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05507v1.pdf)  
  Keywords: novel view, dit, architecture, streaming  
- **[Orthogonal Spatial-temporal Distributional Transfer for 4D Generation](https://arxiv.org/abs/2603.05081v1)**  
  Authors: Wei Liu, Shengqiong Wu, Bobo Li, Haoyu Zhao, Hao Fei, Mong-Li Lee, Wynne Hsu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05081v1.pdf)  
  Keywords: 4d generation, temporal consistency, video diffusion, diffusion model  
- **[ShareVerse: Multi-Agent Consistent Video Generation for Shared World Modeling](https://arxiv.org/abs/2603.02697v1)**  
  Authors: Jiayi Zhu, Jianing Zhang, Yiying Yang, Wei Cheng, Xiaoyun Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02697v1.pdf)  
  Keywords: world model, simulation, dit, interactive, multi-view video, video generation  
- **[HumanOrbit: 3D Human Reconstruction as 360° Orbit Generation](https://arxiv.org/abs/2602.24148v1)**  
  Authors: Keito Suzuki, Kunyao Chen, Lei Wang, Bang Du, Runfa Blark Li, Peng Liu, Ning Bi, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.24148v1.pdf)  
  Keywords: novel view, video diffusion, identity, diffusion model  
- **[BetterScene: 3D Scene Synthesis with Representation-Aligned Generative Model](https://arxiv.org/abs/2602.22596v1)**  
  Authors: Yuci Han, Charles Toth, John E. Anderson, William J. Shuart, Alper Yilmaz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.22596v1.pdf)  
  Keywords: novel view, video diffusion, dit, diffusion model  
- **[Geometry-as-context: Modulating Explicit 3D in Scene-consistent Video Generation to Geometry Context](https://arxiv.org/abs/2602.21929v1)**  
  Authors: JiaKui Hu, Jialun Liu, Liying Yang, Xinliang Zhang, Kaiwen Li, Shuang Zeng, Yuanwei Li, Haibin Huang, Chi Zhang, Yanye Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21929v1.pdf)  
  Keywords: camera control, novel view, video generation, trajectory, autoregressive  
- **[RAYNOVA: Scale-Temporal Autoregressive World Modeling in Ray Space](https://arxiv.org/abs/2602.20685v2)**  
  Authors: Yichen Xie, Chensheng Peng, Mazen Abdelfattah, Yihan Hu, Jiezhi Yang, Eric Higgins, Ryan Brigden, Masayoshi Tomizuka, Wei Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20685v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://raynova-ai.github.io)  
  Keywords: world model, dit, physical, novel view, video generation, multi-view video, autoregressive  
- **[A Single Image and Multimodality Is All You Need for Novel View Synthesis](https://arxiv.org/abs/2602.17909v1)**  
  Authors: Amirhosein Javadi, Chi-Shiang Gau, Konstantinos D. Polyzos, Tara Javidi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.17909v1.pdf)  
  Keywords: novel view, dit, efficient, video generation  
- **[VideoNeuMat: Neural Material Extraction from Generative Video Models](https://arxiv.org/abs/2602.07272v1)**  
  Authors: Bowen Xue, Saeed Hadadan, Zheng Zeng, Fabrice Rousselle, Zahra Montazeri, Milos Hasan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.07272v1.pdf)  
  Keywords: novel view, video diffusion, dit, diffusion model  

### Applications

- **[Risk-Controllable Multi-View Diffusion for Driving Scenario Generation](https://arxiv.org/abs/2603.11534v1)**  
  Authors: Hongyi Lin, Wenxiu Shi, Heye Huang, Dingyi Zhuang, Song Zhang, Yang Liu, Xiaobo Qu, Jinhua Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.11534v1.pdf)  
  Keywords: world model, controllable, physical, autonomous driving  
- **[ShotVerse: Advancing Cinematic Camera Control for Text-Driven Multi-Shot Video Creation](https://arxiv.org/abs/2603.11421v1)**  
  Authors: Songlin Yang, Zhe Wang, Xuyi Yang, Songchun Zhang, Xianghao Kong, Taiyi Wu, Xiaotong Zhao, Ran Zhang, Alan Zhao, Anyi Rao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.11421v1.pdf)  
  Keywords: camera control, film, dit, evaluation, text-driven video, trajectory, video generation  
- **[Motion Forcing: A Decoupled Framework for Robust Video Generation in Motion Dynamics](https://arxiv.org/abs/2603.10408v1)**  
  Authors: Tianshuo Xu, Zhifei Chen, Leyi Wu, Hao Lu, Ying-cong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.10408v1.pdf)  
  Keywords: dynamics, physical, robotics, autonomous driving, physics, evaluation, video generation, benchmark  
- **[EduVQA: Benchmarking AI-Generated Video Quality Assessment for Education](https://arxiv.org/abs/2603.03066v1)**  
  Authors: Baoliang Chen, Xinlong Bu, Lingyu Zhu, Hanwei Zhu, Xiangjie Sui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.03066v1.pdf)  
  Keywords: t2v, education, evaluation, concept, text-to-video, benchmark  
- **[MicroVerse: A Preliminary Exploration Toward a Micro-World Simulation](https://arxiv.org/abs/2603.00585v1)**  
  Authors: Rongsheng Wang, Minghao Wu, Hongru Zhou, Zhihan Yu, Zhenyang Cai, Junying Chen, Benyou Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.00585v1.pdf) | [![GitHub](https://img.shields.io/github/stars/FreedomIntelligence/MicroVerse?style=social)](https://github.com/FreedomIntelligence/MicroVerse)  
  Keywords: simulation, dynamics, physical, education, medical, evaluation, interactive, video generation, concept, benchmark  
- **[HorizonForge: Driving Scene Editing with Any Trajectories and Any Vehicles](https://arxiv.org/abs/2602.21333v2)**  
  Authors: Yifan Wang, Francesco Pittaluga, Zaid Tasneem, Chenyu You, Manmohan Chandraker, Ziyu Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21333v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://horizonforge.github.io)  
  Keywords: temporal consistency, simulation, controllable, dit, autonomous driving, video diffusion, evaluation, trajectory, benchmark  
- **[GA-Drive: Geometry-Appearance Decoupled Modeling for Free-viewpoint Driving Scene Generation](https://arxiv.org/abs/2602.20673v2)**  
  Authors: Hao Zhang, Lue Fan, Qitai Wang, Wenbo Li, Zehuan Wu, Lewei Lu, Zhaoxiang Zhang, Hongsheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20673v2.pdf)  
  Keywords: video editing, simulation, dit, diffusion model, video-to-video, autonomous driving, video diffusion, trajectory  
- **[3DSPA: A 3D Semantic Point Autoencoder for Evaluating Video Realism](https://arxiv.org/abs/2602.20354v1)**  
  Authors: Bhavik Chandna, Kelsey R. Allen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20354v1.pdf) | [![GitHub](https://img.shields.io/github/stars/TheProParadox/3dspa_code?style=social)](https://github.com/TheProParadox/3dspa_code)  
  Keywords: temporal consistency, film, physical, robotics, video generation, evaluation, trajectory, benchmark  
- **[PedaCo-Gen: Scaffolding Pedagogical Agency in Human-AI Collaborative Video Authoring](https://arxiv.org/abs/2602.19623v1)**  
  Authors: Injun Baek, Yearim Kim, Nojun Kwak  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.19623v1.pdf)  
  Keywords: t2v, dit, education, interactive, text-to-video  
- **[VideoSketcher: Video Models Prior Enable Versatile Sequential Sketch Generation](https://arxiv.org/abs/2602.15819v1)**  
  Authors: Hui Ren, Yuval Alaluf, Omer Bar Tal, Alexander Schwing, Antonio Torralba, Yael Vinker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.15819v1.pdf)  
  Keywords: creative, dit, diffusion model, efficient, style, video diffusion, interactive, text-to-video, autoregressive  

### Architecture & Efficiency

*Showing the latest 50 out of 361 papers*

- **[V-Bridge: Bridging Video Generative Priors to Versatile Few-shot Image Restoration](https://arxiv.org/abs/2603.13089v1)**  
  Authors: Shenghe Zheng, Junpeng Jiang, Wenbo Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.13089v1.pdf)  
  Keywords: dit, architecture  
- **[SAW: Toward a Surgical Action World Model via Controllable and Scalable Video Generation](https://arxiv.org/abs/2603.13024v1)**  
  Authors: Sampath Rapuri, Lalithkumar Seenivasan, Dominik Schneider, Roger Soberanis-Mukul, Yufan He, Hao Ding, Jiru Xu, Chenhao Yu, Chenyan Jing, Pengfei Guo, Daguang Xu, Mathias Unberath  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.13024v1.pdf)  
  Keywords: temporal consistency, world model, simulation, controllable, diffusion model, video-to-video, dit, video diffusion, trajectory, video generation  
- **[VGGT-World: Transforming VGGT into an Autoregressive Geometry World Model](https://arxiv.org/abs/2603.12655v1)**  
  Authors: Xiangyu Sun, Shijie Wang, Fengyi Zhang, Lin Liu, Caiyan Jia, Ziying Song, Zi Huang, Yadan Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.12655v1.pdf)  
  Keywords: world model, flow matching, dit, efficient, video generation, trajectory, autoregressive  
- **[VQQA: An Agentic Approach for Video Evaluation and Quality Improvement](https://arxiv.org/abs/2603.12310v1)**  
  Authors: Yiwen Song, Tomas Pfister, Yale Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.12310v1.pdf)  
  Keywords: i2v, t2v, dit, efficient, image-to-video, evaluation, text-to-video, video generation  
- **[EVATok: Adaptive Length Video Tokenization for Efficient Visual Autoregressive Generation](https://arxiv.org/abs/2603.12267v1)**  
  Authors: Tianwei Xiong, Jun Hao Liew, Zilong Huang, Zhijie Lin, Jiashi Feng, Xihui Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.12267v1.pdf)  
  Keywords: dit, efficient, autoregressive, video generation  
- **[OmniStream: Mastering Perception, Reconstruction and Action in Continuous Streams](https://arxiv.org/abs/2603.12265v1)**  
  Authors: Yibin Yan, Jilan Xu, Shangzhe Di, Haoning Wu, Weidi Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.12265v1.pdf)  
  Keywords: efficient, physical, evaluation, interactive, streaming, benchmark  
- **[DreamVideo-Omni: Omni-Motion Controlled Multi-Subject Video Customization with Latent Identity Reinforcement Learning](https://arxiv.org/abs/2603.12257v1)**  
  Authors: Yujie Wei, Xinyu Liu, Shiwei Zhang, Hangjie Yuan, Jinbo Xing, Zhekai Chen, Xiang Wang, Haonan Qiu, Rui Zhao, Yutong Feng, Ruihang Chu, Yingya Zhang, Yike Guo, Xihui Liu, Hongming Shan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.12257v1.pdf)  
  Keywords: customization, identity, video synthesis, controllable, diffusion model, dit, video diffusion, motion control, evaluation, dynamics  
- **[ForensicZip: More Tokens are Better but Not Necessary in Forensic Vision-Language Models](https://arxiv.org/abs/2603.12208v1)**  
  Authors: Yingxin Lai, Zitong Yu, Jun Wang, Linlin Shen, Yong Xu, Xiaochun Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.12208v1.pdf)  
  Keywords: acceleration, physical, benchmark  
- **[FlashMotion: Few-Step Controllable Video Generation with Trajectory Guidance](https://arxiv.org/abs/2603.12146v1)**  
  Authors: Quanhao Li, Zhen Xing, Rui Wang, Haidong Cao, Qi Dai, Daoguo Dong, Zuxuan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.12146v1.pdf)  
  Keywords: denoising, controllable, motion control, evaluation, architecture, distillation, video generation, trajectory, benchmark  
- **[Cornserve: A Distributed Serving System for Any-to-Any Multimodal Models](https://arxiv.org/abs/2603.12118v1)**  
  Authors: Jae-Won Chung, Jeff J. Ma, Jisang Ahn, Yizhuo Liang, Akshay Jajoo, Myungjin Lee, Mosharaf Chowdhury  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.12118v1.pdf)  
  Keywords: efficient  

### Audio & Multi-modal

- **[Fuel Gauge: Estimating Chain-of-Thought Length Ahead of Time in Large Multimodal Models](https://arxiv.org/abs/2603.10335v1)**  
  Authors: Yuedong Yang, Xiwen Wei, Mustafa Munir, Radu Marculescu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.10335v1.pdf)  
  Keywords: multi-modal, efficient, benchmark  
- **[ID-LoRA: Identity-Driven Audio-Video Personalization with In-Context LoRA](https://arxiv.org/abs/2603.10256v1)**  
  Authors: Aviad Dahan, Moran Yanuka, Noa Kraicer, Lior Wolf, Raja Giryes  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.10256v1.pdf)  
  Keywords: identity, denoising, personalization, dit, efficient, sound, style, physical, video diffusion  
- **[FetalAgents: A Multi-Agent System for Fetal Ultrasound Image and Video Analysis](https://arxiv.org/abs/2603.09733v1)**  
  Authors: Xiaotian Hu, Junwei Huang, Mingxuan Liu, Kasidit Anmahapong, Yifei Chen, Yitong Luo, Yiming Huang, Xuguang Bai, Zihan Li, Yi Liao, Haibo Qu, Qiyuan Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09733v1.pdf)  
  Keywords: dit, evaluation, sound  
- **[MM-TS: Multi-Modal Temperature and Margin Schedules for Contrastive Learning with Long-Tail Data](https://arxiv.org/abs/2603.08202v1)**  
  Authors: Siarhei Sheludzko, Dhimitrios Duka, Bernt Schiele, Hilde Kuehne, Anna Kukleva  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08202v1.pdf)  
  Keywords: multi-modal, concept, dit  
- **[StreamWise: Serving Multi-Modal Generation in Real-Time at Scale](https://arxiv.org/abs/2603.05800v1)**  
  Authors: Haoran Qiu, Gohar Irfan Chaudhry, Chaojie Zhang, Íñigo Goiri, Esha Choukse, Rodrigo Fonseca, Ricardo Bianchini  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05800v1.pdf)  
  Keywords: multi-modal, efficient, streaming, video generation  
- **[UniTalking: A Unified Audio-Video Framework for Talking Portrait Generation](https://arxiv.org/abs/2603.01418v1)**  
  Authors: Hebeizi Li, Zihao Liang, Benyuan Sun, Zihao Yin, Xiao Sha, Chenliang Wang, Yi Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01418v1.pdf)  
  Keywords: multi-modal, efficient, style, architecture, video generation  
- **[FlowPortrait: Reinforcement Learning for Audio-Driven Portrait Video Generation](https://arxiv.org/abs/2603.00159v1)**  
  Authors: Weiting Tan, Andy T. Liu, Ming Tu, Xinghua Qu, Philipp Koehn, Lu Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.00159v1.pdf)  
  Keywords: temporal consistency, audio-to-video, evaluation, video generation, autoregressive, audio-driven  
- **[SkyReels-V4: Multi-modal Video-Audio Generation, Inpainting and Editing model](https://arxiv.org/abs/2602.21818v2)**  
  Authors: Guibin Chen, Dixuan Lin, Jiangping Yang, Youqiang Zhang, Zhengcong Fei, Debang Li, Sheng Chen, Chaofeng Ao, Nuo Pang, Yiming Wang, Yikun Dou, Zheng Chen, Mingyuan Fan, Tuanhui Li, Mingshan Chang, Hao Zhang, Xiaopeng Sun, Jingtao Xu, Yuqiang Xie, Jiahua Wang, Zhiheng Xu, Weiming Xiong, Yuzhe Jin, Baoxuan Gu, Binjie Mao, Yunjie Yu, Jujie He, Yuhao Feng, Shiwen Tu, Chaojie Wang, Rui Yan, Wei Shen, Jingchen Wu, Peng Zhao, Xuanyue Zhong, Zhuangzhuang Liu, Kaifei Wang, Fuxiang Zhang, Weikai Xu, Wenyan Liu, Binglu Zhang, Yu Shen, Tianhui Xiong, Bin Peng, Liang Zeng, Xuchen Song, Haoxiang Guo, Peiyu Wang, Max W. Y. Lam, Chien-Hung Liu, Yahui Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21818v2.pdf)  
  Keywords: image to video, video editing, multi-modal, frame interpolation, dit, sound, style, architecture, diffusion transformer, super-resolution, video generation  
- **[JavisDiT++: Unified Modeling and Optimization for Joint Audio-Video Generation](https://arxiv.org/abs/2602.19163v1)**  
  Authors: Kai Liu, Yanhao Zheng, Kai Wang, Shengqiong Wu, Rongjunchen Zhang, Jiebo Luo, Dimitrios Hatzinakos, Ziwei Liu, Hao Fei, Tat-Seng Chua  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.19163v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://JavisVerse.github.io/JavisDiT2-page)  
  Keywords: t2v, dit, sound, evaluation, video generation  
- **[EchoTorrent: Towards Swift, Sustained, and Streaming Multi-Modal Video Generation](https://arxiv.org/abs/2602.13669v2)**  
  Authors: Rang Meng, Yingjie Yin, Yuming Li, Chenguang Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.13669v2.pdf)  
  Keywords: temporal consistency, identity, multi-modal, architecture, video generation, streaming, autoregressive  

### Controllable Generation

*Showing the latest 50 out of 110 papers*

- **[SAW: Toward a Surgical Action World Model via Controllable and Scalable Video Generation](https://arxiv.org/abs/2603.13024v1)**  
  Authors: Sampath Rapuri, Lalithkumar Seenivasan, Dominik Schneider, Roger Soberanis-Mukul, Yufan He, Hao Ding, Jiru Xu, Chenhao Yu, Chenyan Jing, Pengfei Guo, Daguang Xu, Mathias Unberath  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.13024v1.pdf)  
  Keywords: temporal consistency, world model, simulation, controllable, diffusion model, video-to-video, dit, video diffusion, trajectory, video generation  
- **[VGGT-World: Transforming VGGT into an Autoregressive Geometry World Model](https://arxiv.org/abs/2603.12655v1)**  
  Authors: Xiangyu Sun, Shijie Wang, Fengyi Zhang, Lin Liu, Caiyan Jia, Ziying Song, Zi Huang, Yadan Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.12655v1.pdf)  
  Keywords: world model, flow matching, dit, efficient, video generation, trajectory, autoregressive  
- **[DreamVideo-Omni: Omni-Motion Controlled Multi-Subject Video Customization with Latent Identity Reinforcement Learning](https://arxiv.org/abs/2603.12257v1)**  
  Authors: Yujie Wei, Xinyu Liu, Shiwei Zhang, Hangjie Yuan, Jinbo Xing, Zhekai Chen, Xiang Wang, Haonan Qiu, Rui Zhao, Yutong Feng, Ruihang Chu, Yingya Zhang, Yike Guo, Xihui Liu, Hongming Shan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.12257v1.pdf)  
  Keywords: customization, identity, video synthesis, controllable, diffusion model, dit, video diffusion, motion control, evaluation, dynamics  
- **[FlashMotion: Few-Step Controllable Video Generation with Trajectory Guidance](https://arxiv.org/abs/2603.12146v1)**  
  Authors: Quanhao Li, Zhen Xing, Rui Wang, Haidong Cao, Qi Dai, Daoguo Dong, Zuxuan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.12146v1.pdf)  
  Keywords: denoising, controllable, motion control, evaluation, architecture, distillation, video generation, trajectory, benchmark  
- **[Controllable Egocentric Video Generation via Occlusion-Aware Sparse 3D Hand Joints](https://arxiv.org/abs/2603.11755v1)**  
  Authors: Chenyangguang Zhang, Botao Ye, Boqi Chen, Alexandros Delitzas, Fangjinhua Wang, Marc Pollefeys, Xi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.11755v1.pdf)  
  Keywords: controllable, efficient, dit, evaluation, video generation, benchmark  
- **[Risk-Controllable Multi-View Diffusion for Driving Scenario Generation](https://arxiv.org/abs/2603.11534v1)**  
  Authors: Hongyi Lin, Wenxiu Shi, Heye Huang, Dingyi Zhuang, Song Zhang, Yang Liu, Xiaobo Qu, Jinhua Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.11534v1.pdf)  
  Keywords: world model, controllable, physical, autonomous driving  
- **[ShotVerse: Advancing Cinematic Camera Control for Text-Driven Multi-Shot Video Creation](https://arxiv.org/abs/2603.11421v1)**  
  Authors: Songlin Yang, Zhe Wang, Xuyi Yang, Songchun Zhang, Xianghao Kong, Taiyi Wu, Xiaotong Zhao, Ran Zhang, Alan Zhao, Anyi Rao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.11421v1.pdf)  
  Keywords: camera control, film, dit, evaluation, text-driven video, trajectory, video generation  
- **[DISPLAY: Directable Human-Object Interaction Video Generation via Sparse Motion Guidance and Multi-Task Auxiliary](https://arxiv.org/abs/2603.09883v1)**  
  Authors: Jiazhi Guan, Quanwei Yang, Luying Huang, Junhao Liang, Borong Liang, Haocheng Feng, Wei He, Kaisiyuan Wang, Hang Zhou, Jingdong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09883v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://mumuwei.github.io/DISPLAY)  
  Keywords: controllable, physical, dit, video generation  
- **[ConfCtrl: Enabling Precise Camera Control in Video Diffusion via Confidence-Aware Interpolation](https://arxiv.org/abs/2603.09819v1)**  
  Authors: Liudi Yang, George Eskandar, Fengyi Shen, Mohammad Altillawi, Yang Bai, Chi Zhang, Ziyuan Liu, Abhinav Valada  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09819v1.pdf)  
  Keywords: video interpolation, camera control, dit, diffusion model, novel view, video diffusion  
- **[HECTOR: Hybrid Editable Compositional Object References for Video Generation](https://arxiv.org/abs/2603.08850v1)**  
  Authors: Guofeng Zhang, Angtian Wang, Jacob Zhiyuan Fang, Liming Jiang, Haotian Yang, Alan Yuille, Chongyang Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08850v1.pdf)  
  Keywords: dit, physical, motion control, trajectory, video generation  

### Human & Character Animation

- **[SoulX-LiveAct: Towards Hour-Scale Real-Time Human Animation with Neighbor Forcing and ConvKV Memory](https://arxiv.org/abs/2603.11746v1)**  
  Authors: Dingcheng Zhen, Xu Zheng, Ruixin Zhang, Zhiqi Jiang, Yichao Yan, Ming Tao, Shunshun Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.11746v1.pdf)  
  Keywords: video synthesis, dit, diffusion model, efficient, video generation, human animation, streaming, autoregressive  
- **[Controllable Complex Human Motion Video Generation via Text-to-Skeleton Cascades](https://arxiv.org/abs/2603.08028v1)**  
  Authors: Ashkan Taghipour, Morteza Ghahremani, Zinuo Li, Hamid Laga, Farid Boussaid, Mohammed Bennamoun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08028v1.pdf)  
  Keywords: temporal consistency, controllable, diffusion model, dit, video diffusion, motion control, human motion, video generation, autoregressive, benchmark  
- **[ArtHOI: Articulated Human-Object Interaction Synthesis by 4D Reconstruction from Video Priors](https://arxiv.org/abs/2603.04338v1)**  
  Authors: Zihao Huang, Tianqi Liu, Zhaoxi Chen, Shaocong Xu, Saining Zhang, Lixing Xiao, Zhiguo Cao, Wei Li, Hao Zhao, Ziwei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.04338v1.pdf)  
  Keywords: dit, physical, diffusion model, video diffusion, human motion  
- **[Direct Reward Fine-Tuning on Poses for Single Image to 3D Human in the Wild](https://arxiv.org/abs/2603.02619v1)**  
  Authors: Seunguk Do, Minwoo Huh, Joonghyuk Shin, Jaesik Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02619v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://seunguk-do.github.io/drpose)  
  Keywords: dit, diffusion model, evaluation, human motion, benchmark  
- **[LiftAvatar: Kinematic-Space Completion for Expression-Controlled 3D Gaussian Avatar Animation](https://arxiv.org/abs/2603.02129v1)**  
  Authors: Hualiang Wei, Shunran Jia, Jialun Liu, Wenhui Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02129v1.pdf)  
  Keywords: controllable, efficient, dit, avatar, video diffusion, distillation, diffusion transformer  
- **[Non-verbal Real-time Human-AI Interaction in Constrained Robotic Environments](https://arxiv.org/abs/2603.01804v1)**  
  Authors: Dragos Costea, Alina Marcu, Cristina Lazar, Marius Leordeanu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01804v1.pdf)  
  Keywords: architecture, body motion, text-to-video  
- **[GeoDiff4D: Geometry-Aware Diffusion for 4D Head Avatar Reconstruction](https://arxiv.org/abs/2602.24161v2)**  
  Authors: Chao Xu, Xiaochen Zhao, Xiang Deng, Jingxiang Sun, Donglin Di, Zhuo Su, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.24161v2.pdf)  
  Keywords: avatar, identity, diffusion model, video generation  
- **[Spatio-Temporal Garment Reconstruction Using Diffusion Mapping via Pattern Coordinates](https://arxiv.org/abs/2602.24043v1)**  
  Authors: Yingxuan You, Ren Li, Corentin Dumery, Cong Cao, Hao Li, Pascal Fua  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.24043v1.pdf)  
  Keywords: temporal consistency, dit, diffusion model, avatar, virtual try-on  
- **[BigMaQ: A Big Macaque Motion and Animation Dataset Bridging Image and 3D Pose Representations](https://arxiv.org/abs/2602.19874v1)**  
  Authors: Lucas Martini, Alexander Lappe, Anna Bognár, Rufin Vogels, Martin A. Giese  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.19874v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://martinivis.github.io/BigMaQ)  
  Keywords: avatar, dynamics, benchmark  
- **[Ani3DHuman: Photorealistic 3D Human Animation with Self-guided Stochastic Sampling](https://arxiv.org/abs/2602.19089v1)**  
  Authors: Qi Sun, Can Wang, Jiaxiang Shang, Yingchun Liu, Jing Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.19089v1.pdf) | [![GitHub](https://img.shields.io/github/stars/qiisun/ani3dhuman?style=social)](https://github.com/qiisun/ani3dhuman)  
  Keywords: identity, diffusion model, video diffusion, human animation, dynamics  

### Image-to-Video Generation

- **[VQQA: An Agentic Approach for Video Evaluation and Quality Improvement](https://arxiv.org/abs/2603.12310v1)**  
  Authors: Yiwen Song, Tomas Pfister, Yale Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.12310v1.pdf)  
  Keywords: i2v, t2v, dit, efficient, image-to-video, evaluation, text-to-video, video generation  
- **[SPIRAL: A Closed-Loop Framework for Self-Improving Action World Models via Reflective Planning Agents](https://arxiv.org/abs/2603.08403v2)**  
  Authors: Yu Yang, Yue Liao, Jianbiao Mei, Baisen Wang, Xuemeng Yang, Licheng Wen, Jiangning Zhang, Xiangtai Li, Hanlin Chen, Botian Shi, Yong Liu, Shuicheng Yan, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08403v2.pdf)  
  Keywords: temporal consistency, world model, i2v, controllable, dit, evaluation, video generation, benchmark  
- **[Pinterest Canvas: Large-Scale Image Generation at Pinterest](https://arxiv.org/abs/2603.06453v1)**  
  Authors: Yu Wang, Eric Tzeng, Raymond Shiau, Jie Yang, Dmitry Kislyuk, Charles Rosenberg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06453v1.pdf)  
  Keywords: dit, diffusion model, image-to-video, outpainting, video generation  
- **[Helios: Real Real-Time Long Video Generation Model](https://arxiv.org/abs/2603.04379v1)**  
  Authors: Shenghai Yuan, Yuanyang Yin, Zongjian Li, Xinwei Huang, Xiao Yang, Li Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.04379v1.pdf)  
  Keywords: i2v, t2v, diffusion model, acceleration, long video, autoregressive, video generation  
- **[FastLightGen: Fast and Light Video Generation with Fewer Steps and Parameters](https://arxiv.org/abs/2603.01685v3)**  
  Authors: Shitong Shao, Yufei Gu, Zeke Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01685v3.pdf)  
  Keywords: efficient, distillation, i2v, video generation  
- **[FREE-Edit: Using Editing-aware Injection in Rectified Flow Models for Zero-shot Image-Driven Video Editing](https://arxiv.org/abs/2603.01164v1)**  
  Authors: Maomao Li, Yunfei Liu, Yu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01164v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://free-edit.github.io/page)  
  Keywords: video editing, layout, i2v, denoising, dit, image-to-video, image-driven, rectified flow  
- **[Let Your Image Move with Your Motion! -- Implicit Multi-Object Multi-Motion Transfer](https://arxiv.org/abs/2603.01000v2)**  
  Authors: Yuze Li, Dong Gong, Xiao Cao, Junchao Yuan, Dongsheng Li, Lei Zhou, Yun Sing Koh, Cheng Yan, Xinyu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01000v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ethan-li123.github.io/FlexiMMT_page)  
  Keywords: i2v, controllable, efficient, image-to-video, video generation  
- **[SkyReels-V4: Multi-modal Video-Audio Generation, Inpainting and Editing model](https://arxiv.org/abs/2602.21818v2)**  
  Authors: Guibin Chen, Dixuan Lin, Jiangping Yang, Youqiang Zhang, Zhengcong Fei, Debang Li, Sheng Chen, Chaofeng Ao, Nuo Pang, Yiming Wang, Yikun Dou, Zheng Chen, Mingyuan Fan, Tuanhui Li, Mingshan Chang, Hao Zhang, Xiaopeng Sun, Jingtao Xu, Yuqiang Xie, Jiahua Wang, Zhiheng Xu, Weiming Xiong, Yuzhe Jin, Baoxuan Gu, Binjie Mao, Yunjie Yu, Jujie He, Yuhao Feng, Shiwen Tu, Chaojie Wang, Rui Yan, Wei Shen, Jingchen Wu, Peng Zhao, Xuanyue Zhong, Zhuangzhuang Liu, Kaifei Wang, Fuxiang Zhang, Weikai Xu, Wenyan Liu, Binglu Zhang, Yu Shen, Tianhui Xiong, Bin Peng, Liang Zeng, Xuchen Song, Haoxiang Guo, Peiyu Wang, Max W. Y. Lam, Chien-Hung Liu, Yahui Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21818v2.pdf)  
  Keywords: image to video, video editing, multi-modal, frame interpolation, dit, sound, style, architecture, diffusion transformer, super-resolution, video generation  
- **[MultiAnimate: Pose-Guided Image Animation Made Extensible](https://arxiv.org/abs/2602.21581v1)**  
  Authors: Yingcheng Hu, Haowen Gong, Chuanguang Yang, Zhulin An, Yongjun Xu, Songhua Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21581v1.pdf)  
  Keywords: identity, dit, pose-guided, image animation, diffusion transformer, video generation  
- **[Human Video Generation from a Single Image with 3D Pose and View Control](https://arxiv.org/abs/2602.21188v1)**  
  Authors: Tiantian Wang, Chun-Han Yao, Tao Hu, Mallikarjun Byrasandra Ramalinga Reddy, Ming-Hsuan Yang, Varun Jampani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21188v1.pdf)  
  Keywords: video synthesis, diffusion model, image-to-video, latent video, video diffusion, video generation  

### Long Video Generation

*Showing the latest 50 out of 125 papers*

- **[SAW: Toward a Surgical Action World Model via Controllable and Scalable Video Generation](https://arxiv.org/abs/2603.13024v1)**  
  Authors: Sampath Rapuri, Lalithkumar Seenivasan, Dominik Schneider, Roger Soberanis-Mukul, Yufan He, Hao Ding, Jiru Xu, Chenhao Yu, Chenyan Jing, Pengfei Guo, Daguang Xu, Mathias Unberath  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.13024v1.pdf)  
  Keywords: temporal consistency, world model, simulation, controllable, diffusion model, video-to-video, dit, video diffusion, trajectory, video generation  
- **[VGGT-World: Transforming VGGT into an Autoregressive Geometry World Model](https://arxiv.org/abs/2603.12655v1)**  
  Authors: Xiangyu Sun, Shijie Wang, Fengyi Zhang, Lin Liu, Caiyan Jia, Ziying Song, Zi Huang, Yadan Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.12655v1.pdf)  
  Keywords: world model, flow matching, dit, efficient, video generation, trajectory, autoregressive  
- **[MemRoPE: Training-Free Infinite Video Generation via Evolving Memory Tokens](https://arxiv.org/abs/2603.12513v1)**  
  Authors: Youngrae Kim, Qixin Hu, C. -C. Jay Kuo, Peter A. Beerel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.12513v1.pdf)  
  Keywords: identity, video generation, autoregressive, streaming, dynamics  
- **[EVATok: Adaptive Length Video Tokenization for Efficient Visual Autoregressive Generation](https://arxiv.org/abs/2603.12267v1)**  
  Authors: Tianwei Xiong, Jun Hao Liew, Zilong Huang, Zhijie Lin, Jiashi Feng, Xihui Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.12267v1.pdf)  
  Keywords: dit, efficient, autoregressive, video generation  
- **[OmniStream: Mastering Perception, Reconstruction and Action in Continuous Streams](https://arxiv.org/abs/2603.12265v1)**  
  Authors: Yibin Yan, Jilan Xu, Shangzhe Di, Haoning Wu, Weidi Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.12265v1.pdf)  
  Keywords: efficient, physical, evaluation, interactive, streaming, benchmark  
- **[HomeSafe-Bench: Evaluating Vision-Language Models on Unsafe Action Detection for Embodied Agents in Household Scenarios](https://arxiv.org/abs/2603.11975v2)**  
  Authors: Jiayue Pu, Zhongxiang Sun, Zilu Zhang, Xiao Zhang, Jun Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.11975v2.pdf)  
  Keywords: simulation, physical, evaluation, architecture, physical simulation, video generation, streaming, benchmark  
- **[SoulX-LiveAct: Towards Hour-Scale Real-Time Human Animation with Neighbor Forcing and ConvKV Memory](https://arxiv.org/abs/2603.11746v1)**  
  Authors: Dingcheng Zhen, Xu Zheng, Ruixin Zhang, Zhiqi Jiang, Yichao Yan, Ming Tao, Shunshun Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.11746v1.pdf)  
  Keywords: video synthesis, dit, diffusion model, efficient, video generation, human animation, streaming, autoregressive  
- **[Streaming Autoregressive Video Generation via Diagonal Distillation](https://arxiv.org/abs/2603.09488v2)**  
  Authors: Jinxiu Liu, Xuanming Liu, Kangfu Mei, Yandong Wen, Ming-Hsuan Yang, Weiyang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09488v2.pdf)  
  Keywords: video synthesis, denoising, dit, diffusion model, efficient, distillation, video generation, streaming, autoregressive  
- **[HiAR: Efficient Autoregressive Long Video Generation via Hierarchical Denoising](https://arxiv.org/abs/2603.08703v1)**  
  Authors: Kai Zou, Dian Zheng, Hongbo Liu, Tiankai Hang, Bin Liu, Nenghai Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08703v1.pdf)  
  Keywords: temporal consistency, denoising, dit, diffusion model, efficient, long video, distillation, video generation, autoregressive  
- **[CAST: Modeling Visual State Transitions for Consistent Video Retrieval](https://arxiv.org/abs/2603.08648v1)**  
  Authors: Yanqing Liu, Yingcheng Liu, Fanghong Dong, Budianto Budianto, Cihang Xie, Yan Jiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08648v1.pdf)  
  Keywords: identity, dit, long-form, video generation, benchmark  

### Personalization & Customization

*Showing the latest 50 out of 91 papers*

- **[MemRoPE: Training-Free Infinite Video Generation via Evolving Memory Tokens](https://arxiv.org/abs/2603.12513v1)**  
  Authors: Youngrae Kim, Qixin Hu, C. -C. Jay Kuo, Peter A. Beerel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.12513v1.pdf)  
  Keywords: identity, video generation, autoregressive, streaming, dynamics  
- **[DreamVideo-Omni: Omni-Motion Controlled Multi-Subject Video Customization with Latent Identity Reinforcement Learning](https://arxiv.org/abs/2603.12257v1)**  
  Authors: Yujie Wei, Xinyu Liu, Shiwei Zhang, Hangjie Yuan, Jinbo Xing, Zhekai Chen, Xiang Wang, Haonan Qiu, Rui Zhao, Yutong Feng, Ruihang Chu, Yingya Zhang, Yike Guo, Xihui Liu, Hongming Shan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.12257v1.pdf)  
  Keywords: customization, identity, video synthesis, controllable, diffusion model, dit, video diffusion, motion control, evaluation, dynamics  
- **[ID-LoRA: Identity-Driven Audio-Video Personalization with In-Context LoRA](https://arxiv.org/abs/2603.10256v1)**  
  Authors: Aviad Dahan, Moran Yanuka, Noa Kraicer, Lior Wolf, Raja Giryes  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.10256v1.pdf)  
  Keywords: identity, denoising, personalization, dit, efficient, sound, style, physical, video diffusion  
- **[Prune Redundancy, Preserve Essence: Vision Token Compression in VLMs via Synergistic Importance-Diversity](https://arxiv.org/abs/2603.09480v2)**  
  Authors: Zhengyao Fang, Pengyuan Lyu, Chengquan Zhang, Guangming Lu, Jun Yu, Wenjie Pei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09480v2.pdf) | [![GitHub](https://img.shields.io/github/stars/ZhengyaoFang/PruneSID?style=social)](https://github.com/ZhengyaoFang/PruneSID)  
  Keywords: concept, dit  
- **[Chain of Event-Centric Causal Thought for Physically Plausible Video Generation](https://arxiv.org/abs/2603.09094v1)**  
  Authors: Zixuan Wang, Yixin Hu, Haolan Wang, Feng Chen, Yan Liu, Wen Li, Yinjie Lei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09094v1.pdf)  
  Keywords: dit, diffusion model, physical, video diffusion, physics, interactive, video generation, concept, benchmark  
- **[CAST: Modeling Visual State Transitions for Consistent Video Retrieval](https://arxiv.org/abs/2603.08648v1)**  
  Authors: Yanqing Liu, Yingcheng Liu, Fanghong Dong, Budianto Budianto, Cihang Xie, Yan Jiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08648v1.pdf)  
  Keywords: identity, dit, long-form, video generation, benchmark  
- **[Video2LoRA: Unified Semantic-Controlled Video Generation via Per-Reference-Video LoRA](https://arxiv.org/abs/2603.08210v2)**  
  Authors: Zexi Wu, Qinghe Wang, Jing Dai, Baolu Li, Yiming Zhang, Yue Ma, Xu Jia, Hongming Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08210v2.pdf)  
  Keywords: dit, efficient, style, video generation  
- **[MM-TS: Multi-Modal Temperature and Margin Schedules for Contrastive Learning with Long-Tail Data](https://arxiv.org/abs/2603.08202v1)**  
  Authors: Siarhei Sheludzko, Dhimitrios Duka, Bernt Schiele, Hilde Kuehne, Anna Kukleva  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08202v1.pdf)  
  Keywords: multi-modal, concept, dit  
- **[GenHOI: Towards Object-Consistent Hand-Object Interaction with Temporally Balanced and Spatially Selective Object Injection](https://arxiv.org/abs/2603.06048v1)**  
  Authors: Xuan Huang, Mochu Xiang, Zhelun Shen, Jinbo Wu, Chenming Wu, Chen Zhao, Kaisiyuan Wang, Hang Zhou, Shanshan Liu, Haocheng Feng, Wei He, Jingdong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06048v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xuanhuang0.github.io/GenHOI)  
  Keywords: video editing, identity, video synthesis, dit, physical, evaluation, video generation  
- **[FaceCam: Portrait Video Camera Control via Scale-Aware Conditioning](https://arxiv.org/abs/2603.05506v1)**  
  Authors: Weijie Lyu, Ming-Hsuan Yang, Zhixin Shu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05506v1.pdf)  
  Keywords: identity, dit, camera control, video generation  

### Physical Understanding

*Showing the latest 50 out of 134 papers*

- **[MemRoPE: Training-Free Infinite Video Generation via Evolving Memory Tokens](https://arxiv.org/abs/2603.12513v1)**  
  Authors: Youngrae Kim, Qixin Hu, C. -C. Jay Kuo, Peter A. Beerel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.12513v1.pdf)  
  Keywords: identity, video generation, autoregressive, streaming, dynamics  
- **[OmniStream: Mastering Perception, Reconstruction and Action in Continuous Streams](https://arxiv.org/abs/2603.12265v1)**  
  Authors: Yibin Yan, Jilan Xu, Shangzhe Di, Haoning Wu, Weidi Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.12265v1.pdf)  
  Keywords: efficient, physical, evaluation, interactive, streaming, benchmark  
- **[DreamVideo-Omni: Omni-Motion Controlled Multi-Subject Video Customization with Latent Identity Reinforcement Learning](https://arxiv.org/abs/2603.12257v1)**  
  Authors: Yujie Wei, Xinyu Liu, Shiwei Zhang, Hangjie Yuan, Jinbo Xing, Zhekai Chen, Xiang Wang, Haonan Qiu, Rui Zhao, Yutong Feng, Ruihang Chu, Yingya Zhang, Yike Guo, Xihui Liu, Hongming Shan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.12257v1.pdf)  
  Keywords: customization, identity, video synthesis, controllable, diffusion model, dit, video diffusion, motion control, evaluation, dynamics  
- **[ForensicZip: More Tokens are Better but Not Necessary in Forensic Vision-Language Models](https://arxiv.org/abs/2603.12208v1)**  
  Authors: Yingxin Lai, Zitong Yu, Jun Wang, Linlin Shen, Yong Xu, Xiaochun Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.12208v1.pdf)  
  Keywords: acceleration, physical, benchmark  
- **[HomeSafe-Bench: Evaluating Vision-Language Models on Unsafe Action Detection for Embodied Agents in Household Scenarios](https://arxiv.org/abs/2603.11975v2)**  
  Authors: Jiayue Pu, Zhongxiang Sun, Zilu Zhang, Xiao Zhang, Jun Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.11975v2.pdf)  
  Keywords: simulation, physical, evaluation, architecture, physical simulation, video generation, streaming, benchmark  
- **[OSCBench: Benchmarking Object State Change in Text-to-Video Generation](https://arxiv.org/abs/2603.11698v1)**  
  Authors: Xianjing Han, Bin Zhu, Shiqi Hu, Franklin Mingzhe Li, Patrick Carrington, Roger Zimmermann, Jingjing Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.11698v1.pdf)  
  Keywords: t2v, physical, evaluation, video generation, text-to-video, benchmark  
- **[Risk-Controllable Multi-View Diffusion for Driving Scenario Generation](https://arxiv.org/abs/2603.11534v1)**  
  Authors: Hongyi Lin, Wenxiu Shi, Heye Huang, Dingyi Zhuang, Song Zhang, Yang Liu, Xiaobo Qu, Jinhua Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.11534v1.pdf)  
  Keywords: world model, controllable, physical, autonomous driving  
- **[World2Act: Latent Action Post-Training via Skill-Compositional World Models](https://arxiv.org/abs/2603.10422v1)**  
  Authors: An Dinh Vuong, Tuan Van Vo, Abdullah Sohail, Haoran Ding, Liang Ma, Xiaodan Liang, Anqing Duan, Ivan Laptev, Ian Reid  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.10422v1.pdf)  
  Keywords: world model, dynamics, video generation  
- **[Motion Forcing: A Decoupled Framework for Robust Video Generation in Motion Dynamics](https://arxiv.org/abs/2603.10408v1)**  
  Authors: Tianshuo Xu, Zhifei Chen, Leyi Wu, Hao Lu, Ying-cong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.10408v1.pdf)  
  Keywords: dynamics, physical, robotics, autonomous driving, physics, evaluation, video generation, benchmark  
- **[ID-LoRA: Identity-Driven Audio-Video Personalization with In-Context LoRA](https://arxiv.org/abs/2603.10256v1)**  
  Authors: Aviad Dahan, Moran Yanuka, Noa Kraicer, Lior Wolf, Raja Giryes  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.10256v1.pdf)  
  Keywords: identity, denoising, personalization, dit, efficient, sound, style, physical, video diffusion  

### Surveys & Benchmarks

*Showing the latest 50 out of 201 papers*

- **[VQQA: An Agentic Approach for Video Evaluation and Quality Improvement](https://arxiv.org/abs/2603.12310v1)**  
  Authors: Yiwen Song, Tomas Pfister, Yale Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.12310v1.pdf)  
  Keywords: i2v, t2v, dit, efficient, image-to-video, evaluation, text-to-video, video generation  
- **[OmniStream: Mastering Perception, Reconstruction and Action in Continuous Streams](https://arxiv.org/abs/2603.12265v1)**  
  Authors: Yibin Yan, Jilan Xu, Shangzhe Di, Haoning Wu, Weidi Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.12265v1.pdf)  
  Keywords: efficient, physical, evaluation, interactive, streaming, benchmark  
- **[DreamVideo-Omni: Omni-Motion Controlled Multi-Subject Video Customization with Latent Identity Reinforcement Learning](https://arxiv.org/abs/2603.12257v1)**  
  Authors: Yujie Wei, Xinyu Liu, Shiwei Zhang, Hangjie Yuan, Jinbo Xing, Zhekai Chen, Xiang Wang, Haonan Qiu, Rui Zhao, Yutong Feng, Ruihang Chu, Yingya Zhang, Yike Guo, Xihui Liu, Hongming Shan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.12257v1.pdf)  
  Keywords: customization, identity, video synthesis, controllable, diffusion model, dit, video diffusion, motion control, evaluation, dynamics  
- **[DVD: Deterministic Video Depth Estimation with Generative Priors](https://arxiv.org/abs/2603.12250v1)**  
  Authors: Hongfei Zhang, Harold Haodong Chen, Chenfei Liao, Jing He, Zixin Zhang, Haodong Li, Yihao Liang, Kanghao Chen, Bin Ren, Xu Zheng, Shuai Yang, Kun Zhou, Yinchuan Li, Nicu Sebe, Ying-Cong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.12250v1.pdf)  
  Keywords: video diffusion, diffusion model, benchmark  
- **[ForensicZip: More Tokens are Better but Not Necessary in Forensic Vision-Language Models](https://arxiv.org/abs/2603.12208v1)**  
  Authors: Yingxin Lai, Zitong Yu, Jun Wang, Linlin Shen, Yong Xu, Xiaochun Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.12208v1.pdf)  
  Keywords: acceleration, physical, benchmark  
- **[FlashMotion: Few-Step Controllable Video Generation with Trajectory Guidance](https://arxiv.org/abs/2603.12146v1)**  
  Authors: Quanhao Li, Zhen Xing, Rui Wang, Haidong Cao, Qi Dai, Daoguo Dong, Zuxuan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.12146v1.pdf)  
  Keywords: denoising, controllable, motion control, evaluation, architecture, distillation, video generation, trajectory, benchmark  
- **[HomeSafe-Bench: Evaluating Vision-Language Models on Unsafe Action Detection for Embodied Agents in Household Scenarios](https://arxiv.org/abs/2603.11975v2)**  
  Authors: Jiayue Pu, Zhongxiang Sun, Zilu Zhang, Xiao Zhang, Jun Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.11975v2.pdf)  
  Keywords: simulation, physical, evaluation, architecture, physical simulation, video generation, streaming, benchmark  
- **[Controllable Egocentric Video Generation via Occlusion-Aware Sparse 3D Hand Joints](https://arxiv.org/abs/2603.11755v1)**  
  Authors: Chenyangguang Zhang, Botao Ye, Boqi Chen, Alexandros Delitzas, Fangjinhua Wang, Marc Pollefeys, Xi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.11755v1.pdf)  
  Keywords: controllable, efficient, dit, evaluation, video generation, benchmark  
- **[OSCBench: Benchmarking Object State Change in Text-to-Video Generation](https://arxiv.org/abs/2603.11698v1)**  
  Authors: Xianjing Han, Bin Zhu, Shiqi Hu, Franklin Mingzhe Li, Patrick Carrington, Roger Zimmermann, Jingjing Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.11698v1.pdf)  
  Keywords: t2v, physical, evaluation, video generation, text-to-video, benchmark  
- **[ShotVerse: Advancing Cinematic Camera Control for Text-Driven Multi-Shot Video Creation](https://arxiv.org/abs/2603.11421v1)**  
  Authors: Songlin Yang, Zhe Wang, Xuyi Yang, Songchun Zhang, Xianghao Kong, Taiyi Wu, Xiaotong Zhao, Ran Zhang, Alan Zhao, Anyi Rao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.11421v1.pdf)  
  Keywords: camera control, film, dit, evaluation, text-driven video, trajectory, video generation  

### Text-to-Video Generation

*Showing the latest 50 out of 71 papers*

- **[VQQA: An Agentic Approach for Video Evaluation and Quality Improvement](https://arxiv.org/abs/2603.12310v1)**  
  Authors: Yiwen Song, Tomas Pfister, Yale Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.12310v1.pdf)  
  Keywords: i2v, t2v, dit, efficient, image-to-video, evaluation, text-to-video, video generation  
- **[OSCBench: Benchmarking Object State Change in Text-to-Video Generation](https://arxiv.org/abs/2603.11698v1)**  
  Authors: Xianjing Han, Bin Zhu, Shiqi Hu, Franklin Mingzhe Li, Patrick Carrington, Roger Zimmermann, Jingjing Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.11698v1.pdf)  
  Keywords: t2v, physical, evaluation, video generation, text-to-video, benchmark  
- **[ShotVerse: Advancing Cinematic Camera Control for Text-Driven Multi-Shot Video Creation](https://arxiv.org/abs/2603.11421v1)**  
  Authors: Songlin Yang, Zhe Wang, Xuyi Yang, Songchun Zhang, Xianghao Kong, Taiyi Wu, Xiaotong Zhao, Ran Zhang, Alan Zhao, Anyi Rao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.11421v1.pdf)  
  Keywords: camera control, film, dit, evaluation, text-driven video, trajectory, video generation  
- **[VIVECaption: A Split Approach to Caption Quality Improvement](https://arxiv.org/abs/2603.07401v1)**  
  Authors: Varun Ananth, Baqiao Liu, Haoran Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.07401v1.pdf)  
  Keywords: t2v, evaluation, text-to-video  
- **[Two Frames Matter: A Temporal Attack for Text-to-Video Model Jailbreaking](https://arxiv.org/abs/2603.07028v1)**  
  Authors: Moyang Chen, Zonghao Ying, Wenzhuo Xu, Quancheng Zou, Deyue Zhang, Dongdong Yang, Xiangzheng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.07028v1.pdf)  
  Keywords: t2v, dit, evaluation, trajectory, text-to-video  
- **[NEGATE: Constrained Semantic Guidance for Linguistic Negation in Text-to-Video Diffusion](https://arxiv.org/abs/2603.06533v1)**  
  Authors: Taewon Kang, Ming C. Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06533v1.pdf)  
  Keywords: dit, dynamics, video diffusion, evaluation, text-to-video, benchmark  
- **[Accelerating Text-to-Video Generation with Calibrated Sparse Attention](https://arxiv.org/abs/2603.05503v1)**  
  Authors: Shai Yehezkel, Shahar Yadin, Noam Elata, Yaron Ostrovsky-Berman, Bahjat Kawar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05503v1.pdf)  
  Keywords: efficient, diffusion model, text-to-video, video generation  
- **[Helios: Real Real-Time Long Video Generation Model](https://arxiv.org/abs/2603.04379v1)**  
  Authors: Shenghai Yuan, Yuanyang Yin, Zongjian Li, Xinwei Huang, Xiao Yang, Li Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.04379v1.pdf)  
  Keywords: i2v, t2v, diffusion model, acceleration, long video, autoregressive, video generation  
- **[PhyPrompt: RL-based Prompt Refinement for Physically Plausible Text-to-Video Generation](https://arxiv.org/abs/2603.03505v1)**  
  Authors: Shang Wu, Chenwei Xu, Zhuofan Xia, Weijian Li, Lie Lu, Pranav Maneriker, Fan Du, Manling Li, Han Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.03505v1.pdf)  
  Keywords: t2v, physical, physics, architecture, text-to-video, physics-aware, video generation  
- **[EduVQA: Benchmarking AI-Generated Video Quality Assessment for Education](https://arxiv.org/abs/2603.03066v1)**  
  Authors: Baoliang Chen, Xinlong Bu, Lingyu Zhu, Hanwei Zhu, Xiangjie Sui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.03066v1.pdf)  
  Keywords: t2v, education, evaluation, concept, text-to-video, benchmark  

### Video Editing

- **[SAW: Toward a Surgical Action World Model via Controllable and Scalable Video Generation](https://arxiv.org/abs/2603.13024v1)**  
  Authors: Sampath Rapuri, Lalithkumar Seenivasan, Dominik Schneider, Roger Soberanis-Mukul, Yufan He, Hao Ding, Jiru Xu, Chenhao Yu, Chenyan Jing, Pengfei Guo, Daguang Xu, Mathias Unberath  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.13024v1.pdf)  
  Keywords: temporal consistency, world model, simulation, controllable, diffusion model, video-to-video, dit, video diffusion, trajectory, video generation  
- **[When to Lock Attention: Training-Free KV Control in Video Diffusion](https://arxiv.org/abs/2603.09657v1)**  
  Authors: Tianyi Zeng, Jincheng Gao, Tianyi Wang, Zijie Meng, Miao Zhang, Jun Yin, Haoyuan Sun, Junfeng Jiao, Christian Claudel, Junbo Tan, Xueqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09657v1.pdf)  
  Keywords: video editing, denoising, dit, diffusion model, video diffusion  
- **[Place-it-R1: Unlocking Environment-aware Reasoning Potential of MLLM for Video Object Insertion](https://arxiv.org/abs/2603.06140v1)**  
  Authors: Bohai Gu, Taiyi Wu, Dazhao Du, Jian Liu, Shuai Yang, Xiaotong Zhao, Alan Zhao, Song Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06140v1.pdf)  
  Keywords: video editing, dit, physical, diffusion model, video diffusion  
- **[GenHOI: Towards Object-Consistent Hand-Object Interaction with Temporally Balanced and Spatially Selective Object Injection](https://arxiv.org/abs/2603.06048v1)**  
  Authors: Xuan Huang, Mochu Xiang, Zhelun Shen, Jinbo Wu, Chenming Wu, Chen Zhao, Kaisiyuan Wang, Hang Zhou, Shanshan Liu, Haocheng Feng, Wei He, Jingdong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06048v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xuanhuang0.github.io/GenHOI)  
  Keywords: video editing, identity, video synthesis, dit, physical, evaluation, video generation  
- **[Training-free Latent Inter-Frame Pruning with Attention Recovery](https://arxiv.org/abs/2603.05811v1)**  
  Authors: Dennis Menn, Yuedong Yang, Bokun Wang, Xiwen Wei, Mustafa Munir, Feng Liang, Radu Marculescu, Chenfeng Xu, Diana Marculescu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05811v1.pdf)  
  Keywords: video editing, dit, video generation  
- **[FREE-Edit: Using Editing-aware Injection in Rectified Flow Models for Zero-shot Image-Driven Video Editing](https://arxiv.org/abs/2603.01164v1)**  
  Authors: Maomao Li, Yunfei Liu, Yu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01164v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://free-edit.github.io/page)  
  Keywords: video editing, layout, i2v, denoising, dit, image-to-video, image-driven, rectified flow  
- **[UniVBench: Towards Unified Evaluation for Video Foundation Models](https://arxiv.org/abs/2602.21835v2)**  
  Authors: Jianhui Wei, Xiaotian Zhang, Yichen Li, Yuan Wang, Yan Zhang, Ziyi Chen, Zhihang Tang, Wei Xu, Zuozhu Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21835v2.pdf)  
  Keywords: video editing, dit, evaluation, video generation, benchmark  
- **[SkyReels-V4: Multi-modal Video-Audio Generation, Inpainting and Editing model](https://arxiv.org/abs/2602.21818v2)**  
  Authors: Guibin Chen, Dixuan Lin, Jiangping Yang, Youqiang Zhang, Zhengcong Fei, Debang Li, Sheng Chen, Chaofeng Ao, Nuo Pang, Yiming Wang, Yikun Dou, Zheng Chen, Mingyuan Fan, Tuanhui Li, Mingshan Chang, Hao Zhang, Xiaopeng Sun, Jingtao Xu, Yuqiang Xie, Jiahua Wang, Zhiheng Xu, Weiming Xiong, Yuzhe Jin, Baoxuan Gu, Binjie Mao, Yunjie Yu, Jujie He, Yuhao Feng, Shiwen Tu, Chaojie Wang, Rui Yan, Wei Shen, Jingchen Wu, Peng Zhao, Xuanyue Zhong, Zhuangzhuang Liu, Kaifei Wang, Fuxiang Zhang, Weikai Xu, Wenyan Liu, Binglu Zhang, Yu Shen, Tianhui Xiong, Bin Peng, Liang Zeng, Xuchen Song, Haoxiang Guo, Peiyu Wang, Max W. Y. Lam, Chien-Hung Liu, Yahui Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21818v2.pdf)  
  Keywords: image to video, video editing, multi-modal, frame interpolation, dit, sound, style, architecture, diffusion transformer, super-resolution, video generation  
- **[GA-Drive: Geometry-Appearance Decoupled Modeling for Free-viewpoint Driving Scene Generation](https://arxiv.org/abs/2602.20673v2)**  
  Authors: Hao Zhang, Lue Fan, Qitai Wang, Wenbo Li, Zehuan Wu, Lewei Lu, Zhaoxiang Zhang, Hongsheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20673v2.pdf)  
  Keywords: video editing, simulation, dit, diffusion model, video-to-video, autonomous driving, video diffusion, trajectory  
- **[PropFly: Learning to Propagate via On-the-Fly Supervision from Pre-trained Video Diffusion Models](https://arxiv.org/abs/2602.20583v1)**  
  Authors: Wonyong Seo, Jaeho Moon, Jaehyup Lee, Soo Ye Kim, Munchurl Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20583v1.pdf)  
  Keywords: video editing, flow matching, dit, diffusion model, video diffusion  

### Video Inpainting & Completion

- **[ConfCtrl: Enabling Precise Camera Control in Video Diffusion via Confidence-Aware Interpolation](https://arxiv.org/abs/2603.09819v1)**  
  Authors: Liudi Yang, George Eskandar, Fengyi Shen, Mohammad Altillawi, Yang Bai, Chi Zhang, Ziyuan Liu, Abhinav Valada  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09819v1.pdf)  
  Keywords: video interpolation, camera control, dit, diffusion model, novel view, video diffusion  
- **[Pinterest Canvas: Large-Scale Image Generation at Pinterest](https://arxiv.org/abs/2603.06453v1)**  
  Authors: Yu Wang, Eric Tzeng, Raymond Shiau, Jie Yang, Dmitry Kislyuk, Charles Rosenberg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06453v1.pdf)  
  Keywords: dit, diffusion model, image-to-video, outpainting, video generation  
- **[Learning Physics-Grounded 4D Dynamics with Neural Gaussian Force Fields](https://arxiv.org/abs/2602.00148v2)**  
  Authors: Shiqian Li, Ruihong Shen, Junfeng Ni, Chang Pan, Chi Zhang, Yixin Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.00148v2.pdf)  
  Keywords: world model, simulation, dynamics, physical, video prediction, physics, evaluation, interactive, video generation  
- **[DriveLaW:Unifying Planning and Video Generation in a Latent Driving World](https://arxiv.org/abs/2512.23421v2)**  
  Authors: Tianze Xia, Yongkang Li, Lijun Zhou, Jingfeng Yao, Kaixin Xiong, Haiyang Sun, Bing Wang, Kun Ma, Guang Chen, Hangjun Ye, Wenyu Liu, Xinggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.23421v2.pdf)  
  Keywords: world model, autonomous driving, video prediction, video generation, architecture, trajectory, benchmark  
- **[Autoregressive Flow Matching for Motion Prediction](https://arxiv.org/abs/2512.22688v1)**  
  Authors: Johnathan Xie, Stefan Stojanov, Cristobal Eyzaguirre, Daniel L. K. Yamins, Jiajun Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.22688v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Johnathan-Xie/arfm-motion-prediction?style=social)](https://github.com/Johnathan-Xie/arfm-motion-prediction)  
  Keywords: flow matching, dit, robotics, video prediction, human motion, video generation, autoregressive, benchmark  
- **[Over++: Generative Video Compositing for Layer Interaction Effects](https://arxiv.org/abs/2512.19661v1)**  
  Authors: Luchao Qi, Jiaye Wu, Jun Myeong Choi, Cary Phillips, Roni Sengupta, Dan B Goldman  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.19661v1.pdf)  
  Keywords: dit, video inpainting  
- **[Vidarc: Embodied Video Diffusion Model for Closed-loop Control](https://arxiv.org/abs/2512.17661v1)**  
  Authors: Yao Feng, Chendong Xiang, Xinyi Mao, Hengkai Tan, Zuyue Zhang, Shuhe Huang, Kaiwen Zheng, Haitian Liu, Hang Su, Jun Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.17661v1.pdf)  
  Keywords: dynamics, physical, diffusion model, video prediction, video diffusion, autoregressive  

### Video Super-Resolution & Enhancement

*Showing the latest 50 out of 53 papers*

- **[FlashMotion: Few-Step Controllable Video Generation with Trajectory Guidance](https://arxiv.org/abs/2603.12146v1)**  
  Authors: Quanhao Li, Zhen Xing, Rui Wang, Haidong Cao, Qi Dai, Daoguo Dong, Zuxuan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.12146v1.pdf)  
  Keywords: denoising, controllable, motion control, evaluation, architecture, distillation, video generation, trajectory, benchmark  
- **[ID-LoRA: Identity-Driven Audio-Video Personalization with In-Context LoRA](https://arxiv.org/abs/2603.10256v1)**  
  Authors: Aviad Dahan, Moran Yanuka, Noa Kraicer, Lior Wolf, Raja Giryes  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.10256v1.pdf)  
  Keywords: identity, denoising, personalization, dit, efficient, sound, style, physical, video diffusion  
- **[When to Lock Attention: Training-Free KV Control in Video Diffusion](https://arxiv.org/abs/2603.09657v1)**  
  Authors: Tianyi Zeng, Jincheng Gao, Tianyi Wang, Zijie Meng, Miao Zhang, Jun Yin, Haoyuan Sun, Junfeng Jiao, Christian Claudel, Junbo Tan, Xueqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09657v1.pdf)  
  Keywords: video editing, denoising, dit, diffusion model, video diffusion  
- **[Streaming Autoregressive Video Generation via Diagonal Distillation](https://arxiv.org/abs/2603.09488v2)**  
  Authors: Jinxiu Liu, Xuanming Liu, Kangfu Mei, Yandong Wen, Ming-Hsuan Yang, Weiyang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09488v2.pdf)  
  Keywords: video synthesis, denoising, dit, diffusion model, efficient, distillation, video generation, streaming, autoregressive  
- **[HiAR: Efficient Autoregressive Long Video Generation via Hierarchical Denoising](https://arxiv.org/abs/2603.08703v1)**  
  Authors: Kai Zou, Dian Zheng, Hongbo Liu, Tiankai Hang, Bin Liu, Nenghai Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08703v1.pdf)  
  Keywords: temporal consistency, denoising, dit, diffusion model, efficient, long video, distillation, video generation, autoregressive  
- **[Cross-Resolution Distribution Matching for Diffusion Distillation](https://arxiv.org/abs/2603.06136v1)**  
  Authors: Feiyang Chen, Hongpeng Pan, Haonan Xu, Xinyu Duan, Yang Yang, Zhefeng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06136v1.pdf)  
  Keywords: dit, distillation, denoising, video generation  
- **[Frequency-Aware Error-Bounded Caching for Accelerating Diffusion Transformers](https://arxiv.org/abs/2603.05315v1)**  
  Authors: Guandong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05315v1.pdf)  
  Keywords: denoising, dit, dynamics, architecture, trajectory, diffusion transformer, video generation  
- **[FC-VFI: Faithful and Consistent Video Frame Interpolation for High-FPS Slow Motion Video Generation](https://arxiv.org/abs/2603.04899v1)**  
  Authors: Ganggui Ding, Hao Chen, Xiaogang Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.04899v1.pdf)  
  Keywords: temporal consistency, frame interpolation, diffusion model, video diffusion, motion control, video generation  
- **[CubeComposer: Spatio-Temporal Autoregressive 4K 360° Video Generation from Perspective Video](https://arxiv.org/abs/2603.04291v1)**  
  Authors: Lingen Li, Guangzhi Wang, Xiaoyu Li, Zhaoyang Zhang, Qi Dou, Jinwei Gu, Tianfan Xue, Ying Shan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.04291v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lg-li.github.io/project/cubecomposer)  
  Keywords: diffusion model, video generation, autoregressive, super-resolution, benchmark  
- **[TC-Padé: Trajectory-Consistent Padé Approximation for Diffusion Acceleration](https://arxiv.org/abs/2603.02943v1)**  
  Authors: Benlei Cui, Shaoxuan He, Bukun Huang, Zhizeng Ye, Yunyun Sun, Longtao Huang, Hui Xue, Yang Yang, Jingqun Tang, Zhou Zhao, Haiwen Hong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02943v1.pdf)  
  Keywords: denoising, dit, efficient, diffusion model, dynamics, acceleration, trajectory, video generation  

### World Models & Simulation

*Showing the latest 50 out of 93 papers*

- **[SAW: Toward a Surgical Action World Model via Controllable and Scalable Video Generation](https://arxiv.org/abs/2603.13024v1)**  
  Authors: Sampath Rapuri, Lalithkumar Seenivasan, Dominik Schneider, Roger Soberanis-Mukul, Yufan He, Hao Ding, Jiru Xu, Chenhao Yu, Chenyan Jing, Pengfei Guo, Daguang Xu, Mathias Unberath  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.13024v1.pdf)  
  Keywords: temporal consistency, world model, simulation, controllable, diffusion model, video-to-video, dit, video diffusion, trajectory, video generation  
- **[VGGT-World: Transforming VGGT into an Autoregressive Geometry World Model](https://arxiv.org/abs/2603.12655v1)**  
  Authors: Xiangyu Sun, Shijie Wang, Fengyi Zhang, Lin Liu, Caiyan Jia, Ziying Song, Zi Huang, Yadan Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.12655v1.pdf)  
  Keywords: world model, flow matching, dit, efficient, video generation, trajectory, autoregressive  
- **[OmniStream: Mastering Perception, Reconstruction and Action in Continuous Streams](https://arxiv.org/abs/2603.12265v1)**  
  Authors: Yibin Yan, Jilan Xu, Shangzhe Di, Haoning Wu, Weidi Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.12265v1.pdf)  
  Keywords: efficient, physical, evaluation, interactive, streaming, benchmark  
- **[HomeSafe-Bench: Evaluating Vision-Language Models on Unsafe Action Detection for Embodied Agents in Household Scenarios](https://arxiv.org/abs/2603.11975v2)**  
  Authors: Jiayue Pu, Zhongxiang Sun, Zilu Zhang, Xiao Zhang, Jun Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.11975v2.pdf)  
  Keywords: simulation, physical, evaluation, architecture, physical simulation, video generation, streaming, benchmark  
- **[Risk-Controllable Multi-View Diffusion for Driving Scenario Generation](https://arxiv.org/abs/2603.11534v1)**  
  Authors: Hongyi Lin, Wenxiu Shi, Heye Huang, Dingyi Zhuang, Song Zhang, Yang Liu, Xiaobo Qu, Jinhua Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.11534v1.pdf)  
  Keywords: world model, controllable, physical, autonomous driving  
- **[World2Act: Latent Action Post-Training via Skill-Compositional World Models](https://arxiv.org/abs/2603.10422v1)**  
  Authors: An Dinh Vuong, Tuan Van Vo, Abdullah Sohail, Haoran Ding, Liang Ma, Xiaodan Liang, Anqing Duan, Ivan Laptev, Ian Reid  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.10422v1.pdf)  
  Keywords: world model, dynamics, video generation  
- **[Chain of Event-Centric Causal Thought for Physically Plausible Video Generation](https://arxiv.org/abs/2603.09094v1)**  
  Authors: Zixuan Wang, Yixin Hu, Haolan Wang, Feng Chen, Yan Liu, Wen Li, Yinjie Lei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09094v1.pdf)  
  Keywords: dit, diffusion model, physical, video diffusion, physics, interactive, video generation, concept, benchmark  
- **[SPIRAL: A Closed-Loop Framework for Self-Improving Action World Models via Reflective Planning Agents](https://arxiv.org/abs/2603.08403v2)**  
  Authors: Yu Yang, Yue Liao, Jianbiao Mei, Baisen Wang, Xuemeng Yang, Licheng Wen, Jiangning Zhang, Xiangtai Li, Hanlin Chen, Botian Shi, Yong Liu, Shuicheng Yan, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08403v2.pdf)  
  Keywords: temporal consistency, world model, i2v, controllable, dit, evaluation, video generation, benchmark  
- **[RealWonder: Real-Time Physical Action-Conditioned Video Generation](https://arxiv.org/abs/2603.05449v1)**  
  Authors: Wei Liu, Ziyu Chen, Zizhang Li, Yue Wang, Hong-Xing Yu, Jiajun Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05449v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://liuwei283.github.io/RealWonder)  
  Keywords: action-conditioned, simulation, camera control, dit, physical, physics, interactive, video generation  
- **[Phys4D: Fine-Grained Physics-Consistent 4D Modeling from Video Diffusion](https://arxiv.org/abs/2603.03485v2)**  
  Authors: Haoran Lu, Shang Wu, Jianshu Zhang, Maojiang Su, Guo Ye, Chenwei Xu, Lie Lu, Pranav Maneriker, Fan Du, Manling Li, Zhaoran Wang, Han Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.03485v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://sensational-brioche-7657e7.netlify.app/) | [![Demo](https://img.shields.io/badge/-Demo-brightgreen)](https://sensational-brioche-7657e7.netlify.app)  
  Keywords: world model, simulation, diffusion model, physical, video diffusion, physics, evaluation, dynamics  



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
