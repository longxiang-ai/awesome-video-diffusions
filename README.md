# Awesome Video Diffusions [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Video Diffusion Models and Video Generation. Content is automatically updated daily.

> Last Update: 2026-05-17 03:29:30

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
- [Applications](#applications) (58 papers) - Domain-specific applications of video diffusion models
- [Architecture & Efficiency](#architecture-&-efficiency) (356 papers) - Architectural innovations (DiT, UNet), flow matching, and training/inference efficiency
- [Audio & Multi-modal](#audio-&-multi-modal) (36 papers) - Audio-driven and multi-modal conditioned video generation
- [Controllable Generation](#controllable-generation) (137 papers) - Controllable video generation with motion, camera, pose, or layout guidance
- [Human & Character Animation](#human-&-character-animation) (25 papers) - Human-centric video generation including talking heads, dance, and character animation
- [Image-to-Video Generation](#image-to-video-generation) (38 papers) - Methods for animating still images into videos
- [Long Video Generation](#long-video-generation) (113 papers) - Generating temporally consistent long-form videos beyond short clips
- [Personalization & Customization](#personalization-&-customization) (77 papers) - Personalized video generation with custom subjects, identities, or styles
- [Physical Understanding](#physical-understanding) (159 papers) - Physics-aware video generation and dynamics modeling
- [Surveys & Benchmarks](#surveys-&-benchmarks) (222 papers) - Survey papers, benchmarks, and evaluation metrics for video generation
- [Text-to-Video Generation](#text-to-video-generation) (45 papers) - Foundation models and methods for generating videos from text prompts
- [Video Editing](#video-editing) (25 papers) - Diffusion-based video editing, style transfer, and manipulation
- [Video Inpainting & Completion](#video-inpainting-&-completion) (7 papers) - Video inpainting, completion, outpainting, and temporal prediction
- [Video Super-Resolution & Enhancement](#video-super-resolution-&-enhancement) (72 papers) - Video quality improvement, upscaling, restoration, and frame interpolation
- [World Models & Simulation](#world-models-&-simulation) (111 papers) - Video generation as world simulators and interactive environment generation



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3D-aware Video Generation

- **[GTA: Advancing Image-to-3D World Generation via Geometry Then Appearance Video Diffusion](https://arxiv.org/abs/2605.12957v1)**  
  Authors: Hanxin Zhu, Cong Wang, Peiyan Tu, Jiayi Luo, Tianyu He, Xin Jin, Zhibo Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.12957v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hanxinzhu-lab.github.io/GTA)  
  Keywords: dit, autonomous driving, novel view, video diffusion, diffusion model  
- **[GaitProtector: Impersonation-Driven Gait De-Identification via Training-Free Diffusion Latent Optimization](https://arxiv.org/abs/2605.12431v1)**  
  Authors: Huiran Duan, Qian Zhou, Zhongliang Guo, Junhao Dong, Yuqi Li, Guoying Zhao, Yingli Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.12431v1.pdf)  
  Keywords: 3d video, trajectory, identity, video diffusion, dynamics, diffusion model  
- **[VidSplat: Gaussian Splatting Reconstruction with Geometry-Guided Video Diffusion Priors](https://arxiv.org/abs/2605.11424v1)**  
  Authors: Jimin Tang, Wenyuan Zhang, Junsheng Zhou, Zian Huang, Kanle Shi, Shenkun Xu, Yu-Shen Liu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.11424v1.pdf)  
  Keywords: novel view, video diffusion, denoising, benchmark, 3d consistent  
- **[LoViF 2026 The First Challenge on Holistic Quality Assessment for 4D World Model (PhyScore)](https://arxiv.org/abs/2605.05187v1)**  
  Authors: Wei Luo, Yiting Lu, Xin Li, Haoran Li, Fengbin Guan, Chen Gao, Xin Jin, Yong Li, Zhibo Chen, Sijing Wu, Kang Fu, Yunhao Li, Ziang Xiao, Huiyu Duan, Jing Liu, Qiang Hu, Xiongkuo Min, Guangtao Zhai, Manxi Sun, Zixuan Guo, Yun Li, Ziyang Chen, Manabu Tsukada, Zhengyang Li, Zhenglin Du, Yi Wen, Licheng Jiao, Fang Liu, Lingling Li, Yiwen Ren, Zhilong Song, Dubing Chen, Yucheng Zhou, Tianyi Yan, Huan Zheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.05187v1.pdf)  
  Keywords: temporal consistency, evaluation, physical, world model, 4d generation, dit, physics, benchmark, dynamics, creative  
- **[AnyRecon: Arbitrary-View 3D Reconstruction with Video Diffusion Model](https://arxiv.org/abs/2604.19747v1)**  
  Authors: Yutian Chen, Shi Guo, Renbiao Jin, Tianshuo Yang, Xin Cai, Yawen Luo, Mingxin Yang, Mulin Yu, Linning Xu, Tianfan Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19747v1.pdf)  
  Keywords: distillation, dit, novel view, video diffusion, diffusion model  
- **[MultiWorld: Scalable Multi-Agent Multi-View Video World Models](https://arxiv.org/abs/2604.18564v2)**  
  Authors: Haoyu Wu, Jiwen Yu, Yingtian Zou, Xihui Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.18564v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://multi-world.github.io)  
  Keywords: world model, dit, action-conditioned, dynamics, multi-view video, video generation  
- **[ArtifactWorld: Scaling 3D Gaussian Splatting Artifact Restoration via Video Generation Models](https://arxiv.org/abs/2604.12251v1)**  
  Authors: Xinliang Wang, Yifeng Shi, Zhenyu Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.12251v1.pdf)  
  Keywords: novel view, video diffusion, video generation  
- **[Rays as Pixels: Learning A Joint Distribution of Videos and Camera Trajectories](https://arxiv.org/abs/2604.09429v3)**  
  Authors: Wonbong Jang, Shikun Liu, Soubhik Sanyal, Juan Camilo Perez, Kam Woh Ng, Sanskar Agrawal, Juan-Manuel Perez-Rua, Yiannis Douratsos, Tao Xiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.09429v3.pdf)  
  Keywords: trajectory, dit, novel view, video diffusion, video generation, diffusion model  
- **[Novel View Synthesis as Video Completion](https://arxiv.org/abs/2604.08500v1)**  
  Authors: Qi Wu, Khiem Vuong, Minsik Jeon, Srinivasa Narasimhan, Deva Ramanan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08500v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://frame-crafter.github.io)  
  Keywords: video completion, novel view, video diffusion, benchmark, diffusion model  
- **[Multi-View Video Diffusion Policy: A 3D Spatio-Temporal-Aware Video Action Model](https://arxiv.org/abs/2604.03181v1)**  
  Authors: Peiyan Li, Yixiang Chen, Yuan Xu, Jiabing Yang, Xiangnan Wu, Jun Guo, Nan Sun, Long Qian, Xinghang Li, Xin Xiao, Jing Liu, Nianfeng Liu, Tao Kong, Yan Huang, Liang Wang, Tieniu Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.03181v1.pdf)  
  Keywords: dit, efficient, video diffusion, dynamics, multi-view video  

### Applications

*Showing the latest 50 out of 58 papers*

- **[DriveCtrl: Conditioned Sim-to-Real Driving Video Generation](https://arxiv.org/abs/2605.15116v1)**  
  Authors: Haonan Zhao, Yiting Wang, Jingkun Chen, Valentina Donzella, Thomas Bashford-Rogers, Kurt Debattista  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.15116v1.pdf)  
  Keywords: temporal consistency, evaluation, style, dit, autonomous driving, simulation, video synthesis, layout, depth-guided, controllable, video generation, dynamics  
- **[Generating HDR Video from SDR Video](https://arxiv.org/abs/2605.14703v1)**  
  Authors: SaiKiran Tedla, Francesco Banterle, Trevor Canham, Karanpreet Raja, David B. Lindell, Kiriakos N. Kutulakos, Jiacheng Li, Feiran Li, Daisuke Iso  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.14703v1.pdf)  
  Keywords: video synthesis, film, evaluation  
- **[GTA: Advancing Image-to-3D World Generation via Geometry Then Appearance Video Diffusion](https://arxiv.org/abs/2605.12957v1)**  
  Authors: Hanxin Zhu, Cong Wang, Peiyan Tu, Jiayi Luo, Tianyu He, Xin Jin, Zhibo Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.12957v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hanxinzhu-lab.github.io/GTA)  
  Keywords: dit, autonomous driving, novel view, video diffusion, diffusion model  
- **[Images in Sentences: Scaling Interleaved Instructions for Unified Visual Generation](https://arxiv.org/abs/2605.12305v1)**  
  Authors: Yabo Zhang, Kunchang Li, Dewei Zhou, Xinyu Huang, Xun Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.12305v1.pdf)  
  Keywords: dit, evaluation, creative  
- **[TIE: Time Interval Encoding for Video Generation over Events](https://arxiv.org/abs/2605.10543v1)**  
  Authors: Zhilei Shu, Shangwen Zhu, Zihang Liang, Xiaofan Li, Qianyu Peng, Xinyu Cui, Bo Ye, Yiming Li, Fan Cheng, Jian Zhao, Yang Cao, Zheng-Jun Zha, Ruili Feng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.10543v1.pdf) | [![GitHub](https://img.shields.io/github/stars/MatrixTeam-AI/TIE?style=social)](https://github.com/MatrixTeam-AI/TIE)  
  Keywords: trajectory, style, dit, efficient, diffusion transformer, interactive, robotics, video generation  
- **[SocialDirector: Training-Free Social Interaction Control for Multi-Person Video Generation](https://arxiv.org/abs/2605.10079v1)**  
  Authors: Liangyang Ouyang, Ruicong Liu, Caixin Kang, Yifei Huang, Yoichi Sato  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.10079v1.pdf)  
  Keywords: evaluation, gesture, dynamics, robotics, film, video generation  
- **[OphEdit: Training-Free Text-Guided Editing of Ophthalmic Surgical Videos](https://arxiv.org/abs/2605.07695v1)**  
  Authors: Ritul Jangir, Arkya Jyoti Bagchi, Aiman Farooq, Mangalton Okram, Saurabh Seetaram Korgaonkar, Deepak Mishra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.07695v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ophedit/OphEdit?style=social)](https://github.com/ophedit/OphEdit)  
  Keywords: temporal consistency, evaluation, dit, video editing, denoising, video generation, medical  
- **[A$^2$RD: Agentic Autoregressive Diffusion for Long Video Consistency](https://arxiv.org/abs/2605.06924v1)**  
  Authors: Do Xuan Long, Yale Song, Min-Yen Kan, Tomas Pfister, Long T. Le  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.06924v1.pdf)  
  Keywords: long video, evaluation, architecture, video synthesis, autoregressive, benchmark, creative  
- **[Reconstruction or Semantics? What Makes a Latent Space Useful for Robotic World Models](https://arxiv.org/abs/2605.06388v1)**  
  Authors: Nilaksh, Saurav Jha, Artem Zholus, Sarath Chandar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.06388v1.pdf)  
  Keywords: evaluation, world model, dit, video diffusion, action-conditioned, robotics, diffusion model  
- **[RealCam: Real-Time Novel-View Video Generation with Interactive Camera Control](https://arxiv.org/abs/2605.06051v1)**  
  Authors: Youcan Xu, Jiaxin Shi, Zhen Wang, Wensong Song, Feifei Shao, Chen Liang, Jun Xiao, Long Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.06051v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xyc-fly.github.io/RealCam)  
  Keywords: temporal consistency, distillation, style, camera control, video-to-video, autoregressive, efficient, streaming, interactive, film, video generation  

### Architecture & Efficiency

*Showing the latest 50 out of 356 papers*

- **[RefDecoder: Enhancing Visual Generation with Conditional Video Decoding](https://arxiv.org/abs/2605.15196v1)**  
  Authors: Xiang Fan, Yuheng Wang, Bohan Fang, Zhongzheng Ren, Ranjay Krishna  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.15196v1.pdf)  
  Keywords: style, dit, video editing, denoising, benchmark, video generation, diffusion model, i2v  
- **[RAVEN: Real-time Autoregressive Video Extrapolation with Consistency-model GRPO](https://arxiv.org/abs/2605.15190v1)**  
  Authors: Yanzuo Lu, Ronglai Zuo, Jiankang Deng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.15190v1.pdf)  
  Keywords: evaluation, distillation, dit, autoregressive, video diffusion, streaming, denoising, diffusion model  
- **[Quantitative Video World Model Evaluation for Geometric-Consistency](https://arxiv.org/abs/2605.15185v1)**  
  Authors: Jiaxin Wu, Yihao Pi, Yinling Zhang, Yuheng Li, Xueyan Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.15185v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pdi-bench.github.io)  
  Keywords: evaluation, physical, world model, dit, video generation  
- **[Warp-as-History: Generalizable Camera-Controlled Video Generation from One Training Video](https://arxiv.org/abs/2605.15182v1)**  
  Authors: Yifan Wang, Tong He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.15182v1.pdf)  
  Keywords: trajectory, dit, denoising, dynamics, video generation  
- **[Causal Forcing++: Scalable Few-Step Autoregressive Diffusion Distillation for Real-Time Interactive Video Generation](https://arxiv.org/abs/2605.15141v1)**  
  Authors: Min Zhao, Hongzhou Zhu, Kaiwen Zheng, Zihan Zhou, Bokai Yan, Xinyuan Li, Xiao Yang, Chongxuan Li, Jun Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.15141v1.pdf) | [![GitHub](https://img.shields.io/github/stars/thu-ml/Causal-Forcing?style=social)](https://github.com/thu-ml/Causal-Forcing)  
  Keywords: distillation, world model, dit, interactive, autoregressive, efficient, streaming, action-conditioned, controllable, video generation  
- **[DriveCtrl: Conditioned Sim-to-Real Driving Video Generation](https://arxiv.org/abs/2605.15116v1)**  
  Authors: Haonan Zhao, Yiting Wang, Jingkun Chen, Valentina Donzella, Thomas Bashford-Rogers, Kurt Debattista  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.15116v1.pdf)  
  Keywords: temporal consistency, evaluation, style, dit, autonomous driving, simulation, video synthesis, layout, depth-guided, controllable, video generation, dynamics  
- **[EverAnimate: Minute-Scale Human Animation via Latent Flow Restoration](https://arxiv.org/abs/2605.15042v1)**  
  Authors: Wuyang Li, Yang Gao, Mariam Hassan, Lan Feng, Wentao Pan, Po-Chien Luan, Alexandre Alahi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.15042v1.pdf)  
  Keywords: identity, flow matching, human animation, efficient, long-form, human motion, video generation  
- **[Compositional Video Generation via Inference-Time Guidance](https://arxiv.org/abs/2605.14988v1)**  
  Authors: Ariel Shaulov, Eitan Shaar, Amit Edenzon, Gal Chechik, Lior Wolf  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.14988v1.pdf)  
  Keywords: trajectory, architecture, layout, video diffusion, denoising, benchmark, concept, text-to-video, video generation, diffusion model  
- **[SEDiT: Mask-Free Video Subtitle Erasure via One-step Diffusion Transformer](https://arxiv.org/abs/2605.14894v1)**  
  Authors: Zheng Hui, Yunlong Bai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.14894v1.pdf)  
  Keywords: temporal consistency, rectified flow, dit, efficient, video editing, video diffusion, diffusion transformer, streaming, denoising, diffusion model  
- **[MechVerse: Evaluating Physical Motion Consistency in Video Generation Models](https://arxiv.org/abs/2605.14843v1)**  
  Authors: Rahul Jain, Mayank Patel, Asim Unmesh, Karthik Ramani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.14843v1.pdf)  
  Keywords: physical, dit, benchmark, video generation, image-to-video  

### Audio & Multi-modal

- **[OmniNFT: Modality-wise Omni Diffusion Reinforcement for Joint Audio-Video Generation](https://arxiv.org/abs/2605.12480v1)**  
  Authors: Guohui Zhang, XiaoXiao Ma, Jie Huang, Hang Xu, Hu Yu, Siming Fu, Yuming Li, Zeyue Xue, Lin Song, Haoyang Huang, Nan Duan, Feng Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.12480v1.pdf)  
  Keywords: efficient, video generation, dit, multi-modal  
- **[AllocMV: Optimal Resource Allocation for Music Video Generation via Structured Persistent State](https://arxiv.org/abs/2605.10723v1)**  
  Authors: Huimin Wang, Leilei Ouyang, Chang Xia, Yongqi Kang, Yu Fu, Yuqi Ouyang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.10723v1.pdf)  
  Keywords: video synthesis, video generation, dit, music video  
- **[Omni-DeepSearch: A Benchmark for Audio-Driven Omni-Modal Deep Search](https://arxiv.org/abs/2605.08762v1)**  
  Authors: Tao Yu, yiming ding, Shenghua Chai, Minghui Zhang, Zhongtian Luo, Xinming Wang, Xinlong Chen, Zhaolu Kang, Junhao Gong, Yuxuan Zhou, Haopeng Jin, Zhiqing Cui, Jiabing Yang, YiFan Zhang, Hongzhu Yi, Zheqi He, Xi Yang, Yan Huang, Liang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.08762v1.pdf)  
  Keywords: benchmark, audio-driven  
- **[Unison: Harmonizing Motion, Speech, and Sound for Human-Centric Audio-Video Generation](https://arxiv.org/abs/2605.08729v1)**  
  Authors: Shihao Cheng, Jiaxu Zhang, Quanyue Song, Shansong Liu, Zhizhi Guo, Xiaolei Zhang, Chi Zhang, Xuelong Li, Zhigang Tu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.08729v1.pdf)  
  Keywords: sound, dit, video generation, denoising  
- **[Do Joint Audio-Video Generation Models Understand Physics?](https://arxiv.org/abs/2605.07061v1)**  
  Authors: Zijun Cui, Xiulong Liu, Hao Fang, Mingwei Xu, Jiageng Liu, Zexin Xu, Weiguo Pian, Shijian Deng, Feiyu Du, Chenming Ge, Yapeng Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.07061v1.pdf)  
  Keywords: physical, style, physics, sound, benchmark, dynamics, video generation  
- **[Audio-Visual Intelligence in Large Foundation Models](https://arxiv.org/abs/2605.04045v1)**  
  Authors: You Qin, Kai Liu, Shengqiong Wu, Kai Wang, Shijian Deng, Yapeng Tian, Junbin Xiao, Yazhou Xing, Yinghao Ma, Bobo Li, Roger Zimmermann, Lei Cui, Furu Wei, Jiebo Luo, Hao Fei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.04045v1.pdf)  
  Keywords: evaluation, dit, architecture, video synthesis, sound, autoregressive, benchmark, controllable, survey, audio-driven  
- **[Divide and Conquer: Decoupled Representation Alignment for Multimodal World Models](https://arxiv.org/abs/2605.01896v1)**  
  Authors: Junyuan Xiao, Dingkang Liang, Xin Zhou, Yixuan Ye, Tongtong Su, Guangmo Yi, Bin Xia, Qiang Lyu, Shurui Shi, Jun Huang, Jianlou Si, Wenming Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.01896v1.pdf)  
  Keywords: world model, multi-modal, video generation, diffusion model  
- **[Lucid-XR: An Extended-Reality Data Engine for Robotic Manipulation](https://arxiv.org/abs/2605.00244v1)**  
  Authors: Yajvan Ravan, Adam Rashid, Alan Yu, Kai McClennen, Gio Huh, Kevin Yang, Zhutian Yang, Qinxi Yu, Xiaolong Wang, Phillip Isola, Ge Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.00244v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lucidxr.github.io)  
  Keywords: evaluation, physics, simulation, multi-modal, video generation  
- **[CineAGI: Character-Consistent Movie Creation through LLM-Orchestrated Multi-Modal Generation and Cross-Scene Integration](https://arxiv.org/abs/2604.23579v1)**  
  Authors: Tianyidan Xie, Zhentao Huang, Mingjie Wang, Xin Huang, Jun Zhou, Minglun Gong, Zili Yi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.23579v1.pdf)  
  Keywords: multi-modal, video generation, identity  
- **[EAD-Net: Emotion-Aware Talking Head Generation with Spatial Refinement and Temporal Coherence](https://arxiv.org/abs/2604.23325v1)**  
  Authors: Yahui Li, Yinfeng Yu, Liejun Wang, Shengjie Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.23325v1.pdf)  
  Keywords: long video, temporal consistency, talking head, dit, multi-modal, video generation  

### Controllable Generation

*Showing the latest 50 out of 137 papers*

- **[Warp-as-History: Generalizable Camera-Controlled Video Generation from One Training Video](https://arxiv.org/abs/2605.15182v1)**  
  Authors: Yifan Wang, Tong He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.15182v1.pdf)  
  Keywords: trajectory, dit, denoising, dynamics, video generation  
- **[Causal Forcing++: Scalable Few-Step Autoregressive Diffusion Distillation for Real-Time Interactive Video Generation](https://arxiv.org/abs/2605.15141v1)**  
  Authors: Min Zhao, Hongzhou Zhu, Kaiwen Zheng, Zihan Zhou, Bokai Yan, Xinyuan Li, Xiao Yang, Chongxuan Li, Jun Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.15141v1.pdf) | [![GitHub](https://img.shields.io/github/stars/thu-ml/Causal-Forcing?style=social)](https://github.com/thu-ml/Causal-Forcing)  
  Keywords: distillation, world model, dit, interactive, autoregressive, efficient, streaming, action-conditioned, controllable, video generation  
- **[DriveCtrl: Conditioned Sim-to-Real Driving Video Generation](https://arxiv.org/abs/2605.15116v1)**  
  Authors: Haonan Zhao, Yiting Wang, Jingkun Chen, Valentina Donzella, Thomas Bashford-Rogers, Kurt Debattista  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.15116v1.pdf)  
  Keywords: temporal consistency, evaluation, style, dit, autonomous driving, simulation, video synthesis, layout, depth-guided, controllable, video generation, dynamics  
- **[Compositional Video Generation via Inference-Time Guidance](https://arxiv.org/abs/2605.14988v1)**  
  Authors: Ariel Shaulov, Eitan Shaar, Amit Edenzon, Gal Chechik, Lior Wolf  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.14988v1.pdf)  
  Keywords: trajectory, architecture, layout, video diffusion, denoising, benchmark, concept, text-to-video, video generation, diffusion model  
- **[Probing into Camera Control of Video Models](https://arxiv.org/abs/2605.14815v1)**  
  Authors: Chen Hou, Christian Rupprecht  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.14815v1.pdf)  
  Keywords: dit, camera control, video diffusion, denoising, benchmark, dynamics, video generation, diffusion model  
- **[Delta Forcing: Trust Region Steering for Interactive Autoregressive Video Generation](https://arxiv.org/abs/2605.14382v1)**  
  Authors: Yuheng Wu, Xiangbo Gao, Tianhao Chen, Xinghao Chen, Qing Yin, Zhengzhong Tu, Dongman Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.14382v1.pdf)  
  Keywords: trajectory, world model, dit, autoregressive, streaming, interactive, video generation  
- **[KVPO: ODE-Native GRPO for Autoregressive Video Alignment via KV Semantic Exploration](https://arxiv.org/abs/2605.14278v1)**  
  Authors: Ruicheng Zhang, Kaixi Cong, Jun Zhou, Zhizhou Zhong, Zunnan Xu, Shuiyang Mao, Wei Liu, Xiu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.14278v1.pdf)  
  Keywords: trajectory, autoregressive, streaming, dynamics  
- **[AnyFlow: Any-Step Video Diffusion Model with On-Policy Flow Map Distillation](https://arxiv.org/abs/2605.13724v1)**  
  Authors: Yuchao Gu, Guian Fang, Yuxin Jiang, Weijia Mao, Song Han, Han Cai, Mike Zheng Shou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.13724v1.pdf)  
  Keywords: distillation, trajectory, simulation, architecture, efficient, video diffusion, video generation, diffusion model  
- **[CRePE: Curved Ray Expectation Positional Encoding for Unified-Camera-Controlled Video Generation](https://arxiv.org/abs/2605.12938v1)**  
  Authors: Seonghyun Jin, Youngmin Kim, Sunwoo Park, Jong Chul Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.12938v1.pdf)  
  Keywords: style, video generation, dit, camera control  
- **[GaitProtector: Impersonation-Driven Gait De-Identification via Training-Free Diffusion Latent Optimization](https://arxiv.org/abs/2605.12431v1)**  
  Authors: Huiran Duan, Qian Zhou, Zhongliang Guo, Junhao Dong, Yuqi Li, Guoying Zhao, Yingli Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.12431v1.pdf)  
  Keywords: 3d video, trajectory, identity, video diffusion, dynamics, diffusion model  

### Human & Character Animation

- **[EverAnimate: Minute-Scale Human Animation via Latent Flow Restoration](https://arxiv.org/abs/2605.15042v1)**  
  Authors: Wuyang Li, Yang Gao, Mariam Hassan, Lan Feng, Wentao Pan, Po-Chien Luan, Alexandre Alahi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.15042v1.pdf)  
  Keywords: identity, flow matching, human animation, efficient, long-form, human motion, video generation  
- **[PhyMotion: Structured 3D Motion Reward for Physics-Grounded Human Video Generation](https://arxiv.org/abs/2605.14269v1)**  
  Authors: Yidong Huang, Zun Wang, Han Lin, Dong-Ki Kim, Shayegan Omidshafiei, Jaehong Yoon, Jaemin Cho, Yue Zhang, Mohit Bansal  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.14269v1.pdf)  
  Keywords: evaluation, physical, physics, autoregressive, dynamics, human motion, video generation  
- **[SocialDirector: Training-Free Social Interaction Control for Multi-Person Video Generation](https://arxiv.org/abs/2605.10079v1)**  
  Authors: Liangyang Ouyang, Ruicong Liu, Caixin Kang, Yifei Huang, Yoichi Sato  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.10079v1.pdf)  
  Keywords: evaluation, gesture, dynamics, robotics, film, video generation  
- **[MoCoTalk: Multi-Conditional Diffusion with Adaptive Router for Controllable Talking Head Generation](https://arxiv.org/abs/2605.08050v1)**  
  Authors: Xinyan Ye, Jiankang Deng, Abbas Edalat  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.08050v1.pdf)  
  Keywords: talking head, dit, identity, video diffusion, controllable, dynamics  
- **[Omni-Fake: Benchmarking Unified Multimodal Social Media Deepfake Detection](https://arxiv.org/abs/2605.01638v1)**  
  Authors: Tianxiao Li, Zhenglin Huang, Haiquan Wen, Yiwei He, Xinze Li, Bingyu Zhu, Wuhui Duan, Congang Chen, Zeyu Fu, Yi Dong, Baoyuan Wu, Jason Li, Guangliang Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.01638v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://tianxiao1201.github.io/omni-fake-project-page)  
  Keywords: talking head, dit, benchmark  
- **[Generate Your Talking Avatar from Video Reference](https://arxiv.org/abs/2604.27918v1)**  
  Authors: Zujin Guo, Zhenhui Ye, Yi Ren, Yuanming Li, Ce Chen, Zhibin Hong, Chen Change Loy  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.27918v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://www.heygen.com/research)  
  Keywords: dit, identity, benchmark, avatar, image-to-video  
- **[HuM-Eval: A Coarse-to-Fine Framework for Human-Centric Video Evaluation](https://arxiv.org/abs/2604.25361v1)**  
  Authors: Bingzi Zhang, Kaisi Guan, Ruihua Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.25361v1.pdf)  
  Keywords: evaluation, benchmark, text-to-video, human motion, video generation  
- **[Talker-T2AV: Joint Talking Audio-Video Generation with Autoregressive Diffusion Modeling](https://arxiv.org/abs/2604.23586v1)**  
  Authors: Zhen Ye, Xu Tan, Aoxiong Yin, Hongzhan Lin, Guangyan Zhang, Peiwen Sun, Yiming Li, Chi-Min Chan, Wei Ye, Shikun Zhang, Wei Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.23586v1.pdf)  
  Keywords: talking head, autoregressive, diffusion transformer, benchmark, denoising, video generation, diffusion model  
- **[EAD-Net: Emotion-Aware Talking Head Generation with Spatial Refinement and Temporal Coherence](https://arxiv.org/abs/2604.23325v1)**  
  Authors: Yahui Li, Yinfeng Yu, Liejun Wang, Shengjie Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.23325v1.pdf)  
  Keywords: long video, temporal consistency, talking head, dit, multi-modal, video generation  
- **[Agentic AI for Personalized Physiotherapy: A Multi-Agent Framework for Generative Video Training and Real-Time Pose Correction](https://arxiv.org/abs/2604.21154v1)**  
  Authors: Abhishek Dharmaratnakar, Srivaths Ranganathan, Anushree Sinha, Debanshu Das  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21154v1.pdf)  
  Keywords: evaluation, architecture, video synthesis, avatar, video generation, medical  

### Image-to-Video Generation

- **[RefDecoder: Enhancing Visual Generation with Conditional Video Decoding](https://arxiv.org/abs/2605.15196v1)**  
  Authors: Xiang Fan, Yuheng Wang, Bohan Fang, Zhongzheng Ren, Ranjay Krishna  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.15196v1.pdf)  
  Keywords: style, dit, video editing, denoising, benchmark, video generation, diffusion model, i2v  
- **[MechVerse: Evaluating Physical Motion Consistency in Video Generation Models](https://arxiv.org/abs/2605.14843v1)**  
  Authors: Rahul Jain, Mayank Patel, Asim Unmesh, Karthik Ramani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.14843v1.pdf)  
  Keywords: physical, dit, benchmark, video generation, image-to-video  
- **[Improving Human Image Animation via Semantic Representation Alignment](https://arxiv.org/abs/2605.10523v1)**  
  Authors: Chang Liu, Mengting Chen, Yixuan Huang, Haoning Wu, Chen Ju, Shuai Xiao, Jinsong Lan, Yanfeng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.10523v1.pdf)  
  Keywords: long video, dit, identity, image animation, video generation, diffusion model, image-to-video  
- **[Progressive Photorealistic Simplification](https://arxiv.org/abs/2605.10409v1)**  
  Authors: Adi Rosenthal, Dana Berman, Yedid Hoshen, Ariel Shamir  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.10409v1.pdf)  
  Keywords: interactive, video generation, dit, image-to-video  
- **[Not All Tokens Need 40 Steps: Heterogeneous Step Allocation in Diffusion Transformers for Efficient Video Generation](https://arxiv.org/abs/2605.06892v1)**  
  Authors: Ernie Chu, Vishal M. Patel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.06892v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ernestchu.github.io/hsa)  
  Keywords: evaluation, t2v, dit, flow matching, efficient, diffusion transformer, denoising, dynamics, text-to-video, acceleration, video generation, i2v, image-to-video  
- **[ActCam: Zero-Shot Joint Camera and 3D Motion Control for Video Generation](https://arxiv.org/abs/2605.06667v1)**  
  Authors: Omar El Khalifi, Thomas Rossi, Oscar Fossey, Thibault Fouque, Ulysse Mizrahi, Philip Torr, Ivan Laptev, Fabio Pizzati, Baptiste Bellot-Gurlet  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.06667v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://elkhomar.github.io/actcam)  
  Keywords: motion control, evaluation, trajectory, dit, video diffusion, denoising, benchmark, video generation, diffusion model, image-to-video  
- **[SwiftI2V: Efficient High-Resolution Image-to-Video Generation via Conditional Segment-wise Generation](https://arxiv.org/abs/2605.06356v2)**  
  Authors: YaoYang Liu, Yuechen Zhang, Wenbo Li, Yufei Zhao, Rui Liu, Long Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.06356v2.pdf)  
  Keywords: dit, super-resolution, efficient, dynamics, video generation, i2v, image-to-video  
- **[Generate Your Talking Avatar from Video Reference](https://arxiv.org/abs/2604.27918v1)**  
  Authors: Zujin Guo, Zhenhui Ye, Yi Ren, Yuanming Li, Ce Chen, Zhibin Hong, Chen Change Loy  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.27918v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://www.heygen.com/research)  
  Keywords: dit, identity, benchmark, avatar, image-to-video  
- **[PhysLayer: Language-Guided Layered Animation with Depth-Aware Physics](https://arxiv.org/abs/2604.23574v1)**  
  Authors: Tianyidan Xie, Zhentao Huang, Mingjie Wang, Xin Huang, Jun Zhou, Minglun Gong, Zili Yi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.23574v1.pdf)  
  Keywords: evaluation, physical, simulation, physics, video synthesis, image animation, controllable, video generation, dynamics, image-to-video  
- **[WorldMark: A Unified Benchmark Suite for Interactive Video World Models](https://arxiv.org/abs/2604.21686v1)**  
  Authors: Xiaojie Xu, Zhengyuan Lin, Kang He, Yukang Feng, Xiaofeng Mao, Yuanyang Yin, Kaipeng Zhang, Yongtao Ge  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21686v1.pdf)  
  Keywords: evaluation, trajectory, world model, style, dit, benchmark, interactive, video generation, image-to-video  

### Long Video Generation

*Showing the latest 50 out of 113 papers*

- **[RAVEN: Real-time Autoregressive Video Extrapolation with Consistency-model GRPO](https://arxiv.org/abs/2605.15190v1)**  
  Authors: Yanzuo Lu, Ronglai Zuo, Jiankang Deng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.15190v1.pdf)  
  Keywords: evaluation, distillation, dit, autoregressive, video diffusion, streaming, denoising, diffusion model  
- **[Causal Forcing++: Scalable Few-Step Autoregressive Diffusion Distillation for Real-Time Interactive Video Generation](https://arxiv.org/abs/2605.15141v1)**  
  Authors: Min Zhao, Hongzhou Zhu, Kaiwen Zheng, Zihan Zhou, Bokai Yan, Xinyuan Li, Xiao Yang, Chongxuan Li, Jun Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.15141v1.pdf) | [![GitHub](https://img.shields.io/github/stars/thu-ml/Causal-Forcing?style=social)](https://github.com/thu-ml/Causal-Forcing)  
  Keywords: distillation, world model, dit, interactive, autoregressive, efficient, streaming, action-conditioned, controllable, video generation  
- **[DriveCtrl: Conditioned Sim-to-Real Driving Video Generation](https://arxiv.org/abs/2605.15116v1)**  
  Authors: Haonan Zhao, Yiting Wang, Jingkun Chen, Valentina Donzella, Thomas Bashford-Rogers, Kurt Debattista  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.15116v1.pdf)  
  Keywords: temporal consistency, evaluation, style, dit, autonomous driving, simulation, video synthesis, layout, depth-guided, controllable, video generation, dynamics  
- **[EverAnimate: Minute-Scale Human Animation via Latent Flow Restoration](https://arxiv.org/abs/2605.15042v1)**  
  Authors: Wuyang Li, Yang Gao, Mariam Hassan, Lan Feng, Wentao Pan, Po-Chien Luan, Alexandre Alahi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.15042v1.pdf)  
  Keywords: identity, flow matching, human animation, efficient, long-form, human motion, video generation  
- **[SEDiT: Mask-Free Video Subtitle Erasure via One-step Diffusion Transformer](https://arxiv.org/abs/2605.14894v1)**  
  Authors: Zheng Hui, Yunlong Bai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.14894v1.pdf)  
  Keywords: temporal consistency, rectified flow, dit, efficient, video editing, video diffusion, diffusion transformer, streaming, denoising, diffusion model  
- **[PROVE: A Perceptual RemOVal cohErence Benchmark for Visual Media](https://arxiv.org/abs/2605.14534v1)**  
  Authors: Fuhao Li, Shaofeng You, Jiagao Hu, Yu Liu, Yuxuan Chen, Zepeng Wang, Fei Wang, Daiguo Zhou, Jian Luan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.14534v1.pdf) | [![GitHub](https://img.shields.io/github/stars/xiaomi-research/prove?style=social)](https://github.com/xiaomi-research/prove)  
  Keywords: temporal consistency, dit, evaluation, benchmark  
- **[Head Forcing: Long Autoregressive Video Generation via Head Heterogeneity](https://arxiv.org/abs/2605.14487v1)**  
  Authors: Jiahao Tian, Yiwei Wang, Gang Yu, Chi Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.14487v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jiahaotian-sjtu.github.io/headforcing.github.io)  
  Keywords: dit, autoregressive, video diffusion, diffusion transformer, interactive, video generation, diffusion model  
- **[Delta Forcing: Trust Region Steering for Interactive Autoregressive Video Generation](https://arxiv.org/abs/2605.14382v1)**  
  Authors: Yuheng Wu, Xiangbo Gao, Tianhao Chen, Xinghao Chen, Qing Yin, Zhengzhong Tu, Dongman Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.14382v1.pdf)  
  Keywords: trajectory, world model, dit, autoregressive, streaming, interactive, video generation  
- **[KVPO: ODE-Native GRPO for Autoregressive Video Alignment via KV Semantic Exploration](https://arxiv.org/abs/2605.14278v1)**  
  Authors: Ruicheng Zhang, Kaixi Cong, Jun Zhou, Zhizhou Zhong, Zunnan Xu, Shuiyang Mao, Wei Liu, Xiu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.14278v1.pdf)  
  Keywords: trajectory, autoregressive, streaming, dynamics  
- **[PhyMotion: Structured 3D Motion Reward for Physics-Grounded Human Video Generation](https://arxiv.org/abs/2605.14269v1)**  
  Authors: Yidong Huang, Zun Wang, Han Lin, Dong-Ki Kim, Shayegan Omidshafiei, Jaehong Yoon, Jaemin Cho, Yue Zhang, Mohit Bansal  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.14269v1.pdf)  
  Keywords: evaluation, physical, physics, autoregressive, dynamics, human motion, video generation  

### Personalization & Customization

*Showing the latest 50 out of 77 papers*

- **[RefDecoder: Enhancing Visual Generation with Conditional Video Decoding](https://arxiv.org/abs/2605.15196v1)**  
  Authors: Xiang Fan, Yuheng Wang, Bohan Fang, Zhongzheng Ren, Ranjay Krishna  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.15196v1.pdf)  
  Keywords: style, dit, video editing, denoising, benchmark, video generation, diffusion model, i2v  
- **[DriveCtrl: Conditioned Sim-to-Real Driving Video Generation](https://arxiv.org/abs/2605.15116v1)**  
  Authors: Haonan Zhao, Yiting Wang, Jingkun Chen, Valentina Donzella, Thomas Bashford-Rogers, Kurt Debattista  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.15116v1.pdf)  
  Keywords: temporal consistency, evaluation, style, dit, autonomous driving, simulation, video synthesis, layout, depth-guided, controllable, video generation, dynamics  
- **[EverAnimate: Minute-Scale Human Animation via Latent Flow Restoration](https://arxiv.org/abs/2605.15042v1)**  
  Authors: Wuyang Li, Yang Gao, Mariam Hassan, Lan Feng, Wentao Pan, Po-Chien Luan, Alexandre Alahi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.15042v1.pdf)  
  Keywords: identity, flow matching, human animation, efficient, long-form, human motion, video generation  
- **[Compositional Video Generation via Inference-Time Guidance](https://arxiv.org/abs/2605.14988v1)**  
  Authors: Ariel Shaulov, Eitan Shaar, Amit Edenzon, Gal Chechik, Lior Wolf  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.14988v1.pdf)  
  Keywords: trajectory, architecture, layout, video diffusion, denoising, benchmark, concept, text-to-video, video generation, diffusion model  
- **[CRePE: Curved Ray Expectation Positional Encoding for Unified-Camera-Controlled Video Generation](https://arxiv.org/abs/2605.12938v1)**  
  Authors: Seonghyun Jin, Youngmin Kim, Sunwoo Park, Jong Chul Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.12938v1.pdf)  
  Keywords: style, video generation, dit, camera control  
- **[GaitProtector: Impersonation-Driven Gait De-Identification via Training-Free Diffusion Latent Optimization](https://arxiv.org/abs/2605.12431v1)**  
  Authors: Huiran Duan, Qian Zhou, Zhongliang Guo, Junhao Dong, Yuqi Li, Guoying Zhao, Yingli Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.12431v1.pdf)  
  Keywords: 3d video, trajectory, identity, video diffusion, dynamics, diffusion model  
- **[PresentAgent-2: Towards Generalist Multimodal Presentation Agents](https://arxiv.org/abs/2605.11363v1)**  
  Authors: Wei Wu, Ziyang Xu, Zeyu Zhang, Yang Zhao, Hao Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.11363v1.pdf) | [![GitHub](https://img.shields.io/github/stars/AIGeeksGroup/PresentAgent-2?style=social)](https://github.com/AIGeeksGroup/PresentAgent-2) | [![Project](https://img.shields.io/badge/-Project-blue)](https://aigeeksgroup.github.io/PresentAgent-2)  
  Keywords: evaluation, concept, benchmark, interactive, video generation  
- **[TIE: Time Interval Encoding for Video Generation over Events](https://arxiv.org/abs/2605.10543v1)**  
  Authors: Zhilei Shu, Shangwen Zhu, Zihang Liang, Xiaofan Li, Qianyu Peng, Xinyu Cui, Bo Ye, Yiming Li, Fan Cheng, Jian Zhao, Yang Cao, Zheng-Jun Zha, Ruili Feng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.10543v1.pdf) | [![GitHub](https://img.shields.io/github/stars/MatrixTeam-AI/TIE?style=social)](https://github.com/MatrixTeam-AI/TIE)  
  Keywords: trajectory, style, dit, efficient, diffusion transformer, interactive, robotics, video generation  
- **[Improving Human Image Animation via Semantic Representation Alignment](https://arxiv.org/abs/2605.10523v1)**  
  Authors: Chang Liu, Mengting Chen, Yixuan Huang, Haoning Wu, Chen Ju, Shuai Xiao, Jinsong Lan, Yanfeng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.10523v1.pdf)  
  Keywords: long video, dit, identity, image animation, video generation, diffusion model, image-to-video  
- **[MoCoTalk: Multi-Conditional Diffusion with Adaptive Router for Controllable Talking Head Generation](https://arxiv.org/abs/2605.08050v1)**  
  Authors: Xinyan Ye, Jiankang Deng, Abbas Edalat  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.08050v1.pdf)  
  Keywords: talking head, dit, identity, video diffusion, controllable, dynamics  

### Physical Understanding

*Showing the latest 50 out of 159 papers*

- **[Quantitative Video World Model Evaluation for Geometric-Consistency](https://arxiv.org/abs/2605.15185v1)**  
  Authors: Jiaxin Wu, Yihao Pi, Yinling Zhang, Yuheng Li, Xueyan Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.15185v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pdi-bench.github.io)  
  Keywords: evaluation, physical, world model, dit, video generation  
- **[Warp-as-History: Generalizable Camera-Controlled Video Generation from One Training Video](https://arxiv.org/abs/2605.15182v1)**  
  Authors: Yifan Wang, Tong He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.15182v1.pdf)  
  Keywords: trajectory, dit, denoising, dynamics, video generation  
- **[DriveCtrl: Conditioned Sim-to-Real Driving Video Generation](https://arxiv.org/abs/2605.15116v1)**  
  Authors: Haonan Zhao, Yiting Wang, Jingkun Chen, Valentina Donzella, Thomas Bashford-Rogers, Kurt Debattista  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.15116v1.pdf)  
  Keywords: temporal consistency, evaluation, style, dit, autonomous driving, simulation, video synthesis, layout, depth-guided, controllable, video generation, dynamics  
- **[MechVerse: Evaluating Physical Motion Consistency in Video Generation Models](https://arxiv.org/abs/2605.14843v1)**  
  Authors: Rahul Jain, Mayank Patel, Asim Unmesh, Karthik Ramani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.14843v1.pdf)  
  Keywords: physical, dit, benchmark, video generation, image-to-video  
- **[Probing into Camera Control of Video Models](https://arxiv.org/abs/2605.14815v1)**  
  Authors: Chen Hou, Christian Rupprecht  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.14815v1.pdf)  
  Keywords: dit, camera control, video diffusion, denoising, benchmark, dynamics, video generation, diffusion model  
- **[KVPO: ODE-Native GRPO for Autoregressive Video Alignment via KV Semantic Exploration](https://arxiv.org/abs/2605.14278v1)**  
  Authors: Ruicheng Zhang, Kaixi Cong, Jun Zhou, Zhizhou Zhong, Zunnan Xu, Shuiyang Mao, Wei Liu, Xiu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.14278v1.pdf)  
  Keywords: trajectory, autoregressive, streaming, dynamics  
- **[CreFlow: Corrective Reflow for Sparse-Reward Embodied Video Diffusion RL](https://arxiv.org/abs/2605.14274v1)**  
  Authors: Zhenyang Ni, Yijiang Li, Ruochen Jiao, Simon Sinong Zhan, Sipeng Chen, Zhenfei Yin, Minshuo Chen, Philip Torr, Zhaoran Wang, Qi Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.14274v1.pdf)  
  Keywords: evaluation, physical, dit, video diffusion, video generation  
- **[PhyMotion: Structured 3D Motion Reward for Physics-Grounded Human Video Generation](https://arxiv.org/abs/2605.14269v1)**  
  Authors: Yidong Huang, Zun Wang, Han Lin, Dong-Ki Kim, Shayegan Omidshafiei, Jaehong Yoon, Jaemin Cho, Yue Zhang, Mohit Bansal  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.14269v1.pdf)  
  Keywords: evaluation, physical, physics, autoregressive, dynamics, human motion, video generation  
- **[TeDiO: Temporal Diagonal Optimization for Training-Free Coherent Video Diffusion](https://arxiv.org/abs/2605.14136v1)**  
  Authors: Nurislam Tursynbek, Zhiqiang Lao, Heather Yu, Gedas Bertasius, Marc Niethammer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.14136v1.pdf)  
  Keywords: temporal consistency, efficient, video diffusion, diffusion transformer, text-to-video, video generation, diffusion model, dynamics  
- **[RoboEvolve: Co-Evolving Planner-Simulator for Robotic Manipulation with Limited Data](https://arxiv.org/abs/2605.13775v1)**  
  Authors: Harold Haodong Chen, Sirui Chen, Yingjie Xu, Wenhang Ge, Ying-Cong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.13775v1.pdf)  
  Keywords: physical, video generation  

### Surveys & Benchmarks

*Showing the latest 50 out of 222 papers*

- **[EntityBench: Towards Entity-Consistent Long-Range Multi-Shot Video Generation](https://arxiv.org/abs/2605.15199v1)**  
  Authors: Ruozhen He, Meng Wei, Ziyan Yang, Vicente Ordonez  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.15199v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Catherine-R-He/EntityBench?style=social)](https://github.com/Catherine-R-He/EntityBench)  
  Keywords: video generation, evaluation, benchmark  
- **[RefDecoder: Enhancing Visual Generation with Conditional Video Decoding](https://arxiv.org/abs/2605.15196v1)**  
  Authors: Xiang Fan, Yuheng Wang, Bohan Fang, Zhongzheng Ren, Ranjay Krishna  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.15196v1.pdf)  
  Keywords: style, dit, video editing, denoising, benchmark, video generation, diffusion model, i2v  
- **[RAVEN: Real-time Autoregressive Video Extrapolation with Consistency-model GRPO](https://arxiv.org/abs/2605.15190v1)**  
  Authors: Yanzuo Lu, Ronglai Zuo, Jiankang Deng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.15190v1.pdf)  
  Keywords: evaluation, distillation, dit, autoregressive, video diffusion, streaming, denoising, diffusion model  
- **[Quantitative Video World Model Evaluation for Geometric-Consistency](https://arxiv.org/abs/2605.15185v1)**  
  Authors: Jiaxin Wu, Yihao Pi, Yinling Zhang, Yuheng Li, Xueyan Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.15185v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pdi-bench.github.io)  
  Keywords: evaluation, physical, world model, dit, video generation  
- **[DriveCtrl: Conditioned Sim-to-Real Driving Video Generation](https://arxiv.org/abs/2605.15116v1)**  
  Authors: Haonan Zhao, Yiting Wang, Jingkun Chen, Valentina Donzella, Thomas Bashford-Rogers, Kurt Debattista  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.15116v1.pdf)  
  Keywords: temporal consistency, evaluation, style, dit, autonomous driving, simulation, video synthesis, layout, depth-guided, controllable, video generation, dynamics  
- **[Compositional Video Generation via Inference-Time Guidance](https://arxiv.org/abs/2605.14988v1)**  
  Authors: Ariel Shaulov, Eitan Shaar, Amit Edenzon, Gal Chechik, Lior Wolf  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.14988v1.pdf)  
  Keywords: trajectory, architecture, layout, video diffusion, denoising, benchmark, concept, text-to-video, video generation, diffusion model  
- **[Sat3DGen: Comprehensive Street-Level 3D Scene Generation from Single Satellite Image](https://arxiv.org/abs/2605.14984v1)**  
  Authors: Ming Qian, Zimin Xia, Changkun Liu, Shuailei Ma, Wen Wang, Zeran Ke, Bin Tan, Hang Zhang, Gui-Song Xia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.14984v1.pdf) | [![GitHub](https://img.shields.io/github/stars/qianmingduowan/Sat3DGen?style=social)](https://github.com/qianmingduowan/Sat3DGen)  
  Keywords: video generation, benchmark  
- **[MechVerse: Evaluating Physical Motion Consistency in Video Generation Models](https://arxiv.org/abs/2605.14843v1)**  
  Authors: Rahul Jain, Mayank Patel, Asim Unmesh, Karthik Ramani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.14843v1.pdf)  
  Keywords: physical, dit, benchmark, video generation, image-to-video  
- **[Probing into Camera Control of Video Models](https://arxiv.org/abs/2605.14815v1)**  
  Authors: Chen Hou, Christian Rupprecht  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.14815v1.pdf)  
  Keywords: dit, camera control, video diffusion, denoising, benchmark, dynamics, video generation, diffusion model  
- **[Generating HDR Video from SDR Video](https://arxiv.org/abs/2605.14703v1)**  
  Authors: SaiKiran Tedla, Francesco Banterle, Trevor Canham, Karanpreet Raja, David B. Lindell, Kiriakos N. Kutulakos, Jiacheng Li, Feiran Li, Daisuke Iso  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.14703v1.pdf)  
  Keywords: video synthesis, film, evaluation  

### Text-to-Video Generation

- **[Compositional Video Generation via Inference-Time Guidance](https://arxiv.org/abs/2605.14988v1)**  
  Authors: Ariel Shaulov, Eitan Shaar, Amit Edenzon, Gal Chechik, Lior Wolf  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.14988v1.pdf)  
  Keywords: trajectory, architecture, layout, video diffusion, denoising, benchmark, concept, text-to-video, video generation, diffusion model  
- **[TeDiO: Temporal Diagonal Optimization for Training-Free Coherent Video Diffusion](https://arxiv.org/abs/2605.14136v1)**  
  Authors: Nurislam Tursynbek, Zhiqiang Lao, Heather Yu, Gedas Bertasius, Marc Niethammer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.14136v1.pdf)  
  Keywords: temporal consistency, efficient, video diffusion, diffusion transformer, text-to-video, video generation, diffusion model, dynamics  
- **[Not All Tokens Need 40 Steps: Heterogeneous Step Allocation in Diffusion Transformers for Efficient Video Generation](https://arxiv.org/abs/2605.06892v1)**  
  Authors: Ernie Chu, Vishal M. Patel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.06892v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ernestchu.github.io/hsa)  
  Keywords: evaluation, t2v, dit, flow matching, efficient, diffusion transformer, denoising, dynamics, text-to-video, acceleration, video generation, i2v, image-to-video  
- **[FaithfulFaces: Pose-Faithful Facial Identity Preservation for Text-to-Video Generation](https://arxiv.org/abs/2605.04702v1)**  
  Authors: Yuanzhi Wang, Xuhua Ren, Jiaxiang Cheng, Bing Ma, Kai Yu, Sen Liang, Wenyue Li, Tianxiang Zheng, Qinglin Lu, Zhen Cui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.04702v1.pdf)  
  Keywords: text-to-video, t2v, video generation, identity  
- **[TrajShield: Trajectory-Level Safety Mediation for Defending Text-to-Video Models Against Jailbreak Attacks](https://arxiv.org/abs/2605.01761v1)**  
  Authors: Quanchen Zou, Nizhang Li, Wenxin Zhang, Jiaye Lin, Yangchen Zeng, Xiangzheng Zhang, Zonghao Ying  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.01761v1.pdf)  
  Keywords: text-to-video, t2v, trajectory  
- **[HuM-Eval: A Coarse-to-Fine Framework for Human-Centric Video Evaluation](https://arxiv.org/abs/2604.25361v1)**  
  Authors: Bingzi Zhang, Kaisi Guan, Ruihua Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.25361v1.pdf)  
  Keywords: evaluation, benchmark, text-to-video, human motion, video generation  
- **[World-R1: Reinforcing 3D Constraints for Text-to-Video Generation](https://arxiv.org/abs/2604.24764v1)**  
  Authors: Weijie Wang, Xiaoxuan He, Youping Gu, Yifan Yang, Zeyu Zhang, Yefei He, Yanbo Ding, Xirui Hu, Donny Y. Chen, Zhiyuan He, Yuqing Yang, Bohan Zhuang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.24764v1.pdf)  
  Keywords: evaluation, dit, simulation, architecture, text-to-video, video generation  
- **[BRITE: A Benchmark for Reliable and Interpretable T2V Evaluation on Implausible Scenarios](https://arxiv.org/abs/2605.00873v1)**  
  Authors: Advait Tilak, Jiwon Choi, Nazifa Mouli, Wei Le  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.00873v1.pdf)  
  Keywords: text-to-video, t2v, evaluation, benchmark  
- **[KD-CVG: A Knowledge-Driven Approach for Creative Video Generation](https://arxiv.org/abs/2604.21362v1)**  
  Authors: Linkai Liu, Wei Feng, Xi Zhao, Shen Zhang, Xingye Chen, Zheng Zhang, Jingjing Lv, Junjie Shen, Ching Law, Yuchen Zhou, Zipeng Guo, Chao Gou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21362v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kdcvg.github.io/KDCVG)  
  Keywords: advertising, t2v, text-to-video, video generation, creative  
- **[Sparse Forcing: Native Trainable Sparse Attention for Real-time Autoregressive Diffusion Video Generation](https://arxiv.org/abs/2604.21221v1)**  
  Authors: Boxun Xu, Yuming Du, Zichang Liu, Siyu Yang, Ziyang Jiang, Siqi Yan, Rajasi Saha, Albert Pumarola, Wenchen Wang, Peng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21221v1.pdf)  
  Keywords: autoregressive, video diffusion, efficient, text-to-video, video generation, diffusion model  

### Video Editing

- **[RefDecoder: Enhancing Visual Generation with Conditional Video Decoding](https://arxiv.org/abs/2605.15196v1)**  
  Authors: Xiang Fan, Yuheng Wang, Bohan Fang, Zhongzheng Ren, Ranjay Krishna  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.15196v1.pdf)  
  Keywords: style, dit, video editing, denoising, benchmark, video generation, diffusion model, i2v  
- **[SEDiT: Mask-Free Video Subtitle Erasure via One-step Diffusion Transformer](https://arxiv.org/abs/2605.14894v1)**  
  Authors: Zheng Hui, Yunlong Bai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.14894v1.pdf)  
  Keywords: temporal consistency, rectified flow, dit, efficient, video editing, video diffusion, diffusion transformer, streaming, denoising, diffusion model  
- **[OphEdit: Training-Free Text-Guided Editing of Ophthalmic Surgical Videos](https://arxiv.org/abs/2605.07695v1)**  
  Authors: Ritul Jangir, Arkya Jyoti Bagchi, Aiman Farooq, Mangalton Okram, Saurabh Seetaram Korgaonkar, Deepak Mishra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.07695v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ophedit/OphEdit?style=social)](https://github.com/ophedit/OphEdit)  
  Keywords: temporal consistency, evaluation, dit, video editing, denoising, video generation, medical  
- **[RealCam: Real-Time Novel-View Video Generation with Interactive Camera Control](https://arxiv.org/abs/2605.06051v1)**  
  Authors: Youcan Xu, Jiaxin Shi, Zhen Wang, Wensong Song, Feifei Shao, Chen Liang, Jun Xiao, Long Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.06051v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xyc-fly.github.io/RealCam)  
  Keywords: temporal consistency, distillation, style, camera control, video-to-video, autoregressive, efficient, streaming, interactive, film, video generation  
- **[Latent Inter-Frame Pruning: A Training-Free Method Bridging Traditional Video Compression and Modern Diffusion Transformers for Efficient Generation](https://arxiv.org/abs/2604.23858v1)**  
  Authors: Dennis Menn, Chih-Hsien Chou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.23858v1.pdf)  
  Keywords: dit, efficient, video editing, diffusion transformer, video generation, diffusion model  
- **[LIVE: Leveraging Image Manipulation Priors for Instruction-based Video Editing](https://arxiv.org/abs/2604.17021v1)**  
  Authors: Weicheng Wang, Zhicheng Zhang, Zhongqi Zhang, Juncheng Zhou, Yongjie Zhu, Wenyu Qin, Meng Wang, Pengfei Wan, Jufeng Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.17021v1.pdf)  
  Keywords: evaluation, dit, video editing, benchmark, video generation  
- **[UniEditBench: A Unified and Cost-Effective Benchmark for Image and Video Editing via Distilled MLLMs](https://arxiv.org/abs/2604.15871v1)**  
  Authors: Lifan Jiang, Tianrun Wu, Yuhang Pei, Chenyang Wang, Boxi Wu, Deng Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.15871v1.pdf) | [![GitHub](https://img.shields.io/github/stars/wesar1/UniEditBench?style=social)](https://github.com/wesar1/UniEditBench)  
  Keywords: dit, video editing, evaluation, benchmark  
- **[Empowering Video Translation using Multimodal Large Language Models](https://arxiv.org/abs/2604.11283v1)**  
  Authors: Bingzheng QU, Kehai Chen, Xuefeng Bai, Min Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.11283v1.pdf)  
  Keywords: dit, identity, video translation, controllable, survey  
- **[Rein3D: Reinforced 3D Indoor Scene Generation with Panoramic Video Diffusion Models](https://arxiv.org/abs/2604.10578v2)**  
  Authors: Dehui Wang, Congsheng Xu, Rong Wei, Yue Shi, Shoufa Chen, Dingxiang Luo, Tianshuo Yang, Xiaokang Yang, Wei Sui, Yusen Qin, Rui Tang, Yao Mu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.10578v2.pdf)  
  Keywords: video-to-video, super-resolution, video diffusion, diffusion model  
- **[InsEdit: Towards Instruction-based Visual Editing via Data-Efficient Video Diffusion Models Adaptation](https://arxiv.org/abs/2604.08646v1)**  
  Authors: Zhefan Rao, Bin Zou, Haoxuan Che, Xuanhua He, Chong Hou Choi, Yanheng Li, Rui Liu, Qifeng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08646v1.pdf)  
  Keywords: dit, architecture, efficient, video diffusion, video editing, benchmark, video generation, diffusion model  

### Video Inpainting & Completion

- **[Relit-LiVE: Relight Video by Jointly Learning Environment Video](https://arxiv.org/abs/2605.06658v1)**  
  Authors: Weiqing Xiao, Hong Li, Xiuyu Yang, Houyuan Chen, Wenyi Li, Tianqi Liu, Shaocong Xu, Chongjie Ye, Hao Zhao, Beibei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.06658v1.pdf) | [![GitHub](https://img.shields.io/github/stars/zhuxing0/Relit-LiVE?style=social)](https://github.com/zhuxing0/Relit-LiVE)  
  Keywords: physical, video prediction, dit, video diffusion, streaming, benchmark, diffusion model  
- **[Quaternion Nonlinear Transform-Induced Nuclear Norm for Low-Rank Tensor Completion](https://arxiv.org/abs/2605.01467v1)**  
  Authors: Biswarup Karmakar, Ratikanta Behera  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.01467v1.pdf)  
  Keywords: efficient, benchmark, video inpainting  
- **[LMGenDrive: Bridging Multimodal Understanding and Generative World Modeling for End-to-End Driving](https://arxiv.org/abs/2604.08719v1)**  
  Authors: Hao Shao, Letian Wang, Yang Zhou, Yuxuan Hu, Zhuofan Zong, Steven L. Waslander, Wei Zhan, Hongsheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08719v1.pdf)  
  Keywords: world model, video prediction, autonomous driving, autoregressive, benchmark, video generation  
- **[Novel View Synthesis as Video Completion](https://arxiv.org/abs/2604.08500v1)**  
  Authors: Qi Wu, Khiem Vuong, Minsik Jeon, Srinivasa Narasimhan, Deva Ramanan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08500v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://frame-crafter.github.io)  
  Keywords: video completion, novel view, video diffusion, benchmark, diffusion model  
- **[SEM-ROVER: Semantic Voxel-Guided Diffusion for Large-Scale Driving Scene Generation](https://arxiv.org/abs/2604.06113v1)**  
  Authors: Hiba Dahmani, Nathan Piasco, Moussab Bennehar, Luis Roldão, Dzmitry Tsishkou, Laurent Caraffa, Jean-Philippe Tarel, Roland Brémond  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06113v1.pdf)  
  Keywords: outpainting, dit, diffusion model  
- **[ChopGrad: Pixel-Wise Losses for Latent Video Diffusion via Truncated Backpropagation](https://arxiv.org/abs/2603.17812v2)**  
  Authors: Dmitriy Rivkin, Parker Ewen, Lili Gao, Julian Ost, Stefanie Walz, Rasika Kangutkar, Mario Bijelic, Felix Heide  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17812v2.pdf)  
  Keywords: dit, video inpainting, super-resolution, video diffusion, efficient, latent video, video generation, diffusion model, video enhancement  
- **[ConfCtrl: Enabling Precise Camera Control in Video Diffusion via Confidence-Aware Interpolation](https://arxiv.org/abs/2603.09819v1)**  
  Authors: Liudi Yang, George Eskandar, Fengyi Shen, Mohammad Altillawi, Yang Bai, Chi Zhang, Ziyuan Liu, Abhinav Valada  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09819v1.pdf)  
  Keywords: video interpolation, dit, camera control, novel view, video diffusion, diffusion model  

### Video Super-Resolution & Enhancement

*Showing the latest 50 out of 72 papers*

- **[RefDecoder: Enhancing Visual Generation with Conditional Video Decoding](https://arxiv.org/abs/2605.15196v1)**  
  Authors: Xiang Fan, Yuheng Wang, Bohan Fang, Zhongzheng Ren, Ranjay Krishna  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.15196v1.pdf)  
  Keywords: style, dit, video editing, denoising, benchmark, video generation, diffusion model, i2v  
- **[RAVEN: Real-time Autoregressive Video Extrapolation with Consistency-model GRPO](https://arxiv.org/abs/2605.15190v1)**  
  Authors: Yanzuo Lu, Ronglai Zuo, Jiankang Deng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.15190v1.pdf)  
  Keywords: evaluation, distillation, dit, autoregressive, video diffusion, streaming, denoising, diffusion model  
- **[Warp-as-History: Generalizable Camera-Controlled Video Generation from One Training Video](https://arxiv.org/abs/2605.15182v1)**  
  Authors: Yifan Wang, Tong He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.15182v1.pdf)  
  Keywords: trajectory, dit, denoising, dynamics, video generation  
- **[Compositional Video Generation via Inference-Time Guidance](https://arxiv.org/abs/2605.14988v1)**  
  Authors: Ariel Shaulov, Eitan Shaar, Amit Edenzon, Gal Chechik, Lior Wolf  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.14988v1.pdf)  
  Keywords: trajectory, architecture, layout, video diffusion, denoising, benchmark, concept, text-to-video, video generation, diffusion model  
- **[SEDiT: Mask-Free Video Subtitle Erasure via One-step Diffusion Transformer](https://arxiv.org/abs/2605.14894v1)**  
  Authors: Zheng Hui, Yunlong Bai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.14894v1.pdf)  
  Keywords: temporal consistency, rectified flow, dit, efficient, video editing, video diffusion, diffusion transformer, streaming, denoising, diffusion model  
- **[Probing into Camera Control of Video Models](https://arxiv.org/abs/2605.14815v1)**  
  Authors: Chen Hou, Christian Rupprecht  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.14815v1.pdf)  
  Keywords: dit, camera control, video diffusion, denoising, benchmark, dynamics, video generation, diffusion model  
- **[CoReDiT: Spatial Coherence-Guided Token Pruning and Reconstruction for Efficient Diffusion Transformers](https://arxiv.org/abs/2605.14191v1)**  
  Authors: Zhuojin Li, Hsin-Pai Cheng, Hong Cai, Shizhong Han, Fatih Porikli  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.14191v1.pdf)  
  Keywords: dit, efficient, denoising, diffusion transformer, video generation  
- **[DiffST: Spatiotemporal-Aware Diffusion for Real-World Space-Time Video Super-Resolution](https://arxiv.org/abs/2605.13182v1)**  
  Authors: Zheng Chen, Ruofan Yang, Jin Han, Dehua Song, Zichen Zou, Chunming He, Yong Guo, Yulun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.13182v1.pdf) | [![GitHub](https://img.shields.io/github/stars/zhengchen1999/DiffST?style=social)](https://github.com/zhengchen1999/DiffST)  
  Keywords: frame interpolation, super-resolution, video diffusion, efficient, diffusion model  
- **[FIS-DiT: Breaking the Few-Step Video Inference Barrier via Training-Free Frame Interleaved Sparsity](https://arxiv.org/abs/2605.11869v1)**  
  Authors: Jian Tang, Jiawei Fan, Qingbin Liu, Zheng Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.11869v1.pdf)  
  Keywords: evaluation, distillation, trajectory, dit, video diffusion, diffusion transformer, denoising, acceleration, video generation  
- **[VidSplat: Gaussian Splatting Reconstruction with Geometry-Guided Video Diffusion Priors](https://arxiv.org/abs/2605.11424v1)**  
  Authors: Jimin Tang, Wenyuan Zhang, Junsheng Zhou, Zian Huang, Kanle Shi, Shenkun Xu, Yu-Shen Liu, Zhizhong Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.11424v1.pdf)  
  Keywords: novel view, video diffusion, denoising, benchmark, 3d consistent  

### World Models & Simulation

*Showing the latest 50 out of 111 papers*

- **[Quantitative Video World Model Evaluation for Geometric-Consistency](https://arxiv.org/abs/2605.15185v1)**  
  Authors: Jiaxin Wu, Yihao Pi, Yinling Zhang, Yuheng Li, Xueyan Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.15185v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pdi-bench.github.io)  
  Keywords: evaluation, physical, world model, dit, video generation  
- **[Causal Forcing++: Scalable Few-Step Autoregressive Diffusion Distillation for Real-Time Interactive Video Generation](https://arxiv.org/abs/2605.15141v1)**  
  Authors: Min Zhao, Hongzhou Zhu, Kaiwen Zheng, Zihan Zhou, Bokai Yan, Xinyuan Li, Xiao Yang, Chongxuan Li, Jun Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.15141v1.pdf) | [![GitHub](https://img.shields.io/github/stars/thu-ml/Causal-Forcing?style=social)](https://github.com/thu-ml/Causal-Forcing)  
  Keywords: distillation, world model, dit, interactive, autoregressive, efficient, streaming, action-conditioned, controllable, video generation  
- **[DriveCtrl: Conditioned Sim-to-Real Driving Video Generation](https://arxiv.org/abs/2605.15116v1)**  
  Authors: Haonan Zhao, Yiting Wang, Jingkun Chen, Valentina Donzella, Thomas Bashford-Rogers, Kurt Debattista  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.15116v1.pdf)  
  Keywords: temporal consistency, evaluation, style, dit, autonomous driving, simulation, video synthesis, layout, depth-guided, controllable, video generation, dynamics  
- **[Head Forcing: Long Autoregressive Video Generation via Head Heterogeneity](https://arxiv.org/abs/2605.14487v1)**  
  Authors: Jiahao Tian, Yiwei Wang, Gang Yu, Chi Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.14487v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jiahaotian-sjtu.github.io/headforcing.github.io)  
  Keywords: dit, autoregressive, video diffusion, diffusion transformer, interactive, video generation, diffusion model  
- **[Delta Forcing: Trust Region Steering for Interactive Autoregressive Video Generation](https://arxiv.org/abs/2605.14382v1)**  
  Authors: Yuheng Wu, Xiangbo Gao, Tianhao Chen, Xinghao Chen, Qing Yin, Zhengzhong Tu, Dongman Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.14382v1.pdf)  
  Keywords: trajectory, world model, dit, autoregressive, streaming, interactive, video generation  
- **[AnyFlow: Any-Step Video Diffusion Model with On-Policy Flow Map Distillation](https://arxiv.org/abs/2605.13724v1)**  
  Authors: Yuchao Gu, Guian Fang, Yuxin Jiang, Weijia Mao, Song Han, Han Cai, Mike Zheng Shou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.13724v1.pdf)  
  Keywords: distillation, trajectory, simulation, architecture, efficient, video diffusion, video generation, diffusion model  
- **[CausalCine: Real-Time Autoregressive Generation for Multi-Shot Video Narratives](https://arxiv.org/abs/2605.12496v1)**  
  Authors: Yihao Meng, Zichen Liu, Hao Ouyang, Qiuyu Wang, Ka Leong Cheng, Yue Yu, Hanlin Wang, Haobo Li, Jiapeng Zhu, Yanhong Zeng, Xing Zhu, Yujun Shen, Qifeng Chen, Huamin Qu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.12496v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yihao-meng.github.io/CausalCine)  
  Keywords: autoregressive, streaming, interactive, acceleration, video generation  
- **[HorizonDrive: Self-Corrective Autoregressive World Model for Long-horizon Driving Simulation](https://arxiv.org/abs/2605.11596v1)**  
  Authors: Conglang Zhang, Yifan Zhan, Qingjie Wang, Zhanpeng Ouyang, Yu Li, Zihao Yang, Xiaoyang Guo, Weiqiang Ren, Qian Zhang, Zhen Dong, Yinqiang Zheng, Wei Yin, Zhengqing Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.11596v1.pdf)  
  Keywords: distillation, world model, simulation, efficient, autoregressive, streaming  
- **[PresentAgent-2: Towards Generalist Multimodal Presentation Agents](https://arxiv.org/abs/2605.11363v1)**  
  Authors: Wei Wu, Ziyang Xu, Zeyu Zhang, Yang Zhao, Hao Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.11363v1.pdf) | [![GitHub](https://img.shields.io/github/stars/AIGeeksGroup/PresentAgent-2?style=social)](https://github.com/AIGeeksGroup/PresentAgent-2) | [![Project](https://img.shields.io/badge/-Project-blue)](https://aigeeksgroup.github.io/PresentAgent-2)  
  Keywords: evaluation, concept, benchmark, interactive, video generation  
- **[PhyGround: Benchmarking Physical Reasoning in Generative World Models](https://arxiv.org/abs/2605.10806v1)**  
  Authors: Juyi Lin, Arash Akbari, Yumei He, Lin Zhao, Haichao Zhang, Arman Akbari, Xingchen Xu, Zoe Y. Lu, Enfu Nan, Hokin Deng, Edmund Yeh, Sarah Ostadabbas, Yun Fu, Jennifer Dy, Pu Zhao, Yanzhi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.10806v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://phyground.github.io)  
  Keywords: evaluation, physical, world model, physics-aware, dit, physics, benchmark, dynamics, video generation  



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
