# Awesome Video Diffusions [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Video Diffusion Models and Video Generation. Content is automatically updated daily.

> Last Update: 2026-03-31 02:28:25

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

- [3D-aware Video Generation](#3d-aware-video-generation) (30 papers) - Video generation with 3D awareness, multi-view consistency, and 4D content creation
- [Applications](#applications) (39 papers) - Domain-specific applications of video diffusion models
- [Architecture & Efficiency](#architecture-&-efficiency) (353 papers) - Architectural innovations (DiT, UNet), flow matching, and training/inference efficiency
- [Audio & Multi-modal](#audio-&-multi-modal) (29 papers) - Audio-driven and multi-modal conditioned video generation
- [Controllable Generation](#controllable-generation) (123 papers) - Controllable video generation with motion, camera, pose, or layout guidance
- [Human & Character Animation](#human-&-character-animation) (28 papers) - Human-centric video generation including talking heads, dance, and character animation
- [Image-to-Video Generation](#image-to-video-generation) (41 papers) - Methods for animating still images into videos
- [Long Video Generation](#long-video-generation) (118 papers) - Generating temporally consistent long-form videos beyond short clips
- [Personalization & Customization](#personalization-&-customization) (87 papers) - Personalized video generation with custom subjects, identities, or styles
- [Physical Understanding](#physical-understanding) (137 papers) - Physics-aware video generation and dynamics modeling
- [Surveys & Benchmarks](#surveys-&-benchmarks) (203 papers) - Survey papers, benchmarks, and evaluation metrics for video generation
- [Text-to-Video Generation](#text-to-video-generation) (69 papers) - Foundation models and methods for generating videos from text prompts
- [Video Editing](#video-editing) (35 papers) - Diffusion-based video editing, style transfer, and manipulation
- [Video Inpainting & Completion](#video-inpainting-&-completion) (4 papers) - Video inpainting, completion, outpainting, and temporal prediction
- [Video Super-Resolution & Enhancement](#video-super-resolution-&-enhancement) (60 papers) - Video quality improvement, upscaling, restoration, and frame interpolation
- [World Models & Simulation](#world-models-&-simulation) (94 papers) - Video generation as world simulators and interactive environment generation



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3D-aware Video Generation

- **[I3DM: Implicit 3D-aware Memory Retrieval and Injection for Consistent Video Scene Generation](https://arxiv.org/abs/2603.23413v1)**  
  Authors: Jia Li, Han Yan, Yihang Chen, Siqi Li, Xibin Song, Yifu Wang, Jianfei Cai, Tien-Tsin Wong, Pan Ji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23413v1.pdf)  
  Keywords: dit, video generation, novel view, 3d-aware, camera control  
- **[GO-Renderer: Generative Object Rendering with 3D-aware Controllable Video Diffusion Models](https://arxiv.org/abs/2603.23246v1)**  
  Authors: Zekai Gu, Shuoxuan Feng, Yansong Wang, Hanzhuo Huang, Zhongshuo Du, Chengfeng Zhao, Chengwei Ren, Peng Wang, Yuan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23246v1.pdf)  
  Keywords: video diffusion, dit, efficient, controllable, 3d-aware, diffusion model  
- **[Omni-WorldBench: Towards a Comprehensive Interaction-Centric Evaluation for World Models](https://arxiv.org/abs/2603.22212v1)**  
  Authors: Meiqi Wu, Zhixin Cai, Fufangchen Zhao, Xiaokun Feng, Rujing Dang, Bingze Song, Ruitian Tian, Jiashu Zhu, Jiachen Lei, Hao Dou, Jing Tang, Lei Sun, Jiahong Wu, Xiangxiang Chu, Zeming Liu, Kaiqi Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22212v1.pdf)  
  Keywords: video generation, evaluation, world model, benchmark, dynamics, interactive, 4d generation  
- **[X-World: Controllable Ego-Centric Multi-Camera World Models for Scalable End-to-End Driving](https://arxiv.org/abs/2603.19979v1)**  
  Authors: Chaoda Zheng, Sean Li, Jinhao Deng, Zhennan Wang, Shijia Chen, Liqiang Xiao, Ziheng Chi, Hongbin Lin, Kangjie Chen, Boyang Wang, Yu Zhang, Xianming Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19979v1.pdf)  
  Keywords: dit, simulation, video style transfer, video generation, action-conditioned, style, multi-view video, controllable, evaluation, world model, dynamics, autonomous driving, latent video, world simulator  
- **[OrbitNVS: Harnessing Video Diffusion Priors for Novel View Synthesis](https://arxiv.org/abs/2603.19613v1)**  
  Authors: Jinglin Liang, Zijian Zhou, Rui Huang, Shuangping Huang, Yichen Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19613v1.pdf)  
  Keywords: video diffusion, video generation, benchmark, novel view, camera control  
- **[3DreamBooth: High-Fidelity 3D Subject-Driven Video Generation Model](https://arxiv.org/abs/2603.18524v1)**  
  Authors: Hyun-kyu Ko, Jihyeon Park, Younghyun Kim, Dongheok Park, Eunbyung Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18524v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ko-lani.github.io/3DreamBooth)  
  Keywords: dit, subject-driven, video generation, identity, multi-view video, novel view, 3d-aware, customization  
- **[TAPESTRY: From Geometry to Appearance via Consistent Turntable Videos](https://arxiv.org/abs/2603.17735v1)**  
  Authors: Yan Zeng, Haoran Jiang, Kaixin Yao, Qixuan Zhang, Longwen Zhang, Lan Xu, Jingyi Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17735v1.pdf)  
  Keywords: video diffusion, dit, video generation, multi-modal, 3d-aware, diffusion model  
- **[Tri-Prompting: Video Diffusion with Unified Control over Scene, Subject, and Motion](https://arxiv.org/abs/2603.15614v1)**  
  Authors: Zhenghong Zhou, Xiaohang Zhan, Zhiqin Chen, Soo Ye Kim, Nanxuan Zhao, Haitian Zheng, Qing Liu, He Zhang, Zhe Lin, Yuqian Zhou, Jiebo Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15614v1.pdf)  
  Keywords: video diffusion, dit, motion control, identity, controllable, architecture, 3d-aware, diffusion model, customization  
- **[GeoNVS: Geometry Grounded Video Diffusion for Novel View Synthesis](https://arxiv.org/abs/2603.14965v1)**  
  Authors: Minjun Kang, Inkyu Shin, Taeyeop Lee, Myungchul Kim, In So Kweon, Kuk-Jin Yoon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14965v1.pdf)  
  Keywords: video diffusion, dit, camera control, novel view, diffusion model  
- **[MVHOI: Bridge Multi-view Condition to Complex Human-Object Interaction Video Reenactment via 3D Foundation Model](https://arxiv.org/abs/2603.14686v1)**  
  Authors: Jinguang Tong, Jinbo Wu, Kaisiyuan Wang, Zhelun Shen, Xuan Huang, Mochu Xiang, Xuesong Li, Yingying Li, Haocheng Feng, Chen Zhao, Hang Zhou, Wei He, Chuong Nguyen, Jingdong Wang, Hongdong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14686v1.pdf)  
  Keywords: dit, video generation, controllable, dynamics, novel view  

### Applications

- **[Face2Parts: Exploring Coarse-to-Fine Inter-Regional Facial Dependencies for Generalized Deepfake Detection](https://arxiv.org/abs/2603.26036v1)**  
  Authors: Kutub Uddin, Nusrat Tasnim, Byung Tae Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26036v1.pdf)  
  Keywords: advertising, benchmark  
- **[RefAlign: Representation Alignment for Reference-to-Video Generation](https://arxiv.org/abs/2603.25743v1)**  
  Authors: Lei Wang, YuXin Song, Ge Wu, Haocheng Feng, Hang Zhou, Jingdong Wang, Yaxing Wang, jian Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25743v1.pdf)  
  Keywords: dit, video generation, identity, video synthesis, controllable, advertising, benchmark, virtual try-on, diffusion transformer  
- **[AnyID: Ultra-Fidelity Universal Identity-Preserving Video Generation from Any Visual References](https://arxiv.org/abs/2603.25188v1)**  
  Authors: Jiahao Wang, Hualian Sheng, Sijia Cai, Yuxiao Yang, Weizhan Zhang, Caixia Yan, Bing Deng, Jieping Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25188v1.pdf)  
  Keywords: creative, video generation, identity, evaluation, architecture  
- **[DreamerAD: Efficient Reinforcement Learning via Latent World Model for Autonomous Driving](https://arxiv.org/abs/2603.24587v1)**  
  Authors: Pengxuan Yang, Yupeng Zheng, Deheng Qian, Zebin Xing, Qichao Zhang, Linbo Wang, Yichen Zhang, Shaoyu Guo, Zhongpu Xia, Qiang Chen, Junyu Han, Lingyun Xu, Yifeng Pan, Dongbin Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24587v1.pdf)  
  Keywords: autoregressive, dit, efficient, video generation, physical, world model, autonomous driving  
- **[Toward Physically Consistent Driving Video World Models under Challenging Trajectories](https://arxiv.org/abs/2603.24506v1)**  
  Authors: Jiawei Zhou, Zhenxin Zhu, Lingyi Du, Linye Lyu, Lijun Zhou, Zhanqian Wu, Hongcheng Luo, Zhuotao Tian, Bing Wang, Guang Chen, Hangjun Ye, Haiyang Sun, Yu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24506v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wm-research.github.io/PhyGenesis)  
  Keywords: dit, simulation, video generation, physical, world model, dynamics, autonomous driving, trajectory, physics  
- **[Foveated Diffusion: Efficient Spatially Adaptive Image and Video Generation](https://arxiv.org/abs/2603.23491v1)**  
  Authors: Brian Chao, Lior Yariv, Howard Xiao, Gordon Wetzstein  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23491v1.pdf)  
  Keywords: creative, efficient, video generation, interactive, diffusion model, streaming, flow matching  
- **[X-World: Controllable Ego-Centric Multi-Camera World Models for Scalable End-to-End Driving](https://arxiv.org/abs/2603.19979v1)**  
  Authors: Chaoda Zheng, Sean Li, Jinhao Deng, Zhennan Wang, Shijia Chen, Liqiang Xiao, Ziheng Chi, Hongbin Lin, Kangjie Chen, Boyang Wang, Yu Zhang, Xianming Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19979v1.pdf)  
  Keywords: dit, simulation, video style transfer, video generation, action-conditioned, style, multi-view video, controllable, evaluation, world model, dynamics, autonomous driving, latent video, world simulator  
- **[Student views in AI Ethics and Social Impact](https://arxiv.org/abs/2603.18827v1)**  
  Authors: Tudor-Dan Mihoc, Manuela-Andreea Petrescu, Emilia-Loredana Pop  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18827v1.pdf)  
  Keywords: autonomous driving, concept, education, survey  
- **[EVA: Aligning Video World Models with Executable Robot Actions via Inverse Dynamics Rewards](https://arxiv.org/abs/2603.17808v2)**  
  Authors: Ruixiang Wang, Qingming Liu, Yueci Deng, Guiliang Liu, Zhen Liu, Kui Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17808v2.pdf)  
  Keywords: dit, efficient, video generation, robotics, physical, world model, benchmark, dynamics, acceleration  
- **[Surg$Σ$: A Spectrum of Large-Scale Multimodal Data and Foundation Models for Surgical Intelligence](https://arxiv.org/abs/2603.16822v1)**  
  Authors: Zhitao Zeng, Mengya Xu, Jian Jiang, Pengfei Guo, Yunqiu Xu, Zhu Zhuo, Chang Han Low, Yufan He, Dong Yang, Chenxi Lin, Yiming Gu, Jiaxin Guo, Yutong Ban, Daguang Xu, Qi Dou, Yueming Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16822v1.pdf)  
  Keywords: medical  

### Architecture & Efficiency

*Showing the latest 50 out of 353 papers*

- **[MolmoPoint: Better Pointing for VLMs with Grounding Tokens](https://arxiv.org/abs/2603.28069v1)**  
  Authors: Christopher Clark, Yue Yang, Jae Sung Park, Zixian Ma, Jieyu Zhang, Rohun Tripathi, Mohammadreza Salehi, Sangho Lee, Taira Anderson, Winson Han, Ranjay Krishna  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.28069v1.pdf)  
  Keywords: dit, concept  
- **[FlashSign: Pose-Free Guidance for Efficient Sign Language Video Generation](https://arxiv.org/abs/2603.27915v1)**  
  Authors: Liuzhou Zhang, Zeyu Zhang, Biao Wu, Luyao Tang, Zirui Song, Hongyang He, Renda Han, Guangzhen Yao, Huacan Wang, Ronghao Chen, Xiuying Chen, Guan Huang, Zheng Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27915v1.pdf) | [![GitHub](https://img.shields.io/github/stars/AIGeeksGroup/FlashSign?style=social)](https://github.com/AIGeeksGroup/FlashSign)  
  Keywords: video generation, efficient, gesture  
- **[TokenDial: Continuous Attribute Control in Text-to-Video via Spatiotemporal Token Offsets](https://arxiv.org/abs/2603.27520v1)**  
  Authors: Zhixuan Liu, Peter Schaldenbrand, Yijun Li, Long Mai, Aniruddha Mahapatra, Cusuh Ham, Jean Oh, Jui-Hsien Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27520v1.pdf)  
  Keywords: dit, video generation, identity, text-to-video, evaluation, dynamics, style  
- **[LOME: Learning Human-Object Manipulation with Action-Conditioned Egocentric World Model](https://arxiv.org/abs/2603.27449v1)**  
  Authors: Quankai Gao, Jiawei Yang, Qiangeng Xu, Le Chen, Yue Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27449v1.pdf)  
  Keywords: dit, motion control, action-conditioned, text-to-video, gesture, physical, world model, t2v, physics, temporal consistency  
- **[LightMover: Generative Light Movement with Color and Intensity Controls](https://arxiv.org/abs/2603.27209v1)**  
  Authors: Gengze Zhou, Tianyu Wang, Soo Ye Kim, Zhixin Shu, Xin Yu, Yannick Hold-Geoffroy, Sumit Chaturvedi, Qi Wu, Zhe Lin, Scott Cohen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27209v1.pdf)  
  Keywords: video diffusion, dit, physical, controllable  
- **[EFlow: Fast Few-Step Video Generator Training from Scratch via Efficient Solution Flow](https://arxiv.org/abs/2603.27086v1)**  
  Authors: Dogyun Park, Yanyu Li, Sergey Tulyakov, Anil Kag  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27086v1.pdf)  
  Keywords: video diffusion, dit, efficient, text-to-video, diffusion transformer  
- **[LightCtrl: Training-free Controllable Video Relighting](https://arxiv.org/abs/2603.27083v1)**  
  Authors: Yizuo Peng, Xuelin Chen, Kai Zhang, Xiaodong Cun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27083v1.pdf) | [![GitHub](https://img.shields.io/github/stars/GVCLab/LightCtrl?style=social)](https://github.com/GVCLab/LightCtrl)  
  Keywords: video diffusion, dit, controllable, trajectory, temporal consistency, diffusion model  
- **[Think over Trajectories: Leveraging Video Generation to Reconstruct GPS Trajectories from Cellular Signaling](https://arxiv.org/abs/2603.26610v1)**  
  Authors: Ruixing Zhang, Hanzhang Jiang, Leilei Sun, Liangzhe Han, Jibin Wang, Weifeng Lv  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26610v1.pdf)  
  Keywords: video generation, image-to-video, dit, trajectory  
- **[VGGRPO: Towards World-Consistent Video Generation with 4D Latent Reward](https://arxiv.org/abs/2603.26599v1)**  
  Authors: Zhaochong An, Orest Kupyn, Théo Uscidda, Andrea Colaco, Karan Ahuja, Serge Belongie, Mar Gonzalez-Franco, Marta Tintore Gazulla  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26599v1.pdf)  
  Keywords: video diffusion, dit, efficient, video generation, benchmark, diffusion model  
- **[From Static to Dynamic: Exploring Self-supervised Image-to-Video Representation Transfer Learning](https://arxiv.org/abs/2603.26597v1)**  
  Authors: Yang Liu, Qianqian Xu, Peisong Wen, Siran Dai, Xilin Zhao, Qingming Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26597v1.pdf) | [![GitHub](https://img.shields.io/github/stars/yafeng19/Co-Settle?style=social)](https://github.com/yafeng19/Co-Settle)  
  Keywords: temporal consistency, image-to-video, dit  

### Audio & Multi-modal

- **[MoE-GRPO: Optimizing Mixture-of-Experts via Reinforcement Learning in Vision-Language Models](https://arxiv.org/abs/2603.24984v2)**  
  Authors: Dohwan Ko, Jinyoung Park, Seoung Choi, Sanghyeok Lee, Seohyun Lee, Hyunwoo J. Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24984v2.pdf)  
  Keywords: architecture, benchmark, multi-modal  
- **[Attention-aware Inference Optimizations for Large Vision-Language Models with Memory-efficient Decoding](https://arxiv.org/abs/2603.23914v1)**  
  Authors: Fatih Ilhan, Gaowen Liu, Ramana Rao Kompella, Selim Furkan Tekin, Tiansheng Huang, Zachary Yahn, Yichang Xu, Ling Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23914v1.pdf)  
  Keywords: benchmark, efficient, multi-modal  
- **[Mamba-VMR: Multimodal Query Augmentation via Generated Videos for Precise Temporal Grounding](https://arxiv.org/abs/2603.22121v1)**  
  Authors: Yunzhuo Sun, Xinyue Liu, Yanyang Li, Nanding Wu, Yifang Xu, Linlin Zong, Xianchao Zhang, Wenxin Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22121v1.pdf)  
  Keywords: dit, efficient, text-to-video, multi-modal, evaluation, benchmark, dynamics, architecture, text-driven video  
- **[EARTalking: End-to-end GPT-style Autoregressive Talking Head Synthesis with Frame-wise Control](https://arxiv.org/abs/2603.20307v1)**  
  Authors: Yuzhe Weng, Haotian Wang, Yuanhong Yu, Jun Du, Shan He, Xiaoyan Wu, Haoran Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20307v1.pdf)  
  Keywords: autoregressive, dit, efficient, audio-driven, video generation, talking head, identity, denoising, interactive, style, streaming  
- **[Improving Joint Audio-Video Generation with Cross-Modal Context Learning](https://arxiv.org/abs/2603.18600v1)**  
  Authors: Bingqi Ma, Linlong Lang, Ming Zhang, Dailan He, Xingtong Ge, Yi Zhang, Guanglu Song, Yu Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18600v1.pdf)  
  Keywords: video diffusion, dit, video generation, multi-modal, evaluation, architecture, diffusion model  
- **[Insight-V++: Towards Advanced Long-Chain Visual Reasoning with Multimodal Large Language Models](https://arxiv.org/abs/2603.18118v1)**  
  Authors: Yuhao Dong, Zuyan Liu, Shulin Tian, Yongming Rao, Ziwei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18118v1.pdf)  
  Keywords: architecture, benchmark, dit, multi-modal  
- **[TAPESTRY: From Geometry to Appearance via Consistent Turntable Videos](https://arxiv.org/abs/2603.17735v1)**  
  Authors: Yan Zeng, Haoran Jiang, Kaixin Yao, Qixuan Zhang, Longwen Zhang, Lan Xu, Jingyi Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17735v1.pdf)  
  Keywords: video diffusion, dit, video generation, multi-modal, 3d-aware, diffusion model  
- **[Bridging Scene Generation and Planning: Driving with World Model via Unifying Vision and Motion Representation](https://arxiv.org/abs/2603.14948v1)**  
  Authors: Xingtai Gui, Meijie Zhang, Tianyi Yan, Wencheng Han, Jiahao Gong, Feiyang Tan, Cheng-zhong Xu, Jianbing Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14948v1.pdf)  
  Keywords: dit, video generation, multi-modal, world model, benchmark, dynamics, trajectory, autonomous driving  
- **[V-JEPA 2.1: Unlocking Dense Features in Video Self-Supervised Learning](https://arxiv.org/abs/2603.14482v2)**  
  Authors: Lorenzo Mur-Labadia, Matthew Muckley, Amir Bar, Mido Assran, Koustuv Sinha, Mike Rabbat, Yann LeCun, Nicolas Ballas, Adrien Bardes  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14482v2.pdf)  
  Keywords: world model, benchmark, multi-modal  
- **[Fuel Gauge: Estimating Chain-of-Thought Length Ahead of Time in Large Multimodal Models](https://arxiv.org/abs/2603.10335v1)**  
  Authors: Yuedong Yang, Xiwen Wei, Mustafa Munir, Radu Marculescu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.10335v1.pdf)  
  Keywords: benchmark, efficient, multi-modal  

### Controllable Generation

*Showing the latest 50 out of 123 papers*

- **[Wan-R1: Verifiable-Reinforcement Learning for Video Reasoning](https://arxiv.org/abs/2603.27866v1)**  
  Authors: Ming Liu, Yunbei Zhang, Shilong Liu, Liwen Wang, Wensheng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27866v1.pdf)  
  Keywords: video generation, trajectory  
- **[LOME: Learning Human-Object Manipulation with Action-Conditioned Egocentric World Model](https://arxiv.org/abs/2603.27449v1)**  
  Authors: Quankai Gao, Jiawei Yang, Qiangeng Xu, Le Chen, Yue Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27449v1.pdf)  
  Keywords: dit, motion control, action-conditioned, text-to-video, gesture, physical, world model, t2v, physics, temporal consistency  
- **[LightMover: Generative Light Movement with Color and Intensity Controls](https://arxiv.org/abs/2603.27209v1)**  
  Authors: Gengze Zhou, Tianyu Wang, Soo Ye Kim, Zhixin Shu, Xin Yu, Yannick Hold-Geoffroy, Sumit Chaturvedi, Qi Wu, Zhe Lin, Scott Cohen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27209v1.pdf)  
  Keywords: video diffusion, dit, physical, controllable  
- **[LightCtrl: Training-free Controllable Video Relighting](https://arxiv.org/abs/2603.27083v1)**  
  Authors: Yizuo Peng, Xuelin Chen, Kai Zhang, Xiaodong Cun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27083v1.pdf) | [![GitHub](https://img.shields.io/github/stars/GVCLab/LightCtrl?style=social)](https://github.com/GVCLab/LightCtrl)  
  Keywords: video diffusion, dit, controllable, trajectory, temporal consistency, diffusion model  
- **[Think over Trajectories: Leveraging Video Generation to Reconstruct GPS Trajectories from Cellular Signaling](https://arxiv.org/abs/2603.26610v1)**  
  Authors: Ruixing Zhang, Hanzhang Jiang, Leilei Sun, Liangzhe Han, Jibin Wang, Weifeng Lv  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26610v1.pdf)  
  Keywords: video generation, image-to-video, dit, trajectory  
- **[Generation Is Compression: Zero-Shot Video Coding via Stochastic Rectified Flow](https://arxiv.org/abs/2603.26571v1)**  
  Authors: Ziyue Zeng, Xun Su, Haoyuan Liu, Bingyu Lu, Yui Tatsumi, Hiroshi Watanabe  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26571v1.pdf)  
  Keywords: dit, i2v, text-to-video, rectified flow, image-to-video, benchmark, t2v, trajectory  
- **[MemCam: Memory-Augmented Camera Control for Consistent Video Generation](https://arxiv.org/abs/2603.26193v1)**  
  Authors: Xinhang Gao, Junlin Guan, Shuhan Luo, Wenzhuo Li, Guanghuan Tan, Jiacheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26193v1.pdf)  
  Keywords: dit, simulation, video generation, long video, controllable, interactive, camera control  
- **[DiReCT: Disentangled Regularization of Contrastive Trajectories for Physics-Refined Video Generation](https://arxiv.org/abs/2603.25931v1)**  
  Authors: Abolfazl Meyarian, Amin Karimi Monsefi, Rajiv Ramnath, Ser-Nam Lim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25931v1.pdf)  
  Keywords: dit, video generation, physical, dynamics, trajectory, physics, flow matching  
- **[RefAlign: Representation Alignment for Reference-to-Video Generation](https://arxiv.org/abs/2603.25743v1)**  
  Authors: Lei Wang, YuXin Song, Ge Wu, Haocheng Feng, Hang Zhou, Jingdong Wang, Yaxing Wang, jian Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25743v1.pdf)  
  Keywords: dit, video generation, identity, video synthesis, controllable, advertising, benchmark, virtual try-on, diffusion transformer  
- **[TRACE: Object Motion Editing in Videos with First-Frame Trajectory Guidance](https://arxiv.org/abs/2603.25707v1)**  
  Authors: Quynh Phung, Long Mai, Cusuh Ham, Feng Liu, Jia-Bin Huang, Aniruddha Mahapatra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25707v1.pdf)  
  Keywords: dit, video-to-video, controllable, image-to-video, trajectory, video editing  

### Human & Character Animation

- **[FlashSign: Pose-Free Guidance for Efficient Sign Language Video Generation](https://arxiv.org/abs/2603.27915v1)**  
  Authors: Liuzhou Zhang, Zeyu Zhang, Biao Wu, Luyao Tang, Zirui Song, Hongyang He, Renda Han, Guangzhen Yao, Huacan Wang, Ronghao Chen, Xiuying Chen, Guan Huang, Zheng Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27915v1.pdf) | [![GitHub](https://img.shields.io/github/stars/AIGeeksGroup/FlashSign?style=social)](https://github.com/AIGeeksGroup/FlashSign)  
  Keywords: video generation, efficient, gesture  
- **[LOME: Learning Human-Object Manipulation with Action-Conditioned Egocentric World Model](https://arxiv.org/abs/2603.27449v1)**  
  Authors: Quankai Gao, Jiawei Yang, Qiangeng Xu, Le Chen, Yue Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27449v1.pdf)  
  Keywords: dit, motion control, action-conditioned, text-to-video, gesture, physical, world model, t2v, physics, temporal consistency  
- **[RefAlign: Representation Alignment for Reference-to-Video Generation](https://arxiv.org/abs/2603.25743v1)**  
  Authors: Lei Wang, YuXin Song, Ge Wu, Haocheng Feng, Hang Zhou, Jingdong Wang, Yaxing Wang, jian Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25743v1.pdf)  
  Keywords: dit, video generation, identity, video synthesis, controllable, advertising, benchmark, virtual try-on, diffusion transformer  
- **[Anti-I2V: Safeguarding your photos from malicious image-to-video generation](https://arxiv.org/abs/2603.24570v1)**  
  Authors: Duc Vu, Anh Nguyen, Chi Tran, Anh Tran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24570v1.pdf)  
  Keywords: video diffusion, dit, i2v, human animation, video generation, image-to-video, denoising, temporal consistency, architecture, diffusion model, diffusion transformer  
- **[Speed by Simplicity: A Single-Stream Architecture for Fast Audio-Video Generative Foundation Model](https://arxiv.org/abs/2603.21986v1)**  
  Authors: SII-GAIR, Sand. ai, :, Ethan Chern, Hansi Teng, Hanwen Sun, Hao Wang, Hong Pan, Hongyu Jia, Jiadi Su, Jin Li, Junjie Yu, Lijie Liu, Lingzhi Li, Lyumanshan Ye, Min Hu, Qiangang Wang, Quanwei Qi, Steffi Chern, Tao Bu, Taoran Wang, Teren Xu, Tianning Zhang, Tiantian Mi, Weixian Xu, Wenqiang Zhang, Wentai Zhang, Xianping Yi, Xiaojie Cai, Xiaoyang Kang, Yan Ma, Yixiu Liu, Yunbo Zhang, Yunpeng Huang, Yutong Lin, Zewei Tao, Zhaoliang Liu, Zheng Zhang, Zhiyao Cen, Zhixuan Yu, Zhongshu Wang, Zhulin Hu, Zijin Zhou, Zinan Guo, Yue Cao, Pengfei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21986v1.pdf)  
  Keywords: efficient, body motion, super-resolution, evaluation, architecture, distillation  
- **[EARTalking: End-to-end GPT-style Autoregressive Talking Head Synthesis with Frame-wise Control](https://arxiv.org/abs/2603.20307v1)**  
  Authors: Yuzhe Weng, Haotian Wang, Yuanhong Yu, Jun Du, Shan He, Xiaoyan Wu, Haoran Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20307v1.pdf)  
  Keywords: autoregressive, dit, efficient, audio-driven, video generation, talking head, identity, denoising, interactive, style, streaming  
- **[AHOY! Animatable Humans under Occlusion from YouTube Videos with Gaussian Splatting and Video Diffusion Priors](https://arxiv.org/abs/2603.17975v1)**  
  Authors: Aymen Mir, Riza Alp Guler, Xiangjun Tang, Peter Wonka, Gerard Pons-Moll  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17975v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://miraymen.github.io/ahoy)  
  Keywords: video diffusion, identity, avatar, architecture, diffusion model  
- **[SoulX-LiveAct: Towards Hour-Scale Real-Time Human Animation with Neighbor Forcing and ConvKV Memory](https://arxiv.org/abs/2603.11746v2)**  
  Authors: Dingcheng Zhen, Xu Zheng, Ruixin Zhang, Zhiqi Jiang, Yichao Yan, Ming Tao, Shunshun Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.11746v2.pdf)  
  Keywords: autoregressive, dit, efficient, human animation, video generation, video synthesis, diffusion model, streaming  
- **[Controllable Complex Human Motion Video Generation via Text-to-Skeleton Cascades](https://arxiv.org/abs/2603.08028v1)**  
  Authors: Ashkan Taghipour, Morteza Ghahremani, Zinuo Li, Hamid Laga, Farid Boussaid, Mohammed Bennamoun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08028v1.pdf)  
  Keywords: video diffusion, autoregressive, dit, video generation, motion control, controllable, benchmark, human motion, temporal consistency, diffusion model  
- **[ArtHOI: Articulated Human-Object Interaction Synthesis by 4D Reconstruction from Video Priors](https://arxiv.org/abs/2603.04338v1)**  
  Authors: Zihao Huang, Tianqi Liu, Zhaoxi Chen, Shaocong Xu, Saining Zhang, Lixing Xiao, Zhiguo Cao, Wei Li, Hao Zhao, Ziwei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.04338v1.pdf)  
  Keywords: video diffusion, dit, physical, human motion, diffusion model  

### Image-to-Video Generation

- **[Think over Trajectories: Leveraging Video Generation to Reconstruct GPS Trajectories from Cellular Signaling](https://arxiv.org/abs/2603.26610v1)**  
  Authors: Ruixing Zhang, Hanzhang Jiang, Leilei Sun, Liangzhe Han, Jibin Wang, Weifeng Lv  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26610v1.pdf)  
  Keywords: video generation, image-to-video, dit, trajectory  
- **[From Static to Dynamic: Exploring Self-supervised Image-to-Video Representation Transfer Learning](https://arxiv.org/abs/2603.26597v1)**  
  Authors: Yang Liu, Qianqian Xu, Peisong Wen, Siran Dai, Xilin Zhao, Qingming Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26597v1.pdf) | [![GitHub](https://img.shields.io/github/stars/yafeng19/Co-Settle?style=social)](https://github.com/yafeng19/Co-Settle)  
  Keywords: temporal consistency, image-to-video, dit  
- **[Generation Is Compression: Zero-Shot Video Coding via Stochastic Rectified Flow](https://arxiv.org/abs/2603.26571v1)**  
  Authors: Ziyue Zeng, Xun Su, Haoyuan Liu, Bingyu Lu, Yui Tatsumi, Hiroshi Watanabe  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26571v1.pdf)  
  Keywords: dit, i2v, text-to-video, rectified flow, image-to-video, benchmark, t2v, trajectory  
- **[IP-Bench: Benchmark for Image Protection Methods in Image-to-Video Generation Scenarios](https://arxiv.org/abs/2603.26154v1)**  
  Authors: Xiaofeng Li, Leyi Sheng, Zhen Sun, Zongmin Zhang, Jiaheng Wei, Xinlei He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26154v1.pdf)  
  Keywords: i2v, video generation, evaluation, image-to-video, benchmark  
- **[TRACE: Object Motion Editing in Videos with First-Frame Trajectory Guidance](https://arxiv.org/abs/2603.25707v1)**  
  Authors: Quynh Phung, Long Mai, Cusuh Ham, Feng Liu, Jia-Bin Huang, Aniruddha Mahapatra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25707v1.pdf)  
  Keywords: dit, video-to-video, controllable, image-to-video, trajectory, video editing  
- **[Anti-I2V: Safeguarding your photos from malicious image-to-video generation](https://arxiv.org/abs/2603.24570v1)**  
  Authors: Duc Vu, Anh Nguyen, Chi Tran, Anh Tran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24570v1.pdf)  
  Keywords: video diffusion, dit, i2v, human animation, video generation, image-to-video, denoising, temporal consistency, architecture, diffusion model, diffusion transformer  
- **[Leave No Stone Unturned: Uncovering Holistic Audio-Visual Intrinsic Coherence for Deepfake Detection](https://arxiv.org/abs/2603.23960v1)**  
  Authors: Jielun Peng, Yabin Wang, Yaqi Li, Long Kong, Xiaopeng Hong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23960v1.pdf) | [![GitHub](https://img.shields.io/github/stars/tuffy-studio/HAVIC?style=social)](https://github.com/tuffy-studio/HAVIC)  
  Keywords: image-to-video, benchmark, text-to-video, dit  
- **[P-Flow: Prompting Visual Effects Generation](https://arxiv.org/abs/2603.22091v1)**  
  Authors: Rui Zhao, Mike Zheng Shou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22091v1.pdf) | [![GitHub](https://img.shields.io/github/stars/showlab/P-Flow?style=social)](https://github.com/showlab/P-Flow)  
  Keywords: video generation, image-to-video, text-to-video, customization  
- **[TransText: Alpha-as-RGB Representation for Transparent Text Animation](https://arxiv.org/abs/2603.17944v2)**  
  Authors: Fei Zhang, Zijian Zhou, Bohao Tang, Sen He, Hang Li, Zhe Wang, Soubhik Sanyal, Pengfei Liu, Viktar Atliha, Tao Xiang, Frost Xu, Semih Gunel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17944v2.pdf)  
  Keywords: image-to-video  
- **[Learning Transferable Temporal Primitives for Video Reasoning via Synthetic Videos](https://arxiv.org/abs/2603.17693v1)**  
  Authors: Songtao Jiang, Sibo Song, Chenyi Zhou, Yuan Wang, Ruizhe Chen, Tongkun Guan, Ruilin Luo, Yan Zhang, Zhihang Tang, Yuchong Sun, Hang Zhang, Zhibo Yang, Shuai Bai, Junyang Lin, Zuozhu Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17693v1.pdf)  
  Keywords: efficient, video generation, image to video, benchmark, dynamics  

### Long Video Generation

*Showing the latest 50 out of 118 papers*

- **[VistaGEN: Consistent Driving Video Generation with Fine-Grained Control Using Multiview Visual-Language Reasoning](https://arxiv.org/abs/2603.28353v1)**  
  Authors: Li-Heng Chen, Ke Cheng, Yahui Liu, Lei Shi, Shi-Sheng Huang, Hongbo Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.28353v1.pdf)  
  Keywords: video generation, temporal consistency, evaluation, long video  
- **[LOME: Learning Human-Object Manipulation with Action-Conditioned Egocentric World Model](https://arxiv.org/abs/2603.27449v1)**  
  Authors: Quankai Gao, Jiawei Yang, Qiangeng Xu, Le Chen, Yue Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27449v1.pdf)  
  Keywords: dit, motion control, action-conditioned, text-to-video, gesture, physical, world model, t2v, physics, temporal consistency  
- **[LightCtrl: Training-free Controllable Video Relighting](https://arxiv.org/abs/2603.27083v1)**  
  Authors: Yizuo Peng, Xuelin Chen, Kai Zhang, Xiaodong Cun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27083v1.pdf) | [![GitHub](https://img.shields.io/github/stars/GVCLab/LightCtrl?style=social)](https://github.com/GVCLab/LightCtrl)  
  Keywords: video diffusion, dit, controllable, trajectory, temporal consistency, diffusion model  
- **[From Static to Dynamic: Exploring Self-supervised Image-to-Video Representation Transfer Learning](https://arxiv.org/abs/2603.26597v1)**  
  Authors: Yang Liu, Qianqian Xu, Peisong Wen, Siran Dai, Xilin Zhao, Qingming Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26597v1.pdf) | [![GitHub](https://img.shields.io/github/stars/yafeng19/Co-Settle?style=social)](https://github.com/yafeng19/Co-Settle)  
  Keywords: temporal consistency, image-to-video, dit  
- **[MemCam: Memory-Augmented Camera Control for Consistent Video Generation](https://arxiv.org/abs/2603.26193v1)**  
  Authors: Xinhang Gao, Junlin Guan, Shuhan Luo, Wenzhuo Li, Guanghuan Tan, Jiacheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26193v1.pdf)  
  Keywords: dit, simulation, video generation, long video, controllable, interactive, camera control  
- **[ShotStream: Streaming Multi-Shot Video Generation for Interactive Storytelling](https://arxiv.org/abs/2603.25746v1)**  
  Authors: Yawen Luo, Xiaoyu Shi, Junhao Zhuang, Yutian Chen, Quande Liu, Xintao Wang, Pengfei Wan, Tianfan Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25746v1.pdf)  
  Keywords: autoregressive, dit, efficient, video generation, text-to-video, interactive, architecture, streaming, distillation  
- **[PackForcing: Short Video Training Suffices for Long Video Sampling and Long Context Inference](https://arxiv.org/abs/2603.25730v1)**  
  Authors: Xiaofeng Mao, Shaohao Rui, Kaining Ying, Bo Zheng, Chuanhao Li, Mingmin Chi, Kaipeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25730v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ShandaAI/PackForcing?style=social)](https://github.com/ShandaAI/PackForcing)  
  Keywords: video diffusion, autoregressive, efficient, video generation, video synthesis, long video, temporal consistency, diffusion model  
- **[Free-Lunch Long Video Generation via Layer-Adaptive O.O.D Correction](https://arxiv.org/abs/2603.25209v1)**  
  Authors: Jiahao Tian, Chenxi Song, Wei Cheng, Chi Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25209v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Westlake-AGI-Lab/FreeLOC?style=social)](https://github.com/Westlake-AGI-Lab/FreeLOC)  
  Keywords: video diffusion, efficient, video generation, long video, temporal consistency, diffusion model  
- **[DCARL: A Divide-and-Conquer Framework for Autoregressive Long-Trajectory Video Generation](https://arxiv.org/abs/2603.24835v1)**  
  Authors: Junyi Ouyang, Wenbin Teng, Gonglin Chen, Yajie Zhao, Haiwei Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24835v1.pdf)  
  Keywords: video diffusion, autoregressive, video generation, world model, trajectory, diffusion model  
- **[DreamerAD: Efficient Reinforcement Learning via Latent World Model for Autonomous Driving](https://arxiv.org/abs/2603.24587v1)**  
  Authors: Pengxuan Yang, Yupeng Zheng, Deheng Qian, Zebin Xing, Qichao Zhang, Linbo Wang, Yichen Zhang, Shaoyu Guo, Zhongpu Xia, Qiang Chen, Junyu Han, Lingyun Xu, Yifeng Pan, Dongbin Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24587v1.pdf)  
  Keywords: autoregressive, dit, efficient, video generation, physical, world model, autonomous driving  

### Personalization & Customization

*Showing the latest 50 out of 87 papers*

- **[MolmoPoint: Better Pointing for VLMs with Grounding Tokens](https://arxiv.org/abs/2603.28069v1)**  
  Authors: Christopher Clark, Yue Yang, Jae Sung Park, Zixian Ma, Jieyu Zhang, Rohun Tripathi, Mohammadreza Salehi, Sangho Lee, Taira Anderson, Winson Han, Ranjay Krishna  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.28069v1.pdf)  
  Keywords: dit, concept  
- **[TokenDial: Continuous Attribute Control in Text-to-Video via Spatiotemporal Token Offsets](https://arxiv.org/abs/2603.27520v1)**  
  Authors: Zhixuan Liu, Peter Schaldenbrand, Yijun Li, Long Mai, Aniruddha Mahapatra, Cusuh Ham, Jean Oh, Jui-Hsien Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27520v1.pdf)  
  Keywords: dit, video generation, identity, text-to-video, evaluation, dynamics, style  
- **[KV Cache Quantization for Self-Forcing Video Generation: A 33-Method Empirical Study](https://arxiv.org/abs/2603.27469v1)**  
  Authors: Suraj Ranganath, Vaishak Menon, Anish Patnaik  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27469v1.pdf) | [![GitHub](https://img.shields.io/github/stars/suraj-ranganath/kv-quant-longhorizon?style=social)](https://github.com/suraj-ranganath/kv-quant-longhorizon)  
  Keywords: video generation, style, benchmark, evaluation  
- **[RefAlign: Representation Alignment for Reference-to-Video Generation](https://arxiv.org/abs/2603.25743v1)**  
  Authors: Lei Wang, YuXin Song, Ge Wu, Haocheng Feng, Hang Zhou, Jingdong Wang, Yaxing Wang, jian Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25743v1.pdf)  
  Keywords: dit, video generation, identity, video synthesis, controllable, advertising, benchmark, virtual try-on, diffusion transformer  
- **[Beyond the Golden Data: Resolving the Motion-Vision Quality Dilemma via Timestep Selective Training](https://arxiv.org/abs/2603.25527v1)**  
  Authors: Xiangyang Luo, Qingyu Li, Yuming Li, Guanbo Huang, Yongjie Zhu, Wenyu Qin, Meng Wang, Pengfei Wan, Shao-Lun Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25527v1.pdf)  
  Keywords: video diffusion, concept, video generation, dynamics, diffusion model  
- **[AnyID: Ultra-Fidelity Universal Identity-Preserving Video Generation from Any Visual References](https://arxiv.org/abs/2603.25188v1)**  
  Authors: Jiahao Wang, Hualian Sheng, Sijia Cai, Yuxiao Yang, Weizhan Zhang, Caixia Yan, Bing Deng, Jieping Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25188v1.pdf)  
  Keywords: creative, video generation, identity, evaluation, architecture  
- **[RealMaster: Lifting Rendered Scenes into Photorealistic Video](https://arxiv.org/abs/2603.23462v1)**  
  Authors: Dana Cohen-Bar, Ido Sobol, Raphael Bensadoun, Shelly Sheynin, Oran Gafni, Or Patashnik, Daniel Cohen-Or, Amit Zohar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23462v1.pdf)  
  Keywords: video diffusion, dit, video generation, identity, dynamics, video editing, diffusion model  
- **[InterDyad: Interactive Dyadic Speech-to-Video Generation by Querying Intermediate Visual Guidance](https://arxiv.org/abs/2603.23132v1)**  
  Authors: Dongwei Pan, Longwei Guo, Jiazhi Guan, Luying Huang, Yiding Li, Haojie Liu, Haocheng Feng, Wei He, Kaisiyuan Wang, Hang Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23132v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://interdyad.github.io)  
  Keywords: video generation, identity, video synthesis, evaluation, dynamics, interactive  
- **[P-Flow: Prompting Visual Effects Generation](https://arxiv.org/abs/2603.22091v1)**  
  Authors: Rui Zhao, Mike Zheng Shou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22091v1.pdf) | [![GitHub](https://img.shields.io/github/stars/showlab/P-Flow?style=social)](https://github.com/showlab/P-Flow)  
  Keywords: video generation, image-to-video, text-to-video, customization  
- **[PROBE: Diagnosing Residual Concept Capacity in Erased Text-to-Video Diffusion Models](https://arxiv.org/abs/2603.21547v1)**  
  Authors: Yiwei Xie, Zheng Zhang, Ping Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21547v1.pdf) | [![GitHub](https://img.shields.io/github/stars/YiweiXie/PRObingBasedEvaluation?style=social)](https://github.com/YiweiXie/PRObingBasedEvaluation)  
  Keywords: video diffusion, dit, concept, text-to-video, evaluation, t2v, denoising, architecture, diffusion model  

### Physical Understanding

*Showing the latest 50 out of 137 papers*

- **[TokenDial: Continuous Attribute Control in Text-to-Video via Spatiotemporal Token Offsets](https://arxiv.org/abs/2603.27520v1)**  
  Authors: Zhixuan Liu, Peter Schaldenbrand, Yijun Li, Long Mai, Aniruddha Mahapatra, Cusuh Ham, Jean Oh, Jui-Hsien Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27520v1.pdf)  
  Keywords: dit, video generation, identity, text-to-video, evaluation, dynamics, style  
- **[LOME: Learning Human-Object Manipulation with Action-Conditioned Egocentric World Model](https://arxiv.org/abs/2603.27449v1)**  
  Authors: Quankai Gao, Jiawei Yang, Qiangeng Xu, Le Chen, Yue Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27449v1.pdf)  
  Keywords: dit, motion control, action-conditioned, text-to-video, gesture, physical, world model, t2v, physics, temporal consistency  
- **[TrackMAE: Video Representation Learning via Track Mask and Predict](https://arxiv.org/abs/2603.27268v1)**  
  Authors: Renaud Vandeghen, Fida Mohammad Thoker, Marc Van Droogenbroeck, Bernard Ghanem  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27268v1.pdf) | [![GitHub](https://img.shields.io/github/stars/rvandeghen/TrackMAE?style=social)](https://github.com/rvandeghen/TrackMAE)  
  Keywords: dynamics  
- **[LightMover: Generative Light Movement with Color and Intensity Controls](https://arxiv.org/abs/2603.27209v1)**  
  Authors: Gengze Zhou, Tianyu Wang, Soo Ye Kim, Zhixin Shu, Xin Yu, Yannick Hold-Geoffroy, Sumit Chaturvedi, Qi Wu, Zhe Lin, Scott Cohen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27209v1.pdf)  
  Keywords: video diffusion, dit, physical, controllable  
- **[PhysVid: Physics Aware Local Conditioning for Generative Video Models](https://arxiv.org/abs/2603.26285v2)**  
  Authors: Saurabh Pathak, Elahe Arani, Mykola Pechenizkiy, Bahram Zonooz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26285v2.pdf)  
  Keywords: dit, physics-aware, physical, dynamics, physics  
- **[DiReCT: Disentangled Regularization of Contrastive Trajectories for Physics-Refined Video Generation](https://arxiv.org/abs/2603.25931v1)**  
  Authors: Abolfazl Meyarian, Amin Karimi Monsefi, Rajiv Ramnath, Ser-Nam Lim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25931v1.pdf)  
  Keywords: dit, video generation, physical, dynamics, trajectory, physics, flow matching  
- **[ViGoR-Bench: How Far Are Visual Generative Models From Zero-Shot Visual Reasoners?](https://arxiv.org/abs/2603.25823v1)**  
  Authors: Haonan Han, Jiancheng Huang, Xiaopeng Sun, Junyan He, Rui Yang, Jie Hu, Xiaojiang Peng, Lin Ma, Xiaoming Wei, Xiu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25823v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vincenthancoder.github.io/ViGoR-Bench)  
  Keywords: evaluation, benchmark, physical  
- **[Beyond the Golden Data: Resolving the Motion-Vision Quality Dilemma via Timestep Selective Training](https://arxiv.org/abs/2603.25527v1)**  
  Authors: Xiangyang Luo, Qingyu Li, Yuming Li, Guanbo Huang, Yongjie Zhu, Wenyu Qin, Meng Wang, Pengfei Wan, Shao-Lun Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25527v1.pdf)  
  Keywords: video diffusion, concept, video generation, dynamics, diffusion model  
- **[Pixelis: Reasoning in Pixels, from Seeing to Acting](https://arxiv.org/abs/2603.25091v1)**  
  Authors: Yunpeng Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25091v1.pdf)  
  Keywords: benchmark, dit, physical  
- **[DreamerAD: Efficient Reinforcement Learning via Latent World Model for Autonomous Driving](https://arxiv.org/abs/2603.24587v1)**  
  Authors: Pengxuan Yang, Yupeng Zheng, Deheng Qian, Zebin Xing, Qichao Zhang, Linbo Wang, Yichen Zhang, Shaoyu Guo, Zhongpu Xia, Qiang Chen, Junyu Han, Lingyun Xu, Yifeng Pan, Dongbin Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24587v1.pdf)  
  Keywords: autoregressive, dit, efficient, video generation, physical, world model, autonomous driving  

### Surveys & Benchmarks

*Showing the latest 50 out of 203 papers*

- **[VistaGEN: Consistent Driving Video Generation with Fine-Grained Control Using Multiview Visual-Language Reasoning](https://arxiv.org/abs/2603.28353v1)**  
  Authors: Li-Heng Chen, Ke Cheng, Yahui Liu, Lei Shi, Shi-Sheng Huang, Hongbo Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.28353v1.pdf)  
  Keywords: video generation, temporal consistency, evaluation, long video  
- **[LogiStory: A Logic-Aware Framework for Multi-Image Story Visualization](https://arxiv.org/abs/2603.28082v1)**  
  Authors: Chutian Meng, Fan Ma, Chi Zhang, Jiaxu Miao, Yi Yang, Yueting Zhuang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.28082v1.pdf)  
  Keywords: video generation, benchmark, evaluation  
- **[TokenDial: Continuous Attribute Control in Text-to-Video via Spatiotemporal Token Offsets](https://arxiv.org/abs/2603.27520v1)**  
  Authors: Zhixuan Liu, Peter Schaldenbrand, Yijun Li, Long Mai, Aniruddha Mahapatra, Cusuh Ham, Jean Oh, Jui-Hsien Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27520v1.pdf)  
  Keywords: dit, video generation, identity, text-to-video, evaluation, dynamics, style  
- **[KV Cache Quantization for Self-Forcing Video Generation: A 33-Method Empirical Study](https://arxiv.org/abs/2603.27469v1)**  
  Authors: Suraj Ranganath, Vaishak Menon, Anish Patnaik  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27469v1.pdf) | [![GitHub](https://img.shields.io/github/stars/suraj-ranganath/kv-quant-longhorizon?style=social)](https://github.com/suraj-ranganath/kv-quant-longhorizon)  
  Keywords: video generation, style, benchmark, evaluation  
- **[Make Geometry Matter for Spatial Reasoning](https://arxiv.org/abs/2603.26639v1)**  
  Authors: Shihua Zhang, Qiuhong Shen, Shizun Wang, Tianbo Pan, Xinchao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26639v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://suhzhang.github.io/GeoSR)  
  Keywords: benchmark  
- **[VGGRPO: Towards World-Consistent Video Generation with 4D Latent Reward](https://arxiv.org/abs/2603.26599v1)**  
  Authors: Zhaochong An, Orest Kupyn, Théo Uscidda, Andrea Colaco, Karan Ahuja, Serge Belongie, Mar Gonzalez-Franco, Marta Tintore Gazulla  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26599v1.pdf)  
  Keywords: video diffusion, dit, efficient, video generation, benchmark, diffusion model  
- **[Generation Is Compression: Zero-Shot Video Coding via Stochastic Rectified Flow](https://arxiv.org/abs/2603.26571v1)**  
  Authors: Ziyue Zeng, Xun Su, Haoyuan Liu, Bingyu Lu, Yui Tatsumi, Hiroshi Watanabe  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26571v1.pdf)  
  Keywords: dit, i2v, text-to-video, rectified flow, image-to-video, benchmark, t2v, trajectory  
- **[Rocks, Pebbles and Sand: Modality-aware Scheduling for Multimodal Large Language Model Inference](https://arxiv.org/abs/2603.26498v1)**  
  Authors: Konstantinos Papaioannou, Thaleia Dimitra Doudali  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26498v1.pdf)  
  Keywords: evaluation, dit, efficient, interactive  
- **[IP-Bench: Benchmark for Image Protection Methods in Image-to-Video Generation Scenarios](https://arxiv.org/abs/2603.26154v1)**  
  Authors: Xiaofeng Li, Leyi Sheng, Zhen Sun, Zongmin Zhang, Jiaheng Wei, Xinlei He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26154v1.pdf)  
  Keywords: i2v, video generation, evaluation, image-to-video, benchmark  
- **[Face2Parts: Exploring Coarse-to-Fine Inter-Regional Facial Dependencies for Generalized Deepfake Detection](https://arxiv.org/abs/2603.26036v1)**  
  Authors: Kutub Uddin, Nusrat Tasnim, Byung Tae Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26036v1.pdf)  
  Keywords: advertising, benchmark  

### Text-to-Video Generation

*Showing the latest 50 out of 69 papers*

- **[TokenDial: Continuous Attribute Control in Text-to-Video via Spatiotemporal Token Offsets](https://arxiv.org/abs/2603.27520v1)**  
  Authors: Zhixuan Liu, Peter Schaldenbrand, Yijun Li, Long Mai, Aniruddha Mahapatra, Cusuh Ham, Jean Oh, Jui-Hsien Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27520v1.pdf)  
  Keywords: dit, video generation, identity, text-to-video, evaluation, dynamics, style  
- **[LOME: Learning Human-Object Manipulation with Action-Conditioned Egocentric World Model](https://arxiv.org/abs/2603.27449v1)**  
  Authors: Quankai Gao, Jiawei Yang, Qiangeng Xu, Le Chen, Yue Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27449v1.pdf)  
  Keywords: dit, motion control, action-conditioned, text-to-video, gesture, physical, world model, t2v, physics, temporal consistency  
- **[EFlow: Fast Few-Step Video Generator Training from Scratch via Efficient Solution Flow](https://arxiv.org/abs/2603.27086v1)**  
  Authors: Dogyun Park, Yanyu Li, Sergey Tulyakov, Anil Kag  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27086v1.pdf)  
  Keywords: video diffusion, dit, efficient, text-to-video, diffusion transformer  
- **[Generation Is Compression: Zero-Shot Video Coding via Stochastic Rectified Flow](https://arxiv.org/abs/2603.26571v1)**  
  Authors: Ziyue Zeng, Xun Su, Haoyuan Liu, Bingyu Lu, Yui Tatsumi, Hiroshi Watanabe  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26571v1.pdf)  
  Keywords: dit, i2v, text-to-video, rectified flow, image-to-video, benchmark, t2v, trajectory  
- **[THFM: A Unified Video Foundation Model for 4D Human Perception and Beyond](https://arxiv.org/abs/2603.25892v1)**  
  Authors: Letian Wang, Andrei Zanfir, Eduard Gabriel Bazavan, Misha Andriluka, Cristian Sminchisescu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25892v1.pdf)  
  Keywords: video diffusion, text-to-video, benchmark, architecture, diffusion model  
- **[ShotStream: Streaming Multi-Shot Video Generation for Interactive Storytelling](https://arxiv.org/abs/2603.25746v1)**  
  Authors: Yawen Luo, Xiaoyu Shi, Junhao Zhuang, Yutian Chen, Quande Liu, Xintao Wang, Pengfei Wan, Tianfan Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25746v1.pdf)  
  Keywords: autoregressive, dit, efficient, video generation, text-to-video, interactive, architecture, streaming, distillation  
- **[Leave No Stone Unturned: Uncovering Holistic Audio-Visual Intrinsic Coherence for Deepfake Detection](https://arxiv.org/abs/2603.23960v1)**  
  Authors: Jielun Peng, Yabin Wang, Yaqi Li, Long Kong, Xiaopeng Hong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23960v1.pdf) | [![GitHub](https://img.shields.io/github/stars/tuffy-studio/HAVIC?style=social)](https://github.com/tuffy-studio/HAVIC)  
  Keywords: image-to-video, benchmark, text-to-video, dit  
- **[Mamba-VMR: Multimodal Query Augmentation via Generated Videos for Precise Temporal Grounding](https://arxiv.org/abs/2603.22121v1)**  
  Authors: Yunzhuo Sun, Xinyue Liu, Yanyang Li, Nanding Wu, Yifang Xu, Linlin Zong, Xianchao Zhang, Wenxin Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22121v1.pdf)  
  Keywords: dit, efficient, text-to-video, multi-modal, evaluation, benchmark, dynamics, architecture, text-driven video  
- **[P-Flow: Prompting Visual Effects Generation](https://arxiv.org/abs/2603.22091v1)**  
  Authors: Rui Zhao, Mike Zheng Shou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22091v1.pdf) | [![GitHub](https://img.shields.io/github/stars/showlab/P-Flow?style=social)](https://github.com/showlab/P-Flow)  
  Keywords: video generation, image-to-video, text-to-video, customization  
- **[PROBE: Diagnosing Residual Concept Capacity in Erased Text-to-Video Diffusion Models](https://arxiv.org/abs/2603.21547v1)**  
  Authors: Yiwei Xie, Zheng Zhang, Ping Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21547v1.pdf) | [![GitHub](https://img.shields.io/github/stars/YiweiXie/PRObingBasedEvaluation?style=social)](https://github.com/YiweiXie/PRObingBasedEvaluation)  
  Keywords: video diffusion, dit, concept, text-to-video, evaluation, t2v, denoising, architecture, diffusion model  

### Video Editing

- **[TRACE: Object Motion Editing in Videos with First-Frame Trajectory Guidance](https://arxiv.org/abs/2603.25707v1)**  
  Authors: Quynh Phung, Long Mai, Cusuh Ham, Feng Liu, Jia-Bin Huang, Aniruddha Mahapatra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25707v1.pdf)  
  Keywords: dit, video-to-video, controllable, image-to-video, trajectory, video editing  
- **[GaussFusion: Improving 3D Reconstruction in the Wild with A Geometry-Informed Video Generator](https://arxiv.org/abs/2603.25053v2)**  
  Authors: Liyuan Zhu, Manjunath Narayana, Michal Stary, Will Hutchcroft, Gordon Wetzstein, Iro Armeni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25053v2.pdf)  
  Keywords: efficient, video generation, video-to-video, benchmark, interactive  
- **[Accelerating Diffusion-based Video Editing via Heterogeneous Caching: Beyond Full Computing at Sampled Denoising Timestep](https://arxiv.org/abs/2603.24260v1)**  
  Authors: Tianyi Liu, Ye Lu, Linfeng Zhang, Chen Cai, Jianjun Gao, Yi Wang, Kim-Hui Yap, Lap-Pui Chau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24260v1.pdf)  
  Keywords: video diffusion, dit, video-to-video, video editing, denoising, acceleration, diffusion transformer  
- **[RealMaster: Lifting Rendered Scenes into Photorealistic Video](https://arxiv.org/abs/2603.23462v1)**  
  Authors: Dana Cohen-Bar, Ido Sobol, Raphael Bensadoun, Shelly Sheynin, Oran Gafni, Or Patashnik, Daniel Cohen-Or, Amit Zohar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23462v1.pdf)  
  Keywords: video diffusion, dit, video generation, identity, dynamics, video editing, diffusion model  
- **[X-World: Controllable Ego-Centric Multi-Camera World Models for Scalable End-to-End Driving](https://arxiv.org/abs/2603.19979v1)**  
  Authors: Chaoda Zheng, Sean Li, Jinhao Deng, Zhennan Wang, Shijia Chen, Liqiang Xiao, Ziheng Chi, Hongbin Lin, Kangjie Chen, Boyang Wang, Yu Zhang, Xianming Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19979v1.pdf)  
  Keywords: dit, simulation, video style transfer, video generation, action-conditioned, style, multi-view video, controllable, evaluation, world model, dynamics, autonomous driving, latent video, world simulator  
- **[Versatile Editing of Video Content, Actions, and Dynamics without Training](https://arxiv.org/abs/2603.17989v1)**  
  Authors: Vladimir Kulikov, Roni Paiss, Andrey Voynov, Inbar Mosseri, Tali Dekel, Tomer Michaeli  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17989v1.pdf)  
  Keywords: dit, video generation, text-to-video, dynamics, video editing  
- **[Script-to-Slide Grounding: Grounding Script Sentences to Slide Objects for Automatic Instructional Video Generation](https://arxiv.org/abs/2603.16931v1)**  
  Authors: Rena Suzuki, Masato Kikuchi, Tadachika Ozono  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16931v1.pdf)  
  Keywords: video generation, dit, education, video editing  
- **[SAW: Toward a Surgical Action World Model via Controllable and Scalable Video Generation](https://arxiv.org/abs/2603.13024v1)**  
  Authors: Sampath Rapuri, Lalithkumar Seenivasan, Dominik Schneider, Roger Soberanis-Mukul, Yufan He, Hao Ding, Jiru Xu, Chenhao Yu, Chenyan Jing, Pengfei Guo, Daguang Xu, Mathias Unberath  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.13024v1.pdf)  
  Keywords: video diffusion, dit, simulation, video generation, video-to-video, controllable, world model, trajectory, temporal consistency, diffusion model  
- **[When to Lock Attention: Training-Free KV Control in Video Diffusion](https://arxiv.org/abs/2603.09657v1)**  
  Authors: Tianyi Zeng, Jincheng Gao, Tianyi Wang, Zijie Meng, Miao Zhang, Jun Yin, Haoyuan Sun, Junfeng Jiao, Christian Claudel, Junbo Tan, Xueqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09657v1.pdf)  
  Keywords: video diffusion, dit, video editing, denoising, diffusion model  
- **[Place-it-R1: Unlocking Environment-aware Reasoning Potential of MLLM for Video Object Insertion](https://arxiv.org/abs/2603.06140v1)**  
  Authors: Bohai Gu, Taiyi Wu, Dazhao Du, Jian Liu, Shuai Yang, Xiaotong Zhao, Alan Zhao, Song Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06140v1.pdf)  
  Keywords: video diffusion, dit, physical, video editing, diffusion model  

### Video Inpainting & Completion

- **[ChopGrad: Pixel-Wise Losses for Latent Video Diffusion via Truncated Backpropagation](https://arxiv.org/abs/2603.17812v1)**  
  Authors: Dmitriy Rivkin, Parker Ewen, Lili Gao, Julian Ost, Stefanie Walz, Rasika Kangutkar, Mario Bijelic, Felix Heide  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17812v1.pdf)  
  Keywords: video inpainting, video diffusion, dit, efficient, video generation, super-resolution, latent video, diffusion model, video enhancement  
- **[ConfCtrl: Enabling Precise Camera Control in Video Diffusion via Confidence-Aware Interpolation](https://arxiv.org/abs/2603.09819v1)**  
  Authors: Liudi Yang, George Eskandar, Fengyi Shen, Mohammad Altillawi, Yang Bai, Chi Zhang, Ziyuan Liu, Abhinav Valada  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09819v1.pdf)  
  Keywords: video diffusion, dit, camera control, video interpolation, novel view, diffusion model  
- **[Pinterest Canvas: Large-Scale Image Generation at Pinterest](https://arxiv.org/abs/2603.06453v1)**  
  Authors: Yu Wang, Eric Tzeng, Raymond Shiau, Jie Yang, Dmitry Kislyuk, Charles Rosenberg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06453v1.pdf)  
  Keywords: dit, video generation, outpainting, image-to-video, diffusion model  
- **[Learning Physics-Grounded 4D Dynamics with Neural Gaussian Force Fields](https://arxiv.org/abs/2602.00148v2)**  
  Authors: Shiqian Li, Ruihong Shen, Junfeng Ni, Chang Pan, Chi Zhang, Yixin Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.00148v2.pdf)  
  Keywords: simulation, video generation, video prediction, physical, evaluation, world model, dynamics, physics, interactive  

### Video Super-Resolution & Enhancement

*Showing the latest 50 out of 60 papers*

- **[Anti-I2V: Safeguarding your photos from malicious image-to-video generation](https://arxiv.org/abs/2603.24570v1)**  
  Authors: Duc Vu, Anh Nguyen, Chi Tran, Anh Tran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24570v1.pdf)  
  Keywords: video diffusion, dit, i2v, human animation, video generation, image-to-video, denoising, temporal consistency, architecture, diffusion model, diffusion transformer  
- **[ScrollScape: Unlocking 32K Image Generation With Video Diffusion Priors](https://arxiv.org/abs/2603.24270v2)**  
  Authors: Haodong Yu, Yabo Zhang, Donglin Di, Ruyi Zhang, Wangmeng Zuo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24270v2.pdf)  
  Keywords: video diffusion, efficient, video generation, super-resolution, evaluation, temporal consistency, diffusion model  
- **[Accelerating Diffusion-based Video Editing via Heterogeneous Caching: Beyond Full Computing at Sampled Denoising Timestep](https://arxiv.org/abs/2603.24260v1)**  
  Authors: Tianyi Liu, Ye Lu, Linfeng Zhang, Chen Cai, Jianjun Gao, Yi Wang, Kim-Hui Yap, Lap-Pui Chau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24260v1.pdf)  
  Keywords: video diffusion, dit, video-to-video, video editing, denoising, acceleration, diffusion transformer  
- **[TETO: Tracking Events with Teacher Observation for Motion Estimation and Frame Interpolation](https://arxiv.org/abs/2603.23487v1)**  
  Authors: Jini Yang, Eunbeen Hong, Soowon Son, Hyunkoo Lee, Sunghwan Hong, Sunok Kim, Seungryong Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23487v1.pdf)  
  Keywords: video diffusion, dit, diffusion transformer, frame interpolation, distillation  
- **[Speed by Simplicity: A Single-Stream Architecture for Fast Audio-Video Generative Foundation Model](https://arxiv.org/abs/2603.21986v1)**  
  Authors: SII-GAIR, Sand. ai, :, Ethan Chern, Hansi Teng, Hanwen Sun, Hao Wang, Hong Pan, Hongyu Jia, Jiadi Su, Jin Li, Junjie Yu, Lijie Liu, Lingzhi Li, Lyumanshan Ye, Min Hu, Qiangang Wang, Quanwei Qi, Steffi Chern, Tao Bu, Taoran Wang, Teren Xu, Tianning Zhang, Tiantian Mi, Weixian Xu, Wenqiang Zhang, Wentai Zhang, Xianping Yi, Xiaojie Cai, Xiaoyang Kang, Yan Ma, Yixiu Liu, Yunbo Zhang, Yunpeng Huang, Yutong Lin, Zewei Tao, Zhaoliang Liu, Zheng Zhang, Zhiyao Cen, Zhixuan Yu, Zhongshu Wang, Zhulin Hu, Zijin Zhou, Zinan Guo, Yue Cao, Pengfei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21986v1.pdf)  
  Keywords: efficient, body motion, super-resolution, evaluation, architecture, distillation  
- **[Adaptive Video Distillation: Mitigating Oversaturation and Temporal Collapse in Few-Step Generation](https://arxiv.org/abs/2603.21864v1)**  
  Authors: Yuyang You, Yongzhi Li, Jiahui Li, Yadong Mu, Quan Chen, Peng Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21864v1.pdf)  
  Keywords: video diffusion, efficient, video generation, video synthesis, physical, benchmark, diffusion model, frame interpolation, distillation  
- **[PROBE: Diagnosing Residual Concept Capacity in Erased Text-to-Video Diffusion Models](https://arxiv.org/abs/2603.21547v1)**  
  Authors: Yiwei Xie, Zheng Zhang, Ping Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21547v1.pdf) | [![GitHub](https://img.shields.io/github/stars/YiweiXie/PRObingBasedEvaluation?style=social)](https://github.com/YiweiXie/PRObingBasedEvaluation)  
  Keywords: video diffusion, dit, concept, text-to-video, evaluation, t2v, denoising, architecture, diffusion model  
- **[Uni-Classifier: Leveraging Video Diffusion Priors for Universal Guidance Classifier](https://arxiv.org/abs/2603.20382v1)**  
  Authors: Yujie Zhou, Pengyang Ling, Jiazi Bu, Bingjie Gao, Li Niu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20382v1.pdf)  
  Keywords: video diffusion, denoising  
- **[Spectrally-Guided Diffusion Noise Schedules](https://arxiv.org/abs/2603.19222v1)**  
  Authors: Carlos Esteves, Ameesh Makadia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19222v1.pdf)  
  Keywords: video generation, dit, diffusion model, denoising  
- **[EARTalking: End-to-end GPT-style Autoregressive Talking Head Synthesis with Frame-wise Control](https://arxiv.org/abs/2603.20307v1)**  
  Authors: Yuzhe Weng, Haotian Wang, Yuanhong Yu, Jun Du, Shan He, Xiaoyan Wu, Haoran Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20307v1.pdf)  
  Keywords: autoregressive, dit, efficient, audio-driven, video generation, talking head, identity, denoising, interactive, style, streaming  

### World Models & Simulation

*Showing the latest 50 out of 94 papers*

- **[LOME: Learning Human-Object Manipulation with Action-Conditioned Egocentric World Model](https://arxiv.org/abs/2603.27449v1)**  
  Authors: Quankai Gao, Jiawei Yang, Qiangeng Xu, Le Chen, Yue Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27449v1.pdf)  
  Keywords: dit, motion control, action-conditioned, text-to-video, gesture, physical, world model, t2v, physics, temporal consistency  
- **[Rocks, Pebbles and Sand: Modality-aware Scheduling for Multimodal Large Language Model Inference](https://arxiv.org/abs/2603.26498v1)**  
  Authors: Konstantinos Papaioannou, Thaleia Dimitra Doudali  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26498v1.pdf)  
  Keywords: evaluation, dit, efficient, interactive  
- **[MemCam: Memory-Augmented Camera Control for Consistent Video Generation](https://arxiv.org/abs/2603.26193v1)**  
  Authors: Xinhang Gao, Junlin Guan, Shuhan Luo, Wenzhuo Li, Guanghuan Tan, Jiacheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26193v1.pdf)  
  Keywords: dit, simulation, video generation, long video, controllable, interactive, camera control  
- **[ShotStream: Streaming Multi-Shot Video Generation for Interactive Storytelling](https://arxiv.org/abs/2603.25746v1)**  
  Authors: Yawen Luo, Xiaoyu Shi, Junhao Zhuang, Yutian Chen, Quande Liu, Xintao Wang, Pengfei Wan, Tianfan Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25746v1.pdf)  
  Keywords: autoregressive, dit, efficient, video generation, text-to-video, interactive, architecture, streaming, distillation  
- **[GaussFusion: Improving 3D Reconstruction in the Wild with A Geometry-Informed Video Generator](https://arxiv.org/abs/2603.25053v2)**  
  Authors: Liyuan Zhu, Manjunath Narayana, Michal Stary, Will Hutchcroft, Gordon Wetzstein, Iro Armeni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25053v2.pdf)  
  Keywords: efficient, video generation, video-to-video, benchmark, interactive  
- **[DCARL: A Divide-and-Conquer Framework for Autoregressive Long-Trajectory Video Generation](https://arxiv.org/abs/2603.24835v1)**  
  Authors: Junyi Ouyang, Wenbin Teng, Gonglin Chen, Yajie Zhao, Haiwei Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24835v1.pdf)  
  Keywords: video diffusion, autoregressive, video generation, world model, trajectory, diffusion model  
- **[DreamerAD: Efficient Reinforcement Learning via Latent World Model for Autonomous Driving](https://arxiv.org/abs/2603.24587v1)**  
  Authors: Pengxuan Yang, Yupeng Zheng, Deheng Qian, Zebin Xing, Qichao Zhang, Linbo Wang, Yichen Zhang, Shaoyu Guo, Zhongpu Xia, Qiang Chen, Junyu Han, Lingyun Xu, Yifeng Pan, Dongbin Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24587v1.pdf)  
  Keywords: autoregressive, dit, efficient, video generation, physical, world model, autonomous driving  
- **[Toward Physically Consistent Driving Video World Models under Challenging Trajectories](https://arxiv.org/abs/2603.24506v1)**  
  Authors: Jiawei Zhou, Zhenxin Zhu, Lingyi Du, Linye Lyu, Lijun Zhou, Zhanqian Wu, Hongcheng Luo, Zhuotao Tian, Bing Wang, Guang Chen, Hangjun Ye, Haiyang Sun, Yu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24506v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wm-research.github.io/PhyGenesis)  
  Keywords: dit, simulation, video generation, physical, world model, dynamics, autonomous driving, trajectory, physics  
- **[WildWorld: A Large-Scale Dataset for Dynamic World Modeling with Actions and Explicit State toward Generative ARPG](https://arxiv.org/abs/2603.23497v1)**  
  Authors: Zhen Li, Zian Meng, Shuwei Shi, Wenshuo Peng, Yuwei Wu, Bo Zheng, Chuanhao Li, Kaipeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23497v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://shandaai.github.io/wildworld-project)  
  Keywords: dit, video generation, action-conditioned, world model, dynamics  
- **[Foveated Diffusion: Efficient Spatially Adaptive Image and Video Generation](https://arxiv.org/abs/2603.23491v1)**  
  Authors: Brian Chao, Lior Yariv, Howard Xiao, Gordon Wetzstein  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23491v1.pdf)  
  Keywords: creative, efficient, video generation, interactive, diffusion model, streaming, flow matching  



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
