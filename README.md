# Awesome Video Diffusions [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Video Diffusion Models and Video Generation. Content is automatically updated daily.

> Last Update: 2026-04-03 02:26:31

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
- [Applications](#applications) (39 papers) - Domain-specific applications of video diffusion models
- [Architecture & Efficiency](#architecture-&-efficiency) (350 papers) - Architectural innovations (DiT, UNet), flow matching, and training/inference efficiency
- [Audio & Multi-modal](#audio-&-multi-modal) (29 papers) - Audio-driven and multi-modal conditioned video generation
- [Controllable Generation](#controllable-generation) (131 papers) - Controllable video generation with motion, camera, pose, or layout guidance
- [Human & Character Animation](#human-&-character-animation) (28 papers) - Human-centric video generation including talking heads, dance, and character animation
- [Image-to-Video Generation](#image-to-video-generation) (41 papers) - Methods for animating still images into videos
- [Long Video Generation](#long-video-generation) (116 papers) - Generating temporally consistent long-form videos beyond short clips
- [Personalization & Customization](#personalization-&-customization) (88 papers) - Personalized video generation with custom subjects, identities, or styles
- [Physical Understanding](#physical-understanding) (141 papers) - Physics-aware video generation and dynamics modeling
- [Surveys & Benchmarks](#surveys-&-benchmarks) (196 papers) - Survey papers, benchmarks, and evaluation metrics for video generation
- [Text-to-Video Generation](#text-to-video-generation) (66 papers) - Foundation models and methods for generating videos from text prompts
- [Video Editing](#video-editing) (31 papers) - Diffusion-based video editing, style transfer, and manipulation
- [Video Inpainting & Completion](#video-inpainting-&-completion) (4 papers) - Video inpainting, completion, outpainting, and temporal prediction
- [Video Super-Resolution & Enhancement](#video-super-resolution-&-enhancement) (62 papers) - Video quality improvement, upscaling, restoration, and frame interpolation
- [World Models & Simulation](#world-models-&-simulation) (95 papers) - Video generation as world simulators and interactive environment generation



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3D-aware Video Generation

- **[Control-DINO: Feature Space Conditioning for Controllable Image-to-Video Diffusion](https://arxiv.org/abs/2604.01761v1)**  
  Authors: Edoardo A. Dominici, Thomas Deixelberger, Konstantinos Vardis, Markus Steinberger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01761v1.pdf)  
  Keywords: video diffusion, dit, diffusion model, architecture, style, controllable, simulation, novel view, image-to-video  
- **[I3DM: Implicit 3D-aware Memory Retrieval and Injection for Consistent Video Scene Generation](https://arxiv.org/abs/2603.23413v1)**  
  Authors: Jia Li, Han Yan, Yihang Chen, Siqi Li, Xibin Song, Yifu Wang, Jianfei Cai, Tien-Tsin Wong, Pan Ji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23413v1.pdf)  
  Keywords: dit, camera control, novel view, 3d-aware, video generation  
- **[GO-Renderer: Generative Object Rendering with 3D-aware Controllable Video Diffusion Models](https://arxiv.org/abs/2603.23246v1)**  
  Authors: Zekai Gu, Shuoxuan Feng, Yansong Wang, Hanzhuo Huang, Zhongshuo Du, Chengfeng Zhao, Chengwei Ren, Peng Wang, Yuan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23246v1.pdf)  
  Keywords: video diffusion, dit, diffusion model, controllable, 3d-aware, efficient  
- **[Omni-WorldBench: Towards a Comprehensive Interaction-Centric Evaluation for World Models](https://arxiv.org/abs/2603.22212v1)**  
  Authors: Meiqi Wu, Zhixin Cai, Fufangchen Zhao, Xiaokun Feng, Rujing Dang, Bingze Song, Ruitian Tian, Jiashu Zhu, Jiachen Lei, Hao Dou, Jing Tang, Lei Sun, Jiahong Wu, Xiangxiang Chu, Zeming Liu, Kaiqi Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22212v1.pdf)  
  Keywords: 4d generation, benchmark, dynamics, world model, evaluation, interactive, video generation  
- **[X-World: Controllable Ego-Centric Multi-Camera World Models for Scalable End-to-End Driving](https://arxiv.org/abs/2603.19979v2)**  
  Authors: Chaoda Zheng, Sean Li, Jinhao Deng, Zhennan Wang, Shijia Chen, Liqiang Xiao, Ziheng Chi, Hongbin Lin, Kangjie Chen, Boyang Wang, Yu Zhang, Xianming Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19979v2.pdf)  
  Keywords: autonomous driving, dit, dynamics, world model, style, controllable, multi-view video, evaluation, world simulator, simulation, action-conditioned, video style transfer, video generation, latent video  
- **[OrbitNVS: Harnessing Video Diffusion Priors for Novel View Synthesis](https://arxiv.org/abs/2603.19613v1)**  
  Authors: Jinglin Liang, Zijian Zhou, Rui Huang, Shuangping Huang, Yichen Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19613v1.pdf)  
  Keywords: video diffusion, benchmark, camera control, novel view, video generation  
- **[3DreamBooth: High-Fidelity 3D Subject-Driven Video Generation Model](https://arxiv.org/abs/2603.18524v1)**  
  Authors: Hyun-kyu Ko, Jihyeon Park, Younghyun Kim, Dongheok Park, Eunbyung Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18524v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ko-lani.github.io/3DreamBooth)  
  Keywords: dit, identity, multi-view video, customization, novel view, 3d-aware, video generation, subject-driven  
- **[TAPESTRY: From Geometry to Appearance via Consistent Turntable Videos](https://arxiv.org/abs/2603.17735v1)**  
  Authors: Yan Zeng, Haoran Jiang, Kaixin Yao, Qixuan Zhang, Longwen Zhang, Lan Xu, Jingyi Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17735v1.pdf)  
  Keywords: video diffusion, dit, diffusion model, multi-modal, 3d-aware, video generation  
- **[Tri-Prompting: Video Diffusion with Unified Control over Scene, Subject, and Motion](https://arxiv.org/abs/2603.15614v1)**  
  Authors: Zhenghong Zhou, Xiaohang Zhan, Zhiqin Chen, Soo Ye Kim, Nanxuan Zhao, Haitian Zheng, Qing Liu, He Zhang, Zhe Lin, Yuqian Zhou, Jiebo Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.15614v1.pdf)  
  Keywords: video diffusion, dit, identity, diffusion model, architecture, controllable, motion control, customization, 3d-aware  
- **[GeoNVS: Geometry Grounded Video Diffusion for Novel View Synthesis](https://arxiv.org/abs/2603.14965v1)**  
  Authors: Minjun Kang, Inkyu Shin, Taeyeop Lee, Myungchul Kim, In So Kweon, Kuk-Jin Yoon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14965v1.pdf)  
  Keywords: video diffusion, dit, diffusion model, camera control, novel view  

### Applications

- **[ONE-SHOT: Compositional Human-Environment Video Synthesis via Spatial-Decoupled Motion Injection and Hybrid Context Integration](https://arxiv.org/abs/2604.01043v1)**  
  Authors: Fengyuan Yang, Luying Huang, Jiazhi Guan, Quanwei Yang, Dongwei Pan, Jianglin Fu, Haocheng Feng, Wei He, Kaisiyuan Wang, Hang Zhou, Angela Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01043v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://martayang.github.io/ONE-SHOT)  
  Keywords: dit, dynamics, creative, video synthesis, video generation, efficient  
- **[Collaborative AI Agents and Critics for Fault Detection and Cause Analysis in Network Telemetry](https://arxiv.org/abs/2604.00319v1)**  
  Authors: Syed Eqbal Alam, Zhan Shu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00319v1.pdf)  
  Keywords: evaluation, video generation, medical  
- **[Face2Parts: Exploring Coarse-to-Fine Inter-Regional Facial Dependencies for Generalized Deepfake Detection](https://arxiv.org/abs/2603.26036v1)**  
  Authors: Kutub Uddin, Nusrat Tasnim, Byung Tae Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26036v1.pdf)  
  Keywords: benchmark, advertising  
- **[RefAlign: Representation Alignment for Reference-to-Video Generation](https://arxiv.org/abs/2603.25743v1)**  
  Authors: Lei Wang, YuXin Song, Ge Wu, Haocheng Feng, Hang Zhou, Jingdong Wang, Yaxing Wang, jian Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25743v1.pdf)  
  Keywords: benchmark, virtual try-on, dit, identity, controllable, advertising, diffusion transformer, video synthesis, video generation  
- **[AnyID: Ultra-Fidelity Universal Identity-Preserving Video Generation from Any Visual References](https://arxiv.org/abs/2603.25188v1)**  
  Authors: Jiahao Wang, Hualian Sheng, Sijia Cai, Yuxiao Yang, Weizhan Zhang, Caixia Yan, Bing Deng, Jieping Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25188v1.pdf)  
  Keywords: identity, architecture, creative, evaluation, video generation  
- **[DreamerAD: Efficient Reinforcement Learning via Latent World Model for Autonomous Driving](https://arxiv.org/abs/2603.24587v2)**  
  Authors: Pengxuan Yang, Yupeng Zheng, Deheng Qian, Zebin Xing, Qichao Zhang, Linbo Wang, Yichen Zhang, Shaoyu Guo, Zhongpu Xia, Qiang Chen, Junyu Han, Lingyun Xu, Yifeng Pan, Dongbin Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24587v2.pdf)  
  Keywords: autonomous driving, autoregressive, dit, physical, world model, video generation, efficient  
- **[Toward Physically Consistent Driving Video World Models under Challenging Trajectories](https://arxiv.org/abs/2603.24506v2)**  
  Authors: Jiawei Zhou, Zhenxin Zhu, Lingyi Du, Linye Lyu, Lijun Zhou, Zhanqian Wu, Hongcheng Luo, Zhuotao Tian, Bing Wang, Guang Chen, Hangjun Ye, Haiyang Sun, Yu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24506v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wm-research.github.io/PhyGenesis)  
  Keywords: physics, autonomous driving, dit, dynamics, physical, world model, trajectory, simulation, video generation  
- **[Foveated Diffusion: Efficient Spatially Adaptive Image and Video Generation](https://arxiv.org/abs/2603.23491v1)**  
  Authors: Brian Chao, Lior Yariv, Howard Xiao, Gordon Wetzstein  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23491v1.pdf)  
  Keywords: diffusion model, streaming, creative, flow matching, interactive, video generation, efficient  
- **[X-World: Controllable Ego-Centric Multi-Camera World Models for Scalable End-to-End Driving](https://arxiv.org/abs/2603.19979v2)**  
  Authors: Chaoda Zheng, Sean Li, Jinhao Deng, Zhennan Wang, Shijia Chen, Liqiang Xiao, Ziheng Chi, Hongbin Lin, Kangjie Chen, Boyang Wang, Yu Zhang, Xianming Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19979v2.pdf)  
  Keywords: autonomous driving, dit, dynamics, world model, style, controllable, multi-view video, evaluation, world simulator, simulation, action-conditioned, video style transfer, video generation, latent video  
- **[Student views in AI Ethics and Social Impact](https://arxiv.org/abs/2603.18827v1)**  
  Authors: Tudor-Dan Mihoc, Manuela-Andreea Petrescu, Emilia-Loredana Pop  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18827v1.pdf)  
  Keywords: autonomous driving, survey, education, concept  

### Architecture & Efficiency

*Showing the latest 50 out of 350 papers*

- **[Generative World Renderer](https://arxiv.org/abs/2604.02329v1)**  
  Authors: Zheng-Hui Huang, Zhixiang Wang, Jiaming Tan, Ruihan Yu, Yidan Zhang, Bo Zheng, Yu-Lun Liu, Yung-Yu Chuang, Kaipeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02329v1.pdf)  
  Keywords: temporal consistency, dit, style, controllable, evaluation, video generation  
- **[VOID: Video Object and Interaction Deletion](https://arxiv.org/abs/2604.02296v1)**  
  Authors: Saman Motamed, William Harvey, Benjamin Klein, Luc Van Gool, Zhuoning Yuan, Ta-Ying Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02296v1.pdf)  
  Keywords: video diffusion, dit, dynamics, diffusion model, physical, video editing  
- **[DriveDreamer-Policy: A Geometry-Grounded World-Action Model for Unified Generation and Planning](https://arxiv.org/abs/2604.01765v1)**  
  Authors: Yang Zhou, Xiaofeng Wang, Hao Shao, Letian Wang, Guosheng Zhao, Jiangnan Shao, Jiagang Zhu, Tingdong Yu, Zheng Zhu, Guan Huang, Steven L. Waslander  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01765v1.pdf)  
  Keywords: benchmark, physical, world model, architecture, controllable, video generation  
- **[Control-DINO: Feature Space Conditioning for Controllable Image-to-Video Diffusion](https://arxiv.org/abs/2604.01761v1)**  
  Authors: Edoardo A. Dominici, Thomas Deixelberger, Konstantinos Vardis, Markus Steinberger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01761v1.pdf)  
  Keywords: video diffusion, dit, diffusion model, architecture, style, controllable, simulation, novel view, image-to-video  
- **[Can Video Diffusion Models Predict Past Frames? Bidirectional Cycle Consistency for Reversible Interpolation](https://arxiv.org/abs/2604.01700v1)**  
  Authors: Lingyu Liu, Yaxiong Wang, Li Zhu, Zhedong Zheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01700v1.pdf)  
  Keywords: video diffusion, frame interpolation, temporal consistency, dit, dynamics, diffusion model, architecture  
- **[From Understanding to Erasing: Towards Complete and Stable Video Object Removal](https://arxiv.org/abs/2604.01693v1)**  
  Authors: Dingming Liu, Wenjing Wang, Chen Li, Jing Lyu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01693v1.pdf) | [![GitHub](https://img.shields.io/github/stars/WeChatCV/UnderEraser?style=social)](https://github.com/WeChatCV/UnderEraser)  
  Keywords: video diffusion, temporal consistency, distillation, benchmark, denoising, diffusion model, physical  
- **[DynaVid: Learning to Generate Highly Dynamic Videos using Synthetic Motion Data](https://arxiv.org/abs/2604.01666v1)**  
  Authors: Wonjoon Jin, Jiyun Won, Janghyeok Han, Qi Dai, Chong Luo, Seung-Hwan Baek, Sunghyun Cho  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01666v1.pdf)  
  Keywords: video diffusion, dit, diffusion model, motion control, human motion, video synthesis  
- **[ZEUS: Accelerating Diffusion Models with Only Second-Order Predictor](https://arxiv.org/abs/2604.01552v1)**  
  Authors: Yixiao Wang, Ting Jiang, Zishan Shao, Hancheng Ye, Jingwei Sun, Mingyuan Ma, Jianyi Zhang, Yiran Chen, Hai Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01552v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Ting-Justin-Jiang/ZEUS?style=social)](https://github.com/Ting-Justin-Jiang/ZEUS)  
  Keywords: denoising, diffusion model, acceleration, architecture, trajectory, evaluation, video generation  
- **[TRACE: High-Fidelity 3D Scene Editing via Tangible Reconstruction and Geometry-Aligned Contextual Video Masking](https://arxiv.org/abs/2604.01207v1)**  
  Authors: Jiyuan Hu, Zechuan Zhang, Zongxin Yang, Yi Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01207v1.pdf)  
  Keywords: video diffusion, autoregressive, physical, dit  
- **[ReinDriveGen: Reinforcement Post-Training for Out-of-Distribution Driving Scene Generation](https://arxiv.org/abs/2604.01129v1)**  
  Authors: Hao Zhang, Lue Fan, Weikang Bian, Zehuan Wu, Lewei Lu, Zhaoxiang Zhang, Hongsheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01129v1.pdf)  
  Keywords: video diffusion, diffusion model, dit  

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
  Keywords: benchmark, dit, dynamics, architecture, multi-modal, evaluation, text-driven video, efficient, text-to-video  
- **[EARTalking: End-to-end GPT-style Autoregressive Talking Head Synthesis with Frame-wise Control](https://arxiv.org/abs/2603.20307v1)**  
  Authors: Yuzhe Weng, Haotian Wang, Yuanhong Yu, Jun Du, Shan He, Xiaoyan Wu, Haoran Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20307v1.pdf)  
  Keywords: autoregressive, dit, denoising, identity, style, streaming, interactive, talking head, audio-driven, efficient, video generation  
- **[Improving Joint Audio-Video Generation with Cross-Modal Context Learning](https://arxiv.org/abs/2603.18600v1)**  
  Authors: Bingqi Ma, Linlong Lang, Ming Zhang, Dailan He, Xingtong Ge, Yi Zhang, Guanglu Song, Yu Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18600v1.pdf)  
  Keywords: video diffusion, dit, diffusion model, architecture, multi-modal, evaluation, video generation  
- **[Insight-V++: Towards Advanced Long-Chain Visual Reasoning with Multimodal Large Language Models](https://arxiv.org/abs/2603.18118v1)**  
  Authors: Yuhao Dong, Zuyan Liu, Shulin Tian, Yongming Rao, Ziwei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18118v1.pdf)  
  Keywords: architecture, multi-modal, benchmark, dit  
- **[TAPESTRY: From Geometry to Appearance via Consistent Turntable Videos](https://arxiv.org/abs/2603.17735v1)**  
  Authors: Yan Zeng, Haoran Jiang, Kaixin Yao, Qixuan Zhang, Longwen Zhang, Lan Xu, Jingyi Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17735v1.pdf)  
  Keywords: video diffusion, dit, diffusion model, multi-modal, 3d-aware, video generation  
- **[Bridging Scene Generation and Planning: Driving with World Model via Unifying Vision and Motion Representation](https://arxiv.org/abs/2603.14948v1)**  
  Authors: Xingtai Gui, Meijie Zhang, Tianyi Yan, Wencheng Han, Jiahao Gong, Feiyang Tan, Cheng-zhong Xu, Jianbing Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14948v1.pdf)  
  Keywords: autonomous driving, dit, benchmark, dynamics, world model, trajectory, multi-modal, video generation  
- **[V-JEPA 2.1: Unlocking Dense Features in Video Self-Supervised Learning](https://arxiv.org/abs/2603.14482v2)**  
  Authors: Lorenzo Mur-Labadia, Matthew Muckley, Amir Bar, Mido Assran, Koustuv Sinha, Mike Rabbat, Yann LeCun, Nicolas Ballas, Adrien Bardes  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14482v2.pdf)  
  Keywords: world model, benchmark, multi-modal  
- **[Fuel Gauge: Estimating Chain-of-Thought Length Ahead of Time in Large Multimodal Models](https://arxiv.org/abs/2603.10335v1)**  
  Authors: Yuedong Yang, Xiwen Wei, Mustafa Munir, Radu Marculescu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.10335v1.pdf)  
  Keywords: benchmark, efficient, multi-modal  

### Controllable Generation

*Showing the latest 50 out of 131 papers*

- **[ActionParty: Multi-Subject Action Binding in Generative Video Games](https://arxiv.org/abs/2604.02330v1)**  
  Authors: Alexander Pondaven, Ziyi Wu, Igor Gilitschenski, Philip Torr, Sergey Tulyakov, Fabio Pizzati, Aliaksandr Siarohin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02330v1.pdf)  
  Keywords: video diffusion, autoregressive, benchmark, identity, diffusion model, world model, controllable, interactive  
- **[Generative World Renderer](https://arxiv.org/abs/2604.02329v1)**  
  Authors: Zheng-Hui Huang, Zhixiang Wang, Jiaming Tan, Ruihan Yu, Yidan Zhang, Bo Zheng, Yu-Lun Liu, Yung-Yu Chuang, Kaipeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02329v1.pdf)  
  Keywords: temporal consistency, dit, style, controllable, evaluation, video generation  
- **[DriveDreamer-Policy: A Geometry-Grounded World-Action Model for Unified Generation and Planning](https://arxiv.org/abs/2604.01765v1)**  
  Authors: Yang Zhou, Xiaofeng Wang, Hao Shao, Letian Wang, Guosheng Zhao, Jiangnan Shao, Jiagang Zhu, Tingdong Yu, Zheng Zhu, Guan Huang, Steven L. Waslander  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01765v1.pdf)  
  Keywords: benchmark, physical, world model, architecture, controllable, video generation  
- **[Control-DINO: Feature Space Conditioning for Controllable Image-to-Video Diffusion](https://arxiv.org/abs/2604.01761v1)**  
  Authors: Edoardo A. Dominici, Thomas Deixelberger, Konstantinos Vardis, Markus Steinberger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01761v1.pdf)  
  Keywords: video diffusion, dit, diffusion model, architecture, style, controllable, simulation, novel view, image-to-video  
- **[DynaVid: Learning to Generate Highly Dynamic Videos using Synthetic Motion Data](https://arxiv.org/abs/2604.01666v1)**  
  Authors: Wonjoon Jin, Jiyun Won, Janghyeok Han, Qi Dai, Chong Luo, Seung-Hwan Baek, Sunghyun Cho  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01666v1.pdf)  
  Keywords: video diffusion, dit, diffusion model, motion control, human motion, video synthesis  
- **[ZEUS: Accelerating Diffusion Models with Only Second-Order Predictor](https://arxiv.org/abs/2604.01552v1)**  
  Authors: Yixiao Wang, Ting Jiang, Zishan Shao, Hancheng Ye, Jingwei Sun, Mingyuan Ma, Jianyi Zhang, Yiran Chen, Hai Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01552v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Ting-Justin-Jiang/ZEUS?style=social)](https://github.com/Ting-Justin-Jiang/ZEUS)  
  Keywords: denoising, diffusion model, acceleration, architecture, trajectory, evaluation, video generation  
- **[MotionGrounder: Grounded Multi-Object Motion Transfer via Diffusion Transformer](https://arxiv.org/abs/2604.00853v1)**  
  Authors: Samuel Teodoro, Yun Chen, Agus Gunawan, Soo Ye Kim, Jihyong Oh, Munchurl Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00853v1.pdf)  
  Keywords: dit, dynamics, controllable, evaluation, diffusion transformer, video generation  
- **[OmniRoam: World Wandering via Long-Horizon Panoramic Video Generation](https://arxiv.org/abs/2603.30045v1)**  
  Authors: Yuheng Liu, Xin Lin, Xinke Li, Baihan Yang, Chen Wang, Kalyan Sunkavalli, Yannick Hold-Geoffroy, Hao Tan, Kai Zhang, Xiaohui Xie, Zifan Shi, Yiwei Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.30045v1.pdf) | [![GitHub](https://img.shields.io/github/stars/yuhengliu02/OmniRoam?style=social)](https://github.com/yuhengliu02/OmniRoam)  
  Keywords: temporal consistency, video generation, controllable, trajectory  
- **[Video Models Reason Early: Exploiting Plan Commitment for Maze Solving](https://arxiv.org/abs/2603.30043v1)**  
  Authors: Kaleb Newman, Tyler Zhu, Olga Russakovsky  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.30043v1.pdf)  
  Keywords: video diffusion, denoising, dynamics, diffusion model, trajectory  
- **[TrajectoryMover: Generative Movement of Object Trajectories in Videos](https://arxiv.org/abs/2603.29092v1)**  
  Authors: Kiran Chhatre, Hyeonho Jeong, Yulia Gryaditskaya, Christopher E. Peters, Chun-Hao Paul Huang, Paul Guerrero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29092v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://chhatrekiran.github.io/trajectorymover)  
  Keywords: trajectory, video editing, identity, dit  

### Human & Character Animation

- **[DynaVid: Learning to Generate Highly Dynamic Videos using Synthetic Motion Data](https://arxiv.org/abs/2604.01666v1)**  
  Authors: Wonjoon Jin, Jiyun Won, Janghyeok Han, Qi Dai, Chong Luo, Seung-Hwan Baek, Sunghyun Cho  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01666v1.pdf)  
  Keywords: video diffusion, dit, diffusion model, motion control, human motion, video synthesis  
- **[FlashSign: Pose-Free Guidance for Efficient Sign Language Video Generation](https://arxiv.org/abs/2603.27915v1)**  
  Authors: Liuzhou Zhang, Zeyu Zhang, Biao Wu, Luyao Tang, Zirui Song, Hongyang He, Renda Han, Guangzhen Yao, Huacan Wang, Ronghao Chen, Xiuying Chen, Guan Huang, Zheng Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27915v1.pdf) | [![GitHub](https://img.shields.io/github/stars/AIGeeksGroup/FlashSign?style=social)](https://github.com/AIGeeksGroup/FlashSign)  
  Keywords: video generation, gesture, efficient  
- **[LOME: Learning Human-Object Manipulation with Action-Conditioned Egocentric World Model](https://arxiv.org/abs/2603.27449v1)**  
  Authors: Quankai Gao, Jiawei Yang, Qiangeng Xu, Le Chen, Yue Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27449v1.pdf)  
  Keywords: temporal consistency, physics, gesture, dit, physical, world model, motion control, action-conditioned, t2v, text-to-video  
- **[RefAlign: Representation Alignment for Reference-to-Video Generation](https://arxiv.org/abs/2603.25743v1)**  
  Authors: Lei Wang, YuXin Song, Ge Wu, Haocheng Feng, Hang Zhou, Jingdong Wang, Yaxing Wang, jian Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25743v1.pdf)  
  Keywords: benchmark, virtual try-on, dit, identity, controllable, advertising, diffusion transformer, video synthesis, video generation  
- **[Anti-I2V: Safeguarding your photos from malicious image-to-video generation](https://arxiv.org/abs/2603.24570v1)**  
  Authors: Duc Vu, Anh Nguyen, Chi Tran, Anh Tran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24570v1.pdf)  
  Keywords: video diffusion, temporal consistency, dit, denoising, diffusion model, architecture, diffusion transformer, i2v, image-to-video, human animation, video generation  
- **[Speed by Simplicity: A Single-Stream Architecture for Fast Audio-Video Generative Foundation Model](https://arxiv.org/abs/2603.21986v1)**  
  Authors: SII-GAIR, Sand. ai, :, Ethan Chern, Hansi Teng, Hanwen Sun, Hao Wang, Hong Pan, Hongyu Jia, Jiadi Su, Jin Li, Junjie Yu, Lijie Liu, Lingzhi Li, Lyumanshan Ye, Min Hu, Qiangang Wang, Quanwei Qi, Steffi Chern, Tao Bu, Taoran Wang, Teren Xu, Tianning Zhang, Tiantian Mi, Weixian Xu, Wenqiang Zhang, Wentai Zhang, Xianping Yi, Xiaojie Cai, Xiaoyang Kang, Yan Ma, Yixiu Liu, Yunbo Zhang, Yunpeng Huang, Yutong Lin, Zewei Tao, Zhaoliang Liu, Zheng Zhang, Zhiyao Cen, Zhixuan Yu, Zhongshu Wang, Zhulin Hu, Zijin Zhou, Zinan Guo, Yue Cao, Pengfei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21986v1.pdf)  
  Keywords: distillation, architecture, evaluation, body motion, efficient, super-resolution  
- **[EARTalking: End-to-end GPT-style Autoregressive Talking Head Synthesis with Frame-wise Control](https://arxiv.org/abs/2603.20307v1)**  
  Authors: Yuzhe Weng, Haotian Wang, Yuanhong Yu, Jun Du, Shan He, Xiaoyan Wu, Haoran Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20307v1.pdf)  
  Keywords: autoregressive, dit, denoising, identity, style, streaming, interactive, talking head, audio-driven, efficient, video generation  
- **[AHOY! Animatable Humans under Occlusion from YouTube Videos with Gaussian Splatting and Video Diffusion Priors](https://arxiv.org/abs/2603.17975v1)**  
  Authors: Aymen Mir, Riza Alp Guler, Xiangjun Tang, Peter Wonka, Gerard Pons-Moll  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17975v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://miraymen.github.io/ahoy)  
  Keywords: video diffusion, identity, diffusion model, architecture, avatar  
- **[SoulX-LiveAct: Towards Hour-Scale Real-Time Human Animation with Neighbor Forcing and ConvKV Memory](https://arxiv.org/abs/2603.11746v2)**  
  Authors: Dingcheng Zhen, Xu Zheng, Ruixin Zhang, Zhiqi Jiang, Yichao Yan, Ming Tao, Shunshun Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.11746v2.pdf)  
  Keywords: autoregressive, dit, diffusion model, video synthesis, streaming, human animation, video generation, efficient  
- **[Controllable Complex Human Motion Video Generation via Text-to-Skeleton Cascades](https://arxiv.org/abs/2603.08028v1)**  
  Authors: Ashkan Taghipour, Morteza Ghahremani, Zinuo Li, Hamid Laga, Farid Boussaid, Mohammed Bennamoun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.08028v1.pdf)  
  Keywords: video diffusion, temporal consistency, autoregressive, benchmark, dit, diffusion model, controllable, motion control, human motion, video generation  

### Image-to-Video Generation

- **[Control-DINO: Feature Space Conditioning for Controllable Image-to-Video Diffusion](https://arxiv.org/abs/2604.01761v1)**  
  Authors: Edoardo A. Dominici, Thomas Deixelberger, Konstantinos Vardis, Markus Steinberger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01761v1.pdf)  
  Keywords: video diffusion, dit, diffusion model, architecture, style, controllable, simulation, novel view, image-to-video  
- **[Think over Trajectories: Leveraging Video Generation to Reconstruct GPS Trajectories from Cellular Signaling](https://arxiv.org/abs/2603.26610v1)**  
  Authors: Ruixing Zhang, Hanzhang Jiang, Leilei Sun, Liangzhe Han, Jibin Wang, Weifeng Lv  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26610v1.pdf)  
  Keywords: image-to-video, video generation, dit, trajectory  
- **[From Static to Dynamic: Exploring Self-supervised Image-to-Video Representation Transfer Learning](https://arxiv.org/abs/2603.26597v1)**  
  Authors: Yang Liu, Qianqian Xu, Peisong Wen, Siran Dai, Xilin Zhao, Qingming Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26597v1.pdf) | [![GitHub](https://img.shields.io/github/stars/yafeng19/Co-Settle?style=social)](https://github.com/yafeng19/Co-Settle)  
  Keywords: image-to-video, dit, temporal consistency  
- **[Generation Is Compression: Zero-Shot Video Coding via Stochastic Rectified Flow](https://arxiv.org/abs/2603.26571v2)**  
  Authors: Ziyue Zeng, Xun Su, Haoyuan Liu, Bingyu Lu, Yui Tatsumi, Hiroshi Watanabe  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26571v2.pdf)  
  Keywords: autoregressive, benchmark, dit, trajectory, i2v, rectified flow, image-to-video, t2v, text-to-video  
- **[IP-Bench: Benchmark for Image Protection Methods in Image-to-Video Generation Scenarios](https://arxiv.org/abs/2603.26154v1)**  
  Authors: Xiaofeng Li, Leyi Sheng, Zhen Sun, Zongmin Zhang, Jiaheng Wei, Xinlei He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26154v1.pdf)  
  Keywords: benchmark, evaluation, i2v, image-to-video, video generation  
- **[TRACE: Object Motion Editing in Videos with First-Frame Trajectory Guidance](https://arxiv.org/abs/2603.25707v1)**  
  Authors: Quynh Phung, Long Mai, Cusuh Ham, Feng Liu, Jia-Bin Huang, Aniruddha Mahapatra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25707v1.pdf)  
  Keywords: dit, video-to-video, trajectory, controllable, image-to-video, video editing  
- **[Anti-I2V: Safeguarding your photos from malicious image-to-video generation](https://arxiv.org/abs/2603.24570v1)**  
  Authors: Duc Vu, Anh Nguyen, Chi Tran, Anh Tran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24570v1.pdf)  
  Keywords: video diffusion, temporal consistency, dit, denoising, diffusion model, architecture, diffusion transformer, i2v, image-to-video, human animation, video generation  
- **[Leave No Stone Unturned: Uncovering Holistic Audio-Visual Intrinsic Coherence for Deepfake Detection](https://arxiv.org/abs/2603.23960v1)**  
  Authors: Jielun Peng, Yabin Wang, Yaqi Li, Long Kong, Xiaopeng Hong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23960v1.pdf) | [![GitHub](https://img.shields.io/github/stars/tuffy-studio/HAVIC?style=social)](https://github.com/tuffy-studio/HAVIC)  
  Keywords: image-to-video, benchmark, text-to-video, dit  
- **[P-Flow: Prompting Visual Effects Generation](https://arxiv.org/abs/2603.22091v1)**  
  Authors: Rui Zhao, Mike Zheng Shou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22091v1.pdf) | [![GitHub](https://img.shields.io/github/stars/showlab/P-Flow?style=social)](https://github.com/showlab/P-Flow)  
  Keywords: image-to-video, video generation, customization, text-to-video  
- **[TransText: Alpha-as-RGB Representation for Transparent Text Animation](https://arxiv.org/abs/2603.17944v2)**  
  Authors: Fei Zhang, Zijian Zhou, Bohao Tang, Sen He, Hang Li, Zhe Wang, Soubhik Sanyal, Pengfei Liu, Viktar Atliha, Tao Xiang, Frost Xu, Semih Gunel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17944v2.pdf)  
  Keywords: image-to-video  

### Long Video Generation

*Showing the latest 50 out of 116 papers*

- **[ActionParty: Multi-Subject Action Binding in Generative Video Games](https://arxiv.org/abs/2604.02330v1)**  
  Authors: Alexander Pondaven, Ziyi Wu, Igor Gilitschenski, Philip Torr, Sergey Tulyakov, Fabio Pizzati, Aliaksandr Siarohin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02330v1.pdf)  
  Keywords: video diffusion, autoregressive, benchmark, identity, diffusion model, world model, controllable, interactive  
- **[Generative World Renderer](https://arxiv.org/abs/2604.02329v1)**  
  Authors: Zheng-Hui Huang, Zhixiang Wang, Jiaming Tan, Ruihan Yu, Yidan Zhang, Bo Zheng, Yu-Lun Liu, Yung-Yu Chuang, Kaipeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02329v1.pdf)  
  Keywords: temporal consistency, dit, style, controllable, evaluation, video generation  
- **[Can Video Diffusion Models Predict Past Frames? Bidirectional Cycle Consistency for Reversible Interpolation](https://arxiv.org/abs/2604.01700v1)**  
  Authors: Lingyu Liu, Yaxiong Wang, Li Zhu, Zhedong Zheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01700v1.pdf)  
  Keywords: video diffusion, frame interpolation, temporal consistency, dit, dynamics, diffusion model, architecture  
- **[From Understanding to Erasing: Towards Complete and Stable Video Object Removal](https://arxiv.org/abs/2604.01693v1)**  
  Authors: Dingming Liu, Wenjing Wang, Chen Li, Jing Lyu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01693v1.pdf) | [![GitHub](https://img.shields.io/github/stars/WeChatCV/UnderEraser?style=social)](https://github.com/WeChatCV/UnderEraser)  
  Keywords: video diffusion, temporal consistency, distillation, benchmark, denoising, diffusion model, physical  
- **[TRACE: High-Fidelity 3D Scene Editing via Tangible Reconstruction and Geometry-Aligned Contextual Video Masking](https://arxiv.org/abs/2604.01207v1)**  
  Authors: Jiyuan Hu, Zechuan Zhang, Zongxin Yang, Yi Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01207v1.pdf)  
  Keywords: video diffusion, autoregressive, physical, dit  
- **[OmniRoam: World Wandering via Long-Horizon Panoramic Video Generation](https://arxiv.org/abs/2603.30045v1)**  
  Authors: Yuheng Liu, Xin Lin, Xinke Li, Baihan Yang, Chen Wang, Kalyan Sunkavalli, Yannick Hold-Geoffroy, Hao Tan, Kai Zhang, Xiaohui Xie, Zifan Shi, Yiwei Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.30045v1.pdf) | [![GitHub](https://img.shields.io/github/stars/yuhengliu02/OmniRoam?style=social)](https://github.com/yuhengliu02/OmniRoam)  
  Keywords: temporal consistency, video generation, controllable, trajectory  
- **[SLVMEval: Synthetic Meta Evaluation Benchmark for Text-to-Long Video Generation](https://arxiv.org/abs/2603.29186v1)**  
  Authors: Ryosuke Matsuda, Keito Kudo, Haruto Yoshida, Nobuyuki Shimizu, Jun Suzuki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29186v1.pdf)  
  Keywords: benchmark, long video, text-to-video, evaluation, t2v, video generation  
- **[Stepper: Stepwise Immersive Scene Generation with Multiview Panoramas](https://arxiv.org/abs/2603.28980v1)**  
  Authors: Felix Wimbauer, Fabian Manhardt, Michael Oechsle, Nikolai Kalischek, Christian Rupprecht, Daniel Cremers, Federico Tombari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.28980v1.pdf)  
  Keywords: diffusion model, world model, autoregressive, video generation  
- **[VistaGEN: Consistent Driving Video Generation with Fine-Grained Control Using Multiview Visual-Language Reasoning](https://arxiv.org/abs/2603.28353v1)**  
  Authors: Li-Heng Chen, Ke Cheng, Yahui Liu, Lei Shi, Shi-Sheng Huang, Hongbo Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.28353v1.pdf)  
  Keywords: evaluation, video generation, long video, temporal consistency  
- **[LOME: Learning Human-Object Manipulation with Action-Conditioned Egocentric World Model](https://arxiv.org/abs/2603.27449v1)**  
  Authors: Quankai Gao, Jiawei Yang, Qiangeng Xu, Le Chen, Yue Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27449v1.pdf)  
  Keywords: temporal consistency, physics, gesture, dit, physical, world model, motion control, action-conditioned, t2v, text-to-video  

### Personalization & Customization

*Showing the latest 50 out of 88 papers*

- **[ActionParty: Multi-Subject Action Binding in Generative Video Games](https://arxiv.org/abs/2604.02330v1)**  
  Authors: Alexander Pondaven, Ziyi Wu, Igor Gilitschenski, Philip Torr, Sergey Tulyakov, Fabio Pizzati, Aliaksandr Siarohin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02330v1.pdf)  
  Keywords: video diffusion, autoregressive, benchmark, identity, diffusion model, world model, controllable, interactive  
- **[Generative World Renderer](https://arxiv.org/abs/2604.02329v1)**  
  Authors: Zheng-Hui Huang, Zhixiang Wang, Jiaming Tan, Ruihan Yu, Yidan Zhang, Bo Zheng, Yu-Lun Liu, Yung-Yu Chuang, Kaipeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02329v1.pdf)  
  Keywords: temporal consistency, dit, style, controllable, evaluation, video generation  
- **[Control-DINO: Feature Space Conditioning for Controllable Image-to-Video Diffusion](https://arxiv.org/abs/2604.01761v1)**  
  Authors: Edoardo A. Dominici, Thomas Deixelberger, Konstantinos Vardis, Markus Steinberger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01761v1.pdf)  
  Keywords: video diffusion, dit, diffusion model, architecture, style, controllable, simulation, novel view, image-to-video  
- **[Gloria: Consistent Character Video Generation via Content Anchors](https://arxiv.org/abs/2603.29931v1)**  
  Authors: Yuhang Yang, Fan Zhang, Huaijin Pi, Shuai Guo, Guowei Xu, Wei Zhai, Yang Cao, Zheng-Jun Zha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29931v1.pdf)  
  Keywords: video generation, dit, identity  
- **[TrajectoryMover: Generative Movement of Object Trajectories in Videos](https://arxiv.org/abs/2603.29092v1)**  
  Authors: Kiran Chhatre, Hyeonho Jeong, Yulia Gryaditskaya, Christopher E. Peters, Chun-Hao Paul Huang, Paul Guerrero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29092v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://chhatrekiran.github.io/trajectorymover)  
  Keywords: trajectory, video editing, identity, dit  
- **[MolmoPoint: Better Pointing for VLMs with Grounding Tokens](https://arxiv.org/abs/2603.28069v1)**  
  Authors: Christopher Clark, Yue Yang, Jae Sung Park, Zixian Ma, Jieyu Zhang, Rohun Tripathi, Mohammadreza Salehi, Sangho Lee, Taira Anderson, Winson Han, Ranjay Krishna  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.28069v1.pdf)  
  Keywords: dit, concept  
- **[TokenDial: Continuous Attribute Control in Text-to-Video via Spatiotemporal Token Offsets](https://arxiv.org/abs/2603.27520v1)**  
  Authors: Zhixuan Liu, Peter Schaldenbrand, Yijun Li, Long Mai, Aniruddha Mahapatra, Cusuh Ham, Jean Oh, Jui-Hsien Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27520v1.pdf)  
  Keywords: dit, identity, dynamics, style, evaluation, video generation, text-to-video  
- **[KV Cache Quantization for Self-Forcing Video Generation: A 33-Method Empirical Study](https://arxiv.org/abs/2603.27469v1)**  
  Authors: Suraj Ranganath, Vaishak Menon, Anish Patnaik  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27469v1.pdf) | [![GitHub](https://img.shields.io/github/stars/suraj-ranganath/kv-quant-longhorizon?style=social)](https://github.com/suraj-ranganath/kv-quant-longhorizon)  
  Keywords: evaluation, video generation, benchmark, style  
- **[RefAlign: Representation Alignment for Reference-to-Video Generation](https://arxiv.org/abs/2603.25743v1)**  
  Authors: Lei Wang, YuXin Song, Ge Wu, Haocheng Feng, Hang Zhou, Jingdong Wang, Yaxing Wang, jian Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25743v1.pdf)  
  Keywords: benchmark, virtual try-on, dit, identity, controllable, advertising, diffusion transformer, video synthesis, video generation  
- **[Beyond the Golden Data: Resolving the Motion-Vision Quality Dilemma via Timestep Selective Training](https://arxiv.org/abs/2603.25527v2)**  
  Authors: Xiangyang Luo, Qingyu Li, Yuming Li, Guanbo Huang, Yongjie Zhu, Wenyu Qin, Meng Wang, Pengfei Wan, Shao-Lun Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25527v2.pdf)  
  Keywords: video diffusion, dynamics, diffusion model, video generation, concept  

### Physical Understanding

*Showing the latest 50 out of 141 papers*

- **[VOID: Video Object and Interaction Deletion](https://arxiv.org/abs/2604.02296v1)**  
  Authors: Saman Motamed, William Harvey, Benjamin Klein, Luc Van Gool, Zhuoning Yuan, Ta-Ying Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02296v1.pdf)  
  Keywords: video diffusion, dit, dynamics, diffusion model, physical, video editing  
- **[Resonance4D: Frequency-Domain Motion Supervision for Preset-Free Physical Parameter Learning in 4D Dynamic Physical Scene Simulation](https://arxiv.org/abs/2604.01994v1)**  
  Authors: Changshe Zhang, Jie Feng, Siyu Chen, Guanbin Li, Ronghua Shang, Junpeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01994v1.pdf)  
  Keywords: video diffusion, physics, dynamics, simulation, physical  
- **[DriveDreamer-Policy: A Geometry-Grounded World-Action Model for Unified Generation and Planning](https://arxiv.org/abs/2604.01765v1)**  
  Authors: Yang Zhou, Xiaofeng Wang, Hao Shao, Letian Wang, Guosheng Zhao, Jiangnan Shao, Jiagang Zhu, Tingdong Yu, Zheng Zhu, Guan Huang, Steven L. Waslander  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01765v1.pdf)  
  Keywords: benchmark, physical, world model, architecture, controllable, video generation  
- **[Can Video Diffusion Models Predict Past Frames? Bidirectional Cycle Consistency for Reversible Interpolation](https://arxiv.org/abs/2604.01700v1)**  
  Authors: Lingyu Liu, Yaxiong Wang, Li Zhu, Zhedong Zheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01700v1.pdf)  
  Keywords: video diffusion, frame interpolation, temporal consistency, dit, dynamics, diffusion model, architecture  
- **[From Understanding to Erasing: Towards Complete and Stable Video Object Removal](https://arxiv.org/abs/2604.01693v1)**  
  Authors: Dingming Liu, Wenjing Wang, Chen Li, Jing Lyu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01693v1.pdf) | [![GitHub](https://img.shields.io/github/stars/WeChatCV/UnderEraser?style=social)](https://github.com/WeChatCV/UnderEraser)  
  Keywords: video diffusion, temporal consistency, distillation, benchmark, denoising, diffusion model, physical  
- **[Moiré Video Authentication: A Physical Signature Against AI Video Generation](https://arxiv.org/abs/2604.01654v1)**  
  Authors: Yuan Qing, Kunyu Zheng, Lingxiao Li, Boqing Gong, Chang Xiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01654v1.pdf)  
  Keywords: physics, video generation, physical  
- **[TRACE: High-Fidelity 3D Scene Editing via Tangible Reconstruction and Geometry-Aligned Contextual Video Masking](https://arxiv.org/abs/2604.01207v1)**  
  Authors: Jiyuan Hu, Zechuan Zhang, Zongxin Yang, Yi Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01207v1.pdf)  
  Keywords: video diffusion, autoregressive, physical, dit  
- **[ONE-SHOT: Compositional Human-Environment Video Synthesis via Spatial-Decoupled Motion Injection and Hybrid Context Integration](https://arxiv.org/abs/2604.01043v1)**  
  Authors: Fengyuan Yang, Luying Huang, Jiazhi Guan, Quanwei Yang, Dongwei Pan, Jianglin Fu, Haocheng Feng, Wei He, Kaisiyuan Wang, Hang Zhou, Angela Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01043v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://martayang.github.io/ONE-SHOT)  
  Keywords: dit, dynamics, creative, video synthesis, video generation, efficient  
- **[MotionGrounder: Grounded Multi-Object Motion Transfer via Diffusion Transformer](https://arxiv.org/abs/2604.00853v1)**  
  Authors: Samuel Teodoro, Yun Chen, Agus Gunawan, Soo Ye Kim, Jihyong Oh, Munchurl Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00853v1.pdf)  
  Keywords: dit, dynamics, controllable, evaluation, diffusion transformer, video generation  
- **[Video Models Reason Early: Exploiting Plan Commitment for Maze Solving](https://arxiv.org/abs/2603.30043v1)**  
  Authors: Kaleb Newman, Tyler Zhu, Olga Russakovsky  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.30043v1.pdf)  
  Keywords: video diffusion, denoising, dynamics, diffusion model, trajectory  

### Surveys & Benchmarks

*Showing the latest 50 out of 196 papers*

- **[ActionParty: Multi-Subject Action Binding in Generative Video Games](https://arxiv.org/abs/2604.02330v1)**  
  Authors: Alexander Pondaven, Ziyi Wu, Igor Gilitschenski, Philip Torr, Sergey Tulyakov, Fabio Pizzati, Aliaksandr Siarohin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02330v1.pdf)  
  Keywords: video diffusion, autoregressive, benchmark, identity, diffusion model, world model, controllable, interactive  
- **[Generative World Renderer](https://arxiv.org/abs/2604.02329v1)**  
  Authors: Zheng-Hui Huang, Zhixiang Wang, Jiaming Tan, Ruihan Yu, Yidan Zhang, Bo Zheng, Yu-Lun Liu, Yung-Yu Chuang, Kaipeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02329v1.pdf)  
  Keywords: temporal consistency, dit, style, controllable, evaluation, video generation  
- **[DriveDreamer-Policy: A Geometry-Grounded World-Action Model for Unified Generation and Planning](https://arxiv.org/abs/2604.01765v1)**  
  Authors: Yang Zhou, Xiaofeng Wang, Hao Shao, Letian Wang, Guosheng Zhao, Jiangnan Shao, Jiagang Zhu, Tingdong Yu, Zheng Zhu, Guan Huang, Steven L. Waslander  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01765v1.pdf)  
  Keywords: benchmark, physical, world model, architecture, controllable, video generation  
- **[From Understanding to Erasing: Towards Complete and Stable Video Object Removal](https://arxiv.org/abs/2604.01693v1)**  
  Authors: Dingming Liu, Wenjing Wang, Chen Li, Jing Lyu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01693v1.pdf) | [![GitHub](https://img.shields.io/github/stars/WeChatCV/UnderEraser?style=social)](https://github.com/WeChatCV/UnderEraser)  
  Keywords: video diffusion, temporal consistency, distillation, benchmark, denoising, diffusion model, physical  
- **[ZEUS: Accelerating Diffusion Models with Only Second-Order Predictor](https://arxiv.org/abs/2604.01552v1)**  
  Authors: Yixiao Wang, Ting Jiang, Zishan Shao, Hancheng Ye, Jingwei Sun, Mingyuan Ma, Jianyi Zhang, Yiran Chen, Hai Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01552v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Ting-Justin-Jiang/ZEUS?style=social)](https://github.com/Ting-Justin-Jiang/ZEUS)  
  Keywords: denoising, diffusion model, acceleration, architecture, trajectory, evaluation, video generation  
- **[MotionGrounder: Grounded Multi-Object Motion Transfer via Diffusion Transformer](https://arxiv.org/abs/2604.00853v1)**  
  Authors: Samuel Teodoro, Yun Chen, Agus Gunawan, Soo Ye Kim, Jihyong Oh, Munchurl Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00853v1.pdf)  
  Keywords: dit, dynamics, controllable, evaluation, diffusion transformer, video generation  
- **[Collaborative AI Agents and Critics for Fault Detection and Cause Analysis in Network Telemetry](https://arxiv.org/abs/2604.00319v1)**  
  Authors: Syed Eqbal Alam, Zhan Shu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00319v1.pdf)  
  Keywords: evaluation, video generation, medical  
- **[SLVMEval: Synthetic Meta Evaluation Benchmark for Text-to-Long Video Generation](https://arxiv.org/abs/2603.29186v1)**  
  Authors: Ryosuke Matsuda, Keito Kudo, Haruto Yoshida, Nobuyuki Shimizu, Jun Suzuki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29186v1.pdf)  
  Keywords: benchmark, long video, text-to-video, evaluation, t2v, video generation  
- **[VistaGEN: Consistent Driving Video Generation with Fine-Grained Control Using Multiview Visual-Language Reasoning](https://arxiv.org/abs/2603.28353v1)**  
  Authors: Li-Heng Chen, Ke Cheng, Yahui Liu, Lei Shi, Shi-Sheng Huang, Hongbo Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.28353v1.pdf)  
  Keywords: evaluation, video generation, long video, temporal consistency  
- **[LogiStory: A Logic-Aware Framework for Multi-Image Story Visualization](https://arxiv.org/abs/2603.28082v1)**  
  Authors: Chutian Meng, Fan Ma, Chi Zhang, Jiaxu Miao, Yi Yang, Yueting Zhuang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.28082v1.pdf)  
  Keywords: evaluation, video generation, benchmark  

### Text-to-Video Generation

*Showing the latest 50 out of 66 papers*

- **[SLVMEval: Synthetic Meta Evaluation Benchmark for Text-to-Long Video Generation](https://arxiv.org/abs/2603.29186v1)**  
  Authors: Ryosuke Matsuda, Keito Kudo, Haruto Yoshida, Nobuyuki Shimizu, Jun Suzuki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29186v1.pdf)  
  Keywords: benchmark, long video, text-to-video, evaluation, t2v, video generation  
- **[TokenDial: Continuous Attribute Control in Text-to-Video via Spatiotemporal Token Offsets](https://arxiv.org/abs/2603.27520v1)**  
  Authors: Zhixuan Liu, Peter Schaldenbrand, Yijun Li, Long Mai, Aniruddha Mahapatra, Cusuh Ham, Jean Oh, Jui-Hsien Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27520v1.pdf)  
  Keywords: dit, identity, dynamics, style, evaluation, video generation, text-to-video  
- **[LOME: Learning Human-Object Manipulation with Action-Conditioned Egocentric World Model](https://arxiv.org/abs/2603.27449v1)**  
  Authors: Quankai Gao, Jiawei Yang, Qiangeng Xu, Le Chen, Yue Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27449v1.pdf)  
  Keywords: temporal consistency, physics, gesture, dit, physical, world model, motion control, action-conditioned, t2v, text-to-video  
- **[EFlow: Fast Few-Step Video Generator Training from Scratch via Efficient Solution Flow](https://arxiv.org/abs/2603.27086v1)**  
  Authors: Dogyun Park, Yanyu Li, Sergey Tulyakov, Anil Kag  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27086v1.pdf)  
  Keywords: video diffusion, dit, diffusion transformer, efficient, text-to-video  
- **[Generation Is Compression: Zero-Shot Video Coding via Stochastic Rectified Flow](https://arxiv.org/abs/2603.26571v2)**  
  Authors: Ziyue Zeng, Xun Su, Haoyuan Liu, Bingyu Lu, Yui Tatsumi, Hiroshi Watanabe  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26571v2.pdf)  
  Keywords: autoregressive, benchmark, dit, trajectory, i2v, rectified flow, image-to-video, t2v, text-to-video  
- **[THFM: A Unified Video Foundation Model for 4D Human Perception and Beyond](https://arxiv.org/abs/2603.25892v1)**  
  Authors: Letian Wang, Andrei Zanfir, Eduard Gabriel Bazavan, Misha Andriluka, Cristian Sminchisescu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25892v1.pdf)  
  Keywords: video diffusion, benchmark, diffusion model, architecture, text-to-video  
- **[ShotStream: Streaming Multi-Shot Video Generation for Interactive Storytelling](https://arxiv.org/abs/2603.25746v1)**  
  Authors: Yawen Luo, Xiaoyu Shi, Junhao Zhuang, Yutian Chen, Quande Liu, Xintao Wang, Pengfei Wan, Tianfan Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25746v1.pdf)  
  Keywords: distillation, autoregressive, dit, architecture, streaming, interactive, video generation, efficient, text-to-video  
- **[Leave No Stone Unturned: Uncovering Holistic Audio-Visual Intrinsic Coherence for Deepfake Detection](https://arxiv.org/abs/2603.23960v1)**  
  Authors: Jielun Peng, Yabin Wang, Yaqi Li, Long Kong, Xiaopeng Hong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23960v1.pdf) | [![GitHub](https://img.shields.io/github/stars/tuffy-studio/HAVIC?style=social)](https://github.com/tuffy-studio/HAVIC)  
  Keywords: image-to-video, benchmark, text-to-video, dit  
- **[Mamba-VMR: Multimodal Query Augmentation via Generated Videos for Precise Temporal Grounding](https://arxiv.org/abs/2603.22121v1)**  
  Authors: Yunzhuo Sun, Xinyue Liu, Yanyang Li, Nanding Wu, Yifang Xu, Linlin Zong, Xianchao Zhang, Wenxin Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22121v1.pdf)  
  Keywords: benchmark, dit, dynamics, architecture, multi-modal, evaluation, text-driven video, efficient, text-to-video  
- **[P-Flow: Prompting Visual Effects Generation](https://arxiv.org/abs/2603.22091v1)**  
  Authors: Rui Zhao, Mike Zheng Shou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22091v1.pdf) | [![GitHub](https://img.shields.io/github/stars/showlab/P-Flow?style=social)](https://github.com/showlab/P-Flow)  
  Keywords: image-to-video, video generation, customization, text-to-video  

### Video Editing

- **[VOID: Video Object and Interaction Deletion](https://arxiv.org/abs/2604.02296v1)**  
  Authors: Saman Motamed, William Harvey, Benjamin Klein, Luc Van Gool, Zhuoning Yuan, Ta-Ying Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02296v1.pdf)  
  Keywords: video diffusion, dit, dynamics, diffusion model, physical, video editing  
- **[TrajectoryMover: Generative Movement of Object Trajectories in Videos](https://arxiv.org/abs/2603.29092v1)**  
  Authors: Kiran Chhatre, Hyeonho Jeong, Yulia Gryaditskaya, Christopher E. Peters, Chun-Hao Paul Huang, Paul Guerrero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29092v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://chhatrekiran.github.io/trajectorymover)  
  Keywords: trajectory, video editing, identity, dit  
- **[TRACE: Object Motion Editing in Videos with First-Frame Trajectory Guidance](https://arxiv.org/abs/2603.25707v1)**  
  Authors: Quynh Phung, Long Mai, Cusuh Ham, Feng Liu, Jia-Bin Huang, Aniruddha Mahapatra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25707v1.pdf)  
  Keywords: dit, video-to-video, trajectory, controllable, image-to-video, video editing  
- **[GaussFusion: Improving 3D Reconstruction in the Wild with A Geometry-Informed Video Generator](https://arxiv.org/abs/2603.25053v2)**  
  Authors: Liyuan Zhu, Manjunath Narayana, Michal Stary, Will Hutchcroft, Gordon Wetzstein, Iro Armeni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25053v2.pdf)  
  Keywords: benchmark, video-to-video, interactive, video generation, efficient  
- **[Accelerating Diffusion-based Video Editing via Heterogeneous Caching: Beyond Full Computing at Sampled Denoising Timestep](https://arxiv.org/abs/2603.24260v1)**  
  Authors: Tianyi Liu, Ye Lu, Linfeng Zhang, Chen Cai, Jianjun Gao, Yi Wang, Kim-Hui Yap, Lap-Pui Chau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24260v1.pdf)  
  Keywords: video diffusion, dit, video-to-video, denoising, acceleration, diffusion transformer, video editing  
- **[RealMaster: Lifting Rendered Scenes into Photorealistic Video](https://arxiv.org/abs/2603.23462v1)**  
  Authors: Dana Cohen-Bar, Ido Sobol, Raphael Bensadoun, Shelly Sheynin, Oran Gafni, Or Patashnik, Daniel Cohen-Or, Amit Zohar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23462v1.pdf)  
  Keywords: video diffusion, dit, identity, dynamics, diffusion model, video generation, video editing  
- **[X-World: Controllable Ego-Centric Multi-Camera World Models for Scalable End-to-End Driving](https://arxiv.org/abs/2603.19979v2)**  
  Authors: Chaoda Zheng, Sean Li, Jinhao Deng, Zhennan Wang, Shijia Chen, Liqiang Xiao, Ziheng Chi, Hongbin Lin, Kangjie Chen, Boyang Wang, Yu Zhang, Xianming Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19979v2.pdf)  
  Keywords: autonomous driving, dit, dynamics, world model, style, controllable, multi-view video, evaluation, world simulator, simulation, action-conditioned, video style transfer, video generation, latent video  
- **[Versatile Editing of Video Content, Actions, and Dynamics without Training](https://arxiv.org/abs/2603.17989v1)**  
  Authors: Vladimir Kulikov, Roni Paiss, Andrey Voynov, Inbar Mosseri, Tali Dekel, Tomer Michaeli  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17989v1.pdf)  
  Keywords: dit, dynamics, video generation, video editing, text-to-video  
- **[Script-to-Slide Grounding: Grounding Script Sentences to Slide Objects for Automatic Instructional Video Generation](https://arxiv.org/abs/2603.16931v1)**  
  Authors: Rena Suzuki, Masato Kikuchi, Tadachika Ozono  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.16931v1.pdf)  
  Keywords: education, video generation, video editing, dit  
- **[SAW: Toward a Surgical Action World Model via Controllable and Scalable Video Generation](https://arxiv.org/abs/2603.13024v1)**  
  Authors: Sampath Rapuri, Lalithkumar Seenivasan, Dominik Schneider, Roger Soberanis-Mukul, Yufan He, Hao Ding, Jiru Xu, Chenhao Yu, Chenyan Jing, Pengfei Guo, Daguang Xu, Mathias Unberath  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.13024v1.pdf)  
  Keywords: video diffusion, temporal consistency, dit, video-to-video, diffusion model, world model, trajectory, controllable, simulation, video generation  

### Video Inpainting & Completion

- **[ChopGrad: Pixel-Wise Losses for Latent Video Diffusion via Truncated Backpropagation](https://arxiv.org/abs/2603.17812v1)**  
  Authors: Dmitriy Rivkin, Parker Ewen, Lili Gao, Julian Ost, Stefanie Walz, Rasika Kangutkar, Mario Bijelic, Felix Heide  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17812v1.pdf)  
  Keywords: video diffusion, video inpainting, dit, diffusion model, video enhancement, video generation, efficient, latent video, super-resolution  
- **[ConfCtrl: Enabling Precise Camera Control in Video Diffusion via Confidence-Aware Interpolation](https://arxiv.org/abs/2603.09819v1)**  
  Authors: Liudi Yang, George Eskandar, Fengyi Shen, Mohammad Altillawi, Yang Bai, Chi Zhang, Ziyuan Liu, Abhinav Valada  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09819v1.pdf)  
  Keywords: video diffusion, dit, diffusion model, video interpolation, camera control, novel view  
- **[Pinterest Canvas: Large-Scale Image Generation at Pinterest](https://arxiv.org/abs/2603.06453v1)**  
  Authors: Yu Wang, Eric Tzeng, Raymond Shiau, Jie Yang, Dmitry Kislyuk, Charles Rosenberg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06453v1.pdf)  
  Keywords: dit, diffusion model, outpainting, image-to-video, video generation  
- **[Learning Physics-Grounded 4D Dynamics with Neural Gaussian Force Fields](https://arxiv.org/abs/2602.00148v2)**  
  Authors: Shiqian Li, Ruihong Shen, Junfeng Ni, Chang Pan, Chi Zhang, Yixin Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.00148v2.pdf)  
  Keywords: physics, dynamics, video prediction, physical, world model, evaluation, simulation, interactive, video generation  

### Video Super-Resolution & Enhancement

*Showing the latest 50 out of 62 papers*

- **[Can Video Diffusion Models Predict Past Frames? Bidirectional Cycle Consistency for Reversible Interpolation](https://arxiv.org/abs/2604.01700v1)**  
  Authors: Lingyu Liu, Yaxiong Wang, Li Zhu, Zhedong Zheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01700v1.pdf)  
  Keywords: video diffusion, frame interpolation, temporal consistency, dit, dynamics, diffusion model, architecture  
- **[From Understanding to Erasing: Towards Complete and Stable Video Object Removal](https://arxiv.org/abs/2604.01693v1)**  
  Authors: Dingming Liu, Wenjing Wang, Chen Li, Jing Lyu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01693v1.pdf) | [![GitHub](https://img.shields.io/github/stars/WeChatCV/UnderEraser?style=social)](https://github.com/WeChatCV/UnderEraser)  
  Keywords: video diffusion, temporal consistency, distillation, benchmark, denoising, diffusion model, physical  
- **[ZEUS: Accelerating Diffusion Models with Only Second-Order Predictor](https://arxiv.org/abs/2604.01552v1)**  
  Authors: Yixiao Wang, Ting Jiang, Zishan Shao, Hancheng Ye, Jingwei Sun, Mingyuan Ma, Jianyi Zhang, Yiran Chen, Hai Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01552v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Ting-Justin-Jiang/ZEUS?style=social)](https://github.com/Ting-Justin-Jiang/ZEUS)  
  Keywords: denoising, diffusion model, acceleration, architecture, trajectory, evaluation, video generation  
- **[Video Models Reason Early: Exploiting Plan Commitment for Maze Solving](https://arxiv.org/abs/2603.30043v1)**  
  Authors: Kaleb Newman, Tyler Zhu, Olga Russakovsky  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.30043v1.pdf)  
  Keywords: video diffusion, denoising, dynamics, diffusion model, trajectory  
- **[The Surprising Effectiveness of Noise Pretraining for Implicit Neural Representations](https://arxiv.org/abs/2603.29034v1)**  
  Authors: Kushal Vyas, Alper Kayabasi, Daniel Kim, Vishwanath Saragadam, Ashok Veeraraghavan, Guha Balakrishnan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29034v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kushalvyas.github.io/noisepretraining.html)  
  Keywords: efficient, denoising  
- **[Anti-I2V: Safeguarding your photos from malicious image-to-video generation](https://arxiv.org/abs/2603.24570v1)**  
  Authors: Duc Vu, Anh Nguyen, Chi Tran, Anh Tran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24570v1.pdf)  
  Keywords: video diffusion, temporal consistency, dit, denoising, diffusion model, architecture, diffusion transformer, i2v, image-to-video, human animation, video generation  
- **[ScrollScape: Unlocking 32K Image Generation With Video Diffusion Priors](https://arxiv.org/abs/2603.24270v3)**  
  Authors: Haodong Yu, Yabo Zhang, Donglin Di, Ruyi Zhang, Wangmeng Zuo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24270v3.pdf)  
  Keywords: video diffusion, temporal consistency, diffusion model, evaluation, video generation, efficient, super-resolution  
- **[Accelerating Diffusion-based Video Editing via Heterogeneous Caching: Beyond Full Computing at Sampled Denoising Timestep](https://arxiv.org/abs/2603.24260v1)**  
  Authors: Tianyi Liu, Ye Lu, Linfeng Zhang, Chen Cai, Jianjun Gao, Yi Wang, Kim-Hui Yap, Lap-Pui Chau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24260v1.pdf)  
  Keywords: video diffusion, dit, video-to-video, denoising, acceleration, diffusion transformer, video editing  
- **[TETO: Tracking Events with Teacher Observation for Motion Estimation and Frame Interpolation](https://arxiv.org/abs/2603.23487v1)**  
  Authors: Jini Yang, Eunbeen Hong, Soowon Son, Hyunkoo Lee, Sunghwan Hong, Sunok Kim, Seungryong Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23487v1.pdf)  
  Keywords: video diffusion, frame interpolation, distillation, dit, diffusion transformer  
- **[Speed by Simplicity: A Single-Stream Architecture for Fast Audio-Video Generative Foundation Model](https://arxiv.org/abs/2603.21986v1)**  
  Authors: SII-GAIR, Sand. ai, :, Ethan Chern, Hansi Teng, Hanwen Sun, Hao Wang, Hong Pan, Hongyu Jia, Jiadi Su, Jin Li, Junjie Yu, Lijie Liu, Lingzhi Li, Lyumanshan Ye, Min Hu, Qiangang Wang, Quanwei Qi, Steffi Chern, Tao Bu, Taoran Wang, Teren Xu, Tianning Zhang, Tiantian Mi, Weixian Xu, Wenqiang Zhang, Wentai Zhang, Xianping Yi, Xiaojie Cai, Xiaoyang Kang, Yan Ma, Yixiu Liu, Yunbo Zhang, Yunpeng Huang, Yutong Lin, Zewei Tao, Zhaoliang Liu, Zheng Zhang, Zhiyao Cen, Zhixuan Yu, Zhongshu Wang, Zhulin Hu, Zijin Zhou, Zinan Guo, Yue Cao, Pengfei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21986v1.pdf)  
  Keywords: distillation, architecture, evaluation, body motion, efficient, super-resolution  

### World Models & Simulation

*Showing the latest 50 out of 95 papers*

- **[ActionParty: Multi-Subject Action Binding in Generative Video Games](https://arxiv.org/abs/2604.02330v1)**  
  Authors: Alexander Pondaven, Ziyi Wu, Igor Gilitschenski, Philip Torr, Sergey Tulyakov, Fabio Pizzati, Aliaksandr Siarohin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02330v1.pdf)  
  Keywords: video diffusion, autoregressive, benchmark, identity, diffusion model, world model, controllable, interactive  
- **[Resonance4D: Frequency-Domain Motion Supervision for Preset-Free Physical Parameter Learning in 4D Dynamic Physical Scene Simulation](https://arxiv.org/abs/2604.01994v1)**  
  Authors: Changshe Zhang, Jie Feng, Siyu Chen, Guanbin Li, Ronghua Shang, Junpeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01994v1.pdf)  
  Keywords: video diffusion, physics, dynamics, simulation, physical  
- **[DriveDreamer-Policy: A Geometry-Grounded World-Action Model for Unified Generation and Planning](https://arxiv.org/abs/2604.01765v1)**  
  Authors: Yang Zhou, Xiaofeng Wang, Hao Shao, Letian Wang, Guosheng Zhao, Jiangnan Shao, Jiagang Zhu, Tingdong Yu, Zheng Zhu, Guan Huang, Steven L. Waslander  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01765v1.pdf)  
  Keywords: benchmark, physical, world model, architecture, controllable, video generation  
- **[Control-DINO: Feature Space Conditioning for Controllable Image-to-Video Diffusion](https://arxiv.org/abs/2604.01761v1)**  
  Authors: Edoardo A. Dominici, Thomas Deixelberger, Konstantinos Vardis, Markus Steinberger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01761v1.pdf)  
  Keywords: video diffusion, dit, diffusion model, architecture, style, controllable, simulation, novel view, image-to-video  
- **[Stepper: Stepwise Immersive Scene Generation with Multiview Panoramas](https://arxiv.org/abs/2603.28980v1)**  
  Authors: Felix Wimbauer, Fabian Manhardt, Michael Oechsle, Nikolai Kalischek, Christian Rupprecht, Daniel Cremers, Federico Tombari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.28980v1.pdf)  
  Keywords: diffusion model, world model, autoregressive, video generation  
- **[LOME: Learning Human-Object Manipulation with Action-Conditioned Egocentric World Model](https://arxiv.org/abs/2603.27449v1)**  
  Authors: Quankai Gao, Jiawei Yang, Qiangeng Xu, Le Chen, Yue Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27449v1.pdf)  
  Keywords: temporal consistency, physics, gesture, dit, physical, world model, motion control, action-conditioned, t2v, text-to-video  
- **[Rocks, Pebbles and Sand: Modality-aware Scheduling for Multimodal Large Language Model Inference](https://arxiv.org/abs/2603.26498v1)**  
  Authors: Konstantinos Papaioannou, Thaleia Dimitra Doudali  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26498v1.pdf)  
  Keywords: evaluation, dit, efficient, interactive  
- **[MemCam: Memory-Augmented Camera Control for Consistent Video Generation](https://arxiv.org/abs/2603.26193v1)**  
  Authors: Xinhang Gao, Junlin Guan, Shuhan Luo, Wenzhuo Li, Guanghuan Tan, Jiacheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26193v1.pdf)  
  Keywords: dit, long video, controllable, camera control, simulation, interactive, video generation  
- **[ShotStream: Streaming Multi-Shot Video Generation for Interactive Storytelling](https://arxiv.org/abs/2603.25746v1)**  
  Authors: Yawen Luo, Xiaoyu Shi, Junhao Zhuang, Yutian Chen, Quande Liu, Xintao Wang, Pengfei Wan, Tianfan Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25746v1.pdf)  
  Keywords: distillation, autoregressive, dit, architecture, streaming, interactive, video generation, efficient, text-to-video  
- **[GaussFusion: Improving 3D Reconstruction in the Wild with A Geometry-Informed Video Generator](https://arxiv.org/abs/2603.25053v2)**  
  Authors: Liyuan Zhu, Manjunath Narayana, Michal Stary, Will Hutchcroft, Gordon Wetzstein, Iro Armeni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25053v2.pdf)  
  Keywords: benchmark, video-to-video, interactive, video generation, efficient  



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
