# Awesome Video Diffusions [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Video Diffusion Models and Video Generation. Content is automatically updated daily.

> Last Update: 2026-03-28 02:11:00

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
- [Applications](#applications) (41 papers) - Domain-specific applications of video diffusion models
- [Architecture & Efficiency](#architecture-&-efficiency) (355 papers) - Architectural innovations (DiT, UNet), flow matching, and training/inference efficiency
- [Audio & Multi-modal](#audio-&-multi-modal) (32 papers) - Audio-driven and multi-modal conditioned video generation
- [Controllable Generation](#controllable-generation) (122 papers) - Controllable video generation with motion, camera, pose, or layout guidance
- [Human & Character Animation](#human-&-character-animation) (30 papers) - Human-centric video generation including talking heads, dance, and character animation
- [Image-to-Video Generation](#image-to-video-generation) (38 papers) - Methods for animating still images into videos
- [Long Video Generation](#long-video-generation) (117 papers) - Generating temporally consistent long-form videos beyond short clips
- [Personalization & Customization](#personalization-&-customization) (87 papers) - Personalized video generation with custom subjects, identities, or styles
- [Physical Understanding](#physical-understanding) (138 papers) - Physics-aware video generation and dynamics modeling
- [Surveys & Benchmarks](#surveys-&-benchmarks) (197 papers) - Survey papers, benchmarks, and evaluation metrics for video generation
- [Text-to-Video Generation](#text-to-video-generation) (65 papers) - Foundation models and methods for generating videos from text prompts
- [Video Editing](#video-editing) (35 papers) - Diffusion-based video editing, style transfer, and manipulation
- [Video Inpainting & Completion](#video-inpainting-&-completion) (4 papers) - Video inpainting, completion, outpainting, and temporal prediction
- [Video Super-Resolution & Enhancement](#video-super-resolution-&-enhancement) (63 papers) - Video quality improvement, upscaling, restoration, and frame interpolation
- [World Models & Simulation](#world-models-&-simulation) (99 papers) - Video generation as world simulators and interactive environment generation



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
  Keywords: dit, 3d-aware, novel view, camera control, video generation  
- **[GO-Renderer: Generative Object Rendering with 3D-aware Controllable Video Diffusion Models](https://arxiv.org/abs/2603.23246v1)**  
  Authors: Zekai Gu, Shuoxuan Feng, Yansong Wang, Hanzhuo Huang, Zhongshuo Du, Chengfeng Zhao, Chengwei Ren, Peng Wang, Yuan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23246v1.pdf)  
  Keywords: diffusion model, dit, controllable, 3d-aware, video diffusion, efficient  
- **[Omni-WorldBench: Towards a Comprehensive Interaction-Centric Evaluation for World Models](https://arxiv.org/abs/2603.22212v1)**  
  Authors: Meiqi Wu, Zhixin Cai, Fufangchen Zhao, Xiaokun Feng, Rujing Dang, Bingze Song, Ruitian Tian, Jiashu Zhu, Jiachen Lei, Hao Dou, Jing Tang, Lei Sun, Jiahong Wu, Xiangxiang Chu, Zeming Liu, Kaiqi Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22212v1.pdf)  
  Keywords: dynamics, 4d generation, world model, interactive, evaluation, video generation, benchmark  
- **[X-World: Controllable Ego-Centric Multi-Camera World Models for Scalable End-to-End Driving](https://arxiv.org/abs/2603.19979v1)**  
  Authors: Chaoda Zheng, Sean Li, Jinhao Deng, Zhennan Wang, Shijia Chen, Liqiang Xiao, Ziheng Chi, Hongbin Lin, Kangjie Chen, Boyang Wang, Yu Zhang, Xianming Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19979v1.pdf)  
  Keywords: dynamics, world model, latent video, world simulator, multi-view video, action-conditioned, dit, controllable, evaluation, autonomous driving, style, simulation, video generation, video style transfer  
- **[OrbitNVS: Harnessing Video Diffusion Priors for Novel View Synthesis](https://arxiv.org/abs/2603.19613v1)**  
  Authors: Jinglin Liang, Zijian Zhou, Rui Huang, Shuangping Huang, Yichen Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19613v1.pdf)  
  Keywords: novel view, video diffusion, camera control, video generation, benchmark  
- **[3DreamBooth: High-Fidelity 3D Subject-Driven Video Generation Model](https://arxiv.org/abs/2603.18524v1)**  
  Authors: Hyun-kyu Ko, Jihyeon Park, Younghyun Kim, Dongheok Park, Eunbyung Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18524v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ko-lani.github.io/3DreamBooth)  
  Keywords: subject-driven, multi-view video, dit, customization, 3d-aware, novel view, video generation, identity  
- **[TAPESTRY: From Geometry to Appearance via Consistent Turntable Videos](https://arxiv.org/abs/2603.17735v1)**  
  Authors: Yan Zeng, Haoran Jiang, Kaixin Yao, Qixuan Zhang, Longwen Zhang, Lan Xu, Jingyi Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17735v1.pdf)  
  Keywords: diffusion model, multi-modal, dit, 3d-aware, video diffusion, video generation  
- **[Tri-Prompting: Video Diffusion with Unified Control over Scene, Subject, and Motion](https://arxiv.org/abs/2603.15614v1)**  
  Authors: Zhenghong Zhou, Xiaohang Zhan, Zhiqin Chen, Soo Ye Kim, Nanxuan Zhao, Haitian Zheng, Qing Liu, He Zhang, Zhe Lin, Yuqian Zhou, Jiebo Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15614v1.pdf)  
  Keywords: architecture, diffusion model, dit, controllable, 3d-aware, video diffusion, motion control, customization, identity  
- **[GeoNVS: Geometry Grounded Video Diffusion for Novel View Synthesis](https://arxiv.org/abs/2603.14965v1)**  
  Authors: Minjun Kang, Inkyu Shin, Taeyeop Lee, Myungchul Kim, In So Kweon, Kuk-Jin Yoon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14965v1.pdf)  
  Keywords: diffusion model, dit, novel view, video diffusion, camera control  
- **[MVHOI: Bridge Multi-view Condition to Complex Human-Object Interaction Video Reenactment via 3D Foundation Model](https://arxiv.org/abs/2603.14686v1)**  
  Authors: Jinguang Tong, Jinbo Wu, Kaisiyuan Wang, Zhelun Shen, Xuan Huang, Mochu Xiang, Xuesong Li, Yingying Li, Haocheng Feng, Chen Zhao, Hang Zhou, Wei He, Chuong Nguyen, Jingdong Wang, Hongdong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14686v1.pdf)  
  Keywords: dynamics, dit, controllable, novel view, video generation  

### Applications

- **[RefAlign: Representation Alignment for Reference-to-Video Generation](https://arxiv.org/abs/2603.25743v1)**  
  Authors: Lei Wang, YuXin Song, Ge Wu, Haocheng Feng, Hang Zhou, Jingdong Wang, Yaxing Wang, jian Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25743v1.pdf)  
  Keywords: advertising, video synthesis, virtual try-on, dit, controllable, diffusion transformer, video generation, benchmark, identity  
- **[AnyID: Ultra-Fidelity Universal Identity-Preserving Video Generation from Any Visual References](https://arxiv.org/abs/2603.25188v1)**  
  Authors: Jiahao Wang, Hualian Sheng, Sijia Cai, Yuxiao Yang, Weizhan Zhang, Caixia Yan, Bing Deng, Jieping Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25188v1.pdf)  
  Keywords: architecture, evaluation, creative, video generation, identity  
- **[DreamerAD: Efficient Reinforcement Learning via Latent World Model for Autonomous Driving](https://arxiv.org/abs/2603.24587v1)**  
  Authors: Pengxuan Yang, Yupeng Zheng, Deheng Qian, Zebin Xing, Qichao Zhang, Linbo Wang, Yichen Zhang, Shaoyu Guo, Zhongpu Xia, Qiang Chen, Junyu Han, Lingyun Xu, Yifeng Pan, Dongbin Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24587v1.pdf)  
  Keywords: world model, autoregressive, dit, autonomous driving, physical, video generation, efficient  
- **[Toward Physically Consistent Driving Video World Models under Challenging Trajectories](https://arxiv.org/abs/2603.24506v1)**  
  Authors: Jiawei Zhou, Zhenxin Zhu, Lingyi Du, Linye Lyu, Lijun Zhou, Zhanqian Wu, Hongcheng Luo, Zhuotao Tian, Bing Wang, Guang Chen, Hangjun Ye, Haiyang Sun, Yu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24506v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wm-research.github.io/PhyGenesis)  
  Keywords: dynamics, trajectory, world model, physics, dit, autonomous driving, physical, simulation, video generation  
- **[Foveated Diffusion: Efficient Spatially Adaptive Image and Video Generation](https://arxiv.org/abs/2603.23491v1)**  
  Authors: Brian Chao, Lior Yariv, Howard Xiao, Gordon Wetzstein  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23491v1.pdf)  
  Keywords: flow matching, diffusion model, interactive, streaming, creative, video generation, efficient  
- **[X-World: Controllable Ego-Centric Multi-Camera World Models for Scalable End-to-End Driving](https://arxiv.org/abs/2603.19979v1)**  
  Authors: Chaoda Zheng, Sean Li, Jinhao Deng, Zhennan Wang, Shijia Chen, Liqiang Xiao, Ziheng Chi, Hongbin Lin, Kangjie Chen, Boyang Wang, Yu Zhang, Xianming Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19979v1.pdf)  
  Keywords: dynamics, world model, latent video, world simulator, multi-view video, action-conditioned, dit, controllable, evaluation, autonomous driving, style, simulation, video generation, video style transfer  
- **[Student views in AI Ethics and Social Impact](https://arxiv.org/abs/2603.18827v1)**  
  Authors: Tudor-Dan Mihoc, Manuela-Andreea Petrescu, Emilia-Loredana Pop  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18827v1.pdf)  
  Keywords: education, survey, autonomous driving, concept  
- **[EVA: Aligning Video World Models with Executable Robot Actions via Inverse Dynamics Rewards](https://arxiv.org/abs/2603.17808v2)**  
  Authors: Ruixiang Wang, Qingming Liu, Yueci Deng, Guiliang Liu, Zhen Liu, Kui Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17808v2.pdf)  
  Keywords: dynamics, world model, dit, physical, robotics, video generation, acceleration, benchmark, efficient  
- **[Surg$Σ$: A Spectrum of Large-Scale Multimodal Data and Foundation Models for Surgical Intelligence](https://arxiv.org/abs/2603.16822v1)**  
  Authors: Zhitao Zeng, Mengya Xu, Jian Jiang, Pengfei Guo, Yunqiu Xu, Zhu Zhuo, Chang Han Low, Yufan He, Dong Yang, Chenxi Lin, Yiming Gu, Jiaxin Guo, Yutong Ban, Daguang Xu, Qi Dou, Yueming Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16822v1.pdf)  
  Keywords: medical  
- **[Bridging Scene Generation and Planning: Driving with World Model via Unifying Vision and Motion Representation](https://arxiv.org/abs/2603.14948v1)**  
  Authors: Xingtai Gui, Meijie Zhang, Tianyi Yan, Wencheng Han, Jiahao Gong, Feiyang Tan, Cheng-zhong Xu, Jianbing Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14948v1.pdf)  
  Keywords: dynamics, trajectory, world model, multi-modal, dit, autonomous driving, video generation, benchmark  

### Architecture & Efficiency

*Showing the latest 50 out of 355 papers*

- **[ShotStream: Streaming Multi-Shot Video Generation for Interactive Storytelling](https://arxiv.org/abs/2603.25746v1)**  
  Authors: Yawen Luo, Xiaoyu Shi, Junhao Zhuang, Yutian Chen, Quande Liu, Xintao Wang, Pengfei Wan, Tianfan Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25746v1.pdf)  
  Keywords: architecture, interactive, autoregressive, streaming, dit, text-to-video, video generation, efficient, distillation  
- **[RefAlign: Representation Alignment for Reference-to-Video Generation](https://arxiv.org/abs/2603.25743v1)**  
  Authors: Lei Wang, YuXin Song, Ge Wu, Haocheng Feng, Hang Zhou, Jingdong Wang, Yaxing Wang, jian Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25743v1.pdf)  
  Keywords: advertising, video synthesis, virtual try-on, dit, controllable, diffusion transformer, video generation, benchmark, identity  
- **[PackForcing: Short Video Training Suffices for Long Video Sampling and Long Context Inference](https://arxiv.org/abs/2603.25730v1)**  
  Authors: Xiaofeng Mao, Shaohao Rui, Kaining Ying, Bo Zheng, Chuanhao Li, Mingmin Chi, Kaipeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25730v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ShandaAI/PackForcing?style=social)](https://github.com/ShandaAI/PackForcing)  
  Keywords: diffusion model, video synthesis, long video, temporal consistency, autoregressive, video diffusion, video generation, efficient  
- **[TRACE: Object Motion Editing in Videos with First-Frame Trajectory Guidance](https://arxiv.org/abs/2603.25707v1)**  
  Authors: Quynh Phung, Long Mai, Cusuh Ham, Feng Liu, Jia-Bin Huang, Aniruddha Mahapatra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25707v1.pdf)  
  Keywords: trajectory, image-to-video, video-to-video, dit, controllable, video editing  
- **[EagleNet: Energy-Aware Fine-Grained Relationship Learning Network for Text-Video Retrieval](https://arxiv.org/abs/2603.25267v1)**  
  Authors: Yuhan Chen, Pengwen Dai, Chuan Wang, Dayan Wu, Xiaochun Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25267v1.pdf) | [![GitHub](https://img.shields.io/github/stars/draym28/EagleNet?style=social)](https://github.com/draym28/EagleNet)  
  Keywords: dit  
- **[Free-Lunch Long Video Generation via Layer-Adaptive O.O.D Correction](https://arxiv.org/abs/2603.25209v1)**  
  Authors: Jiahao Tian, Chenxi Song, Wei Cheng, Chi Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25209v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Westlake-AGI-Lab/FreeLOC?style=social)](https://github.com/Westlake-AGI-Lab/FreeLOC)  
  Keywords: diffusion model, long video, temporal consistency, video diffusion, video generation, efficient  
- **[AnyID: Ultra-Fidelity Universal Identity-Preserving Video Generation from Any Visual References](https://arxiv.org/abs/2603.25188v1)**  
  Authors: Jiahao Wang, Hualian Sheng, Sijia Cai, Yuxiao Yang, Weizhan Zhang, Caixia Yan, Bing Deng, Jieping Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25188v1.pdf)  
  Keywords: architecture, evaluation, creative, video generation, identity  
- **[Pixelis: Reasoning in Pixels, from Seeing to Acting](https://arxiv.org/abs/2603.25091v1)**  
  Authors: Yunpeng Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25091v1.pdf)  
  Keywords: dit, benchmark, physical  
- **[GaussFusion: Improving 3D Reconstruction in the Wild with A Geometry-Informed Video Generator](https://arxiv.org/abs/2603.25053v1)**  
  Authors: Liyuan Zhu, Manjunath Narayana, Michal Stary, Will Hutchcroft, Gordon Wetzstein, Iro Armeni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25053v1.pdf)  
  Keywords: video-to-video, interactive, video generation, benchmark, efficient  
- **[MoE-GRPO: Optimizing Mixture-of-Experts via Reinforcement Learning in Vision-Language Models](https://arxiv.org/abs/2603.24984v1)**  
  Authors: Dohwan Ko, Jinyoung Park, Seoung Choi, Sanghyeok Lee, Seohyun Lee, Hyunwoo J. Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24984v1.pdf)  
  Keywords: multi-modal, benchmark, architecture  

### Audio & Multi-modal

- **[MoE-GRPO: Optimizing Mixture-of-Experts via Reinforcement Learning in Vision-Language Models](https://arxiv.org/abs/2603.24984v1)**  
  Authors: Dohwan Ko, Jinyoung Park, Seoung Choi, Sanghyeok Lee, Seohyun Lee, Hyunwoo J. Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24984v1.pdf)  
  Keywords: multi-modal, benchmark, architecture  
- **[Attention-aware Inference Optimizations for Large Vision-Language Models with Memory-efficient Decoding](https://arxiv.org/abs/2603.23914v1)**  
  Authors: Fatih Ilhan, Gaowen Liu, Ramana Rao Kompella, Selim Furkan Tekin, Tiansheng Huang, Zachary Yahn, Yichang Xu, Ling Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23914v1.pdf)  
  Keywords: multi-modal, benchmark, efficient  
- **[Mamba-VMR: Multimodal Query Augmentation via Generated Videos for Precise Temporal Grounding](https://arxiv.org/abs/2603.22121v1)**  
  Authors: Yunzhuo Sun, Xinyue Liu, Yanyang Li, Nanding Wu, Yifang Xu, Linlin Zong, Xianchao Zhang, Wenxin Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22121v1.pdf)  
  Keywords: architecture, text-driven video, dynamics, multi-modal, dit, text-to-video, evaluation, benchmark, efficient  
- **[EARTalking: End-to-end GPT-style Autoregressive Talking Head Synthesis with Frame-wise Control](https://arxiv.org/abs/2603.20307v1)**  
  Authors: Yuzhe Weng, Haotian Wang, Yuanhong Yu, Jun Du, Shan He, Xiaoyan Wu, Haoran Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20307v1.pdf)  
  Keywords: denoising, talking head, interactive, autoregressive, streaming, dit, style, audio-driven, video generation, identity, efficient  
- **[Improving Joint Audio-Video Generation with Cross-Modal Context Learning](https://arxiv.org/abs/2603.18600v1)**  
  Authors: Bingqi Ma, Linlong Lang, Ming Zhang, Dailan He, Xingtong Ge, Yi Zhang, Guanglu Song, Yu Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18600v1.pdf)  
  Keywords: architecture, diffusion model, multi-modal, dit, evaluation, video diffusion, video generation  
- **[Insight-V++: Towards Advanced Long-Chain Visual Reasoning with Multimodal Large Language Models](https://arxiv.org/abs/2603.18118v1)**  
  Authors: Yuhao Dong, Zuyan Liu, Shulin Tian, Yongming Rao, Ziwei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18118v1.pdf)  
  Keywords: dit, multi-modal, benchmark, architecture  
- **[TAPESTRY: From Geometry to Appearance via Consistent Turntable Videos](https://arxiv.org/abs/2603.17735v1)**  
  Authors: Yan Zeng, Haoran Jiang, Kaixin Yao, Qixuan Zhang, Longwen Zhang, Lan Xu, Jingyi Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17735v1.pdf)  
  Keywords: diffusion model, multi-modal, dit, 3d-aware, video diffusion, video generation  
- **[Bridging Scene Generation and Planning: Driving with World Model via Unifying Vision and Motion Representation](https://arxiv.org/abs/2603.14948v1)**  
  Authors: Xingtai Gui, Meijie Zhang, Tianyi Yan, Wencheng Han, Jiahao Gong, Feiyang Tan, Cheng-zhong Xu, Jianbing Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14948v1.pdf)  
  Keywords: dynamics, trajectory, world model, multi-modal, dit, autonomous driving, video generation, benchmark  
- **[V-JEPA 2.1: Unlocking Dense Features in Video Self-Supervised Learning](https://arxiv.org/abs/2603.14482v2)**  
  Authors: Lorenzo Mur-Labadia, Matthew Muckley, Amir Bar, Mido Assran, Koustuv Sinha, Mike Rabbat, Yann LeCun, Nicolas Ballas, Adrien Bardes  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14482v2.pdf)  
  Keywords: multi-modal, benchmark, world model  
- **[Fuel Gauge: Estimating Chain-of-Thought Length Ahead of Time in Large Multimodal Models](https://arxiv.org/abs/2603.10335v1)**  
  Authors: Yuedong Yang, Xiwen Wei, Mustafa Munir, Radu Marculescu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.10335v1.pdf)  
  Keywords: multi-modal, benchmark, efficient  

### Controllable Generation

*Showing the latest 50 out of 122 papers*

- **[RefAlign: Representation Alignment for Reference-to-Video Generation](https://arxiv.org/abs/2603.25743v1)**  
  Authors: Lei Wang, YuXin Song, Ge Wu, Haocheng Feng, Hang Zhou, Jingdong Wang, Yaxing Wang, jian Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25743v1.pdf)  
  Keywords: advertising, video synthesis, virtual try-on, dit, controllable, diffusion transformer, video generation, benchmark, identity  
- **[TRACE: Object Motion Editing in Videos with First-Frame Trajectory Guidance](https://arxiv.org/abs/2603.25707v1)**  
  Authors: Quynh Phung, Long Mai, Cusuh Ham, Feng Liu, Jia-Bin Huang, Aniruddha Mahapatra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25707v1.pdf)  
  Keywords: trajectory, image-to-video, video-to-video, dit, controllable, video editing  
- **[DCARL: A Divide-and-Conquer Framework for Autoregressive Long-Trajectory Video Generation](https://arxiv.org/abs/2603.24835v1)**  
  Authors: Junyi Ouyang, Wenbin Teng, Gonglin Chen, Yajie Zhao, Haiwei Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24835v1.pdf)  
  Keywords: trajectory, world model, diffusion model, autoregressive, video diffusion, video generation  
- **[Toward Physically Consistent Driving Video World Models under Challenging Trajectories](https://arxiv.org/abs/2603.24506v1)**  
  Authors: Jiawei Zhou, Zhenxin Zhu, Lingyi Du, Linye Lyu, Lijun Zhou, Zhanqian Wu, Hongcheng Luo, Zhuotao Tian, Bing Wang, Guang Chen, Hangjun Ye, Haiyang Sun, Yu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24506v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wm-research.github.io/PhyGenesis)  
  Keywords: dynamics, trajectory, world model, physics, dit, autonomous driving, physical, simulation, video generation  
- **[I3DM: Implicit 3D-aware Memory Retrieval and Injection for Consistent Video Scene Generation](https://arxiv.org/abs/2603.23413v1)**  
  Authors: Jia Li, Han Yan, Yihang Chen, Siqi Li, Xibin Song, Yifu Wang, Jianfei Cai, Tien-Tsin Wong, Pan Ji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23413v1.pdf)  
  Keywords: dit, 3d-aware, novel view, camera control, video generation  
- **[ABot-PhysWorld: Interactive World Foundation Model for Robotic Manipulation with Physics Alignment](https://arxiv.org/abs/2603.23376v1)**  
  Authors: Yuzhi Chen, Ronghan Chen, Dongjie Huo, Yandan Yang, Dekang Qi, Haoyun Liu, Tong Lin, Shuang Zeng, Junjin Xiao, Xinyuan Chang, Feng Xiong, Xing Wei, Zhiheng Ma, Mu Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23376v1.pdf)  
  Keywords: trajectory, world model, physics-aware, interactive, physics, controllable, evaluation, physical, diffusion transformer, simulation, video generation, benchmark  
- **[GO-Renderer: Generative Object Rendering with 3D-aware Controllable Video Diffusion Models](https://arxiv.org/abs/2603.23246v1)**  
  Authors: Zekai Gu, Shuoxuan Feng, Yansong Wang, Hanzhuo Huang, Zhongshuo Du, Chengfeng Zhao, Chengwei Ren, Peng Wang, Yuan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23246v1.pdf)  
  Keywords: diffusion model, dit, controllable, 3d-aware, video diffusion, efficient  
- **[WorldMesh: Generating Navigable Multi-Room 3D Scenes via Mesh-Conditioned Image Diffusion](https://arxiv.org/abs/2603.22972v2)**  
  Authors: Manuel-Andreas Schneider, Angela Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22972v2.pdf)  
  Keywords: dit, video synthesis, layout  
- **[TrajLoom: Dense Future Trajectory Generation from Video](https://arxiv.org/abs/2603.22606v1)**  
  Authors: Zewei Zhang, Jia Jun Cheng Xian, Kaiwen Liu, Ming Liang, Hang Chu, Jun Chen, Renjie Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22606v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://trajloom.github.io)  
  Keywords: flow matching, trajectory, temporal consistency, dit, controllable, video generation, benchmark  
- **[PAM: A Pose-Appearance-Motion Engine for Sim-to-Real HOI Video Generation](https://arxiv.org/abs/2603.22193v2)**  
  Authors: Mingju Gao, Kaisen Yang, Huan-ang Gao, Bohan Li, Ao Ding, Wenyi Li, Yangcheng Yu, Jinkun Liu, Shaocong Xu, Yike Niu, Haohan Chi, Hao Chen, Hao Tang, Yu Zhang, Li Yi, Hao Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22193v2.pdf)  
  Keywords: dit, video generation, controllable, dynamics  

### Human & Character Animation

- **[RefAlign: Representation Alignment for Reference-to-Video Generation](https://arxiv.org/abs/2603.25743v1)**  
  Authors: Lei Wang, YuXin Song, Ge Wu, Haocheng Feng, Hang Zhou, Jingdong Wang, Yaxing Wang, jian Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25743v1.pdf)  
  Keywords: advertising, video synthesis, virtual try-on, dit, controllable, diffusion transformer, video generation, benchmark, identity  
- **[Anti-I2V: Safeguarding your photos from malicious image-to-video generation](https://arxiv.org/abs/2603.24570v1)**  
  Authors: Duc Vu, Anh Nguyen, Chi Tran, Anh Tran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24570v1.pdf)  
  Keywords: denoising, architecture, image-to-video, diffusion model, temporal consistency, dit, human animation, video diffusion, i2v, diffusion transformer, video generation  
- **[Speed by Simplicity: A Single-Stream Architecture for Fast Audio-Video Generative Foundation Model](https://arxiv.org/abs/2603.21986v1)**  
  Authors: SII-GAIR, Sand. ai, :, Ethan Chern, Hansi Teng, Hanwen Sun, Hao Wang, Hong Pan, Hongyu Jia, Jiadi Su, Jin Li, Junjie Yu, Lijie Liu, Lingzhi Li, Lyumanshan Ye, Min Hu, Qiangang Wang, Quanwei Qi, Steffi Chern, Tao Bu, Taoran Wang, Teren Xu, Tianning Zhang, Tiantian Mi, Weixian Xu, Wenqiang Zhang, Wentai Zhang, Xianping Yi, Xiaojie Cai, Xiaoyang Kang, Yan Ma, Yixiu Liu, Yunbo Zhang, Yunpeng Huang, Yutong Lin, Zewei Tao, Zhaoliang Liu, Zheng Zhang, Zhiyao Cen, Zhixuan Yu, Zhongshu Wang, Zhulin Hu, Zijin Zhou, Zinan Guo, Yue Cao, Pengfei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21986v1.pdf)  
  Keywords: architecture, super-resolution, evaluation, body motion, efficient, distillation  
- **[EARTalking: End-to-end GPT-style Autoregressive Talking Head Synthesis with Frame-wise Control](https://arxiv.org/abs/2603.20307v1)**  
  Authors: Yuzhe Weng, Haotian Wang, Yuanhong Yu, Jun Du, Shan He, Xiaoyan Wu, Haoran Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20307v1.pdf)  
  Keywords: denoising, talking head, interactive, autoregressive, streaming, dit, style, audio-driven, video generation, identity, efficient  
- **[AHOY! Animatable Humans under Occlusion from YouTube Videos with Gaussian Splatting and Video Diffusion Priors](https://arxiv.org/abs/2603.17975v1)**  
  Authors: Aymen Mir, Riza Alp Guler, Xiangjun Tang, Peter Wonka, Gerard Pons-Moll  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17975v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://miraymen.github.io/ahoy)  
  Keywords: architecture, diffusion model, video diffusion, identity, avatar  
- **[SoulX-LiveAct: Towards Hour-Scale Real-Time Human Animation with Neighbor Forcing and ConvKV Memory](https://arxiv.org/abs/2603.11746v2)**  
  Authors: Dingcheng Zhen, Xu Zheng, Ruixin Zhang, Zhiqi Jiang, Yichao Yan, Ming Tao, Shunshun Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.11746v2.pdf)  
  Keywords: diffusion model, video synthesis, autoregressive, streaming, human animation, dit, video generation, efficient  
- **[Controllable Complex Human Motion Video Generation via Text-to-Skeleton Cascades](https://arxiv.org/abs/2603.08028v1)**  
  Authors: Ashkan Taghipour, Morteza Ghahremani, Zinuo Li, Hamid Laga, Farid Boussaid, Mohammed Bennamoun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08028v1.pdf)  
  Keywords: diffusion model, temporal consistency, autoregressive, dit, controllable, video diffusion, motion control, video generation, benchmark, human motion  
- **[ArtHOI: Articulated Human-Object Interaction Synthesis by 4D Reconstruction from Video Priors](https://arxiv.org/abs/2603.04338v1)**  
  Authors: Zihao Huang, Tianqi Liu, Zhaoxi Chen, Shaocong Xu, Saining Zhang, Lixing Xiao, Zhiguo Cao, Wei Li, Hao Zhao, Ziwei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.04338v1.pdf)  
  Keywords: diffusion model, dit, video diffusion, physical, human motion  
- **[Direct Reward Fine-Tuning on Poses for Single Image to 3D Human in the Wild](https://arxiv.org/abs/2603.02619v1)**  
  Authors: Seunguk Do, Minwoo Huh, Joonghyuk Shin, Jaesik Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02619v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://seunguk-do.github.io/drpose)  
  Keywords: diffusion model, dit, evaluation, benchmark, human motion  
- **[LiftAvatar: Kinematic-Space Completion for Expression-Controlled 3D Gaussian Avatar Animation](https://arxiv.org/abs/2603.02129v1)**  
  Authors: Hualiang Wei, Shunran Jia, Jialun Liu, Wenhui Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.02129v1.pdf)  
  Keywords: dit, controllable, video diffusion, diffusion transformer, avatar, efficient, distillation  

### Image-to-Video Generation

- **[TRACE: Object Motion Editing in Videos with First-Frame Trajectory Guidance](https://arxiv.org/abs/2603.25707v1)**  
  Authors: Quynh Phung, Long Mai, Cusuh Ham, Feng Liu, Jia-Bin Huang, Aniruddha Mahapatra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25707v1.pdf)  
  Keywords: trajectory, image-to-video, video-to-video, dit, controllable, video editing  
- **[Anti-I2V: Safeguarding your photos from malicious image-to-video generation](https://arxiv.org/abs/2603.24570v1)**  
  Authors: Duc Vu, Anh Nguyen, Chi Tran, Anh Tran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24570v1.pdf)  
  Keywords: denoising, architecture, image-to-video, diffusion model, temporal consistency, dit, human animation, video diffusion, i2v, diffusion transformer, video generation  
- **[Leave No Stone Unturned: Uncovering Holistic Audio-Visual Intrinsic Coherence for Deepfake Detection](https://arxiv.org/abs/2603.23960v1)**  
  Authors: Jielun Peng, Yabin Wang, Yaqi Li, Long Kong, Xiaopeng Hong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23960v1.pdf) | [![GitHub](https://img.shields.io/github/stars/tuffy-studio/HAVIC?style=social)](https://github.com/tuffy-studio/HAVIC)  
  Keywords: dit, text-to-video, benchmark, image-to-video  
- **[P-Flow: Prompting Visual Effects Generation](https://arxiv.org/abs/2603.22091v1)**  
  Authors: Rui Zhao, Mike Zheng Shou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22091v1.pdf) | [![GitHub](https://img.shields.io/github/stars/showlab/P-Flow?style=social)](https://github.com/showlab/P-Flow)  
  Keywords: video generation, text-to-video, customization, image-to-video  
- **[TransText: Alpha-as-RGB Representation for Transparent Text Animation](https://arxiv.org/abs/2603.17944v2)**  
  Authors: Fei Zhang, Zijian Zhou, Bohao Tang, Sen He, Hang Li, Zhe Wang, Soubhik Sanyal, Pengfei Liu, Viktar Atliha, Tao Xiang, Frost Xu, Semih Gunel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17944v2.pdf)  
  Keywords: image-to-video  
- **[Learning Transferable Temporal Primitives for Video Reasoning via Synthetic Videos](https://arxiv.org/abs/2603.17693v1)**  
  Authors: Songtao Jiang, Sibo Song, Chenyi Zhou, Yuan Wang, Ruizhe Chen, Tongkun Guan, Ruilin Luo, Yan Zhang, Zhihang Tang, Yuchong Sun, Hang Zhang, Zhibo Yang, Shuai Bai, Junyang Lin, Zuozhu Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17693v1.pdf)  
  Keywords: dynamics, image to video, video generation, benchmark, efficient  
- **[FrescoDiffusion: 4K Image-to-Video with Prior-Regularized Tiled Diffusion](https://arxiv.org/abs/2603.17555v1)**  
  Authors: Hugo Caselles-Dupré, Mathis Koroglu, Guillaume Jeanneret, Arnaud Dapogny, Matthieu Cord  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17555v1.pdf)  
  Keywords: denoising, trajectory, image-to-video, layout, dit, i2v, efficient  
- **[Search2Motion: Training-Free Object-Level Motion Control via Attention-Consensus Search](https://arxiv.org/abs/2603.16711v2)**  
  Authors: Sainan Liu, Tz-Ying Wu, Hector A Valdez, Subarna Tripathi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16711v2.pdf)  
  Keywords: dynamics, image-to-video, dit, evaluation, motion control, video generation, benchmark  
- **[GenState-AI: State-Aware Dataset for Text-to-Video Retrieval on AI-Generated Videos](https://arxiv.org/abs/2603.14426v1)**  
  Authors: Minghan Li, Tongna Chen, Tianrui Lv, Yishuai Zhang, Suchao An, Guodong Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14426v1.pdf)  
  Keywords: dit, controllable, text-to-video, evaluation, i2v, benchmark  
- **[PhysAlign: Physics-Coherent Image-to-Video Generation through Feature and 3D Representation Alignment](https://arxiv.org/abs/2603.13770v1)**  
  Authors: Zhexiao Xiong, Yizhi Song, Liu He, Wei Xiong, Yu Yuan, Feng Qiao, Nathan Jacobs  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.13770v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://physalign.github.io/PhysAlign)  
  Keywords: image-to-video, diffusion model, physics, controllable, i2v, video diffusion, simulation, physical, robotics, video generation, efficient  

### Long Video Generation

*Showing the latest 50 out of 117 papers*

- **[ShotStream: Streaming Multi-Shot Video Generation for Interactive Storytelling](https://arxiv.org/abs/2603.25746v1)**  
  Authors: Yawen Luo, Xiaoyu Shi, Junhao Zhuang, Yutian Chen, Quande Liu, Xintao Wang, Pengfei Wan, Tianfan Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25746v1.pdf)  
  Keywords: architecture, interactive, autoregressive, streaming, dit, text-to-video, video generation, efficient, distillation  
- **[PackForcing: Short Video Training Suffices for Long Video Sampling and Long Context Inference](https://arxiv.org/abs/2603.25730v1)**  
  Authors: Xiaofeng Mao, Shaohao Rui, Kaining Ying, Bo Zheng, Chuanhao Li, Mingmin Chi, Kaipeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25730v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ShandaAI/PackForcing?style=social)](https://github.com/ShandaAI/PackForcing)  
  Keywords: diffusion model, video synthesis, long video, temporal consistency, autoregressive, video diffusion, video generation, efficient  
- **[Free-Lunch Long Video Generation via Layer-Adaptive O.O.D Correction](https://arxiv.org/abs/2603.25209v1)**  
  Authors: Jiahao Tian, Chenxi Song, Wei Cheng, Chi Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25209v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Westlake-AGI-Lab/FreeLOC?style=social)](https://github.com/Westlake-AGI-Lab/FreeLOC)  
  Keywords: diffusion model, long video, temporal consistency, video diffusion, video generation, efficient  
- **[DCARL: A Divide-and-Conquer Framework for Autoregressive Long-Trajectory Video Generation](https://arxiv.org/abs/2603.24835v1)**  
  Authors: Junyi Ouyang, Wenbin Teng, Gonglin Chen, Yajie Zhao, Haiwei Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24835v1.pdf)  
  Keywords: trajectory, world model, diffusion model, autoregressive, video diffusion, video generation  
- **[DreamerAD: Efficient Reinforcement Learning via Latent World Model for Autonomous Driving](https://arxiv.org/abs/2603.24587v1)**  
  Authors: Pengxuan Yang, Yupeng Zheng, Deheng Qian, Zebin Xing, Qichao Zhang, Linbo Wang, Yichen Zhang, Shaoyu Guo, Zhongpu Xia, Qiang Chen, Junyu Han, Lingyun Xu, Yifeng Pan, Dongbin Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24587v1.pdf)  
  Keywords: world model, autoregressive, dit, autonomous driving, physical, video generation, efficient  
- **[Anti-I2V: Safeguarding your photos from malicious image-to-video generation](https://arxiv.org/abs/2603.24570v1)**  
  Authors: Duc Vu, Anh Nguyen, Chi Tran, Anh Tran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24570v1.pdf)  
  Keywords: denoising, architecture, image-to-video, diffusion model, temporal consistency, dit, human animation, video diffusion, i2v, diffusion transformer, video generation  
- **[ScrollScape: Unlocking 32K Image Generation With Video Diffusion Priors](https://arxiv.org/abs/2603.24270v2)**  
  Authors: Haodong Yu, Yabo Zhang, Donglin Di, Ruyi Zhang, Wangmeng Zuo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24270v2.pdf)  
  Keywords: diffusion model, temporal consistency, super-resolution, evaluation, video diffusion, video generation, efficient  
- **[Foveated Diffusion: Efficient Spatially Adaptive Image and Video Generation](https://arxiv.org/abs/2603.23491v1)**  
  Authors: Brian Chao, Lior Yariv, Howard Xiao, Gordon Wetzstein  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23491v1.pdf)  
  Keywords: flow matching, diffusion model, interactive, streaming, creative, video generation, efficient  
- **[TrajLoom: Dense Future Trajectory Generation from Video](https://arxiv.org/abs/2603.22606v1)**  
  Authors: Zewei Zhang, Jia Jun Cheng Xian, Kaiwen Liu, Ming Liang, Hang Chu, Jun Chen, Renjie Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22606v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://trajloom.github.io)  
  Keywords: flow matching, trajectory, temporal consistency, dit, controllable, video generation, benchmark  
- **[Relax Forcing: Relaxed KV-Memory for Consistent Long Video Generation](https://arxiv.org/abs/2603.21366v1)**  
  Authors: Zengqun Zhao, Yanzuo Lu, Ziquan Liu, Jifei Song, Jiankang Deng, Ioannis Patras  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21366v1.pdf)  
  Keywords: dynamics, long video, temporal consistency, autoregressive, dit, video diffusion, video generation  

### Personalization & Customization

*Showing the latest 50 out of 87 papers*

- **[RefAlign: Representation Alignment for Reference-to-Video Generation](https://arxiv.org/abs/2603.25743v1)**  
  Authors: Lei Wang, YuXin Song, Ge Wu, Haocheng Feng, Hang Zhou, Jingdong Wang, Yaxing Wang, jian Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25743v1.pdf)  
  Keywords: advertising, video synthesis, virtual try-on, dit, controllable, diffusion transformer, video generation, benchmark, identity  
- **[Beyond the Golden Data: Resolving the Motion-Vision Quality Dilemma via Timestep Selective Training](https://arxiv.org/abs/2603.25527v1)**  
  Authors: Xiangyang Luo, Qingyu Li, Yuming Li, Guanbo Huang, Yongjie Zhu, Wenyu Qin, Meng Wang, Pengfei Wan, Shao-Lun Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25527v1.pdf)  
  Keywords: dynamics, diffusion model, concept, video diffusion, video generation  
- **[AnyID: Ultra-Fidelity Universal Identity-Preserving Video Generation from Any Visual References](https://arxiv.org/abs/2603.25188v1)**  
  Authors: Jiahao Wang, Hualian Sheng, Sijia Cai, Yuxiao Yang, Weizhan Zhang, Caixia Yan, Bing Deng, Jieping Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25188v1.pdf)  
  Keywords: architecture, evaluation, creative, video generation, identity  
- **[RealMaster: Lifting Rendered Scenes into Photorealistic Video](https://arxiv.org/abs/2603.23462v1)**  
  Authors: Dana Cohen-Bar, Ido Sobol, Raphael Bensadoun, Shelly Sheynin, Oran Gafni, Or Patashnik, Daniel Cohen-Or, Amit Zohar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23462v1.pdf)  
  Keywords: dynamics, diffusion model, dit, video diffusion, video editing, video generation, identity  
- **[InterDyad: Interactive Dyadic Speech-to-Video Generation by Querying Intermediate Visual Guidance](https://arxiv.org/abs/2603.23132v1)**  
  Authors: Dongwei Pan, Longwei Guo, Jiazhi Guan, Luying Huang, Yiding Li, Haojie Liu, Haocheng Feng, Wei He, Kaisiyuan Wang, Hang Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23132v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://interdyad.github.io)  
  Keywords: dynamics, video synthesis, interactive, evaluation, video generation, identity  
- **[P-Flow: Prompting Visual Effects Generation](https://arxiv.org/abs/2603.22091v1)**  
  Authors: Rui Zhao, Mike Zheng Shou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22091v1.pdf) | [![GitHub](https://img.shields.io/github/stars/showlab/P-Flow?style=social)](https://github.com/showlab/P-Flow)  
  Keywords: video generation, text-to-video, customization, image-to-video  
- **[PROBE: Diagnosing Residual Concept Capacity in Erased Text-to-Video Diffusion Models](https://arxiv.org/abs/2603.21547v1)**  
  Authors: Yiwei Xie, Zheng Zhang, Ping Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21547v1.pdf) | [![GitHub](https://img.shields.io/github/stars/YiweiXie/PRObingBasedEvaluation?style=social)](https://github.com/YiweiXie/PRObingBasedEvaluation)  
  Keywords: denoising, architecture, t2v, diffusion model, concept, dit, text-to-video, evaluation, video diffusion  
- **[Identity-Consistent Video Generation under Large Facial-Angle Variations](https://arxiv.org/abs/2603.21299v1)**  
  Authors: Bin Hu, Zipeng Qi, Guoxi Huang, Zunnan Xu, Ruicheng Zhang, Chongjie Ye, Jun Zhou, Xiu Li, Jingdong Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21299v1.pdf)  
  Keywords: dit, video generation, evaluation, identity  
- **[LumosX: Relate Any Identities with Their Attributes for Personalized Video Generation](https://arxiv.org/abs/2603.20192v1)**  
  Authors: Jiazheng Xing, Fei Du, Hangjie Yuan, Pengwei Liu, Hongbin Xu, Hai Ci, Ruigang Niu, Weihua Chen, Fan Wang, Yong Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20192v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jiazheng-xing.github.io/lumosx-home)  
  Keywords: dynamics, diffusion model, text-to-video, evaluation, video generation, benchmark, identity  
- **[X-World: Controllable Ego-Centric Multi-Camera World Models for Scalable End-to-End Driving](https://arxiv.org/abs/2603.19979v1)**  
  Authors: Chaoda Zheng, Sean Li, Jinhao Deng, Zhennan Wang, Shijia Chen, Liqiang Xiao, Ziheng Chi, Hongbin Lin, Kangjie Chen, Boyang Wang, Yu Zhang, Xianming Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19979v1.pdf)  
  Keywords: dynamics, world model, latent video, world simulator, multi-view video, action-conditioned, dit, controllable, evaluation, autonomous driving, style, simulation, video generation, video style transfer  

### Physical Understanding

*Showing the latest 50 out of 138 papers*

- **[Beyond the Golden Data: Resolving the Motion-Vision Quality Dilemma via Timestep Selective Training](https://arxiv.org/abs/2603.25527v1)**  
  Authors: Xiangyang Luo, Qingyu Li, Yuming Li, Guanbo Huang, Yongjie Zhu, Wenyu Qin, Meng Wang, Pengfei Wan, Shao-Lun Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25527v1.pdf)  
  Keywords: dynamics, diffusion model, concept, video diffusion, video generation  
- **[Pixelis: Reasoning in Pixels, from Seeing to Acting](https://arxiv.org/abs/2603.25091v1)**  
  Authors: Yunpeng Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25091v1.pdf)  
  Keywords: dit, benchmark, physical  
- **[DreamerAD: Efficient Reinforcement Learning via Latent World Model for Autonomous Driving](https://arxiv.org/abs/2603.24587v1)**  
  Authors: Pengxuan Yang, Yupeng Zheng, Deheng Qian, Zebin Xing, Qichao Zhang, Linbo Wang, Yichen Zhang, Shaoyu Guo, Zhongpu Xia, Qiang Chen, Junyu Han, Lingyun Xu, Yifeng Pan, Dongbin Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24587v1.pdf)  
  Keywords: world model, autoregressive, dit, autonomous driving, physical, video generation, efficient  
- **[Toward Physically Consistent Driving Video World Models under Challenging Trajectories](https://arxiv.org/abs/2603.24506v1)**  
  Authors: Jiawei Zhou, Zhenxin Zhu, Lingyi Du, Linye Lyu, Lijun Zhou, Zhanqian Wu, Hongcheng Luo, Zhuotao Tian, Bing Wang, Guang Chen, Hangjun Ye, Haiyang Sun, Yu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24506v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wm-research.github.io/PhyGenesis)  
  Keywords: dynamics, trajectory, world model, physics, dit, autonomous driving, physical, simulation, video generation  
- **[WildWorld: A Large-Scale Dataset for Dynamic World Modeling with Actions and Explicit State toward Generative ARPG](https://arxiv.org/abs/2603.23497v1)**  
  Authors: Zhen Li, Zian Meng, Shuwei Shi, Wenshuo Peng, Yuwei Wu, Bo Zheng, Chuanhao Li, Kaipeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23497v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://shandaai.github.io/wildworld-project)  
  Keywords: dynamics, world model, action-conditioned, dit, video generation  
- **[RealMaster: Lifting Rendered Scenes into Photorealistic Video](https://arxiv.org/abs/2603.23462v1)**  
  Authors: Dana Cohen-Bar, Ido Sobol, Raphael Bensadoun, Shelly Sheynin, Oran Gafni, Or Patashnik, Daniel Cohen-Or, Amit Zohar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23462v1.pdf)  
  Keywords: dynamics, diffusion model, dit, video diffusion, video editing, video generation, identity  
- **[ABot-PhysWorld: Interactive World Foundation Model for Robotic Manipulation with Physics Alignment](https://arxiv.org/abs/2603.23376v1)**  
  Authors: Yuzhi Chen, Ronghan Chen, Dongjie Huo, Yandan Yang, Dekang Qi, Haoyun Liu, Tong Lin, Shuang Zeng, Junjin Xiao, Xinyuan Chang, Feng Xiong, Xing Wei, Zhiheng Ma, Mu Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23376v1.pdf)  
  Keywords: trajectory, world model, physics-aware, interactive, physics, controllable, evaluation, physical, diffusion transformer, simulation, video generation, benchmark  
- **[InterDyad: Interactive Dyadic Speech-to-Video Generation by Querying Intermediate Visual Guidance](https://arxiv.org/abs/2603.23132v1)**  
  Authors: Dongwei Pan, Longwei Guo, Jiazhi Guan, Luying Huang, Yiding Li, Haojie Liu, Haocheng Feng, Wei He, Kaisiyuan Wang, Hang Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23132v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://interdyad.github.io)  
  Keywords: dynamics, video synthesis, interactive, evaluation, video generation, identity  
- **[Omni-WorldBench: Towards a Comprehensive Interaction-Centric Evaluation for World Models](https://arxiv.org/abs/2603.22212v1)**  
  Authors: Meiqi Wu, Zhixin Cai, Fufangchen Zhao, Xiaokun Feng, Rujing Dang, Bingze Song, Ruitian Tian, Jiashu Zhu, Jiachen Lei, Hao Dou, Jing Tang, Lei Sun, Jiahong Wu, Xiangxiang Chu, Zeming Liu, Kaiqi Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22212v1.pdf)  
  Keywords: dynamics, 4d generation, world model, interactive, evaluation, video generation, benchmark  
- **[PAM: A Pose-Appearance-Motion Engine for Sim-to-Real HOI Video Generation](https://arxiv.org/abs/2603.22193v2)**  
  Authors: Mingju Gao, Kaisen Yang, Huan-ang Gao, Bohan Li, Ao Ding, Wenyi Li, Yangcheng Yu, Jinkun Liu, Shaocong Xu, Yike Niu, Haohan Chi, Hao Chen, Hao Tang, Yu Zhang, Li Yi, Hao Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22193v2.pdf)  
  Keywords: dit, video generation, controllable, dynamics  

### Surveys & Benchmarks

*Showing the latest 50 out of 197 papers*

- **[RefAlign: Representation Alignment for Reference-to-Video Generation](https://arxiv.org/abs/2603.25743v1)**  
  Authors: Lei Wang, YuXin Song, Ge Wu, Haocheng Feng, Hang Zhou, Jingdong Wang, Yaxing Wang, jian Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25743v1.pdf)  
  Keywords: advertising, video synthesis, virtual try-on, dit, controllable, diffusion transformer, video generation, benchmark, identity  
- **[PMT: Plain Mask Transformer for Image and Video Segmentation with Frozen Vision Encoders](https://arxiv.org/abs/2603.25398v1)**  
  Authors: Niccolò Cavagnero, Narges Norouzi, Gijs Dubbelman, Daan de Geus  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25398v1.pdf) | [![GitHub](https://img.shields.io/github/stars/tue-mps/pmt?style=social)](https://github.com/tue-mps/pmt)  
  Keywords: benchmark  
- **[AnyID: Ultra-Fidelity Universal Identity-Preserving Video Generation from Any Visual References](https://arxiv.org/abs/2603.25188v1)**  
  Authors: Jiahao Wang, Hualian Sheng, Sijia Cai, Yuxiao Yang, Weizhan Zhang, Caixia Yan, Bing Deng, Jieping Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25188v1.pdf)  
  Keywords: architecture, evaluation, creative, video generation, identity  
- **[Pixelis: Reasoning in Pixels, from Seeing to Acting](https://arxiv.org/abs/2603.25091v1)**  
  Authors: Yunpeng Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25091v1.pdf)  
  Keywords: dit, benchmark, physical  
- **[GaussFusion: Improving 3D Reconstruction in the Wild with A Geometry-Informed Video Generator](https://arxiv.org/abs/2603.25053v1)**  
  Authors: Liyuan Zhu, Manjunath Narayana, Michal Stary, Will Hutchcroft, Gordon Wetzstein, Iro Armeni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25053v1.pdf)  
  Keywords: video-to-video, interactive, video generation, benchmark, efficient  
- **[MoE-GRPO: Optimizing Mixture-of-Experts via Reinforcement Learning in Vision-Language Models](https://arxiv.org/abs/2603.24984v1)**  
  Authors: Dohwan Ko, Jinyoung Park, Seoung Choi, Sanghyeok Lee, Seohyun Lee, Hyunwoo J. Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24984v1.pdf)  
  Keywords: multi-modal, benchmark, architecture  
- **[OmniWeaving: Towards Unified Video Generation with Free-form Composition and Reasoning](https://arxiv.org/abs/2603.24458v1)**  
  Authors: Kaihang Pan, Qi Tian, Jianwei Zhang, Weijie Kong, Jiangfeng Xiong, Yanxin Long, Shixue Zhang, Haiyi Qiu, Tan Wang, Zheqi Lv, Yue Wu, Liefeng Bo, Siliang Tang, Zhao Zhong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24458v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://omniweaving.github.io)  
  Keywords: video generation, benchmark  
- **[ScrollScape: Unlocking 32K Image Generation With Video Diffusion Priors](https://arxiv.org/abs/2603.24270v2)**  
  Authors: Haodong Yu, Yabo Zhang, Donglin Di, Ruyi Zhang, Wangmeng Zuo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24270v2.pdf)  
  Keywords: diffusion model, temporal consistency, super-resolution, evaluation, video diffusion, video generation, efficient  
- **[Leave No Stone Unturned: Uncovering Holistic Audio-Visual Intrinsic Coherence for Deepfake Detection](https://arxiv.org/abs/2603.23960v1)**  
  Authors: Jielun Peng, Yabin Wang, Yaqi Li, Long Kong, Xiaopeng Hong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23960v1.pdf) | [![GitHub](https://img.shields.io/github/stars/tuffy-studio/HAVIC?style=social)](https://github.com/tuffy-studio/HAVIC)  
  Keywords: dit, text-to-video, benchmark, image-to-video  
- **[Attention-aware Inference Optimizations for Large Vision-Language Models with Memory-efficient Decoding](https://arxiv.org/abs/2603.23914v1)**  
  Authors: Fatih Ilhan, Gaowen Liu, Ramana Rao Kompella, Selim Furkan Tekin, Tiansheng Huang, Zachary Yahn, Yichang Xu, Ling Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23914v1.pdf)  
  Keywords: multi-modal, benchmark, efficient  

### Text-to-Video Generation

*Showing the latest 50 out of 65 papers*

- **[ShotStream: Streaming Multi-Shot Video Generation for Interactive Storytelling](https://arxiv.org/abs/2603.25746v1)**  
  Authors: Yawen Luo, Xiaoyu Shi, Junhao Zhuang, Yutian Chen, Quande Liu, Xintao Wang, Pengfei Wan, Tianfan Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25746v1.pdf)  
  Keywords: architecture, interactive, autoregressive, streaming, dit, text-to-video, video generation, efficient, distillation  
- **[Leave No Stone Unturned: Uncovering Holistic Audio-Visual Intrinsic Coherence for Deepfake Detection](https://arxiv.org/abs/2603.23960v1)**  
  Authors: Jielun Peng, Yabin Wang, Yaqi Li, Long Kong, Xiaopeng Hong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23960v1.pdf) | [![GitHub](https://img.shields.io/github/stars/tuffy-studio/HAVIC?style=social)](https://github.com/tuffy-studio/HAVIC)  
  Keywords: dit, text-to-video, benchmark, image-to-video  
- **[Mamba-VMR: Multimodal Query Augmentation via Generated Videos for Precise Temporal Grounding](https://arxiv.org/abs/2603.22121v1)**  
  Authors: Yunzhuo Sun, Xinyue Liu, Yanyang Li, Nanding Wu, Yifang Xu, Linlin Zong, Xianchao Zhang, Wenxin Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22121v1.pdf)  
  Keywords: architecture, text-driven video, dynamics, multi-modal, dit, text-to-video, evaluation, benchmark, efficient  
- **[P-Flow: Prompting Visual Effects Generation](https://arxiv.org/abs/2603.22091v1)**  
  Authors: Rui Zhao, Mike Zheng Shou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22091v1.pdf) | [![GitHub](https://img.shields.io/github/stars/showlab/P-Flow?style=social)](https://github.com/showlab/P-Flow)  
  Keywords: video generation, text-to-video, customization, image-to-video  
- **[PROBE: Diagnosing Residual Concept Capacity in Erased Text-to-Video Diffusion Models](https://arxiv.org/abs/2603.21547v1)**  
  Authors: Yiwei Xie, Zheng Zhang, Ping Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21547v1.pdf) | [![GitHub](https://img.shields.io/github/stars/YiweiXie/PRObingBasedEvaluation?style=social)](https://github.com/YiweiXie/PRObingBasedEvaluation)  
  Keywords: denoising, architecture, t2v, diffusion model, concept, dit, text-to-video, evaluation, video diffusion  
- **[LumosX: Relate Any Identities with Their Attributes for Personalized Video Generation](https://arxiv.org/abs/2603.20192v1)**  
  Authors: Jiazheng Xing, Fei Du, Hangjie Yuan, Pengwei Liu, Hongbin Xu, Hai Ci, Ruigang Niu, Weihua Chen, Fan Wang, Yong Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20192v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jiazheng-xing.github.io/lumosx-home)  
  Keywords: dynamics, diffusion model, text-to-video, evaluation, video generation, benchmark, identity  
- **[Making Video Models Adhere to User Intent with Minor Adjustments](https://arxiv.org/abs/2603.19672v1)**  
  Authors: Daniel Ajisafe, Eric Hedlin, Helge Rhodin, Kwang Moo Yi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19672v1.pdf)  
  Keywords: diffusion model, text-to-video, video diffusion, layout  
- **[Versatile Editing of Video Content, Actions, and Dynamics without Training](https://arxiv.org/abs/2603.17989v1)**  
  Authors: Vladimir Kulikov, Roni Paiss, Andrey Voynov, Inbar Mosseri, Tali Dekel, Tomer Michaeli  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17989v1.pdf)  
  Keywords: dynamics, dit, text-to-video, video editing, video generation  
- **[Steering Video Diffusion Transformers with Massive Activations](https://arxiv.org/abs/2603.17825v1)**  
  Authors: Xianhang Cheng, Yujian Zheng, Zhenyu Xie, Tingting Liao, Hao Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17825v1.pdf)  
  Keywords: video generation, text-to-video, video diffusion, diffusion transformer  
- **[GenState-AI: State-Aware Dataset for Text-to-Video Retrieval on AI-Generated Videos](https://arxiv.org/abs/2603.14426v1)**  
  Authors: Minghan Li, Tongna Chen, Tianrui Lv, Yishuai Zhang, Suchao An, Guodong Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14426v1.pdf)  
  Keywords: dit, controllable, text-to-video, evaluation, i2v, benchmark  

### Video Editing

- **[TRACE: Object Motion Editing in Videos with First-Frame Trajectory Guidance](https://arxiv.org/abs/2603.25707v1)**  
  Authors: Quynh Phung, Long Mai, Cusuh Ham, Feng Liu, Jia-Bin Huang, Aniruddha Mahapatra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25707v1.pdf)  
  Keywords: trajectory, image-to-video, video-to-video, dit, controllable, video editing  
- **[GaussFusion: Improving 3D Reconstruction in the Wild with A Geometry-Informed Video Generator](https://arxiv.org/abs/2603.25053v1)**  
  Authors: Liyuan Zhu, Manjunath Narayana, Michal Stary, Will Hutchcroft, Gordon Wetzstein, Iro Armeni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25053v1.pdf)  
  Keywords: video-to-video, interactive, video generation, benchmark, efficient  
- **[Accelerating Diffusion-based Video Editing via Heterogeneous Caching: Beyond Full Computing at Sampled Denoising Timestep](https://arxiv.org/abs/2603.24260v1)**  
  Authors: Tianyi Liu, Ye Lu, Linfeng Zhang, Chen Cai, Jianjun Gao, Yi Wang, Kim-Hui Yap, Lap-Pui Chau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24260v1.pdf)  
  Keywords: denoising, video-to-video, dit, video diffusion, diffusion transformer, video editing, acceleration  
- **[RealMaster: Lifting Rendered Scenes into Photorealistic Video](https://arxiv.org/abs/2603.23462v1)**  
  Authors: Dana Cohen-Bar, Ido Sobol, Raphael Bensadoun, Shelly Sheynin, Oran Gafni, Or Patashnik, Daniel Cohen-Or, Amit Zohar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23462v1.pdf)  
  Keywords: dynamics, diffusion model, dit, video diffusion, video editing, video generation, identity  
- **[X-World: Controllable Ego-Centric Multi-Camera World Models for Scalable End-to-End Driving](https://arxiv.org/abs/2603.19979v1)**  
  Authors: Chaoda Zheng, Sean Li, Jinhao Deng, Zhennan Wang, Shijia Chen, Liqiang Xiao, Ziheng Chi, Hongbin Lin, Kangjie Chen, Boyang Wang, Yu Zhang, Xianming Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19979v1.pdf)  
  Keywords: dynamics, world model, latent video, world simulator, multi-view video, action-conditioned, dit, controllable, evaluation, autonomous driving, style, simulation, video generation, video style transfer  
- **[Versatile Editing of Video Content, Actions, and Dynamics without Training](https://arxiv.org/abs/2603.17989v1)**  
  Authors: Vladimir Kulikov, Roni Paiss, Andrey Voynov, Inbar Mosseri, Tali Dekel, Tomer Michaeli  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17989v1.pdf)  
  Keywords: dynamics, dit, text-to-video, video editing, video generation  
- **[Script-to-Slide Grounding: Grounding Script Sentences to Slide Objects for Automatic Instructional Video Generation](https://arxiv.org/abs/2603.16931v1)**  
  Authors: Rena Suzuki, Masato Kikuchi, Tadachika Ozono  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16931v1.pdf)  
  Keywords: video editing, video generation, dit, education  
- **[SAW: Toward a Surgical Action World Model via Controllable and Scalable Video Generation](https://arxiv.org/abs/2603.13024v1)**  
  Authors: Sampath Rapuri, Lalithkumar Seenivasan, Dominik Schneider, Roger Soberanis-Mukul, Yufan He, Hao Ding, Jiru Xu, Chenhao Yu, Chenyan Jing, Pengfei Guo, Daguang Xu, Mathias Unberath  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.13024v1.pdf)  
  Keywords: trajectory, world model, diffusion model, video-to-video, temporal consistency, dit, controllable, video diffusion, simulation, video generation  
- **[When to Lock Attention: Training-Free KV Control in Video Diffusion](https://arxiv.org/abs/2603.09657v1)**  
  Authors: Tianyi Zeng, Jincheng Gao, Tianyi Wang, Zijie Meng, Miao Zhang, Jun Yin, Haoyuan Sun, Junfeng Jiao, Christian Claudel, Junbo Tan, Xueqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09657v1.pdf)  
  Keywords: denoising, diffusion model, dit, video diffusion, video editing  
- **[Place-it-R1: Unlocking Environment-aware Reasoning Potential of MLLM for Video Object Insertion](https://arxiv.org/abs/2603.06140v1)**  
  Authors: Bohai Gu, Taiyi Wu, Dazhao Du, Jian Liu, Shuai Yang, Xiaotong Zhao, Alan Zhao, Song Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06140v1.pdf)  
  Keywords: diffusion model, dit, video diffusion, physical, video editing  

### Video Inpainting & Completion

- **[ChopGrad: Pixel-Wise Losses for Latent Video Diffusion via Truncated Backpropagation](https://arxiv.org/abs/2603.17812v1)**  
  Authors: Dmitriy Rivkin, Parker Ewen, Lili Gao, Julian Ost, Stefanie Walz, Rasika Kangutkar, Mario Bijelic, Felix Heide  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17812v1.pdf)  
  Keywords: diffusion model, latent video, super-resolution, video enhancement, dit, video diffusion, video inpainting, video generation, efficient  
- **[ConfCtrl: Enabling Precise Camera Control in Video Diffusion via Confidence-Aware Interpolation](https://arxiv.org/abs/2603.09819v1)**  
  Authors: Liudi Yang, George Eskandar, Fengyi Shen, Mohammad Altillawi, Yang Bai, Chi Zhang, Ziyuan Liu, Abhinav Valada  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09819v1.pdf)  
  Keywords: diffusion model, dit, novel view, video diffusion, camera control, video interpolation  
- **[Pinterest Canvas: Large-Scale Image Generation at Pinterest](https://arxiv.org/abs/2603.06453v1)**  
  Authors: Yu Wang, Eric Tzeng, Raymond Shiau, Jie Yang, Dmitry Kislyuk, Charles Rosenberg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06453v1.pdf)  
  Keywords: image-to-video, diffusion model, dit, video generation, outpainting  
- **[Learning Physics-Grounded 4D Dynamics with Neural Gaussian Force Fields](https://arxiv.org/abs/2602.00148v2)**  
  Authors: Shiqian Li, Ruihong Shen, Junfeng Ni, Chang Pan, Chi Zhang, Yixin Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.00148v2.pdf)  
  Keywords: dynamics, world model, interactive, physics, video prediction, evaluation, physical, simulation, video generation  

### Video Super-Resolution & Enhancement

*Showing the latest 50 out of 63 papers*

- **[Anti-I2V: Safeguarding your photos from malicious image-to-video generation](https://arxiv.org/abs/2603.24570v1)**  
  Authors: Duc Vu, Anh Nguyen, Chi Tran, Anh Tran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24570v1.pdf)  
  Keywords: denoising, architecture, image-to-video, diffusion model, temporal consistency, dit, human animation, video diffusion, i2v, diffusion transformer, video generation  
- **[ScrollScape: Unlocking 32K Image Generation With Video Diffusion Priors](https://arxiv.org/abs/2603.24270v2)**  
  Authors: Haodong Yu, Yabo Zhang, Donglin Di, Ruyi Zhang, Wangmeng Zuo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24270v2.pdf)  
  Keywords: diffusion model, temporal consistency, super-resolution, evaluation, video diffusion, video generation, efficient  
- **[Accelerating Diffusion-based Video Editing via Heterogeneous Caching: Beyond Full Computing at Sampled Denoising Timestep](https://arxiv.org/abs/2603.24260v1)**  
  Authors: Tianyi Liu, Ye Lu, Linfeng Zhang, Chen Cai, Jianjun Gao, Yi Wang, Kim-Hui Yap, Lap-Pui Chau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24260v1.pdf)  
  Keywords: denoising, video-to-video, dit, video diffusion, diffusion transformer, video editing, acceleration  
- **[TETO: Tracking Events with Teacher Observation for Motion Estimation and Frame Interpolation](https://arxiv.org/abs/2603.23487v1)**  
  Authors: Jini Yang, Eunbeen Hong, Soowon Son, Hyunkoo Lee, Sunghwan Hong, Sunok Kim, Seungryong Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23487v1.pdf)  
  Keywords: dit, video diffusion, diffusion transformer, frame interpolation, distillation  
- **[Speed by Simplicity: A Single-Stream Architecture for Fast Audio-Video Generative Foundation Model](https://arxiv.org/abs/2603.21986v1)**  
  Authors: SII-GAIR, Sand. ai, :, Ethan Chern, Hansi Teng, Hanwen Sun, Hao Wang, Hong Pan, Hongyu Jia, Jiadi Su, Jin Li, Junjie Yu, Lijie Liu, Lingzhi Li, Lyumanshan Ye, Min Hu, Qiangang Wang, Quanwei Qi, Steffi Chern, Tao Bu, Taoran Wang, Teren Xu, Tianning Zhang, Tiantian Mi, Weixian Xu, Wenqiang Zhang, Wentai Zhang, Xianping Yi, Xiaojie Cai, Xiaoyang Kang, Yan Ma, Yixiu Liu, Yunbo Zhang, Yunpeng Huang, Yutong Lin, Zewei Tao, Zhaoliang Liu, Zheng Zhang, Zhiyao Cen, Zhixuan Yu, Zhongshu Wang, Zhulin Hu, Zijin Zhou, Zinan Guo, Yue Cao, Pengfei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21986v1.pdf)  
  Keywords: architecture, super-resolution, evaluation, body motion, efficient, distillation  
- **[Adaptive Video Distillation: Mitigating Oversaturation and Temporal Collapse in Few-Step Generation](https://arxiv.org/abs/2603.21864v1)**  
  Authors: Yuyang You, Yongzhi Li, Jiahui Li, Yadong Mu, Quan Chen, Peng Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21864v1.pdf)  
  Keywords: diffusion model, video synthesis, video diffusion, physical, frame interpolation, video generation, benchmark, efficient, distillation  
- **[PROBE: Diagnosing Residual Concept Capacity in Erased Text-to-Video Diffusion Models](https://arxiv.org/abs/2603.21547v1)**  
  Authors: Yiwei Xie, Zheng Zhang, Ping Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21547v1.pdf) | [![GitHub](https://img.shields.io/github/stars/YiweiXie/PRObingBasedEvaluation?style=social)](https://github.com/YiweiXie/PRObingBasedEvaluation)  
  Keywords: denoising, architecture, t2v, diffusion model, concept, dit, text-to-video, evaluation, video diffusion  
- **[Uni-Classifier: Leveraging Video Diffusion Priors for Universal Guidance Classifier](https://arxiv.org/abs/2603.20382v1)**  
  Authors: Yujie Zhou, Pengyang Ling, Jiazi Bu, Bingjie Gao, Li Niu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20382v1.pdf)  
  Keywords: denoising, video diffusion  
- **[Spectrally-Guided Diffusion Noise Schedules](https://arxiv.org/abs/2603.19222v1)**  
  Authors: Carlos Esteves, Ameesh Makadia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19222v1.pdf)  
  Keywords: diffusion model, video generation, dit, denoising  
- **[EARTalking: End-to-end GPT-style Autoregressive Talking Head Synthesis with Frame-wise Control](https://arxiv.org/abs/2603.20307v1)**  
  Authors: Yuzhe Weng, Haotian Wang, Yuanhong Yu, Jun Du, Shan He, Xiaoyan Wu, Haoran Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20307v1.pdf)  
  Keywords: denoising, talking head, interactive, autoregressive, streaming, dit, style, audio-driven, video generation, identity, efficient  

### World Models & Simulation

*Showing the latest 50 out of 99 papers*

- **[ShotStream: Streaming Multi-Shot Video Generation for Interactive Storytelling](https://arxiv.org/abs/2603.25746v1)**  
  Authors: Yawen Luo, Xiaoyu Shi, Junhao Zhuang, Yutian Chen, Quande Liu, Xintao Wang, Pengfei Wan, Tianfan Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25746v1.pdf)  
  Keywords: architecture, interactive, autoregressive, streaming, dit, text-to-video, video generation, efficient, distillation  
- **[GaussFusion: Improving 3D Reconstruction in the Wild with A Geometry-Informed Video Generator](https://arxiv.org/abs/2603.25053v1)**  
  Authors: Liyuan Zhu, Manjunath Narayana, Michal Stary, Will Hutchcroft, Gordon Wetzstein, Iro Armeni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25053v1.pdf)  
  Keywords: video-to-video, interactive, video generation, benchmark, efficient  
- **[DCARL: A Divide-and-Conquer Framework for Autoregressive Long-Trajectory Video Generation](https://arxiv.org/abs/2603.24835v1)**  
  Authors: Junyi Ouyang, Wenbin Teng, Gonglin Chen, Yajie Zhao, Haiwei Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24835v1.pdf)  
  Keywords: trajectory, world model, diffusion model, autoregressive, video diffusion, video generation  
- **[DreamerAD: Efficient Reinforcement Learning via Latent World Model for Autonomous Driving](https://arxiv.org/abs/2603.24587v1)**  
  Authors: Pengxuan Yang, Yupeng Zheng, Deheng Qian, Zebin Xing, Qichao Zhang, Linbo Wang, Yichen Zhang, Shaoyu Guo, Zhongpu Xia, Qiang Chen, Junyu Han, Lingyun Xu, Yifeng Pan, Dongbin Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24587v1.pdf)  
  Keywords: world model, autoregressive, dit, autonomous driving, physical, video generation, efficient  
- **[Toward Physically Consistent Driving Video World Models under Challenging Trajectories](https://arxiv.org/abs/2603.24506v1)**  
  Authors: Jiawei Zhou, Zhenxin Zhu, Lingyi Du, Linye Lyu, Lijun Zhou, Zhanqian Wu, Hongcheng Luo, Zhuotao Tian, Bing Wang, Guang Chen, Hangjun Ye, Haiyang Sun, Yu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24506v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wm-research.github.io/PhyGenesis)  
  Keywords: dynamics, trajectory, world model, physics, dit, autonomous driving, physical, simulation, video generation  
- **[WildWorld: A Large-Scale Dataset for Dynamic World Modeling with Actions and Explicit State toward Generative ARPG](https://arxiv.org/abs/2603.23497v1)**  
  Authors: Zhen Li, Zian Meng, Shuwei Shi, Wenshuo Peng, Yuwei Wu, Bo Zheng, Chuanhao Li, Kaipeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23497v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://shandaai.github.io/wildworld-project)  
  Keywords: dynamics, world model, action-conditioned, dit, video generation  
- **[Foveated Diffusion: Efficient Spatially Adaptive Image and Video Generation](https://arxiv.org/abs/2603.23491v1)**  
  Authors: Brian Chao, Lior Yariv, Howard Xiao, Gordon Wetzstein  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23491v1.pdf)  
  Keywords: flow matching, diffusion model, interactive, streaming, creative, video generation, efficient  
- **[ABot-PhysWorld: Interactive World Foundation Model for Robotic Manipulation with Physics Alignment](https://arxiv.org/abs/2603.23376v1)**  
  Authors: Yuzhi Chen, Ronghan Chen, Dongjie Huo, Yandan Yang, Dekang Qi, Haoyun Liu, Tong Lin, Shuang Zeng, Junjin Xiao, Xinyuan Chang, Feng Xiong, Xing Wei, Zhiheng Ma, Mu Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23376v1.pdf)  
  Keywords: trajectory, world model, physics-aware, interactive, physics, controllable, evaluation, physical, diffusion transformer, simulation, video generation, benchmark  
- **[InterDyad: Interactive Dyadic Speech-to-Video Generation by Querying Intermediate Visual Guidance](https://arxiv.org/abs/2603.23132v1)**  
  Authors: Dongwei Pan, Longwei Guo, Jiazhi Guan, Luying Huang, Yiding Li, Haojie Liu, Haocheng Feng, Wei He, Kaisiyuan Wang, Hang Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23132v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://interdyad.github.io)  
  Keywords: dynamics, video synthesis, interactive, evaluation, video generation, identity  
- **[Omni-WorldBench: Towards a Comprehensive Interaction-Centric Evaluation for World Models](https://arxiv.org/abs/2603.22212v1)**  
  Authors: Meiqi Wu, Zhixin Cai, Fufangchen Zhao, Xiaokun Feng, Rujing Dang, Bingze Song, Ruitian Tian, Jiashu Zhu, Jiachen Lei, Hao Dou, Jing Tang, Lei Sun, Jiahong Wu, Xiangxiang Chu, Zeming Liu, Kaiqi Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22212v1.pdf)  
  Keywords: dynamics, 4d generation, world model, interactive, evaluation, video generation, benchmark  



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
