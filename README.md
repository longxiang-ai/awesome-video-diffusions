# Awesome Video Diffusions [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Video Diffusion Models and Video Generation. Content is automatically updated daily.

> Last Update: 2026-03-19 02:22:05

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

- [3D-aware Video Generation](#3d-aware-video-generation) (26 papers) - Video generation with 3D awareness, multi-view consistency, and 4D content creation
- [Applications](#applications) (43 papers) - Domain-specific applications of video diffusion models
- [Architecture & Efficiency](#architecture-&-efficiency) (361 papers) - Architectural innovations (DiT, UNet), flow matching, and training/inference efficiency
- [Audio & Multi-modal](#audio-&-multi-modal) (29 papers) - Audio-driven and multi-modal conditioned video generation
- [Controllable Generation](#controllable-generation) (123 papers) - Controllable video generation with motion, camera, pose, or layout guidance
- [Human & Character Animation](#human-&-character-animation) (28 papers) - Human-centric video generation including talking heads, dance, and character animation
- [Image-to-Video Generation](#image-to-video-generation) (41 papers) - Methods for animating still images into videos
- [Long Video Generation](#long-video-generation) (119 papers) - Generating temporally consistent long-form videos beyond short clips
- [Personalization & Customization](#personalization-&-customization) (89 papers) - Personalized video generation with custom subjects, identities, or styles
- [Physical Understanding](#physical-understanding) (139 papers) - Physics-aware video generation and dynamics modeling
- [Surveys & Benchmarks](#surveys-&-benchmarks) (192 papers) - Survey papers, benchmarks, and evaluation metrics for video generation
- [Text-to-Video Generation](#text-to-video-generation) (70 papers) - Foundation models and methods for generating videos from text prompts
- [Video Editing](#video-editing) (32 papers) - Diffusion-based video editing, style transfer, and manipulation
- [Video Inpainting & Completion](#video-inpainting-&-completion) (4 papers) - Video inpainting, completion, outpainting, and temporal prediction
- [Video Super-Resolution & Enhancement](#video-super-resolution-&-enhancement) (60 papers) - Video quality improvement, upscaling, restoration, and frame interpolation
- [World Models & Simulation](#world-models-&-simulation) (95 papers) - Video generation as world simulators and interactive environment generation



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3D-aware Video Generation

- **[TAPESTRY: From Geometry to Appearance via Consistent Turntable Videos](https://arxiv.org/abs/2603.17735v1)**  
  Authors: Yan Zeng, Haoran Jiang, Kaixin Yao, Qixuan Zhang, Longwen Zhang, Lan Xu, Jingyi Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17735v1.pdf)  
  Keywords: video generation, multi-modal, 3d-aware, dit, diffusion model, video diffusion  
- **[Tri-Prompting: Video Diffusion with Unified Control over Scene, Subject, and Motion](https://arxiv.org/abs/2603.15614v1)**  
  Authors: Zhenghong Zhou, Xiaohang Zhan, Zhiqin Chen, Soo Ye Kim, Nanxuan Zhao, Haitian Zheng, Qing Liu, He Zhang, Zhe Lin, Yuqian Zhou, Jiebo Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15614v1.pdf)  
  Keywords: motion control, architecture, 3d-aware, identity, dit, diffusion model, video diffusion, customization, controllable  
- **[GeoNVS: Geometry Grounded Video Diffusion for Novel View Synthesis](https://arxiv.org/abs/2603.14965v1)**  
  Authors: Minjun Kang, Inkyu Shin, Taeyeop Lee, Myungchul Kim, In So Kweon, Kuk-Jin Yoon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14965v1.pdf)  
  Keywords: novel view, dit, diffusion model, video diffusion, camera control  
- **[MVHOI: Bridge Multi-view Condition to Complex Human-Object Interaction Video Reenactment via 3D Foundation Model](https://arxiv.org/abs/2603.14686v1)**  
  Authors: Jinguang Tong, Jinbo Wu, Kaisiyuan Wang, Zhelun Shen, Xuan Huang, Mochu Xiang, Xuesong Li, Yingying Li, Haocheng Feng, Chen Zhao, Hang Zhou, Wei He, Chuong Nguyen, Jingdong Wang, Hongdong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14686v1.pdf)  
  Keywords: novel view, video generation, dynamics, dit, controllable  
- **[CamLit: Unified Video Diffusion with Explicit Camera and Lighting Control](https://arxiv.org/abs/2603.14241v1)**  
  Authors: Zhiyi Kuang, Chengan He, Egor Zakharov, Yuxuan Xue, Shunsuke Saito, Olivier Maury, Timur Bagautdinov, Youyi Zheng, Giljoo Nam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14241v1.pdf)  
  Keywords: novel view, trajectory, video generation, diffusion model, video diffusion  
- **[Ego-1K -- A Large-Scale Multiview Video Dataset for Egocentric Vision](https://arxiv.org/abs/2603.13741v1)**  
  Authors: Jae Yong Lee, Daniel Scharstein, Akash Bapat, Hao Hu, Andrew Fu, Haoru Zhao, Paul Sammut, Xiang Li, Stephen Jeapes, Anik Gupta, Lior David, Saketh Madhuvarasu, Jay Girish Joshi, Jason Wither  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.13741v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://huggingface.co/datasets/facebook/ego-1k.) | [![Dataset](https://img.shields.io/badge/-Dataset-orange)](https://huggingface.co/datasets/facebook/ego-1k)  
  Keywords: video synthesis, benchmark, novel view, 3d video  
- **[ConfCtrl: Enabling Precise Camera Control in Video Diffusion via Confidence-Aware Interpolation](https://arxiv.org/abs/2603.09819v1)**  
  Authors: Liudi Yang, George Eskandar, Fengyi Shen, Mohammad Altillawi, Yang Bai, Chi Zhang, Ziyuan Liu, Abhinav Valada  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09819v1.pdf)  
  Keywords: novel view, dit, diffusion model, video diffusion, video interpolation, camera control  
- **[Transformer-Based Inpainting for Real-Time 3D Streaming in Sparse Multi-Camera Setups](https://arxiv.org/abs/2603.05507v1)**  
  Authors: Leif Van Holland, Domenic Zingsheim, Mana Takhsha, Hannah Dröge, Patrick Stotko, Markus Plack, Reinhard Klein  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05507v1.pdf)  
  Keywords: novel view, streaming, architecture, dit  
- **[Orthogonal Spatial-temporal Distributional Transfer for 4D Generation](https://arxiv.org/abs/2603.05081v1)**  
  Authors: Wei Liu, Shengqiong Wu, Bobo Li, Haoyu Zhao, Hao Fei, Mong-Li Lee, Wynne Hsu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05081v1.pdf)  
  Keywords: diffusion model, video diffusion, 4d generation, temporal consistency  
- **[ShareVerse: Multi-Agent Consistent Video Generation for Shared World Modeling](https://arxiv.org/abs/2603.02697v1)**  
  Authors: Jiayi Zhu, Jianing Zhang, Yiying Yang, Wei Cheng, Xiaoyun Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02697v1.pdf)  
  Keywords: video generation, interactive, multi-view video, dit, world model, simulation  

### Applications

- **[EVA: Aligning Video World Models with Executable Robot Actions via Inverse Dynamics Rewards](https://arxiv.org/abs/2603.17808v1)**  
  Authors: Ruixiang Wang, Qingming Liu, Yueci Deng, Guiliang Liu, Zhen Liu, Kui Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17808v1.pdf)  
  Keywords: physical, efficient, video generation, robotics, benchmark, dynamics, dit, world model, acceleration  
- **[Surg$Σ$: A Spectrum of Large-Scale Multimodal Data and Foundation Models for Surgical Intelligence](https://arxiv.org/abs/2603.16822v1)**  
  Authors: Zhitao Zeng, Mengya Xu, Jian Jiang, Pengfei Guo, Yunqiu Xu, Zhu Zhuo, Chang Han Low, Yufan He, Dong Yang, Chenxi Lin, Yiming Gu, Jiaxin Guo, Yutong Ban, Daguang Xu, Qi Dou, Yueming Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16822v1.pdf)  
  Keywords: medical  
- **[Bridging Scene Generation and Planning: Driving with World Model via Unifying Vision and Motion Representation](https://arxiv.org/abs/2603.14948v1)**  
  Authors: Xingtai Gui, Meijie Zhang, Tianyi Yan, Wencheng Han, Jiahao Gong, Feiyang Tan, Cheng-zhong Xu, Jianbing Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14948v1.pdf)  
  Keywords: trajectory, video generation, multi-modal, benchmark, dynamics, dit, world model, autonomous driving  
- **[FAR-Drive: Frame-AutoRegressive Video Generation in Closed-Loop Autonomous Driving](https://arxiv.org/abs/2603.14938v1)**  
  Authors: Yaoru Li, Federico Landi, Marco Godi, Xin Jin, Ruiju Fu, Yufei Ma, Muyang Sun, Heyu Si, Qi Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14938v1.pdf)  
  Keywords: video generation, interactive, evaluation, diffusion transformer, autoregressive, dit, simulation, autonomous driving, acceleration  
- **[Script-to-Slide Grounding: Grounding Script Sentences to Slide Objects for Automatic Instructional Video Generation](https://arxiv.org/abs/2603.16931v1)**  
  Authors: Rena Suzuki, Masato Kikuchi, Tadachika Ozono  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16931v1.pdf)  
  Keywords: dit, education, video editing, video generation  
- **[PhysAlign: Physics-Coherent Image-to-Video Generation through Feature and 3D Representation Alignment](https://arxiv.org/abs/2603.13770v1)**  
  Authors: Zhexiao Xiong, Yizhi Song, Liu He, Wei Xiong, Yu Yuan, Feng Qiao, Nathan Jacobs  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.13770v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://physalign.github.io/PhysAlign)  
  Keywords: physical, efficient, video generation, robotics, i2v, physics, diffusion model, video diffusion, simulation, image-to-video, controllable  
- **[Risk-Controllable Multi-View Diffusion for Driving Scenario Generation](https://arxiv.org/abs/2603.11534v1)**  
  Authors: Hongyi Lin, Wenxiu Shi, Heye Huang, Dingyi Zhuang, Song Zhang, Yang Liu, Xiaobo Qu, Jinhua Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.11534v1.pdf)  
  Keywords: physical, controllable, world model, autonomous driving  
- **[ShotVerse: Advancing Cinematic Camera Control for Text-Driven Multi-Shot Video Creation](https://arxiv.org/abs/2603.11421v1)**  
  Authors: Songlin Yang, Zhe Wang, Xuyi Yang, Songchun Zhang, Xianghao Kong, Taiyi Wu, Xiaotong Zhao, Ran Zhang, Alan Zhao, Anyi Rao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.11421v1.pdf)  
  Keywords: trajectory, video generation, film, evaluation, dit, text-driven video, camera control  
- **[Motion Forcing: A Decoupled Framework for Robust Video Generation in Motion Dynamics](https://arxiv.org/abs/2603.10408v1)**  
  Authors: Tianshuo Xu, Zhifei Chen, Leyi Wu, Hao Lu, Ying-cong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.10408v1.pdf)  
  Keywords: physical, video generation, robotics, benchmark, evaluation, dynamics, physics, autonomous driving  
- **[EduVQA: Benchmarking AI-Generated Video Quality Assessment for Education](https://arxiv.org/abs/2603.03066v1)**  
  Authors: Baoliang Chen, Xinlong Bu, Lingyu Zhu, Hanwei Zhu, Xiangjie Sui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.03066v1.pdf)  
  Keywords: benchmark, t2v, evaluation, concept, education, text-to-video  

### Architecture & Efficiency

*Showing the latest 50 out of 361 papers*

- **[The Unreasonable Effectiveness of Text Embedding Interpolation for Continuous Image Steering](https://arxiv.org/abs/2603.17998v1)**  
  Authors: Yigit Ekin, Yossi Gandelsman  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17998v1.pdf)  
  Keywords: video generation, evaluation, dit, concept, controllable  
- **[Versatile Editing of Video Content, Actions, and Dynamics without Training](https://arxiv.org/abs/2603.17989v1)**  
  Authors: Vladimir Kulikov, Roni Paiss, Andrey Voynov, Inbar Mosseri, Tali Dekel, Tomer Michaeli  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17989v1.pdf)  
  Keywords: video generation, video editing, dynamics, dit, text-to-video  
- **[AHOY! Animatable Humans under Occlusion from YouTube Videos with Gaussian Splatting and Video Diffusion Priors](https://arxiv.org/abs/2603.17975v1)**  
  Authors: Aymen Mir, Riza Alp Guler, Xiangjun Tang, Peter Wonka, Gerard Pons-Moll  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17975v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://miraymen.github.io/ahoy)  
  Keywords: architecture, identity, diffusion model, video diffusion, avatar  
- **[ChopGrad: Pixel-Wise Losses for Latent Video Diffusion via Truncated Backpropagation](https://arxiv.org/abs/2603.17812v1)**  
  Authors: Dmitriy Rivkin, Parker Ewen, Lili Gao, Julian Ost, Stefanie Walz, Rasika Kangutkar, Mario Bijelic, Felix Heide  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17812v1.pdf)  
  Keywords: latent video, video inpainting, efficient, video generation, video enhancement, diffusion model, video diffusion, dit, super-resolution  
- **[EVA: Aligning Video World Models with Executable Robot Actions via Inverse Dynamics Rewards](https://arxiv.org/abs/2603.17808v1)**  
  Authors: Ruixiang Wang, Qingming Liu, Yueci Deng, Guiliang Liu, Zhen Liu, Kui Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17808v1.pdf)  
  Keywords: physical, efficient, video generation, robotics, benchmark, dynamics, dit, world model, acceleration  
- **[TAPESTRY: From Geometry to Appearance via Consistent Turntable Videos](https://arxiv.org/abs/2603.17735v1)**  
  Authors: Yan Zeng, Haoran Jiang, Kaixin Yao, Qixuan Zhang, Longwen Zhang, Lan Xu, Jingyi Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17735v1.pdf)  
  Keywords: video generation, multi-modal, 3d-aware, dit, diffusion model, video diffusion  
- **[Learning Transferable Temporal Primitives for Video Reasoning via Synthetic Videos](https://arxiv.org/abs/2603.17693v1)**  
  Authors: Songtao Jiang, Sibo Song, Chenyi Zhou, Yuan Wang, Ruizhe Chen, Tongkun Guan, Ruilin Luo, Yan Zhang, Zhihang Tang, Yuchong Sun, Hang Zhang, Zhibo Yang, Shuai Bai, Junyang Lin, Zuozhu Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17693v1.pdf)  
  Keywords: image to video, efficient, video generation, benchmark, dynamics  
- **[Few-Step Diffusion Sampling Through Instance-Aware Discretizations](https://arxiv.org/abs/2603.17671v1)**  
  Authors: Liangyu Yuan, Ruoyu Wang, Tong Zhao, Dingwen Fu, Mingkun Lei, Beier Zhu, Chi Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17671v1.pdf)  
  Keywords: flow matching, dit, dynamics  
- **[FrescoDiffusion: 4K Image-to-Video with Prior-Regularized Tiled Diffusion](https://arxiv.org/abs/2603.17555v1)**  
  Authors: Hugo Caselles-Dupré, Mathis Koroglu, Guillaume Jeanneret, Arnaud Dapogny, Matthieu Cord  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17555v1.pdf)  
  Keywords: trajectory, efficient, denoising, i2v, dit, image-to-video, layout  
- **[AR-CoPO: Align Autoregressive Video Generation with Contrastive Policy Optimization](https://arxiv.org/abs/2603.17461v1)**  
  Authors: Dailan He, Guanlin Feng, Xingtong Ge, Yi Zhang, Bingqi Ma, Guanglu Song, Yu Liu, Hongsheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17461v1.pdf)  
  Keywords: streaming, autoregressive, distillation, video generation  

### Audio & Multi-modal

- **[TAPESTRY: From Geometry to Appearance via Consistent Turntable Videos](https://arxiv.org/abs/2603.17735v1)**  
  Authors: Yan Zeng, Haoran Jiang, Kaixin Yao, Qixuan Zhang, Longwen Zhang, Lan Xu, Jingyi Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17735v1.pdf)  
  Keywords: video generation, multi-modal, 3d-aware, dit, diffusion model, video diffusion  
- **[Bridging Scene Generation and Planning: Driving with World Model via Unifying Vision and Motion Representation](https://arxiv.org/abs/2603.14948v1)**  
  Authors: Xingtai Gui, Meijie Zhang, Tianyi Yan, Wencheng Han, Jiahao Gong, Feiyang Tan, Cheng-zhong Xu, Jianbing Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14948v1.pdf)  
  Keywords: trajectory, video generation, multi-modal, benchmark, dynamics, dit, world model, autonomous driving  
- **[V-JEPA 2.1: Unlocking Dense Features in Video Self-Supervised Learning](https://arxiv.org/abs/2603.14482v2)**  
  Authors: Lorenzo Mur-Labadia, Matthew Muckley, Amir Bar, Mido Assran, Koustuv Sinha, Mike Rabbat, Yann LeCun, Nicolas Ballas, Adrien Bardes  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14482v2.pdf)  
  Keywords: benchmark, world model, multi-modal  
- **[Fuel Gauge: Estimating Chain-of-Thought Length Ahead of Time in Large Multimodal Models](https://arxiv.org/abs/2603.10335v1)**  
  Authors: Yuedong Yang, Xiwen Wei, Mustafa Munir, Radu Marculescu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.10335v1.pdf)  
  Keywords: benchmark, efficient, multi-modal  
- **[ID-LoRA: Identity-Driven Audio-Video Personalization with In-Context LoRA](https://arxiv.org/abs/2603.10256v1)**  
  Authors: Aviad Dahan, Moran Yanuka, Noa Kraicer, Lior Wolf, Raja Giryes  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.10256v1.pdf)  
  Keywords: physical, efficient, denoising, style, identity, dit, video diffusion, sound, personalization  
- **[FetalAgents: A Multi-Agent System for Fetal Ultrasound Image and Video Analysis](https://arxiv.org/abs/2603.09733v1)**  
  Authors: Xiaotian Hu, Junwei Huang, Mingxuan Liu, Kasidit Anmahapong, Yifei Chen, Yitong Luo, Yiming Huang, Xuguang Bai, Zihan Li, Yi Liao, Haibo Qu, Qiyuan Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09733v1.pdf)  
  Keywords: sound, dit, evaluation  
- **[MM-TS: Multi-Modal Temperature and Margin Schedules for Contrastive Learning with Long-Tail Data](https://arxiv.org/abs/2603.08202v1)**  
  Authors: Siarhei Sheludzko, Dhimitrios Duka, Bernt Schiele, Hilde Kuehne, Anna Kukleva  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08202v1.pdf)  
  Keywords: dit, concept, multi-modal  
- **[StreamWise: Serving Multi-Modal Generation in Real-Time at Scale](https://arxiv.org/abs/2603.05800v1)**  
  Authors: Haoran Qiu, Gohar Irfan Chaudhry, Chaojie Zhang, Íñigo Goiri, Esha Choukse, Rodrigo Fonseca, Ricardo Bianchini  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05800v1.pdf)  
  Keywords: streaming, efficient, video generation, multi-modal  
- **[UniTalking: A Unified Audio-Video Framework for Talking Portrait Generation](https://arxiv.org/abs/2603.01418v1)**  
  Authors: Hebeizi Li, Zihao Liang, Benyuan Sun, Zihao Yin, Xiao Sha, Chenliang Wang, Yi Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01418v1.pdf)  
  Keywords: efficient, video generation, multi-modal, architecture, style  
- **[FlowPortrait: Reinforcement Learning for Audio-Driven Portrait Video Generation](https://arxiv.org/abs/2603.00159v1)**  
  Authors: Weiting Tan, Andy T. Liu, Ming Tu, Xinghua Qu, Philipp Koehn, Lu Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.00159v1.pdf)  
  Keywords: audio-driven, video generation, evaluation, audio-to-video, temporal consistency, autoregressive  

### Controllable Generation

*Showing the latest 50 out of 123 papers*

- **[The Unreasonable Effectiveness of Text Embedding Interpolation for Continuous Image Steering](https://arxiv.org/abs/2603.17998v1)**  
  Authors: Yigit Ekin, Yossi Gandelsman  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17998v1.pdf)  
  Keywords: video generation, evaluation, dit, concept, controllable  
- **[FrescoDiffusion: 4K Image-to-Video with Prior-Regularized Tiled Diffusion](https://arxiv.org/abs/2603.17555v1)**  
  Authors: Hugo Caselles-Dupré, Mathis Koroglu, Guillaume Jeanneret, Arnaud Dapogny, Matthieu Cord  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17555v1.pdf)  
  Keywords: trajectory, efficient, denoising, i2v, dit, image-to-video, layout  
- **[MosaicMem: Hybrid Spatial Memory for Controllable Video World Models](https://arxiv.org/abs/2603.17117v1)**  
  Authors: Wei Yu, Runjia Qian, Yumeng Li, Liquan Wang, Songheng Yin, Sri Siddarth Chakaravarthy P, Dennis Anthony, Yang Ye, Yidi Li, Weiwei Wan, Animesh Garg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17117v1.pdf)  
  Keywords: diffusion model, autoregressive, video diffusion, world model, dit, controllable, world simulator  
- **[Search2Motion: Training-Free Object-Level Motion Control via Attention-Consensus Search](https://arxiv.org/abs/2603.16711v2)**  
  Authors: Sainan Liu, Tz-Ying Wu, Hector A Valdez, Subarna Tripathi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16711v2.pdf)  
  Keywords: motion control, video generation, benchmark, evaluation, dynamics, dit, image-to-video  
- **[Kinema4D: Kinematic 4D World Modeling for Spatiotemporal Embodied Simulation](https://arxiv.org/abs/2603.16669v1)**  
  Authors: Mutian Xu, Tianbao Zhang, Tianqi Liu, Zhaoxi Chen, Xiaoguang Han, Ziwei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16669v1.pdf)  
  Keywords: trajectory, physical, video generation, interactive, dynamics, dit, world model, simulation, action-conditioned  
- **[Tri-Prompting: Video Diffusion with Unified Control over Scene, Subject, and Motion](https://arxiv.org/abs/2603.15614v1)**  
  Authors: Zhenghong Zhou, Xiaohang Zhan, Zhiqin Chen, Soo Ye Kim, Nanxuan Zhao, Haitian Zheng, Qing Liu, He Zhang, Zhe Lin, Yuqian Zhou, Jiebo Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15614v1.pdf)  
  Keywords: motion control, architecture, 3d-aware, identity, dit, diffusion model, video diffusion, customization, controllable  
- **[Grounding World Simulation Models in a Real-World Metropolis](https://arxiv.org/abs/2603.15583v1)**  
  Authors: Junyoung Seo, Hyunwook Choi, Minkyung Kwon, Jinhyeok Choi, Siyoon Jin, Gayoung Lee, Junho Kim, JoungBin Lee, Geonmo Gu, Dongyoon Han, Sangdoo Yun, Seungryong Kim, Jin-Hwa Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15583v1.pdf)  
  Keywords: trajectory, video generation, dit, autoregressive, world model, simulation  
- **[ViFeEdit: A Video-Free Tuner of Your Video Diffusion Transformer](https://arxiv.org/abs/2603.15478v1)**  
  Authors: Ruonan Yu, Zhenxiong Tan, Zigeng Chen, Songhua Liu, Xinchao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15478v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Lexie-YU/ViFeEdit?style=social)](https://github.com/Lexie-YU/ViFeEdit)  
  Keywords: video generation, temporal consistency, diffusion transformer, diffusion model, video diffusion, dit, controllable  
- **[AnyCrowd: Instance-Isolated Identity-Pose Binding for Arbitrary Multi-Character Animation](https://arxiv.org/abs/2603.15415v1)**  
  Authors: Zhenyu Xie, Ji Xia, Michael Kampffmeyer, Panwen Hu, Zehua Ma, Yujian Zheng, Jing Wang, Zheng Chong, Xujie Zhang, Xianhang Cheng, Xiaodan Liang, Hao Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15415v1.pdf)  
  Keywords: video generation, identity, dit, diffusion transformer, controllable  
- **[Next-Frame Decoding for Ultra-Low-Bitrate Image Compression with Video Diffusion Priors](https://arxiv.org/abs/2603.15129v2)**  
  Authors: Yunuo Chen, Chuqin Zhou, Jiangchuan Li, Xiaoyue Ling, Bing He, Jincheng Dai, Li Song, Guo Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15129v2.pdf)  
  Keywords: diffusion model, video diffusion, layout  

### Human & Character Animation

- **[AHOY! Animatable Humans under Occlusion from YouTube Videos with Gaussian Splatting and Video Diffusion Priors](https://arxiv.org/abs/2603.17975v1)**  
  Authors: Aymen Mir, Riza Alp Guler, Xiangjun Tang, Peter Wonka, Gerard Pons-Moll  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17975v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://miraymen.github.io/ahoy)  
  Keywords: architecture, identity, diffusion model, video diffusion, avatar  
- **[SoulX-LiveAct: Towards Hour-Scale Real-Time Human Animation with Neighbor Forcing and ConvKV Memory](https://arxiv.org/abs/2603.11746v1)**  
  Authors: Dingcheng Zhen, Xu Zheng, Ruixin Zhang, Zhiqi Jiang, Yichao Yan, Ming Tao, Shunshun Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.11746v1.pdf)  
  Keywords: efficient, video generation, video synthesis, streaming, diffusion model, autoregressive, human animation, dit  
- **[Controllable Complex Human Motion Video Generation via Text-to-Skeleton Cascades](https://arxiv.org/abs/2603.08028v1)**  
  Authors: Ashkan Taghipour, Morteza Ghahremani, Zinuo Li, Hamid Laga, Farid Boussaid, Mohammed Bennamoun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08028v1.pdf)  
  Keywords: motion control, video generation, benchmark, temporal consistency, diffusion model, video diffusion, autoregressive, dit, controllable, human motion  
- **[ArtHOI: Articulated Human-Object Interaction Synthesis by 4D Reconstruction from Video Priors](https://arxiv.org/abs/2603.04338v1)**  
  Authors: Zihao Huang, Tianqi Liu, Zhaoxi Chen, Shaocong Xu, Saining Zhang, Lixing Xiao, Zhiguo Cao, Wei Li, Hao Zhao, Ziwei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.04338v1.pdf)  
  Keywords: physical, dit, diffusion model, video diffusion, human motion  
- **[Direct Reward Fine-Tuning on Poses for Single Image to 3D Human in the Wild](https://arxiv.org/abs/2603.02619v1)**  
  Authors: Seunguk Do, Minwoo Huh, Joonghyuk Shin, Jaesik Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02619v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://seunguk-do.github.io/drpose)  
  Keywords: benchmark, evaluation, dit, diffusion model, human motion  
- **[LiftAvatar: Kinematic-Space Completion for Expression-Controlled 3D Gaussian Avatar Animation](https://arxiv.org/abs/2603.02129v1)**  
  Authors: Hualiang Wei, Shunran Jia, Jialun Liu, Wenhui Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02129v1.pdf)  
  Keywords: efficient, diffusion transformer, video diffusion, dit, controllable, distillation, avatar  
- **[Non-verbal Real-time Human-AI Interaction in Constrained Robotic Environments](https://arxiv.org/abs/2603.01804v1)**  
  Authors: Dragos Costea, Alina Marcu, Cristina Lazar, Marius Leordeanu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01804v1.pdf)  
  Keywords: text-to-video, body motion, architecture  
- **[GeoDiff4D: Geometry-Aware Diffusion for 4D Head Avatar Reconstruction](https://arxiv.org/abs/2602.24161v2)**  
  Authors: Chao Xu, Xiaochen Zhao, Xiang Deng, Jingxiang Sun, Donglin Di, Zhuo Su, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.24161v2.pdf)  
  Keywords: identity, avatar, diffusion model, video generation  
- **[Spatio-Temporal Garment Reconstruction Using Diffusion Mapping via Pattern Coordinates](https://arxiv.org/abs/2602.24043v1)**  
  Authors: Yingxuan You, Ren Li, Corentin Dumery, Cong Cao, Hao Li, Pascal Fua  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.24043v1.pdf)  
  Keywords: temporal consistency, dit, diffusion model, avatar, virtual try-on  
- **[BigMaQ: A Big Macaque Motion and Animation Dataset Bridging Image and 3D Pose Representations](https://arxiv.org/abs/2602.19874v1)**  
  Authors: Lucas Martini, Alexander Lappe, Anna Bognár, Rufin Vogels, Martin A. Giese  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.19874v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://martinivis.github.io/BigMaQ)  
  Keywords: benchmark, dynamics, avatar  

### Image-to-Video Generation

- **[TransText: Transparency Aware Image-to-Video Typography Animation](https://arxiv.org/abs/2603.17944v1)**  
  Authors: Fei Zhang, Zijian Zhou, Bohao Tang, Sen He, Hang Li, Zhe Wang, Soubhik Sanyal, Pengfei Liu, Viktar Atliha, Tao Xiang, Frost Xu, Semih Gunel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17944v1.pdf)  
  Keywords: image-to-video  
- **[Learning Transferable Temporal Primitives for Video Reasoning via Synthetic Videos](https://arxiv.org/abs/2603.17693v1)**  
  Authors: Songtao Jiang, Sibo Song, Chenyi Zhou, Yuan Wang, Ruizhe Chen, Tongkun Guan, Ruilin Luo, Yan Zhang, Zhihang Tang, Yuchong Sun, Hang Zhang, Zhibo Yang, Shuai Bai, Junyang Lin, Zuozhu Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17693v1.pdf)  
  Keywords: image to video, efficient, video generation, benchmark, dynamics  
- **[FrescoDiffusion: 4K Image-to-Video with Prior-Regularized Tiled Diffusion](https://arxiv.org/abs/2603.17555v1)**  
  Authors: Hugo Caselles-Dupré, Mathis Koroglu, Guillaume Jeanneret, Arnaud Dapogny, Matthieu Cord  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17555v1.pdf)  
  Keywords: trajectory, efficient, denoising, i2v, dit, image-to-video, layout  
- **[Search2Motion: Training-Free Object-Level Motion Control via Attention-Consensus Search](https://arxiv.org/abs/2603.16711v2)**  
  Authors: Sainan Liu, Tz-Ying Wu, Hector A Valdez, Subarna Tripathi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16711v2.pdf)  
  Keywords: motion control, video generation, benchmark, evaluation, dynamics, dit, image-to-video  
- **[GenState-AI: State-Aware Dataset for Text-to-Video Retrieval on AI-Generated Videos](https://arxiv.org/abs/2603.14426v1)**  
  Authors: Minghan Li, Tongna Chen, Tianrui Lv, Yishuai Zhang, Suchao An, Guodong Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14426v1.pdf)  
  Keywords: benchmark, i2v, evaluation, dit, text-to-video, controllable  
- **[PhysAlign: Physics-Coherent Image-to-Video Generation through Feature and 3D Representation Alignment](https://arxiv.org/abs/2603.13770v1)**  
  Authors: Zhexiao Xiong, Yizhi Song, Liu He, Wei Xiong, Yu Yuan, Feng Qiao, Nathan Jacobs  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.13770v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://physalign.github.io/PhysAlign)  
  Keywords: physical, efficient, video generation, robotics, i2v, physics, diffusion model, video diffusion, simulation, image-to-video, controllable  
- **[UniVid: Pyramid Diffusion Model for High Quality Video Generation](https://arxiv.org/abs/2603.13739v1)**  
  Authors: Xinyu Xiao, Binbin Yang, Tingtian Li, Yipeng Yu, Sen Lei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.13739v1.pdf)  
  Keywords: video generation, i2v, t2v, diffusion model, dit, image-to-video, text-to-video  
- **[CtrlAttack: A Unified Attack on World-Model Control in Diffusion Models](https://arxiv.org/abs/2603.13435v1)**  
  Authors: Shuhan Xu, Siyuan Liang, Hongling Zheng, Yong Luo, Han Hu, Lefei Zhang, Dacheng Tao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.13435v1.pdf)  
  Keywords: trajectory, i2v, dynamics, temporal consistency, diffusion model, image-to-video  
- **[VQQA: An Agentic Approach for Video Evaluation and Quality Improvement](https://arxiv.org/abs/2603.12310v1)**  
  Authors: Yiwen Song, Tomas Pfister, Yale Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.12310v1.pdf)  
  Keywords: efficient, video generation, i2v, evaluation, t2v, dit, image-to-video, text-to-video  
- **[SPIRAL: A Closed-Loop Framework for Self-Improving Action World Models via Reflective Planning Agents](https://arxiv.org/abs/2603.08403v2)**  
  Authors: Yu Yang, Yue Liao, Jianbiao Mei, Baisen Wang, Xuemeng Yang, Licheng Wen, Jiangning Zhang, Xiangtai Li, Hanlin Chen, Botian Shi, Yong Liu, Shuicheng Yan, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08403v2.pdf)  
  Keywords: video generation, benchmark, i2v, evaluation, temporal consistency, dit, world model, controllable  

### Long Video Generation

*Showing the latest 50 out of 119 papers*

- **[AR-CoPO: Align Autoregressive Video Generation with Contrastive Policy Optimization](https://arxiv.org/abs/2603.17461v1)**  
  Authors: Dailan He, Guanlin Feng, Xingtong Ge, Yi Zhang, Bingqi Ma, Guanglu Song, Yu Liu, Hongsheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17461v1.pdf)  
  Keywords: streaming, autoregressive, distillation, video generation  
- **[Motion-Adaptive Temporal Attention for Lightweight Video Generation with Stable Diffusion](https://arxiv.org/abs/2603.17398v1)**  
  Authors: Rui Hong, Shuxue Quan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17398v1.pdf)  
  Keywords: efficient, video generation, denoising, temporal consistency, diffusion model  
- **[MosaicMem: Hybrid Spatial Memory for Controllable Video World Models](https://arxiv.org/abs/2603.17117v1)**  
  Authors: Wei Yu, Runjia Qian, Yumeng Li, Liquan Wang, Songheng Yin, Sri Siddarth Chakaravarthy P, Dennis Anthony, Yang Ye, Yidi Li, Weiwei Wan, Animesh Garg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17117v1.pdf)  
  Keywords: diffusion model, autoregressive, video diffusion, world model, dit, controllable, world simulator  
- **[WorldCam: Interactive Autoregressive 3D Gaming Worlds with Camera Pose as a Unifying Geometric Representation](https://arxiv.org/abs/2603.16871v1)**  
  Authors: Jisu Nam, Yicong Hong, Chun-Hao Paul Huang, Feng Liu, JoungBin Lee, Jiyoung Kim, Siyoon Jin, Yunsung Lee, Jaeyoon Jung, Suhwan Choi, Seungryong Kim, Yang Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16871v1.pdf)  
  Keywords: interactive, physics, diffusion transformer, autoregressive, video diffusion, world model, dit  
- **[Fanar 2.0: Arabic Generative AI Stack](https://arxiv.org/abs/2603.16397v1)**  
  Authors: FANAR TEAM, Ummar Abbas, Mohammad Shahmeer Ahmad, Minhaj Ahmad, Abdulaziz Al-Homaid, Anas Al-Nuaimi, Enes Altinisik, Ehsaneddin Asgari, Sanjay Chawla, Shammur Chowdhury, Fahim Dalvi, Kareem Darwish, Nadir Durrani, Mohamed Elfeky, Ahmed Elmagarmid, Mohamed Eltabakh, Asim Ersoy, Masoomali Fatehkia, Mohammed Qusay Hashim, Majd Hawasly, Mohamed Hefeeda, Mus'ab Husaini, Keivin Isufaj, Soon-Gyo Jung, Houssam Lachemat, Ji Kim Lucas, Abubakr Mohamed, Tasnim Mohiuddin, Basel Mousi, Hamdy Mubarak, Ahmad Musleh, Mourad Ouzzani, Amin Sadeghi, Husrev Taha Sencar, Mohammed Shinoy, Omar Sinan, Yifan Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16397v1.pdf)  
  Keywords: benchmark, long-form, architecture  
- **[VIGOR: VIdeo Geometry-Oriented Reward for Temporal Generative Alignment](https://arxiv.org/abs/2603.16271v1)**  
  Authors: Tengjiao Yin, Jinglei Shi, Heng Guo, Xi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16271v1.pdf)  
  Keywords: physical, efficient, evaluation, streaming, diffusion model, video diffusion, dit  
- **[Grounding World Simulation Models in a Real-World Metropolis](https://arxiv.org/abs/2603.15583v1)**  
  Authors: Junyoung Seo, Hyunwook Choi, Minkyung Kwon, Jinhyeok Choi, Siyoon Jin, Gayoung Lee, Junho Kim, JoungBin Lee, Geonmo Gu, Dongyoon Han, Sangdoo Yun, Seungryong Kim, Jin-Hwa Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15583v1.pdf)  
  Keywords: trajectory, video generation, dit, autoregressive, world model, simulation  
- **[ViFeEdit: A Video-Free Tuner of Your Video Diffusion Transformer](https://arxiv.org/abs/2603.15478v1)**  
  Authors: Ruonan Yu, Zhenxiong Tan, Zigeng Chen, Songhua Liu, Xinchao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15478v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Lexie-YU/ViFeEdit?style=social)](https://github.com/Lexie-YU/ViFeEdit)  
  Keywords: video generation, temporal consistency, diffusion transformer, diffusion model, video diffusion, dit, controllable  
- **[FAR-Drive: Frame-AutoRegressive Video Generation in Closed-Loop Autonomous Driving](https://arxiv.org/abs/2603.14938v1)**  
  Authors: Yaoru Li, Federico Landi, Marco Godi, Xin Jin, Ruiju Fu, Yufei Ma, Muyang Sun, Heyu Si, Qi Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14938v1.pdf)  
  Keywords: video generation, interactive, evaluation, diffusion transformer, autoregressive, dit, simulation, autonomous driving, acceleration  
- **[SAW: Toward a Surgical Action World Model via Controllable and Scalable Video Generation](https://arxiv.org/abs/2603.13024v1)**  
  Authors: Sampath Rapuri, Lalithkumar Seenivasan, Dominik Schneider, Roger Soberanis-Mukul, Yufan He, Hao Ding, Jiru Xu, Chenhao Yu, Chenyan Jing, Pengfei Guo, Daguang Xu, Mathias Unberath  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.13024v1.pdf)  
  Keywords: trajectory, video-to-video, video generation, temporal consistency, diffusion model, video diffusion, world model, simulation, dit, controllable  

### Personalization & Customization

*Showing the latest 50 out of 89 papers*

- **[The Unreasonable Effectiveness of Text Embedding Interpolation for Continuous Image Steering](https://arxiv.org/abs/2603.17998v1)**  
  Authors: Yigit Ekin, Yossi Gandelsman  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17998v1.pdf)  
  Keywords: video generation, evaluation, dit, concept, controllable  
- **[AHOY! Animatable Humans under Occlusion from YouTube Videos with Gaussian Splatting and Video Diffusion Priors](https://arxiv.org/abs/2603.17975v1)**  
  Authors: Aymen Mir, Riza Alp Guler, Xiangjun Tang, Peter Wonka, Gerard Pons-Moll  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17975v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://miraymen.github.io/ahoy)  
  Keywords: architecture, identity, diffusion model, video diffusion, avatar  
- **[Identity as Presence: Towards Appearance and Voice Personalized Joint Audio-Video Generation](https://arxiv.org/abs/2603.17889v1)**  
  Authors: Yingjie Chen, Shilun Lin, Cai Xing, Qixin Yan, Wenjing Wang, Dingming Liu, Hao Liu, Chen Li, Jing Lyu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17889v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://chen-yingjie.github.io/projects/Identity-as-Presence)  
  Keywords: identity, personalization, video generation  
- **[Demystifing Video Reasoning](https://arxiv.org/abs/2603.16870v1)**  
  Authors: Ruisi Wang, Zhongang Cai, Fanyi Pu, Junxiang Xu, Wanqi Yin, Maijunxian Wang, Ran Ji, Chenyang Gu, Bo Li, Ziqi Huang, Hokin Deng, Dahua Lin, Ziwei Liu, Lei Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16870v1.pdf)  
  Keywords: video generation, denoising, dynamics, diffusion transformer, concept  
- **[Tri-Prompting: Video Diffusion with Unified Control over Scene, Subject, and Motion](https://arxiv.org/abs/2603.15614v1)**  
  Authors: Zhenghong Zhou, Xiaohang Zhan, Zhiqin Chen, Soo Ye Kim, Nanxuan Zhao, Haitian Zheng, Qing Liu, He Zhang, Zhe Lin, Yuqian Zhou, Jiebo Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15614v1.pdf)  
  Keywords: motion control, architecture, 3d-aware, identity, dit, diffusion model, video diffusion, customization, controllable  
- **[AnyCrowd: Instance-Isolated Identity-Pose Binding for Arbitrary Multi-Character Animation](https://arxiv.org/abs/2603.15415v1)**  
  Authors: Zhenyu Xie, Ji Xia, Michael Kampffmeyer, Panwen Hu, Zehua Ma, Yujian Zheng, Jing Wang, Zheng Chong, Xujie Zhang, Xianhang Cheng, Xiaodan Liang, Hao Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15415v1.pdf)  
  Keywords: video generation, identity, dit, diffusion transformer, controllable  
- **[Seeking Physics in Diffusion Noise](https://arxiv.org/abs/2603.14294v1)**  
  Authors: Chujun Tang, Lei Zhong, Fangqiang Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14294v1.pdf)  
  Keywords: trajectory, physical, denoising, identity, physics, diffusion transformer, diffusion model, video diffusion, dit  
- **[MotionCFG: Boosting Motion Dynamics via Stochastic Concept Perturbation](https://arxiv.org/abs/2603.14073v1)**  
  Authors: Byungjun Kim, Soobin Um, Jong Chul Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14073v1.pdf)  
  Keywords: denoising, t2v, dynamics, identity, dit, concept, text-to-video  
- **[LibraGen: Playing a Balance Game in Subject-Driven Video Generation](https://arxiv.org/abs/2603.13506v2)**  
  Authors: Jiahao Zhu, Shanshan Lao, Lijie Liu, Gen Li, Tianhao Qi, Wei Han, Bingchuan Li, Fangfang Liu, Zhuowei Chen, Tianxiang Ma, Qian HE, Yi Zhou, Xiaohua Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.13506v2.pdf)  
  Keywords: subject-driven, video generation  
- **[MemRoPE: Training-Free Infinite Video Generation via Evolving Memory Tokens](https://arxiv.org/abs/2603.12513v1)**  
  Authors: Youngrae Kim, Qixin Hu, C. -C. Jay Kuo, Peter A. Beerel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.12513v1.pdf)  
  Keywords: video generation, dynamics, streaming, identity, autoregressive  

### Physical Understanding

*Showing the latest 50 out of 139 papers*

- **[Versatile Editing of Video Content, Actions, and Dynamics without Training](https://arxiv.org/abs/2603.17989v1)**  
  Authors: Vladimir Kulikov, Roni Paiss, Andrey Voynov, Inbar Mosseri, Tali Dekel, Tomer Michaeli  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17989v1.pdf)  
  Keywords: video generation, video editing, dynamics, dit, text-to-video  
- **[Video Understanding: From Geometry and Semantics to Unified Models](https://arxiv.org/abs/2603.17840v1)**  
  Authors: Zhaochong An, Zirui Li, Mingqiao Ye, Feng Qiao, Jiaang Li, Zongwei Wu, Vishal Thengane, Chengzu Li, Lei Li, Luc Van Gool, Guolei Sun, Serge Belongie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17840v1.pdf)  
  Keywords: survey, dynamics  
- **[EVA: Aligning Video World Models with Executable Robot Actions via Inverse Dynamics Rewards](https://arxiv.org/abs/2603.17808v1)**  
  Authors: Ruixiang Wang, Qingming Liu, Yueci Deng, Guiliang Liu, Zhen Liu, Kui Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17808v1.pdf)  
  Keywords: physical, efficient, video generation, robotics, benchmark, dynamics, dit, world model, acceleration  
- **[Learning Transferable Temporal Primitives for Video Reasoning via Synthetic Videos](https://arxiv.org/abs/2603.17693v1)**  
  Authors: Songtao Jiang, Sibo Song, Chenyi Zhou, Yuan Wang, Ruizhe Chen, Tongkun Guan, Ruilin Luo, Yan Zhang, Zhihang Tang, Yuchong Sun, Hang Zhang, Zhibo Yang, Shuai Bai, Junyang Lin, Zuozhu Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17693v1.pdf)  
  Keywords: image to video, efficient, video generation, benchmark, dynamics  
- **[Few-Step Diffusion Sampling Through Instance-Aware Discretizations](https://arxiv.org/abs/2603.17671v1)**  
  Authors: Liangyu Yuan, Ruoyu Wang, Tong Zhao, Dingwen Fu, Mingkun Lei, Beier Zhu, Chi Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17671v1.pdf)  
  Keywords: flow matching, dit, dynamics  
- **[SHIFT: Motion Alignment in Video Diffusion Models with Adversarial Hybrid Fine-Tuning](https://arxiv.org/abs/2603.17426v1)**  
  Authors: Xi Ye, Wenjia Yang, Yangyang Xu, Xiaoyang Liu, Duo Su, Mengfei Xia, Jun Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17426v1.pdf)  
  Keywords: efficient, dynamics, dit, diffusion model, video diffusion  
- **[GigaWorld-Policy: An Efficient Action-Centered World--Action Model](https://arxiv.org/abs/2603.17240v1)**  
  Authors: Angen Ye, Boyuan Wang, Chaojun Ni, Guan Huang, Guosheng Zhao, Hao Li, Hengtao Li, Jie Li, Jindi Lv, Jingyu Liu, Min Cao, Peng Li, Qiuping Deng, Wenjun Mei, Xiaofeng Wang, Xinze Chen, Xinyu Zhou, Yang Wang, Yifan Chang, Yifan Li, Yukun Zhou, Yun Ye, Zhichao Liu, Zheng Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17240v1.pdf)  
  Keywords: physical, efficient, video generation, dynamics, dit  
- **[WorldCam: Interactive Autoregressive 3D Gaming Worlds with Camera Pose as a Unifying Geometric Representation](https://arxiv.org/abs/2603.16871v1)**  
  Authors: Jisu Nam, Yicong Hong, Chun-Hao Paul Huang, Feng Liu, JoungBin Lee, Jiyoung Kim, Siyoon Jin, Yunsung Lee, Jaeyoon Jung, Suhwan Choi, Seungryong Kim, Yang Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16871v1.pdf)  
  Keywords: interactive, physics, diffusion transformer, autoregressive, video diffusion, world model, dit  
- **[Demystifing Video Reasoning](https://arxiv.org/abs/2603.16870v1)**  
  Authors: Ruisi Wang, Zhongang Cai, Fanyi Pu, Junxiang Xu, Wanqi Yin, Maijunxian Wang, Ran Ji, Chenyang Gu, Bo Li, Ziqi Huang, Hokin Deng, Dahua Lin, Ziwei Liu, Lei Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16870v1.pdf)  
  Keywords: video generation, denoising, dynamics, diffusion transformer, concept  
- **[Search2Motion: Training-Free Object-Level Motion Control via Attention-Consensus Search](https://arxiv.org/abs/2603.16711v2)**  
  Authors: Sainan Liu, Tz-Ying Wu, Hector A Valdez, Subarna Tripathi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16711v2.pdf)  
  Keywords: motion control, video generation, benchmark, evaluation, dynamics, dit, image-to-video  

### Surveys & Benchmarks

*Showing the latest 50 out of 192 papers*

- **[The Unreasonable Effectiveness of Text Embedding Interpolation for Continuous Image Steering](https://arxiv.org/abs/2603.17998v1)**  
  Authors: Yigit Ekin, Yossi Gandelsman  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17998v1.pdf)  
  Keywords: video generation, evaluation, dit, concept, controllable  
- **[Video Understanding: From Geometry and Semantics to Unified Models](https://arxiv.org/abs/2603.17840v1)**  
  Authors: Zhaochong An, Zirui Li, Mingqiao Ye, Feng Qiao, Jiaang Li, Zongwei Wu, Vishal Thengane, Chengzu Li, Lei Li, Luc Van Gool, Guolei Sun, Serge Belongie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17840v1.pdf)  
  Keywords: survey, dynamics  
- **[EVA: Aligning Video World Models with Executable Robot Actions via Inverse Dynamics Rewards](https://arxiv.org/abs/2603.17808v1)**  
  Authors: Ruixiang Wang, Qingming Liu, Yueci Deng, Guiliang Liu, Zhen Liu, Kui Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17808v1.pdf)  
  Keywords: physical, efficient, video generation, robotics, benchmark, dynamics, dit, world model, acceleration  
- **[Learning Transferable Temporal Primitives for Video Reasoning via Synthetic Videos](https://arxiv.org/abs/2603.17693v1)**  
  Authors: Songtao Jiang, Sibo Song, Chenyi Zhou, Yuan Wang, Ruizhe Chen, Tongkun Guan, Ruilin Luo, Yan Zhang, Zhihang Tang, Yuchong Sun, Hang Zhang, Zhibo Yang, Shuai Bai, Junyang Lin, Zuozhu Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17693v1.pdf)  
  Keywords: image to video, efficient, video generation, benchmark, dynamics  
- **[Stereo World Model: Camera-Guided Stereo Video Generation](https://arxiv.org/abs/2603.17375v1)**  
  Authors: Yang-Tian Sun, Zehuan Huang, Yifan Niu, Lin Ma, Yan-Pei Cao, Yuewen Ma, Xiaojuan Qi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17375v1.pdf)  
  Keywords: efficient, video generation, interactive, benchmark, dit, world model, distillation  
- **[Search2Motion: Training-Free Object-Level Motion Control via Attention-Consensus Search](https://arxiv.org/abs/2603.16711v2)**  
  Authors: Sainan Liu, Tz-Ying Wu, Hector A Valdez, Subarna Tripathi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16711v2.pdf)  
  Keywords: motion control, video generation, benchmark, evaluation, dynamics, dit, image-to-video  
- **[Fanar 2.0: Arabic Generative AI Stack](https://arxiv.org/abs/2603.16397v1)**  
  Authors: FANAR TEAM, Ummar Abbas, Mohammad Shahmeer Ahmad, Minhaj Ahmad, Abdulaziz Al-Homaid, Anas Al-Nuaimi, Enes Altinisik, Ehsaneddin Asgari, Sanjay Chawla, Shammur Chowdhury, Fahim Dalvi, Kareem Darwish, Nadir Durrani, Mohamed Elfeky, Ahmed Elmagarmid, Mohamed Eltabakh, Asim Ersoy, Masoomali Fatehkia, Mohammed Qusay Hashim, Majd Hawasly, Mohamed Hefeeda, Mus'ab Husaini, Keivin Isufaj, Soon-Gyo Jung, Houssam Lachemat, Ji Kim Lucas, Abubakr Mohamed, Tasnim Mohiuddin, Basel Mousi, Hamdy Mubarak, Ahmad Musleh, Mourad Ouzzani, Amin Sadeghi, Husrev Taha Sencar, Mohammed Shinoy, Omar Sinan, Yifan Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16397v1.pdf)  
  Keywords: benchmark, long-form, architecture  
- **[VIGOR: VIdeo Geometry-Oriented Reward for Temporal Generative Alignment](https://arxiv.org/abs/2603.16271v1)**  
  Authors: Tengjiao Yin, Jinglei Shi, Heng Guo, Xi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16271v1.pdf)  
  Keywords: physical, efficient, evaluation, streaming, diffusion model, video diffusion, dit  
- **[Training-free Detection of Generated Videos via Spatial-Temporal Likelihoods](https://arxiv.org/abs/2603.15026v2)**  
  Authors: Omer Ben Hayun, Roy Betser, Meir Yossef Levi, Levi Kassel, Guy Gilboa  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15026v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://omerbenhayun.github.io/stall-video)  
  Keywords: benchmark, controllable, dynamics  
- **[Bridging Scene Generation and Planning: Driving with World Model via Unifying Vision and Motion Representation](https://arxiv.org/abs/2603.14948v1)**  
  Authors: Xingtai Gui, Meijie Zhang, Tianyi Yan, Wencheng Han, Jiahao Gong, Feiyang Tan, Cheng-zhong Xu, Jianbing Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14948v1.pdf)  
  Keywords: trajectory, video generation, multi-modal, benchmark, dynamics, dit, world model, autonomous driving  

### Text-to-Video Generation

*Showing the latest 50 out of 70 papers*

- **[Versatile Editing of Video Content, Actions, and Dynamics without Training](https://arxiv.org/abs/2603.17989v1)**  
  Authors: Vladimir Kulikov, Roni Paiss, Andrey Voynov, Inbar Mosseri, Tali Dekel, Tomer Michaeli  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17989v1.pdf)  
  Keywords: video generation, video editing, dynamics, dit, text-to-video  
- **[Steering Video Diffusion Transformers with Massive Activations](https://arxiv.org/abs/2603.17825v1)**  
  Authors: Xianhang Cheng, Yujian Zheng, Zhenyu Xie, Tingting Liao, Hao Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17825v1.pdf)  
  Keywords: text-to-video, diffusion transformer, video diffusion, video generation  
- **[GenState-AI: State-Aware Dataset for Text-to-Video Retrieval on AI-Generated Videos](https://arxiv.org/abs/2603.14426v1)**  
  Authors: Minghan Li, Tongna Chen, Tianrui Lv, Yishuai Zhang, Suchao An, Guodong Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14426v1.pdf)  
  Keywords: benchmark, i2v, evaluation, dit, text-to-video, controllable  
- **[Early Failure Detection and Intervention in Video Diffusion Models](https://arxiv.org/abs/2603.14320v1)**  
  Authors: Kwon Byung-Ki, Sohwi Lim, Nam Hyeon-Woo, Moon Ye-Bin, Tae-Hyun Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14320v1.pdf)  
  Keywords: efficient, denoising, t2v, diffusion model, video diffusion, text-to-video  
- **[MotionCFG: Boosting Motion Dynamics via Stochastic Concept Perturbation](https://arxiv.org/abs/2603.14073v1)**  
  Authors: Byungjun Kim, Soobin Um, Jong Chul Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14073v1.pdf)  
  Keywords: denoising, t2v, dynamics, identity, dit, concept, text-to-video  
- **[UniVid: Pyramid Diffusion Model for High Quality Video Generation](https://arxiv.org/abs/2603.13739v1)**  
  Authors: Xinyu Xiao, Binbin Yang, Tingtian Li, Yipeng Yu, Sen Lei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.13739v1.pdf)  
  Keywords: video generation, i2v, t2v, diffusion model, dit, image-to-video, text-to-video  
- **[VQQA: An Agentic Approach for Video Evaluation and Quality Improvement](https://arxiv.org/abs/2603.12310v1)**  
  Authors: Yiwen Song, Tomas Pfister, Yale Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.12310v1.pdf)  
  Keywords: efficient, video generation, i2v, evaluation, t2v, dit, image-to-video, text-to-video  
- **[OSCBench: Benchmarking Object State Change in Text-to-Video Generation](https://arxiv.org/abs/2603.11698v1)**  
  Authors: Xianjing Han, Bin Zhu, Shiqi Hu, Franklin Mingzhe Li, Patrick Carrington, Roger Zimmermann, Jingjing Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.11698v1.pdf)  
  Keywords: physical, video generation, benchmark, t2v, evaluation, text-to-video  
- **[ShotVerse: Advancing Cinematic Camera Control for Text-Driven Multi-Shot Video Creation](https://arxiv.org/abs/2603.11421v1)**  
  Authors: Songlin Yang, Zhe Wang, Xuyi Yang, Songchun Zhang, Xianghao Kong, Taiyi Wu, Xiaotong Zhao, Ran Zhang, Alan Zhao, Anyi Rao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.11421v1.pdf)  
  Keywords: trajectory, video generation, film, evaluation, dit, text-driven video, camera control  
- **[Event-Driven Video Generation](https://arxiv.org/abs/2603.13402v2)**  
  Authors: Chika Maduabuchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.13402v2.pdf)  
  Keywords: video generation, denoising, dynamics, dit, text-to-video  

### Video Editing

- **[Versatile Editing of Video Content, Actions, and Dynamics without Training](https://arxiv.org/abs/2603.17989v1)**  
  Authors: Vladimir Kulikov, Roni Paiss, Andrey Voynov, Inbar Mosseri, Tali Dekel, Tomer Michaeli  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17989v1.pdf)  
  Keywords: video generation, video editing, dynamics, dit, text-to-video  
- **[Script-to-Slide Grounding: Grounding Script Sentences to Slide Objects for Automatic Instructional Video Generation](https://arxiv.org/abs/2603.16931v1)**  
  Authors: Rena Suzuki, Masato Kikuchi, Tadachika Ozono  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16931v1.pdf)  
  Keywords: dit, education, video editing, video generation  
- **[SAW: Toward a Surgical Action World Model via Controllable and Scalable Video Generation](https://arxiv.org/abs/2603.13024v1)**  
  Authors: Sampath Rapuri, Lalithkumar Seenivasan, Dominik Schneider, Roger Soberanis-Mukul, Yufan He, Hao Ding, Jiru Xu, Chenhao Yu, Chenyan Jing, Pengfei Guo, Daguang Xu, Mathias Unberath  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.13024v1.pdf)  
  Keywords: trajectory, video-to-video, video generation, temporal consistency, diffusion model, video diffusion, world model, simulation, dit, controllable  
- **[When to Lock Attention: Training-Free KV Control in Video Diffusion](https://arxiv.org/abs/2603.09657v1)**  
  Authors: Tianyi Zeng, Jincheng Gao, Tianyi Wang, Zijie Meng, Miao Zhang, Jun Yin, Haoyuan Sun, Junfeng Jiao, Christian Claudel, Junbo Tan, Xueqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09657v1.pdf)  
  Keywords: denoising, video editing, dit, diffusion model, video diffusion  
- **[Place-it-R1: Unlocking Environment-aware Reasoning Potential of MLLM for Video Object Insertion](https://arxiv.org/abs/2603.06140v1)**  
  Authors: Bohai Gu, Taiyi Wu, Dazhao Du, Jian Liu, Shuai Yang, Xiaotong Zhao, Alan Zhao, Song Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06140v1.pdf)  
  Keywords: physical, video editing, dit, diffusion model, video diffusion  
- **[GenHOI: Towards Object-Consistent Hand-Object Interaction with Temporally Balanced and Spatially Selective Object Injection](https://arxiv.org/abs/2603.06048v1)**  
  Authors: Xuan Huang, Mochu Xiang, Zhelun Shen, Jinbo Wu, Chenming Wu, Chen Zhao, Kaisiyuan Wang, Hang Zhou, Shanshan Liu, Haocheng Feng, Wei He, Jingdong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06048v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xuanhuang0.github.io/GenHOI)  
  Keywords: physical, video generation, video editing, evaluation, video synthesis, identity, dit  
- **[Training-free Latent Inter-Frame Pruning with Attention Recovery](https://arxiv.org/abs/2603.05811v1)**  
  Authors: Dennis Menn, Yuedong Yang, Bokun Wang, Xiwen Wei, Mustafa Munir, Feng Liang, Radu Marculescu, Chenfeng Xu, Diana Marculescu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05811v1.pdf)  
  Keywords: dit, video editing, video generation  
- **[FREE-Edit: Using Editing-aware Injection in Rectified Flow Models for Zero-shot Image-Driven Video Editing](https://arxiv.org/abs/2603.01164v1)**  
  Authors: Maomao Li, Yunfei Liu, Yu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01164v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://free-edit.github.io/page)  
  Keywords: image-driven, i2v, video editing, denoising, rectified flow, dit, image-to-video, layout  
- **[UniVBench: Towards Unified Evaluation for Video Foundation Models](https://arxiv.org/abs/2602.21835v2)**  
  Authors: Jianhui Wei, Xiaotian Zhang, Yichen Li, Yuan Wang, Yan Zhang, Ziyi Chen, Zhihang Tang, Wei Xu, Zuozhu Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21835v2.pdf)  
  Keywords: video generation, benchmark, video editing, evaluation, dit  
- **[SkyReels-V4: Multi-modal Video-Audio Generation, Inpainting and Editing model](https://arxiv.org/abs/2602.21818v3)**  
  Authors: Guibin Chen, Dixuan Lin, Jiangping Yang, Youqiang Zhang, Zhengcong Fei, Debang Li, Sheng Chen, Chaofeng Ao, Nuo Pang, Yiming Wang, Yikun Dou, Zheng Chen, Mingyuan Fan, Tuanhui Li, Mingshan Chang, Hao Zhang, Xiaopeng Sun, Jingtao Xu, Yuqiang Xie, Jiahua Wang, Zhiheng Xu, Weiming Xiong, Yuzhe Jin, Baoxuan Gu, Binjie Mao, Yunjie Yu, Jujie He, Yuhao Feng, Shiwen Tu, Chaojie Wang, Rui Yan, Wei Shen, Jingchen Wu, Peng Zhao, Xuanyue Zhong, Zhuangzhuang Liu, Kaifei Wang, Fuxiang Zhang, Weikai Xu, Wenyan Liu, Binglu Zhang, Yu Shen, Tianhui Xiong, Bin Peng, Liang Zeng, Xuchen Song, Haoxiang Guo, Peiyu Wang, Max W. Y. Lam, Chien-Hung Liu, Yahui Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21818v3.pdf)  
  Keywords: image to video, video generation, multi-modal, architecture, video editing, style, diffusion transformer, frame interpolation, dit, sound, super-resolution  

### Video Inpainting & Completion

- **[ChopGrad: Pixel-Wise Losses for Latent Video Diffusion via Truncated Backpropagation](https://arxiv.org/abs/2603.17812v1)**  
  Authors: Dmitriy Rivkin, Parker Ewen, Lili Gao, Julian Ost, Stefanie Walz, Rasika Kangutkar, Mario Bijelic, Felix Heide  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17812v1.pdf)  
  Keywords: latent video, video inpainting, efficient, video generation, video enhancement, diffusion model, video diffusion, dit, super-resolution  
- **[ConfCtrl: Enabling Precise Camera Control in Video Diffusion via Confidence-Aware Interpolation](https://arxiv.org/abs/2603.09819v1)**  
  Authors: Liudi Yang, George Eskandar, Fengyi Shen, Mohammad Altillawi, Yang Bai, Chi Zhang, Ziyuan Liu, Abhinav Valada  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09819v1.pdf)  
  Keywords: novel view, dit, diffusion model, video diffusion, video interpolation, camera control  
- **[Pinterest Canvas: Large-Scale Image Generation at Pinterest](https://arxiv.org/abs/2603.06453v1)**  
  Authors: Yu Wang, Eric Tzeng, Raymond Shiau, Jie Yang, Dmitry Kislyuk, Charles Rosenberg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06453v1.pdf)  
  Keywords: outpainting, video generation, dit, diffusion model, image-to-video  
- **[Learning Physics-Grounded 4D Dynamics with Neural Gaussian Force Fields](https://arxiv.org/abs/2602.00148v2)**  
  Authors: Shiqian Li, Ruihong Shen, Junfeng Ni, Chang Pan, Chi Zhang, Yixin Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.00148v2.pdf)  
  Keywords: physical, video generation, interactive, video prediction, evaluation, dynamics, physics, world model, simulation  

### Video Super-Resolution & Enhancement

*Showing the latest 50 out of 60 papers*

- **[ChopGrad: Pixel-Wise Losses for Latent Video Diffusion via Truncated Backpropagation](https://arxiv.org/abs/2603.17812v1)**  
  Authors: Dmitriy Rivkin, Parker Ewen, Lili Gao, Julian Ost, Stefanie Walz, Rasika Kangutkar, Mario Bijelic, Felix Heide  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17812v1.pdf)  
  Keywords: latent video, video inpainting, efficient, video generation, video enhancement, diffusion model, video diffusion, dit, super-resolution  
- **[FrescoDiffusion: 4K Image-to-Video with Prior-Regularized Tiled Diffusion](https://arxiv.org/abs/2603.17555v1)**  
  Authors: Hugo Caselles-Dupré, Mathis Koroglu, Guillaume Jeanneret, Arnaud Dapogny, Matthieu Cord  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17555v1.pdf)  
  Keywords: trajectory, efficient, denoising, i2v, dit, image-to-video, layout  
- **[Motion-Adaptive Temporal Attention for Lightweight Video Generation with Stable Diffusion](https://arxiv.org/abs/2603.17398v1)**  
  Authors: Rui Hong, Shuxue Quan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17398v1.pdf)  
  Keywords: efficient, video generation, denoising, temporal consistency, diffusion model  
- **[Demystifing Video Reasoning](https://arxiv.org/abs/2603.16870v1)**  
  Authors: Ruisi Wang, Zhongang Cai, Fanyi Pu, Junxiang Xu, Wanqi Yin, Maijunxian Wang, Ran Ji, Chenyang Gu, Bo Li, Ziqi Huang, Hokin Deng, Dahua Lin, Ziwei Liu, Lei Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16870v1.pdf)  
  Keywords: video generation, denoising, dynamics, diffusion transformer, concept  
- **[S-VAM: Shortcut Video-Action Model by Self-Distilling Geometric and Semantic Foresight](https://arxiv.org/abs/2603.16195v2)**  
  Authors: Haodong Yan, Zhide Zhong, Jiaguan Zhu, Junjie He, Weilin Yuan, Wenxuan Song, Xin Gong, Yingjie Cai, Guanyi Zhao, Xu Yan, Bingbing Liu, Ying-Cong Chen, Haoang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16195v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://haodong-yan.github.io/S-VAM)  
  Keywords: efficient, video generation, denoising, diffusion model, simulation, distillation  
- **[Edit2Interp: Adapting Image Foundation Models from Spatial Editing to Video Frame Interpolation with Few-Shot Learning](https://arxiv.org/abs/2603.15003v1)**  
  Authors: Nasrin Rahimi, Mısra Yavuz, Burak Can Biner, Yunus Bilge Kurt, Ahmet Rasim Emirdağı, Süleyman Aslan, Görkay Aydemir, M. Akın Yılmaz, A. Murat Tekalp  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15003v1.pdf)  
  Keywords: efficient, architecture, video synthesis, dit, frame interpolation  
- **[LatSearch: Latent Reward-Guided Search for Faster Inference-Time Scaling in Video Diffusion](https://arxiv.org/abs/2603.14526v1)**  
  Authors: Zengqun Zhao, Ziquan Liu, Yu Cao, Shaogang Gong, Zhensong Zhang, Jifei Song, Jiankang Deng, Ioannis Patras  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14526v1.pdf)  
  Keywords: trajectory, efficient, video generation, benchmark, denoising, evaluation, video diffusion  
- **[Early Failure Detection and Intervention in Video Diffusion Models](https://arxiv.org/abs/2603.14320v1)**  
  Authors: Kwon Byung-Ki, Sohwi Lim, Nam Hyeon-Woo, Moon Ye-Bin, Tae-Hyun Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14320v1.pdf)  
  Keywords: efficient, denoising, t2v, diffusion model, video diffusion, text-to-video  
- **[Seeking Physics in Diffusion Noise](https://arxiv.org/abs/2603.14294v1)**  
  Authors: Chujun Tang, Lei Zhong, Fangqiang Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14294v1.pdf)  
  Keywords: trajectory, physical, denoising, identity, physics, diffusion transformer, diffusion model, video diffusion, dit  
- **[MotionCFG: Boosting Motion Dynamics via Stochastic Concept Perturbation](https://arxiv.org/abs/2603.14073v1)**  
  Authors: Byungjun Kim, Soobin Um, Jong Chul Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14073v1.pdf)  
  Keywords: denoising, t2v, dynamics, identity, dit, concept, text-to-video  

### World Models & Simulation

*Showing the latest 50 out of 95 papers*

- **[EVA: Aligning Video World Models with Executable Robot Actions via Inverse Dynamics Rewards](https://arxiv.org/abs/2603.17808v1)**  
  Authors: Ruixiang Wang, Qingming Liu, Yueci Deng, Guiliang Liu, Zhen Liu, Kui Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17808v1.pdf)  
  Keywords: physical, efficient, video generation, robotics, benchmark, dynamics, dit, world model, acceleration  
- **[Stereo World Model: Camera-Guided Stereo Video Generation](https://arxiv.org/abs/2603.17375v1)**  
  Authors: Yang-Tian Sun, Zehuan Huang, Yifan Niu, Lin Ma, Yan-Pei Cao, Yuewen Ma, Xiaojuan Qi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17375v1.pdf)  
  Keywords: efficient, video generation, interactive, benchmark, dit, world model, distillation  
- **[MosaicMem: Hybrid Spatial Memory for Controllable Video World Models](https://arxiv.org/abs/2603.17117v1)**  
  Authors: Wei Yu, Runjia Qian, Yumeng Li, Liquan Wang, Songheng Yin, Sri Siddarth Chakaravarthy P, Dennis Anthony, Yang Ye, Yidi Li, Weiwei Wan, Animesh Garg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17117v1.pdf)  
  Keywords: diffusion model, autoregressive, video diffusion, world model, dit, controllable, world simulator  
- **[WorldCam: Interactive Autoregressive 3D Gaming Worlds with Camera Pose as a Unifying Geometric Representation](https://arxiv.org/abs/2603.16871v1)**  
  Authors: Jisu Nam, Yicong Hong, Chun-Hao Paul Huang, Feng Liu, JoungBin Lee, Jiyoung Kim, Siyoon Jin, Yunsung Lee, Jaeyoon Jung, Suhwan Choi, Seungryong Kim, Yang Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16871v1.pdf)  
  Keywords: interactive, physics, diffusion transformer, autoregressive, video diffusion, world model, dit  
- **[Kinema4D: Kinematic 4D World Modeling for Spatiotemporal Embodied Simulation](https://arxiv.org/abs/2603.16669v1)**  
  Authors: Mutian Xu, Tianbao Zhang, Tianqi Liu, Zhaoxi Chen, Xiaoguang Han, Ziwei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16669v1.pdf)  
  Keywords: trajectory, physical, video generation, interactive, dynamics, dit, world model, simulation, action-conditioned  
- **[S-VAM: Shortcut Video-Action Model by Self-Distilling Geometric and Semantic Foresight](https://arxiv.org/abs/2603.16195v2)**  
  Authors: Haodong Yan, Zhide Zhong, Jiaguan Zhu, Junjie He, Weilin Yuan, Wenxuan Song, Xin Gong, Yingjie Cai, Guanyi Zhao, Xu Yan, Bingbing Liu, Ying-Cong Chen, Haoang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16195v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://haodong-yan.github.io/S-VAM)  
  Keywords: efficient, video generation, denoising, diffusion model, simulation, distillation  
- **[Grounding World Simulation Models in a Real-World Metropolis](https://arxiv.org/abs/2603.15583v1)**  
  Authors: Junyoung Seo, Hyunwook Choi, Minkyung Kwon, Jinhyeok Choi, Siyoon Jin, Gayoung Lee, Junho Kim, JoungBin Lee, Geonmo Gu, Dongyoon Han, Sangdoo Yun, Seungryong Kim, Jin-Hwa Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15583v1.pdf)  
  Keywords: trajectory, video generation, dit, autoregressive, world model, simulation  
- **[Faster Inference of Flow-Based Generative Models via Improved Data-Noise Coupling](https://arxiv.org/abs/2603.15279v1)**  
  Authors: Aram Davtyan, Leello Tadesse Dadi, Volkan Cevher, Paolo Favaro  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15279v1.pdf)  
  Keywords: efficient, video generation, flow matching, dit, diffusion model, simulation, distillation  
- **[Bridging Scene Generation and Planning: Driving with World Model via Unifying Vision and Motion Representation](https://arxiv.org/abs/2603.14948v1)**  
  Authors: Xingtai Gui, Meijie Zhang, Tianyi Yan, Wencheng Han, Jiahao Gong, Feiyang Tan, Cheng-zhong Xu, Jianbing Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14948v1.pdf)  
  Keywords: trajectory, video generation, multi-modal, benchmark, dynamics, dit, world model, autonomous driving  
- **[FAR-Drive: Frame-AutoRegressive Video Generation in Closed-Loop Autonomous Driving](https://arxiv.org/abs/2603.14938v1)**  
  Authors: Yaoru Li, Federico Landi, Marco Godi, Xin Jin, Ruiju Fu, Yufei Ma, Muyang Sun, Heyu Si, Qi Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14938v1.pdf)  
  Keywords: video generation, interactive, evaluation, diffusion transformer, autoregressive, dit, simulation, autonomous driving, acceleration  



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
