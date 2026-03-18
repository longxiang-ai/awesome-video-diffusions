# Awesome Video Diffusions [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Video Diffusion Models and Video Generation. Content is automatically updated daily.

> Last Update: 2026-03-18 02:13:10

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
- [Applications](#applications) (48 papers) - Domain-specific applications of video diffusion models
- [Architecture & Efficiency](#architecture-&-efficiency) (361 papers) - Architectural innovations (DiT, UNet), flow matching, and training/inference efficiency
- [Audio & Multi-modal](#audio-&-multi-modal) (30 papers) - Audio-driven and multi-modal conditioned video generation
- [Controllable Generation](#controllable-generation) (123 papers) - Controllable video generation with motion, camera, pose, or layout guidance
- [Human & Character Animation](#human-&-character-animation) (29 papers) - Human-centric video generation including talking heads, dance, and character animation
- [Image-to-Video Generation](#image-to-video-generation) (38 papers) - Methods for animating still images into videos
- [Long Video Generation](#long-video-generation) (121 papers) - Generating temporally consistent long-form videos beyond short clips
- [Personalization & Customization](#personalization-&-customization) (90 papers) - Personalized video generation with custom subjects, identities, or styles
- [Physical Understanding](#physical-understanding) (138 papers) - Physics-aware video generation and dynamics modeling
- [Surveys & Benchmarks](#surveys-&-benchmarks) (195 papers) - Survey papers, benchmarks, and evaluation metrics for video generation
- [Text-to-Video Generation](#text-to-video-generation) (72 papers) - Foundation models and methods for generating videos from text prompts
- [Video Editing](#video-editing) (33 papers) - Diffusion-based video editing, style transfer, and manipulation
- [Video Inpainting & Completion](#video-inpainting-&-completion) (5 papers) - Video inpainting, completion, outpainting, and temporal prediction
- [Video Super-Resolution & Enhancement](#video-super-resolution-&-enhancement) (60 papers) - Video quality improvement, upscaling, restoration, and frame interpolation
- [World Models & Simulation](#world-models-&-simulation) (96 papers) - Video generation as world simulators and interactive environment generation



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3D-aware Video Generation

- **[Tri-Prompting: Video Diffusion with Unified Control over Scene, Subject, and Motion](https://arxiv.org/abs/2603.15614v1)**  
  Authors: Zhenghong Zhou, Xiaohang Zhan, Zhiqin Chen, Soo Ye Kim, Nanxuan Zhao, Haitian Zheng, Qing Liu, He Zhang, Zhe Lin, Yuqian Zhou, Jiebo Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15614v1.pdf)  
  Keywords: motion control, controllable, architecture, 3d-aware, customization, diffusion model, identity, dit, video diffusion  
- **[GeoNVS: Geometry Grounded Video Diffusion for Novel View Synthesis](https://arxiv.org/abs/2603.14965v1)**  
  Authors: Minjun Kang, Inkyu Shin, Taeyeop Lee, Myungchul Kim, In So Kweon, Kuk-Jin Yoon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14965v1.pdf)  
  Keywords: camera control, diffusion model, dit, video diffusion, novel view  
- **[MVHOI: Bridge Multi-view Condition to Complex Human-Object Interaction Video Reenactment via 3D Foundation Model](https://arxiv.org/abs/2603.14686v1)**  
  Authors: Jinguang Tong, Jinbo Wu, Kaisiyuan Wang, Zhelun Shen, Xuan Huang, Mochu Xiang, Xuesong Li, Yingying Li, Haocheng Feng, Chen Zhao, Hang Zhou, Wei He, Chuong Nguyen, Jingdong Wang, Hongdong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14686v1.pdf)  
  Keywords: video generation, controllable, dynamics, dit, novel view  
- **[CamLit: Unified Video Diffusion with Explicit Camera and Lighting Control](https://arxiv.org/abs/2603.14241v1)**  
  Authors: Zhiyi Kuang, Chengan He, Egor Zakharov, Yuxuan Xue, Shunsuke Saito, Olivier Maury, Timur Bagautdinov, Youyi Zheng, Giljoo Nam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14241v1.pdf)  
  Keywords: video generation, trajectory, diffusion model, video diffusion, novel view  
- **[Ego-1K -- A Large-Scale Multiview Video Dataset for Egocentric Vision](https://arxiv.org/abs/2603.13741v1)**  
  Authors: Jae Yong Lee, Daniel Scharstein, Akash Bapat, Hao Hu, Andrew Fu, Haoru Zhao, Paul Sammut, Xiang Li, Stephen Jeapes, Anik Gupta, Lior David, Saketh Madhuvarasu, Jay Girish Joshi, Jason Wither  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.13741v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://huggingface.co/datasets/facebook/ego-1k.) | [![Dataset](https://img.shields.io/badge/-Dataset-orange)](https://huggingface.co/datasets/facebook/ego-1k)  
  Keywords: benchmark, novel view, 3d video, video synthesis  
- **[ConfCtrl: Enabling Precise Camera Control in Video Diffusion via Confidence-Aware Interpolation](https://arxiv.org/abs/2603.09819v1)**  
  Authors: Liudi Yang, George Eskandar, Fengyi Shen, Mohammad Altillawi, Yang Bai, Chi Zhang, Ziyuan Liu, Abhinav Valada  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09819v1.pdf)  
  Keywords: camera control, video interpolation, diffusion model, dit, video diffusion, novel view  
- **[Transformer-Based Inpainting for Real-Time 3D Streaming in Sparse Multi-Camera Setups](https://arxiv.org/abs/2603.05507v1)**  
  Authors: Leif Van Holland, Domenic Zingsheim, Mana Takhsha, Hannah Dröge, Patrick Stotko, Markus Plack, Reinhard Klein  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05507v1.pdf)  
  Keywords: novel view, streaming, dit, architecture  
- **[Orthogonal Spatial-temporal Distributional Transfer for 4D Generation](https://arxiv.org/abs/2603.05081v1)**  
  Authors: Wei Liu, Shengqiong Wu, Bobo Li, Haoyu Zhao, Hao Fei, Mong-Li Lee, Wynne Hsu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05081v1.pdf)  
  Keywords: diffusion model, temporal consistency, 4d generation, video diffusion  
- **[ShareVerse: Multi-Agent Consistent Video Generation for Shared World Modeling](https://arxiv.org/abs/2603.02697v1)**  
  Authors: Jiayi Zhu, Jianing Zhang, Yiying Yang, Wei Cheng, Xiaoyun Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02697v1.pdf)  
  Keywords: video generation, simulation, multi-view video, interactive, dit, world model  
- **[HumanOrbit: 3D Human Reconstruction as 360° Orbit Generation](https://arxiv.org/abs/2602.24148v1)**  
  Authors: Keito Suzuki, Kunyao Chen, Lei Wang, Bang Du, Runfa Blark Li, Peng Liu, Ning Bi, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.24148v1.pdf)  
  Keywords: diffusion model, novel view, video diffusion, identity  

### Applications

- **[Surg$Σ$: A Spectrum of Large-Scale Multimodal Data and Foundation Models for Surgical Intelligence](https://arxiv.org/abs/2603.16822v1)**  
  Authors: Zhitao Zeng, Mengya Xu, Jian Jiang, Pengfei Guo, Yunqiu Xu, Zhu Zhuo, Chang Han Low, Yufan He, Dong Yang, Chenxi Lin, Yiming Gu, Jiaxin Guo, Yutong Ban, Daguang Xu, Qi Dou, Yueming Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16822v1.pdf)  
  Keywords: medical  
- **[Bridging Scene Generation and Planning: Driving with World Model via Unifying Vision and Motion Representation](https://arxiv.org/abs/2603.14948v1)**  
  Authors: Xingtai Gui, Meijie Zhang, Tianyi Yan, Wencheng Han, Jiahao Gong, Feiyang Tan, Cheng-zhong Xu, Jianbing Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14948v1.pdf)  
  Keywords: video generation, trajectory, multi-modal, dynamics, dit, world model, benchmark, autonomous driving  
- **[FAR-Drive: Frame-AutoRegressive Video Generation in Closed-Loop Autonomous Driving](https://arxiv.org/abs/2603.14938v1)**  
  Authors: Yaoru Li, Federico Landi, Marco Godi, Xin Jin, Ruiju Fu, Yufei Ma, Muyang Sun, Heyu Si, Qi Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14938v1.pdf)  
  Keywords: video generation, autoregressive, simulation, interactive, dit, acceleration, diffusion transformer, evaluation, autonomous driving  
- **[PhysAlign: Physics-Coherent Image-to-Video Generation through Feature and 3D Representation Alignment](https://arxiv.org/abs/2603.13770v1)**  
  Authors: Zhexiao Xiong, Yizhi Song, Liu He, Wei Xiong, Yu Yuan, Feng Qiao, Nathan Jacobs  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.13770v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://physalign.github.io/PhysAlign)  
  Keywords: i2v, video generation, controllable, image-to-video, efficient, physics, simulation, robotics, diffusion model, physical, video diffusion  
- **[Risk-Controllable Multi-View Diffusion for Driving Scenario Generation](https://arxiv.org/abs/2603.11534v1)**  
  Authors: Hongyi Lin, Wenxiu Shi, Heye Huang, Dingyi Zhuang, Song Zhang, Yang Liu, Xiaobo Qu, Jinhua Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.11534v1.pdf)  
  Keywords: physical, controllable, world model, autonomous driving  
- **[ShotVerse: Advancing Cinematic Camera Control for Text-Driven Multi-Shot Video Creation](https://arxiv.org/abs/2603.11421v1)**  
  Authors: Songlin Yang, Zhe Wang, Xuyi Yang, Songchun Zhang, Xianghao Kong, Taiyi Wu, Xiaotong Zhao, Ran Zhang, Alan Zhao, Anyi Rao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.11421v1.pdf)  
  Keywords: film, video generation, camera control, text-driven video, trajectory, dit, evaluation  
- **[Motion Forcing: A Decoupled Framework for Robust Video Generation in Motion Dynamics](https://arxiv.org/abs/2603.10408v1)**  
  Authors: Tianshuo Xu, Zhifei Chen, Leyi Wu, Hao Lu, Ying-cong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.10408v1.pdf)  
  Keywords: video generation, physics, robotics, physical, dynamics, benchmark, evaluation, autonomous driving  
- **[EduVQA: Benchmarking AI-Generated Video Quality Assessment for Education](https://arxiv.org/abs/2603.03066v1)**  
  Authors: Baoliang Chen, Xinlong Bu, Lingyu Zhu, Hanwei Zhu, Xiangjie Sui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.03066v1.pdf)  
  Keywords: concept, t2v, text-to-video, education, benchmark, evaluation  
- **[MicroVerse: A Preliminary Exploration Toward a Micro-World Simulation](https://arxiv.org/abs/2603.00585v1)**  
  Authors: Rongsheng Wang, Minghao Wu, Hongru Zhou, Zhihan Yu, Zhenyang Cai, Junying Chen, Benyou Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.00585v1.pdf) | [![GitHub](https://img.shields.io/github/stars/FreedomIntelligence/MicroVerse?style=social)](https://github.com/FreedomIntelligence/MicroVerse)  
  Keywords: video generation, medical, concept, simulation, education, interactive, physical, dynamics, benchmark, evaluation  
- **[HorizonForge: Driving Scene Editing with Any Trajectories and Any Vehicles](https://arxiv.org/abs/2602.21333v2)**  
  Authors: Yifan Wang, Francesco Pittaluga, Zaid Tasneem, Chenyu You, Manmohan Chandraker, Ziyu Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21333v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://horizonforge.github.io)  
  Keywords: temporal consistency, controllable, trajectory, simulation, dit, video diffusion, benchmark, evaluation, autonomous driving  

### Architecture & Efficiency

*Showing the latest 50 out of 361 papers*

- **[WorldCam: Interactive Autoregressive 3D Gaming Worlds with Camera Pose as a Unifying Geometric Representation](https://arxiv.org/abs/2603.16871v1)**  
  Authors: Jisu Nam, Yicong Hong, Chun-Hao Paul Huang, Feng Liu, JoungBin Lee, Jiyoung Kim, Siyoon Jin, Yunsung Lee, Jaeyoon Jung, Suhwan Choi, Seungryong Kim, Yang Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16871v1.pdf)  
  Keywords: autoregressive, physics, interactive, dit, diffusion transformer, world model, video diffusion  
- **[Search2Motion: Training-Free Object-Level Motion Control via Attention-Consensus Search](https://arxiv.org/abs/2603.16711v1)**  
  Authors: Sainan Liu, Tz-Ying Wu, Hector A Valdez, Subarna Tripathi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16711v1.pdf)  
  Keywords: video generation, motion control, image-to-video, dynamics, dit, benchmark, evaluation  
- **[vAccSOL: Efficient and Transparent AI Vision Offloading for Mobile Robots](https://arxiv.org/abs/2603.16685v1)**  
  Authors: Adam Zahir, Michele Gucciardom Falk Selker, Anastasios Nanos, Kostis Papazafeiropoulos, Carlos J. Bernardos, Nicolas Weber, Roberto Gonzalez  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16685v1.pdf)  
  Keywords: efficient  
- **[Kinema4D: Kinematic 4D World Modeling for Spatiotemporal Embodied Simulation](https://arxiv.org/abs/2603.16669v1)**  
  Authors: Mutian Xu, Tianbao Zhang, Tianqi Liu, Zhaoxi Chen, Xiaoguang Han, Ziwei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16669v1.pdf)  
  Keywords: video generation, trajectory, simulation, interactive, physical, dit, dynamics, world model, action-conditioned  
- **[VideoMatGen: PBR Materials through Joint Generative Modeling](https://arxiv.org/abs/2603.16566v1)**  
  Authors: Jon Hasselgren, Zheng Zeng, Milos Hasan, Jacob Munkberg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16566v1.pdf)  
  Keywords: architecture, physical, dit, diffusion transformer, video diffusion  
- **[Fanar 2.0: Arabic Generative AI Stack](https://arxiv.org/abs/2603.16397v1)**  
  Authors: FANAR TEAM, Ummar Abbas, Mohammad Shahmeer Ahmad, Minhaj Ahmad, Abdulaziz Al-Homaid, Anas Al-Nuaimi, Enes Altinisik, Ehsaneddin Asgari, Sanjay Chawla, Shammur Chowdhury, Fahim Dalvi, Kareem Darwish, Nadir Durrani, Mohamed Elfeky, Ahmed Elmagarmid, Mohamed Eltabakh, Asim Ersoy, Masoomali Fatehkia, Mohammed Qusay Hashim, Majd Hawasly, Mohamed Hefeeda, Mus'ab Husaini, Keivin Isufaj, Soon-Gyo Jung, Houssam Lachemat, Ji Kim Lucas, Abubakr Mohamed, Tasnim Mohiuddin, Basel Mousi, Hamdy Mubarak, Ahmad Musleh, Mourad Ouzzani, Amin Sadeghi, Husrev Taha Sencar, Mohammed Shinoy, Omar Sinan, Yifan Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16397v1.pdf)  
  Keywords: benchmark, long-form, architecture  
- **[VIGOR: VIdeo Geometry-Oriented Reward for Temporal Generative Alignment](https://arxiv.org/abs/2603.16271v1)**  
  Authors: Tengjiao Yin, Jinglei Shi, Heng Guo, Xi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16271v1.pdf)  
  Keywords: efficient, streaming, diffusion model, physical, dit, video diffusion, evaluation  
- **[S-VAM: Shortcut Video-Action Model by Self-Distilling Geometric and Semantic Foresight](https://arxiv.org/abs/2603.16195v1)**  
  Authors: Haodong Yan, Zhide Zhong, Jiaguan Zhu, Junjie He, Weilin Yuan, Wenxuan Song, Xin Gong, Yingjie Cai, Guanyi Zhao, Xu Yan, Bingbing Liu, Ying-Cong Chen, Haoang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16195v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://haodong-yan.github.io/S-VAM)  
  Keywords: video generation, efficient, distillation, denoising, simulation, diffusion model  
- **[Diffusion Models for Joint Audio-Video Generation](https://arxiv.org/abs/2603.16093v1)**  
  Authors: Alejandro Paredes La Torre  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16093v1.pdf)  
  Keywords: diffusion model, architecture, video generation, dit  
- **[Tri-Prompting: Video Diffusion with Unified Control over Scene, Subject, and Motion](https://arxiv.org/abs/2603.15614v1)**  
  Authors: Zhenghong Zhou, Xiaohang Zhan, Zhiqin Chen, Soo Ye Kim, Nanxuan Zhao, Haitian Zheng, Qing Liu, He Zhang, Zhe Lin, Yuqian Zhou, Jiebo Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15614v1.pdf)  
  Keywords: motion control, controllable, architecture, 3d-aware, customization, diffusion model, identity, dit, video diffusion  

### Audio & Multi-modal

- **[Bridging Scene Generation and Planning: Driving with World Model via Unifying Vision and Motion Representation](https://arxiv.org/abs/2603.14948v1)**  
  Authors: Xingtai Gui, Meijie Zhang, Tianyi Yan, Wencheng Han, Jiahao Gong, Feiyang Tan, Cheng-zhong Xu, Jianbing Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14948v1.pdf)  
  Keywords: video generation, trajectory, multi-modal, dynamics, dit, world model, benchmark, autonomous driving  
- **[V-JEPA 2.1: Unlocking Dense Features in Video Self-Supervised Learning](https://arxiv.org/abs/2603.14482v2)**  
  Authors: Lorenzo Mur-Labadia, Matthew Muckley, Amir Bar, Mido Assran, Koustuv Sinha, Mike Rabbat, Yann LeCun, Nicolas Ballas, Adrien Bardes  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14482v2.pdf)  
  Keywords: benchmark, world model, multi-modal  
- **[Fuel Gauge: Estimating Chain-of-Thought Length Ahead of Time in Large Multimodal Models](https://arxiv.org/abs/2603.10335v1)**  
  Authors: Yuedong Yang, Xiwen Wei, Mustafa Munir, Radu Marculescu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.10335v1.pdf)  
  Keywords: benchmark, multi-modal, efficient  
- **[ID-LoRA: Identity-Driven Audio-Video Personalization with In-Context LoRA](https://arxiv.org/abs/2603.10256v1)**  
  Authors: Aviad Dahan, Moran Yanuka, Noa Kraicer, Lior Wolf, Raja Giryes  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.10256v1.pdf)  
  Keywords: efficient, denoising, style, sound, identity, physical, dit, personalization, video diffusion  
- **[FetalAgents: A Multi-Agent System for Fetal Ultrasound Image and Video Analysis](https://arxiv.org/abs/2603.09733v1)**  
  Authors: Xiaotian Hu, Junwei Huang, Mingxuan Liu, Kasidit Anmahapong, Yifei Chen, Yitong Luo, Yiming Huang, Xuguang Bai, Zihan Li, Yi Liao, Haibo Qu, Qiyuan Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09733v1.pdf)  
  Keywords: dit, evaluation, sound  
- **[MM-TS: Multi-Modal Temperature and Margin Schedules for Contrastive Learning with Long-Tail Data](https://arxiv.org/abs/2603.08202v1)**  
  Authors: Siarhei Sheludzko, Dhimitrios Duka, Bernt Schiele, Hilde Kuehne, Anna Kukleva  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08202v1.pdf)  
  Keywords: dit, concept, multi-modal  
- **[StreamWise: Serving Multi-Modal Generation in Real-Time at Scale](https://arxiv.org/abs/2603.05800v1)**  
  Authors: Haoran Qiu, Gohar Irfan Chaudhry, Chaojie Zhang, Íñigo Goiri, Esha Choukse, Rodrigo Fonseca, Ricardo Bianchini  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05800v1.pdf)  
  Keywords: multi-modal, streaming, video generation, efficient  
- **[UniTalking: A Unified Audio-Video Framework for Talking Portrait Generation](https://arxiv.org/abs/2603.01418v1)**  
  Authors: Hebeizi Li, Zihao Liang, Benyuan Sun, Zihao Yin, Xiao Sha, Chenliang Wang, Yi Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01418v1.pdf)  
  Keywords: video generation, architecture, efficient, style, multi-modal  
- **[FlowPortrait: Reinforcement Learning for Audio-Driven Portrait Video Generation](https://arxiv.org/abs/2603.00159v1)**  
  Authors: Weiting Tan, Andy T. Liu, Ming Tu, Xinghua Qu, Philipp Koehn, Lu Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.00159v1.pdf)  
  Keywords: video generation, audio-to-video, autoregressive, temporal consistency, evaluation, audio-driven  
- **[SkyReels-V4: Multi-modal Video-Audio Generation, Inpainting and Editing model](https://arxiv.org/abs/2602.21818v2)**  
  Authors: Guibin Chen, Dixuan Lin, Jiangping Yang, Youqiang Zhang, Zhengcong Fei, Debang Li, Sheng Chen, Chaofeng Ao, Nuo Pang, Yiming Wang, Yikun Dou, Zheng Chen, Mingyuan Fan, Tuanhui Li, Mingshan Chang, Hao Zhang, Xiaopeng Sun, Jingtao Xu, Yuqiang Xie, Jiahua Wang, Zhiheng Xu, Weiming Xiong, Yuzhe Jin, Baoxuan Gu, Binjie Mao, Yunjie Yu, Jujie He, Yuhao Feng, Shiwen Tu, Chaojie Wang, Rui Yan, Wei Shen, Jingchen Wu, Peng Zhao, Xuanyue Zhong, Zhuangzhuang Liu, Kaifei Wang, Fuxiang Zhang, Weikai Xu, Wenyan Liu, Binglu Zhang, Yu Shen, Tianhui Xiong, Bin Peng, Liang Zeng, Xuchen Song, Haoxiang Guo, Peiyu Wang, Max W. Y. Lam, Chien-Hung Liu, Yahui Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21818v2.pdf)  
  Keywords: video generation, architecture, super-resolution, style, sound, multi-modal, dit, diffusion transformer, image to video, frame interpolation, video editing  

### Controllable Generation

*Showing the latest 50 out of 123 papers*

- **[Search2Motion: Training-Free Object-Level Motion Control via Attention-Consensus Search](https://arxiv.org/abs/2603.16711v1)**  
  Authors: Sainan Liu, Tz-Ying Wu, Hector A Valdez, Subarna Tripathi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16711v1.pdf)  
  Keywords: video generation, motion control, image-to-video, dynamics, dit, benchmark, evaluation  
- **[Kinema4D: Kinematic 4D World Modeling for Spatiotemporal Embodied Simulation](https://arxiv.org/abs/2603.16669v1)**  
  Authors: Mutian Xu, Tianbao Zhang, Tianqi Liu, Zhaoxi Chen, Xiaoguang Han, Ziwei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16669v1.pdf)  
  Keywords: video generation, trajectory, simulation, interactive, physical, dit, dynamics, world model, action-conditioned  
- **[Tri-Prompting: Video Diffusion with Unified Control over Scene, Subject, and Motion](https://arxiv.org/abs/2603.15614v1)**  
  Authors: Zhenghong Zhou, Xiaohang Zhan, Zhiqin Chen, Soo Ye Kim, Nanxuan Zhao, Haitian Zheng, Qing Liu, He Zhang, Zhe Lin, Yuqian Zhou, Jiebo Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15614v1.pdf)  
  Keywords: motion control, controllable, architecture, 3d-aware, customization, diffusion model, identity, dit, video diffusion  
- **[Grounding World Simulation Models in a Real-World Metropolis](https://arxiv.org/abs/2603.15583v1)**  
  Authors: Junyoung Seo, Hyunwook Choi, Minkyung Kwon, Jinhyeok Choi, Siyoon Jin, Gayoung Lee, Junho Kim, JoungBin Lee, Geonmo Gu, Dongyoon Han, Sangdoo Yun, Seungryong Kim, Jin-Hwa Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15583v1.pdf)  
  Keywords: video generation, autoregressive, trajectory, simulation, dit, world model  
- **[ViFeEdit: A Video-Free Tuner of Your Video Diffusion Transformer](https://arxiv.org/abs/2603.15478v1)**  
  Authors: Ruonan Yu, Zhenxiong Tan, Zigeng Chen, Songhua Liu, Xinchao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15478v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Lexie-YU/ViFeEdit?style=social)](https://github.com/Lexie-YU/ViFeEdit)  
  Keywords: video generation, controllable, diffusion model, dit, diffusion transformer, video diffusion, temporal consistency  
- **[AnyCrowd: Instance-Isolated Identity-Pose Binding for Arbitrary Multi-Character Animation](https://arxiv.org/abs/2603.15415v1)**  
  Authors: Zhenyu Xie, Ji Xia, Michael Kampffmeyer, Panwen Hu, Zehua Ma, Yujian Zheng, Jing Wang, Zheng Chong, Xujie Zhang, Xianhang Cheng, Xiaodan Liang, Hao Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15415v1.pdf)  
  Keywords: video generation, controllable, identity, dit, diffusion transformer  
- **[Next-Frame Decoding for Ultra-Low-Bitrate Image Compression with Video Diffusion Priors](https://arxiv.org/abs/2603.15129v1)**  
  Authors: Yunuo Chen, Chuqin Zhou, Jiangchuan Li, Xiaoyue Ling, Bing He, Jincheng Dai, Li Song, Guo Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15129v1.pdf)  
  Keywords: diffusion model, layout, video diffusion  
- **[Training-free Detection of Generated Videos via Spatial-Temporal Likelihoods](https://arxiv.org/abs/2603.15026v1)**  
  Authors: Omer Ben Hayun, Roy Betser, Meir Yossef Levi, Levi Kassel, Guy Gilboa  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15026v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://omerbenhayun.github.io/stall-video)  
  Keywords: benchmark, dynamics, controllable  
- **[GeoNVS: Geometry Grounded Video Diffusion for Novel View Synthesis](https://arxiv.org/abs/2603.14965v1)**  
  Authors: Minjun Kang, Inkyu Shin, Taeyeop Lee, Myungchul Kim, In So Kweon, Kuk-Jin Yoon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14965v1.pdf)  
  Keywords: camera control, diffusion model, dit, video diffusion, novel view  
- **[Bridging Scene Generation and Planning: Driving with World Model via Unifying Vision and Motion Representation](https://arxiv.org/abs/2603.14948v1)**  
  Authors: Xingtai Gui, Meijie Zhang, Tianyi Yan, Wencheng Han, Jiahao Gong, Feiyang Tan, Cheng-zhong Xu, Jianbing Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14948v1.pdf)  
  Keywords: video generation, trajectory, multi-modal, dynamics, dit, world model, benchmark, autonomous driving  

### Human & Character Animation

- **[SoulX-LiveAct: Towards Hour-Scale Real-Time Human Animation with Neighbor Forcing and ConvKV Memory](https://arxiv.org/abs/2603.11746v1)**  
  Authors: Dingcheng Zhen, Xu Zheng, Ruixin Zhang, Zhiqi Jiang, Yichao Yan, Ming Tao, Shunshun Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.11746v1.pdf)  
  Keywords: video generation, autoregressive, efficient, streaming, video synthesis, diffusion model, dit, human animation  
- **[Controllable Complex Human Motion Video Generation via Text-to-Skeleton Cascades](https://arxiv.org/abs/2603.08028v1)**  
  Authors: Ashkan Taghipour, Morteza Ghahremani, Zinuo Li, Hamid Laga, Farid Boussaid, Mohammed Bennamoun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08028v1.pdf)  
  Keywords: temporal consistency, video generation, motion control, controllable, autoregressive, diffusion model, dit, video diffusion, benchmark, human motion  
- **[ArtHOI: Articulated Human-Object Interaction Synthesis by 4D Reconstruction from Video Priors](https://arxiv.org/abs/2603.04338v1)**  
  Authors: Zihao Huang, Tianqi Liu, Zhaoxi Chen, Shaocong Xu, Saining Zhang, Lixing Xiao, Zhiguo Cao, Wei Li, Hao Zhao, Ziwei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.04338v1.pdf)  
  Keywords: diffusion model, physical, dit, video diffusion, human motion  
- **[Direct Reward Fine-Tuning on Poses for Single Image to 3D Human in the Wild](https://arxiv.org/abs/2603.02619v1)**  
  Authors: Seunguk Do, Minwoo Huh, Joonghyuk Shin, Jaesik Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02619v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://seunguk-do.github.io/drpose)  
  Keywords: diffusion model, dit, benchmark, human motion, evaluation  
- **[LiftAvatar: Kinematic-Space Completion for Expression-Controlled 3D Gaussian Avatar Animation](https://arxiv.org/abs/2603.02129v1)**  
  Authors: Hualiang Wei, Shunran Jia, Jialun Liu, Wenhui Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02129v1.pdf)  
  Keywords: avatar, controllable, efficient, distillation, dit, diffusion transformer, video diffusion  
- **[Non-verbal Real-time Human-AI Interaction in Constrained Robotic Environments](https://arxiv.org/abs/2603.01804v1)**  
  Authors: Dragos Costea, Alina Marcu, Cristina Lazar, Marius Leordeanu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01804v1.pdf)  
  Keywords: body motion, architecture, text-to-video  
- **[GeoDiff4D: Geometry-Aware Diffusion for 4D Head Avatar Reconstruction](https://arxiv.org/abs/2602.24161v2)**  
  Authors: Chao Xu, Xiaochen Zhao, Xiang Deng, Jingxiang Sun, Donglin Di, Zhuo Su, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.24161v2.pdf)  
  Keywords: diffusion model, video generation, avatar, identity  
- **[Spatio-Temporal Garment Reconstruction Using Diffusion Mapping via Pattern Coordinates](https://arxiv.org/abs/2602.24043v1)**  
  Authors: Yingxuan You, Ren Li, Corentin Dumery, Cong Cao, Hao Li, Pascal Fua  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.24043v1.pdf)  
  Keywords: avatar, virtual try-on, diffusion model, dit, temporal consistency  
- **[BigMaQ: A Big Macaque Motion and Animation Dataset Bridging Image and 3D Pose Representations](https://arxiv.org/abs/2602.19874v1)**  
  Authors: Lucas Martini, Alexander Lappe, Anna Bognár, Rufin Vogels, Martin A. Giese  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.19874v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://martinivis.github.io/BigMaQ)  
  Keywords: benchmark, dynamics, avatar  
- **[Ani3DHuman: Photorealistic 3D Human Animation with Self-guided Stochastic Sampling](https://arxiv.org/abs/2602.19089v1)**  
  Authors: Qi Sun, Can Wang, Jiaxiang Shang, Yingchun Liu, Jing Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.19089v1.pdf) | [![GitHub](https://img.shields.io/github/stars/qiisun/ani3dhuman?style=social)](https://github.com/qiisun/ani3dhuman)  
  Keywords: identity, diffusion model, dynamics, video diffusion, human animation  

### Image-to-Video Generation

- **[Search2Motion: Training-Free Object-Level Motion Control via Attention-Consensus Search](https://arxiv.org/abs/2603.16711v1)**  
  Authors: Sainan Liu, Tz-Ying Wu, Hector A Valdez, Subarna Tripathi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16711v1.pdf)  
  Keywords: video generation, motion control, image-to-video, dynamics, dit, benchmark, evaluation  
- **[GenState-AI: State-Aware Dataset for Text-to-Video Retrieval on AI-Generated Videos](https://arxiv.org/abs/2603.14426v1)**  
  Authors: Minghan Li, Tongna Chen, Tianrui Lv, Yishuai Zhang, Suchao An, Guodong Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14426v1.pdf)  
  Keywords: i2v, controllable, text-to-video, dit, benchmark, evaluation  
- **[PhysAlign: Physics-Coherent Image-to-Video Generation through Feature and 3D Representation Alignment](https://arxiv.org/abs/2603.13770v1)**  
  Authors: Zhexiao Xiong, Yizhi Song, Liu He, Wei Xiong, Yu Yuan, Feng Qiao, Nathan Jacobs  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.13770v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://physalign.github.io/PhysAlign)  
  Keywords: i2v, video generation, controllable, image-to-video, efficient, physics, simulation, robotics, diffusion model, physical, video diffusion  
- **[UniVid: Pyramid Diffusion Model for High Quality Video Generation](https://arxiv.org/abs/2603.13739v1)**  
  Authors: Xinyu Xiao, Binbin Yang, Tingtian Li, Yipeng Yu, Sen Lei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.13739v1.pdf)  
  Keywords: i2v, video generation, image-to-video, t2v, text-to-video, diffusion model, dit  
- **[CtrlAttack: A Unified Attack on World-Model Control in Diffusion Models](https://arxiv.org/abs/2603.13435v1)**  
  Authors: Shuhan Xu, Siyuan Liang, Hongling Zheng, Yong Luo, Han Hu, Lefei Zhang, Dacheng Tao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.13435v1.pdf)  
  Keywords: i2v, image-to-video, trajectory, diffusion model, dynamics, temporal consistency  
- **[VQQA: An Agentic Approach for Video Evaluation and Quality Improvement](https://arxiv.org/abs/2603.12310v1)**  
  Authors: Yiwen Song, Tomas Pfister, Yale Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.12310v1.pdf)  
  Keywords: i2v, video generation, image-to-video, t2v, text-to-video, efficient, dit, evaluation  
- **[SPIRAL: A Closed-Loop Framework for Self-Improving Action World Models via Reflective Planning Agents](https://arxiv.org/abs/2603.08403v2)**  
  Authors: Yu Yang, Yue Liao, Jianbiao Mei, Baisen Wang, Xuemeng Yang, Licheng Wen, Jiangning Zhang, Xiangtai Li, Hanlin Chen, Botian Shi, Yong Liu, Shuicheng Yan, Gim Hee Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08403v2.pdf)  
  Keywords: i2v, temporal consistency, video generation, controllable, dit, world model, benchmark, evaluation  
- **[Pinterest Canvas: Large-Scale Image Generation at Pinterest](https://arxiv.org/abs/2603.06453v1)**  
  Authors: Yu Wang, Eric Tzeng, Raymond Shiau, Jie Yang, Dmitry Kislyuk, Charles Rosenberg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06453v1.pdf)  
  Keywords: video generation, image-to-video, outpainting, diffusion model, dit  
- **[Helios: Real Real-Time Long Video Generation Model](https://arxiv.org/abs/2603.04379v1)**  
  Authors: Shenghai Yuan, Yuanyang Yin, Zongjian Li, Xinwei Huang, Xiao Yang, Li Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.04379v1.pdf)  
  Keywords: i2v, video generation, t2v, autoregressive, diffusion model, acceleration, long video  
- **[FastLightGen: Fast and Light Video Generation with Fewer Steps and Parameters](https://arxiv.org/abs/2603.01685v3)**  
  Authors: Shitong Shao, Yufei Gu, Zeke Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01685v3.pdf)  
  Keywords: i2v, distillation, video generation, efficient  

### Long Video Generation

*Showing the latest 50 out of 121 papers*

- **[WorldCam: Interactive Autoregressive 3D Gaming Worlds with Camera Pose as a Unifying Geometric Representation](https://arxiv.org/abs/2603.16871v1)**  
  Authors: Jisu Nam, Yicong Hong, Chun-Hao Paul Huang, Feng Liu, JoungBin Lee, Jiyoung Kim, Siyoon Jin, Yunsung Lee, Jaeyoon Jung, Suhwan Choi, Seungryong Kim, Yang Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16871v1.pdf)  
  Keywords: autoregressive, physics, interactive, dit, diffusion transformer, world model, video diffusion  
- **[Fanar 2.0: Arabic Generative AI Stack](https://arxiv.org/abs/2603.16397v1)**  
  Authors: FANAR TEAM, Ummar Abbas, Mohammad Shahmeer Ahmad, Minhaj Ahmad, Abdulaziz Al-Homaid, Anas Al-Nuaimi, Enes Altinisik, Ehsaneddin Asgari, Sanjay Chawla, Shammur Chowdhury, Fahim Dalvi, Kareem Darwish, Nadir Durrani, Mohamed Elfeky, Ahmed Elmagarmid, Mohamed Eltabakh, Asim Ersoy, Masoomali Fatehkia, Mohammed Qusay Hashim, Majd Hawasly, Mohamed Hefeeda, Mus'ab Husaini, Keivin Isufaj, Soon-Gyo Jung, Houssam Lachemat, Ji Kim Lucas, Abubakr Mohamed, Tasnim Mohiuddin, Basel Mousi, Hamdy Mubarak, Ahmad Musleh, Mourad Ouzzani, Amin Sadeghi, Husrev Taha Sencar, Mohammed Shinoy, Omar Sinan, Yifan Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16397v1.pdf)  
  Keywords: benchmark, long-form, architecture  
- **[VIGOR: VIdeo Geometry-Oriented Reward for Temporal Generative Alignment](https://arxiv.org/abs/2603.16271v1)**  
  Authors: Tengjiao Yin, Jinglei Shi, Heng Guo, Xi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16271v1.pdf)  
  Keywords: efficient, streaming, diffusion model, physical, dit, video diffusion, evaluation  
- **[Grounding World Simulation Models in a Real-World Metropolis](https://arxiv.org/abs/2603.15583v1)**  
  Authors: Junyoung Seo, Hyunwook Choi, Minkyung Kwon, Jinhyeok Choi, Siyoon Jin, Gayoung Lee, Junho Kim, JoungBin Lee, Geonmo Gu, Dongyoon Han, Sangdoo Yun, Seungryong Kim, Jin-Hwa Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15583v1.pdf)  
  Keywords: video generation, autoregressive, trajectory, simulation, dit, world model  
- **[ViFeEdit: A Video-Free Tuner of Your Video Diffusion Transformer](https://arxiv.org/abs/2603.15478v1)**  
  Authors: Ruonan Yu, Zhenxiong Tan, Zigeng Chen, Songhua Liu, Xinchao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15478v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Lexie-YU/ViFeEdit?style=social)](https://github.com/Lexie-YU/ViFeEdit)  
  Keywords: video generation, controllable, diffusion model, dit, diffusion transformer, video diffusion, temporal consistency  
- **[FAR-Drive: Frame-AutoRegressive Video Generation in Closed-Loop Autonomous Driving](https://arxiv.org/abs/2603.14938v1)**  
  Authors: Yaoru Li, Federico Landi, Marco Godi, Xin Jin, Ruiju Fu, Yufei Ma, Muyang Sun, Heyu Si, Qi Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14938v1.pdf)  
  Keywords: video generation, autoregressive, simulation, interactive, dit, acceleration, diffusion transformer, evaluation, autonomous driving  
- **[SAW: Toward a Surgical Action World Model via Controllable and Scalable Video Generation](https://arxiv.org/abs/2603.13024v1)**  
  Authors: Sampath Rapuri, Lalithkumar Seenivasan, Dominik Schneider, Roger Soberanis-Mukul, Yufan He, Hao Ding, Jiru Xu, Chenhao Yu, Chenyan Jing, Pengfei Guo, Daguang Xu, Mathias Unberath  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.13024v1.pdf)  
  Keywords: video generation, controllable, trajectory, simulation, diffusion model, dit, video diffusion, world model, temporal consistency, video-to-video  
- **[CtrlAttack: A Unified Attack on World-Model Control in Diffusion Models](https://arxiv.org/abs/2603.13435v1)**  
  Authors: Shuhan Xu, Siyuan Liang, Hongling Zheng, Yong Luo, Han Hu, Lefei Zhang, Dacheng Tao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.13435v1.pdf)  
  Keywords: i2v, image-to-video, trajectory, diffusion model, dynamics, temporal consistency  
- **[VGGT-World: Transforming VGGT into an Autoregressive Geometry World Model](https://arxiv.org/abs/2603.12655v1)**  
  Authors: Xiangyu Sun, Shijie Wang, Fengyi Zhang, Lin Liu, Caiyan Jia, Ziying Song, Zi Huang, Yadan Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.12655v1.pdf)  
  Keywords: video generation, efficient, autoregressive, trajectory, dit, world model, flow matching  
- **[MemRoPE: Training-Free Infinite Video Generation via Evolving Memory Tokens](https://arxiv.org/abs/2603.12513v1)**  
  Authors: Youngrae Kim, Qixin Hu, C. -C. Jay Kuo, Peter A. Beerel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.12513v1.pdf)  
  Keywords: video generation, autoregressive, streaming, identity, dynamics  

### Personalization & Customization

*Showing the latest 50 out of 90 papers*

- **[Demystifing Video Reasoning](https://arxiv.org/abs/2603.16870v1)**  
  Authors: Ruisi Wang, Zhongang Cai, Fanyi Pu, Junxiang Xu, Wanqi Yin, Maijunxian Wang, Ran Ji, Chenyang Gu, Bo Li, Ziqi Huang, Hokin Deng, Dahua Lin, Ziwei Liu, Lei Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16870v1.pdf)  
  Keywords: video generation, concept, denoising, dynamics, diffusion transformer  
- **[Tri-Prompting: Video Diffusion with Unified Control over Scene, Subject, and Motion](https://arxiv.org/abs/2603.15614v1)**  
  Authors: Zhenghong Zhou, Xiaohang Zhan, Zhiqin Chen, Soo Ye Kim, Nanxuan Zhao, Haitian Zheng, Qing Liu, He Zhang, Zhe Lin, Yuqian Zhou, Jiebo Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15614v1.pdf)  
  Keywords: motion control, controllable, architecture, 3d-aware, customization, diffusion model, identity, dit, video diffusion  
- **[AnyCrowd: Instance-Isolated Identity-Pose Binding for Arbitrary Multi-Character Animation](https://arxiv.org/abs/2603.15415v1)**  
  Authors: Zhenyu Xie, Ji Xia, Michael Kampffmeyer, Panwen Hu, Zehua Ma, Yujian Zheng, Jing Wang, Zheng Chong, Xujie Zhang, Xianhang Cheng, Xiaodan Liang, Hao Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15415v1.pdf)  
  Keywords: video generation, controllable, identity, dit, diffusion transformer  
- **[Seeking Physics in Diffusion Noise](https://arxiv.org/abs/2603.14294v1)**  
  Authors: Chujun Tang, Lei Zhong, Fangqiang Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14294v1.pdf)  
  Keywords: physics, denoising, trajectory, identity, diffusion model, physical, dit, diffusion transformer, video diffusion  
- **[MotionCFG: Boosting Motion Dynamics via Stochastic Concept Perturbation](https://arxiv.org/abs/2603.14073v1)**  
  Authors: Byungjun Kim, Soobin Um, Jong Chul Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14073v1.pdf)  
  Keywords: concept, t2v, text-to-video, denoising, identity, dynamics, dit  
- **[LibraGen: Playing a Balance Game in Subject-Driven Video Generation](https://arxiv.org/abs/2603.13506v2)**  
  Authors: Jiahao Zhu, Shanshan Lao, Lijie Liu, Gen Li, Tianhao Qi, Wei Han, Bingchuan Li, Fangfang Liu, Zhuowei Chen, Tianxiang Ma, Qian HE, Yi Zhou, Xiaohua Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.13506v2.pdf)  
  Keywords: subject-driven, video generation  
- **[MemRoPE: Training-Free Infinite Video Generation via Evolving Memory Tokens](https://arxiv.org/abs/2603.12513v1)**  
  Authors: Youngrae Kim, Qixin Hu, C. -C. Jay Kuo, Peter A. Beerel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.12513v1.pdf)  
  Keywords: video generation, autoregressive, streaming, identity, dynamics  
- **[DreamVideo-Omni: Omni-Motion Controlled Multi-Subject Video Customization with Latent Identity Reinforcement Learning](https://arxiv.org/abs/2603.12257v1)**  
  Authors: Yujie Wei, Xinyu Liu, Shiwei Zhang, Hangjie Yuan, Jinbo Xing, Zhekai Chen, Xiang Wang, Haonan Qiu, Rui Zhao, Yutong Feng, Ruihang Chu, Yingya Zhang, Yike Guo, Xihui Liu, Hongming Shan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.12257v1.pdf)  
  Keywords: motion control, controllable, video synthesis, diffusion model, customization, dit, identity, dynamics, video diffusion, evaluation  
- **[ID-LoRA: Identity-Driven Audio-Video Personalization with In-Context LoRA](https://arxiv.org/abs/2603.10256v1)**  
  Authors: Aviad Dahan, Moran Yanuka, Noa Kraicer, Lior Wolf, Raja Giryes  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.10256v1.pdf)  
  Keywords: efficient, denoising, style, sound, identity, physical, dit, personalization, video diffusion  
- **[Prune Redundancy, Preserve Essence: Vision Token Compression in VLMs via Synergistic Importance-Diversity](https://arxiv.org/abs/2603.09480v2)**  
  Authors: Zhengyao Fang, Pengyuan Lyu, Chengquan Zhang, Guangming Lu, Jun Yu, Wenjie Pei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09480v2.pdf) | [![GitHub](https://img.shields.io/github/stars/ZhengyaoFang/PruneSID?style=social)](https://github.com/ZhengyaoFang/PruneSID)  
  Keywords: dit, concept  

### Physical Understanding

*Showing the latest 50 out of 138 papers*

- **[WorldCam: Interactive Autoregressive 3D Gaming Worlds with Camera Pose as a Unifying Geometric Representation](https://arxiv.org/abs/2603.16871v1)**  
  Authors: Jisu Nam, Yicong Hong, Chun-Hao Paul Huang, Feng Liu, JoungBin Lee, Jiyoung Kim, Siyoon Jin, Yunsung Lee, Jaeyoon Jung, Suhwan Choi, Seungryong Kim, Yang Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16871v1.pdf)  
  Keywords: autoregressive, physics, interactive, dit, diffusion transformer, world model, video diffusion  
- **[Demystifing Video Reasoning](https://arxiv.org/abs/2603.16870v1)**  
  Authors: Ruisi Wang, Zhongang Cai, Fanyi Pu, Junxiang Xu, Wanqi Yin, Maijunxian Wang, Ran Ji, Chenyang Gu, Bo Li, Ziqi Huang, Hokin Deng, Dahua Lin, Ziwei Liu, Lei Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16870v1.pdf)  
  Keywords: video generation, concept, denoising, dynamics, diffusion transformer  
- **[Search2Motion: Training-Free Object-Level Motion Control via Attention-Consensus Search](https://arxiv.org/abs/2603.16711v1)**  
  Authors: Sainan Liu, Tz-Ying Wu, Hector A Valdez, Subarna Tripathi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16711v1.pdf)  
  Keywords: video generation, motion control, image-to-video, dynamics, dit, benchmark, evaluation  
- **[Kinema4D: Kinematic 4D World Modeling for Spatiotemporal Embodied Simulation](https://arxiv.org/abs/2603.16669v1)**  
  Authors: Mutian Xu, Tianbao Zhang, Tianqi Liu, Zhaoxi Chen, Xiaoguang Han, Ziwei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16669v1.pdf)  
  Keywords: video generation, trajectory, simulation, interactive, physical, dit, dynamics, world model, action-conditioned  
- **[VideoMatGen: PBR Materials through Joint Generative Modeling](https://arxiv.org/abs/2603.16566v1)**  
  Authors: Jon Hasselgren, Zheng Zeng, Milos Hasan, Jacob Munkberg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16566v1.pdf)  
  Keywords: architecture, physical, dit, diffusion transformer, video diffusion  
- **[VIGOR: VIdeo Geometry-Oriented Reward for Temporal Generative Alignment](https://arxiv.org/abs/2603.16271v1)**  
  Authors: Tengjiao Yin, Jinglei Shi, Heng Guo, Xi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16271v1.pdf)  
  Keywords: efficient, streaming, diffusion model, physical, dit, video diffusion, evaluation  
- **[Training-free Detection of Generated Videos via Spatial-Temporal Likelihoods](https://arxiv.org/abs/2603.15026v1)**  
  Authors: Omer Ben Hayun, Roy Betser, Meir Yossef Levi, Levi Kassel, Guy Gilboa  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15026v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://omerbenhayun.github.io/stall-video)  
  Keywords: benchmark, dynamics, controllable  
- **[Bridging Scene Generation and Planning: Driving with World Model via Unifying Vision and Motion Representation](https://arxiv.org/abs/2603.14948v1)**  
  Authors: Xingtai Gui, Meijie Zhang, Tianyi Yan, Wencheng Han, Jiahao Gong, Feiyang Tan, Cheng-zhong Xu, Jianbing Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14948v1.pdf)  
  Keywords: video generation, trajectory, multi-modal, dynamics, dit, world model, benchmark, autonomous driving  
- **[MVHOI: Bridge Multi-view Condition to Complex Human-Object Interaction Video Reenactment via 3D Foundation Model](https://arxiv.org/abs/2603.14686v1)**  
  Authors: Jinguang Tong, Jinbo Wu, Kaisiyuan Wang, Zhelun Shen, Xuan Huang, Mochu Xiang, Xuesong Li, Yingying Li, Haocheng Feng, Chen Zhao, Hang Zhou, Wei He, Chuong Nguyen, Jingdong Wang, Hongdong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14686v1.pdf)  
  Keywords: video generation, controllable, dynamics, dit, novel view  
- **[The Pulse of Motion: Measuring Physical Frame Rate from Visual Dynamics](https://arxiv.org/abs/2603.14375v1)**  
  Authors: Xiangbo Gao, Mingyang Wu, Siyuan Yang, Jiongze Yu, Pardis Taghavi, Fangzhou Lin, Zhengzhong Tu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14375v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xiangbogaobarry.github.io/Visual_Chronometer)  
  Keywords: controllable, simulation, physical, dynamics, world model, benchmark, physical simulation, evaluation  

### Surveys & Benchmarks

*Showing the latest 50 out of 195 papers*

- **[Search2Motion: Training-Free Object-Level Motion Control via Attention-Consensus Search](https://arxiv.org/abs/2603.16711v1)**  
  Authors: Sainan Liu, Tz-Ying Wu, Hector A Valdez, Subarna Tripathi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16711v1.pdf)  
  Keywords: video generation, motion control, image-to-video, dynamics, dit, benchmark, evaluation  
- **[Fanar 2.0: Arabic Generative AI Stack](https://arxiv.org/abs/2603.16397v1)**  
  Authors: FANAR TEAM, Ummar Abbas, Mohammad Shahmeer Ahmad, Minhaj Ahmad, Abdulaziz Al-Homaid, Anas Al-Nuaimi, Enes Altinisik, Ehsaneddin Asgari, Sanjay Chawla, Shammur Chowdhury, Fahim Dalvi, Kareem Darwish, Nadir Durrani, Mohamed Elfeky, Ahmed Elmagarmid, Mohamed Eltabakh, Asim Ersoy, Masoomali Fatehkia, Mohammed Qusay Hashim, Majd Hawasly, Mohamed Hefeeda, Mus'ab Husaini, Keivin Isufaj, Soon-Gyo Jung, Houssam Lachemat, Ji Kim Lucas, Abubakr Mohamed, Tasnim Mohiuddin, Basel Mousi, Hamdy Mubarak, Ahmad Musleh, Mourad Ouzzani, Amin Sadeghi, Husrev Taha Sencar, Mohammed Shinoy, Omar Sinan, Yifan Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16397v1.pdf)  
  Keywords: benchmark, long-form, architecture  
- **[VIGOR: VIdeo Geometry-Oriented Reward for Temporal Generative Alignment](https://arxiv.org/abs/2603.16271v1)**  
  Authors: Tengjiao Yin, Jinglei Shi, Heng Guo, Xi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16271v1.pdf)  
  Keywords: efficient, streaming, diffusion model, physical, dit, video diffusion, evaluation  
- **[Training-free Detection of Generated Videos via Spatial-Temporal Likelihoods](https://arxiv.org/abs/2603.15026v1)**  
  Authors: Omer Ben Hayun, Roy Betser, Meir Yossef Levi, Levi Kassel, Guy Gilboa  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15026v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://omerbenhayun.github.io/stall-video)  
  Keywords: benchmark, dynamics, controllable  
- **[Bridging Scene Generation and Planning: Driving with World Model via Unifying Vision and Motion Representation](https://arxiv.org/abs/2603.14948v1)**  
  Authors: Xingtai Gui, Meijie Zhang, Tianyi Yan, Wencheng Han, Jiahao Gong, Feiyang Tan, Cheng-zhong Xu, Jianbing Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14948v1.pdf)  
  Keywords: video generation, trajectory, multi-modal, dynamics, dit, world model, benchmark, autonomous driving  
- **[FAR-Drive: Frame-AutoRegressive Video Generation in Closed-Loop Autonomous Driving](https://arxiv.org/abs/2603.14938v1)**  
  Authors: Yaoru Li, Federico Landi, Marco Godi, Xin Jin, Ruiju Fu, Yufei Ma, Muyang Sun, Heyu Si, Qi Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14938v1.pdf)  
  Keywords: video generation, autoregressive, simulation, interactive, dit, acceleration, diffusion transformer, evaluation, autonomous driving  
- **[LatSearch: Latent Reward-Guided Search for Faster Inference-Time Scaling in Video Diffusion](https://arxiv.org/abs/2603.14526v1)**  
  Authors: Zengqun Zhao, Ziquan Liu, Yu Cao, Shaogang Gong, Zhensong Zhang, Jifei Song, Jiankang Deng, Ioannis Patras  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14526v1.pdf)  
  Keywords: video generation, efficient, trajectory, denoising, video diffusion, benchmark, evaluation  
- **[V-JEPA 2.1: Unlocking Dense Features in Video Self-Supervised Learning](https://arxiv.org/abs/2603.14482v2)**  
  Authors: Lorenzo Mur-Labadia, Matthew Muckley, Amir Bar, Mido Assran, Koustuv Sinha, Mike Rabbat, Yann LeCun, Nicolas Ballas, Adrien Bardes  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14482v2.pdf)  
  Keywords: benchmark, world model, multi-modal  
- **[GenState-AI: State-Aware Dataset for Text-to-Video Retrieval on AI-Generated Videos](https://arxiv.org/abs/2603.14426v1)**  
  Authors: Minghan Li, Tongna Chen, Tianrui Lv, Yishuai Zhang, Suchao An, Guodong Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14426v1.pdf)  
  Keywords: i2v, controllable, text-to-video, dit, benchmark, evaluation  
- **[The Pulse of Motion: Measuring Physical Frame Rate from Visual Dynamics](https://arxiv.org/abs/2603.14375v1)**  
  Authors: Xiangbo Gao, Mingyang Wu, Siyuan Yang, Jiongze Yu, Pardis Taghavi, Fangzhou Lin, Zhengzhong Tu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14375v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xiangbogaobarry.github.io/Visual_Chronometer)  
  Keywords: controllable, simulation, physical, dynamics, world model, benchmark, physical simulation, evaluation  

### Text-to-Video Generation

*Showing the latest 50 out of 72 papers*

- **[GenState-AI: State-Aware Dataset for Text-to-Video Retrieval on AI-Generated Videos](https://arxiv.org/abs/2603.14426v1)**  
  Authors: Minghan Li, Tongna Chen, Tianrui Lv, Yishuai Zhang, Suchao An, Guodong Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14426v1.pdf)  
  Keywords: i2v, controllable, text-to-video, dit, benchmark, evaluation  
- **[Early Failure Detection and Intervention in Video Diffusion Models](https://arxiv.org/abs/2603.14320v1)**  
  Authors: Kwon Byung-Ki, Sohwi Lim, Nam Hyeon-Woo, Moon Ye-Bin, Tae-Hyun Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14320v1.pdf)  
  Keywords: t2v, text-to-video, efficient, denoising, diffusion model, video diffusion  
- **[MotionCFG: Boosting Motion Dynamics via Stochastic Concept Perturbation](https://arxiv.org/abs/2603.14073v1)**  
  Authors: Byungjun Kim, Soobin Um, Jong Chul Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14073v1.pdf)  
  Keywords: concept, t2v, text-to-video, denoising, identity, dynamics, dit  
- **[UniVid: Pyramid Diffusion Model for High Quality Video Generation](https://arxiv.org/abs/2603.13739v1)**  
  Authors: Xinyu Xiao, Binbin Yang, Tingtian Li, Yipeng Yu, Sen Lei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.13739v1.pdf)  
  Keywords: i2v, video generation, image-to-video, t2v, text-to-video, diffusion model, dit  
- **[VQQA: An Agentic Approach for Video Evaluation and Quality Improvement](https://arxiv.org/abs/2603.12310v1)**  
  Authors: Yiwen Song, Tomas Pfister, Yale Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.12310v1.pdf)  
  Keywords: i2v, video generation, image-to-video, t2v, text-to-video, efficient, dit, evaluation  
- **[OSCBench: Benchmarking Object State Change in Text-to-Video Generation](https://arxiv.org/abs/2603.11698v1)**  
  Authors: Xianjing Han, Bin Zhu, Shiqi Hu, Franklin Mingzhe Li, Patrick Carrington, Roger Zimmermann, Jingjing Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.11698v1.pdf)  
  Keywords: video generation, t2v, text-to-video, physical, benchmark, evaluation  
- **[ShotVerse: Advancing Cinematic Camera Control for Text-Driven Multi-Shot Video Creation](https://arxiv.org/abs/2603.11421v1)**  
  Authors: Songlin Yang, Zhe Wang, Xuyi Yang, Songchun Zhang, Xianghao Kong, Taiyi Wu, Xiaotong Zhao, Ran Zhang, Alan Zhao, Anyi Rao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.11421v1.pdf)  
  Keywords: film, video generation, camera control, text-driven video, trajectory, dit, evaluation  
- **[Event-Driven Video Generation](https://arxiv.org/abs/2603.13402v1)**  
  Authors: Chika Maduabuchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.13402v1.pdf)  
  Keywords: video generation, text-to-video, denoising, dynamics, dit  
- **[VIVECaption: A Split Approach to Caption Quality Improvement](https://arxiv.org/abs/2603.07401v1)**  
  Authors: Varun Ananth, Baqiao Liu, Haoran Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.07401v1.pdf)  
  Keywords: t2v, evaluation, text-to-video  
- **[Two Frames Matter: A Temporal Attack for Text-to-Video Model Jailbreaking](https://arxiv.org/abs/2603.07028v1)**  
  Authors: Moyang Chen, Zonghao Ying, Wenzhuo Xu, Quancheng Zou, Deyue Zhang, Dongdong Yang, Xiangzheng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.07028v1.pdf)  
  Keywords: t2v, text-to-video, trajectory, dit, evaluation  

### Video Editing

- **[SAW: Toward a Surgical Action World Model via Controllable and Scalable Video Generation](https://arxiv.org/abs/2603.13024v1)**  
  Authors: Sampath Rapuri, Lalithkumar Seenivasan, Dominik Schneider, Roger Soberanis-Mukul, Yufan He, Hao Ding, Jiru Xu, Chenhao Yu, Chenyan Jing, Pengfei Guo, Daguang Xu, Mathias Unberath  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.13024v1.pdf)  
  Keywords: video generation, controllable, trajectory, simulation, diffusion model, dit, video diffusion, world model, temporal consistency, video-to-video  
- **[When to Lock Attention: Training-Free KV Control in Video Diffusion](https://arxiv.org/abs/2603.09657v1)**  
  Authors: Tianyi Zeng, Jincheng Gao, Tianyi Wang, Zijie Meng, Miao Zhang, Jun Yin, Haoyuan Sun, Junfeng Jiao, Christian Claudel, Junbo Tan, Xueqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09657v1.pdf)  
  Keywords: denoising, diffusion model, dit, video diffusion, video editing  
- **[Place-it-R1: Unlocking Environment-aware Reasoning Potential of MLLM for Video Object Insertion](https://arxiv.org/abs/2603.06140v1)**  
  Authors: Bohai Gu, Taiyi Wu, Dazhao Du, Jian Liu, Shuai Yang, Xiaotong Zhao, Alan Zhao, Song Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06140v1.pdf)  
  Keywords: diffusion model, physical, dit, video diffusion, video editing  
- **[GenHOI: Towards Object-Consistent Hand-Object Interaction with Temporally Balanced and Spatially Selective Object Injection](https://arxiv.org/abs/2603.06048v1)**  
  Authors: Xuan Huang, Mochu Xiang, Zhelun Shen, Jinbo Wu, Chenming Wu, Chen Zhao, Kaisiyuan Wang, Hang Zhou, Shanshan Liu, Haocheng Feng, Wei He, Jingdong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06048v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xuanhuang0.github.io/GenHOI)  
  Keywords: video generation, video synthesis, identity, physical, dit, evaluation, video editing  
- **[Training-free Latent Inter-Frame Pruning with Attention Recovery](https://arxiv.org/abs/2603.05811v1)**  
  Authors: Dennis Menn, Yuedong Yang, Bokun Wang, Xiwen Wei, Mustafa Munir, Feng Liang, Radu Marculescu, Chenfeng Xu, Diana Marculescu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.05811v1.pdf)  
  Keywords: video generation, dit, video editing  
- **[FREE-Edit: Using Editing-aware Injection in Rectified Flow Models for Zero-shot Image-Driven Video Editing](https://arxiv.org/abs/2603.01164v1)**  
  Authors: Maomao Li, Yunfei Liu, Yu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.01164v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://free-edit.github.io/page)  
  Keywords: i2v, rectified flow, image-to-video, denoising, image-driven, dit, layout, video editing  
- **[UniVBench: Towards Unified Evaluation for Video Foundation Models](https://arxiv.org/abs/2602.21835v2)**  
  Authors: Jianhui Wei, Xiaotian Zhang, Yichen Li, Yuan Wang, Yan Zhang, Ziyi Chen, Zhihang Tang, Wei Xu, Zuozhu Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21835v2.pdf)  
  Keywords: video generation, dit, benchmark, evaluation, video editing  
- **[SkyReels-V4: Multi-modal Video-Audio Generation, Inpainting and Editing model](https://arxiv.org/abs/2602.21818v2)**  
  Authors: Guibin Chen, Dixuan Lin, Jiangping Yang, Youqiang Zhang, Zhengcong Fei, Debang Li, Sheng Chen, Chaofeng Ao, Nuo Pang, Yiming Wang, Yikun Dou, Zheng Chen, Mingyuan Fan, Tuanhui Li, Mingshan Chang, Hao Zhang, Xiaopeng Sun, Jingtao Xu, Yuqiang Xie, Jiahua Wang, Zhiheng Xu, Weiming Xiong, Yuzhe Jin, Baoxuan Gu, Binjie Mao, Yunjie Yu, Jujie He, Yuhao Feng, Shiwen Tu, Chaojie Wang, Rui Yan, Wei Shen, Jingchen Wu, Peng Zhao, Xuanyue Zhong, Zhuangzhuang Liu, Kaifei Wang, Fuxiang Zhang, Weikai Xu, Wenyan Liu, Binglu Zhang, Yu Shen, Tianhui Xiong, Bin Peng, Liang Zeng, Xuchen Song, Haoxiang Guo, Peiyu Wang, Max W. Y. Lam, Chien-Hung Liu, Yahui Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21818v2.pdf)  
  Keywords: video generation, architecture, super-resolution, style, sound, multi-modal, dit, diffusion transformer, image to video, frame interpolation, video editing  
- **[GA-Drive: Geometry-Appearance Decoupled Modeling for Free-viewpoint Driving Scene Generation](https://arxiv.org/abs/2602.20673v2)**  
  Authors: Hao Zhang, Lue Fan, Qitai Wang, Wenbo Li, Zehuan Wu, Lewei Lu, Zhaoxiang Zhang, Hongsheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20673v2.pdf)  
  Keywords: trajectory, simulation, diffusion model, dit, video diffusion, video-to-video, autonomous driving, video editing  
- **[PropFly: Learning to Propagate via On-the-Fly Supervision from Pre-trained Video Diffusion Models](https://arxiv.org/abs/2602.20583v1)**  
  Authors: Wonyong Seo, Jaeho Moon, Jaehyup Lee, Soo Ye Kim, Munchurl Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20583v1.pdf)  
  Keywords: diffusion model, dit, video diffusion, flow matching, video editing  

### Video Inpainting & Completion

- **[ConfCtrl: Enabling Precise Camera Control in Video Diffusion via Confidence-Aware Interpolation](https://arxiv.org/abs/2603.09819v1)**  
  Authors: Liudi Yang, George Eskandar, Fengyi Shen, Mohammad Altillawi, Yang Bai, Chi Zhang, Ziyuan Liu, Abhinav Valada  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09819v1.pdf)  
  Keywords: camera control, video interpolation, diffusion model, dit, video diffusion, novel view  
- **[Pinterest Canvas: Large-Scale Image Generation at Pinterest](https://arxiv.org/abs/2603.06453v1)**  
  Authors: Yu Wang, Eric Tzeng, Raymond Shiau, Jie Yang, Dmitry Kislyuk, Charles Rosenberg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06453v1.pdf)  
  Keywords: video generation, image-to-video, outpainting, diffusion model, dit  
- **[Learning Physics-Grounded 4D Dynamics with Neural Gaussian Force Fields](https://arxiv.org/abs/2602.00148v2)**  
  Authors: Shiqian Li, Ruihong Shen, Junfeng Ni, Chang Pan, Chi Zhang, Yixin Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.00148v2.pdf)  
  Keywords: video generation, physics, simulation, video prediction, interactive, physical, dynamics, world model, evaluation  
- **[DriveLaW:Unifying Planning and Video Generation in a Latent Driving World](https://arxiv.org/abs/2512.23421v2)**  
  Authors: Tianze Xia, Yongkang Li, Lijun Zhou, Jingfeng Yao, Kaixin Xiong, Haiyang Sun, Bing Wang, Kun Ma, Guang Chen, Hangjun Ye, Wenyu Liu, Xinggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.23421v2.pdf)  
  Keywords: video generation, architecture, trajectory, video prediction, world model, benchmark, autonomous driving  
- **[Autoregressive Flow Matching for Motion Prediction](https://arxiv.org/abs/2512.22688v1)**  
  Authors: Johnathan Xie, Stefan Stojanov, Cristobal Eyzaguirre, Daniel L. K. Yamins, Jiajun Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.22688v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Johnathan-Xie/arfm-motion-prediction?style=social)](https://github.com/Johnathan-Xie/arfm-motion-prediction)  
  Keywords: video generation, flow matching, autoregressive, video prediction, robotics, dit, benchmark, human motion  

### Video Super-Resolution & Enhancement

*Showing the latest 50 out of 60 papers*

- **[Demystifing Video Reasoning](https://arxiv.org/abs/2603.16870v1)**  
  Authors: Ruisi Wang, Zhongang Cai, Fanyi Pu, Junxiang Xu, Wanqi Yin, Maijunxian Wang, Ran Ji, Chenyang Gu, Bo Li, Ziqi Huang, Hokin Deng, Dahua Lin, Ziwei Liu, Lei Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16870v1.pdf)  
  Keywords: video generation, concept, denoising, dynamics, diffusion transformer  
- **[S-VAM: Shortcut Video-Action Model by Self-Distilling Geometric and Semantic Foresight](https://arxiv.org/abs/2603.16195v1)**  
  Authors: Haodong Yan, Zhide Zhong, Jiaguan Zhu, Junjie He, Weilin Yuan, Wenxuan Song, Xin Gong, Yingjie Cai, Guanyi Zhao, Xu Yan, Bingbing Liu, Ying-Cong Chen, Haoang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16195v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://haodong-yan.github.io/S-VAM)  
  Keywords: video generation, efficient, distillation, denoising, simulation, diffusion model  
- **[Edit2Interp: Adapting Image Foundation Models from Spatial Editing to Video Frame Interpolation with Few-Shot Learning](https://arxiv.org/abs/2603.15003v1)**  
  Authors: Nasrin Rahimi, Mısra Yavuz, Burak Can Biner, Yunus Bilge Kurt, Ahmet Rasim Emirdağı, Süleyman Aslan, Görkay Aydemir, M. Akın Yılmaz, A. Murat Tekalp  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15003v1.pdf)  
  Keywords: architecture, efficient, video synthesis, dit, frame interpolation  
- **[LatSearch: Latent Reward-Guided Search for Faster Inference-Time Scaling in Video Diffusion](https://arxiv.org/abs/2603.14526v1)**  
  Authors: Zengqun Zhao, Ziquan Liu, Yu Cao, Shaogang Gong, Zhensong Zhang, Jifei Song, Jiankang Deng, Ioannis Patras  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14526v1.pdf)  
  Keywords: video generation, efficient, trajectory, denoising, video diffusion, benchmark, evaluation  
- **[Early Failure Detection and Intervention in Video Diffusion Models](https://arxiv.org/abs/2603.14320v1)**  
  Authors: Kwon Byung-Ki, Sohwi Lim, Nam Hyeon-Woo, Moon Ye-Bin, Tae-Hyun Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14320v1.pdf)  
  Keywords: t2v, text-to-video, efficient, denoising, diffusion model, video diffusion  
- **[Seeking Physics in Diffusion Noise](https://arxiv.org/abs/2603.14294v1)**  
  Authors: Chujun Tang, Lei Zhong, Fangqiang Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14294v1.pdf)  
  Keywords: physics, denoising, trajectory, identity, diffusion model, physical, dit, diffusion transformer, video diffusion  
- **[MotionCFG: Boosting Motion Dynamics via Stochastic Concept Perturbation](https://arxiv.org/abs/2603.14073v1)**  
  Authors: Byungjun Kim, Soobin Um, Jong Chul Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14073v1.pdf)  
  Keywords: concept, t2v, text-to-video, denoising, identity, dynamics, dit  
- **[Draft-and-Target Sampling for Video Generation Policy](https://arxiv.org/abs/2603.13438v1)**  
  Authors: Qikang Zhang, Yingjie Lei, Wei Liu, Daochang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.13438v1.pdf)  
  Keywords: video generation, denoising, trajectory, dit, benchmark  
- **[FlashMotion: Few-Step Controllable Video Generation with Trajectory Guidance](https://arxiv.org/abs/2603.12146v1)**  
  Authors: Quanhao Li, Zhen Xing, Rui Wang, Haidong Cao, Qi Dai, Daoguo Dong, Zuxuan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.12146v1.pdf)  
  Keywords: video generation, motion control, controllable, architecture, distillation, trajectory, denoising, benchmark, evaluation  
- **[Event-Driven Video Generation](https://arxiv.org/abs/2603.13402v1)**  
  Authors: Chika Maduabuchi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.13402v1.pdf)  
  Keywords: video generation, text-to-video, denoising, dynamics, dit  

### World Models & Simulation

*Showing the latest 50 out of 96 papers*

- **[WorldCam: Interactive Autoregressive 3D Gaming Worlds with Camera Pose as a Unifying Geometric Representation](https://arxiv.org/abs/2603.16871v1)**  
  Authors: Jisu Nam, Yicong Hong, Chun-Hao Paul Huang, Feng Liu, JoungBin Lee, Jiyoung Kim, Siyoon Jin, Yunsung Lee, Jaeyoon Jung, Suhwan Choi, Seungryong Kim, Yang Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16871v1.pdf)  
  Keywords: autoregressive, physics, interactive, dit, diffusion transformer, world model, video diffusion  
- **[Kinema4D: Kinematic 4D World Modeling for Spatiotemporal Embodied Simulation](https://arxiv.org/abs/2603.16669v1)**  
  Authors: Mutian Xu, Tianbao Zhang, Tianqi Liu, Zhaoxi Chen, Xiaoguang Han, Ziwei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16669v1.pdf)  
  Keywords: video generation, trajectory, simulation, interactive, physical, dit, dynamics, world model, action-conditioned  
- **[S-VAM: Shortcut Video-Action Model by Self-Distilling Geometric and Semantic Foresight](https://arxiv.org/abs/2603.16195v1)**  
  Authors: Haodong Yan, Zhide Zhong, Jiaguan Zhu, Junjie He, Weilin Yuan, Wenxuan Song, Xin Gong, Yingjie Cai, Guanyi Zhao, Xu Yan, Bingbing Liu, Ying-Cong Chen, Haoang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16195v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://haodong-yan.github.io/S-VAM)  
  Keywords: video generation, efficient, distillation, denoising, simulation, diffusion model  
- **[Grounding World Simulation Models in a Real-World Metropolis](https://arxiv.org/abs/2603.15583v1)**  
  Authors: Junyoung Seo, Hyunwook Choi, Minkyung Kwon, Jinhyeok Choi, Siyoon Jin, Gayoung Lee, Junho Kim, JoungBin Lee, Geonmo Gu, Dongyoon Han, Sangdoo Yun, Seungryong Kim, Jin-Hwa Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15583v1.pdf)  
  Keywords: video generation, autoregressive, trajectory, simulation, dit, world model  
- **[Faster Inference of Flow-Based Generative Models via Improved Data-Noise Coupling](https://arxiv.org/abs/2603.15279v1)**  
  Authors: Aram Davtyan, Leello Tadesse Dadi, Volkan Cevher, Paolo Favaro  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15279v1.pdf)  
  Keywords: video generation, efficient, distillation, simulation, diffusion model, dit, flow matching  
- **[Bridging Scene Generation and Planning: Driving with World Model via Unifying Vision and Motion Representation](https://arxiv.org/abs/2603.14948v1)**  
  Authors: Xingtai Gui, Meijie Zhang, Tianyi Yan, Wencheng Han, Jiahao Gong, Feiyang Tan, Cheng-zhong Xu, Jianbing Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14948v1.pdf)  
  Keywords: video generation, trajectory, multi-modal, dynamics, dit, world model, benchmark, autonomous driving  
- **[FAR-Drive: Frame-AutoRegressive Video Generation in Closed-Loop Autonomous Driving](https://arxiv.org/abs/2603.14938v1)**  
  Authors: Yaoru Li, Federico Landi, Marco Godi, Xin Jin, Ruiju Fu, Yufei Ma, Muyang Sun, Heyu Si, Qi Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14938v1.pdf)  
  Keywords: video generation, autoregressive, simulation, interactive, dit, acceleration, diffusion transformer, evaluation, autonomous driving  
- **[V-JEPA 2.1: Unlocking Dense Features in Video Self-Supervised Learning](https://arxiv.org/abs/2603.14482v2)**  
  Authors: Lorenzo Mur-Labadia, Matthew Muckley, Amir Bar, Mido Assran, Koustuv Sinha, Mike Rabbat, Yann LeCun, Nicolas Ballas, Adrien Bardes  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14482v2.pdf)  
  Keywords: benchmark, world model, multi-modal  
- **[The Pulse of Motion: Measuring Physical Frame Rate from Visual Dynamics](https://arxiv.org/abs/2603.14375v1)**  
  Authors: Xiangbo Gao, Mingyang Wu, Siyuan Yang, Jiongze Yu, Pardis Taghavi, Fangzhou Lin, Zhengzhong Tu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14375v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xiangbogaobarry.github.io/Visual_Chronometer)  
  Keywords: controllable, simulation, physical, dynamics, world model, benchmark, physical simulation, evaluation  
- **[PhysAlign: Physics-Coherent Image-to-Video Generation through Feature and 3D Representation Alignment](https://arxiv.org/abs/2603.13770v1)**  
  Authors: Zhexiao Xiong, Yizhi Song, Liu He, Wei Xiong, Yu Yuan, Feng Qiao, Nathan Jacobs  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.13770v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://physalign.github.io/PhysAlign)  
  Keywords: i2v, video generation, controllable, image-to-video, efficient, physics, simulation, robotics, diffusion model, physical, video diffusion  



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
