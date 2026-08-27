# Awesome Video Diffusions [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Video Diffusion Models and Video Generation. Content is automatically updated daily.

> Last Update: 2026-08-27 07:48:57

## 📰 Latest Updates

🔧 **[2026-08-08] Resilient Scheduled Updates**
- Temporary arXiv rate limits, server errors, and timeouts now preserve the latest valid data and finish with a warning
- Added stable search exit codes, atomic publication, strict JSON validation, and fallback to any valid historical snapshot

🔎 **[2026-08-08] Broader and More Accurate Video Indexing**
- Expanded coverage to 1,000 relevant papers across diffusion, flow matching, autoregressive generation, world models, editing, enhancement, and audio-video generation
- Added broader arXiv domains, local relevance filtering, and boundary-aware category matching for acronyms such as DiT, T2V, I2V, and V2V

🚀 **[2026-02] Project Launched — v1.0**
- Adapted from [awesome-gaussians](https://github.com/longxiang-ai/awesome-gaussians) framework for tracking video diffusion research
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

- [3D-aware Video Generation](#3d-aware-video-generation) (54 papers) - Video generation with 3D awareness, multi-view consistency, and 4D content creation
- [Applications](#applications) (215 papers) - Domain-specific applications of video diffusion models
- [Architecture & Efficiency](#architecture-&-efficiency) (402 papers) - Architectural innovations (DiT, UNet), flow matching, and training/inference efficiency
- [Audio & Multi-modal](#audio-&-multi-modal) (69 papers) - Audio-driven and multi-modal conditioned video generation
- [Controllable Generation](#controllable-generation) (322 papers) - Controllable video generation with motion, camera, pose, or layout guidance
- [Human & Character Animation](#human-&-character-animation) (68 papers) - Human-centric video generation including talking heads, dance, and character animation
- [Image-to-Video Generation](#image-to-video-generation) (98 papers) - Methods for animating still images into videos
- [Long Video Generation](#long-video-generation) (265 papers) - Generating temporally consistent long-form videos beyond short clips
- [Personalization & Customization](#personalization-&-customization) (178 papers) - Personalized video generation with custom subjects, identities, or styles
- [Physical Understanding](#physical-understanding) (309 papers) - Physics-aware video generation and dynamics modeling
- [Surveys & Benchmarks](#surveys-&-benchmarks) (303 papers) - Survey papers, benchmarks, and evaluation metrics for video generation
- [Text-to-Video Generation](#text-to-video-generation) (139 papers) - Foundation models and methods for generating videos from text prompts
- [Video Editing](#video-editing) (104 papers) - Diffusion-based video editing, style transfer, and manipulation
- [Video Inpainting & Completion](#video-inpainting-&-completion) (27 papers) - Video inpainting, completion, outpainting, and temporal prediction
- [Video Super-Resolution & Enhancement](#video-super-resolution-&-enhancement) (162 papers) - Video quality improvement, upscaling, restoration, and frame interpolation
- [World Models & Simulation](#world-models-&-simulation) (258 papers) - Video generation as world simulators and interactive environment generation



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3D-aware Video Generation

*Showing the latest 50 out of 54 papers*

- **[4DStreamCtrl: Interactive Video Generation with Online 4D Control](https://arxiv.org/abs/2608.25479v1)**  
  Authors: Shiqian Li, Chenguo Lin, Zhiguang Liu, Yu Tang, Jiarong Ou, Rui Chen, Yixin Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.25479v1.pdf)  
  Keywords: 3d consistent, camera motion, controllable, denoising, diffusion model, efficient, embodied, interactive, long video, motion control, motion transfer, streaming, trajectory, video diffusion, video generation  
- **[FixAnything: 3D-Consistent Rendering Refinement via Video Generative Priors](https://arxiv.org/abs/2608.23549v1)**  
  Authors: Khiem Vuong, Deva Ramanan, Srinivasa Narasimhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.23549v1.pdf)  
  Keywords: 3d consistent, camera motion, video to video, video translation, video-to-video  
- **[GaussVid: Sparse-View Gaussian Splatting with 3D-Aware Video Diffusion Priors](https://arxiv.org/abs/2608.21849v1)**  
  Authors: Xinhui Liu, Can Wang, Wei Jiang, Wei Wang, Dong Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.21849v1.pdf)  
  Keywords: 3d-aware, camera-conditioned, novel view, video diffusion, video generation, video restoration  
- **[Grounded-Exo2Ego: Structured Semantic Grounding for Robust Exocentric-to-Egocentric Video Generation](https://arxiv.org/abs/2608.20534v1)**  
  Authors: Shengze Wang, Michael Stengel, Tianye Li, Seonwook Park, Amrita Mazumdar, Koki Nagano, Alex Trevithick, Shalini De Mello  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.20534v1.pdf)  
  Keywords: diffusion model, evaluation, novel view, physical, video diffusion, video generation  
- **[4DAnyone: Create Anyone in 4D from a Casual Monocular Video](https://arxiv.org/abs/2608.20335v1)**  
  Authors: Yudong Jin, Tao Xie, Qihang Zhang, Zehong Shen, Zhen Xu, Yujun Shen, Hujun Bao, Xiaowei Zhou, Yinghao Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.20335v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://4danyone.github.io)  
  Keywords: denoising, dit, game, novel view, video diffusion  
- **[AvatarDynamizer: From Static to Dynamic Human Avatars via Generative Dynamic Textures](https://arxiv.org/abs/2608.19900v1)**  
  Authors: Guoxing Sun, Heming Zhu, Linjie Lyu, Pascal Fua, Christian Theobalt, Marc Habermann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.19900v1.pdf)  
  Keywords: avatar, controllable, dynamics, video diffusion, view-consistent  
- **[MSEditor: Toward Consistent Multi-Shot Video Editing](https://arxiv.org/abs/2608.17559v1)**  
  Authors: Kunyu Feng, Yue Ma, Bingyuan Wang, Yuefeng Wang, Zhiyuan Qin, Hao Cheng, Hao Li, Qifeng Chen, Zeyu Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.17559v1.pdf)  
  Keywords: benchmark, identity, multi-view video, video editing  
- **[SPVC: Structured and Panoptic Video Fixing for Cross-Dataset Driving Scene Rendering](https://arxiv.org/abs/2608.17420v1)**  
  Authors: Gen Li, Shu Han, Yun Xi Qiao, Hua Chen, Xuyang Dai, Bohan Li, Hao Zhao, Chaojian Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.17420v1.pdf)  
  Keywords: autonomous driving, controllable, diffusion model, driving, layout, novel view, simulation, video diffusion  
- **[Context-Matched Distillation: Teacher Causality for Autoregressive Video Distillation](https://arxiv.org/abs/2608.13391v1)**  
  Authors: Hmrishav Bandyopadhyay, Xuanchi Ren, Zijian Huang, Jay Zhangjie Wu, Tianshi Cao, Ruilong Li, Bryan Chu, Sanja Fidler, Yi-Zhe Song, Zian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.13391v1.pdf)  
  Keywords: autoregressive, autoregressive video, camera-conditioned, denoising, distillation, interactive, long video, video generation  
- **[Beyond Pixels: From Video Priors to 4D Worlds](https://arxiv.org/abs/2608.10744v1)**  
  Authors: Zihao Liu, Xiaolong Shen, Zhenglin Zhou, Ruijie Quan, Yi Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.10744v1.pdf)  
  Keywords: 4d generation, dynamic 3d, video diffusion  

### Applications

*Showing the latest 50 out of 215 papers*

- **[One Policy, Many Embodiments: Unified Camera-Centric Action Geometry Pre-training for Heterogeneous Embodied Manipulation](https://arxiv.org/abs/2608.26058v1)**  
  Authors: Xiaomi Embodied Intelligence Team, University of Macau, :, Shaoqing Xu, Fang Li, Guozhi Zhan, Zhixiang Duan, Yuhan Wang, Yuechen Luo, Shengyin Jiang, Hanbing Li, Zhiying Du, Longlong Wang, Longmei Jiang, Weixiang Liang, Ying Gong, Yong Pan, Ziping Zhao, Zhiyuan Chen, Yangwei You, Kun Ma, Qinyuan Liu, Hangjun Ye, Zhi-xin Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.26058v1.pdf)  
  Keywords: architecture, benchmark, embodied, simulation, video synthesis  
- **[4DStreamCtrl: Interactive Video Generation with Online 4D Control](https://arxiv.org/abs/2608.25479v1)**  
  Authors: Shiqian Li, Chenguo Lin, Zhiguang Liu, Yu Tang, Jiarong Ou, Rui Chen, Yixin Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.25479v1.pdf)  
  Keywords: 3d consistent, camera motion, controllable, denoising, diffusion model, efficient, embodied, interactive, long video, motion control, motion transfer, streaming, trajectory, video diffusion, video generation  
- **[Game2World Engine: Unlocking In-the-Wild Gameplay Videos for World Model Training](https://arxiv.org/abs/2608.24680v1)**  
  Authors: Wenxuan Shen, Dongna Jin, Dongping Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.24680v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Dongping-Chen/Game2World?style=social)](https://github.com/Dongping-Chen/Game2World)  
  Keywords: dynamics, evaluation, game, video editing, world model  
- **[How Do Professional Editors Evaluate the Editing Quality of AI-Generated Cinematic Video Ads?](https://arxiv.org/abs/2608.24329v1)**  
  Authors: Po-Ming Law, Weizhi Li, Arpit Narechania  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.24329v1.pdf)  
  Keywords: cinematic, evaluation, human evaluation, sound, video generation  
- **[NVIDIA Cosmos-H-Dreams: Real-Time Generative Physics Simulation for Surgical Robotics](https://arxiv.org/abs/2608.24199v1)**  
  Authors: Javier Gamazo Tejero, Lukas Zbinden, Keyur Sheth, Raghavendra K M, Nadim Daher, Diego Granero Maraña, Filip Binkiewicz, Patrick Thornycroft, Mahdi Azizian, Sean D. Huver  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.24199v1.pdf)  
  Keywords: action-conditioned, controllable, distillation, dynamics, education, interactive, physical, physics, robotics, simulation, streaming, video world model, world model  
- **[GlanceWAM: Sparse Test-Time Imagination for World-Action Models](https://arxiv.org/abs/2608.23927v1)**  
  Authors: Linhan Wang, Zijian An, Mingyuan Zhang, Chen Dai, Yi Xu, Can Cui, Zichong Yang, Yinlin Chen, Lifeng Zhou, Chang-Tien Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.23927v1.pdf) | [![GitHub](https://img.shields.io/github/stars/linhanwang/GlanceWAM?style=social)](https://github.com/linhanwang/GlanceWAM)  
  Keywords: benchmark, dit, physical, robot learning, video dit, video generation  
- **[GeoWAM: Visual Geometry World Action Models for Autonomous Driving](https://arxiv.org/abs/2608.23486v2)**  
  Authors: Yiren Lu, Xin Ye, Jiaming Liu, Philip Jacobson, Jin Yao, Yi-chung Chen, Liam Merino, Dhruva Dixith Kurra, Min Cai, Tom Lampo, Yu Yin, Danhua Guo, Burhan Yaman  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.23486v2.pdf)  
  Keywords: autonomous driving, driving, dynamics, trajectory, video generation  
- **[Loopy: Seamless Video Loop Generation via Anchored Looping Shift of Positional Embedding](https://arxiv.org/abs/2608.23090v1)**  
  Authors: Haotian Dong, Wenjing Wang, Chen Li, Jing Lyu, Xin Wang, Di Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.23090v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://donghaotian123.github.io/Loopy)  
  Keywords: dit, game, identity, style, temporal consistency, video generation  
- **[From Generation to Simulation: How Far Are World Models from Being True Simulators?](https://arxiv.org/abs/2608.23070v1)**  
  Authors: Tong Wang, Huan Deng, Mucheng Yang, Yang He, Xiaohui Kuang, Gang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.23070v1.pdf) | [![GitHub](https://img.shields.io/github/stars/AtongWang/world-model-simulators?style=social)](https://github.com/AtongWang/world-model-simulators)  
  Keywords: dynamics, evaluation, game, physical, physics, simulation, video generation, world model  
- **[InfinityEdit: Infinite Video Editing with a Lightweight Edit-Ignition Adapter](https://arxiv.org/abs/2608.20910v1)**  
  Authors: Yunze Tong, Mushui Liu, Canyu Zhao, Shiyi Zhang, Didi Zhu, Peng Zhang, Wanggui He, Jinlong Liu, Ying Chen, Hao Jiang, Pipei Huang, Bo Zheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.20910v1.pdf)  
  Keywords: denoising, game, infinite video, instruction-based video editing, streaming, video editing  

### Architecture & Efficiency

*Showing the latest 50 out of 402 papers*

- **[VBVR-Pro: A Scalable and Verifiable Suite for Native Visual Reasoning](https://arxiv.org/abs/2608.26105v1)**  
  Authors: Junxiang Xu, Ruisi Wang, Fanyi Pu, Maijunxian Wang, Ran Ji, Tongxi Zhou, Chenyang Gu, Jing Zuo, Hongcan Xiao, Yimeng Geng, Wanqi Yin, Wei Chen, Oscar Qian, Zhengan Yan, Ziqi Huang, Haiwen Diao, Liang Pan, Bo Li, Xiangyu Fan, Dezhi Luo, Fengyuan Yu, Zehong Zhao, Qingying Gao, Tinghui Zhu, Yilan Zhang, Jingqi Tong, Pinyuan Feng, Zhengze Jiang, Letian Wang, Ziyu Guo, Renrui Zhang, Jieneng Chen, Sonia Joseph, Constantin Venhoff, Saman Motamed, Mengyue Yang, Chandra Sripada, Alan Yuille, Philip Torr, Lvmin Zhang, Vikash Kumar, Daniel Khashabi, Nikolaus Kriegeskorte, Raphaël Millière, Vincent C. Müller, Anyi Rao, Quan Wang, Ziwei Liu, Dahua Lin, Lei Yang, Hokin Deng, Zhongang Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.26105v1.pdf)  
  Keywords: controllable, efficient, evaluation, video generation  
- **[One Policy, Many Embodiments: Unified Camera-Centric Action Geometry Pre-training for Heterogeneous Embodied Manipulation](https://arxiv.org/abs/2608.26058v1)**  
  Authors: Xiaomi Embodied Intelligence Team, University of Macau, :, Shaoqing Xu, Fang Li, Guozhi Zhan, Zhixiang Duan, Yuhan Wang, Yuechen Luo, Shengyin Jiang, Hanbing Li, Zhiying Du, Longlong Wang, Longmei Jiang, Weixiang Liang, Ying Gong, Yong Pan, Ziping Zhao, Zhiyuan Chen, Yangwei You, Kun Ma, Qinyuan Liu, Hangjun Ye, Zhi-xin Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.26058v1.pdf)  
  Keywords: architecture, benchmark, embodied, simulation, video synthesis  
- **[Plans You Can Check: Verifier-Grounded Learning of an Open-Weight Planner for Executable Video-Editing](https://arxiv.org/abs/2608.25622v1)**  
  Authors: Haoyu Wang, Cheng Feng, Liuyang Bian, Ruiyang Huang, Lei Wei, Yafei Wen, Xiaoxin Chen, Xiaoying Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.25622v1.pdf)  
  Keywords: distillation, video editing  
- **[4DStreamCtrl: Interactive Video Generation with Online 4D Control](https://arxiv.org/abs/2608.25479v1)**  
  Authors: Shiqian Li, Chenguo Lin, Zhiguang Liu, Yu Tang, Jiarong Ou, Rui Chen, Yixin Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.25479v1.pdf)  
  Keywords: 3d consistent, camera motion, controllable, denoising, diffusion model, efficient, embodied, interactive, long video, motion control, motion transfer, streaming, trajectory, video diffusion, video generation  
- **[VGA-BenchV2: An Expanded Unified Benchmark and Multi-Model Framework for Evaluating Video Aesthetics and Generation Quality](https://arxiv.org/abs/2608.25452v1)**  
  Authors: Longteng Jiang, DanDan Zheng, Qianqian Qiao, Heng Huang, Huaye Wang, Yihang Bo, Bao Peng, Jingdong Chen, Jun Zhou, Xin Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.25452v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://huggingface.co/datasets/BestiVictoryLab/VGA-Bench.) | [![Dataset](https://img.shields.io/badge/-Dataset-orange)](https://huggingface.co/datasets/BestiVictoryLab/VGA-Bench)  
  Keywords: architecture, benchmark, evaluation, video generation  
- **[TurboT2VA: Fast Large-Scale Text-to-Video-Audio Generation via Score-Regularized Consistency Distillation](https://arxiv.org/abs/2608.24674v1)**  
  Authors: Xiaoda Yang, Yuxiang Liu, Kaiwen Zheng, Yuan Liu, Yibo Lai, Shengpeng Ji, Kai Jiang, Jianfei Chen, Xiaobin Hu, Shuicheng Yan, Jintao Zhang, Jun Zhu, Zhou Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.24674v1.pdf) | [![GitHub](https://img.shields.io/github/stars/thu-ml/TurboDiffusion?style=social)](https://github.com/thu-ml/TurboDiffusion)  
  Keywords: architecture, consistency distillation, distillation, evaluation, sparse attention, text to video, text-to-video, trajectory  
- **[NVIDIA Cosmos-H-Dreams: Real-Time Generative Physics Simulation for Surgical Robotics](https://arxiv.org/abs/2608.24199v1)**  
  Authors: Javier Gamazo Tejero, Lukas Zbinden, Keyur Sheth, Raghavendra K M, Nadim Daher, Diego Granero Maraña, Filip Binkiewicz, Patrick Thornycroft, Mahdi Azizian, Sean D. Huver  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.24199v1.pdf)  
  Keywords: action-conditioned, controllable, distillation, dynamics, education, interactive, physical, physics, robotics, simulation, streaming, video world model, world model  
- **[GlanceWAM: Sparse Test-Time Imagination for World-Action Models](https://arxiv.org/abs/2608.23927v1)**  
  Authors: Linhan Wang, Zijian An, Mingyuan Zhang, Chen Dai, Yi Xu, Can Cui, Zichong Yang, Yinlin Chen, Lifeng Zhou, Chang-Tien Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.23927v1.pdf) | [![GitHub](https://img.shields.io/github/stars/linhanwang/GlanceWAM?style=social)](https://github.com/linhanwang/GlanceWAM)  
  Keywords: benchmark, dit, physical, robot learning, video dit, video generation  
- **[Long-Horizon Audio-Visual Generation for Persistent Stories and Interactive Worlds](https://arxiv.org/abs/2608.23383v2)**  
  Authors: Nan Duan, Haoyang Huang, Weiyang Jin, Haoran Li, Yaowei Li, Yuming Li, Yijun Liu, Xin Lu, Xiaoxiao Ma, Yanwen Ma, Yaofeng Su, Yilang Sun, Haoyu Wang, Zeyue Xue, Songchun Zhang, Junhao Zhuang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.23383v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://echo-team-joy-future-academy-jd.github.io/Echo-1.5-Page)  
  Keywords: audio-visual generation, efficient, identity, interactive, long video, long-form, video generation, world model  
- **[Loopy: Seamless Video Loop Generation via Anchored Looping Shift of Positional Embedding](https://arxiv.org/abs/2608.23090v1)**  
  Authors: Haotian Dong, Wenjing Wang, Chen Li, Jing Lyu, Xin Wang, Di Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.23090v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://donghaotian123.github.io/Loopy)  
  Keywords: dit, game, identity, style, temporal consistency, video generation  

### Audio & Multi-modal

*Showing the latest 50 out of 69 papers*

- **[How Do Professional Editors Evaluate the Editing Quality of AI-Generated Cinematic Video Ads?](https://arxiv.org/abs/2608.24329v1)**  
  Authors: Po-Ming Law, Weizhi Li, Arpit Narechania  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.24329v1.pdf)  
  Keywords: cinematic, evaluation, human evaluation, sound, video generation  
- **[Long-Horizon Audio-Visual Generation for Persistent Stories and Interactive Worlds](https://arxiv.org/abs/2608.23383v2)**  
  Authors: Nan Duan, Haoyang Huang, Weiyang Jin, Haoran Li, Yaowei Li, Yuming Li, Yijun Liu, Xin Lu, Xiaoxiao Ma, Yanwen Ma, Yaofeng Su, Yilang Sun, Haoyu Wang, Zeyue Xue, Songchun Zhang, Junhao Zhuang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.23383v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://echo-team-joy-future-academy-jd.github.io/Echo-1.5-Page)  
  Keywords: audio-visual generation, efficient, identity, interactive, long video, long-form, video generation, world model  
- **[VA-Judger: Reward Modeling from Human Preference Feedback for Joint Video-Audio Generation](https://arxiv.org/abs/2608.18607v2)**  
  Authors: Yinming Huang, Shuyuan Tu, Xi Yan, Zihan Yang, Jianhua Han, Xu Hang, Yu-Gang Jiang, Zuxuan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.18607v2.pdf)  
  Keywords: audio-video generation, benchmark, video generation  
- **[VicEdit: Learning to Edit Videos from Visual In-Context Examples](https://arxiv.org/abs/2608.16745v1)**  
  Authors: Yuji Wang, Teng Hu, Yuheng Chen, Ran Yi, Han Feng, Weijian Cao, Chengjie Wang, Lizhuang Ma, Jiangning Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.16745v1.pdf)  
  Keywords: controllable, distillation, dynamics, instruction-based video editing, multi-modal, video editing  
- **[SingDance: Compositional Zero-Shot Singing-and-Dancing Video Generation with Role-Aware Audio Conditioning](https://arxiv.org/abs/2608.16220v1)**  
  Authors: Tao Feng, Xu Li, Xiangyang Luo, Ming Wen, Huadai Liu, Chen Zhang, Wei Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.16220v1.pdf)  
  Keywords: body motion, controllable, speech-driven, video diffusion, video generation  
- **[AnyTalk: Speech Animation for Arbitrary Characters Leveraging a Video Generation Model](https://arxiv.org/abs/2608.16143v1)**  
  Authors: Kwan Yun, Serin Yoon, Sunjin Jung, Jung Eun Yoo, Inyup Lee, Junyong Noh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.16143v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://serin-yoon.github.io/projects/anytalk)  
  Keywords: audio-driven, diffusion model, talking head, video diffusion, video generation  
- **[Efficient Audio-Visual Generation via Synchrony-Aware Cross-Modal Sparse Attention](https://arxiv.org/abs/2608.15522v1)**  
  Authors: Shengchuan Gao, Teng Hu, Bohao Feng, Luchen Li, Wenqiang Wang, Hongqian Deng, Ran Yi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.15522v1.pdf)  
  Keywords: acceleration, audio-visual generation, denoising, efficient, long video, sound, sparse attention, video generation  
- **[Avatar-Forever: Decoupled Parallel Training for High-Quality Real-Time Infinite Avatars](https://arxiv.org/abs/2608.12107v1)**  
  Authors: Ruibin Li, Tao Yang, Zhiyuan Ma, Fangzhou Ai, Shilei Wen, Lei Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.12107v1.pdf)  
  Keywords: audio-driven, audio-driven avatar, autoregressive, avatar, distillation, efficient, identity, interactive, long video, streaming, video foundation model, video generation  
- **[Omni-LiveAvatar: Minute-Level Real-Time Streaming Joint Audio-Video Avatar Generation](https://arxiv.org/abs/2608.13602v2)**  
  Authors: Lunjie Zhu, Xingtong Ge, Fangyu Lin, Yi Zhang, Zhening Liu, Mengfei Li, Yumeng Zhang, Guanglu Song, Yu Liu, Jun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.13602v2.pdf) | [![GitHub](https://img.shields.io/github/stars/Aoko955/Omni-LiveAvatar?style=social)](https://github.com/Aoko955/Omni-LiveAvatar)  
  Keywords: autoregressive, avatar, denoising, diffusion model, digital human, distillation, interactive, joint audio-video, streaming, video diffusion  
- **[Vorch-Omni: Multi-Task Orchestration of Sight and Sound](https://arxiv.org/abs/2608.05803v1)**  
  Authors: Vorch Team, Xiaoyu Chen, Yang Ding, Cong Han, Menglin Han, Yuxin Hong, Jiebo Hou, Zequn Jie, Xiang Li, Jing Liu, Qi Liu, Yulei Lu, Siyuan Luo, Lin Ma, Xin Ma, Yinlong Qian, Peng Shi, Fang Wan, Siqi Wang, Yaohui Wang, Yaole Wang, Yidi Wu, Siqian Yang, Mingyu Yin, Haoran Yu, Gang Yue, Lisai Zhang, Yuting Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05803v1.pdf)  
  Keywords: audio-driven, audio-visual generation, diffusion transformer, flow matching, sound, text to video, text-to-video  

### Controllable Generation

*Showing the latest 50 out of 322 papers*

- **[VBVR-Pro: A Scalable and Verifiable Suite for Native Visual Reasoning](https://arxiv.org/abs/2608.26105v1)**  
  Authors: Junxiang Xu, Ruisi Wang, Fanyi Pu, Maijunxian Wang, Ran Ji, Tongxi Zhou, Chenyang Gu, Jing Zuo, Hongcan Xiao, Yimeng Geng, Wanqi Yin, Wei Chen, Oscar Qian, Zhengan Yan, Ziqi Huang, Haiwen Diao, Liang Pan, Bo Li, Xiangyu Fan, Dezhi Luo, Fengyuan Yu, Zehong Zhao, Qingying Gao, Tinghui Zhu, Yilan Zhang, Jingqi Tong, Pinyuan Feng, Zhengze Jiang, Letian Wang, Ziyu Guo, Renrui Zhang, Jieneng Chen, Sonia Joseph, Constantin Venhoff, Saman Motamed, Mengyue Yang, Chandra Sripada, Alan Yuille, Philip Torr, Lvmin Zhang, Vikash Kumar, Daniel Khashabi, Nikolaus Kriegeskorte, Raphaël Millière, Vincent C. Müller, Anyi Rao, Quan Wang, Ziwei Liu, Dahua Lin, Lei Yang, Hokin Deng, Zhongang Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.26105v1.pdf)  
  Keywords: controllable, efficient, evaluation, video generation  
- **[RefVideo-6M: A Reliable Reference-Based Dataset for Instructional Video Editing](https://arxiv.org/abs/2608.26101v1)**  
  Authors: Bojia Zi, Xiaoyan Yang, Yu Zhou, Ruijie Sun, Lihan Zhang, Bin Liang, Kam-Fai Wong, Haibin Huang, Chi Zhang, Xuelong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.26101v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://huggingface.co/datasets/RefVideo6M/RefVideo6M.) | [![Dataset](https://img.shields.io/badge/-Dataset-orange)](https://huggingface.co/datasets/RefVideo6M/RefVideo6M)  
  Keywords: controllable, identity, identity-preserving, reference-guided, video editing  
- **[4DStreamCtrl: Interactive Video Generation with Online 4D Control](https://arxiv.org/abs/2608.25479v1)**  
  Authors: Shiqian Li, Chenguo Lin, Zhiguang Liu, Yu Tang, Jiarong Ou, Rui Chen, Yixin Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.25479v1.pdf)  
  Keywords: 3d consistent, camera motion, controllable, denoising, diffusion model, efficient, embodied, interactive, long video, motion control, motion transfer, streaming, trajectory, video diffusion, video generation  
- **[TurboT2VA: Fast Large-Scale Text-to-Video-Audio Generation via Score-Regularized Consistency Distillation](https://arxiv.org/abs/2608.24674v1)**  
  Authors: Xiaoda Yang, Yuxiang Liu, Kaiwen Zheng, Yuan Liu, Yibo Lai, Shengpeng Ji, Kai Jiang, Jianfei Chen, Xiaobin Hu, Shuicheng Yan, Jintao Zhang, Jun Zhu, Zhou Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.24674v1.pdf) | [![GitHub](https://img.shields.io/github/stars/thu-ml/TurboDiffusion?style=social)](https://github.com/thu-ml/TurboDiffusion)  
  Keywords: architecture, consistency distillation, distillation, evaluation, sparse attention, text to video, text-to-video, trajectory  
- **[NVIDIA Cosmos-H-Dreams: Real-Time Generative Physics Simulation for Surgical Robotics](https://arxiv.org/abs/2608.24199v1)**  
  Authors: Javier Gamazo Tejero, Lukas Zbinden, Keyur Sheth, Raghavendra K M, Nadim Daher, Diego Granero Maraña, Filip Binkiewicz, Patrick Thornycroft, Mahdi Azizian, Sean D. Huver  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.24199v1.pdf)  
  Keywords: action-conditioned, controllable, distillation, dynamics, education, interactive, physical, physics, robotics, simulation, streaming, video world model, world model  
- **[FixAnything: 3D-Consistent Rendering Refinement via Video Generative Priors](https://arxiv.org/abs/2608.23549v1)**  
  Authors: Khiem Vuong, Deva Ramanan, Srinivasa Narasimhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.23549v1.pdf)  
  Keywords: 3d consistent, camera motion, video to video, video translation, video-to-video  
- **[Scaling Reinforcement Learning for Diffusion Models via Velocity Matching](https://arxiv.org/abs/2608.23664v1)**  
  Authors: Jaemoo Choi, Wei Guo, Yuchen Zhu, Arash Vahdat, Molei Tao, Julius Berner, Yongxin Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.23664v1.pdf)  
  Keywords: autoregressive, denoising, trajectory, video generation  
- **[GeoWAM: Visual Geometry World Action Models for Autonomous Driving](https://arxiv.org/abs/2608.23486v2)**  
  Authors: Yiren Lu, Xin Ye, Jiaming Liu, Philip Jacobson, Jin Yao, Yi-chung Chen, Liam Merino, Dhruva Dixith Kurra, Min Cai, Tom Lampo, Yu Yin, Danhua Guo, Burhan Yaman  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.23486v2.pdf)  
  Keywords: autonomous driving, driving, dynamics, trajectory, video generation  
- **[Direct, Parallel, or Sequential? A Comparative Study of Training-Free Multi-Subject Image-to-Video Generation](https://arxiv.org/abs/2608.22819v1)**  
  Authors: Yanliang Qi, Kexi Chen, Muchao Ye, Haomiao Ni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.22819v1.pdf)  
  Keywords: controllable, i2v, image to video, image-to-video, temporal consistency, video generation  
- **[MotionPhys: Detecting AI-Generated Videos via Physical Consistency of Optical-Flow Trajectories](https://arxiv.org/abs/2608.20770v1)**  
  Authors: Haojin He, Hao Tan, Zichang Tan, Ajian Liu, Jun Wan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.20770v1.pdf)  
  Keywords: efficient, physical, physical consistency, trajectory, video generation  

### Human & Character Animation

*Showing the latest 50 out of 68 papers*

- **[4DStreamCtrl: Interactive Video Generation with Online 4D Control](https://arxiv.org/abs/2608.25479v1)**  
  Authors: Shiqian Li, Chenguo Lin, Zhiguang Liu, Yu Tang, Jiarong Ou, Rui Chen, Yixin Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.25479v1.pdf)  
  Keywords: 3d consistent, camera motion, controllable, denoising, diffusion model, efficient, embodied, interactive, long video, motion control, motion transfer, streaming, trajectory, video diffusion, video generation  
- **[AvatarDynamizer: From Static to Dynamic Human Avatars via Generative Dynamic Textures](https://arxiv.org/abs/2608.19900v1)**  
  Authors: Guoxing Sun, Heming Zhu, Linjie Lyu, Pascal Fua, Christian Theobalt, Marc Habermann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.19900v1.pdf)  
  Keywords: avatar, controllable, dynamics, video diffusion, view-consistent  
- **[SingDance: Compositional Zero-Shot Singing-and-Dancing Video Generation with Role-Aware Audio Conditioning](https://arxiv.org/abs/2608.16220v1)**  
  Authors: Tao Feng, Xu Li, Xiangyang Luo, Ming Wen, Huadai Liu, Chen Zhang, Wei Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.16220v1.pdf)  
  Keywords: body motion, controllable, speech-driven, video diffusion, video generation  
- **[AnyTalk: Speech Animation for Arbitrary Characters Leveraging a Video Generation Model](https://arxiv.org/abs/2608.16143v1)**  
  Authors: Kwan Yun, Serin Yoon, Sunjin Jung, Jung Eun Yoo, Inyup Lee, Junyong Noh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.16143v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://serin-yoon.github.io/projects/anytalk)  
  Keywords: audio-driven, diffusion model, talking head, video diffusion, video generation  
- **[FlowDance: Music-Driven Dance Video Generation with Parallel Pose and RGB Streams](https://arxiv.org/abs/2608.15818v1)**  
  Authors: Genying Li, Boda Lin, Jiachen Li, Zijian Jia, Haojie Zheng, Yiming Wang, Shuchen Weng, Si Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.15818v1.pdf)  
  Keywords: body motion, denoising, human animation, identity, identity-preserving, long video, video generation, video synthesis  
- **[Avatar-Forever: Decoupled Parallel Training for High-Quality Real-Time Infinite Avatars](https://arxiv.org/abs/2608.12107v1)**  
  Authors: Ruibin Li, Tao Yang, Zhiyuan Ma, Fangzhou Ai, Shilei Wen, Lei Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.12107v1.pdf)  
  Keywords: audio-driven, audio-driven avatar, autoregressive, avatar, distillation, efficient, identity, interactive, long video, streaming, video foundation model, video generation  
- **[LiveAnimate: Stable Long-Form Streaming Human Animation in Real-Time](https://arxiv.org/abs/2608.11745v2)**  
  Authors: Yuxuan Zhang, Haozhong Xiong, Yubo Huang, Jiayi Song, Jinpeng Yu, Haofan Wang, Jiaming Liu, Ruihua Huang, Liwei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.11745v2.pdf)  
  Keywords: autoregressive, benchmark, diffusion transformer, distillation, dit, driving, human animation, identity, interactive, long-form, streaming, video diffusion, video diffusion transformer  
- **[Omni-LiveAvatar: Minute-Level Real-Time Streaming Joint Audio-Video Avatar Generation](https://arxiv.org/abs/2608.13602v2)**  
  Authors: Lunjie Zhu, Xingtong Ge, Fangyu Lin, Yi Zhang, Zhening Liu, Mengfei Li, Yumeng Zhang, Guanglu Song, Yu Liu, Jun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.13602v2.pdf) | [![GitHub](https://img.shields.io/github/stars/Aoko955/Omni-LiveAvatar?style=social)](https://github.com/Aoko955/Omni-LiveAvatar)  
  Keywords: autoregressive, avatar, denoising, diffusion model, digital human, distillation, interactive, joint audio-video, streaming, video diffusion  
- **[UniVVT: A Unified End-to-End Framework for High-Fidelity Video Virtual Try-on](https://arxiv.org/abs/2608.05745v1)**  
  Authors: Yushe Cao, Shikun Feng, Fei Shen, Haikuo Peng, Jianqiang Xia, Yiheng Zhu, Dianxi Shi, Chun Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05745v1.pdf)  
  Keywords: dynamics, identity, video generation, video inpainting, virtual try-on  
- **[Vorch-Streamer: Extending Human Audio-Visual Generation to Real-Time Long-Form Streaming](https://arxiv.org/abs/2608.05663v2)**  
  Authors: Menglin Han, Yang Ding, Yulei Lu, Haoran Yu, Xin Ma, Junyi Chen, Zhangkai Ni, Lin Ma, Yaohui Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05663v2.pdf)  
  Keywords: audio-video generation, audio-visual generation, avatar, denoising, distillation, identity, long-form, streaming, video generation  

### Image-to-Video Generation

*Showing the latest 50 out of 98 papers*

- **[Direct, Parallel, or Sequential? A Comparative Study of Training-Free Multi-Subject Image-to-Video Generation](https://arxiv.org/abs/2608.22819v1)**  
  Authors: Yanliang Qi, Kexi Chen, Muchao Ye, Haomiao Ni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.22819v1.pdf)  
  Keywords: controllable, i2v, image to video, image-to-video, temporal consistency, video generation  
- **[CaliBench: Are the Stochastic Dynamics of Video World Models Physically Calibrated?](https://arxiv.org/abs/2608.16829v1)**  
  Authors: Jonathan Sadeghi, Jenny Seidenschwarz, Jesse Allardice, Sirish Srinivasan, Benjamin Graham, Jeffrey Hawke  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.16829v1.pdf)  
  Keywords: dynamics, image to video, image-to-video, physical  
- **[EditStream: A Unified Autoregressive Framework for Interactive Video Generation and Editing](https://arxiv.org/abs/2608.21424v1)**  
  Authors: Yuqian Zhou, Zhenghong Zhou, Zongze Wu, Cameron Smith, Richard Zhang, Jiebo Luo, Eli Shechtman, Zhe Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.21424v1.pdf)  
  Keywords: autoregressive, autoregressive video, creative, distillation, dit, efficient, image to video, image-to-video, interactive, reference-guided, streaming, text to video, text-to-video, video editing, video generation, video to video, video-to-video  
- **[HPSD: Hybrid-Policy Self-Distillation for Text-Image-to-Video Diffusion Models](https://arxiv.org/abs/2608.13205v1)**  
  Authors: Jiazi Bu, Pengyang Ling, Yujie Zhou, Yibin Wang, Yuhang Zang, Xuanlang Dai, Shengyuan Ding, Tianyi Wei, Xiaohang Zhan, Jiaqi Wang, Tong Wu, Dahua Lin, Xingang Pan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.13205v1.pdf)  
  Keywords: architecture, distillation, i2v, image to video, image-to-video, t2v, text to video, text-to-video, trajectory, video diffusion  
- **[Beyond Trial-and-Error: Agentic Optimization for Image-to-Video Adherence](https://arxiv.org/abs/2608.12290v1)**  
  Authors: Aman Tyagi, Hemanth Boinpally, Jonathan Chen, Douglas Gebert, Steven Hickson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.12290v1.pdf)  
  Keywords: i2v, image to video, image-to-video, video generation, video synthesis  
- **[SparSTAR: Sparse Attention for SpaceTime AutoRegressive Video Synthesis](https://arxiv.org/abs/2608.10519v2)**  
  Authors: Jongbeom Lee, Hyunwoo Yu, Jincheol Yang, Jaemin Choi, Suk-Ju Kang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.10519v2.pdf)  
  Keywords: autoregressive, autoregressive video, image to video, image-to-video, sparse attention, text to video, text-to-video, video generation, video synthesis  
- **[Bridging Event Streams and DiT: Event-Guided Video Frame Interpolation](https://arxiv.org/abs/2608.10479v2)**  
  Authors: Guixu Lin, Yuyang Yu, Xiang Ji, Linyao Chen, Zhengwei Yin, Mengshun Hu, Mingdeng Cao, Shengfeng He, Yinqiang Zheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.10479v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://joseph-lin-tech.github.io/BridgeEventDiT-VFI)  
  Keywords: diffusion model, dit, frame interpolation, image to video, image-to-video, video diffusion, video frame interpolation  
- **[Alpha as an Efficiency Signal: Visibility-Routed RGBA Image-to-Video Generation](https://arxiv.org/abs/2608.09355v1)**  
  Authors: Zhe Li, Honghao Qiao, Zhixin Xu, Qijie Wang, Bo Peng, Dawei Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.09355v1.pdf)  
  Keywords: denoising, dit, flow matching, game, image to video, image-to-video, style, video generation  
- **[RAVEN-Eval: Rubric-Guided Automatic Evaluation for AI Video Generation Models Based on LMM Preference Judgement](https://arxiv.org/abs/2608.09111v1)**  
  Authors: Ziheng Jia, Jiaying Qian, Zicheng Zhang, Xiaorong Zhu, Lancheng Gao, Xiongkuo Min  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.09111v1.pdf)  
  Keywords: evaluation, human evaluation, i2v, image to video, image-to-video, t2v, text to video, text-to-video, video generation  
- **[EmoWorld: A Decoupled Affective Field for Controllable Emotional Video Generation](https://arxiv.org/abs/2608.06231v1)**  
  Authors: Bingyuan Wang, Baistan Zhyldyzbekov, Kunyu Feng, Zeyu Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.06231v1.pdf)  
  Keywords: camera-conditioned, controllable, denoising, diffusion transformer, dit, flow matching, image to video, image-to-video, text to video, text-to-video, video diffusion, video diffusion transformer, video dit, video generation  

### Long Video Generation

*Showing the latest 50 out of 265 papers*

- **[4DStreamCtrl: Interactive Video Generation with Online 4D Control](https://arxiv.org/abs/2608.25479v1)**  
  Authors: Shiqian Li, Chenguo Lin, Zhiguang Liu, Yu Tang, Jiarong Ou, Rui Chen, Yixin Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.25479v1.pdf)  
  Keywords: 3d consistent, camera motion, controllable, denoising, diffusion model, efficient, embodied, interactive, long video, motion control, motion transfer, streaming, trajectory, video diffusion, video generation  
- **[NVIDIA Cosmos-H-Dreams: Real-Time Generative Physics Simulation for Surgical Robotics](https://arxiv.org/abs/2608.24199v1)**  
  Authors: Javier Gamazo Tejero, Lukas Zbinden, Keyur Sheth, Raghavendra K M, Nadim Daher, Diego Granero Maraña, Filip Binkiewicz, Patrick Thornycroft, Mahdi Azizian, Sean D. Huver  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.24199v1.pdf)  
  Keywords: action-conditioned, controllable, distillation, dynamics, education, interactive, physical, physics, robotics, simulation, streaming, video world model, world model  
- **[Scaling Reinforcement Learning for Diffusion Models via Velocity Matching](https://arxiv.org/abs/2608.23664v1)**  
  Authors: Jaemoo Choi, Wei Guo, Yuchen Zhu, Arash Vahdat, Molei Tao, Julius Berner, Yongxin Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.23664v1.pdf)  
  Keywords: autoregressive, denoising, trajectory, video generation  
- **[Long-Horizon Audio-Visual Generation for Persistent Stories and Interactive Worlds](https://arxiv.org/abs/2608.23383v2)**  
  Authors: Nan Duan, Haoyang Huang, Weiyang Jin, Haoran Li, Yaowei Li, Yuming Li, Yijun Liu, Xin Lu, Xiaoxiao Ma, Yanwen Ma, Yaofeng Su, Yilang Sun, Haoyu Wang, Zeyue Xue, Songchun Zhang, Junhao Zhuang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.23383v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://echo-team-joy-future-academy-jd.github.io/Echo-1.5-Page)  
  Keywords: audio-visual generation, efficient, identity, interactive, long video, long-form, video generation, world model  
- **[Loopy: Seamless Video Loop Generation via Anchored Looping Shift of Positional Embedding](https://arxiv.org/abs/2608.23090v1)**  
  Authors: Haotian Dong, Wenjing Wang, Chen Li, Jing Lyu, Xin Wang, Di Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.23090v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://donghaotian123.github.io/Loopy)  
  Keywords: dit, game, identity, style, temporal consistency, video generation  
- **[Direct, Parallel, or Sequential? A Comparative Study of Training-Free Multi-Subject Image-to-Video Generation](https://arxiv.org/abs/2608.22819v1)**  
  Authors: Yanliang Qi, Kexi Chen, Muchao Ye, Haomiao Ni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.22819v1.pdf)  
  Keywords: controllable, i2v, image to video, image-to-video, temporal consistency, video generation  
- **[InfinityEdit: Infinite Video Editing with a Lightweight Edit-Ignition Adapter](https://arxiv.org/abs/2608.20910v1)**  
  Authors: Yunze Tong, Mushui Liu, Canyu Zhao, Shiyi Zhang, Didi Zhu, Peng Zhang, Wanggui He, Jinlong Liu, Ying Chen, Hao Jiang, Pipei Huang, Bo Zheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.20910v1.pdf)  
  Keywords: denoising, game, infinite video, instruction-based video editing, streaming, video editing  
- **[DiffVC-ONE: Diffusion-based Generative Video Compression with One-Step Video Diffusion Transformer](https://arxiv.org/abs/2608.20515v1)**  
  Authors: Wenzhuo Ma, Zhenzhong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.20515v1.pdf)  
  Keywords: diffusion transformer, dit, temporal consistency, video diffusion, video diffusion transformer, video dit  
- **[Stream4D: 4D-Consistency for Streaming Autoregressive Diffusion Video Models](https://arxiv.org/abs/2608.19556v1)**  
  Authors: Yuanhao Ban, Jiaqi Feng, Hengguang Zhou, Xiaohuan Pei, Justin Cui, Cho-Jui Hsieh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.19556v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://banyuanhao.github.io/Stream4D)  
  Keywords: autoregressive, autoregressive video, dynamics, frame prediction, streaming, video generation  
- **[CoinVE-200K: A Large-Scale High-Quality Dataset for Compositional Instruction-Guided Video Editing](https://arxiv.org/abs/2608.17566v2)**  
  Authors: Fuchen Long, Cong Wang, Zitao Gao, Wenhao Zhong, Yu Cheng, Xiaolu Hou, Yan Li, Xiao Cao, Xinlong Sun, Xi Chen, Yu Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.17566v2.pdf)  
  Keywords: benchmark, instruction-based video editing, instruction-guided, t2v, temporal consistency, video editing  

### Personalization & Customization

*Showing the latest 50 out of 178 papers*

- **[RefVideo-6M: A Reliable Reference-Based Dataset for Instructional Video Editing](https://arxiv.org/abs/2608.26101v1)**  
  Authors: Bojia Zi, Xiaoyan Yang, Yu Zhou, Ruijie Sun, Lihan Zhang, Bin Liang, Kam-Fai Wong, Haibin Huang, Chi Zhang, Xuelong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.26101v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://huggingface.co/datasets/RefVideo6M/RefVideo6M.) | [![Dataset](https://img.shields.io/badge/-Dataset-orange)](https://huggingface.co/datasets/RefVideo6M/RefVideo6M)  
  Keywords: controllable, identity, identity-preserving, reference-guided, video editing  
- **[Long-Horizon Audio-Visual Generation for Persistent Stories and Interactive Worlds](https://arxiv.org/abs/2608.23383v2)**  
  Authors: Nan Duan, Haoyang Huang, Weiyang Jin, Haoran Li, Yaowei Li, Yuming Li, Yijun Liu, Xin Lu, Xiaoxiao Ma, Yanwen Ma, Yaofeng Su, Yilang Sun, Haoyu Wang, Zeyue Xue, Songchun Zhang, Junhao Zhuang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.23383v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://echo-team-joy-future-academy-jd.github.io/Echo-1.5-Page)  
  Keywords: audio-visual generation, efficient, identity, interactive, long video, long-form, video generation, world model  
- **[Loopy: Seamless Video Loop Generation via Anchored Looping Shift of Positional Embedding](https://arxiv.org/abs/2608.23090v1)**  
  Authors: Haotian Dong, Wenjing Wang, Chen Li, Jing Lyu, Xin Wang, Di Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.23090v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://donghaotian123.github.io/Loopy)  
  Keywords: dit, game, identity, style, temporal consistency, video generation  
- **[Identity-Preserving Text-to-Video Generation via Agentic Enhancement and Semantic Repair](https://arxiv.org/abs/2608.20749v1)**  
  Authors: Jiayi Gao, Changcheng Hua, Jiaqi Tang, Yuxin Peng, Yang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.20749v1.pdf) | [![GitHub](https://img.shields.io/github/stars/oceanflowlab/AESR?style=social)](https://github.com/oceanflowlab/AESR)  
  Keywords: evaluation, identity, identity-preserving, text to video, text-to-video, video editing, video generation  
- **[MSEditor: Toward Consistent Multi-Shot Video Editing](https://arxiv.org/abs/2608.17559v1)**  
  Authors: Kunyu Feng, Yue Ma, Bingyuan Wang, Yuefeng Wang, Zhiyuan Qin, Hao Cheng, Hao Li, Qifeng Chen, Zeyu Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.17559v1.pdf)  
  Keywords: benchmark, identity, multi-view video, video editing  
- **[GRNEdit: Efficient General Video Editing from a New Binary-Evidence Perspective in Generative Refinement Networks](https://arxiv.org/abs/2608.16328v1)**  
  Authors: Feng Xie, Jiagao Hu, Fuhao Li, Zepeng Wang, Yuxuan Chen, Dahua Gao, Fei Wang, Daiguo Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.16328v1.pdf)  
  Keywords: efficient, identity, video editing  
- **[KeyID: Decoupled Drafting and Keyframe Editing for Identity-Preserving Video Generation](https://arxiv.org/abs/2608.16154v1)**  
  Authors: Jianjie Luo, Yiming Zhong, Haoming Shen, Yupeng Xiao, Zhenguo Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.16154v1.pdf) | [![GitHub](https://img.shields.io/github/stars/WISLab-GDUT/KeyID?style=social)](https://github.com/WISLab-GDUT/KeyID)  
  Keywords: benchmark, dynamics, identity, identity-preserving, keyframe, video generation  
- **[FlowDance: Music-Driven Dance Video Generation with Parallel Pose and RGB Streams](https://arxiv.org/abs/2608.15818v1)**  
  Authors: Genying Li, Boda Lin, Jiachen Li, Zijian Jia, Haojie Zheng, Yiming Wang, Shuchen Weng, Si Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.15818v1.pdf)  
  Keywords: body motion, denoising, human animation, identity, identity-preserving, long video, video generation, video synthesis  
- **[EditStream: A Unified Autoregressive Framework for Interactive Video Generation and Editing](https://arxiv.org/abs/2608.21424v1)**  
  Authors: Yuqian Zhou, Zhenghong Zhou, Zongze Wu, Cameron Smith, Richard Zhang, Jiebo Luo, Eli Shechtman, Zhe Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.21424v1.pdf)  
  Keywords: autoregressive, autoregressive video, creative, distillation, dit, efficient, image to video, image-to-video, interactive, reference-guided, streaming, text to video, text-to-video, video editing, video generation, video to video, video-to-video  
- **[RigidBench: Evaluating Rigid-Body Physics in Video Generation Models](https://arxiv.org/abs/2608.15555v1)**  
  Authors: Swarnim Jain, Shangzhe Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.15555v1.pdf)  
  Keywords: benchmark, denoising, diffusion transformer, identity, physics, trajectory, video generation  

### Physical Understanding

*Showing the latest 50 out of 309 papers*

- **[Game2World Engine: Unlocking In-the-Wild Gameplay Videos for World Model Training](https://arxiv.org/abs/2608.24680v1)**  
  Authors: Wenxuan Shen, Dongna Jin, Dongping Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.24680v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Dongping-Chen/Game2World?style=social)](https://github.com/Dongping-Chen/Game2World)  
  Keywords: dynamics, evaluation, game, video editing, world model  
- **[NVIDIA Cosmos-H-Dreams: Real-Time Generative Physics Simulation for Surgical Robotics](https://arxiv.org/abs/2608.24199v1)**  
  Authors: Javier Gamazo Tejero, Lukas Zbinden, Keyur Sheth, Raghavendra K M, Nadim Daher, Diego Granero Maraña, Filip Binkiewicz, Patrick Thornycroft, Mahdi Azizian, Sean D. Huver  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.24199v1.pdf)  
  Keywords: action-conditioned, controllable, distillation, dynamics, education, interactive, physical, physics, robotics, simulation, streaming, video world model, world model  
- **[GlanceWAM: Sparse Test-Time Imagination for World-Action Models](https://arxiv.org/abs/2608.23927v1)**  
  Authors: Linhan Wang, Zijian An, Mingyuan Zhang, Chen Dai, Yi Xu, Can Cui, Zichong Yang, Yinlin Chen, Lifeng Zhou, Chang-Tien Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.23927v1.pdf) | [![GitHub](https://img.shields.io/github/stars/linhanwang/GlanceWAM?style=social)](https://github.com/linhanwang/GlanceWAM)  
  Keywords: benchmark, dit, physical, robot learning, video dit, video generation  
- **[GeoWAM: Visual Geometry World Action Models for Autonomous Driving](https://arxiv.org/abs/2608.23486v2)**  
  Authors: Yiren Lu, Xin Ye, Jiaming Liu, Philip Jacobson, Jin Yao, Yi-chung Chen, Liam Merino, Dhruva Dixith Kurra, Min Cai, Tom Lampo, Yu Yin, Danhua Guo, Burhan Yaman  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.23486v2.pdf)  
  Keywords: autonomous driving, driving, dynamics, trajectory, video generation  
- **[From Generation to Simulation: How Far Are World Models from Being True Simulators?](https://arxiv.org/abs/2608.23070v1)**  
  Authors: Tong Wang, Huan Deng, Mucheng Yang, Yang He, Xiaohui Kuang, Gang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.23070v1.pdf) | [![GitHub](https://img.shields.io/github/stars/AtongWang/world-model-simulators?style=social)](https://github.com/AtongWang/world-model-simulators)  
  Keywords: dynamics, evaluation, game, physical, physics, simulation, video generation, world model  
- **[LD4WAM: Learning Latent Dynamics from Human Videos for World Action Models](https://arxiv.org/abs/2608.22403v1)**  
  Authors: Zhenhao Shen, Jiaqi Liang, Jasper Lu, Feng Jiang, Yuran Wang, Chuanbo Wei, Jiayi Liu, Jianchun Yang, Qize Yu, Jiadi You, Ce Hao, Guanqi He, Chen Xie, Ruihai Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.22403v1.pdf)  
  Keywords: dynamics, simulation, video generation  
- **[DELE-w0.5: Inferring Action from Future Latent State for Robotic Manipulation](https://arxiv.org/abs/2608.22067v3)**  
  Authors: Fenghao Lei, Zhixiong Huang, Long Yang, Jiabao Chen, Peilin Huang, Han Fu, Zhuo Li, Xiaoxue Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.22067v3.pdf)  
  Keywords: physical, video generation, world model  
- **[CIVA: Critic-Induced Value-Subspace Attacks on Visual World-Model Agents](https://arxiv.org/abs/2608.21114v2)**  
  Authors: Jiancheng Wang, Mingli Zhu, Tong Zhang, Jiaqi Ruan, Wei Wang, Siyuan Liang, Dacheng Tao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.21114v2.pdf)  
  Keywords: dynamics, visual world model, world model  
- **[MotionPhys: Detecting AI-Generated Videos via Physical Consistency of Optical-Flow Trajectories](https://arxiv.org/abs/2608.20770v1)**  
  Authors: Haojin He, Hao Tan, Zichang Tan, Ajian Liu, Jun Wan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.20770v1.pdf)  
  Keywords: efficient, physical, physical consistency, trajectory, video generation  
- **[Grounded-Exo2Ego: Structured Semantic Grounding for Robust Exocentric-to-Egocentric Video Generation](https://arxiv.org/abs/2608.20534v1)**  
  Authors: Shengze Wang, Michael Stengel, Tianye Li, Seonwook Park, Amrita Mazumdar, Koki Nagano, Alex Trevithick, Shalini De Mello  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.20534v1.pdf)  
  Keywords: diffusion model, evaluation, novel view, physical, video diffusion, video generation  

### Surveys & Benchmarks

*Showing the latest 50 out of 303 papers*

- **[VBVR-Pro: A Scalable and Verifiable Suite for Native Visual Reasoning](https://arxiv.org/abs/2608.26105v1)**  
  Authors: Junxiang Xu, Ruisi Wang, Fanyi Pu, Maijunxian Wang, Ran Ji, Tongxi Zhou, Chenyang Gu, Jing Zuo, Hongcan Xiao, Yimeng Geng, Wanqi Yin, Wei Chen, Oscar Qian, Zhengan Yan, Ziqi Huang, Haiwen Diao, Liang Pan, Bo Li, Xiangyu Fan, Dezhi Luo, Fengyuan Yu, Zehong Zhao, Qingying Gao, Tinghui Zhu, Yilan Zhang, Jingqi Tong, Pinyuan Feng, Zhengze Jiang, Letian Wang, Ziyu Guo, Renrui Zhang, Jieneng Chen, Sonia Joseph, Constantin Venhoff, Saman Motamed, Mengyue Yang, Chandra Sripada, Alan Yuille, Philip Torr, Lvmin Zhang, Vikash Kumar, Daniel Khashabi, Nikolaus Kriegeskorte, Raphaël Millière, Vincent C. Müller, Anyi Rao, Quan Wang, Ziwei Liu, Dahua Lin, Lei Yang, Hokin Deng, Zhongang Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.26105v1.pdf)  
  Keywords: controllable, efficient, evaluation, video generation  
- **[One Policy, Many Embodiments: Unified Camera-Centric Action Geometry Pre-training for Heterogeneous Embodied Manipulation](https://arxiv.org/abs/2608.26058v1)**  
  Authors: Xiaomi Embodied Intelligence Team, University of Macau, :, Shaoqing Xu, Fang Li, Guozhi Zhan, Zhixiang Duan, Yuhan Wang, Yuechen Luo, Shengyin Jiang, Hanbing Li, Zhiying Du, Longlong Wang, Longmei Jiang, Weixiang Liang, Ying Gong, Yong Pan, Ziping Zhao, Zhiyuan Chen, Yangwei You, Kun Ma, Qinyuan Liu, Hangjun Ye, Zhi-xin Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.26058v1.pdf)  
  Keywords: architecture, benchmark, embodied, simulation, video synthesis  
- **[VGA-BenchV2: An Expanded Unified Benchmark and Multi-Model Framework for Evaluating Video Aesthetics and Generation Quality](https://arxiv.org/abs/2608.25452v1)**  
  Authors: Longteng Jiang, DanDan Zheng, Qianqian Qiao, Heng Huang, Huaye Wang, Yihang Bo, Bao Peng, Jingdong Chen, Jun Zhou, Xin Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.25452v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://huggingface.co/datasets/BestiVictoryLab/VGA-Bench.) | [![Dataset](https://img.shields.io/badge/-Dataset-orange)](https://huggingface.co/datasets/BestiVictoryLab/VGA-Bench)  
  Keywords: architecture, benchmark, evaluation, video generation  
- **[Game2World Engine: Unlocking In-the-Wild Gameplay Videos for World Model Training](https://arxiv.org/abs/2608.24680v1)**  
  Authors: Wenxuan Shen, Dongna Jin, Dongping Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.24680v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Dongping-Chen/Game2World?style=social)](https://github.com/Dongping-Chen/Game2World)  
  Keywords: dynamics, evaluation, game, video editing, world model  
- **[TurboT2VA: Fast Large-Scale Text-to-Video-Audio Generation via Score-Regularized Consistency Distillation](https://arxiv.org/abs/2608.24674v1)**  
  Authors: Xiaoda Yang, Yuxiang Liu, Kaiwen Zheng, Yuan Liu, Yibo Lai, Shengpeng Ji, Kai Jiang, Jianfei Chen, Xiaobin Hu, Shuicheng Yan, Jintao Zhang, Jun Zhu, Zhou Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.24674v1.pdf) | [![GitHub](https://img.shields.io/github/stars/thu-ml/TurboDiffusion?style=social)](https://github.com/thu-ml/TurboDiffusion)  
  Keywords: architecture, consistency distillation, distillation, evaluation, sparse attention, text to video, text-to-video, trajectory  
- **[How Do Professional Editors Evaluate the Editing Quality of AI-Generated Cinematic Video Ads?](https://arxiv.org/abs/2608.24329v1)**  
  Authors: Po-Ming Law, Weizhi Li, Arpit Narechania  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.24329v1.pdf)  
  Keywords: cinematic, evaluation, human evaluation, sound, video generation  
- **[OmniJudge or OmniBias? Diagnosing Multimodal Judges through Balanced, Decoupled Lenses](https://arxiv.org/abs/2608.24160v1)**  
  Authors: Guangzheng Hu, Ziyue Jiang, Weixu Qiao, Lixin Zhang, Jianye Kang, Yuru Wu, Rong Bao, Niantong Li, Wei Wang, Ziyi Cheng, Xinfa Zhu, HangRui Hu, Ting He, Bing Zhao, Lin Qu, Hu Wei, Jin Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.24160v1.pdf)  
  Keywords: benchmark, evaluation, t2v, text to video, text-to-video  
- **[GlanceWAM: Sparse Test-Time Imagination for World-Action Models](https://arxiv.org/abs/2608.23927v1)**  
  Authors: Linhan Wang, Zijian An, Mingyuan Zhang, Chen Dai, Yi Xu, Can Cui, Zichong Yang, Yinlin Chen, Lifeng Zhou, Chang-Tien Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.23927v1.pdf) | [![GitHub](https://img.shields.io/github/stars/linhanwang/GlanceWAM?style=social)](https://github.com/linhanwang/GlanceWAM)  
  Keywords: benchmark, dit, physical, robot learning, video dit, video generation  
- **[From Generation to Simulation: How Far Are World Models from Being True Simulators?](https://arxiv.org/abs/2608.23070v1)**  
  Authors: Tong Wang, Huan Deng, Mucheng Yang, Yang He, Xiaohui Kuang, Gang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.23070v1.pdf) | [![GitHub](https://img.shields.io/github/stars/AtongWang/world-model-simulators?style=social)](https://github.com/AtongWang/world-model-simulators)  
  Keywords: dynamics, evaluation, game, physical, physics, simulation, video generation, world model  
- **[FIRM-Video: Check Before You Score for Reliable Text-to-Video Reward Modeling](https://arxiv.org/abs/2608.21839v1)**  
  Authors: Peiyuan Zhang, Xiangyu Zhao, Hongbo Liu, Xiaoxing Hu, Mingxin Liu, Shuran Ma, Yunhang Shen, Jian Hu, Haihan Gao, Haoyu Cao, Xue Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.21839v1.pdf)  
  Keywords: evaluation, text to video, text-to-video  

### Text-to-Video Generation

*Showing the latest 50 out of 139 papers*

- **[TurboT2VA: Fast Large-Scale Text-to-Video-Audio Generation via Score-Regularized Consistency Distillation](https://arxiv.org/abs/2608.24674v1)**  
  Authors: Xiaoda Yang, Yuxiang Liu, Kaiwen Zheng, Yuan Liu, Yibo Lai, Shengpeng Ji, Kai Jiang, Jianfei Chen, Xiaobin Hu, Shuicheng Yan, Jintao Zhang, Jun Zhu, Zhou Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.24674v1.pdf) | [![GitHub](https://img.shields.io/github/stars/thu-ml/TurboDiffusion?style=social)](https://github.com/thu-ml/TurboDiffusion)  
  Keywords: architecture, consistency distillation, distillation, evaluation, sparse attention, text to video, text-to-video, trajectory  
- **[OmniJudge or OmniBias? Diagnosing Multimodal Judges through Balanced, Decoupled Lenses](https://arxiv.org/abs/2608.24160v1)**  
  Authors: Guangzheng Hu, Ziyue Jiang, Weixu Qiao, Lixin Zhang, Jianye Kang, Yuru Wu, Rong Bao, Niantong Li, Wei Wang, Ziyi Cheng, Xinfa Zhu, HangRui Hu, Ting He, Bing Zhao, Lin Qu, Hu Wei, Jin Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.24160v1.pdf)  
  Keywords: benchmark, evaluation, t2v, text to video, text-to-video  
- **[FIRM-Video: Check Before You Score for Reliable Text-to-Video Reward Modeling](https://arxiv.org/abs/2608.21839v1)**  
  Authors: Peiyuan Zhang, Xiangyu Zhao, Hongbo Liu, Xiaoxing Hu, Mingxin Liu, Shuran Ma, Yunhang Shen, Jian Hu, Haihan Gao, Haoyu Cao, Xue Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.21839v1.pdf)  
  Keywords: evaluation, text to video, text-to-video  
- **[Identity-Preserving Text-to-Video Generation via Agentic Enhancement and Semantic Repair](https://arxiv.org/abs/2608.20749v1)**  
  Authors: Jiayi Gao, Changcheng Hua, Jiaqi Tang, Yuxin Peng, Yang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.20749v1.pdf) | [![GitHub](https://img.shields.io/github/stars/oceanflowlab/AESR?style=social)](https://github.com/oceanflowlab/AESR)  
  Keywords: evaluation, identity, identity-preserving, text to video, text-to-video, video editing, video generation  
- **[CoinVE-200K: A Large-Scale High-Quality Dataset for Compositional Instruction-Guided Video Editing](https://arxiv.org/abs/2608.17566v2)**  
  Authors: Fuchen Long, Cong Wang, Zitao Gao, Wenhao Zhong, Yu Cheng, Xiaolu Hou, Yan Li, Xiao Cao, Xinlong Sun, Xi Chen, Yu Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.17566v2.pdf)  
  Keywords: benchmark, instruction-based video editing, instruction-guided, t2v, temporal consistency, video editing  
- **[SQuad: Sub-Quadratic Attention Distillation for Efficient Video Generation](https://arxiv.org/abs/2608.16585v1)**  
  Authors: Animesh Karnewar, Denis Korzhenkov, Amirhossein Habibian, Mohsen Ghafoorian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.16585v1.pdf)  
  Keywords: distillation, dit, efficient, flow matching, text to video, text-to-video, video diffusion, video dit, video generation  
- **[MLLM-Guided Semantic Correction for Text-to-Video Generation](https://arxiv.org/abs/2608.16513v1)**  
  Authors: Junhao Chen, Zheqi Lv, Keting Yin, Shengyu Zhang, Zhou Zhao, Feiyang Chen, Xinyu Duan, Baoxing Huai, Fei Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.16513v1.pdf)  
  Keywords: controllable, evaluation, temporal consistency, text to video, text-to-video, trajectory, video generation, video synthesis  
- **[EditStream: A Unified Autoregressive Framework for Interactive Video Generation and Editing](https://arxiv.org/abs/2608.21424v1)**  
  Authors: Yuqian Zhou, Zhenghong Zhou, Zongze Wu, Cameron Smith, Richard Zhang, Jiebo Luo, Eli Shechtman, Zhe Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.21424v1.pdf)  
  Keywords: autoregressive, autoregressive video, creative, distillation, dit, efficient, image to video, image-to-video, interactive, reference-guided, streaming, text to video, text-to-video, video editing, video generation, video to video, video-to-video  
- **[Beyond Text Conditioning: A Systematic Study of MLLM-DiT Fusion for Video Generation](https://arxiv.org/abs/2608.14043v1)**  
  Authors: Yanbo Ding, Yijia Fan, Caihua Shan, Yifan Yang, Yifei Shen, Weijie Wang, Xirui Hu, Dongsheng Li, Lili Qiu, Yuqing Yang, Yali Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.14043v1.pdf)  
  Keywords: autoregressive, dit, text to video, text-to-video, video generation  
- **[HPSD: Hybrid-Policy Self-Distillation for Text-Image-to-Video Diffusion Models](https://arxiv.org/abs/2608.13205v1)**  
  Authors: Jiazi Bu, Pengyang Ling, Yujie Zhou, Yibin Wang, Yuhang Zang, Xuanlang Dai, Shengyuan Ding, Tianyi Wei, Xiaohang Zhan, Jiaqi Wang, Tong Wu, Dahua Lin, Xingang Pan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.13205v1.pdf)  
  Keywords: architecture, distillation, i2v, image to video, image-to-video, t2v, text to video, text-to-video, trajectory, video diffusion  

### Video Editing

*Showing the latest 50 out of 104 papers*

- **[RefVideo-6M: A Reliable Reference-Based Dataset for Instructional Video Editing](https://arxiv.org/abs/2608.26101v1)**  
  Authors: Bojia Zi, Xiaoyan Yang, Yu Zhou, Ruijie Sun, Lihan Zhang, Bin Liang, Kam-Fai Wong, Haibin Huang, Chi Zhang, Xuelong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.26101v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://huggingface.co/datasets/RefVideo6M/RefVideo6M.) | [![Dataset](https://img.shields.io/badge/-Dataset-orange)](https://huggingface.co/datasets/RefVideo6M/RefVideo6M)  
  Keywords: controllable, identity, identity-preserving, reference-guided, video editing  
- **[Plans You Can Check: Verifier-Grounded Learning of an Open-Weight Planner for Executable Video-Editing](https://arxiv.org/abs/2608.25622v1)**  
  Authors: Haoyu Wang, Cheng Feng, Liuyang Bian, Ruiyang Huang, Lei Wei, Yafei Wen, Xiaoxin Chen, Xiaoying Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.25622v1.pdf)  
  Keywords: distillation, video editing  
- **[Game2World Engine: Unlocking In-the-Wild Gameplay Videos for World Model Training](https://arxiv.org/abs/2608.24680v1)**  
  Authors: Wenxuan Shen, Dongna Jin, Dongping Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.24680v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Dongping-Chen/Game2World?style=social)](https://github.com/Dongping-Chen/Game2World)  
  Keywords: dynamics, evaluation, game, video editing, world model  
- **[FixAnything: 3D-Consistent Rendering Refinement via Video Generative Priors](https://arxiv.org/abs/2608.23549v1)**  
  Authors: Khiem Vuong, Deva Ramanan, Srinivasa Narasimhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.23549v1.pdf)  
  Keywords: 3d consistent, camera motion, video to video, video translation, video-to-video  
- **[InfinityEdit: Infinite Video Editing with a Lightweight Edit-Ignition Adapter](https://arxiv.org/abs/2608.20910v1)**  
  Authors: Yunze Tong, Mushui Liu, Canyu Zhao, Shiyi Zhang, Didi Zhu, Peng Zhang, Wanggui He, Jinlong Liu, Ying Chen, Hao Jiang, Pipei Huang, Bo Zheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.20910v1.pdf)  
  Keywords: denoising, game, infinite video, instruction-based video editing, streaming, video editing  
- **[Identity-Preserving Text-to-Video Generation via Agentic Enhancement and Semantic Repair](https://arxiv.org/abs/2608.20749v1)**  
  Authors: Jiayi Gao, Changcheng Hua, Jiaqi Tang, Yuxin Peng, Yang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.20749v1.pdf) | [![GitHub](https://img.shields.io/github/stars/oceanflowlab/AESR?style=social)](https://github.com/oceanflowlab/AESR)  
  Keywords: evaluation, identity, identity-preserving, text to video, text-to-video, video editing, video generation  
- **[RoboEdit: Turning Human Manipulation Videos into Scalable Robot Experience](https://arxiv.org/abs/2608.18948v1)**  
  Authors: Yaowei Guo, Zeng Tao, Yuxin Jiang, Yunuo Chen, Zhiyang Dou, Yuxiang Ma, Yin Yang, Demetri Terzopoulos, Ying Jiang, Chenfanfu Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.18948v1.pdf)  
  Keywords: robot learning, video editing  
- **[CoinVE-200K: A Large-Scale High-Quality Dataset for Compositional Instruction-Guided Video Editing](https://arxiv.org/abs/2608.17566v2)**  
  Authors: Fuchen Long, Cong Wang, Zitao Gao, Wenhao Zhong, Yu Cheng, Xiaolu Hou, Yan Li, Xiao Cao, Xinlong Sun, Xi Chen, Yu Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.17566v2.pdf)  
  Keywords: benchmark, instruction-based video editing, instruction-guided, t2v, temporal consistency, video editing  
- **[MSEditor: Toward Consistent Multi-Shot Video Editing](https://arxiv.org/abs/2608.17559v1)**  
  Authors: Kunyu Feng, Yue Ma, Bingyuan Wang, Yuefeng Wang, Zhiyuan Qin, Hao Cheng, Hao Li, Qifeng Chen, Zeyu Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.17559v1.pdf)  
  Keywords: benchmark, identity, multi-view video, video editing  
- **[VicEdit: Learning to Edit Videos from Visual In-Context Examples](https://arxiv.org/abs/2608.16745v1)**  
  Authors: Yuji Wang, Teng Hu, Yuheng Chen, Ran Yi, Han Feng, Weijian Cao, Chengjie Wang, Lizhuang Ma, Jiangning Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.16745v1.pdf)  
  Keywords: controllable, distillation, dynamics, instruction-based video editing, multi-modal, video editing  

### Video Inpainting & Completion

- **[Stream4D: 4D-Consistency for Streaming Autoregressive Diffusion Video Models](https://arxiv.org/abs/2608.19556v1)**  
  Authors: Yuanhao Ban, Jiaqi Feng, Hengguang Zhou, Xiaohuan Pei, Justin Cui, Cho-Jui Hsieh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.19556v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://banyuanhao.github.io/Stream4D)  
  Keywords: autoregressive, autoregressive video, dynamics, frame prediction, streaming, video generation  
- **[V-RAE: Rethinking Video Latent Spaces for Generation](https://arxiv.org/abs/2608.13556v1)**  
  Authors: Minghui Guo, Shengqiong Wu, Hao Fei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.13556v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://v-rae.github.io)  
  Keywords: latent video, video autoencoder, video generation, video prediction, video tokenizer  
- **[GeoRoute: Geometry-Aware Hybrid Inference for Traffic Future-Frame Prediction](https://arxiv.org/abs/2608.09493v1)**  
  Authors: Khang Minh Le, Hieu Dinh Trung Pham, Luu Thanh Danh, Nam-Tien Le, Hieu Anh Ngo, Phuong Huu Vu Tran, Son Nguyen Minh Le, Nguyen Trong Nghia, Tu Tran Thi Cam, Huy Minh Nhat Nguyen, Cuong Tuan Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.09493v1.pdf)  
  Keywords: architecture, autonomous driving, benchmark, driving, frame prediction, future frame prediction, latent video, latent video diffusion, video diffusion  
- **[SimWAM: A Simple World Action Model for End-to-End Autonomous Driving](https://arxiv.org/abs/2608.07468v3)**  
  Authors: Zongchuang Zhao, Xin Zhou, Tianyang Xu, Zhengyang Sun, Kaixuan Zhou, Honglin Li, Dingkang Liang, Xiang Bai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.07468v3.pdf) | [![GitHub](https://img.shields.io/github/stars/H-EmbodVis/SimWAM?style=social)](https://github.com/H-EmbodVis/SimWAM)  
  Keywords: autonomous driving, driving, dynamics, efficient, flow matching, trajectory, video generation, video prediction  
- **[MirrorWorld: Taming Video Diffusion Models for Mirror Reflection Generation](https://arxiv.org/abs/2608.07463v1)**  
  Authors: Youjun Zhao, Alex Warren, Gary K. L. Tam, Rynson W. H. Lau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.07463v1.pdf)  
  Keywords: benchmark, distillation, video diffusion, video inpainting, video synthesis  
- **[UniVVT: A Unified End-to-End Framework for High-Fidelity Video Virtual Try-on](https://arxiv.org/abs/2608.05745v1)**  
  Authors: Yushe Cao, Shikun Feng, Fei Shen, Haikuo Peng, Jianqiang Xia, Yiheng Zhu, Dianxi Shi, Chun Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05745v1.pdf)  
  Keywords: dynamics, identity, video generation, video inpainting, virtual try-on  
- **[CrossScope: A Role-Asymmetric World Model for Joint Dual-Scope Surgical Video Prediction](https://arxiv.org/abs/2608.03211v1)**  
  Authors: Wanhao Liu, Jinsong Lin, Rulin Zhou, Chi Kit Ng, Wenbin Pan, Zhiqing Tang, Dongyue Li, Liwei Luo, Yanshen Wu, Panshuo Li, Zhiyong Xiong, Huxin Gao, Tamas Haidegger, Hongliang Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.03211v1.pdf)  
  Keywords: benchmark, dynamics, video generation, video prediction, world model  
- **[CameraAnything: Refilming Videos with Arbitrary Camera Control](https://arxiv.org/abs/2607.24591v1)**  
  Authors: Yixuan Li, Yanhong Zeng, Ka Leong Cheng, Jiayi Zhu, Hanlin Wang, Wen Wang, Yihao Meng, Hao Ouyang, Qiuyu Wang, Yue Yu, ZiDong Wang, Yiyuan Zhang, Yujun Shen, Dahua Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.24591v1.pdf)  
  Keywords: camera control, cinematic, outpainting, video editing  
- **[The Seriality Gap in Video Diffusion Models](https://arxiv.org/abs/2607.13031v1)**  
  Authors: Jorge Diaz Chao, Konpat Preechakul, Yuxi Liu, Yutong Bai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.13031v1.pdf)  
  Keywords: autoregressive, denoising, dynamics, simulation, video diffusion, video prediction  
- **[Video Generation Models Are Inherent Lighting Estimators](https://arxiv.org/abs/2607.04674v1)**  
  Authors: Ziqi Cai, Shuchen Weng, Kaiqi Liu, Zifeng Wang, Zhiquan Zhang, Minggui Teng, Han Jiang, Boxin Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.04674v1.pdf)  
  Keywords: efficient, physical, video diffusion, video generation, video inpainting  

### Video Super-Resolution & Enhancement

*Showing the latest 50 out of 162 papers*

- **[4DStreamCtrl: Interactive Video Generation with Online 4D Control](https://arxiv.org/abs/2608.25479v1)**  
  Authors: Shiqian Li, Chenguo Lin, Zhiguang Liu, Yu Tang, Jiarong Ou, Rui Chen, Yixin Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.25479v1.pdf)  
  Keywords: 3d consistent, camera motion, controllable, denoising, diffusion model, efficient, embodied, interactive, long video, motion control, motion transfer, streaming, trajectory, video diffusion, video generation  
- **[Generalization, memorization, and overfitting for diffusion models trained in the lazy high-dimensional regime](https://arxiv.org/abs/2608.23938v1)**  
  Authors: Hugo Latourelle-Vigeant, Sinho Chewi, Aram-Alexandre Pooladian, John Sous, Theodor Misiakiewicz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.23938v1.pdf)  
  Keywords: denoising, video synthesis  
- **[Scaling Reinforcement Learning for Diffusion Models via Velocity Matching](https://arxiv.org/abs/2608.23664v1)**  
  Authors: Jaemoo Choi, Wei Guo, Yuchen Zhu, Arash Vahdat, Molei Tao, Julius Berner, Yongxin Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.23664v1.pdf)  
  Keywords: autoregressive, denoising, trajectory, video generation  
- **[GaussVid: Sparse-View Gaussian Splatting with 3D-Aware Video Diffusion Priors](https://arxiv.org/abs/2608.21849v1)**  
  Authors: Xinhui Liu, Can Wang, Wei Jiang, Wei Wang, Dong Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.21849v1.pdf)  
  Keywords: 3d-aware, camera-conditioned, novel view, video diffusion, video generation, video restoration  
- **[InfinityEdit: Infinite Video Editing with a Lightweight Edit-Ignition Adapter](https://arxiv.org/abs/2608.20910v1)**  
  Authors: Yunze Tong, Mushui Liu, Canyu Zhao, Shiyi Zhang, Didi Zhu, Peng Zhang, Wanggui He, Jinlong Liu, Ying Chen, Hao Jiang, Pipei Huang, Bo Zheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.20910v1.pdf)  
  Keywords: denoising, game, infinite video, instruction-based video editing, streaming, video editing  
- **[4DAnyone: Create Anyone in 4D from a Casual Monocular Video](https://arxiv.org/abs/2608.20335v1)**  
  Authors: Yudong Jin, Tao Xie, Qihang Zhang, Zehong Shen, Zhen Xu, Yujun Shen, Hujun Bao, Xiaowei Zhou, Yinghao Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.20335v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://4danyone.github.io)  
  Keywords: denoising, dit, game, novel view, video diffusion  
- **[VGI-Bench: Probing Visual Intelligence in Video Generation Models](https://arxiv.org/abs/2608.19583v3)**  
  Authors: Xuan He, Cong Wei, Yuhao Cheng, Linrui Ma, Yuxuan Zhang, Zuojun Li, Yuhao Wen, Jize Jiang, Zeyi Liu, Yuren Hao, Songcheng Cai, Keming Wu, Penghui Du, Kai Zou, Rui Yang, Chenkai Sun, Ke Yang, Ping Nie, Kelsey R Allen, Chenglong Wang, Michel Galley, Jianfeng Gao, ChengXiang Zhai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.19583v3.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://hexuan21.github.io/VGI-Bench)  
  Keywords: denoising, evaluation, video generation  
- **[Magnitude-Direction Decoupling for Fast Video Generation with Flow Matching Models](https://arxiv.org/abs/2608.17695v1)**  
  Authors: Haonan Xu, Feiyang Chen, Songkui Chen, Hongpeng Pan, Zhefeng Wang, Xinyu Duan, Baoxing Huai, Yang Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.17695v1.pdf)  
  Keywords: acceleration, denoising, flow matching, trajectory, video generation  
- **[DriveCache: Action-Aware Caching for Driving World Model Inference](https://arxiv.org/abs/2608.16354v1)**  
  Authors: Jianchun Yang, Jian Liang, Xianda Guo, Pinhan Fu, Yanlun Peng, Conglang Zhang, Wenke Huang, Mang Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.16354v1.pdf)  
  Keywords: acceleration, autonomous driving, controllable, denoising, driving, driving world model, evaluation, simulation, video generation, world model  
- **[FlowDance: Music-Driven Dance Video Generation with Parallel Pose and RGB Streams](https://arxiv.org/abs/2608.15818v1)**  
  Authors: Genying Li, Boda Lin, Jiachen Li, Zijian Jia, Haojie Zheng, Yiming Wang, Shuchen Weng, Si Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.15818v1.pdf)  
  Keywords: body motion, denoising, human animation, identity, identity-preserving, long video, video generation, video synthesis  

### World Models & Simulation

*Showing the latest 50 out of 258 papers*

- **[One Policy, Many Embodiments: Unified Camera-Centric Action Geometry Pre-training for Heterogeneous Embodied Manipulation](https://arxiv.org/abs/2608.26058v1)**  
  Authors: Xiaomi Embodied Intelligence Team, University of Macau, :, Shaoqing Xu, Fang Li, Guozhi Zhan, Zhixiang Duan, Yuhan Wang, Yuechen Luo, Shengyin Jiang, Hanbing Li, Zhiying Du, Longlong Wang, Longmei Jiang, Weixiang Liang, Ying Gong, Yong Pan, Ziping Zhao, Zhiyuan Chen, Yangwei You, Kun Ma, Qinyuan Liu, Hangjun Ye, Zhi-xin Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.26058v1.pdf)  
  Keywords: architecture, benchmark, embodied, simulation, video synthesis  
- **[4DStreamCtrl: Interactive Video Generation with Online 4D Control](https://arxiv.org/abs/2608.25479v1)**  
  Authors: Shiqian Li, Chenguo Lin, Zhiguang Liu, Yu Tang, Jiarong Ou, Rui Chen, Yixin Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.25479v1.pdf)  
  Keywords: 3d consistent, camera motion, controllable, denoising, diffusion model, efficient, embodied, interactive, long video, motion control, motion transfer, streaming, trajectory, video diffusion, video generation  
- **[Game2World Engine: Unlocking In-the-Wild Gameplay Videos for World Model Training](https://arxiv.org/abs/2608.24680v1)**  
  Authors: Wenxuan Shen, Dongna Jin, Dongping Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.24680v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Dongping-Chen/Game2World?style=social)](https://github.com/Dongping-Chen/Game2World)  
  Keywords: dynamics, evaluation, game, video editing, world model  
- **[NVIDIA Cosmos-H-Dreams: Real-Time Generative Physics Simulation for Surgical Robotics](https://arxiv.org/abs/2608.24199v1)**  
  Authors: Javier Gamazo Tejero, Lukas Zbinden, Keyur Sheth, Raghavendra K M, Nadim Daher, Diego Granero Maraña, Filip Binkiewicz, Patrick Thornycroft, Mahdi Azizian, Sean D. Huver  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.24199v1.pdf)  
  Keywords: action-conditioned, controllable, distillation, dynamics, education, interactive, physical, physics, robotics, simulation, streaming, video world model, world model  
- **[Long-Horizon Audio-Visual Generation for Persistent Stories and Interactive Worlds](https://arxiv.org/abs/2608.23383v2)**  
  Authors: Nan Duan, Haoyang Huang, Weiyang Jin, Haoran Li, Yaowei Li, Yuming Li, Yijun Liu, Xin Lu, Xiaoxiao Ma, Yanwen Ma, Yaofeng Su, Yilang Sun, Haoyu Wang, Zeyue Xue, Songchun Zhang, Junhao Zhuang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.23383v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://echo-team-joy-future-academy-jd.github.io/Echo-1.5-Page)  
  Keywords: audio-visual generation, efficient, identity, interactive, long video, long-form, video generation, world model  
- **[From Generation to Simulation: How Far Are World Models from Being True Simulators?](https://arxiv.org/abs/2608.23070v1)**  
  Authors: Tong Wang, Huan Deng, Mucheng Yang, Yang He, Xiaohui Kuang, Gang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.23070v1.pdf) | [![GitHub](https://img.shields.io/github/stars/AtongWang/world-model-simulators?style=social)](https://github.com/AtongWang/world-model-simulators)  
  Keywords: dynamics, evaluation, game, physical, physics, simulation, video generation, world model  
- **[LD4WAM: Learning Latent Dynamics from Human Videos for World Action Models](https://arxiv.org/abs/2608.22403v1)**  
  Authors: Zhenhao Shen, Jiaqi Liang, Jasper Lu, Feng Jiang, Yuran Wang, Chuanbo Wei, Jiayi Liu, Jianchun Yang, Qize Yu, Jiadi You, Ce Hao, Guanqi He, Chen Xie, Ruihai Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.22403v1.pdf)  
  Keywords: dynamics, simulation, video generation  
- **[DELE-w0.5: Inferring Action from Future Latent State for Robotic Manipulation](https://arxiv.org/abs/2608.22067v3)**  
  Authors: Fenghao Lei, Zhixiong Huang, Long Yang, Jiabao Chen, Peilin Huang, Han Fu, Zhuo Li, Xiaoxue Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.22067v3.pdf)  
  Keywords: physical, video generation, world model  
- **[CIVA: Critic-Induced Value-Subspace Attacks on Visual World-Model Agents](https://arxiv.org/abs/2608.21114v2)**  
  Authors: Jiancheng Wang, Mingli Zhu, Tong Zhang, Jiaqi Ruan, Wei Wang, Siyuan Liang, Dacheng Tao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.21114v2.pdf)  
  Keywords: dynamics, visual world model, world model  
- **[Hydra-0: Action Flow for Generalist World Modeling and Control](https://arxiv.org/abs/2608.18077v1)**  
  Authors: Hongyu Li, Bowen Wen, Xinghao Zhu, Yixuan Wang, Yilun Du, Yunzhu Li, George Konidaris, Stan Birchfield, Soha Pouya, Chenran Li, Yan Chang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.18077v1.pdf)  
  Keywords: action-conditioned, benchmark, efficient, evaluation, video generation, world model  



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
      "both_abstract_and_title": ["video diffusion", "video generation", "text-to-video", "video-to-video"],
      "abstract_only": ["diffusion-based video generation", "flow-based video generation"],
      "title_only": ["world foundation model", "world simulator", "video tokenizer"]
    },
    "domains": ["cs.CV", "cs.AI", "cs.MM", "cs.LG", "cs.RO", "cs.GR", "eess.IV"],
    "time_range": {
      "mode": "relative",
      "relative": "1y"
    },
    "max_results": 1000
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
