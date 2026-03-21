# Awesome Video Diffusions [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Video Diffusion Models and Video Generation. Content is automatically updated daily.

> Last Update: 2026-03-21 02:01:53

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

- [3D-aware Video Generation](#3d-aware-video-generation) (27 papers) - Video generation with 3D awareness, multi-view consistency, and 4D content creation
- [Applications](#applications) (43 papers) - Domain-specific applications of video diffusion models
- [Architecture & Efficiency](#architecture-&-efficiency) (363 papers) - Architectural innovations (DiT, UNet), flow matching, and training/inference efficiency
- [Audio & Multi-modal](#audio-&-multi-modal) (30 papers) - Audio-driven and multi-modal conditioned video generation
- [Controllable Generation](#controllable-generation) (121 papers) - Controllable video generation with motion, camera, pose, or layout guidance
- [Human & Character Animation](#human-&-character-animation) (28 papers) - Human-centric video generation including talking heads, dance, and character animation
- [Image-to-Video Generation](#image-to-video-generation) (40 papers) - Methods for animating still images into videos
- [Long Video Generation](#long-video-generation) (119 papers) - Generating temporally consistent long-form videos beyond short clips
- [Personalization & Customization](#personalization-&-customization) (89 papers) - Personalized video generation with custom subjects, identities, or styles
- [Physical Understanding](#physical-understanding) (135 papers) - Physics-aware video generation and dynamics modeling
- [Surveys & Benchmarks](#surveys-&-benchmarks) (192 papers) - Survey papers, benchmarks, and evaluation metrics for video generation
- [Text-to-Video Generation](#text-to-video-generation) (68 papers) - Foundation models and methods for generating videos from text prompts
- [Video Editing](#video-editing) (32 papers) - Diffusion-based video editing, style transfer, and manipulation
- [Video Inpainting & Completion](#video-inpainting-&-completion) (4 papers) - Video inpainting, completion, outpainting, and temporal prediction
- [Video Super-Resolution & Enhancement](#video-super-resolution-&-enhancement) (59 papers) - Video quality improvement, upscaling, restoration, and frame interpolation
- [World Models & Simulation](#world-models-&-simulation) (93 papers) - Video generation as world simulators and interactive environment generation



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3D-aware Video Generation

- **[3DreamBooth: High-Fidelity 3D Subject-Driven Video Generation Model](https://arxiv.org/abs/2603.18524v1)**  
  Authors: Hyun-kyu Ko, Jihyeon Park, Younghyun Kim, Dongheok Park, Eunbyung Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18524v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ko-lani.github.io/3DreamBooth)  
  Keywords: subject-driven, 3d-aware, multi-view video, video generation, dit, novel view, customization, identity  
- **[TAPESTRY: From Geometry to Appearance via Consistent Turntable Videos](https://arxiv.org/abs/2603.17735v1)**  
  Authors: Yan Zeng, Haoran Jiang, Kaixin Yao, Qixuan Zhang, Longwen Zhang, Lan Xu, Jingyi Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17735v1.pdf)  
  Keywords: 3d-aware, video generation, dit, video diffusion, multi-modal, diffusion model  
- **[Tri-Prompting: Video Diffusion with Unified Control over Scene, Subject, and Motion](https://arxiv.org/abs/2603.15614v1)**  
  Authors: Zhenghong Zhou, Xiaohang Zhan, Zhiqin Chen, Soo Ye Kim, Nanxuan Zhao, Haitian Zheng, Qing Liu, He Zhang, Zhe Lin, Yuqian Zhou, Jiebo Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15614v1.pdf)  
  Keywords: architecture, 3d-aware, motion control, customization, dit, controllable, video diffusion, identity, diffusion model  
- **[GeoNVS: Geometry Grounded Video Diffusion for Novel View Synthesis](https://arxiv.org/abs/2603.14965v1)**  
  Authors: Minjun Kang, Inkyu Shin, Taeyeop Lee, Myungchul Kim, In So Kweon, Kuk-Jin Yoon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14965v1.pdf)  
  Keywords: dit, novel view, video diffusion, diffusion model, camera control  
- **[MVHOI: Bridge Multi-view Condition to Complex Human-Object Interaction Video Reenactment via 3D Foundation Model](https://arxiv.org/abs/2603.14686v1)**  
  Authors: Jinguang Tong, Jinbo Wu, Kaisiyuan Wang, Zhelun Shen, Xuan Huang, Mochu Xiang, Xuesong Li, Yingying Li, Haocheng Feng, Chen Zhao, Hang Zhou, Wei He, Chuong Nguyen, Jingdong Wang, Hongdong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14686v1.pdf)  
  Keywords: controllable, video generation, dit, novel view, dynamics  
- **[CamLit: Unified Video Diffusion with Explicit Camera and Lighting Control](https://arxiv.org/abs/2603.14241v1)**  
  Authors: Zhiyi Kuang, Chengan He, Egor Zakharov, Yuxuan Xue, Shunsuke Saito, Olivier Maury, Timur Bagautdinov, Youyi Zheng, Giljoo Nam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14241v1.pdf)  
  Keywords: video generation, novel view, video diffusion, trajectory, diffusion model  
- **[Ego-1K -- A Large-Scale Multiview Video Dataset for Egocentric Vision](https://arxiv.org/abs/2603.13741v1)**  
  Authors: Jae Yong Lee, Daniel Scharstein, Akash Bapat, Hao Hu, Andrew Fu, Haoru Zhao, Paul Sammut, Xiang Li, Stephen Jeapes, Anik Gupta, Lior David, Saketh Madhuvarasu, Jay Girish Joshi, Jason Wither  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.13741v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://huggingface.co/datasets/facebook/ego-1k.) | [![Dataset](https://img.shields.io/badge/-Dataset-orange)](https://huggingface.co/datasets/facebook/ego-1k)  
  Keywords: 3d video, benchmark, video synthesis, novel view  
- **[ConfCtrl: Enabling Precise Camera Control in Video Diffusion via Confidence-Aware Interpolation](https://arxiv.org/abs/2603.09819v1)**  
  Authors: Liudi Yang, George Eskandar, Fengyi Shen, Mohammad Altillawi, Yang Bai, Chi Zhang, Ziyuan Liu, Abhinav Valada  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09819v1.pdf)  
  Keywords: dit, novel view, video diffusion, video interpolation, diffusion model, camera control  
- **[Transformer-Based Inpainting for Real-Time 3D Streaming in Sparse Multi-Camera Setups](https://arxiv.org/abs/2603.05507v1)**  
  Authors: Leif Van Holland, Domenic Zingsheim, Mana Takhsha, Hannah Dröge, Patrick Stotko, Markus Plack, Reinhard Klein  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05507v1.pdf)  
  Keywords: architecture, streaming, dit, novel view  
- **[Orthogonal Spatial-temporal Distributional Transfer for 4D Generation](https://arxiv.org/abs/2603.05081v1)**  
  Authors: Wei Liu, Shengqiong Wu, Bobo Li, Haoyu Zhao, Hao Fei, Mong-Li Lee, Wynne Hsu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05081v1.pdf)  
  Keywords: video diffusion, temporal consistency, diffusion model, 4d generation  

### Applications

- **[Student views in AI Ethics and Social Impact](https://arxiv.org/abs/2603.18827v1)**  
  Authors: Tudor-Dan Mihoc, Manuela-Andreea Petrescu, Emilia-Loredana Pop  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18827v1.pdf)  
  Keywords: concept, education, autonomous driving, survey  
- **[EVA: Aligning Video World Models with Executable Robot Actions via Inverse Dynamics Rewards](https://arxiv.org/abs/2603.17808v1)**  
  Authors: Ruixiang Wang, Qingming Liu, Yueci Deng, Guiliang Liu, Zhen Liu, Kui Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17808v1.pdf)  
  Keywords: robotics, benchmark, world model, physical, video generation, dit, efficient, acceleration, dynamics  
- **[Surg$Σ$: A Spectrum of Large-Scale Multimodal Data and Foundation Models for Surgical Intelligence](https://arxiv.org/abs/2603.16822v1)**  
  Authors: Zhitao Zeng, Mengya Xu, Jian Jiang, Pengfei Guo, Yunqiu Xu, Zhu Zhuo, Chang Han Low, Yufan He, Dong Yang, Chenxi Lin, Yiming Gu, Jiaxin Guo, Yutong Ban, Daguang Xu, Qi Dou, Yueming Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16822v1.pdf)  
  Keywords: medical  
- **[Bridging Scene Generation and Planning: Driving with World Model via Unifying Vision and Motion Representation](https://arxiv.org/abs/2603.14948v1)**  
  Authors: Xingtai Gui, Meijie Zhang, Tianyi Yan, Wencheng Han, Jiahao Gong, Feiyang Tan, Cheng-zhong Xu, Jianbing Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14948v1.pdf)  
  Keywords: benchmark, autonomous driving, world model, video generation, dit, trajectory, multi-modal, dynamics  
- **[FAR-Drive: Frame-AutoRegressive Video Generation in Closed-Loop Autonomous Driving](https://arxiv.org/abs/2603.14938v1)**  
  Authors: Yaoru Li, Federico Landi, Marco Godi, Xin Jin, Ruiju Fu, Yufei Ma, Muyang Sun, Heyu Si, Qi Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14938v1.pdf)  
  Keywords: autonomous driving, autoregressive, simulation, diffusion transformer, video generation, dit, interactive, acceleration, evaluation  
- **[Script-to-Slide Grounding: Grounding Script Sentences to Slide Objects for Automatic Instructional Video Generation](https://arxiv.org/abs/2603.16931v1)**  
  Authors: Rena Suzuki, Masato Kikuchi, Tadachika Ozono  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16931v1.pdf)  
  Keywords: education, dit, video generation, video editing  
- **[PhysAlign: Physics-Coherent Image-to-Video Generation through Feature and 3D Representation Alignment](https://arxiv.org/abs/2603.13770v1)**  
  Authors: Zhexiao Xiong, Yizhi Song, Liu He, Wei Xiong, Yu Yuan, Feng Qiao, Nathan Jacobs  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.13770v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://physalign.github.io/PhysAlign)  
  Keywords: robotics, simulation, physics, physical, video generation, controllable, video diffusion, efficient, image-to-video, diffusion model, i2v  
- **[Risk-Controllable Multi-View Diffusion for Driving Scenario Generation](https://arxiv.org/abs/2603.11534v1)**  
  Authors: Hongyi Lin, Wenxiu Shi, Heye Huang, Dingyi Zhuang, Song Zhang, Yang Liu, Xiaobo Qu, Jinhua Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.11534v1.pdf)  
  Keywords: physical, autonomous driving, world model, controllable  
- **[ShotVerse: Advancing Cinematic Camera Control for Text-Driven Multi-Shot Video Creation](https://arxiv.org/abs/2603.11421v1)**  
  Authors: Songlin Yang, Zhe Wang, Xuyi Yang, Songchun Zhang, Xianghao Kong, Taiyi Wu, Xiaotong Zhao, Ran Zhang, Alan Zhao, Anyi Rao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.11421v1.pdf)  
  Keywords: film, text-driven video, video generation, dit, trajectory, evaluation, camera control  
- **[Motion Forcing: A Decoupled Framework for Robust Video Generation in Motion Dynamics](https://arxiv.org/abs/2603.10408v1)**  
  Authors: Tianshuo Xu, Zhifei Chen, Leyi Wu, Hao Lu, Ying-cong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.10408v1.pdf)  
  Keywords: robotics, benchmark, autonomous driving, physics, physical, video generation, evaluation, dynamics  

### Architecture & Efficiency

*Showing the latest 50 out of 363 papers*

- **[MonoArt: Progressive Structural Reasoning for Monocular Articulated 3D Reconstruction](https://arxiv.org/abs/2603.19231v1)**  
  Authors: Haitian Li, Haozhe Xie, Junxiang Xu, Beichen Wen, Fangzhou Hong, Ziwei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19231v1.pdf)  
  Keywords: architecture, video generation  
- **[Spectrally-Guided Diffusion Noise Schedules](https://arxiv.org/abs/2603.19222v1)**  
  Authors: Carlos Esteves, Ameesh Makadia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19222v1.pdf)  
  Keywords: diffusion model, denoising, video generation, dit  
- **[6Bit-Diffusion: Inference-Time Mixed-Precision Quantization for Video Diffusion Models](https://arxiv.org/abs/2603.18742v1)**  
  Authors: Rundong Su, Jintao Zhang, Zhihang Yuan, Haojie Duanmu, Jianfei Chen, Jun Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18742v1.pdf)  
  Keywords: temporal consistency, diffusion transformer, dit, video diffusion, acceleration, efficient, diffusion model  
- **[Training-Free Sparse Attention for Fast Video Generation via Offline Layer-Wise Sparsity Profiling and Online Bidirectional Co-Clustering](https://arxiv.org/abs/2603.18636v1)**  
  Authors: Jiayi Luo, Jiayu Chen, Jiankun Wang, Cong Wang, Hanxin Zhu, Qingyun Sun, Chen Gao, Zhibo Chen, Jianxin Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18636v1.pdf)  
  Keywords: dit, video generation, diffusion transformer  
- **[Improving Joint Audio-Video Generation with Cross-Modal Context Learning](https://arxiv.org/abs/2603.18600v1)**  
  Authors: Bingqi Ma, Linlong Lang, Ming Zhang, Dailan He, Xingtong Ge, Yi Zhang, Guanglu Song, Yu Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18600v1.pdf)  
  Keywords: architecture, video generation, dit, video diffusion, evaluation, diffusion model, multi-modal  
- **[3DreamBooth: High-Fidelity 3D Subject-Driven Video Generation Model](https://arxiv.org/abs/2603.18524v1)**  
  Authors: Hyun-kyu Ko, Jihyeon Park, Younghyun Kim, Dongheok Park, Eunbyung Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18524v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ko-lani.github.io/3DreamBooth)  
  Keywords: subject-driven, 3d-aware, multi-view video, video generation, dit, novel view, customization, identity  
- **[Efficient Video Diffusion with Sparse Information Transmission for Video Compression](https://arxiv.org/abs/2603.18501v1)**  
  Authors: Mingde Zhou, Zheng Chen, Yulun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18501v1.pdf) | [![GitHub](https://img.shields.io/github/stars/MingdeZhou/Diff-SIT?style=social)](https://github.com/MingdeZhou/Diff-SIT)  
  Keywords: temporal consistency, dit, video diffusion, efficient, diffusion model  
- **[The Unreasonable Effectiveness of Text Embedding Interpolation for Continuous Image Steering](https://arxiv.org/abs/2603.17998v1)**  
  Authors: Yigit Ekin, Yossi Gandelsman  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17998v1.pdf)  
  Keywords: video generation, dit, controllable, concept, evaluation  
- **[Versatile Editing of Video Content, Actions, and Dynamics without Training](https://arxiv.org/abs/2603.17989v1)**  
  Authors: Vladimir Kulikov, Roni Paiss, Andrey Voynov, Inbar Mosseri, Tali Dekel, Tomer Michaeli  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17989v1.pdf)  
  Keywords: text-to-video, video editing, video generation, dit, dynamics  
- **[AHOY! Animatable Humans under Occlusion from YouTube Videos with Gaussian Splatting and Video Diffusion Priors](https://arxiv.org/abs/2603.17975v1)**  
  Authors: Aymen Mir, Riza Alp Guler, Xiangjun Tang, Peter Wonka, Gerard Pons-Moll  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17975v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://miraymen.github.io/ahoy)  
  Keywords: architecture, avatar, video diffusion, identity, diffusion model  

### Audio & Multi-modal

- **[Improving Joint Audio-Video Generation with Cross-Modal Context Learning](https://arxiv.org/abs/2603.18600v1)**  
  Authors: Bingqi Ma, Linlong Lang, Ming Zhang, Dailan He, Xingtong Ge, Yi Zhang, Guanglu Song, Yu Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18600v1.pdf)  
  Keywords: architecture, video generation, dit, video diffusion, evaluation, diffusion model, multi-modal  
- **[Insight-V++: Towards Advanced Long-Chain Visual Reasoning with Multimodal Large Language Models](https://arxiv.org/abs/2603.18118v1)**  
  Authors: Yuhao Dong, Zuyan Liu, Shulin Tian, Yongming Rao, Ziwei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18118v1.pdf)  
  Keywords: architecture, benchmark, dit, multi-modal  
- **[TAPESTRY: From Geometry to Appearance via Consistent Turntable Videos](https://arxiv.org/abs/2603.17735v1)**  
  Authors: Yan Zeng, Haoran Jiang, Kaixin Yao, Qixuan Zhang, Longwen Zhang, Lan Xu, Jingyi Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17735v1.pdf)  
  Keywords: 3d-aware, video generation, dit, video diffusion, multi-modal, diffusion model  
- **[Bridging Scene Generation and Planning: Driving with World Model via Unifying Vision and Motion Representation](https://arxiv.org/abs/2603.14948v1)**  
  Authors: Xingtai Gui, Meijie Zhang, Tianyi Yan, Wencheng Han, Jiahao Gong, Feiyang Tan, Cheng-zhong Xu, Jianbing Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14948v1.pdf)  
  Keywords: benchmark, autonomous driving, world model, video generation, dit, trajectory, multi-modal, dynamics  
- **[V-JEPA 2.1: Unlocking Dense Features in Video Self-Supervised Learning](https://arxiv.org/abs/2603.14482v2)**  
  Authors: Lorenzo Mur-Labadia, Matthew Muckley, Amir Bar, Mido Assran, Koustuv Sinha, Mike Rabbat, Yann LeCun, Nicolas Ballas, Adrien Bardes  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14482v2.pdf)  
  Keywords: world model, benchmark, multi-modal  
- **[Fuel Gauge: Estimating Chain-of-Thought Length Ahead of Time in Large Multimodal Models](https://arxiv.org/abs/2603.10335v1)**  
  Authors: Yuedong Yang, Xiwen Wei, Mustafa Munir, Radu Marculescu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.10335v1.pdf)  
  Keywords: efficient, benchmark, multi-modal  
- **[ID-LoRA: Identity-Driven Audio-Video Personalization with In-Context LoRA](https://arxiv.org/abs/2603.10256v1)**  
  Authors: Aviad Dahan, Moran Yanuka, Noa Kraicer, Lior Wolf, Raja Giryes  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.10256v1.pdf)  
  Keywords: style, personalization, physical, sound, dit, video diffusion, identity, efficient, denoising  
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
  Keywords: efficient, multi-modal, video generation, streaming  

### Controllable Generation

*Showing the latest 50 out of 121 papers*

- **[PhysVideo: Physically Plausible Video Generation with Cross-View Geometry Guidance](https://arxiv.org/abs/2603.18639v1)**  
  Authors: Cong Wang, Hanxin Zhu, Xiao Tang, Jiayi Luo, Xin Jin, Long Chen, Fei-Yue Wang, Zhibo Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18639v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://anonymous.4open.science/w/Phys4D)  
  Keywords: temporal consistency, physics, physical, video generation, controllable, physics-aware, dynamics, video synthesis  
- **[The Unreasonable Effectiveness of Text Embedding Interpolation for Continuous Image Steering](https://arxiv.org/abs/2603.17998v1)**  
  Authors: Yigit Ekin, Yossi Gandelsman  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17998v1.pdf)  
  Keywords: video generation, dit, controllable, concept, evaluation  
- **[FrescoDiffusion: 4K Image-to-Video with Prior-Regularized Tiled Diffusion](https://arxiv.org/abs/2603.17555v1)**  
  Authors: Hugo Caselles-Dupré, Mathis Koroglu, Guillaume Jeanneret, Arnaud Dapogny, Matthieu Cord  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17555v1.pdf)  
  Keywords: layout, efficient, dit, i2v, trajectory, image-to-video, denoising  
- **[MosaicMem: Hybrid Spatial Memory for Controllable Video World Models](https://arxiv.org/abs/2603.17117v1)**  
  Authors: Wei Yu, Runjia Qian, Yumeng Li, Liquan Wang, Songheng Yin, Sri Siddarth Chakaravarthy P, Dennis Anthony, Yang Ye, Yidi Li, Weiwei Wan, Animesh Garg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17117v1.pdf)  
  Keywords: world simulator, autoregressive, world model, dit, controllable, video diffusion, diffusion model  
- **[Search2Motion: Training-Free Object-Level Motion Control via Attention-Consensus Search](https://arxiv.org/abs/2603.16711v2)**  
  Authors: Sainan Liu, Tz-Ying Wu, Hector A Valdez, Subarna Tripathi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16711v2.pdf)  
  Keywords: benchmark, evaluation, motion control, video generation, dit, image-to-video, dynamics  
- **[Kinema4D: Kinematic 4D World Modeling for Spatiotemporal Embodied Simulation](https://arxiv.org/abs/2603.16669v1)**  
  Authors: Mutian Xu, Tianbao Zhang, Tianqi Liu, Zhaoxi Chen, Xiaoguang Han, Ziwei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16669v1.pdf)  
  Keywords: action-conditioned, simulation, world model, physical, video generation, dit, interactive, trajectory, dynamics  
- **[Tri-Prompting: Video Diffusion with Unified Control over Scene, Subject, and Motion](https://arxiv.org/abs/2603.15614v1)**  
  Authors: Zhenghong Zhou, Xiaohang Zhan, Zhiqin Chen, Soo Ye Kim, Nanxuan Zhao, Haitian Zheng, Qing Liu, He Zhang, Zhe Lin, Yuqian Zhou, Jiebo Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15614v1.pdf)  
  Keywords: architecture, 3d-aware, motion control, customization, dit, controllable, video diffusion, identity, diffusion model  
- **[Grounding World Simulation Models in a Real-World Metropolis](https://arxiv.org/abs/2603.15583v1)**  
  Authors: Junyoung Seo, Hyunwook Choi, Minkyung Kwon, Jinhyeok Choi, Siyoon Jin, Gayoung Lee, Junho Kim, JoungBin Lee, Geonmo Gu, Dongyoon Han, Sangdoo Yun, Seungryong Kim, Jin-Hwa Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15583v1.pdf)  
  Keywords: autoregressive, simulation, world model, video generation, dit, trajectory  
- **[ViFeEdit: A Video-Free Tuner of Your Video Diffusion Transformer](https://arxiv.org/abs/2603.15478v1)**  
  Authors: Ruonan Yu, Zhenxiong Tan, Zigeng Chen, Songhua Liu, Xinchao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15478v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Lexie-YU/ViFeEdit?style=social)](https://github.com/Lexie-YU/ViFeEdit)  
  Keywords: temporal consistency, diffusion transformer, video generation, dit, controllable, video diffusion, diffusion model  
- **[AnyCrowd: Instance-Isolated Identity-Pose Binding for Arbitrary Multi-Character Animation](https://arxiv.org/abs/2603.15415v1)**  
  Authors: Zhenyu Xie, Ji Xia, Michael Kampffmeyer, Panwen Hu, Zehua Ma, Yujian Zheng, Jing Wang, Zheng Chong, Xujie Zhang, Xianhang Cheng, Xiaodan Liang, Hao Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15415v1.pdf)  
  Keywords: diffusion transformer, video generation, dit, controllable, identity  

### Human & Character Animation

- **[AHOY! Animatable Humans under Occlusion from YouTube Videos with Gaussian Splatting and Video Diffusion Priors](https://arxiv.org/abs/2603.17975v1)**  
  Authors: Aymen Mir, Riza Alp Guler, Xiangjun Tang, Peter Wonka, Gerard Pons-Moll  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17975v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://miraymen.github.io/ahoy)  
  Keywords: architecture, avatar, video diffusion, identity, diffusion model  
- **[SoulX-LiveAct: Towards Hour-Scale Real-Time Human Animation with Neighbor Forcing and ConvKV Memory](https://arxiv.org/abs/2603.11746v2)**  
  Authors: Dingcheng Zhen, Xu Zheng, Ruixin Zhang, Zhiqi Jiang, Yichao Yan, Ming Tao, Shunshun Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.11746v2.pdf)  
  Keywords: autoregressive, human animation, streaming, video generation, dit, efficient, diffusion model, video synthesis  
- **[Controllable Complex Human Motion Video Generation via Text-to-Skeleton Cascades](https://arxiv.org/abs/2603.08028v1)**  
  Authors: Ashkan Taghipour, Morteza Ghahremani, Zinuo Li, Hamid Laga, Farid Boussaid, Mohammed Bennamoun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08028v1.pdf)  
  Keywords: benchmark, temporal consistency, autoregressive, human motion, motion control, video generation, dit, controllable, video diffusion, diffusion model  
- **[ArtHOI: Articulated Human-Object Interaction Synthesis by 4D Reconstruction from Video Priors](https://arxiv.org/abs/2603.04338v1)**  
  Authors: Zihao Huang, Tianqi Liu, Zhaoxi Chen, Shaocong Xu, Saining Zhang, Lixing Xiao, Zhiguo Cao, Wei Li, Hao Zhao, Ziwei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.04338v1.pdf)  
  Keywords: human motion, physical, dit, video diffusion, diffusion model  
- **[Direct Reward Fine-Tuning on Poses for Single Image to 3D Human in the Wild](https://arxiv.org/abs/2603.02619v1)**  
  Authors: Seunguk Do, Minwoo Huh, Joonghyuk Shin, Jaesik Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02619v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://seunguk-do.github.io/drpose)  
  Keywords: benchmark, human motion, dit, evaluation, diffusion model  
- **[LiftAvatar: Kinematic-Space Completion for Expression-Controlled 3D Gaussian Avatar Animation](https://arxiv.org/abs/2603.02129v1)**  
  Authors: Hualiang Wei, Shunran Jia, Jialun Liu, Wenhui Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02129v1.pdf)  
  Keywords: avatar, diffusion transformer, dit, controllable, video diffusion, efficient, distillation  
- **[Non-verbal Real-time Human-AI Interaction in Constrained Robotic Environments](https://arxiv.org/abs/2603.01804v1)**  
  Authors: Dragos Costea, Alina Marcu, Cristina Lazar, Marius Leordeanu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01804v1.pdf)  
  Keywords: text-to-video, architecture, body motion  
- **[GeoDiff4D: Geometry-Aware Diffusion for 4D Head Avatar Reconstruction](https://arxiv.org/abs/2602.24161v2)**  
  Authors: Chao Xu, Xiaochen Zhao, Xiang Deng, Jingxiang Sun, Donglin Di, Zhuo Su, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.24161v2.pdf)  
  Keywords: identity, diffusion model, video generation, avatar  
- **[Spatio-Temporal Garment Reconstruction Using Diffusion Mapping via Pattern Coordinates](https://arxiv.org/abs/2602.24043v1)**  
  Authors: Yingxuan You, Ren Li, Corentin Dumery, Cong Cao, Hao Li, Pascal Fua  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.24043v1.pdf)  
  Keywords: temporal consistency, avatar, virtual try-on, dit, diffusion model  
- **[BigMaQ: A Big Macaque Motion and Animation Dataset Bridging Image and 3D Pose Representations](https://arxiv.org/abs/2602.19874v1)**  
  Authors: Lucas Martini, Alexander Lappe, Anna Bognár, Rufin Vogels, Martin A. Giese  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.19874v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://martinivis.github.io/BigMaQ)  
  Keywords: benchmark, dynamics, avatar  

### Image-to-Video Generation

- **[TransText: Alpha-as-RGB Representation for Transparent Text Animation](https://arxiv.org/abs/2603.17944v2)**  
  Authors: Fei Zhang, Zijian Zhou, Bohao Tang, Sen He, Hang Li, Zhe Wang, Soubhik Sanyal, Pengfei Liu, Viktar Atliha, Tao Xiang, Frost Xu, Semih Gunel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17944v2.pdf)  
  Keywords: image-to-video  
- **[Learning Transferable Temporal Primitives for Video Reasoning via Synthetic Videos](https://arxiv.org/abs/2603.17693v1)**  
  Authors: Songtao Jiang, Sibo Song, Chenyi Zhou, Yuan Wang, Ruizhe Chen, Tongkun Guan, Ruilin Luo, Yan Zhang, Zhihang Tang, Yuchong Sun, Hang Zhang, Zhibo Yang, Shuai Bai, Junyang Lin, Zuozhu Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17693v1.pdf)  
  Keywords: benchmark, image to video, video generation, efficient, dynamics  
- **[FrescoDiffusion: 4K Image-to-Video with Prior-Regularized Tiled Diffusion](https://arxiv.org/abs/2603.17555v1)**  
  Authors: Hugo Caselles-Dupré, Mathis Koroglu, Guillaume Jeanneret, Arnaud Dapogny, Matthieu Cord  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17555v1.pdf)  
  Keywords: layout, efficient, dit, i2v, trajectory, image-to-video, denoising  
- **[Search2Motion: Training-Free Object-Level Motion Control via Attention-Consensus Search](https://arxiv.org/abs/2603.16711v2)**  
  Authors: Sainan Liu, Tz-Ying Wu, Hector A Valdez, Subarna Tripathi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16711v2.pdf)  
  Keywords: benchmark, evaluation, motion control, video generation, dit, image-to-video, dynamics  
- **[GenState-AI: State-Aware Dataset for Text-to-Video Retrieval on AI-Generated Videos](https://arxiv.org/abs/2603.14426v1)**  
  Authors: Minghan Li, Tongna Chen, Tianrui Lv, Yishuai Zhang, Suchao An, Guodong Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14426v1.pdf)  
  Keywords: text-to-video, benchmark, dit, controllable, i2v, evaluation  
- **[PhysAlign: Physics-Coherent Image-to-Video Generation through Feature and 3D Representation Alignment](https://arxiv.org/abs/2603.13770v1)**  
  Authors: Zhexiao Xiong, Yizhi Song, Liu He, Wei Xiong, Yu Yuan, Feng Qiao, Nathan Jacobs  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.13770v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://physalign.github.io/PhysAlign)  
  Keywords: robotics, simulation, physics, physical, video generation, controllable, video diffusion, efficient, image-to-video, diffusion model, i2v  
- **[UniVid: Pyramid Diffusion Model for High Quality Video Generation](https://arxiv.org/abs/2603.13739v1)**  
  Authors: Xinyu Xiao, Binbin Yang, Tingtian Li, Yipeng Yu, Sen Lei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.13739v1.pdf)  
  Keywords: text-to-video, video generation, dit, t2v, i2v, image-to-video, diffusion model  
- **[CtrlAttack: A Unified Attack on World-Model Control in Diffusion Models](https://arxiv.org/abs/2603.13435v1)**  
  Authors: Shuhan Xu, Siyuan Liang, Hongling Zheng, Yong Luo, Han Hu, Lefei Zhang, Dacheng Tao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.13435v1.pdf)  
  Keywords: temporal consistency, dynamics, i2v, trajectory, image-to-video, diffusion model  
- **[VQQA: An Agentic Approach for Video Evaluation and Quality Improvement](https://arxiv.org/abs/2603.12310v1)**  
  Authors: Yiwen Song, Tomas Pfister, Yale Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.12310v1.pdf)  
  Keywords: text-to-video, evaluation, video generation, dit, t2v, i2v, efficient, image-to-video  
- **[SPIRAL: A Closed-Loop Framework for Self-Improving Action World Models via Reflective Planning Agents](https://arxiv.org/abs/2603.08403v2)**  
  Authors: Yu Yang, Yue Liao, Jianbiao Mei, Baisen Wang, Xuemeng Yang, Licheng Wen, Jiangning Zhang, Xiangtai Li, Hanlin Chen, Botian Shi, Yong Liu, Shuicheng Yan, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08403v2.pdf)  
  Keywords: benchmark, temporal consistency, world model, video generation, dit, controllable, i2v, evaluation  

### Long Video Generation

*Showing the latest 50 out of 119 papers*

- **[6Bit-Diffusion: Inference-Time Mixed-Precision Quantization for Video Diffusion Models](https://arxiv.org/abs/2603.18742v1)**  
  Authors: Rundong Su, Jintao Zhang, Zhihang Yuan, Haojie Duanmu, Jianfei Chen, Jun Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18742v1.pdf)  
  Keywords: temporal consistency, diffusion transformer, dit, video diffusion, acceleration, efficient, diffusion model  
- **[PhysVideo: Physically Plausible Video Generation with Cross-View Geometry Guidance](https://arxiv.org/abs/2603.18639v1)**  
  Authors: Cong Wang, Hanxin Zhu, Xiao Tang, Jiayi Luo, Xin Jin, Long Chen, Fei-Yue Wang, Zhibo Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18639v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://anonymous.4open.science/w/Phys4D)  
  Keywords: temporal consistency, physics, physical, video generation, controllable, physics-aware, dynamics, video synthesis  
- **[Efficient Video Diffusion with Sparse Information Transmission for Video Compression](https://arxiv.org/abs/2603.18501v1)**  
  Authors: Mingde Zhou, Zheng Chen, Yulun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18501v1.pdf) | [![GitHub](https://img.shields.io/github/stars/MingdeZhou/Diff-SIT?style=social)](https://github.com/MingdeZhou/Diff-SIT)  
  Keywords: temporal consistency, dit, video diffusion, efficient, diffusion model  
- **[AR-CoPO: Align Autoregressive Video Generation with Contrastive Policy Optimization](https://arxiv.org/abs/2603.17461v1)**  
  Authors: Dailan He, Guanlin Feng, Xingtong Ge, Yi Zhang, Bingqi Ma, Guanglu Song, Yu Liu, Hongsheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17461v1.pdf)  
  Keywords: distillation, autoregressive, video generation, streaming  
- **[Motion-Adaptive Temporal Attention for Lightweight Video Generation with Stable Diffusion](https://arxiv.org/abs/2603.17398v1)**  
  Authors: Rui Hong, Shuxue Quan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17398v1.pdf)  
  Keywords: temporal consistency, diffusion model, video generation, efficient, denoising  
- **[MosaicMem: Hybrid Spatial Memory for Controllable Video World Models](https://arxiv.org/abs/2603.17117v1)**  
  Authors: Wei Yu, Runjia Qian, Yumeng Li, Liquan Wang, Songheng Yin, Sri Siddarth Chakaravarthy P, Dennis Anthony, Yang Ye, Yidi Li, Weiwei Wan, Animesh Garg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17117v1.pdf)  
  Keywords: world simulator, autoregressive, world model, dit, controllable, video diffusion, diffusion model  
- **[WorldCam: Interactive Autoregressive 3D Gaming Worlds with Camera Pose as a Unifying Geometric Representation](https://arxiv.org/abs/2603.16871v1)**  
  Authors: Jisu Nam, Yicong Hong, Chun-Hao Paul Huang, Feng Liu, JoungBin Lee, Jiyoung Kim, Siyoon Jin, Yunsung Lee, Jaeyoon Jung, Suhwan Choi, Seungryong Kim, Yang Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16871v1.pdf)  
  Keywords: autoregressive, world model, diffusion transformer, physics, interactive, dit, video diffusion  
- **[Fanar 2.0: Arabic Generative AI Stack](https://arxiv.org/abs/2603.16397v1)**  
  Authors: FANAR TEAM, Ummar Abbas, Mohammad Shahmeer Ahmad, Minhaj Ahmad, Abdulaziz Al-Homaid, Anas Al-Nuaimi, Enes Altinisik, Ehsaneddin Asgari, Sanjay Chawla, Shammur Chowdhury, Fahim Dalvi, Kareem Darwish, Nadir Durrani, Mohamed Elfeky, Ahmed Elmagarmid, Mohamed Eltabakh, Asim Ersoy, Masoomali Fatehkia, Mohammed Qusay Hashim, Majd Hawasly, Mohamed Hefeeda, Mus'ab Husaini, Keivin Isufaj, Soon-Gyo Jung, Houssam Lachemat, Ji Kim Lucas, Abubakr Mohamed, Tasnim Mohiuddin, Basel Mousi, Hamdy Mubarak, Ahmad Musleh, Mourad Ouzzani, Amin Sadeghi, Husrev Taha Sencar, Mohammed Shinoy, Omar Sinan, Yifan Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16397v1.pdf)  
  Keywords: architecture, benchmark, long-form  
- **[VIGOR: VIdeo Geometry-Oriented Reward for Temporal Generative Alignment](https://arxiv.org/abs/2603.16271v1)**  
  Authors: Tengjiao Yin, Jinglei Shi, Heng Guo, Xi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16271v1.pdf)  
  Keywords: physical, streaming, dit, video diffusion, efficient, evaluation, diffusion model  
- **[Grounding World Simulation Models in a Real-World Metropolis](https://arxiv.org/abs/2603.15583v1)**  
  Authors: Junyoung Seo, Hyunwook Choi, Minkyung Kwon, Jinhyeok Choi, Siyoon Jin, Gayoung Lee, Junho Kim, JoungBin Lee, Geonmo Gu, Dongyoon Han, Sangdoo Yun, Seungryong Kim, Jin-Hwa Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15583v1.pdf)  
  Keywords: autoregressive, simulation, world model, video generation, dit, trajectory  

### Personalization & Customization

*Showing the latest 50 out of 89 papers*

- **[Student views in AI Ethics and Social Impact](https://arxiv.org/abs/2603.18827v1)**  
  Authors: Tudor-Dan Mihoc, Manuela-Andreea Petrescu, Emilia-Loredana Pop  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18827v1.pdf)  
  Keywords: concept, education, autonomous driving, survey  
- **[3DreamBooth: High-Fidelity 3D Subject-Driven Video Generation Model](https://arxiv.org/abs/2603.18524v1)**  
  Authors: Hyun-kyu Ko, Jihyeon Park, Younghyun Kim, Dongheok Park, Eunbyung Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18524v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ko-lani.github.io/3DreamBooth)  
  Keywords: subject-driven, 3d-aware, multi-view video, video generation, dit, novel view, customization, identity  
- **[The Unreasonable Effectiveness of Text Embedding Interpolation for Continuous Image Steering](https://arxiv.org/abs/2603.17998v1)**  
  Authors: Yigit Ekin, Yossi Gandelsman  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17998v1.pdf)  
  Keywords: video generation, dit, controllable, concept, evaluation  
- **[AHOY! Animatable Humans under Occlusion from YouTube Videos with Gaussian Splatting and Video Diffusion Priors](https://arxiv.org/abs/2603.17975v1)**  
  Authors: Aymen Mir, Riza Alp Guler, Xiangjun Tang, Peter Wonka, Gerard Pons-Moll  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17975v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://miraymen.github.io/ahoy)  
  Keywords: architecture, avatar, video diffusion, identity, diffusion model  
- **[Identity as Presence: Towards Appearance and Voice Personalized Joint Audio-Video Generation](https://arxiv.org/abs/2603.17889v1)**  
  Authors: Yingjie Chen, Shilun Lin, Cai Xing, Qixin Yan, Wenjing Wang, Dingming Liu, Hao Liu, Chen Li, Jing Lyu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17889v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://chen-yingjie.github.io/projects/Identity-as-Presence)  
  Keywords: personalization, identity, video generation  
- **[Demystifing Video Reasoning](https://arxiv.org/abs/2603.16870v1)**  
  Authors: Ruisi Wang, Zhongang Cai, Fanyi Pu, Junxiang Xu, Wanqi Yin, Maijunxian Wang, Ran Ji, Chenyang Gu, Bo Li, Ziqi Huang, Hokin Deng, Dahua Lin, Ziwei Liu, Lei Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16870v1.pdf)  
  Keywords: diffusion transformer, denoising, video generation, concept, dynamics  
- **[Tri-Prompting: Video Diffusion with Unified Control over Scene, Subject, and Motion](https://arxiv.org/abs/2603.15614v1)**  
  Authors: Zhenghong Zhou, Xiaohang Zhan, Zhiqin Chen, Soo Ye Kim, Nanxuan Zhao, Haitian Zheng, Qing Liu, He Zhang, Zhe Lin, Yuqian Zhou, Jiebo Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15614v1.pdf)  
  Keywords: architecture, 3d-aware, motion control, customization, dit, controllable, video diffusion, identity, diffusion model  
- **[AnyCrowd: Instance-Isolated Identity-Pose Binding for Arbitrary Multi-Character Animation](https://arxiv.org/abs/2603.15415v1)**  
  Authors: Zhenyu Xie, Ji Xia, Michael Kampffmeyer, Panwen Hu, Zehua Ma, Yujian Zheng, Jing Wang, Zheng Chong, Xujie Zhang, Xianhang Cheng, Xiaodan Liang, Hao Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15415v1.pdf)  
  Keywords: diffusion transformer, video generation, dit, controllable, identity  
- **[Seeking Physics in Diffusion Noise](https://arxiv.org/abs/2603.14294v1)**  
  Authors: Chujun Tang, Lei Zhong, Fangqiang Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14294v1.pdf)  
  Keywords: diffusion model, diffusion transformer, physics, physical, dit, video diffusion, identity, trajectory, denoising  
- **[MotionCFG: Boosting Motion Dynamics via Stochastic Concept Perturbation](https://arxiv.org/abs/2603.14073v1)**  
  Authors: Byungjun Kim, Soobin Um, Jong Chul Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14073v1.pdf)  
  Keywords: text-to-video, dynamics, dit, t2v, identity, concept, denoising  

### Physical Understanding

*Showing the latest 50 out of 135 papers*

- **[Generation Models Know Space: Unleashing Implicit 3D Priors for Scene Understanding](https://arxiv.org/abs/2603.19235v1)**  
  Authors: Xianjin Wu, Dingkang Liang, Tianrui Feng, Kui Xia, Yumeng Zhang, Xiaofan Li, Xiao Tan, Xiang Bai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19235v1.pdf) | [![GitHub](https://img.shields.io/github/stars/H-EmbodVis/VEGA-3D?style=social)](https://github.com/H-EmbodVis/VEGA-3D)  
  Keywords: world simulator, benchmark, physical, dynamics, video generation, video diffusion, diffusion model  
- **[PhysVideo: Physically Plausible Video Generation with Cross-View Geometry Guidance](https://arxiv.org/abs/2603.18639v1)**  
  Authors: Cong Wang, Hanxin Zhu, Xiao Tang, Jiayi Luo, Xin Jin, Long Chen, Fei-Yue Wang, Zhibo Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18639v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://anonymous.4open.science/w/Phys4D)  
  Keywords: temporal consistency, physics, physical, video generation, controllable, physics-aware, dynamics, video synthesis  
- **[Versatile Editing of Video Content, Actions, and Dynamics without Training](https://arxiv.org/abs/2603.17989v1)**  
  Authors: Vladimir Kulikov, Roni Paiss, Andrey Voynov, Inbar Mosseri, Tali Dekel, Tomer Michaeli  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17989v1.pdf)  
  Keywords: text-to-video, video editing, video generation, dit, dynamics  
- **[Video Understanding: From Geometry and Semantics to Unified Models](https://arxiv.org/abs/2603.17840v1)**  
  Authors: Zhaochong An, Zirui Li, Mingqiao Ye, Feng Qiao, Jiaang Li, Zongwei Wu, Vishal Thengane, Chengzu Li, Lei Li, Luc Van Gool, Guolei Sun, Serge Belongie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17840v1.pdf)  
  Keywords: dynamics, survey  
- **[EVA: Aligning Video World Models with Executable Robot Actions via Inverse Dynamics Rewards](https://arxiv.org/abs/2603.17808v1)**  
  Authors: Ruixiang Wang, Qingming Liu, Yueci Deng, Guiliang Liu, Zhen Liu, Kui Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17808v1.pdf)  
  Keywords: robotics, benchmark, world model, physical, video generation, dit, efficient, acceleration, dynamics  
- **[Learning Transferable Temporal Primitives for Video Reasoning via Synthetic Videos](https://arxiv.org/abs/2603.17693v1)**  
  Authors: Songtao Jiang, Sibo Song, Chenyi Zhou, Yuan Wang, Ruizhe Chen, Tongkun Guan, Ruilin Luo, Yan Zhang, Zhihang Tang, Yuchong Sun, Hang Zhang, Zhibo Yang, Shuai Bai, Junyang Lin, Zuozhu Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17693v1.pdf)  
  Keywords: benchmark, image to video, video generation, efficient, dynamics  
- **[Few-Step Diffusion Sampling Through Instance-Aware Discretizations](https://arxiv.org/abs/2603.17671v1)**  
  Authors: Liangyu Yuan, Ruoyu Wang, Tong Zhao, Dingwen Fu, Mingkun Lei, Beier Zhu, Chi Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17671v1.pdf)  
  Keywords: flow matching, dynamics, dit  
- **[SHIFT: Motion Alignment in Video Diffusion Models with Adversarial Hybrid Fine-Tuning](https://arxiv.org/abs/2603.17426v1)**  
  Authors: Xi Ye, Wenjia Yang, Yangyang Xu, Xiaoyang Liu, Duo Su, Mengfei Xia, Jun Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17426v1.pdf)  
  Keywords: diffusion model, dit, video diffusion, efficient, dynamics  
- **[GigaWorld-Policy: An Efficient Action-Centered World--Action Model](https://arxiv.org/abs/2603.17240v1)**  
  Authors: Angen Ye, Boyuan Wang, Chaojun Ni, Guan Huang, Guosheng Zhao, Hao Li, Hengtao Li, Jie Li, Jindi Lv, Jingyu Liu, Min Cao, Peng Li, Qiuping Deng, Wenjun Mei, Xiaofeng Wang, Xinze Chen, Xinyu Zhou, Yang Wang, Yifan Chang, Yifan Li, Yukun Zhou, Yun Ye, Zhichao Liu, Zheng Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17240v1.pdf)  
  Keywords: physical, video generation, dit, efficient, dynamics  
- **[WorldCam: Interactive Autoregressive 3D Gaming Worlds with Camera Pose as a Unifying Geometric Representation](https://arxiv.org/abs/2603.16871v1)**  
  Authors: Jisu Nam, Yicong Hong, Chun-Hao Paul Huang, Feng Liu, JoungBin Lee, Jiyoung Kim, Siyoon Jin, Yunsung Lee, Jaeyoon Jung, Suhwan Choi, Seungryong Kim, Yang Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16871v1.pdf)  
  Keywords: autoregressive, world model, diffusion transformer, physics, interactive, dit, video diffusion  

### Surveys & Benchmarks

*Showing the latest 50 out of 192 papers*

- **[Generation Models Know Space: Unleashing Implicit 3D Priors for Scene Understanding](https://arxiv.org/abs/2603.19235v1)**  
  Authors: Xianjin Wu, Dingkang Liang, Tianrui Feng, Kui Xia, Yumeng Zhang, Xiaofan Li, Xiao Tan, Xiang Bai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19235v1.pdf) | [![GitHub](https://img.shields.io/github/stars/H-EmbodVis/VEGA-3D?style=social)](https://github.com/H-EmbodVis/VEGA-3D)  
  Keywords: world simulator, benchmark, physical, dynamics, video generation, video diffusion, diffusion model  
- **[Student views in AI Ethics and Social Impact](https://arxiv.org/abs/2603.18827v1)**  
  Authors: Tudor-Dan Mihoc, Manuela-Andreea Petrescu, Emilia-Loredana Pop  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18827v1.pdf)  
  Keywords: concept, education, autonomous driving, survey  
- **[Improving Joint Audio-Video Generation with Cross-Modal Context Learning](https://arxiv.org/abs/2603.18600v1)**  
  Authors: Bingqi Ma, Linlong Lang, Ming Zhang, Dailan He, Xingtong Ge, Yi Zhang, Guanglu Song, Yu Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18600v1.pdf)  
  Keywords: architecture, video generation, dit, video diffusion, evaluation, diffusion model, multi-modal  
- **[The Unreasonable Effectiveness of Text Embedding Interpolation for Continuous Image Steering](https://arxiv.org/abs/2603.17998v1)**  
  Authors: Yigit Ekin, Yossi Gandelsman  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17998v1.pdf)  
  Keywords: video generation, dit, controllable, concept, evaluation  
- **[Video Understanding: From Geometry and Semantics to Unified Models](https://arxiv.org/abs/2603.17840v1)**  
  Authors: Zhaochong An, Zirui Li, Mingqiao Ye, Feng Qiao, Jiaang Li, Zongwei Wu, Vishal Thengane, Chengzu Li, Lei Li, Luc Van Gool, Guolei Sun, Serge Belongie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17840v1.pdf)  
  Keywords: dynamics, survey  
- **[Insight-V++: Towards Advanced Long-Chain Visual Reasoning with Multimodal Large Language Models](https://arxiv.org/abs/2603.18118v1)**  
  Authors: Yuhao Dong, Zuyan Liu, Shulin Tian, Yongming Rao, Ziwei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18118v1.pdf)  
  Keywords: architecture, benchmark, dit, multi-modal  
- **[EVA: Aligning Video World Models with Executable Robot Actions via Inverse Dynamics Rewards](https://arxiv.org/abs/2603.17808v1)**  
  Authors: Ruixiang Wang, Qingming Liu, Yueci Deng, Guiliang Liu, Zhen Liu, Kui Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17808v1.pdf)  
  Keywords: robotics, benchmark, world model, physical, video generation, dit, efficient, acceleration, dynamics  
- **[Learning Transferable Temporal Primitives for Video Reasoning via Synthetic Videos](https://arxiv.org/abs/2603.17693v1)**  
  Authors: Songtao Jiang, Sibo Song, Chenyi Zhou, Yuan Wang, Ruizhe Chen, Tongkun Guan, Ruilin Luo, Yan Zhang, Zhihang Tang, Yuchong Sun, Hang Zhang, Zhibo Yang, Shuai Bai, Junyang Lin, Zuozhu Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17693v1.pdf)  
  Keywords: benchmark, image to video, video generation, efficient, dynamics  
- **[Stereo World Model: Camera-Guided Stereo Video Generation](https://arxiv.org/abs/2603.17375v1)**  
  Authors: Yang-Tian Sun, Zehuan Huang, Yifan Niu, Lin Ma, Yan-Pei Cao, Yuewen Ma, Xiaojuan Qi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17375v1.pdf)  
  Keywords: benchmark, world model, video generation, dit, interactive, efficient, distillation  
- **[Search2Motion: Training-Free Object-Level Motion Control via Attention-Consensus Search](https://arxiv.org/abs/2603.16711v2)**  
  Authors: Sainan Liu, Tz-Ying Wu, Hector A Valdez, Subarna Tripathi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16711v2.pdf)  
  Keywords: benchmark, evaluation, motion control, video generation, dit, image-to-video, dynamics  

### Text-to-Video Generation

*Showing the latest 50 out of 68 papers*

- **[Versatile Editing of Video Content, Actions, and Dynamics without Training](https://arxiv.org/abs/2603.17989v1)**  
  Authors: Vladimir Kulikov, Roni Paiss, Andrey Voynov, Inbar Mosseri, Tali Dekel, Tomer Michaeli  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17989v1.pdf)  
  Keywords: text-to-video, video editing, video generation, dit, dynamics  
- **[Steering Video Diffusion Transformers with Massive Activations](https://arxiv.org/abs/2603.17825v1)**  
  Authors: Xianhang Cheng, Yujian Zheng, Zhenyu Xie, Tingting Liao, Hao Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17825v1.pdf)  
  Keywords: video diffusion, diffusion transformer, video generation, text-to-video  
- **[GenState-AI: State-Aware Dataset for Text-to-Video Retrieval on AI-Generated Videos](https://arxiv.org/abs/2603.14426v1)**  
  Authors: Minghan Li, Tongna Chen, Tianrui Lv, Yishuai Zhang, Suchao An, Guodong Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14426v1.pdf)  
  Keywords: text-to-video, benchmark, dit, controllable, i2v, evaluation  
- **[Early Failure Detection and Intervention in Video Diffusion Models](https://arxiv.org/abs/2603.14320v1)**  
  Authors: Kwon Byung-Ki, Sohwi Lim, Nam Hyeon-Woo, Moon Ye-Bin, Tae-Hyun Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14320v1.pdf)  
  Keywords: text-to-video, denoising, t2v, video diffusion, efficient, diffusion model  
- **[MotionCFG: Boosting Motion Dynamics via Stochastic Concept Perturbation](https://arxiv.org/abs/2603.14073v1)**  
  Authors: Byungjun Kim, Soobin Um, Jong Chul Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14073v1.pdf)  
  Keywords: text-to-video, dynamics, dit, t2v, identity, concept, denoising  
- **[UniVid: Pyramid Diffusion Model for High Quality Video Generation](https://arxiv.org/abs/2603.13739v1)**  
  Authors: Xinyu Xiao, Binbin Yang, Tingtian Li, Yipeng Yu, Sen Lei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.13739v1.pdf)  
  Keywords: text-to-video, video generation, dit, t2v, i2v, image-to-video, diffusion model  
- **[VQQA: An Agentic Approach for Video Evaluation and Quality Improvement](https://arxiv.org/abs/2603.12310v1)**  
  Authors: Yiwen Song, Tomas Pfister, Yale Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.12310v1.pdf)  
  Keywords: text-to-video, evaluation, video generation, dit, t2v, i2v, efficient, image-to-video  
- **[OSCBench: Benchmarking Object State Change in Text-to-Video Generation](https://arxiv.org/abs/2603.11698v1)**  
  Authors: Xianjing Han, Bin Zhu, Shiqi Hu, Franklin Mingzhe Li, Patrick Carrington, Roger Zimmermann, Jingjing Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.11698v1.pdf)  
  Keywords: text-to-video, benchmark, physical, video generation, t2v, evaluation  
- **[ShotVerse: Advancing Cinematic Camera Control for Text-Driven Multi-Shot Video Creation](https://arxiv.org/abs/2603.11421v1)**  
  Authors: Songlin Yang, Zhe Wang, Xuyi Yang, Songchun Zhang, Xianghao Kong, Taiyi Wu, Xiaotong Zhao, Ran Zhang, Alan Zhao, Anyi Rao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.11421v1.pdf)  
  Keywords: film, text-driven video, video generation, dit, trajectory, evaluation, camera control  
- **[Event-Driven Video Generation](https://arxiv.org/abs/2603.13402v2)**  
  Authors: Chika Maduabuchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.13402v2.pdf)  
  Keywords: text-to-video, denoising, video generation, dit, dynamics  

### Video Editing

- **[Versatile Editing of Video Content, Actions, and Dynamics without Training](https://arxiv.org/abs/2603.17989v1)**  
  Authors: Vladimir Kulikov, Roni Paiss, Andrey Voynov, Inbar Mosseri, Tali Dekel, Tomer Michaeli  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17989v1.pdf)  
  Keywords: text-to-video, video editing, video generation, dit, dynamics  
- **[Script-to-Slide Grounding: Grounding Script Sentences to Slide Objects for Automatic Instructional Video Generation](https://arxiv.org/abs/2603.16931v1)**  
  Authors: Rena Suzuki, Masato Kikuchi, Tadachika Ozono  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16931v1.pdf)  
  Keywords: education, dit, video generation, video editing  
- **[SAW: Toward a Surgical Action World Model via Controllable and Scalable Video Generation](https://arxiv.org/abs/2603.13024v1)**  
  Authors: Sampath Rapuri, Lalithkumar Seenivasan, Dominik Schneider, Roger Soberanis-Mukul, Yufan He, Hao Ding, Jiru Xu, Chenhao Yu, Chenyan Jing, Pengfei Guo, Daguang Xu, Mathias Unberath  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.13024v1.pdf)  
  Keywords: temporal consistency, video-to-video, world model, simulation, video generation, dit, controllable, video diffusion, trajectory, diffusion model  
- **[When to Lock Attention: Training-Free KV Control in Video Diffusion](https://arxiv.org/abs/2603.09657v1)**  
  Authors: Tianyi Zeng, Jincheng Gao, Tianyi Wang, Zijie Meng, Miao Zhang, Jun Yin, Haoyuan Sun, Junfeng Jiao, Christian Claudel, Junbo Tan, Xueqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09657v1.pdf)  
  Keywords: video editing, diffusion model, dit, video diffusion, denoising  
- **[Place-it-R1: Unlocking Environment-aware Reasoning Potential of MLLM for Video Object Insertion](https://arxiv.org/abs/2603.06140v1)**  
  Authors: Bohai Gu, Taiyi Wu, Dazhao Du, Jian Liu, Shuai Yang, Xiaotong Zhao, Alan Zhao, Song Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06140v1.pdf)  
  Keywords: video editing, physical, dit, video diffusion, diffusion model  
- **[GenHOI: Towards Object-Consistent Hand-Object Interaction with Temporally Balanced and Spatially Selective Object Injection](https://arxiv.org/abs/2603.06048v1)**  
  Authors: Xuan Huang, Mochu Xiang, Zhelun Shen, Jinbo Wu, Chenming Wu, Chen Zhao, Kaisiyuan Wang, Hang Zhou, Shanshan Liu, Haocheng Feng, Wei He, Jingdong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06048v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xuanhuang0.github.io/GenHOI)  
  Keywords: video editing, physical, video generation, dit, identity, evaluation, video synthesis  
- **[Training-free Latent Inter-Frame Pruning with Attention Recovery](https://arxiv.org/abs/2603.05811v1)**  
  Authors: Dennis Menn, Yuedong Yang, Bokun Wang, Xiwen Wei, Mustafa Munir, Feng Liang, Radu Marculescu, Chenfeng Xu, Diana Marculescu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05811v1.pdf)  
  Keywords: dit, video generation, video editing  
- **[FREE-Edit: Using Editing-aware Injection in Rectified Flow Models for Zero-shot Image-Driven Video Editing](https://arxiv.org/abs/2603.01164v1)**  
  Authors: Maomao Li, Yunfei Liu, Yu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01164v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://free-edit.github.io/page)  
  Keywords: video editing, rectified flow, layout, dit, i2v, image-driven, image-to-video, denoising  
- **[UniVBench: Towards Unified Evaluation for Video Foundation Models](https://arxiv.org/abs/2602.21835v2)**  
  Authors: Jianhui Wei, Xiaotian Zhang, Yichen Li, Yuan Wang, Yan Zhang, Ziyi Chen, Zhihang Tang, Wei Xu, Zuozhu Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21835v2.pdf)  
  Keywords: benchmark, video editing, video generation, dit, evaluation  
- **[SkyReels-V4: Multi-modal Video-Audio Generation, Inpainting and Editing model](https://arxiv.org/abs/2602.21818v3)**  
  Authors: Guibin Chen, Dixuan Lin, Jiangping Yang, Youqiang Zhang, Zhengcong Fei, Debang Li, Sheng Chen, Chaofeng Ao, Nuo Pang, Yiming Wang, Yikun Dou, Zheng Chen, Mingyuan Fan, Tuanhui Li, Mingshan Chang, Hao Zhang, Xiaopeng Sun, Jingtao Xu, Yuqiang Xie, Jiahua Wang, Zhiheng Xu, Weiming Xiong, Yuzhe Jin, Baoxuan Gu, Binjie Mao, Yunjie Yu, Jujie He, Yuhao Feng, Shiwen Tu, Chaojie Wang, Rui Yan, Wei Shen, Jingchen Wu, Peng Zhao, Xuanyue Zhong, Zhuangzhuang Liu, Kaifei Wang, Fuxiang Zhang, Weikai Xu, Wenyan Liu, Binglu Zhang, Yu Shen, Tianhui Xiong, Bin Peng, Liang Zeng, Xuchen Song, Haoxiang Guo, Peiyu Wang, Max W. Y. Lam, Chien-Hung Liu, Yahui Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21818v3.pdf)  
  Keywords: architecture, video editing, style, image to video, super-resolution, frame interpolation, diffusion transformer, sound, video generation, dit, multi-modal  

### Video Inpainting & Completion

- **[ChopGrad: Pixel-Wise Losses for Latent Video Diffusion via Truncated Backpropagation](https://arxiv.org/abs/2603.17812v1)**  
  Authors: Dmitriy Rivkin, Parker Ewen, Lili Gao, Julian Ost, Stefanie Walz, Rasika Kangutkar, Mario Bijelic, Felix Heide  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17812v1.pdf)  
  Keywords: super-resolution, video inpainting, efficient, video generation, dit, latent video, video diffusion, video enhancement, diffusion model  
- **[ConfCtrl: Enabling Precise Camera Control in Video Diffusion via Confidence-Aware Interpolation](https://arxiv.org/abs/2603.09819v1)**  
  Authors: Liudi Yang, George Eskandar, Fengyi Shen, Mohammad Altillawi, Yang Bai, Chi Zhang, Ziyuan Liu, Abhinav Valada  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09819v1.pdf)  
  Keywords: dit, novel view, video diffusion, video interpolation, diffusion model, camera control  
- **[Pinterest Canvas: Large-Scale Image Generation at Pinterest](https://arxiv.org/abs/2603.06453v1)**  
  Authors: Yu Wang, Eric Tzeng, Raymond Shiau, Jie Yang, Dmitry Kislyuk, Charles Rosenberg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06453v1.pdf)  
  Keywords: outpainting, video generation, dit, image-to-video, diffusion model  
- **[Learning Physics-Grounded 4D Dynamics with Neural Gaussian Force Fields](https://arxiv.org/abs/2602.00148v2)**  
  Authors: Shiqian Li, Ruihong Shen, Junfeng Ni, Chang Pan, Chi Zhang, Yixin Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.00148v2.pdf)  
  Keywords: video prediction, world model, simulation, physics, physical, video generation, interactive, evaluation, dynamics  

### Video Super-Resolution & Enhancement

*Showing the latest 50 out of 59 papers*

- **[Spectrally-Guided Diffusion Noise Schedules](https://arxiv.org/abs/2603.19222v1)**  
  Authors: Carlos Esteves, Ameesh Makadia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19222v1.pdf)  
  Keywords: diffusion model, denoising, video generation, dit  
- **[ChopGrad: Pixel-Wise Losses for Latent Video Diffusion via Truncated Backpropagation](https://arxiv.org/abs/2603.17812v1)**  
  Authors: Dmitriy Rivkin, Parker Ewen, Lili Gao, Julian Ost, Stefanie Walz, Rasika Kangutkar, Mario Bijelic, Felix Heide  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17812v1.pdf)  
  Keywords: super-resolution, video inpainting, efficient, video generation, dit, latent video, video diffusion, video enhancement, diffusion model  
- **[FrescoDiffusion: 4K Image-to-Video with Prior-Regularized Tiled Diffusion](https://arxiv.org/abs/2603.17555v1)**  
  Authors: Hugo Caselles-Dupré, Mathis Koroglu, Guillaume Jeanneret, Arnaud Dapogny, Matthieu Cord  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17555v1.pdf)  
  Keywords: layout, efficient, dit, i2v, trajectory, image-to-video, denoising  
- **[Motion-Adaptive Temporal Attention for Lightweight Video Generation with Stable Diffusion](https://arxiv.org/abs/2603.17398v1)**  
  Authors: Rui Hong, Shuxue Quan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17398v1.pdf)  
  Keywords: temporal consistency, diffusion model, video generation, efficient, denoising  
- **[Demystifing Video Reasoning](https://arxiv.org/abs/2603.16870v1)**  
  Authors: Ruisi Wang, Zhongang Cai, Fanyi Pu, Junxiang Xu, Wanqi Yin, Maijunxian Wang, Ran Ji, Chenyang Gu, Bo Li, Ziqi Huang, Hokin Deng, Dahua Lin, Ziwei Liu, Lei Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16870v1.pdf)  
  Keywords: diffusion transformer, denoising, video generation, concept, dynamics  
- **[S-VAM: Shortcut Video-Action Model by Self-Distilling Geometric and Semantic Foresight](https://arxiv.org/abs/2603.16195v2)**  
  Authors: Haodong Yan, Zhide Zhong, Jiaguan Zhu, Junjie He, Weilin Yuan, Wenxuan Song, Xin Gong, Yingjie Cai, Guanyi Zhao, Xu Yan, Bingbing Liu, Ying-Cong Chen, Haoang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16195v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://haodong-yan.github.io/S-VAM)  
  Keywords: simulation, diffusion model, video generation, distillation, efficient, denoising  
- **[Edit2Interp: Adapting Image Foundation Models from Spatial Editing to Video Frame Interpolation with Few-Shot Learning](https://arxiv.org/abs/2603.15003v1)**  
  Authors: Nasrin Rahimi, Mısra Yavuz, Burak Can Biner, Yunus Bilge Kurt, Ahmet Rasim Emirdağı, Süleyman Aslan, Görkay Aydemir, M. Akın Yılmaz, A. Murat Tekalp  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15003v1.pdf)  
  Keywords: architecture, frame interpolation, dit, efficient, video synthesis  
- **[LatSearch: Latent Reward-Guided Search for Faster Inference-Time Scaling in Video Diffusion](https://arxiv.org/abs/2603.14526v1)**  
  Authors: Zengqun Zhao, Ziquan Liu, Yu Cao, Shaogang Gong, Zhensong Zhang, Jifei Song, Jiankang Deng, Ioannis Patras  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14526v1.pdf)  
  Keywords: benchmark, efficient, video generation, video diffusion, trajectory, evaluation, denoising  
- **[Early Failure Detection and Intervention in Video Diffusion Models](https://arxiv.org/abs/2603.14320v1)**  
  Authors: Kwon Byung-Ki, Sohwi Lim, Nam Hyeon-Woo, Moon Ye-Bin, Tae-Hyun Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14320v1.pdf)  
  Keywords: text-to-video, denoising, t2v, video diffusion, efficient, diffusion model  
- **[Seeking Physics in Diffusion Noise](https://arxiv.org/abs/2603.14294v1)**  
  Authors: Chujun Tang, Lei Zhong, Fangqiang Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14294v1.pdf)  
  Keywords: diffusion model, diffusion transformer, physics, physical, dit, video diffusion, identity, trajectory, denoising  

### World Models & Simulation

*Showing the latest 50 out of 93 papers*

- **[Generation Models Know Space: Unleashing Implicit 3D Priors for Scene Understanding](https://arxiv.org/abs/2603.19235v1)**  
  Authors: Xianjin Wu, Dingkang Liang, Tianrui Feng, Kui Xia, Yumeng Zhang, Xiaofan Li, Xiao Tan, Xiang Bai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19235v1.pdf) | [![GitHub](https://img.shields.io/github/stars/H-EmbodVis/VEGA-3D?style=social)](https://github.com/H-EmbodVis/VEGA-3D)  
  Keywords: world simulator, benchmark, physical, dynamics, video generation, video diffusion, diffusion model  
- **[EVA: Aligning Video World Models with Executable Robot Actions via Inverse Dynamics Rewards](https://arxiv.org/abs/2603.17808v1)**  
  Authors: Ruixiang Wang, Qingming Liu, Yueci Deng, Guiliang Liu, Zhen Liu, Kui Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17808v1.pdf)  
  Keywords: robotics, benchmark, world model, physical, video generation, dit, efficient, acceleration, dynamics  
- **[Stereo World Model: Camera-Guided Stereo Video Generation](https://arxiv.org/abs/2603.17375v1)**  
  Authors: Yang-Tian Sun, Zehuan Huang, Yifan Niu, Lin Ma, Yan-Pei Cao, Yuewen Ma, Xiaojuan Qi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17375v1.pdf)  
  Keywords: benchmark, world model, video generation, dit, interactive, efficient, distillation  
- **[MosaicMem: Hybrid Spatial Memory for Controllable Video World Models](https://arxiv.org/abs/2603.17117v1)**  
  Authors: Wei Yu, Runjia Qian, Yumeng Li, Liquan Wang, Songheng Yin, Sri Siddarth Chakaravarthy P, Dennis Anthony, Yang Ye, Yidi Li, Weiwei Wan, Animesh Garg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17117v1.pdf)  
  Keywords: world simulator, autoregressive, world model, dit, controllable, video diffusion, diffusion model  
- **[WorldCam: Interactive Autoregressive 3D Gaming Worlds with Camera Pose as a Unifying Geometric Representation](https://arxiv.org/abs/2603.16871v1)**  
  Authors: Jisu Nam, Yicong Hong, Chun-Hao Paul Huang, Feng Liu, JoungBin Lee, Jiyoung Kim, Siyoon Jin, Yunsung Lee, Jaeyoon Jung, Suhwan Choi, Seungryong Kim, Yang Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16871v1.pdf)  
  Keywords: autoregressive, world model, diffusion transformer, physics, interactive, dit, video diffusion  
- **[Kinema4D: Kinematic 4D World Modeling for Spatiotemporal Embodied Simulation](https://arxiv.org/abs/2603.16669v1)**  
  Authors: Mutian Xu, Tianbao Zhang, Tianqi Liu, Zhaoxi Chen, Xiaoguang Han, Ziwei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16669v1.pdf)  
  Keywords: action-conditioned, simulation, world model, physical, video generation, dit, interactive, trajectory, dynamics  
- **[S-VAM: Shortcut Video-Action Model by Self-Distilling Geometric and Semantic Foresight](https://arxiv.org/abs/2603.16195v2)**  
  Authors: Haodong Yan, Zhide Zhong, Jiaguan Zhu, Junjie He, Weilin Yuan, Wenxuan Song, Xin Gong, Yingjie Cai, Guanyi Zhao, Xu Yan, Bingbing Liu, Ying-Cong Chen, Haoang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16195v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://haodong-yan.github.io/S-VAM)  
  Keywords: simulation, diffusion model, video generation, distillation, efficient, denoising  
- **[Grounding World Simulation Models in a Real-World Metropolis](https://arxiv.org/abs/2603.15583v1)**  
  Authors: Junyoung Seo, Hyunwook Choi, Minkyung Kwon, Jinhyeok Choi, Siyoon Jin, Gayoung Lee, Junho Kim, JoungBin Lee, Geonmo Gu, Dongyoon Han, Sangdoo Yun, Seungryong Kim, Jin-Hwa Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15583v1.pdf)  
  Keywords: autoregressive, simulation, world model, video generation, dit, trajectory  
- **[Faster Inference of Flow-Based Generative Models via Improved Data-Noise Coupling](https://arxiv.org/abs/2603.15279v1)**  
  Authors: Aram Davtyan, Leello Tadesse Dadi, Volkan Cevher, Paolo Favaro  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15279v1.pdf)  
  Keywords: simulation, flow matching, video generation, dit, distillation, efficient, diffusion model  
- **[Bridging Scene Generation and Planning: Driving with World Model via Unifying Vision and Motion Representation](https://arxiv.org/abs/2603.14948v1)**  
  Authors: Xingtai Gui, Meijie Zhang, Tianyi Yan, Wencheng Han, Jiahao Gong, Feiyang Tan, Cheng-zhong Xu, Jianbing Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14948v1.pdf)  
  Keywords: benchmark, autonomous driving, world model, video generation, dit, trajectory, multi-modal, dynamics  



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
