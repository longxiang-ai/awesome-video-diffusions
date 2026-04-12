# Awesome Video Diffusions [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Video Diffusion Models and Video Generation. Content is automatically updated daily.

> Last Update: 2026-04-12 02:38:11

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

- [3D-aware Video Generation](#3d-aware-video-generation) (29 papers) - Video generation with 3D awareness, multi-view consistency, and 4D content creation
- [Applications](#applications) (43 papers) - Domain-specific applications of video diffusion models
- [Architecture & Efficiency](#architecture-&-efficiency) (353 papers) - Architectural innovations (DiT, UNet), flow matching, and training/inference efficiency
- [Audio & Multi-modal](#audio-&-multi-modal) (28 papers) - Audio-driven and multi-modal conditioned video generation
- [Controllable Generation](#controllable-generation) (140 papers) - Controllable video generation with motion, camera, pose, or layout guidance
- [Human & Character Animation](#human-&-character-animation) (27 papers) - Human-centric video generation including talking heads, dance, and character animation
- [Image-to-Video Generation](#image-to-video-generation) (40 papers) - Methods for animating still images into videos
- [Long Video Generation](#long-video-generation) (115 papers) - Generating temporally consistent long-form videos beyond short clips
- [Personalization & Customization](#personalization-&-customization) (85 papers) - Personalized video generation with custom subjects, identities, or styles
- [Physical Understanding](#physical-understanding) (144 papers) - Physics-aware video generation and dynamics modeling
- [Surveys & Benchmarks](#surveys-&-benchmarks) (198 papers) - Survey papers, benchmarks, and evaluation metrics for video generation
- [Text-to-Video Generation](#text-to-video-generation) (65 papers) - Foundation models and methods for generating videos from text prompts
- [Video Editing](#video-editing) (32 papers) - Diffusion-based video editing, style transfer, and manipulation
- [Video Inpainting & Completion](#video-inpainting-&-completion) (5 papers) - Video inpainting, completion, outpainting, and temporal prediction
- [Video Super-Resolution & Enhancement](#video-super-resolution-&-enhancement) (61 papers) - Video quality improvement, upscaling, restoration, and frame interpolation
- [World Models & Simulation](#world-models-&-simulation) (89 papers) - Video generation as world simulators and interactive environment generation



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3D-aware Video Generation

- **[Novel View Synthesis as Video Completion](https://arxiv.org/abs/2604.08500v1)**  
  Authors: Qi Wu, Khiem Vuong, Minsik Jeon, Srinivasa Narasimhan, Deva Ramanan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08500v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://frame-crafter.github.io)  
  Keywords: benchmark, diffusion model, video completion, novel view, video diffusion  
- **[Multi-View Video Diffusion Policy: A 3D Spatio-Temporal-Aware Video Action Model](https://arxiv.org/abs/2604.03181v1)**  
  Authors: Peiyan Li, Yixiang Chen, Yuan Xu, Jiabing Yang, Xiangnan Wu, Jun Guo, Nan Sun, Long Qian, Xinghang Li, Xin Xiao, Jing Liu, Nianfeng Liu, Tao Kong, Yan Huang, Liang Wang, Tieniu Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.03181v1.pdf)  
  Keywords: efficient, dit, dynamics, video diffusion, multi-view video  
- **[Control-DINO: Feature Space Conditioning for Controllable Image-to-Video Diffusion](https://arxiv.org/abs/2604.01761v1)**  
  Authors: Edoardo A. Dominici, Thomas Deixelberger, Konstantinos Vardis, Markus Steinberger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01761v1.pdf)  
  Keywords: architecture, style, controllable, diffusion model, dit, simulation, novel view, image-to-video, video diffusion  
- **[HVG-3D: Bridging Real and Simulation Domains for 3D-Conditional Hand-Object Interaction Video Synthesis](https://arxiv.org/abs/2604.03305v1)**  
  Authors: Mingjin Chen, Junhao Chen, Zhaoxin Fan, Yujian Lee, Zichen Dang, Lili Wang, Yawen Cui, Lap-Pui Chau, Yi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.03305v1.pdf)  
  Keywords: architecture, 3d-aware, video generation, dit, video synthesis, simulation  
- **[I3DM: Implicit 3D-aware Memory Retrieval and Injection for Consistent Video Scene Generation](https://arxiv.org/abs/2603.23413v1)**  
  Authors: Jia Li, Han Yan, Yihang Chen, Siqi Li, Xibin Song, Yifu Wang, Jianfei Cai, Tien-Tsin Wong, Pan Ji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23413v1.pdf)  
  Keywords: 3d-aware, video generation, dit, camera control, novel view  
- **[GO-Renderer: Generative Object Rendering with 3D-aware Controllable Video Diffusion Models](https://arxiv.org/abs/2603.23246v1)**  
  Authors: Zekai Gu, Shuoxuan Feng, Yansong Wang, Hanzhuo Huang, Zhongshuo Du, Chengfeng Zhao, Chengwei Ren, Peng Wang, Yuan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23246v1.pdf)  
  Keywords: 3d-aware, efficient, controllable, diffusion model, dit, video diffusion  
- **[Omni-WorldBench: Towards a Comprehensive Interaction-Centric Evaluation for World Models](https://arxiv.org/abs/2603.22212v1)**  
  Authors: Meiqi Wu, Zhixin Cai, Fufangchen Zhao, Xiaokun Feng, Rujing Dang, Bingze Song, Ruitian Tian, Jiashu Zhu, Jiachen Lei, Hao Dou, Jing Tang, Lei Sun, Jiahong Wu, Xiangxiang Chu, Zeming Liu, Kaiqi Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22212v1.pdf)  
  Keywords: world model, evaluation, 4d generation, interactive, benchmark, video generation, dynamics  
- **[X-World: Controllable Ego-Centric Multi-Camera World Models for Scalable End-to-End Driving](https://arxiv.org/abs/2603.19979v2)**  
  Authors: Chaoda Zheng, Sean Li, Jinhao Deng, Zhennan Wang, Shijia Chen, Liqiang Xiao, Ziheng Chi, Hongbin Lin, Kangjie Chen, Boyang Wang, Yu Zhang, Xianming Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19979v2.pdf)  
  Keywords: world model, evaluation, latent video, style, world simulator, action-conditioned, controllable, video generation, video style transfer, dit, autonomous driving, simulation, dynamics, multi-view video  
- **[OrbitNVS: Harnessing Video Diffusion Priors for Novel View Synthesis](https://arxiv.org/abs/2603.19613v1)**  
  Authors: Jinglin Liang, Zijian Zhou, Rui Huang, Shuangping Huang, Yichen Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19613v1.pdf)  
  Keywords: benchmark, video generation, camera control, novel view, video diffusion  
- **[3DreamBooth: High-Fidelity 3D Subject-Driven Video Generation Model](https://arxiv.org/abs/2603.18524v1)**  
  Authors: Hyun-kyu Ko, Jihyeon Park, Younghyun Kim, Dongheok Park, Eunbyung Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18524v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ko-lani.github.io/3DreamBooth)  
  Keywords: 3d-aware, subject-driven, customization, video generation, dit, identity, novel view, multi-view video  

### Applications

- **[Lighting-grounded Video Generation with Renderer-based Agent Reasoning](https://arxiv.org/abs/2604.07966v1)**  
  Authors: Ziqi Cai, Taoyu Yang, Zheng Chang, Si Li, Han Jiang, Shuchen Weng, Boxin Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07966v1.pdf)  
  Keywords: layout, temporal consistency, controllable, video generation, diffusion model, video-to-video, trajectory, video synthesis, dit, film, image-to-video, video diffusion  
- **[Evolution of Video Generative Foundations](https://arxiv.org/abs/2604.06339v1)**  
  Authors: Teng Hu, Jiangning Zhang, Hongrui Huang, Ran Yi, Zihan Su, Jieyu Weng, Zhucun Xue, Lizhuang Ma, Ming-Hsuan Yang, Dacheng Tao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06339v1.pdf) | [![GitHub](https://img.shields.io/github/stars/sjtuplayer/Awesome-Video-Foundations?style=social)](https://github.com/sjtuplayer/Awesome-Video-Foundations)  
  Keywords: education, world model, survey, video generation, diffusion model, dit, autonomous driving, simulation, dynamics, video editing  
- **[OmniCamera: A Unified Framework for Multi-task Video Generation with Arbitrary Camera Control](https://arxiv.org/abs/2604.06010v1)**  
  Authors: Yukun Wang, Ruihuang Li, Jiale Tao, Shiyuan Yang, Liyi Chen, Zhantao Yang, Handz, Yulan Guo, Shuai Shao, Qinglin Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06010v1.pdf)  
  Keywords: video generation, dit, creative, camera control  
- **[DriveVA: Video Action Models are Zero-Shot Drivers](https://arxiv.org/abs/2604.04198v1)**  
  Authors: Mengmeng Liu, Diankun Zhang, Jiuming Liu, Jianfeng Cui, Hongwei Xie, Guang Chen, Hangjun Ye, Michael Ying Yang, Francesco Nex, Hao Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04198v1.pdf)  
  Keywords: world model, video generation, physical, dit, autonomous driving, dynamics, multi-modal, trajectory  
- **[ONE-SHOT: Compositional Human-Environment Video Synthesis via Spatial-Decoupled Motion Injection and Hybrid Context Integration](https://arxiv.org/abs/2604.01043v1)**  
  Authors: Fengyuan Yang, Luying Huang, Jiazhi Guan, Quanwei Yang, Dongwei Pan, Jianglin Fu, Haocheng Feng, Wei He, Kaisiyuan Wang, Hang Zhou, Angela Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01043v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://martayang.github.io/ONE-SHOT)  
  Keywords: efficient, video generation, dit, video synthesis, dynamics, creative  
- **[Collaborative AI Agents and Critics for Fault Detection and Cause Analysis in Network Telemetry](https://arxiv.org/abs/2604.00319v1)**  
  Authors: Syed Eqbal Alam, Zhan Shu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00319v1.pdf)  
  Keywords: video generation, medical, evaluation  
- **[Face2Parts: Exploring Coarse-to-Fine Inter-Regional Facial Dependencies for Generalized Deepfake Detection](https://arxiv.org/abs/2603.26036v1)**  
  Authors: Kutub Uddin, Nusrat Tasnim, Byung Tae Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26036v1.pdf)  
  Keywords: advertising, benchmark  
- **[RefAlign: Representation Alignment for Reference-to-Video Generation](https://arxiv.org/abs/2603.25743v1)**  
  Authors: Lei Wang, YuXin Song, Ge Wu, Haocheng Feng, Hang Zhou, Jingdong Wang, Yaxing Wang, jian Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25743v1.pdf)  
  Keywords: diffusion transformer, controllable, benchmark, video generation, advertising, dit, video synthesis, identity, virtual try-on  
- **[AnyID: Ultra-Fidelity Universal Identity-Preserving Video Generation from Any Visual References](https://arxiv.org/abs/2603.25188v1)**  
  Authors: Jiahao Wang, Hualian Sheng, Sijia Cai, Yuxiao Yang, Weizhan Zhang, Caixia Yan, Bing Deng, Jieping Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25188v1.pdf)  
  Keywords: architecture, evaluation, video generation, identity, creative  
- **[DreamerAD: Efficient Reinforcement Learning via Latent World Model for Autonomous Driving](https://arxiv.org/abs/2603.24587v2)**  
  Authors: Pengxuan Yang, Yupeng Zheng, Deheng Qian, Zebin Xing, Qichao Zhang, Linbo Wang, Yichen Zhang, Shaoyu Guo, Zhongpu Xia, Qiang Chen, Junyu Han, Lingyun Xu, Yifeng Pan, Dongbin Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24587v2.pdf)  
  Keywords: autoregressive, world model, efficient, video generation, physical, dit, autonomous driving  

### Architecture & Efficiency

*Showing the latest 50 out of 353 papers*

- **[Phantom: Physics-Infused Video Generation via Joint Modeling of Visual and Latent Physical Dynamics](https://arxiv.org/abs/2604.08503v1)**  
  Authors: Ying Shen, Jerry Xiong, Tianjiao Yu, Ismini Lourentzou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08503v1.pdf)  
  Keywords: architecture, physics, benchmark, video generation, physical, dit, dynamics, physics-aware  
- **[DiV-INR: Extreme Low-Bitrate Diffusion Video Compression with INR Conditioning](https://arxiv.org/abs/2604.08329v1)**  
  Authors: Eren Çetin, Lucas Relic, Yuanyi Xue, Markus Gross, Christopher Schroers, Roberto Azevedo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08329v1.pdf)  
  Keywords: layout, efficient, benchmark, diffusion model, dit, video diffusion  
- **[Uni-ViGU: Towards Unified Video Generation and Understanding via A Diffusion-Based Video Generator](https://arxiv.org/abs/2604.08121v1)**  
  Authors: Luozheng Qin, Jia Gong, Qian Qiao, Tianjiao Li, Li Xu, Haoyu Pan, Chao Qu, Zhiyu Tan, Hao Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08121v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://fr0zencrane.github.io/uni-vigu-page)  
  Keywords: video generation, architecture, flow matching  
- **[Lighting-grounded Video Generation with Renderer-based Agent Reasoning](https://arxiv.org/abs/2604.07966v1)**  
  Authors: Ziqi Cai, Taoyu Yang, Zheng Chang, Si Li, Han Jiang, Shuchen Weng, Boxin Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07966v1.pdf)  
  Keywords: layout, temporal consistency, controllable, video generation, diffusion model, video-to-video, trajectory, video synthesis, dit, film, image-to-video, video diffusion  
- **[ImVideoEdit: Image-learning Video Editing via 2D Spatial Difference Attention Blocks](https://arxiv.org/abs/2604.07958v1)**  
  Authors: Jiayang Xu, Fan Zhuo, Majun Zhang, Changhao Pan, Zehan Wang, Siyu Chen, Xiaoda Yang, Tao Jin, Zhou Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07958v1.pdf)  
  Keywords: efficient, temporal consistency, dit, dynamics, video editing  
- **[INSPATIO-WORLD: A Real-Time 4D World Simulator via Spatiotemporal Autoregressive Modeling](https://arxiv.org/abs/2604.07209v1)**  
  Authors: InSpatio Team, Donghui Shen, Guofeng Zhang, Haomin Liu, Haoyu Ji, Hujun Bao, Hongjia Zhai, Jialin Liu, Jing Guo, Nan Wang, Siji Pan, Weihong Pan, Weijian Xie, Xianbin Liu, Xiaojun Xiang, Xiaoyu Zhang, Xinyu Chen, Yifu Wang, Yipeng Chen, Zhenzhou Fan, Zhewen Le, Zhichao Ye, Ziqiang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07209v1.pdf)  
  Keywords: architecture, autoregressive, world model, world simulator, controllable, interactive, benchmark, video generation, physical, distillation  
- **[Not all tokens contribute equally to diffusion learning](https://arxiv.org/abs/2604.07026v1)**  
  Authors: Guoqing Zhang, Lu Shi, Wanru Xu, Linna Zhang, Sen Wang, Fangfang Wang, Yigang Cen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07026v1.pdf)  
  Keywords: text-to-video, benchmark, video generation, diffusion model, dit  
- **[Controllable Generative Video Compression](https://arxiv.org/abs/2604.06655v1)**  
  Authors: Ding Ding, Daowen Li, Ying Chen, Yixin Gao, Ruixiao Dong, Kai Li, Li Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06655v1.pdf)  
  Keywords: video generation, dit, controllable  
- **[Evolution of Video Generative Foundations](https://arxiv.org/abs/2604.06339v1)**  
  Authors: Teng Hu, Jiangning Zhang, Hongrui Huang, Ran Yi, Zihan Su, Jieyu Weng, Zhucun Xue, Lizhuang Ma, Ming-Hsuan Yang, Dacheng Tao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06339v1.pdf) | [![GitHub](https://img.shields.io/github/stars/sjtuplayer/Awesome-Video-Foundations?style=social)](https://github.com/sjtuplayer/Awesome-Video-Foundations)  
  Keywords: education, world model, survey, video generation, diffusion model, dit, autonomous driving, simulation, dynamics, video editing  
- **[Action Images: End-to-End Policy Learning via Multiview Video Generation](https://arxiv.org/abs/2604.06168v1)**  
  Authors: Haoyu Zhen, Zixian Gao, Qiao Sun, Yilin Zhao, Yuncong Yang, Yilun Du, Tsun-Hsuan Wang, Yi-Ling Qiao, Chuang Gan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06168v1.pdf)  
  Keywords: world model, evaluation, action-conditioned, video generation, dit  

### Audio & Multi-modal

- **[SceneScribe-1M: A Large-Scale Video Dataset with Comprehensive Geometric and Semantic Annotations](https://arxiv.org/abs/2604.07990v1)**  
  Authors: Yunnan Wang, Kecheng Zheng, Jianyuan Wang, Minghao Chen, David Novotny, Christian Rupprecht, Yinghao Xu, Xing Zhu, Wenjun Zeng, Xin Jin, Yujun Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07990v1.pdf)  
  Keywords: text-to-video, controllable, benchmark, video generation, video synthesis, camera control, multi-modal  
- **[DriveVA: Video Action Models are Zero-Shot Drivers](https://arxiv.org/abs/2604.04198v1)**  
  Authors: Mengmeng Liu, Diankun Zhang, Jiuming Liu, Jianfeng Cui, Hongwei Xie, Guang Chen, Hangjun Ye, Michael Ying Yang, Francesco Nex, Hao Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04198v1.pdf)  
  Keywords: world model, video generation, physical, dit, autonomous driving, dynamics, multi-modal, trajectory  
- **[Beyond Static Vision: Scene Dynamic Field Unlocks Intuitive Physics Understanding in Multi-modal Large Language Models](https://arxiv.org/abs/2604.03302v1)**  
  Authors: Nanxi Li, Xiang Wang, Yuanjie Chen, Haode Zhang, Hong Li, Yong-Lu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.03302v1.pdf) | [![GitHub](https://img.shields.io/github/stars/andylinx/Scene-Dynamic-Field?style=social)](https://github.com/andylinx/Scene-Dynamic-Field)  
  Keywords: physics, efficient, benchmark, physical, dynamics, multi-modal  
- **[MoE-GRPO: Optimizing Mixture-of-Experts via Reinforcement Learning in Vision-Language Models](https://arxiv.org/abs/2603.24984v2)**  
  Authors: Dohwan Ko, Jinyoung Park, Seoung Choi, Sanghyeok Lee, Seohyun Lee, Hyunwoo J. Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24984v2.pdf)  
  Keywords: architecture, multi-modal, benchmark  
- **[Attention-aware Inference Optimizations for Large Vision-Language Models with Memory-efficient Decoding](https://arxiv.org/abs/2603.23914v1)**  
  Authors: Fatih Ilhan, Gaowen Liu, Ramana Rao Kompella, Selim Furkan Tekin, Tiansheng Huang, Zachary Yahn, Yichang Xu, Ling Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23914v1.pdf)  
  Keywords: multi-modal, efficient, benchmark  
- **[Mamba-VMR: Multimodal Query Augmentation via Generated Videos for Precise Temporal Grounding](https://arxiv.org/abs/2603.22121v1)**  
  Authors: Yunzhuo Sun, Xinyue Liu, Yanyang Li, Nanding Wu, Yifang Xu, Linlin Zong, Xianchao Zhang, Wenxin Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22121v1.pdf)  
  Keywords: architecture, evaluation, efficient, text-to-video, benchmark, text-driven video, dit, dynamics, multi-modal  
- **[EARTalking: End-to-end GPT-style Autoregressive Talking Head Synthesis with Frame-wise Control](https://arxiv.org/abs/2603.20307v1)**  
  Authors: Yuzhe Weng, Haotian Wang, Yuanhong Yu, Jun Du, Shan He, Xiaoyan Wu, Haoran Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20307v1.pdf)  
  Keywords: autoregressive, efficient, audio-driven, style, interactive, talking head, video generation, dit, identity, denoising, streaming  
- **[Improving Joint Audio-Video Generation with Cross-Modal Context Learning](https://arxiv.org/abs/2603.18600v1)**  
  Authors: Bingqi Ma, Linlong Lang, Ming Zhang, Dailan He, Xingtong Ge, Yi Zhang, Guanglu Song, Yu Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18600v1.pdf)  
  Keywords: architecture, evaluation, video generation, diffusion model, dit, multi-modal, video diffusion  
- **[Insight-V++: Towards Advanced Long-Chain Visual Reasoning with Multimodal Large Language Models](https://arxiv.org/abs/2603.18118v1)**  
  Authors: Yuhao Dong, Zuyan Liu, Shulin Tian, Yongming Rao, Ziwei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18118v1.pdf)  
  Keywords: architecture, multi-modal, dit, benchmark  
- **[TAPESTRY: From Geometry to Appearance via Consistent Turntable Videos](https://arxiv.org/abs/2603.17735v1)**  
  Authors: Yan Zeng, Haoran Jiang, Kaixin Yao, Qixuan Zhang, Longwen Zhang, Lan Xu, Jingyi Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17735v1.pdf)  
  Keywords: 3d-aware, video generation, diffusion model, dit, multi-modal, video diffusion  

### Controllable Generation

*Showing the latest 50 out of 140 papers*

- **[When Numbers Speak: Aligning Textual Numerals and Visual Instances in Text-to-Video Diffusion Models](https://arxiv.org/abs/2604.08546v1)**  
  Authors: Zhengyang Sun, Yu Chen, Xin Zhou, Xiaofan Li, Xiwu Chen, Dingkang Liang, Xiang Bai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08546v1.pdf) | [![GitHub](https://img.shields.io/github/stars/H-EmbodVis/NUMINA?style=social)](https://github.com/H-EmbodVis/NUMINA)  
  Keywords: layout, temporal consistency, text-to-video, diffusion model, video synthesis, video diffusion  
- **[DiV-INR: Extreme Low-Bitrate Diffusion Video Compression with INR Conditioning](https://arxiv.org/abs/2604.08329v1)**  
  Authors: Eren Çetin, Lucas Relic, Yuanyi Xue, Markus Gross, Christopher Schroers, Roberto Azevedo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08329v1.pdf)  
  Keywords: layout, efficient, benchmark, diffusion model, dit, video diffusion  
- **[SceneScribe-1M: A Large-Scale Video Dataset with Comprehensive Geometric and Semantic Annotations](https://arxiv.org/abs/2604.07990v1)**  
  Authors: Yunnan Wang, Kecheng Zheng, Jianyuan Wang, Minghao Chen, David Novotny, Christian Rupprecht, Yinghao Xu, Xing Zhu, Wenjun Zeng, Xin Jin, Yujun Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07990v1.pdf)  
  Keywords: text-to-video, controllable, benchmark, video generation, video synthesis, camera control, multi-modal  
- **[Lighting-grounded Video Generation with Renderer-based Agent Reasoning](https://arxiv.org/abs/2604.07966v1)**  
  Authors: Ziqi Cai, Taoyu Yang, Zheng Chang, Si Li, Han Jiang, Shuchen Weng, Boxin Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07966v1.pdf)  
  Keywords: layout, temporal consistency, controllable, video generation, diffusion model, video-to-video, trajectory, video synthesis, dit, film, image-to-video, video diffusion  
- **[INSPATIO-WORLD: A Real-Time 4D World Simulator via Spatiotemporal Autoregressive Modeling](https://arxiv.org/abs/2604.07209v1)**  
  Authors: InSpatio Team, Donghui Shen, Guofeng Zhang, Haomin Liu, Haoyu Ji, Hujun Bao, Hongjia Zhai, Jialin Liu, Jing Guo, Nan Wang, Siji Pan, Weihong Pan, Weijian Xie, Xianbin Liu, Xiaojun Xiang, Xiaoyu Zhang, Xinyu Chen, Yifu Wang, Yipeng Chen, Zhenzhou Fan, Zhewen Le, Zhichao Ye, Ziqiang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07209v1.pdf)  
  Keywords: architecture, autoregressive, world model, world simulator, controllable, interactive, benchmark, video generation, physical, distillation  
- **[Controllable Generative Video Compression](https://arxiv.org/abs/2604.06655v1)**  
  Authors: Ding Ding, Daowen Li, Ying Chen, Yixin Gao, Ruixiao Dong, Kai Li, Li Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06655v1.pdf)  
  Keywords: video generation, dit, controllable  
- **[DiffHDR: Re-Exposing LDR Videos with Video Diffusion Models](https://arxiv.org/abs/2604.06161v1)**  
  Authors: Zhengming Yu, Li Ma, Mingming He, Leo Isikdogan, Yuancheng Xu, Dmitriy Smirnov, Pablo Salamanca, Dao Mi, Pablo Delgado, Ning Yu, Julien Philip, Xin Li, Wenping Wang, Paul Debevec  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06161v1.pdf)  
  Keywords: diffusion model, video diffusion, controllable  
- **[OmniCamera: A Unified Framework for Multi-task Video Generation with Arbitrary Camera Control](https://arxiv.org/abs/2604.06010v1)**  
  Authors: Yukun Wang, Ruihuang Li, Jiale Tao, Shiyuan Yang, Liyi Chen, Zhantao Yang, Handz, Yulan Guo, Shuai Shao, Qinglin Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06010v1.pdf)  
  Keywords: video generation, dit, creative, camera control  
- **[HumANDiff: Articulated Noise Diffusion for Motion-Consistent Human Video Generation](https://arxiv.org/abs/2604.05961v1)**  
  Authors: Tao Hu, Varun Jampani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.05961v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://taohuumd.github.io/projects/HumANDiff)  
  Keywords: architecture, physics, style, controllable, video generation, motion control, diffusion model, dit, physical, video synthesis, human motion, dynamics, image-to-video, video diffusion  
- **[DriveVA: Video Action Models are Zero-Shot Drivers](https://arxiv.org/abs/2604.04198v1)**  
  Authors: Mengmeng Liu, Diankun Zhang, Jiuming Liu, Jianfeng Cui, Hongwei Xie, Guang Chen, Hangjun Ye, Michael Ying Yang, Francesco Nex, Hao Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04198v1.pdf)  
  Keywords: world model, video generation, physical, dit, autonomous driving, dynamics, multi-modal, trajectory  

### Human & Character Animation

- **[HumANDiff: Articulated Noise Diffusion for Motion-Consistent Human Video Generation](https://arxiv.org/abs/2604.05961v1)**  
  Authors: Tao Hu, Varun Jampani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.05961v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://taohuumd.github.io/projects/HumANDiff)  
  Keywords: architecture, physics, style, controllable, video generation, motion control, diffusion model, dit, physical, video synthesis, human motion, dynamics, image-to-video, video diffusion  
- **[Vanast: Virtual Try-On with Human Image Animation via Synthetic Triplet Supervision](https://arxiv.org/abs/2604.04934v1)**  
  Authors: Hyunsoo Cha, Wonjung Woo, Byungjun Kim, Hanbyul Joo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04934v1.pdf)  
  Keywords: architecture, diffusion transformer, image animation, human animation, identity, virtual try-on, video diffusion  
- **[DynaVid: Learning to Generate Highly Dynamic Videos using Synthetic Motion Data](https://arxiv.org/abs/2604.01666v1)**  
  Authors: Wonjoon Jin, Jiyun Won, Janghyeok Han, Qi Dai, Chong Luo, Seung-Hwan Baek, Sunghyun Cho  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01666v1.pdf)  
  Keywords: motion control, diffusion model, dit, human motion, video synthesis, video diffusion  
- **[FlashSign: Pose-Free Guidance for Efficient Sign Language Video Generation](https://arxiv.org/abs/2603.27915v1)**  
  Authors: Liuzhou Zhang, Zeyu Zhang, Biao Wu, Luyao Tang, Zirui Song, Hongyang He, Renda Han, Guangzhen Yao, Huacan Wang, Ronghao Chen, Xiuying Chen, Guan Huang, Zheng Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27915v1.pdf) | [![GitHub](https://img.shields.io/github/stars/AIGeeksGroup/FlashSign?style=social)](https://github.com/AIGeeksGroup/FlashSign)  
  Keywords: video generation, efficient, gesture  
- **[LOME: Learning Human-Object Manipulation with Action-Conditioned Egocentric World Model](https://arxiv.org/abs/2603.27449v1)**  
  Authors: Quankai Gao, Jiawei Yang, Qiangeng Xu, Le Chen, Yue Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27449v1.pdf)  
  Keywords: world model, physics, temporal consistency, text-to-video, action-conditioned, motion control, physical, dit, gesture, t2v  
- **[RefAlign: Representation Alignment for Reference-to-Video Generation](https://arxiv.org/abs/2603.25743v1)**  
  Authors: Lei Wang, YuXin Song, Ge Wu, Haocheng Feng, Hang Zhou, Jingdong Wang, Yaxing Wang, jian Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25743v1.pdf)  
  Keywords: diffusion transformer, controllable, benchmark, video generation, advertising, dit, video synthesis, identity, virtual try-on  
- **[Anti-I2V: Safeguarding your photos from malicious image-to-video generation](https://arxiv.org/abs/2603.24570v1)**  
  Authors: Duc Vu, Anh Nguyen, Chi Tran, Anh Tran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24570v1.pdf)  
  Keywords: architecture, temporal consistency, diffusion transformer, denoising, video generation, diffusion model, dit, human animation, i2v, image-to-video, video diffusion  
- **[Speed by Simplicity: A Single-Stream Architecture for Fast Audio-Video Generative Foundation Model](https://arxiv.org/abs/2603.21986v1)**  
  Authors: SII-GAIR, Sand. ai, :, Ethan Chern, Hansi Teng, Hanwen Sun, Hao Wang, Hong Pan, Hongyu Jia, Jiadi Su, Jin Li, Junjie Yu, Lijie Liu, Lingzhi Li, Lyumanshan Ye, Min Hu, Qiangang Wang, Quanwei Qi, Steffi Chern, Tao Bu, Taoran Wang, Teren Xu, Tianning Zhang, Tiantian Mi, Weixian Xu, Wenqiang Zhang, Wentai Zhang, Xianping Yi, Xiaojie Cai, Xiaoyang Kang, Yan Ma, Yixiu Liu, Yunbo Zhang, Yunpeng Huang, Yutong Lin, Zewei Tao, Zhaoliang Liu, Zheng Zhang, Zhiyao Cen, Zhixuan Yu, Zhongshu Wang, Zhulin Hu, Zijin Zhou, Zinan Guo, Yue Cao, Pengfei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21986v1.pdf)  
  Keywords: architecture, evaluation, efficient, body motion, super-resolution, distillation  
- **[EARTalking: End-to-end GPT-style Autoregressive Talking Head Synthesis with Frame-wise Control](https://arxiv.org/abs/2603.20307v1)**  
  Authors: Yuzhe Weng, Haotian Wang, Yuanhong Yu, Jun Du, Shan He, Xiaoyan Wu, Haoran Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20307v1.pdf)  
  Keywords: autoregressive, efficient, audio-driven, style, interactive, talking head, video generation, dit, identity, denoising, streaming  
- **[AHOY! Animatable Humans under Occlusion from YouTube Videos with Gaussian Splatting and Video Diffusion Priors](https://arxiv.org/abs/2603.17975v1)**  
  Authors: Aymen Mir, Riza Alp Guler, Xiangjun Tang, Peter Wonka, Gerard Pons-Moll  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17975v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://miraymen.github.io/ahoy)  
  Keywords: avatar, architecture, diffusion model, identity, video diffusion  

### Image-to-Video Generation

- **[Lighting-grounded Video Generation with Renderer-based Agent Reasoning](https://arxiv.org/abs/2604.07966v1)**  
  Authors: Ziqi Cai, Taoyu Yang, Zheng Chang, Si Li, Han Jiang, Shuchen Weng, Boxin Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07966v1.pdf)  
  Keywords: layout, temporal consistency, controllable, video generation, diffusion model, video-to-video, trajectory, video synthesis, dit, film, image-to-video, video diffusion  
- **[HumANDiff: Articulated Noise Diffusion for Motion-Consistent Human Video Generation](https://arxiv.org/abs/2604.05961v1)**  
  Authors: Tao Hu, Varun Jampani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.05961v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://taohuumd.github.io/projects/HumANDiff)  
  Keywords: architecture, physics, style, controllable, video generation, motion control, diffusion model, dit, physical, video synthesis, human motion, dynamics, image-to-video, video diffusion  
- **[Vanast: Virtual Try-On with Human Image Animation via Synthetic Triplet Supervision](https://arxiv.org/abs/2604.04934v1)**  
  Authors: Hyunsoo Cha, Wonjung Woo, Byungjun Kim, Hanbyul Joo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04934v1.pdf)  
  Keywords: architecture, diffusion transformer, image animation, human animation, identity, virtual try-on, video diffusion  
- **[Control-DINO: Feature Space Conditioning for Controllable Image-to-Video Diffusion](https://arxiv.org/abs/2604.01761v1)**  
  Authors: Edoardo A. Dominici, Thomas Deixelberger, Konstantinos Vardis, Markus Steinberger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01761v1.pdf)  
  Keywords: architecture, style, controllable, diffusion model, dit, simulation, novel view, image-to-video, video diffusion  
- **[Think over Trajectories: Leveraging Video Generation to Reconstruct GPS Trajectories from Cellular Signaling](https://arxiv.org/abs/2603.26610v1)**  
  Authors: Ruixing Zhang, Hanzhang Jiang, Leilei Sun, Liangzhe Han, Jibin Wang, Weifeng Lv  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26610v1.pdf)  
  Keywords: video generation, image-to-video, trajectory, dit  
- **[From Static to Dynamic: Exploring Self-supervised Image-to-Video Representation Transfer Learning](https://arxiv.org/abs/2603.26597v1)**  
  Authors: Yang Liu, Qianqian Xu, Peisong Wen, Siran Dai, Xilin Zhao, Qingming Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26597v1.pdf) | [![GitHub](https://img.shields.io/github/stars/yafeng19/Co-Settle?style=social)](https://github.com/yafeng19/Co-Settle)  
  Keywords: image-to-video, dit, temporal consistency  
- **[Generation Is Compression: Zero-Shot Video Coding via Stochastic Rectified Flow](https://arxiv.org/abs/2603.26571v2)**  
  Authors: Ziyue Zeng, Xun Su, Haoyuan Liu, Bingyu Lu, Yui Tatsumi, Hiroshi Watanabe  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26571v2.pdf)  
  Keywords: autoregressive, text-to-video, benchmark, dit, i2v, image-to-video, trajectory, t2v, rectified flow  
- **[IP-Bench: Benchmark for Image Protection Methods in Image-to-Video Generation Scenarios](https://arxiv.org/abs/2603.26154v1)**  
  Authors: Xiaofeng Li, Leyi Sheng, Zhen Sun, Zongmin Zhang, Jiaheng Wei, Xinlei He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26154v1.pdf)  
  Keywords: evaluation, benchmark, video generation, i2v, image-to-video  
- **[TRACE: Object Motion Editing in Videos with First-Frame Trajectory Guidance](https://arxiv.org/abs/2603.25707v1)**  
  Authors: Quynh Phung, Long Mai, Cusuh Ham, Feng Liu, Jia-Bin Huang, Aniruddha Mahapatra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25707v1.pdf)  
  Keywords: controllable, video-to-video, dit, image-to-video, trajectory, video editing  
- **[Anti-I2V: Safeguarding your photos from malicious image-to-video generation](https://arxiv.org/abs/2603.24570v1)**  
  Authors: Duc Vu, Anh Nguyen, Chi Tran, Anh Tran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24570v1.pdf)  
  Keywords: architecture, temporal consistency, diffusion transformer, denoising, video generation, diffusion model, dit, human animation, i2v, image-to-video, video diffusion  

### Long Video Generation

*Showing the latest 50 out of 115 papers*

- **[When Numbers Speak: Aligning Textual Numerals and Visual Instances in Text-to-Video Diffusion Models](https://arxiv.org/abs/2604.08546v1)**  
  Authors: Zhengyang Sun, Yu Chen, Xin Zhou, Xiaofan Li, Xiwu Chen, Dingkang Liang, Xiang Bai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08546v1.pdf) | [![GitHub](https://img.shields.io/github/stars/H-EmbodVis/NUMINA?style=social)](https://github.com/H-EmbodVis/NUMINA)  
  Keywords: layout, temporal consistency, text-to-video, diffusion model, video synthesis, video diffusion  
- **[Lighting-grounded Video Generation with Renderer-based Agent Reasoning](https://arxiv.org/abs/2604.07966v1)**  
  Authors: Ziqi Cai, Taoyu Yang, Zheng Chang, Si Li, Han Jiang, Shuchen Weng, Boxin Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07966v1.pdf)  
  Keywords: layout, temporal consistency, controllable, video generation, diffusion model, video-to-video, trajectory, video synthesis, dit, film, image-to-video, video diffusion  
- **[ImVideoEdit: Image-learning Video Editing via 2D Spatial Difference Attention Blocks](https://arxiv.org/abs/2604.07958v1)**  
  Authors: Jiayang Xu, Fan Zhuo, Majun Zhang, Changhao Pan, Zehan Wang, Siyu Chen, Xiaoda Yang, Tao Jin, Zhou Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07958v1.pdf)  
  Keywords: efficient, temporal consistency, dit, dynamics, video editing  
- **[INSPATIO-WORLD: A Real-Time 4D World Simulator via Spatiotemporal Autoregressive Modeling](https://arxiv.org/abs/2604.07209v1)**  
  Authors: InSpatio Team, Donghui Shen, Guofeng Zhang, Haomin Liu, Haoyu Ji, Hujun Bao, Hongjia Zhai, Jialin Liu, Jing Guo, Nan Wang, Siji Pan, Weihong Pan, Weijian Xie, Xianbin Liu, Xiaojun Xiang, Xiaoyu Zhang, Xinyu Chen, Yifu Wang, Yipeng Chen, Zhenzhou Fan, Zhewen Le, Zhichao Ye, Ziqiang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07209v1.pdf)  
  Keywords: architecture, autoregressive, world model, world simulator, controllable, interactive, benchmark, video generation, physical, distillation  
- **[Grounded Forcing: Bridging Time-Independent Semantics and Proximal Dynamics in Autoregressive Video Synthesis](https://arxiv.org/abs/2604.06939v1)**  
  Authors: Jintao Chen, Chengyu Bai, Junjun hu, Xinda Xue, Mu Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06939v1.pdf)  
  Keywords: autoregressive, long-form, interactive, video synthesis, dynamics, identity  
- **[Accelerating Training of Autoregressive Video Generation Models via Local Optimization with Representation Continuity](https://arxiv.org/abs/2604.07402v1)**  
  Authors: Yucheng Zhou, Jianbing Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07402v1.pdf)  
  Keywords: video generation, autoregressive, text-to-video  
- **[Salt: Self-Consistent Distribution Matching with Cache-Aware Training for Fast Video Generation](https://arxiv.org/abs/2604.03118v1)**  
  Authors: Xingtong Ge, Yi Zhang, Yushi Huang, Dailan He, Xiahong Wang, Bingqi Ma, Guanglu Song, Yu Liu, Jun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.03118v1.pdf) | [![GitHub](https://img.shields.io/github/stars/XingtongGe/Salt?style=social)](https://github.com/XingtongGe/Salt)  
  Keywords: autoregressive, style, video generation, dit, dynamics, denoising, trajectory, distillation  
- **[Not All Frames Deserve Full Computation: Accelerating Autoregressive Video Generation via Selective Computation and Predictive Extrapolation](https://arxiv.org/abs/2604.02979v1)**  
  Authors: Hanshuai Cui, Zhiqing Tang, Zhi Yao, Fanshuai Meng, Weijia Jia, Wei Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02979v1.pdf)  
  Keywords: autoregressive, efficient, long-form, acceleration, video generation, diffusion model, denoising, video diffusion  
- **[Generative AI for Video Trailer Synthesis: From Extractive Heuristics to Autoregressive Creativity](https://arxiv.org/abs/2604.04953v1)**  
  Authors: Abhishek Dharmaratnakar, Srivaths Ranganathan, Debanshu Das, Anushree Sinha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04953v1.pdf)  
  Keywords: autoregressive, survey, text-to-video, controllable, dit, video synthesis  
- **[ActionParty: Multi-Subject Action Binding in Generative Video Games](https://arxiv.org/abs/2604.02330v1)**  
  Authors: Alexander Pondaven, Ziyi Wu, Igor Gilitschenski, Philip Torr, Sergey Tulyakov, Fabio Pizzati, Aliaksandr Siarohin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02330v1.pdf)  
  Keywords: autoregressive, world model, controllable, interactive, benchmark, diffusion model, identity, video diffusion  

### Personalization & Customization

*Showing the latest 50 out of 85 papers*

- **[Grounded Forcing: Bridging Time-Independent Semantics and Proximal Dynamics in Autoregressive Video Synthesis](https://arxiv.org/abs/2604.06939v1)**  
  Authors: Jintao Chen, Chengyu Bai, Junjun hu, Xinda Xue, Mu Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06939v1.pdf)  
  Keywords: autoregressive, long-form, interactive, video synthesis, dynamics, identity  
- **[HumANDiff: Articulated Noise Diffusion for Motion-Consistent Human Video Generation](https://arxiv.org/abs/2604.05961v1)**  
  Authors: Tao Hu, Varun Jampani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.05961v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://taohuumd.github.io/projects/HumANDiff)  
  Keywords: architecture, physics, style, controllable, video generation, motion control, diffusion model, dit, physical, video synthesis, human motion, dynamics, image-to-video, video diffusion  
- **[Vanast: Virtual Try-On with Human Image Animation via Synthetic Triplet Supervision](https://arxiv.org/abs/2604.04934v1)**  
  Authors: Hyunsoo Cha, Wonjung Woo, Byungjun Kim, Hanbyul Joo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04934v1.pdf)  
  Keywords: architecture, diffusion transformer, image animation, human animation, identity, virtual try-on, video diffusion  
- **[Salt: Self-Consistent Distribution Matching with Cache-Aware Training for Fast Video Generation](https://arxiv.org/abs/2604.03118v1)**  
  Authors: Xingtong Ge, Yi Zhang, Yushi Huang, Dailan He, Xiahong Wang, Bingqi Ma, Guanglu Song, Yu Liu, Jun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.03118v1.pdf) | [![GitHub](https://img.shields.io/github/stars/XingtongGe/Salt?style=social)](https://github.com/XingtongGe/Salt)  
  Keywords: autoregressive, style, video generation, dit, dynamics, denoising, trajectory, distillation  
- **[HairOrbit: Multi-view Aware 3D Hair Modeling from Single Portraits](https://arxiv.org/abs/2604.02867v1)**  
  Authors: Leyang Jin, Yujian Zheng, Bingkui Tong, Yuda Qiu, Zhenyu Xie, Hao Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02867v1.pdf)  
  Keywords: video generation, style, dit  
- **[ActionParty: Multi-Subject Action Binding in Generative Video Games](https://arxiv.org/abs/2604.02330v1)**  
  Authors: Alexander Pondaven, Ziyi Wu, Igor Gilitschenski, Philip Torr, Sergey Tulyakov, Fabio Pizzati, Aliaksandr Siarohin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02330v1.pdf)  
  Keywords: autoregressive, world model, controllable, interactive, benchmark, diffusion model, identity, video diffusion  
- **[Generative World Renderer](https://arxiv.org/abs/2604.02329v1)**  
  Authors: Zheng-Hui Huang, Zhixiang Wang, Jiaming Tan, Ruihan Yu, Yidan Zhang, Bo Zheng, Yu-Lun Liu, Yung-Yu Chuang, Kaipeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02329v1.pdf)  
  Keywords: evaluation, temporal consistency, style, controllable, video generation, dit  
- **[Control-DINO: Feature Space Conditioning for Controllable Image-to-Video Diffusion](https://arxiv.org/abs/2604.01761v1)**  
  Authors: Edoardo A. Dominici, Thomas Deixelberger, Konstantinos Vardis, Markus Steinberger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01761v1.pdf)  
  Keywords: architecture, style, controllable, diffusion model, dit, simulation, novel view, image-to-video, video diffusion  
- **[Gloria: Consistent Character Video Generation via Content Anchors](https://arxiv.org/abs/2603.29931v1)**  
  Authors: Yuhang Yang, Fan Zhang, Huaijin Pi, Shuai Guo, Guowei Xu, Wei Zhai, Yang Cao, Zheng-Jun Zha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29931v1.pdf)  
  Keywords: video generation, dit, identity  
- **[TrajectoryMover: Generative Movement of Object Trajectories in Videos](https://arxiv.org/abs/2603.29092v2)**  
  Authors: Kiran Chhatre, Hyeonho Jeong, Yulia Gryaditskaya, Christopher E. Peters, Chun-Hao Paul Huang, Paul Guerrero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29092v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://chhatrekiran.github.io/trajectorymover)  
  Keywords: dit, trajectory, video editing, identity  

### Physical Understanding

*Showing the latest 50 out of 144 papers*

- **[AVGen-Bench: A Task-Driven Benchmark for Multi-Granular Evaluation of Text-to-Audio-Video Generation](https://arxiv.org/abs/2604.08540v1)**  
  Authors: Ziwei Zhou, Zeyuan Lai, Rui Wang, Yifan Yang, Zhen Xing, Yuqing Yang, Qi Dai, Lili Qiu, Chong Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08540v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](http://aka.ms/avgenbench)  
  Keywords: video generation, evaluation, physical, benchmark  
- **[Phantom: Physics-Infused Video Generation via Joint Modeling of Visual and Latent Physical Dynamics](https://arxiv.org/abs/2604.08503v1)**  
  Authors: Ying Shen, Jerry Xiong, Tianjiao Yu, Ismini Lourentzou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08503v1.pdf)  
  Keywords: architecture, physics, benchmark, video generation, physical, dit, dynamics, physics-aware  
- **[ViVa: A Video-Generative Value Model for Robot Reinforcement Learning](https://arxiv.org/abs/2604.08168v1)**  
  Authors: Jindi Lv, Hao Li, Jie Li, Yifei Nie, Fankun Kong, Yang Wang, Xiaofeng Wang, Zheng Zhu, Chaojun Ni, Qiuping Deng, Hengtao Li, Jiancheng Lv, Guan Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08168v1.pdf)  
  Keywords: dynamics  
- **[ImVideoEdit: Image-learning Video Editing via 2D Spatial Difference Attention Blocks](https://arxiv.org/abs/2604.07958v1)**  
  Authors: Jiayang Xu, Fan Zhuo, Majun Zhang, Changhao Pan, Zehan Wang, Siyu Chen, Xiaoda Yang, Tao Jin, Zhou Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07958v1.pdf)  
  Keywords: efficient, temporal consistency, dit, dynamics, video editing  
- **[INSPATIO-WORLD: A Real-Time 4D World Simulator via Spatiotemporal Autoregressive Modeling](https://arxiv.org/abs/2604.07209v1)**  
  Authors: InSpatio Team, Donghui Shen, Guofeng Zhang, Haomin Liu, Haoyu Ji, Hujun Bao, Hongjia Zhai, Jialin Liu, Jing Guo, Nan Wang, Siji Pan, Weihong Pan, Weijian Xie, Xianbin Liu, Xiaojun Xiang, Xiaoyu Zhang, Xinyu Chen, Yifu Wang, Yipeng Chen, Zhenzhou Fan, Zhewen Le, Zhichao Ye, Ziqiang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07209v1.pdf)  
  Keywords: architecture, autoregressive, world model, world simulator, controllable, interactive, benchmark, video generation, physical, distillation  
- **[Grounded Forcing: Bridging Time-Independent Semantics and Proximal Dynamics in Autoregressive Video Synthesis](https://arxiv.org/abs/2604.06939v1)**  
  Authors: Jintao Chen, Chengyu Bai, Junjun hu, Xinda Xue, Mu Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06939v1.pdf)  
  Keywords: autoregressive, long-form, interactive, video synthesis, dynamics, identity  
- **[Evolution of Video Generative Foundations](https://arxiv.org/abs/2604.06339v1)**  
  Authors: Teng Hu, Jiangning Zhang, Hongrui Huang, Ran Yi, Zihan Su, Jieyu Weng, Zhucun Xue, Lizhuang Ma, Ming-Hsuan Yang, Dacheng Tao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06339v1.pdf) | [![GitHub](https://img.shields.io/github/stars/sjtuplayer/Awesome-Video-Foundations?style=social)](https://github.com/sjtuplayer/Awesome-Video-Foundations)  
  Keywords: education, world model, survey, video generation, diffusion model, dit, autonomous driving, simulation, dynamics, video editing  
- **[HumANDiff: Articulated Noise Diffusion for Motion-Consistent Human Video Generation](https://arxiv.org/abs/2604.05961v1)**  
  Authors: Tao Hu, Varun Jampani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.05961v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://taohuumd.github.io/projects/HumANDiff)  
  Keywords: architecture, physics, style, controllable, video generation, motion control, diffusion model, dit, physical, video synthesis, human motion, dynamics, image-to-video, video diffusion  
- **[UENR-600K: A Large-Scale Physically Grounded Dataset for Nighttime Video Deraining](https://arxiv.org/abs/2604.04402v1)**  
  Authors: Pei Yang, Hai Ci, Beibei Lin, Yiren Song, Mike Zheng Shou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04402v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://showlab.github.io/UENR-600K)  
  Keywords: video generation, physical, video-to-video, benchmark  
- **[DriveVA: Video Action Models are Zero-Shot Drivers](https://arxiv.org/abs/2604.04198v1)**  
  Authors: Mengmeng Liu, Diankun Zhang, Jiuming Liu, Jianfeng Cui, Hongwei Xie, Guang Chen, Hangjun Ye, Michael Ying Yang, Francesco Nex, Hao Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04198v1.pdf)  
  Keywords: world model, video generation, physical, dit, autonomous driving, dynamics, multi-modal, trajectory  

### Surveys & Benchmarks

*Showing the latest 50 out of 198 papers*

- **[AVGen-Bench: A Task-Driven Benchmark for Multi-Granular Evaluation of Text-to-Audio-Video Generation](https://arxiv.org/abs/2604.08540v1)**  
  Authors: Ziwei Zhou, Zeyuan Lai, Rui Wang, Yifan Yang, Zhen Xing, Yuqing Yang, Qi Dai, Lili Qiu, Chong Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08540v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](http://aka.ms/avgenbench)  
  Keywords: video generation, evaluation, physical, benchmark  
- **[Phantom: Physics-Infused Video Generation via Joint Modeling of Visual and Latent Physical Dynamics](https://arxiv.org/abs/2604.08503v1)**  
  Authors: Ying Shen, Jerry Xiong, Tianjiao Yu, Ismini Lourentzou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08503v1.pdf)  
  Keywords: architecture, physics, benchmark, video generation, physical, dit, dynamics, physics-aware  
- **[Novel View Synthesis as Video Completion](https://arxiv.org/abs/2604.08500v1)**  
  Authors: Qi Wu, Khiem Vuong, Minsik Jeon, Srinivasa Narasimhan, Deva Ramanan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08500v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://frame-crafter.github.io)  
  Keywords: benchmark, diffusion model, video completion, novel view, video diffusion  
- **[InstAP: Instance-Aware Vision-Language Pre-Train for Spatial-Temporal Understanding](https://arxiv.org/abs/2604.08337v1)**  
  Authors: Ashutosh Kumar, Rajat Saini, Jingjing Pan, Mustafa Erdogan, Mingfang Zhang, Betty Le Dem, Norimasa Kobori, Quan Kong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08337v1.pdf)  
  Keywords: benchmark  
- **[DiV-INR: Extreme Low-Bitrate Diffusion Video Compression with INR Conditioning](https://arxiv.org/abs/2604.08329v1)**  
  Authors: Eren Çetin, Lucas Relic, Yuanyi Xue, Markus Gross, Christopher Schroers, Roberto Azevedo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08329v1.pdf)  
  Keywords: layout, efficient, benchmark, diffusion model, dit, video diffusion  
- **[SceneScribe-1M: A Large-Scale Video Dataset with Comprehensive Geometric and Semantic Annotations](https://arxiv.org/abs/2604.07990v1)**  
  Authors: Yunnan Wang, Kecheng Zheng, Jianyuan Wang, Minghao Chen, David Novotny, Christian Rupprecht, Yinghao Xu, Xing Zhu, Wenjun Zeng, Xin Jin, Yujun Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07990v1.pdf)  
  Keywords: text-to-video, controllable, benchmark, video generation, video synthesis, camera control, multi-modal  
- **[INSPATIO-WORLD: A Real-Time 4D World Simulator via Spatiotemporal Autoregressive Modeling](https://arxiv.org/abs/2604.07209v1)**  
  Authors: InSpatio Team, Donghui Shen, Guofeng Zhang, Haomin Liu, Haoyu Ji, Hujun Bao, Hongjia Zhai, Jialin Liu, Jing Guo, Nan Wang, Siji Pan, Weihong Pan, Weijian Xie, Xianbin Liu, Xiaojun Xiang, Xiaoyu Zhang, Xinyu Chen, Yifu Wang, Yipeng Chen, Zhenzhou Fan, Zhewen Le, Zhichao Ye, Ziqiang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07209v1.pdf)  
  Keywords: architecture, autoregressive, world model, world simulator, controllable, interactive, benchmark, video generation, physical, distillation  
- **[Not all tokens contribute equally to diffusion learning](https://arxiv.org/abs/2604.07026v1)**  
  Authors: Guoqing Zhang, Lu Shi, Wanru Xu, Linna Zhang, Sen Wang, Fangfang Wang, Yigang Cen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07026v1.pdf)  
  Keywords: text-to-video, benchmark, video generation, diffusion model, dit  
- **[Evolution of Video Generative Foundations](https://arxiv.org/abs/2604.06339v1)**  
  Authors: Teng Hu, Jiangning Zhang, Hongrui Huang, Ran Yi, Zihan Su, Jieyu Weng, Zhucun Xue, Lizhuang Ma, Ming-Hsuan Yang, Dacheng Tao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06339v1.pdf) | [![GitHub](https://img.shields.io/github/stars/sjtuplayer/Awesome-Video-Foundations?style=social)](https://github.com/sjtuplayer/Awesome-Video-Foundations)  
  Keywords: education, world model, survey, video generation, diffusion model, dit, autonomous driving, simulation, dynamics, video editing  
- **[Action Images: End-to-End Policy Learning via Multiview Video Generation](https://arxiv.org/abs/2604.06168v1)**  
  Authors: Haoyu Zhen, Zixian Gao, Qiao Sun, Yilin Zhao, Yuncong Yang, Yilun Du, Tsun-Hsuan Wang, Yi-Ling Qiao, Chuang Gan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06168v1.pdf)  
  Keywords: world model, evaluation, action-conditioned, video generation, dit  

### Text-to-Video Generation

*Showing the latest 50 out of 65 papers*

- **[When Numbers Speak: Aligning Textual Numerals and Visual Instances in Text-to-Video Diffusion Models](https://arxiv.org/abs/2604.08546v1)**  
  Authors: Zhengyang Sun, Yu Chen, Xin Zhou, Xiaofan Li, Xiwu Chen, Dingkang Liang, Xiang Bai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08546v1.pdf) | [![GitHub](https://img.shields.io/github/stars/H-EmbodVis/NUMINA?style=social)](https://github.com/H-EmbodVis/NUMINA)  
  Keywords: layout, temporal consistency, text-to-video, diffusion model, video synthesis, video diffusion  
- **[SceneScribe-1M: A Large-Scale Video Dataset with Comprehensive Geometric and Semantic Annotations](https://arxiv.org/abs/2604.07990v1)**  
  Authors: Yunnan Wang, Kecheng Zheng, Jianyuan Wang, Minghao Chen, David Novotny, Christian Rupprecht, Yinghao Xu, Xing Zhu, Wenjun Zeng, Xin Jin, Yujun Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07990v1.pdf)  
  Keywords: text-to-video, controllable, benchmark, video generation, video synthesis, camera control, multi-modal  
- **[Not all tokens contribute equally to diffusion learning](https://arxiv.org/abs/2604.07026v1)**  
  Authors: Guoqing Zhang, Lu Shi, Wanru Xu, Linna Zhang, Sen Wang, Fangfang Wang, Yigang Cen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07026v1.pdf)  
  Keywords: text-to-video, benchmark, video generation, diffusion model, dit  
- **[Accelerating Training of Autoregressive Video Generation Models via Local Optimization with Representation Continuity](https://arxiv.org/abs/2604.07402v1)**  
  Authors: Yucheng Zhou, Jianbing Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07402v1.pdf)  
  Keywords: video generation, autoregressive, text-to-video  
- **[SCMAPR: Self-Correcting Multi-Agent Prompt Refinement for Complex-Scenario Text-to-Video Generation](https://arxiv.org/abs/2604.05489v2)**  
  Authors: Chengyi Yang, Pengzhen Li, Jiayin Qi, Aimin Zhou, Ji Wu, Ji Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.05489v2.pdf)  
  Keywords: evaluation, text-to-video, benchmark, video generation, diffusion model, dit, t2v  
- **[Generative AI for Video Trailer Synthesis: From Extractive Heuristics to Autoregressive Creativity](https://arxiv.org/abs/2604.04953v1)**  
  Authors: Abhishek Dharmaratnakar, Srivaths Ranganathan, Debanshu Das, Anushree Sinha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04953v1.pdf)  
  Keywords: autoregressive, survey, text-to-video, controllable, dit, video synthesis  
- **[SLVMEval: Synthetic Meta Evaluation Benchmark for Text-to-Long Video Generation](https://arxiv.org/abs/2603.29186v1)**  
  Authors: Ryosuke Matsuda, Keito Kudo, Haruto Yoshida, Nobuyuki Shimizu, Jun Suzuki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29186v1.pdf)  
  Keywords: evaluation, long video, text-to-video, benchmark, video generation, t2v  
- **[TokenDial: Continuous Attribute Control in Text-to-Video via Spatiotemporal Token Offsets](https://arxiv.org/abs/2603.27520v1)**  
  Authors: Zhixuan Liu, Peter Schaldenbrand, Yijun Li, Long Mai, Aniruddha Mahapatra, Cusuh Ham, Jean Oh, Jui-Hsien Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27520v1.pdf)  
  Keywords: evaluation, style, text-to-video, video generation, dit, dynamics, identity  
- **[LOME: Learning Human-Object Manipulation with Action-Conditioned Egocentric World Model](https://arxiv.org/abs/2603.27449v1)**  
  Authors: Quankai Gao, Jiawei Yang, Qiangeng Xu, Le Chen, Yue Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27449v1.pdf)  
  Keywords: world model, physics, temporal consistency, text-to-video, action-conditioned, motion control, physical, dit, gesture, t2v  
- **[EFlow: Fast Few-Step Video Generator Training from Scratch via Efficient Solution Flow](https://arxiv.org/abs/2603.27086v1)**  
  Authors: Dogyun Park, Yanyu Li, Sergey Tulyakov, Anil Kag  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27086v1.pdf)  
  Keywords: efficient, diffusion transformer, text-to-video, dit, video diffusion  

### Video Editing

- **[Lighting-grounded Video Generation with Renderer-based Agent Reasoning](https://arxiv.org/abs/2604.07966v1)**  
  Authors: Ziqi Cai, Taoyu Yang, Zheng Chang, Si Li, Han Jiang, Shuchen Weng, Boxin Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07966v1.pdf)  
  Keywords: layout, temporal consistency, controllable, video generation, diffusion model, video-to-video, trajectory, video synthesis, dit, film, image-to-video, video diffusion  
- **[ImVideoEdit: Image-learning Video Editing via 2D Spatial Difference Attention Blocks](https://arxiv.org/abs/2604.07958v1)**  
  Authors: Jiayang Xu, Fan Zhuo, Majun Zhang, Changhao Pan, Zehan Wang, Siyu Chen, Xiaoda Yang, Tao Jin, Zhou Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07958v1.pdf)  
  Keywords: efficient, temporal consistency, dit, dynamics, video editing  
- **[Evolution of Video Generative Foundations](https://arxiv.org/abs/2604.06339v1)**  
  Authors: Teng Hu, Jiangning Zhang, Hongrui Huang, Ran Yi, Zihan Su, Jieyu Weng, Zhucun Xue, Lizhuang Ma, Ming-Hsuan Yang, Dacheng Tao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06339v1.pdf) | [![GitHub](https://img.shields.io/github/stars/sjtuplayer/Awesome-Video-Foundations?style=social)](https://github.com/sjtuplayer/Awesome-Video-Foundations)  
  Keywords: education, world model, survey, video generation, diffusion model, dit, autonomous driving, simulation, dynamics, video editing  
- **[UENR-600K: A Large-Scale Physically Grounded Dataset for Nighttime Video Deraining](https://arxiv.org/abs/2604.04402v1)**  
  Authors: Pei Yang, Hai Ci, Beibei Lin, Yiren Song, Mike Zheng Shou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04402v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://showlab.github.io/UENR-600K)  
  Keywords: video generation, physical, video-to-video, benchmark  
- **[VOID: Video Object and Interaction Deletion](https://arxiv.org/abs/2604.02296v1)**  
  Authors: Saman Motamed, William Harvey, Benjamin Klein, Luc Van Gool, Zhuoning Yuan, Ta-Ying Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02296v1.pdf)  
  Keywords: physical, diffusion model, dit, dynamics, video diffusion, video editing  
- **[TrajectoryMover: Generative Movement of Object Trajectories in Videos](https://arxiv.org/abs/2603.29092v2)**  
  Authors: Kiran Chhatre, Hyeonho Jeong, Yulia Gryaditskaya, Christopher E. Peters, Chun-Hao Paul Huang, Paul Guerrero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29092v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://chhatrekiran.github.io/trajectorymover)  
  Keywords: dit, trajectory, video editing, identity  
- **[TRACE: Object Motion Editing in Videos with First-Frame Trajectory Guidance](https://arxiv.org/abs/2603.25707v1)**  
  Authors: Quynh Phung, Long Mai, Cusuh Ham, Feng Liu, Jia-Bin Huang, Aniruddha Mahapatra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25707v1.pdf)  
  Keywords: controllable, video-to-video, dit, image-to-video, trajectory, video editing  
- **[GaussFusion: Improving 3D Reconstruction in the Wild with A Geometry-Informed Video Generator](https://arxiv.org/abs/2603.25053v2)**  
  Authors: Liyuan Zhu, Manjunath Narayana, Michal Stary, Will Hutchcroft, Gordon Wetzstein, Iro Armeni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25053v2.pdf)  
  Keywords: efficient, interactive, benchmark, video generation, video-to-video  
- **[Accelerating Diffusion-based Video Editing via Heterogeneous Caching: Beyond Full Computing at Sampled Denoising Timestep](https://arxiv.org/abs/2603.24260v1)**  
  Authors: Tianyi Liu, Ye Lu, Linfeng Zhang, Chen Cai, Jianjun Gao, Yi Wang, Kim-Hui Yap, Lap-Pui Chau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24260v1.pdf)  
  Keywords: diffusion transformer, acceleration, video-to-video, dit, denoising, video diffusion, video editing  
- **[RealMaster: Lifting Rendered Scenes into Photorealistic Video](https://arxiv.org/abs/2603.23462v1)**  
  Authors: Dana Cohen-Bar, Ido Sobol, Raphael Bensadoun, Shelly Sheynin, Oran Gafni, Or Patashnik, Daniel Cohen-Or, Amit Zohar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23462v1.pdf)  
  Keywords: video generation, diffusion model, dit, dynamics, identity, video diffusion, video editing  

### Video Inpainting & Completion

- **[Novel View Synthesis as Video Completion](https://arxiv.org/abs/2604.08500v1)**  
  Authors: Qi Wu, Khiem Vuong, Minsik Jeon, Srinivasa Narasimhan, Deva Ramanan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08500v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://frame-crafter.github.io)  
  Keywords: benchmark, diffusion model, video completion, novel view, video diffusion  
- **[SEM-ROVER: Semantic Voxel-Guided Diffusion for Large-Scale Driving Scene Generation](https://arxiv.org/abs/2604.06113v1)**  
  Authors: Hiba Dahmani, Nathan Piasco, Moussab Bennehar, Luis Roldão, Dzmitry Tsishkou, Laurent Caraffa, Jean-Philippe Tarel, Roland Brémond  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06113v1.pdf)  
  Keywords: outpainting, diffusion model, dit  
- **[ChopGrad: Pixel-Wise Losses for Latent Video Diffusion via Truncated Backpropagation](https://arxiv.org/abs/2603.17812v2)**  
  Authors: Dmitriy Rivkin, Parker Ewen, Lili Gao, Julian Ost, Stefanie Walz, Rasika Kangutkar, Mario Bijelic, Felix Heide  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17812v2.pdf)  
  Keywords: video inpainting, efficient, video enhancement, latent video, video generation, diffusion model, dit, super-resolution, video diffusion  
- **[ConfCtrl: Enabling Precise Camera Control in Video Diffusion via Confidence-Aware Interpolation](https://arxiv.org/abs/2603.09819v1)**  
  Authors: Liudi Yang, George Eskandar, Fengyi Shen, Mohammad Altillawi, Yang Bai, Chi Zhang, Ziyuan Liu, Abhinav Valada  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09819v1.pdf)  
  Keywords: diffusion model, dit, camera control, novel view, video diffusion, video interpolation  
- **[Pinterest Canvas: Large-Scale Image Generation at Pinterest](https://arxiv.org/abs/2603.06453v1)**  
  Authors: Yu Wang, Eric Tzeng, Raymond Shiau, Jie Yang, Dmitry Kislyuk, Charles Rosenberg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06453v1.pdf)  
  Keywords: outpainting, video generation, diffusion model, dit, image-to-video  

### Video Super-Resolution & Enhancement

*Showing the latest 50 out of 61 papers*

- **[Beyond Few-Step Inference: Accelerating Video Diffusion Transformer Model Serving with Inter-Request Caching Reuse](https://arxiv.org/abs/2604.04451v1)**  
  Authors: Hao Liu, Ye Huang, Chenghuan Huang, Zhenyi Zheng, Jiangsu Du, Ziyang Ma, Jing Lyu, Yutong Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04451v1.pdf)  
  Keywords: diffusion transformer, video generation, diffusion model, dit, denoising, video diffusion  
- **[OP-GRPO: Efficient Off-Policy GRPO for Flow-Matching Models](https://arxiv.org/abs/2604.04142v1)**  
  Authors: Liyu Zhang, Kehan Li, Tingrui Han, Tao Zhao, Yuxuan Sheng, Shibo He, Chao Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04142v1.pdf)  
  Keywords: efficient, benchmark, video generation, dit, denoising  
- **[Salt: Self-Consistent Distribution Matching with Cache-Aware Training for Fast Video Generation](https://arxiv.org/abs/2604.03118v1)**  
  Authors: Xingtong Ge, Yi Zhang, Yushi Huang, Dailan He, Xiahong Wang, Bingqi Ma, Guanglu Song, Yu Liu, Jun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.03118v1.pdf) | [![GitHub](https://img.shields.io/github/stars/XingtongGe/Salt?style=social)](https://github.com/XingtongGe/Salt)  
  Keywords: autoregressive, style, video generation, dit, dynamics, denoising, trajectory, distillation  
- **[Not All Frames Deserve Full Computation: Accelerating Autoregressive Video Generation via Selective Computation and Predictive Extrapolation](https://arxiv.org/abs/2604.02979v1)**  
  Authors: Hanshuai Cui, Zhiqing Tang, Zhi Yao, Fanshuai Meng, Weijia Jia, Wei Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02979v1.pdf)  
  Keywords: autoregressive, efficient, long-form, acceleration, video generation, diffusion model, denoising, video diffusion  
- **[Can Video Diffusion Models Predict Past Frames? Bidirectional Cycle Consistency for Reversible Interpolation](https://arxiv.org/abs/2604.01700v1)**  
  Authors: Lingyu Liu, Yaxiong Wang, Li Zhu, Zhedong Zheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01700v1.pdf)  
  Keywords: architecture, frame interpolation, temporal consistency, diffusion model, dit, dynamics, video diffusion  
- **[From Understanding to Erasing: Towards Complete and Stable Video Object Removal](https://arxiv.org/abs/2604.01693v1)**  
  Authors: Dingming Liu, Wenjing Wang, Chen Li, Jing Lyu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01693v1.pdf) | [![GitHub](https://img.shields.io/github/stars/WeChatCV/UnderEraser?style=social)](https://github.com/WeChatCV/UnderEraser)  
  Keywords: temporal consistency, benchmark, physical, diffusion model, denoising, video diffusion, distillation  
- **[ZEUS: Accelerating Diffusion Models with Only Second-Order Predictor](https://arxiv.org/abs/2604.01552v1)**  
  Authors: Yixiao Wang, Ting Jiang, Zishan Shao, Hancheng Ye, Jingwei Sun, Mingyuan Ma, Jianyi Zhang, Yiran Chen, Hai Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01552v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Ting-Justin-Jiang/ZEUS?style=social)](https://github.com/Ting-Justin-Jiang/ZEUS)  
  Keywords: architecture, evaluation, acceleration, video generation, diffusion model, denoising, trajectory  
- **[Video Models Reason Early: Exploiting Plan Commitment for Maze Solving](https://arxiv.org/abs/2603.30043v1)**  
  Authors: Kaleb Newman, Tyler Zhu, Olga Russakovsky  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.30043v1.pdf)  
  Keywords: diffusion model, dynamics, denoising, trajectory, video diffusion  
- **[The Surprising Effectiveness of Noise Pretraining for Implicit Neural Representations](https://arxiv.org/abs/2603.29034v1)**  
  Authors: Kushal Vyas, Alper Kayabasi, Daniel Kim, Vishwanath Saragadam, Ashok Veeraraghavan, Guha Balakrishnan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29034v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kushalvyas.github.io/noisepretraining.html)  
  Keywords: denoising, efficient  
- **[Anti-I2V: Safeguarding your photos from malicious image-to-video generation](https://arxiv.org/abs/2603.24570v1)**  
  Authors: Duc Vu, Anh Nguyen, Chi Tran, Anh Tran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24570v1.pdf)  
  Keywords: architecture, temporal consistency, diffusion transformer, denoising, video generation, diffusion model, dit, human animation, i2v, image-to-video, video diffusion  

### World Models & Simulation

*Showing the latest 50 out of 89 papers*

- **[INSPATIO-WORLD: A Real-Time 4D World Simulator via Spatiotemporal Autoregressive Modeling](https://arxiv.org/abs/2604.07209v1)**  
  Authors: InSpatio Team, Donghui Shen, Guofeng Zhang, Haomin Liu, Haoyu Ji, Hujun Bao, Hongjia Zhai, Jialin Liu, Jing Guo, Nan Wang, Siji Pan, Weihong Pan, Weijian Xie, Xianbin Liu, Xiaojun Xiang, Xiaoyu Zhang, Xinyu Chen, Yifu Wang, Yipeng Chen, Zhenzhou Fan, Zhewen Le, Zhichao Ye, Ziqiang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07209v1.pdf)  
  Keywords: architecture, autoregressive, world model, world simulator, controllable, interactive, benchmark, video generation, physical, distillation  
- **[Grounded Forcing: Bridging Time-Independent Semantics and Proximal Dynamics in Autoregressive Video Synthesis](https://arxiv.org/abs/2604.06939v1)**  
  Authors: Jintao Chen, Chengyu Bai, Junjun hu, Xinda Xue, Mu Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06939v1.pdf)  
  Keywords: autoregressive, long-form, interactive, video synthesis, dynamics, identity  
- **[Evolution of Video Generative Foundations](https://arxiv.org/abs/2604.06339v1)**  
  Authors: Teng Hu, Jiangning Zhang, Hongrui Huang, Ran Yi, Zihan Su, Jieyu Weng, Zhucun Xue, Lizhuang Ma, Ming-Hsuan Yang, Dacheng Tao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06339v1.pdf) | [![GitHub](https://img.shields.io/github/stars/sjtuplayer/Awesome-Video-Foundations?style=social)](https://github.com/sjtuplayer/Awesome-Video-Foundations)  
  Keywords: education, world model, survey, video generation, diffusion model, dit, autonomous driving, simulation, dynamics, video editing  
- **[Action Images: End-to-End Policy Learning via Multiview Video Generation](https://arxiv.org/abs/2604.06168v1)**  
  Authors: Haoyu Zhen, Zixian Gao, Qiao Sun, Yilin Zhao, Yuncong Yang, Yilun Du, Tsun-Hsuan Wang, Yi-Ling Qiao, Chuang Gan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06168v1.pdf)  
  Keywords: world model, evaluation, action-conditioned, video generation, dit  
- **[DriveVA: Video Action Models are Zero-Shot Drivers](https://arxiv.org/abs/2604.04198v1)**  
  Authors: Mengmeng Liu, Diankun Zhang, Jiuming Liu, Jianfeng Cui, Hongwei Xie, Guang Chen, Hangjun Ye, Michael Ying Yang, Francesco Nex, Hao Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04198v1.pdf)  
  Keywords: world model, video generation, physical, dit, autonomous driving, dynamics, multi-modal, trajectory  
- **[CRAFT: Video Diffusion for Bimanual Robot Data Generation](https://arxiv.org/abs/2604.03552v1)**  
  Authors: Jason Chen, I-Chun Arthur Liu, Gaurav Sukhatme, Daniel Seita  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.03552v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://craftaug.github.io)  
  Keywords: diffusion transformer, video generation, physical, diffusion model, dit, simulation, trajectory, video diffusion  
- **[ActionParty: Multi-Subject Action Binding in Generative Video Games](https://arxiv.org/abs/2604.02330v1)**  
  Authors: Alexander Pondaven, Ziyi Wu, Igor Gilitschenski, Philip Torr, Sergey Tulyakov, Fabio Pizzati, Aliaksandr Siarohin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02330v1.pdf)  
  Keywords: autoregressive, world model, controllable, interactive, benchmark, diffusion model, identity, video diffusion  
- **[Resonance4D: Frequency-Domain Motion Supervision for Preset-Free Physical Parameter Learning in 4D Dynamic Physical Scene Simulation](https://arxiv.org/abs/2604.01994v1)**  
  Authors: Changshe Zhang, Jie Feng, Siyu Chen, Guanbin Li, Ronghua Shang, Junpeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01994v1.pdf)  
  Keywords: physics, physical, dynamics, simulation, video diffusion  
- **[DriveDreamer-Policy: A Geometry-Grounded World-Action Model for Unified Generation and Planning](https://arxiv.org/abs/2604.01765v1)**  
  Authors: Yang Zhou, Xiaofeng Wang, Hao Shao, Letian Wang, Guosheng Zhao, Jiangnan Shao, Jiagang Zhu, Tingdong Yu, Zheng Zhu, Guan Huang, Steven L. Waslander  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01765v1.pdf)  
  Keywords: architecture, world model, controllable, benchmark, video generation, physical  
- **[Control-DINO: Feature Space Conditioning for Controllable Image-to-Video Diffusion](https://arxiv.org/abs/2604.01761v1)**  
  Authors: Edoardo A. Dominici, Thomas Deixelberger, Konstantinos Vardis, Markus Steinberger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01761v1.pdf)  
  Keywords: architecture, style, controllable, diffusion model, dit, simulation, novel view, image-to-video, video diffusion  



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
