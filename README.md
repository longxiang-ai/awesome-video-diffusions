# Awesome Video Diffusions [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Video Diffusion Models and Video Generation. Content is automatically updated daily.

> Last Update: 2026-04-09 02:25:25

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

- [3D-aware Video Generation](#3d-aware-video-generation) (28 papers) - Video generation with 3D awareness, multi-view consistency, and 4D content creation
- [Applications](#applications) (42 papers) - Domain-specific applications of video diffusion models
- [Architecture & Efficiency](#architecture-&-efficiency) (356 papers) - Architectural innovations (DiT, UNet), flow matching, and training/inference efficiency
- [Audio & Multi-modal](#audio-&-multi-modal) (28 papers) - Audio-driven and multi-modal conditioned video generation
- [Controllable Generation](#controllable-generation) (138 papers) - Controllable video generation with motion, camera, pose, or layout guidance
- [Human & Character Animation](#human-&-character-animation) (28 papers) - Human-centric video generation including talking heads, dance, and character animation
- [Image-to-Video Generation](#image-to-video-generation) (41 papers) - Methods for animating still images into videos
- [Long Video Generation](#long-video-generation) (115 papers) - Generating temporally consistent long-form videos beyond short clips
- [Personalization & Customization](#personalization-&-customization) (86 papers) - Personalized video generation with custom subjects, identities, or styles
- [Physical Understanding](#physical-understanding) (144 papers) - Physics-aware video generation and dynamics modeling
- [Surveys & Benchmarks](#surveys-&-benchmarks) (197 papers) - Survey papers, benchmarks, and evaluation metrics for video generation
- [Text-to-Video Generation](#text-to-video-generation) (63 papers) - Foundation models and methods for generating videos from text prompts
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

- **[Multi-View Video Diffusion Policy: A 3D Spatio-Temporal-Aware Video Action Model](https://arxiv.org/abs/2604.03181v1)**  
  Authors: Peiyan Li, Yixiang Chen, Yuan Xu, Jiabing Yang, Xiangnan Wu, Jun Guo, Nan Sun, Long Qian, Xinghang Li, Xin Xiao, Jing Liu, Nianfeng Liu, Tao Kong, Yan Huang, Liang Wang, Tieniu Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.03181v1.pdf)  
  Keywords: efficient, dynamics, video diffusion, multi-view video, dit  
- **[Control-DINO: Feature Space Conditioning for Controllable Image-to-Video Diffusion](https://arxiv.org/abs/2604.01761v1)**  
  Authors: Edoardo A. Dominici, Thomas Deixelberger, Konstantinos Vardis, Markus Steinberger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01761v1.pdf)  
  Keywords: image-to-video, style, simulation, video diffusion, diffusion model, novel view, architecture, controllable, dit  
- **[HVG-3D: Bridging Real and Simulation Domains for 3D-Conditional Hand-Object Interaction Video Synthesis](https://arxiv.org/abs/2604.03305v1)**  
  Authors: Mingjin Chen, Junhao Chen, Zhaoxin Fan, Yujian Lee, Zichen Dang, Lili Wang, Yawen Cui, Lap-Pui Chau, Yi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.03305v1.pdf)  
  Keywords: video synthesis, video generation, simulation, 3d-aware, architecture, dit  
- **[I3DM: Implicit 3D-aware Memory Retrieval and Injection for Consistent Video Scene Generation](https://arxiv.org/abs/2603.23413v1)**  
  Authors: Jia Li, Han Yan, Yihang Chen, Siqi Li, Xibin Song, Yifu Wang, Jianfei Cai, Tien-Tsin Wong, Pan Ji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23413v1.pdf)  
  Keywords: video generation, camera control, 3d-aware, novel view, dit  
- **[GO-Renderer: Generative Object Rendering with 3D-aware Controllable Video Diffusion Models](https://arxiv.org/abs/2603.23246v1)**  
  Authors: Zekai Gu, Shuoxuan Feng, Yansong Wang, Hanzhuo Huang, Zhongshuo Du, Chengfeng Zhao, Chengwei Ren, Peng Wang, Yuan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23246v1.pdf)  
  Keywords: efficient, video diffusion, diffusion model, 3d-aware, controllable, dit  
- **[Omni-WorldBench: Towards a Comprehensive Interaction-Centric Evaluation for World Models](https://arxiv.org/abs/2603.22212v1)**  
  Authors: Meiqi Wu, Zhixin Cai, Fufangchen Zhao, Xiaokun Feng, Rujing Dang, Bingze Song, Ruitian Tian, Jiashu Zhu, Jiachen Lei, Hao Dou, Jing Tang, Lei Sun, Jiahong Wu, Xiangxiang Chu, Zeming Liu, Kaiqi Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22212v1.pdf)  
  Keywords: interactive, dynamics, video generation, world model, benchmark, 4d generation, evaluation  
- **[X-World: Controllable Ego-Centric Multi-Camera World Models for Scalable End-to-End Driving](https://arxiv.org/abs/2603.19979v2)**  
  Authors: Chaoda Zheng, Sean Li, Jinhao Deng, Zhennan Wang, Shijia Chen, Liqiang Xiao, Ziheng Chi, Hongbin Lin, Kangjie Chen, Boyang Wang, Yu Zhang, Xianming Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19979v2.pdf)  
  Keywords: world simulator, dynamics, latent video, style, action-conditioned, video generation, world model, simulation, video style transfer, autonomous driving, multi-view video, controllable, dit, evaluation  
- **[OrbitNVS: Harnessing Video Diffusion Priors for Novel View Synthesis](https://arxiv.org/abs/2603.19613v1)**  
  Authors: Jinglin Liang, Zijian Zhou, Rui Huang, Shuangping Huang, Yichen Gong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19613v1.pdf)  
  Keywords: video generation, camera control, video diffusion, benchmark, novel view  
- **[3DreamBooth: High-Fidelity 3D Subject-Driven Video Generation Model](https://arxiv.org/abs/2603.18524v1)**  
  Authors: Hyun-kyu Ko, Jihyeon Park, Younghyun Kim, Dongheok Park, Eunbyung Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18524v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ko-lani.github.io/3DreamBooth)  
  Keywords: identity, video generation, customization, subject-driven, novel view, 3d-aware, multi-view video, dit  
- **[TAPESTRY: From Geometry to Appearance via Consistent Turntable Videos](https://arxiv.org/abs/2603.17735v1)**  
  Authors: Yan Zeng, Haoran Jiang, Kaixin Yao, Qixuan Zhang, Longwen Zhang, Lan Xu, Jingyi Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17735v1.pdf)  
  Keywords: video generation, video diffusion, diffusion model, 3d-aware, multi-modal, dit  

### Applications

- **[Evolution of Video Generative Foundations](https://arxiv.org/abs/2604.06339v1)**  
  Authors: Teng Hu, Jiangning Zhang, Hongrui Huang, Ran Yi, Zihan Su, Jieyu Weng, Zhucun Xue, Lizhuang Ma, Ming-Hsuan Yang, Dacheng Tao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06339v1.pdf) | [![GitHub](https://img.shields.io/github/stars/sjtuplayer/Awesome-Video-Foundations?style=social)](https://github.com/sjtuplayer/Awesome-Video-Foundations)  
  Keywords: dynamics, autonomous driving, video generation, world model, simulation, diffusion model, survey, education, video editing, dit  
- **[OmniCamera: A Unified Framework for Multi-task Video Generation with Arbitrary Camera Control](https://arxiv.org/abs/2604.06010v1)**  
  Authors: Yukun Wang, Ruihuang Li, Jiale Tao, Shiyuan Yang, Liyi Chen, Zhantao Yang, Handz, Yulan Guo, Shuai Shao, Qinglin Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06010v1.pdf)  
  Keywords: video generation, camera control, creative, dit  
- **[DriveVA: Video Action Models are Zero-Shot Drivers](https://arxiv.org/abs/2604.04198v1)**  
  Authors: Mengmeng Liu, Diankun Zhang, Jiuming Liu, Jianfeng Cui, Hongwei Xie, Guang Chen, Hangjun Ye, Michael Ying Yang, Francesco Nex, Hao Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04198v1.pdf)  
  Keywords: dynamics, video generation, world model, trajectory, autonomous driving, multi-modal, physical, dit  
- **[ONE-SHOT: Compositional Human-Environment Video Synthesis via Spatial-Decoupled Motion Injection and Hybrid Context Integration](https://arxiv.org/abs/2604.01043v1)**  
  Authors: Fengyuan Yang, Luying Huang, Jiazhi Guan, Quanwei Yang, Dongwei Pan, Jianglin Fu, Haocheng Feng, Wei He, Kaisiyuan Wang, Hang Zhou, Angela Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01043v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://martayang.github.io/ONE-SHOT)  
  Keywords: efficient, dynamics, video synthesis, video generation, creative, dit  
- **[Collaborative AI Agents and Critics for Fault Detection and Cause Analysis in Network Telemetry](https://arxiv.org/abs/2604.00319v1)**  
  Authors: Syed Eqbal Alam, Zhan Shu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.00319v1.pdf)  
  Keywords: video generation, medical, evaluation  
- **[Face2Parts: Exploring Coarse-to-Fine Inter-Regional Facial Dependencies for Generalized Deepfake Detection](https://arxiv.org/abs/2603.26036v1)**  
  Authors: Kutub Uddin, Nusrat Tasnim, Byung Tae Oh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26036v1.pdf)  
  Keywords: benchmark, advertising  
- **[RefAlign: Representation Alignment for Reference-to-Video Generation](https://arxiv.org/abs/2603.25743v1)**  
  Authors: Lei Wang, YuXin Song, Ge Wu, Haocheng Feng, Hang Zhou, Jingdong Wang, Yaxing Wang, jian Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25743v1.pdf)  
  Keywords: identity, advertising, controllable, video synthesis, video generation, benchmark, virtual try-on, diffusion transformer, dit  
- **[AnyID: Ultra-Fidelity Universal Identity-Preserving Video Generation from Any Visual References](https://arxiv.org/abs/2603.25188v1)**  
  Authors: Jiahao Wang, Hualian Sheng, Sijia Cai, Yuxiao Yang, Weizhan Zhang, Caixia Yan, Bing Deng, Jieping Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25188v1.pdf)  
  Keywords: identity, video generation, creative, architecture, evaluation  
- **[DreamerAD: Efficient Reinforcement Learning via Latent World Model for Autonomous Driving](https://arxiv.org/abs/2603.24587v2)**  
  Authors: Pengxuan Yang, Yupeng Zheng, Deheng Qian, Zebin Xing, Qichao Zhang, Linbo Wang, Yichen Zhang, Shaoyu Guo, Zhongpu Xia, Qiang Chen, Junyu Han, Lingyun Xu, Yifeng Pan, Dongbin Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24587v2.pdf)  
  Keywords: efficient, video generation, world model, autonomous driving, autoregressive, physical, dit  
- **[Toward Physically Consistent Driving Video World Models under Challenging Trajectories](https://arxiv.org/abs/2603.24506v2)**  
  Authors: Jiawei Zhou, Zhenxin Zhu, Lingyi Du, Linye Lyu, Lijun Zhou, Zhanqian Wu, Hongcheng Luo, Zhuotao Tian, Bing Wang, Guang Chen, Hangjun Ye, Haiyang Sun, Yu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24506v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wm-research.github.io/PhyGenesis)  
  Keywords: dynamics, physics, video generation, world model, simulation, trajectory, autonomous driving, physical, dit  

### Architecture & Efficiency

*Showing the latest 50 out of 356 papers*

- **[INSPATIO-WORLD: A Real-Time 4D World Simulator via Spatiotemporal Autoregressive Modeling](https://arxiv.org/abs/2604.07209v1)**  
  Authors: InSpatio Team, Donghui Shen, Guofeng Zhang, Haomin Liu, Haoyu Ji, Hujun Bao, Hongjia Zhai, Jialin Liu, Jing Guo, Nan Wang, Siji Pan, Weihong Pan, Weijian Xie, Xianbin Liu, Xiaojun Xiang, Xiaoyu Zhang, Xinyu Chen, Yifu Wang, Yipeng Chen, Zhenzhou Fan, Zhewen Le, Zhichao Ye, Ziqiang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07209v1.pdf)  
  Keywords: world simulator, interactive, video generation, world model, distillation, benchmark, architecture, autoregressive, physical, controllable  
- **[Not all tokens contribute equally to diffusion learning](https://arxiv.org/abs/2604.07026v1)**  
  Authors: Guoqing Zhang, Lu Shi, Wanru Xu, Linna Zhang, Sen Wang, Fangfang Wang, Yigang Cen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07026v1.pdf)  
  Keywords: video generation, text-to-video, diffusion model, benchmark, dit  
- **[Controllable Generative Video Compression](https://arxiv.org/abs/2604.06655v1)**  
  Authors: Ding Ding, Daowen Li, Ying Chen, Yixin Gao, Ruixiao Dong, Kai Li, Li Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06655v1.pdf)  
  Keywords: video generation, controllable, dit  
- **[Evolution of Video Generative Foundations](https://arxiv.org/abs/2604.06339v1)**  
  Authors: Teng Hu, Jiangning Zhang, Hongrui Huang, Ran Yi, Zihan Su, Jieyu Weng, Zhucun Xue, Lizhuang Ma, Ming-Hsuan Yang, Dacheng Tao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06339v1.pdf) | [![GitHub](https://img.shields.io/github/stars/sjtuplayer/Awesome-Video-Foundations?style=social)](https://github.com/sjtuplayer/Awesome-Video-Foundations)  
  Keywords: dynamics, autonomous driving, video generation, world model, simulation, diffusion model, survey, education, video editing, dit  
- **[Action Images: End-to-End Policy Learning via Multiview Video Generation](https://arxiv.org/abs/2604.06168v1)**  
  Authors: Haoyu Zhen, Zixian Gao, Qiao Sun, Yilin Zhao, Yuncong Yang, Yilun Du, Tsun-Hsuan Wang, Yi-Ling Qiao, Chuang Gan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06168v1.pdf)  
  Keywords: action-conditioned, video generation, world model, dit, evaluation  
- **[SEM-ROVER: Semantic Voxel-Guided Diffusion for Large-Scale Driving Scene Generation](https://arxiv.org/abs/2604.06113v1)**  
  Authors: Hiba Dahmani, Nathan Piasco, Moussab Bennehar, Luis Roldão, Dzmitry Tsishkou, Laurent Caraffa, Jean-Philippe Tarel, Roland Brémond  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06113v1.pdf)  
  Keywords: outpainting, dit, diffusion model  
- **[OmniCamera: A Unified Framework for Multi-task Video Generation with Arbitrary Camera Control](https://arxiv.org/abs/2604.06010v1)**  
  Authors: Yukun Wang, Ruihuang Li, Jiale Tao, Shiyuan Yang, Liyi Chen, Zhantao Yang, Handz, Yulan Guo, Shuai Shao, Qinglin Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06010v1.pdf)  
  Keywords: video generation, camera control, creative, dit  
- **[HumANDiff: Articulated Noise Diffusion for Motion-Consistent Human Video Generation](https://arxiv.org/abs/2604.05961v1)**  
  Authors: Tao Hu, Varun Jampani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.05961v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://taohuumd.github.io/projects/HumANDiff)  
  Keywords: image-to-video, dynamics, style, video synthesis, video generation, human motion, motion control, physics, video diffusion, diffusion model, architecture, physical, controllable, dit  
- **[HybridKV: Hybrid KV Cache Compression for Efficient Multimodal Large Language Model Inference](https://arxiv.org/abs/2604.05887v1)**  
  Authors: Bowen Zeng, Feiyang Ren, Jun Zhang, Xiaoling Gu, Ke Chen, Lidan Shou, Huan Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.05887v1.pdf)  
  Keywords: efficient, benchmark  
- **[SCMAPR: Self-Correcting Multi-Agent Prompt Refinement for Complex-Scenario Text-to-Video Generation](https://arxiv.org/abs/2604.05489v1)**  
  Authors: Chengyi Yang, Pengzhen Li, Jiayin Qi, Aimin Zhou, Ji Wu, Ji Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.05489v1.pdf)  
  Keywords: video generation, text-to-video, diffusion model, t2v, benchmark, dit, evaluation  

### Audio & Multi-modal

- **[DriveVA: Video Action Models are Zero-Shot Drivers](https://arxiv.org/abs/2604.04198v1)**  
  Authors: Mengmeng Liu, Diankun Zhang, Jiuming Liu, Jianfeng Cui, Hongwei Xie, Guang Chen, Hangjun Ye, Michael Ying Yang, Francesco Nex, Hao Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04198v1.pdf)  
  Keywords: dynamics, video generation, world model, trajectory, autonomous driving, multi-modal, physical, dit  
- **[Beyond Static Vision: Scene Dynamic Field Unlocks Intuitive Physics Understanding in Multi-modal Large Language Models](https://arxiv.org/abs/2604.03302v1)**  
  Authors: Nanxi Li, Xiang Wang, Yuanjie Chen, Haode Zhang, Hong Li, Yong-Lu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.03302v1.pdf) | [![GitHub](https://img.shields.io/github/stars/andylinx/Scene-Dynamic-Field?style=social)](https://github.com/andylinx/Scene-Dynamic-Field)  
  Keywords: efficient, dynamics, physics, benchmark, multi-modal, physical  
- **[MoE-GRPO: Optimizing Mixture-of-Experts via Reinforcement Learning in Vision-Language Models](https://arxiv.org/abs/2603.24984v2)**  
  Authors: Dohwan Ko, Jinyoung Park, Seoung Choi, Sanghyeok Lee, Seohyun Lee, Hyunwoo J. Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24984v2.pdf)  
  Keywords: architecture, multi-modal, benchmark  
- **[Attention-aware Inference Optimizations for Large Vision-Language Models with Memory-efficient Decoding](https://arxiv.org/abs/2603.23914v1)**  
  Authors: Fatih Ilhan, Gaowen Liu, Ramana Rao Kompella, Selim Furkan Tekin, Tiansheng Huang, Zachary Yahn, Yichang Xu, Ling Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23914v1.pdf)  
  Keywords: efficient, multi-modal, benchmark  
- **[Mamba-VMR: Multimodal Query Augmentation via Generated Videos for Precise Temporal Grounding](https://arxiv.org/abs/2603.22121v1)**  
  Authors: Yunzhuo Sun, Xinyue Liu, Yanyang Li, Nanding Wu, Yifang Xu, Linlin Zong, Xianchao Zhang, Wenxin Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.22121v1.pdf)  
  Keywords: efficient, dynamics, text-to-video, benchmark, text-driven video, architecture, multi-modal, dit, evaluation  
- **[EARTalking: End-to-end GPT-style Autoregressive Talking Head Synthesis with Frame-wise Control](https://arxiv.org/abs/2603.20307v1)**  
  Authors: Yuzhe Weng, Haotian Wang, Yuanhong Yu, Jun Du, Shan He, Xiaoyan Wu, Haoran Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20307v1.pdf)  
  Keywords: interactive, efficient, identity, talking head, denoising, style, video generation, audio-driven, dit, autoregressive, streaming  
- **[Improving Joint Audio-Video Generation with Cross-Modal Context Learning](https://arxiv.org/abs/2603.18600v1)**  
  Authors: Bingqi Ma, Linlong Lang, Ming Zhang, Dailan He, Xingtong Ge, Yi Zhang, Guanglu Song, Yu Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18600v1.pdf)  
  Keywords: video generation, video diffusion, diffusion model, architecture, multi-modal, dit, evaluation  
- **[Insight-V++: Towards Advanced Long-Chain Visual Reasoning with Multimodal Large Language Models](https://arxiv.org/abs/2603.18118v1)**  
  Authors: Yuhao Dong, Zuyan Liu, Shulin Tian, Yongming Rao, Ziwei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.18118v1.pdf)  
  Keywords: architecture, multi-modal, benchmark, dit  
- **[TAPESTRY: From Geometry to Appearance via Consistent Turntable Videos](https://arxiv.org/abs/2603.17735v1)**  
  Authors: Yan Zeng, Haoran Jiang, Kaixin Yao, Qixuan Zhang, Longwen Zhang, Lan Xu, Jingyi Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17735v1.pdf)  
  Keywords: video generation, video diffusion, diffusion model, 3d-aware, multi-modal, dit  
- **[Bridging Scene Generation and Planning: Driving with World Model via Unifying Vision and Motion Representation](https://arxiv.org/abs/2603.14948v1)**  
  Authors: Xingtai Gui, Meijie Zhang, Tianyi Yan, Wencheng Han, Jiahao Gong, Feiyang Tan, Cheng-zhong Xu, Jianbing Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.14948v1.pdf)  
  Keywords: dynamics, video generation, world model, benchmark, trajectory, autonomous driving, multi-modal, dit  

### Controllable Generation

*Showing the latest 50 out of 138 papers*

- **[INSPATIO-WORLD: A Real-Time 4D World Simulator via Spatiotemporal Autoregressive Modeling](https://arxiv.org/abs/2604.07209v1)**  
  Authors: InSpatio Team, Donghui Shen, Guofeng Zhang, Haomin Liu, Haoyu Ji, Hujun Bao, Hongjia Zhai, Jialin Liu, Jing Guo, Nan Wang, Siji Pan, Weihong Pan, Weijian Xie, Xianbin Liu, Xiaojun Xiang, Xiaoyu Zhang, Xinyu Chen, Yifu Wang, Yipeng Chen, Zhenzhou Fan, Zhewen Le, Zhichao Ye, Ziqiang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07209v1.pdf)  
  Keywords: world simulator, interactive, video generation, world model, distillation, benchmark, architecture, autoregressive, physical, controllable  
- **[Controllable Generative Video Compression](https://arxiv.org/abs/2604.06655v1)**  
  Authors: Ding Ding, Daowen Li, Ying Chen, Yixin Gao, Ruixiao Dong, Kai Li, Li Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06655v1.pdf)  
  Keywords: video generation, controllable, dit  
- **[DiffHDR: Re-Exposing LDR Videos with Video Diffusion Models](https://arxiv.org/abs/2604.06161v1)**  
  Authors: Zhengming Yu, Li Ma, Mingming He, Leo Isikdogan, Yuancheng Xu, Dmitriy Smirnov, Pablo Salamanca, Dao Mi, Pablo Delgado, Ning Yu, Julien Philip, Xin Li, Wenping Wang, Paul Debevec  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06161v1.pdf)  
  Keywords: controllable, video diffusion, diffusion model  
- **[OmniCamera: A Unified Framework for Multi-task Video Generation with Arbitrary Camera Control](https://arxiv.org/abs/2604.06010v1)**  
  Authors: Yukun Wang, Ruihuang Li, Jiale Tao, Shiyuan Yang, Liyi Chen, Zhantao Yang, Handz, Yulan Guo, Shuai Shao, Qinglin Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06010v1.pdf)  
  Keywords: video generation, camera control, creative, dit  
- **[HumANDiff: Articulated Noise Diffusion for Motion-Consistent Human Video Generation](https://arxiv.org/abs/2604.05961v1)**  
  Authors: Tao Hu, Varun Jampani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.05961v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://taohuumd.github.io/projects/HumANDiff)  
  Keywords: image-to-video, dynamics, style, video synthesis, video generation, human motion, motion control, physics, video diffusion, diffusion model, architecture, physical, controllable, dit  
- **[DriveVA: Video Action Models are Zero-Shot Drivers](https://arxiv.org/abs/2604.04198v1)**  
  Authors: Mengmeng Liu, Diankun Zhang, Jiuming Liu, Jianfeng Cui, Hongwei Xie, Guang Chen, Hangjun Ye, Michael Ying Yang, Francesco Nex, Hao Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04198v1.pdf)  
  Keywords: dynamics, video generation, world model, trajectory, autonomous driving, multi-modal, physical, dit  
- **[SymphoMotion: Joint Control of Camera Motion and Object Dynamics for Coherent Video Generation](https://arxiv.org/abs/2604.03723v1)**  
  Authors: Guiyu Zhang, Yabo Chen, Xunzhi Xiang, Junchao Huang, Zhongyu Wang, Li Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.03723v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://grenoble-zhang.github.io/SymphoMotion)  
  Keywords: dynamics, video generation, camera control, motion control, benchmark, trajectory, evaluation  
- **[CRAFT: Video Diffusion for Bimanual Robot Data Generation](https://arxiv.org/abs/2604.03552v1)**  
  Authors: Jason Chen, I-Chun Arthur Liu, Gaurav Sukhatme, Daniel Seita  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.03552v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://craftaug.github.io)  
  Keywords: video generation, simulation, video diffusion, diffusion model, trajectory, physical, diffusion transformer, dit  
- **[Salt: Self-Consistent Distribution Matching with Cache-Aware Training for Fast Video Generation](https://arxiv.org/abs/2604.03118v1)**  
  Authors: Xingtong Ge, Yi Zhang, Yushi Huang, Dailan He, Xiahong Wang, Bingqi Ma, Guanglu Song, Yu Liu, Jun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.03118v1.pdf) | [![GitHub](https://img.shields.io/github/stars/XingtongGe/Salt?style=social)](https://github.com/XingtongGe/Salt)  
  Keywords: dynamics, denoising, style, video generation, distillation, trajectory, autoregressive, dit  
- **[NavCrafter: Exploring 3D Scenes from a Single Image](https://arxiv.org/abs/2604.02828v1)**  
  Authors: Hongbo Duan, Peiyu Zhuang, Yi Liu, Zhengyang Zhang, Yuxin Zhang, Pengting Luo, Fangming Liu, Xueqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02828v1.pdf)  
  Keywords: camera control, video diffusion, diffusion model, trajectory, controllable, dit  

### Human & Character Animation

- **[HumANDiff: Articulated Noise Diffusion for Motion-Consistent Human Video Generation](https://arxiv.org/abs/2604.05961v1)**  
  Authors: Tao Hu, Varun Jampani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.05961v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://taohuumd.github.io/projects/HumANDiff)  
  Keywords: image-to-video, dynamics, style, video synthesis, video generation, human motion, motion control, physics, video diffusion, diffusion model, architecture, physical, controllable, dit  
- **[Vanast: Virtual Try-On with Human Image Animation via Synthetic Triplet Supervision](https://arxiv.org/abs/2604.04934v1)**  
  Authors: Hyunsoo Cha, Wonjung Woo, Byungjun Kim, Hanbyul Joo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04934v1.pdf)  
  Keywords: identity, human animation, video diffusion, image animation, virtual try-on, architecture, diffusion transformer  
- **[DynaVid: Learning to Generate Highly Dynamic Videos using Synthetic Motion Data](https://arxiv.org/abs/2604.01666v1)**  
  Authors: Wonjoon Jin, Jiyun Won, Janghyeok Han, Qi Dai, Chong Luo, Seung-Hwan Baek, Sunghyun Cho  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01666v1.pdf)  
  Keywords: video synthesis, human motion, motion control, video diffusion, diffusion model, dit  
- **[FlashSign: Pose-Free Guidance for Efficient Sign Language Video Generation](https://arxiv.org/abs/2603.27915v1)**  
  Authors: Liuzhou Zhang, Zeyu Zhang, Biao Wu, Luyao Tang, Zirui Song, Hongyang He, Renda Han, Guangzhen Yao, Huacan Wang, Ronghao Chen, Xiuying Chen, Guan Huang, Zheng Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27915v1.pdf) | [![GitHub](https://img.shields.io/github/stars/AIGeeksGroup/FlashSign?style=social)](https://github.com/AIGeeksGroup/FlashSign)  
  Keywords: video generation, efficient, gesture  
- **[LOME: Learning Human-Object Manipulation with Action-Conditioned Egocentric World Model](https://arxiv.org/abs/2603.27449v1)**  
  Authors: Quankai Gao, Jiawei Yang, Qiangeng Xu, Le Chen, Yue Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27449v1.pdf)  
  Keywords: action-conditioned, physics, world model, motion control, gesture, text-to-video, temporal consistency, t2v, physical, dit  
- **[RefAlign: Representation Alignment for Reference-to-Video Generation](https://arxiv.org/abs/2603.25743v1)**  
  Authors: Lei Wang, YuXin Song, Ge Wu, Haocheng Feng, Hang Zhou, Jingdong Wang, Yaxing Wang, jian Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25743v1.pdf)  
  Keywords: identity, advertising, controllable, video synthesis, video generation, benchmark, virtual try-on, diffusion transformer, dit  
- **[Anti-I2V: Safeguarding your photos from malicious image-to-video generation](https://arxiv.org/abs/2603.24570v1)**  
  Authors: Duc Vu, Anh Nguyen, Chi Tran, Anh Tran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24570v1.pdf)  
  Keywords: image-to-video, i2v, human animation, denoising, video generation, video diffusion, diffusion model, temporal consistency, architecture, diffusion transformer, dit  
- **[Speed by Simplicity: A Single-Stream Architecture for Fast Audio-Video Generative Foundation Model](https://arxiv.org/abs/2603.21986v1)**  
  Authors: SII-GAIR, Sand. ai, :, Ethan Chern, Hansi Teng, Hanwen Sun, Hao Wang, Hong Pan, Hongyu Jia, Jiadi Su, Jin Li, Junjie Yu, Lijie Liu, Lingzhi Li, Lyumanshan Ye, Min Hu, Qiangang Wang, Quanwei Qi, Steffi Chern, Tao Bu, Taoran Wang, Teren Xu, Tianning Zhang, Tiantian Mi, Weixian Xu, Wenqiang Zhang, Wentai Zhang, Xianping Yi, Xiaojie Cai, Xiaoyang Kang, Yan Ma, Yixiu Liu, Yunbo Zhang, Yunpeng Huang, Yutong Lin, Zewei Tao, Zhaoliang Liu, Zheng Zhang, Zhiyao Cen, Zhixuan Yu, Zhongshu Wang, Zhulin Hu, Zijin Zhou, Zinan Guo, Yue Cao, Pengfei Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.21986v1.pdf)  
  Keywords: efficient, super-resolution, body motion, distillation, architecture, evaluation  
- **[EARTalking: End-to-end GPT-style Autoregressive Talking Head Synthesis with Frame-wise Control](https://arxiv.org/abs/2603.20307v1)**  
  Authors: Yuzhe Weng, Haotian Wang, Yuanhong Yu, Jun Du, Shan He, Xiaoyan Wu, Haoran Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.20307v1.pdf)  
  Keywords: interactive, efficient, identity, talking head, denoising, style, video generation, audio-driven, dit, autoregressive, streaming  
- **[AHOY! Animatable Humans under Occlusion from YouTube Videos with Gaussian Splatting and Video Diffusion Priors](https://arxiv.org/abs/2603.17975v1)**  
  Authors: Aymen Mir, Riza Alp Guler, Xiangjun Tang, Peter Wonka, Gerard Pons-Moll  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17975v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://miraymen.github.io/ahoy)  
  Keywords: avatar, identity, video diffusion, diffusion model, architecture  

### Image-to-Video Generation

- **[HumANDiff: Articulated Noise Diffusion for Motion-Consistent Human Video Generation](https://arxiv.org/abs/2604.05961v1)**  
  Authors: Tao Hu, Varun Jampani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.05961v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://taohuumd.github.io/projects/HumANDiff)  
  Keywords: image-to-video, dynamics, style, video synthesis, video generation, human motion, motion control, physics, video diffusion, diffusion model, architecture, physical, controllable, dit  
- **[Vanast: Virtual Try-On with Human Image Animation via Synthetic Triplet Supervision](https://arxiv.org/abs/2604.04934v1)**  
  Authors: Hyunsoo Cha, Wonjung Woo, Byungjun Kim, Hanbyul Joo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04934v1.pdf)  
  Keywords: identity, human animation, video diffusion, image animation, virtual try-on, architecture, diffusion transformer  
- **[Control-DINO: Feature Space Conditioning for Controllable Image-to-Video Diffusion](https://arxiv.org/abs/2604.01761v1)**  
  Authors: Edoardo A. Dominici, Thomas Deixelberger, Konstantinos Vardis, Markus Steinberger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01761v1.pdf)  
  Keywords: image-to-video, style, simulation, video diffusion, diffusion model, novel view, architecture, controllable, dit  
- **[Think over Trajectories: Leveraging Video Generation to Reconstruct GPS Trajectories from Cellular Signaling](https://arxiv.org/abs/2603.26610v1)**  
  Authors: Ruixing Zhang, Hanzhang Jiang, Leilei Sun, Liangzhe Han, Jibin Wang, Weifeng Lv  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26610v1.pdf)  
  Keywords: video generation, trajectory, dit, image-to-video  
- **[From Static to Dynamic: Exploring Self-supervised Image-to-Video Representation Transfer Learning](https://arxiv.org/abs/2603.26597v1)**  
  Authors: Yang Liu, Qianqian Xu, Peisong Wen, Siran Dai, Xilin Zhao, Qingming Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26597v1.pdf) | [![GitHub](https://img.shields.io/github/stars/yafeng19/Co-Settle?style=social)](https://github.com/yafeng19/Co-Settle)  
  Keywords: image-to-video, dit, temporal consistency  
- **[Generation Is Compression: Zero-Shot Video Coding via Stochastic Rectified Flow](https://arxiv.org/abs/2603.26571v2)**  
  Authors: Ziyue Zeng, Xun Su, Haoyuan Liu, Bingyu Lu, Yui Tatsumi, Hiroshi Watanabe  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26571v2.pdf)  
  Keywords: image-to-video, i2v, text-to-video, t2v, benchmark, trajectory, rectified flow, autoregressive, dit  
- **[IP-Bench: Benchmark for Image Protection Methods in Image-to-Video Generation Scenarios](https://arxiv.org/abs/2603.26154v1)**  
  Authors: Xiaofeng Li, Leyi Sheng, Zhen Sun, Zongmin Zhang, Jiaheng Wei, Xinlei He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26154v1.pdf)  
  Keywords: image-to-video, i2v, video generation, benchmark, evaluation  
- **[TRACE: Object Motion Editing in Videos with First-Frame Trajectory Guidance](https://arxiv.org/abs/2603.25707v1)**  
  Authors: Quynh Phung, Long Mai, Cusuh Ham, Feng Liu, Jia-Bin Huang, Aniruddha Mahapatra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25707v1.pdf)  
  Keywords: image-to-video, trajectory, video editing, controllable, dit, video-to-video  
- **[Anti-I2V: Safeguarding your photos from malicious image-to-video generation](https://arxiv.org/abs/2603.24570v1)**  
  Authors: Duc Vu, Anh Nguyen, Chi Tran, Anh Tran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24570v1.pdf)  
  Keywords: image-to-video, i2v, human animation, denoising, video generation, video diffusion, diffusion model, temporal consistency, architecture, diffusion transformer, dit  
- **[Leave No Stone Unturned: Uncovering Holistic Audio-Visual Intrinsic Coherence for Deepfake Detection](https://arxiv.org/abs/2603.23960v1)**  
  Authors: Jielun Peng, Yabin Wang, Yaqi Li, Long Kong, Xiaopeng Hong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23960v1.pdf) | [![GitHub](https://img.shields.io/github/stars/tuffy-studio/HAVIC?style=social)](https://github.com/tuffy-studio/HAVIC)  
  Keywords: image-to-video, benchmark, text-to-video, dit  

### Long Video Generation

*Showing the latest 50 out of 115 papers*

- **[INSPATIO-WORLD: A Real-Time 4D World Simulator via Spatiotemporal Autoregressive Modeling](https://arxiv.org/abs/2604.07209v1)**  
  Authors: InSpatio Team, Donghui Shen, Guofeng Zhang, Haomin Liu, Haoyu Ji, Hujun Bao, Hongjia Zhai, Jialin Liu, Jing Guo, Nan Wang, Siji Pan, Weihong Pan, Weijian Xie, Xianbin Liu, Xiaojun Xiang, Xiaoyu Zhang, Xinyu Chen, Yifu Wang, Yipeng Chen, Zhenzhou Fan, Zhewen Le, Zhichao Ye, Ziqiang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07209v1.pdf)  
  Keywords: world simulator, interactive, video generation, world model, distillation, benchmark, architecture, autoregressive, physical, controllable  
- **[Grounded Forcing: Bridging Time-Independent Semantics and Proximal Dynamics in Autoregressive Video Synthesis](https://arxiv.org/abs/2604.06939v1)**  
  Authors: Jintao Chen, Chengyu Bai, Junjun hu, Xinda Xue, Mu Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06939v1.pdf)  
  Keywords: interactive, dynamics, identity, video synthesis, autoregressive, long-form  
- **[Salt: Self-Consistent Distribution Matching with Cache-Aware Training for Fast Video Generation](https://arxiv.org/abs/2604.03118v1)**  
  Authors: Xingtong Ge, Yi Zhang, Yushi Huang, Dailan He, Xiahong Wang, Bingqi Ma, Guanglu Song, Yu Liu, Jun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.03118v1.pdf) | [![GitHub](https://img.shields.io/github/stars/XingtongGe/Salt?style=social)](https://github.com/XingtongGe/Salt)  
  Keywords: dynamics, denoising, style, video generation, distillation, trajectory, autoregressive, dit  
- **[Not All Frames Deserve Full Computation: Accelerating Autoregressive Video Generation via Selective Computation and Predictive Extrapolation](https://arxiv.org/abs/2604.02979v1)**  
  Authors: Hanshuai Cui, Zhiqing Tang, Zhi Yao, Fanshuai Meng, Weijia Jia, Wei Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02979v1.pdf)  
  Keywords: efficient, denoising, video generation, autoregressive, video diffusion, diffusion model, acceleration, long-form  
- **[Generative AI for Video Trailer Synthesis: From Extractive Heuristics to Autoregressive Creativity](https://arxiv.org/abs/2604.04953v1)**  
  Authors: Abhishek Dharmaratnakar, Srivaths Ranganathan, Debanshu Das, Anushree Sinha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04953v1.pdf)  
  Keywords: video synthesis, text-to-video, survey, autoregressive, controllable, dit  
- **[ActionParty: Multi-Subject Action Binding in Generative Video Games](https://arxiv.org/abs/2604.02330v1)**  
  Authors: Alexander Pondaven, Ziyi Wu, Igor Gilitschenski, Philip Torr, Sergey Tulyakov, Fabio Pizzati, Aliaksandr Siarohin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02330v1.pdf)  
  Keywords: interactive, identity, world model, video diffusion, diffusion model, benchmark, autoregressive, controllable  
- **[Generative World Renderer](https://arxiv.org/abs/2604.02329v1)**  
  Authors: Zheng-Hui Huang, Zhixiang Wang, Jiaming Tan, Ruihan Yu, Yidan Zhang, Bo Zheng, Yu-Lun Liu, Yung-Yu Chuang, Kaipeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02329v1.pdf)  
  Keywords: style, video generation, temporal consistency, controllable, dit, evaluation  
- **[Can Video Diffusion Models Predict Past Frames? Bidirectional Cycle Consistency for Reversible Interpolation](https://arxiv.org/abs/2604.01700v1)**  
  Authors: Lingyu Liu, Yaxiong Wang, Li Zhu, Zhedong Zheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01700v1.pdf)  
  Keywords: dynamics, frame interpolation, temporal consistency, video diffusion, diffusion model, architecture, dit  
- **[From Understanding to Erasing: Towards Complete and Stable Video Object Removal](https://arxiv.org/abs/2604.01693v1)**  
  Authors: Dingming Liu, Wenjing Wang, Chen Li, Jing Lyu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01693v1.pdf) | [![GitHub](https://img.shields.io/github/stars/WeChatCV/UnderEraser?style=social)](https://github.com/WeChatCV/UnderEraser)  
  Keywords: denoising, temporal consistency, video diffusion, diffusion model, distillation, benchmark, physical  
- **[TRACE: High-Fidelity 3D Scene Editing via Tangible Reconstruction and Geometry-Aligned Contextual Video Masking](https://arxiv.org/abs/2604.01207v1)**  
  Authors: Jiyuan Hu, Zechuan Zhang, Zongxin Yang, Yi Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01207v1.pdf)  
  Keywords: autoregressive, dit, physical, video diffusion  

### Personalization & Customization

*Showing the latest 50 out of 86 papers*

- **[Grounded Forcing: Bridging Time-Independent Semantics and Proximal Dynamics in Autoregressive Video Synthesis](https://arxiv.org/abs/2604.06939v1)**  
  Authors: Jintao Chen, Chengyu Bai, Junjun hu, Xinda Xue, Mu Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06939v1.pdf)  
  Keywords: interactive, dynamics, identity, video synthesis, autoregressive, long-form  
- **[HumANDiff: Articulated Noise Diffusion for Motion-Consistent Human Video Generation](https://arxiv.org/abs/2604.05961v1)**  
  Authors: Tao Hu, Varun Jampani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.05961v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://taohuumd.github.io/projects/HumANDiff)  
  Keywords: image-to-video, dynamics, style, video synthesis, video generation, human motion, motion control, physics, video diffusion, diffusion model, architecture, physical, controllable, dit  
- **[Vanast: Virtual Try-On with Human Image Animation via Synthetic Triplet Supervision](https://arxiv.org/abs/2604.04934v1)**  
  Authors: Hyunsoo Cha, Wonjung Woo, Byungjun Kim, Hanbyul Joo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04934v1.pdf)  
  Keywords: identity, human animation, video diffusion, image animation, virtual try-on, architecture, diffusion transformer  
- **[Salt: Self-Consistent Distribution Matching with Cache-Aware Training for Fast Video Generation](https://arxiv.org/abs/2604.03118v1)**  
  Authors: Xingtong Ge, Yi Zhang, Yushi Huang, Dailan He, Xiahong Wang, Bingqi Ma, Guanglu Song, Yu Liu, Jun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.03118v1.pdf) | [![GitHub](https://img.shields.io/github/stars/XingtongGe/Salt?style=social)](https://github.com/XingtongGe/Salt)  
  Keywords: dynamics, denoising, style, video generation, distillation, trajectory, autoregressive, dit  
- **[HairOrbit: Multi-view Aware 3D Hair Modeling from Single Portraits](https://arxiv.org/abs/2604.02867v1)**  
  Authors: Leyang Jin, Yujian Zheng, Bingkui Tong, Yuda Qiu, Zhenyu Xie, Hao Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02867v1.pdf)  
  Keywords: video generation, style, dit  
- **[ActionParty: Multi-Subject Action Binding in Generative Video Games](https://arxiv.org/abs/2604.02330v1)**  
  Authors: Alexander Pondaven, Ziyi Wu, Igor Gilitschenski, Philip Torr, Sergey Tulyakov, Fabio Pizzati, Aliaksandr Siarohin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02330v1.pdf)  
  Keywords: interactive, identity, world model, video diffusion, diffusion model, benchmark, autoregressive, controllable  
- **[Generative World Renderer](https://arxiv.org/abs/2604.02329v1)**  
  Authors: Zheng-Hui Huang, Zhixiang Wang, Jiaming Tan, Ruihan Yu, Yidan Zhang, Bo Zheng, Yu-Lun Liu, Yung-Yu Chuang, Kaipeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02329v1.pdf)  
  Keywords: style, video generation, temporal consistency, controllable, dit, evaluation  
- **[Control-DINO: Feature Space Conditioning for Controllable Image-to-Video Diffusion](https://arxiv.org/abs/2604.01761v1)**  
  Authors: Edoardo A. Dominici, Thomas Deixelberger, Konstantinos Vardis, Markus Steinberger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01761v1.pdf)  
  Keywords: image-to-video, style, simulation, video diffusion, diffusion model, novel view, architecture, controllable, dit  
- **[Gloria: Consistent Character Video Generation via Content Anchors](https://arxiv.org/abs/2603.29931v1)**  
  Authors: Yuhang Yang, Fan Zhang, Huaijin Pi, Shuai Guo, Guowei Xu, Wei Zhai, Yang Cao, Zheng-Jun Zha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29931v1.pdf)  
  Keywords: video generation, identity, dit  
- **[TrajectoryMover: Generative Movement of Object Trajectories in Videos](https://arxiv.org/abs/2603.29092v2)**  
  Authors: Kiran Chhatre, Hyeonho Jeong, Yulia Gryaditskaya, Christopher E. Peters, Chun-Hao Paul Huang, Paul Guerrero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29092v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://chhatrekiran.github.io/trajectorymover)  
  Keywords: video editing, identity, trajectory, dit  

### Physical Understanding

*Showing the latest 50 out of 144 papers*

- **[INSPATIO-WORLD: A Real-Time 4D World Simulator via Spatiotemporal Autoregressive Modeling](https://arxiv.org/abs/2604.07209v1)**  
  Authors: InSpatio Team, Donghui Shen, Guofeng Zhang, Haomin Liu, Haoyu Ji, Hujun Bao, Hongjia Zhai, Jialin Liu, Jing Guo, Nan Wang, Siji Pan, Weihong Pan, Weijian Xie, Xianbin Liu, Xiaojun Xiang, Xiaoyu Zhang, Xinyu Chen, Yifu Wang, Yipeng Chen, Zhenzhou Fan, Zhewen Le, Zhichao Ye, Ziqiang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07209v1.pdf)  
  Keywords: world simulator, interactive, video generation, world model, distillation, benchmark, architecture, autoregressive, physical, controllable  
- **[Grounded Forcing: Bridging Time-Independent Semantics and Proximal Dynamics in Autoregressive Video Synthesis](https://arxiv.org/abs/2604.06939v1)**  
  Authors: Jintao Chen, Chengyu Bai, Junjun hu, Xinda Xue, Mu Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06939v1.pdf)  
  Keywords: interactive, dynamics, identity, video synthesis, autoregressive, long-form  
- **[Evolution of Video Generative Foundations](https://arxiv.org/abs/2604.06339v1)**  
  Authors: Teng Hu, Jiangning Zhang, Hongrui Huang, Ran Yi, Zihan Su, Jieyu Weng, Zhucun Xue, Lizhuang Ma, Ming-Hsuan Yang, Dacheng Tao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06339v1.pdf) | [![GitHub](https://img.shields.io/github/stars/sjtuplayer/Awesome-Video-Foundations?style=social)](https://github.com/sjtuplayer/Awesome-Video-Foundations)  
  Keywords: dynamics, autonomous driving, video generation, world model, simulation, diffusion model, survey, education, video editing, dit  
- **[HumANDiff: Articulated Noise Diffusion for Motion-Consistent Human Video Generation](https://arxiv.org/abs/2604.05961v1)**  
  Authors: Tao Hu, Varun Jampani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.05961v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://taohuumd.github.io/projects/HumANDiff)  
  Keywords: image-to-video, dynamics, style, video synthesis, video generation, human motion, motion control, physics, video diffusion, diffusion model, architecture, physical, controllable, dit  
- **[UENR-600K: A Large-Scale Physically Grounded Dataset for Nighttime Video Deraining](https://arxiv.org/abs/2604.04402v1)**  
  Authors: Pei Yang, Hai Ci, Beibei Lin, Yiren Song, Mike Zheng Shou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04402v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://showlab.github.io/UENR-600K)  
  Keywords: video generation, benchmark, physical, video-to-video  
- **[DriveVA: Video Action Models are Zero-Shot Drivers](https://arxiv.org/abs/2604.04198v1)**  
  Authors: Mengmeng Liu, Diankun Zhang, Jiuming Liu, Jianfeng Cui, Hongwei Xie, Guang Chen, Hangjun Ye, Michael Ying Yang, Francesco Nex, Hao Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04198v1.pdf)  
  Keywords: dynamics, video generation, world model, trajectory, autonomous driving, multi-modal, physical, dit  
- **[ATSS: Detecting AI-Generated Videos via Anomalous Temporal Self-Similarity](https://arxiv.org/abs/2604.04029v1)**  
  Authors: Hang Wang, Chao Shen, Lei Zhang, Zhi-Qi Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04029v1.pdf) | [![GitHub](https://img.shields.io/github/stars/hwang-cs-ime/ATSS?style=social)](https://github.com/hwang-cs-ime/ATSS)  
  Keywords: video generation, dynamics, benchmark  
- **[SymphoMotion: Joint Control of Camera Motion and Object Dynamics for Coherent Video Generation](https://arxiv.org/abs/2604.03723v1)**  
  Authors: Guiyu Zhang, Yabo Chen, Xunzhi Xiang, Junchao Huang, Zhongyu Wang, Li Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.03723v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://grenoble-zhang.github.io/SymphoMotion)  
  Keywords: dynamics, video generation, camera control, motion control, benchmark, trajectory, evaluation  
- **[CRAFT: Video Diffusion for Bimanual Robot Data Generation](https://arxiv.org/abs/2604.03552v1)**  
  Authors: Jason Chen, I-Chun Arthur Liu, Gaurav Sukhatme, Daniel Seita  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.03552v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://craftaug.github.io)  
  Keywords: video generation, simulation, video diffusion, diffusion model, trajectory, physical, diffusion transformer, dit  
- **[Multi-View Video Diffusion Policy: A 3D Spatio-Temporal-Aware Video Action Model](https://arxiv.org/abs/2604.03181v1)**  
  Authors: Peiyan Li, Yixiang Chen, Yuan Xu, Jiabing Yang, Xiangnan Wu, Jun Guo, Nan Sun, Long Qian, Xinghang Li, Xin Xiao, Jing Liu, Nianfeng Liu, Tao Kong, Yan Huang, Liang Wang, Tieniu Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.03181v1.pdf)  
  Keywords: efficient, dynamics, video diffusion, multi-view video, dit  

### Surveys & Benchmarks

*Showing the latest 50 out of 197 papers*

- **[INSPATIO-WORLD: A Real-Time 4D World Simulator via Spatiotemporal Autoregressive Modeling](https://arxiv.org/abs/2604.07209v1)**  
  Authors: InSpatio Team, Donghui Shen, Guofeng Zhang, Haomin Liu, Haoyu Ji, Hujun Bao, Hongjia Zhai, Jialin Liu, Jing Guo, Nan Wang, Siji Pan, Weihong Pan, Weijian Xie, Xianbin Liu, Xiaojun Xiang, Xiaoyu Zhang, Xinyu Chen, Yifu Wang, Yipeng Chen, Zhenzhou Fan, Zhewen Le, Zhichao Ye, Ziqiang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07209v1.pdf)  
  Keywords: world simulator, interactive, video generation, world model, distillation, benchmark, architecture, autoregressive, physical, controllable  
- **[Not all tokens contribute equally to diffusion learning](https://arxiv.org/abs/2604.07026v1)**  
  Authors: Guoqing Zhang, Lu Shi, Wanru Xu, Linna Zhang, Sen Wang, Fangfang Wang, Yigang Cen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07026v1.pdf)  
  Keywords: video generation, text-to-video, diffusion model, benchmark, dit  
- **[Evolution of Video Generative Foundations](https://arxiv.org/abs/2604.06339v1)**  
  Authors: Teng Hu, Jiangning Zhang, Hongrui Huang, Ran Yi, Zihan Su, Jieyu Weng, Zhucun Xue, Lizhuang Ma, Ming-Hsuan Yang, Dacheng Tao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06339v1.pdf) | [![GitHub](https://img.shields.io/github/stars/sjtuplayer/Awesome-Video-Foundations?style=social)](https://github.com/sjtuplayer/Awesome-Video-Foundations)  
  Keywords: dynamics, autonomous driving, video generation, world model, simulation, diffusion model, survey, education, video editing, dit  
- **[Action Images: End-to-End Policy Learning via Multiview Video Generation](https://arxiv.org/abs/2604.06168v1)**  
  Authors: Haoyu Zhen, Zixian Gao, Qiao Sun, Yilin Zhao, Yuncong Yang, Yilun Du, Tsun-Hsuan Wang, Yi-Ling Qiao, Chuang Gan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06168v1.pdf)  
  Keywords: action-conditioned, video generation, world model, dit, evaluation  
- **[HybridKV: Hybrid KV Cache Compression for Efficient Multimodal Large Language Model Inference](https://arxiv.org/abs/2604.05887v1)**  
  Authors: Bowen Zeng, Feiyang Ren, Jun Zhang, Xiaoling Gu, Ke Chen, Lidan Shou, Huan Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.05887v1.pdf)  
  Keywords: efficient, benchmark  
- **[SCMAPR: Self-Correcting Multi-Agent Prompt Refinement for Complex-Scenario Text-to-Video Generation](https://arxiv.org/abs/2604.05489v1)**  
  Authors: Chengyi Yang, Pengzhen Li, Jiayin Qi, Aimin Zhou, Ji Wu, Ji Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.05489v1.pdf)  
  Keywords: video generation, text-to-video, diffusion model, t2v, benchmark, dit, evaluation  
- **[Preserving Forgery Artifacts: AI-Generated Video Detection at Native Scale](https://arxiv.org/abs/2604.04634v1)**  
  Authors: Zhengcen Li, Chenyang Jiang, Hang Zhao, Shiyang Zhou, Yunyang Mo, Feng Gao, Fan Yang, Qiben Shan, Shaocong Wu, Jingyong Su  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04634v1.pdf)  
  Keywords: video generation, benchmark, dit  
- **[UENR-600K: A Large-Scale Physically Grounded Dataset for Nighttime Video Deraining](https://arxiv.org/abs/2604.04402v1)**  
  Authors: Pei Yang, Hai Ci, Beibei Lin, Yiren Song, Mike Zheng Shou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04402v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://showlab.github.io/UENR-600K)  
  Keywords: video generation, benchmark, physical, video-to-video  
- **[OP-GRPO: Efficient Off-Policy GRPO for Flow-Matching Models](https://arxiv.org/abs/2604.04142v1)**  
  Authors: Liyu Zhang, Kehan Li, Tingrui Han, Tao Zhao, Yuxuan Sheng, Shibo He, Chao Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04142v1.pdf)  
  Keywords: efficient, denoising, video generation, benchmark, dit  
- **[ATSS: Detecting AI-Generated Videos via Anomalous Temporal Self-Similarity](https://arxiv.org/abs/2604.04029v1)**  
  Authors: Hang Wang, Chao Shen, Lei Zhang, Zhi-Qi Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04029v1.pdf) | [![GitHub](https://img.shields.io/github/stars/hwang-cs-ime/ATSS?style=social)](https://github.com/hwang-cs-ime/ATSS)  
  Keywords: video generation, dynamics, benchmark  

### Text-to-Video Generation

*Showing the latest 50 out of 63 papers*

- **[Not all tokens contribute equally to diffusion learning](https://arxiv.org/abs/2604.07026v1)**  
  Authors: Guoqing Zhang, Lu Shi, Wanru Xu, Linna Zhang, Sen Wang, Fangfang Wang, Yigang Cen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07026v1.pdf)  
  Keywords: video generation, text-to-video, diffusion model, benchmark, dit  
- **[SCMAPR: Self-Correcting Multi-Agent Prompt Refinement for Complex-Scenario Text-to-Video Generation](https://arxiv.org/abs/2604.05489v1)**  
  Authors: Chengyi Yang, Pengzhen Li, Jiayin Qi, Aimin Zhou, Ji Wu, Ji Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.05489v1.pdf)  
  Keywords: video generation, text-to-video, diffusion model, t2v, benchmark, dit, evaluation  
- **[Generative AI for Video Trailer Synthesis: From Extractive Heuristics to Autoregressive Creativity](https://arxiv.org/abs/2604.04953v1)**  
  Authors: Abhishek Dharmaratnakar, Srivaths Ranganathan, Debanshu Das, Anushree Sinha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04953v1.pdf)  
  Keywords: video synthesis, text-to-video, survey, autoregressive, controllable, dit  
- **[SLVMEval: Synthetic Meta Evaluation Benchmark for Text-to-Long Video Generation](https://arxiv.org/abs/2603.29186v1)**  
  Authors: Ryosuke Matsuda, Keito Kudo, Haruto Yoshida, Nobuyuki Shimizu, Jun Suzuki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29186v1.pdf)  
  Keywords: video generation, long video, text-to-video, t2v, benchmark, evaluation  
- **[TokenDial: Continuous Attribute Control in Text-to-Video via Spatiotemporal Token Offsets](https://arxiv.org/abs/2603.27520v1)**  
  Authors: Zhixuan Liu, Peter Schaldenbrand, Yijun Li, Long Mai, Aniruddha Mahapatra, Cusuh Ham, Jean Oh, Jui-Hsien Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27520v1.pdf)  
  Keywords: dynamics, identity, style, video generation, text-to-video, dit, evaluation  
- **[LOME: Learning Human-Object Manipulation with Action-Conditioned Egocentric World Model](https://arxiv.org/abs/2603.27449v1)**  
  Authors: Quankai Gao, Jiawei Yang, Qiangeng Xu, Le Chen, Yue Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27449v1.pdf)  
  Keywords: action-conditioned, physics, world model, motion control, gesture, text-to-video, temporal consistency, t2v, physical, dit  
- **[EFlow: Fast Few-Step Video Generator Training from Scratch via Efficient Solution Flow](https://arxiv.org/abs/2603.27086v1)**  
  Authors: Dogyun Park, Yanyu Li, Sergey Tulyakov, Anil Kag  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27086v1.pdf)  
  Keywords: efficient, text-to-video, video diffusion, diffusion transformer, dit  
- **[Generation Is Compression: Zero-Shot Video Coding via Stochastic Rectified Flow](https://arxiv.org/abs/2603.26571v2)**  
  Authors: Ziyue Zeng, Xun Su, Haoyuan Liu, Bingyu Lu, Yui Tatsumi, Hiroshi Watanabe  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.26571v2.pdf)  
  Keywords: image-to-video, i2v, text-to-video, t2v, benchmark, trajectory, rectified flow, autoregressive, dit  
- **[THFM: A Unified Video Foundation Model for 4D Human Perception and Beyond](https://arxiv.org/abs/2603.25892v1)**  
  Authors: Letian Wang, Andrei Zanfir, Eduard Gabriel Bazavan, Misha Andriluka, Cristian Sminchisescu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25892v1.pdf)  
  Keywords: text-to-video, video diffusion, diffusion model, benchmark, architecture  
- **[ShotStream: Streaming Multi-Shot Video Generation for Interactive Storytelling](https://arxiv.org/abs/2603.25746v1)**  
  Authors: Yawen Luo, Xiaoyu Shi, Junhao Zhuang, Yutian Chen, Quande Liu, Xintao Wang, Pengfei Wan, Tianfan Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25746v1.pdf)  
  Keywords: interactive, efficient, video generation, text-to-video, distillation, dit, architecture, autoregressive, streaming  

### Video Editing

- **[Evolution of Video Generative Foundations](https://arxiv.org/abs/2604.06339v1)**  
  Authors: Teng Hu, Jiangning Zhang, Hongrui Huang, Ran Yi, Zihan Su, Jieyu Weng, Zhucun Xue, Lizhuang Ma, Ming-Hsuan Yang, Dacheng Tao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06339v1.pdf) | [![GitHub](https://img.shields.io/github/stars/sjtuplayer/Awesome-Video-Foundations?style=social)](https://github.com/sjtuplayer/Awesome-Video-Foundations)  
  Keywords: dynamics, autonomous driving, video generation, world model, simulation, diffusion model, survey, education, video editing, dit  
- **[UENR-600K: A Large-Scale Physically Grounded Dataset for Nighttime Video Deraining](https://arxiv.org/abs/2604.04402v1)**  
  Authors: Pei Yang, Hai Ci, Beibei Lin, Yiren Song, Mike Zheng Shou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04402v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://showlab.github.io/UENR-600K)  
  Keywords: video generation, benchmark, physical, video-to-video  
- **[VOID: Video Object and Interaction Deletion](https://arxiv.org/abs/2604.02296v1)**  
  Authors: Saman Motamed, William Harvey, Benjamin Klein, Luc Van Gool, Zhuoning Yuan, Ta-Ying Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02296v1.pdf)  
  Keywords: dynamics, video diffusion, diffusion model, video editing, physical, dit  
- **[TrajectoryMover: Generative Movement of Object Trajectories in Videos](https://arxiv.org/abs/2603.29092v2)**  
  Authors: Kiran Chhatre, Hyeonho Jeong, Yulia Gryaditskaya, Christopher E. Peters, Chun-Hao Paul Huang, Paul Guerrero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29092v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://chhatrekiran.github.io/trajectorymover)  
  Keywords: video editing, identity, trajectory, dit  
- **[TRACE: Object Motion Editing in Videos with First-Frame Trajectory Guidance](https://arxiv.org/abs/2603.25707v1)**  
  Authors: Quynh Phung, Long Mai, Cusuh Ham, Feng Liu, Jia-Bin Huang, Aniruddha Mahapatra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25707v1.pdf)  
  Keywords: image-to-video, trajectory, video editing, controllable, dit, video-to-video  
- **[GaussFusion: Improving 3D Reconstruction in the Wild with A Geometry-Informed Video Generator](https://arxiv.org/abs/2603.25053v2)**  
  Authors: Liyuan Zhu, Manjunath Narayana, Michal Stary, Will Hutchcroft, Gordon Wetzstein, Iro Armeni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25053v2.pdf)  
  Keywords: interactive, efficient, video generation, benchmark, video-to-video  
- **[Accelerating Diffusion-based Video Editing via Heterogeneous Caching: Beyond Full Computing at Sampled Denoising Timestep](https://arxiv.org/abs/2603.24260v1)**  
  Authors: Tianyi Liu, Ye Lu, Linfeng Zhang, Chen Cai, Jianjun Gao, Yi Wang, Kim-Hui Yap, Lap-Pui Chau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24260v1.pdf)  
  Keywords: denoising, video diffusion, acceleration, video editing, diffusion transformer, dit, video-to-video  
- **[RealMaster: Lifting Rendered Scenes into Photorealistic Video](https://arxiv.org/abs/2603.23462v1)**  
  Authors: Dana Cohen-Bar, Ido Sobol, Raphael Bensadoun, Shelly Sheynin, Oran Gafni, Or Patashnik, Daniel Cohen-Or, Amit Zohar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23462v1.pdf)  
  Keywords: dynamics, identity, video generation, video diffusion, diffusion model, video editing, dit  
- **[X-World: Controllable Ego-Centric Multi-Camera World Models for Scalable End-to-End Driving](https://arxiv.org/abs/2603.19979v2)**  
  Authors: Chaoda Zheng, Sean Li, Jinhao Deng, Zhennan Wang, Shijia Chen, Liqiang Xiao, Ziheng Chi, Hongbin Lin, Kangjie Chen, Boyang Wang, Yu Zhang, Xianming Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.19979v2.pdf)  
  Keywords: world simulator, dynamics, latent video, style, action-conditioned, video generation, world model, simulation, video style transfer, autonomous driving, multi-view video, controllable, dit, evaluation  
- **[Versatile Editing of Video Content, Actions, and Dynamics without Training](https://arxiv.org/abs/2603.17989v1)**  
  Authors: Vladimir Kulikov, Roni Paiss, Andrey Voynov, Inbar Mosseri, Tali Dekel, Tomer Michaeli  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17989v1.pdf)  
  Keywords: dynamics, video generation, text-to-video, video editing, dit  

### Video Inpainting & Completion

- **[SEM-ROVER: Semantic Voxel-Guided Diffusion for Large-Scale Driving Scene Generation](https://arxiv.org/abs/2604.06113v1)**  
  Authors: Hiba Dahmani, Nathan Piasco, Moussab Bennehar, Luis Roldão, Dzmitry Tsishkou, Laurent Caraffa, Jean-Philippe Tarel, Roland Brémond  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06113v1.pdf)  
  Keywords: outpainting, dit, diffusion model  
- **[ChopGrad: Pixel-Wise Losses for Latent Video Diffusion via Truncated Backpropagation](https://arxiv.org/abs/2603.17812v2)**  
  Authors: Dmitriy Rivkin, Parker Ewen, Lili Gao, Julian Ost, Stefanie Walz, Rasika Kangutkar, Mario Bijelic, Felix Heide  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17812v2.pdf)  
  Keywords: efficient, latent video, super-resolution, video generation, video diffusion, video enhancement, diffusion model, video inpainting, dit  
- **[ConfCtrl: Enabling Precise Camera Control in Video Diffusion via Confidence-Aware Interpolation](https://arxiv.org/abs/2603.09819v1)**  
  Authors: Liudi Yang, George Eskandar, Fengyi Shen, Mohammad Altillawi, Yang Bai, Chi Zhang, Ziyuan Liu, Abhinav Valada  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09819v1.pdf)  
  Keywords: video interpolation, camera control, video diffusion, diffusion model, novel view, dit  
- **[Pinterest Canvas: Large-Scale Image Generation at Pinterest](https://arxiv.org/abs/2603.06453v1)**  
  Authors: Yu Wang, Eric Tzeng, Raymond Shiau, Jie Yang, Dmitry Kislyuk, Charles Rosenberg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06453v1.pdf)  
  Keywords: image-to-video, video generation, diffusion model, dit, outpainting  

### Video Super-Resolution & Enhancement

*Showing the latest 50 out of 62 papers*

- **[Beyond Few-Step Inference: Accelerating Video Diffusion Transformer Model Serving with Inter-Request Caching Reuse](https://arxiv.org/abs/2604.04451v1)**  
  Authors: Hao Liu, Ye Huang, Chenghuan Huang, Zhenyi Zheng, Jiangsu Du, Ziyang Ma, Jing Lyu, Yutong Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04451v1.pdf)  
  Keywords: denoising, video generation, video diffusion, diffusion model, diffusion transformer, dit  
- **[OP-GRPO: Efficient Off-Policy GRPO for Flow-Matching Models](https://arxiv.org/abs/2604.04142v1)**  
  Authors: Liyu Zhang, Kehan Li, Tingrui Han, Tao Zhao, Yuxuan Sheng, Shibo He, Chao Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04142v1.pdf)  
  Keywords: efficient, denoising, video generation, benchmark, dit  
- **[Salt: Self-Consistent Distribution Matching with Cache-Aware Training for Fast Video Generation](https://arxiv.org/abs/2604.03118v1)**  
  Authors: Xingtong Ge, Yi Zhang, Yushi Huang, Dailan He, Xiahong Wang, Bingqi Ma, Guanglu Song, Yu Liu, Jun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.03118v1.pdf) | [![GitHub](https://img.shields.io/github/stars/XingtongGe/Salt?style=social)](https://github.com/XingtongGe/Salt)  
  Keywords: dynamics, denoising, style, video generation, distillation, trajectory, autoregressive, dit  
- **[Not All Frames Deserve Full Computation: Accelerating Autoregressive Video Generation via Selective Computation and Predictive Extrapolation](https://arxiv.org/abs/2604.02979v1)**  
  Authors: Hanshuai Cui, Zhiqing Tang, Zhi Yao, Fanshuai Meng, Weijia Jia, Wei Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02979v1.pdf)  
  Keywords: efficient, denoising, video generation, autoregressive, video diffusion, diffusion model, acceleration, long-form  
- **[Can Video Diffusion Models Predict Past Frames? Bidirectional Cycle Consistency for Reversible Interpolation](https://arxiv.org/abs/2604.01700v1)**  
  Authors: Lingyu Liu, Yaxiong Wang, Li Zhu, Zhedong Zheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01700v1.pdf)  
  Keywords: dynamics, frame interpolation, temporal consistency, video diffusion, diffusion model, architecture, dit  
- **[From Understanding to Erasing: Towards Complete and Stable Video Object Removal](https://arxiv.org/abs/2604.01693v1)**  
  Authors: Dingming Liu, Wenjing Wang, Chen Li, Jing Lyu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01693v1.pdf) | [![GitHub](https://img.shields.io/github/stars/WeChatCV/UnderEraser?style=social)](https://github.com/WeChatCV/UnderEraser)  
  Keywords: denoising, temporal consistency, video diffusion, diffusion model, distillation, benchmark, physical  
- **[ZEUS: Accelerating Diffusion Models with Only Second-Order Predictor](https://arxiv.org/abs/2604.01552v1)**  
  Authors: Yixiao Wang, Ting Jiang, Zishan Shao, Hancheng Ye, Jingwei Sun, Mingyuan Ma, Jianyi Zhang, Yiran Chen, Hai Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01552v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Ting-Justin-Jiang/ZEUS?style=social)](https://github.com/Ting-Justin-Jiang/ZEUS)  
  Keywords: denoising, video generation, diffusion model, acceleration, trajectory, architecture, evaluation  
- **[Video Models Reason Early: Exploiting Plan Commitment for Maze Solving](https://arxiv.org/abs/2603.30043v1)**  
  Authors: Kaleb Newman, Tyler Zhu, Olga Russakovsky  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.30043v1.pdf)  
  Keywords: dynamics, denoising, video diffusion, diffusion model, trajectory  
- **[The Surprising Effectiveness of Noise Pretraining for Implicit Neural Representations](https://arxiv.org/abs/2603.29034v1)**  
  Authors: Kushal Vyas, Alper Kayabasi, Daniel Kim, Vishwanath Saragadam, Ashok Veeraraghavan, Guha Balakrishnan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.29034v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kushalvyas.github.io/noisepretraining.html)  
  Keywords: efficient, denoising  
- **[Anti-I2V: Safeguarding your photos from malicious image-to-video generation](https://arxiv.org/abs/2603.24570v1)**  
  Authors: Duc Vu, Anh Nguyen, Chi Tran, Anh Tran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24570v1.pdf)  
  Keywords: image-to-video, i2v, human animation, denoising, video generation, video diffusion, diffusion model, temporal consistency, architecture, diffusion transformer, dit  

### World Models & Simulation

*Showing the latest 50 out of 95 papers*

- **[INSPATIO-WORLD: A Real-Time 4D World Simulator via Spatiotemporal Autoregressive Modeling](https://arxiv.org/abs/2604.07209v1)**  
  Authors: InSpatio Team, Donghui Shen, Guofeng Zhang, Haomin Liu, Haoyu Ji, Hujun Bao, Hongjia Zhai, Jialin Liu, Jing Guo, Nan Wang, Siji Pan, Weihong Pan, Weijian Xie, Xianbin Liu, Xiaojun Xiang, Xiaoyu Zhang, Xinyu Chen, Yifu Wang, Yipeng Chen, Zhenzhou Fan, Zhewen Le, Zhichao Ye, Ziqiang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07209v1.pdf)  
  Keywords: world simulator, interactive, video generation, world model, distillation, benchmark, architecture, autoregressive, physical, controllable  
- **[Grounded Forcing: Bridging Time-Independent Semantics and Proximal Dynamics in Autoregressive Video Synthesis](https://arxiv.org/abs/2604.06939v1)**  
  Authors: Jintao Chen, Chengyu Bai, Junjun hu, Xinda Xue, Mu Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06939v1.pdf)  
  Keywords: interactive, dynamics, identity, video synthesis, autoregressive, long-form  
- **[Evolution of Video Generative Foundations](https://arxiv.org/abs/2604.06339v1)**  
  Authors: Teng Hu, Jiangning Zhang, Hongrui Huang, Ran Yi, Zihan Su, Jieyu Weng, Zhucun Xue, Lizhuang Ma, Ming-Hsuan Yang, Dacheng Tao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06339v1.pdf) | [![GitHub](https://img.shields.io/github/stars/sjtuplayer/Awesome-Video-Foundations?style=social)](https://github.com/sjtuplayer/Awesome-Video-Foundations)  
  Keywords: dynamics, autonomous driving, video generation, world model, simulation, diffusion model, survey, education, video editing, dit  
- **[Action Images: End-to-End Policy Learning via Multiview Video Generation](https://arxiv.org/abs/2604.06168v1)**  
  Authors: Haoyu Zhen, Zixian Gao, Qiao Sun, Yilin Zhao, Yuncong Yang, Yilun Du, Tsun-Hsuan Wang, Yi-Ling Qiao, Chuang Gan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06168v1.pdf)  
  Keywords: action-conditioned, video generation, world model, dit, evaluation  
- **[DriveVA: Video Action Models are Zero-Shot Drivers](https://arxiv.org/abs/2604.04198v1)**  
  Authors: Mengmeng Liu, Diankun Zhang, Jiuming Liu, Jianfeng Cui, Hongwei Xie, Guang Chen, Hangjun Ye, Michael Ying Yang, Francesco Nex, Hao Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04198v1.pdf)  
  Keywords: dynamics, video generation, world model, trajectory, autonomous driving, multi-modal, physical, dit  
- **[CRAFT: Video Diffusion for Bimanual Robot Data Generation](https://arxiv.org/abs/2604.03552v1)**  
  Authors: Jason Chen, I-Chun Arthur Liu, Gaurav Sukhatme, Daniel Seita  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.03552v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://craftaug.github.io)  
  Keywords: video generation, simulation, video diffusion, diffusion model, trajectory, physical, diffusion transformer, dit  
- **[ActionParty: Multi-Subject Action Binding in Generative Video Games](https://arxiv.org/abs/2604.02330v1)**  
  Authors: Alexander Pondaven, Ziyi Wu, Igor Gilitschenski, Philip Torr, Sergey Tulyakov, Fabio Pizzati, Aliaksandr Siarohin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02330v1.pdf)  
  Keywords: interactive, identity, world model, video diffusion, diffusion model, benchmark, autoregressive, controllable  
- **[Resonance4D: Frequency-Domain Motion Supervision for Preset-Free Physical Parameter Learning in 4D Dynamic Physical Scene Simulation](https://arxiv.org/abs/2604.01994v1)**  
  Authors: Changshe Zhang, Jie Feng, Siyu Chen, Guanbin Li, Ronghua Shang, Junpeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01994v1.pdf)  
  Keywords: dynamics, physics, simulation, video diffusion, physical  
- **[DriveDreamer-Policy: A Geometry-Grounded World-Action Model for Unified Generation and Planning](https://arxiv.org/abs/2604.01765v1)**  
  Authors: Yang Zhou, Xiaofeng Wang, Hao Shao, Letian Wang, Guosheng Zhao, Jiangnan Shao, Jiagang Zhu, Tingdong Yu, Zheng Zhu, Guan Huang, Steven L. Waslander  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01765v1.pdf)  
  Keywords: video generation, world model, benchmark, architecture, physical, controllable  
- **[Control-DINO: Feature Space Conditioning for Controllable Image-to-Video Diffusion](https://arxiv.org/abs/2604.01761v1)**  
  Authors: Edoardo A. Dominici, Thomas Deixelberger, Konstantinos Vardis, Markus Steinberger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01761v1.pdf)  
  Keywords: image-to-video, style, simulation, video diffusion, diffusion model, novel view, architecture, controllable, dit  



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
