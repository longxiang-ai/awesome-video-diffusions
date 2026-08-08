# Awesome Video Diffusions [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Video Diffusion Models and Video Generation. Content is automatically updated daily.

> Last Update: 2026-08-08 13:00:55

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

- [3D-aware Video Generation](#3d-aware-video-generation) (58 papers) - Video generation with 3D awareness, multi-view consistency, and 4D content creation
- [Applications](#applications) (213 papers) - Domain-specific applications of video diffusion models
- [Architecture & Efficiency](#architecture-&-efficiency) (388 papers) - Architectural innovations (DiT, UNet), flow matching, and training/inference efficiency
- [Audio & Multi-modal](#audio-&-multi-modal) (62 papers) - Audio-driven and multi-modal conditioned video generation
- [Controllable Generation](#controllable-generation) (327 papers) - Controllable video generation with motion, camera, pose, or layout guidance
- [Human & Character Animation](#human-&-character-animation) (69 papers) - Human-centric video generation including talking heads, dance, and character animation
- [Image-to-Video Generation](#image-to-video-generation) (99 papers) - Methods for animating still images into videos
- [Long Video Generation](#long-video-generation) (268 papers) - Generating temporally consistent long-form videos beyond short clips
- [Personalization & Customization](#personalization-&-customization) (183 papers) - Personalized video generation with custom subjects, identities, or styles
- [Physical Understanding](#physical-understanding) (316 papers) - Physics-aware video generation and dynamics modeling
- [Surveys & Benchmarks](#surveys-&-benchmarks) (292 papers) - Survey papers, benchmarks, and evaluation metrics for video generation
- [Text-to-Video Generation](#text-to-video-generation) (135 papers) - Foundation models and methods for generating videos from text prompts
- [Video Editing](#video-editing) (107 papers) - Diffusion-based video editing, style transfer, and manipulation
- [Video Inpainting & Completion](#video-inpainting-&-completion) (24 papers) - Video inpainting, completion, outpainting, and temporal prediction
- [Video Super-Resolution & Enhancement](#video-super-resolution-&-enhancement) (148 papers) - Video quality improvement, upscaling, restoration, and frame interpolation
- [World Models & Simulation](#world-models-&-simulation) (253 papers) - Video generation as world simulators and interactive environment generation



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3D-aware Video Generation

*Showing the latest 50 out of 58 papers*

- **[EmoWorld: A Decoupled Affective Field for Controllable Emotional Video Generation](https://arxiv.org/abs/2608.06231v1)**  
  Authors: Bingyuan Wang, Baistan Zhyldyzbekov, Kunyu Feng, Zeyu Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.06231v1.pdf)  
  Keywords: camera-conditioned, controllable, denoising, diffusion transformer, dit, flow matching, image to video, image-to-video, text to video, text-to-video, video diffusion, video diffusion transformer, video dit, video generation  
- **[UniWorld-View: Large-Baseline View Synthesis via Video Diffusion Models](https://arxiv.org/abs/2608.04701v1)**  
  Authors: Haiyang Zhou, Wangbo Yu, Chaoran Feng, Xunyu Zhou, Yonghong Tian, Li Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.04701v1.pdf)  
  Keywords: benchmark, camera control, controllable, novel view, video diffusion  
- **[AniGS: Bridging Rendering and Diffusion Prior for 3D Scene Animation](https://arxiv.org/abs/2607.18539v1)**  
  Authors: Yen-Chi Cheng, Chen Gao, Chuhan Chen, Tuotuo Li, Rajvi Shah, Ayush Saraf, Changil Kim, Liangyan Gui, Alexander Schwing, Johannes Kopf, Hung-Yu Tseng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.18539v1.pdf)  
  Keywords: diffusion model, dynamics, novel view, video diffusion, video to video, video-to-video  
- **[PE-Field 4D: Video Generation Models as Canvas](https://arxiv.org/abs/2607.15667v1)**  
  Authors: Yunpeng Bai, Haoxiang Li, Qixing Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.15667v1.pdf) | [![GitHub](https://img.shields.io/github/stars/MTLab/PE-Field?style=social)](https://github.com/MTLab/PE-Field)  
  Keywords: camera motion, camera trajectory, controllable, denoising, diffusion model, novel view, trajectory, video diffusion, video editing, video generation, video synthesis  
- **[Delving into the Temporal Challenges of Unified Video Protection Against Image-to-Video and Fine-Tuning-based Customization](https://arxiv.org/abs/2607.13336v1)**  
  Authors: Yuxin Huang, Ziming Hong, Mingming Gong, Wanyu Wang, Jing Zhang, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.13336v1.pdf)  
  Keywords: 3d video, customization, diffusion model, identity, image to video, image-to-video, video diffusion, video generation  
- **[4D Human-Scene Reconstruction from Low-Overlap Captures](https://arxiv.org/abs/2607.09125v1)**  
  Authors: Minhyuk Hwang, Sangmin Kim, Seunguk Do, Daneul Kim, Jaesik Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.09125v1.pdf)  
  Keywords: diffusion model, identity, novel view, trajectory, video diffusion  
- **[MV-Forcing: Long Multi-View Video Generation via 4D-Grounded Spatio-Temporal Self-Forcing](https://arxiv.org/abs/2607.05376v1)**  
  Authors: Gal Fiebelman, Hadar Averbuch-Elor, Sagie Benaim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.05376v1.pdf)  
  Keywords: autoregressive, denoising, diffusion model, distillation, multi-view video, multi-view video generation, video diffusion, video generation, view-consistent  
- **[HandsOnWorld: Unconstrained Egocentric Video Generation with Camera-Disentangled Hand Control](https://arxiv.org/abs/2607.02075v1)**  
  Authors: Yushuo Chen, Xiaoyu Shi, Xiaoshi Wu, Xintao Wang, Pengfei Wan, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.02075v1.pdf)  
  Keywords: 3d-aware, video generation  
- **[NeoMap: Training-free Novel-View Synthesis from Single Images and Videos](https://arxiv.org/abs/2607.01962v1)**  
  Authors: Jinxi Li, Tianyi Zhang, Yafei Yang, Zihui Zhang, Peng Huang, Koon Wing Macgyver Lin, Bo Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.01962v1.pdf)  
  Keywords: denoising, novel view, video synthesis, view-consistent  
- **[SimWorlds: A Multi-Agent System for Dynamic 3D Scene Creation](https://arxiv.org/abs/2607.01766v1)**  
  Authors: Chunjiang Liu, Xiaoyuan Wang, Haoyu Chen, Yizhou Zhao, Ming-Hsuan Yang, László A. Jeni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.01766v1.pdf)  
  Keywords: benchmark, driving, dynamic 3d, embodied, layout, physical, physical consistency, physics, video generation  

### Applications

*Showing the latest 50 out of 213 papers*

- **[Adaptive-WAM: Quality-Guided Early-Exit Planning from Intermediate Video-Diffusion Features](https://arxiv.org/abs/2608.06008v1)**  
  Authors: Sining Ang, Yuguang Yang, Yan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.06008v1.pdf)  
  Keywords: autonomous driving, denoising, diffusion model, diffusion transformer, dit, driving, trajectory, video denoising, video diffusion, video generation, video synthesis, video world model, world model  
- **[GAUGE: A Measurement-Grounded Benchmark for Physical Fidelity in Simulation Engines and Video World Models](https://arxiv.org/abs/2608.05948v1)**  
  Authors: Shuai Wang, Yaxin Feng, Xuekun Jiang, Shihan Tian, Ningyu Yan, Xing Shen, Chaoyang Lyu, Hui Wang, Yunsong Zhou, Hanqing Wang, Jiangmiao Pang, Yang Xiang, Xing Gao, Chunhua Shen, Weinan Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05948v1.pdf)  
  Keywords: benchmark, embodied, evaluation, image to video, image-to-video, physical, physics, simulation, trajectory  
- **[Vorch-IR: Long-Form Unified Multimodal Identity Replacement Video Generation](https://arxiv.org/abs/2608.05648v1)**  
  Authors: Yaole Wang, Xiaoyu Chen, Xin Ma, Yang Ding, Gang Yue, Jingjing Chen, Lin Ma, Yaohui Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05648v1.pdf)  
  Keywords: autoregressive, driving, evaluation, human evaluation, identity, layout, long-form, minute-long, video generation  
- **[MobileWAM: Bridging World Action Models to Mobile Manipulation with Chain-of-Foresight](https://arxiv.org/abs/2608.04657v2)**  
  Authors: Zehua Fan, Junjie He, Wenxuan Song, Xi Wang, Wenqi Lyu, Linge Zhao, Fuhao Li, Zihan You, Yifei Yang, Kaiming Xu, Qi Jiang, Yue Jiang, Haoang Li, Cheng Chi, Feng Gao, Bailin Li, Yan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.04657v2.pdf)  
  Keywords: architecture, denoising, diffusion transformer, dynamics, robot learning, video diffusion, video diffusion transformer, video generation  
- **[muSync-GS: Physics-Synchronized Driving Video Synthesis for Weather and Geometric Road Hazards](https://arxiv.org/abs/2608.04412v1)**  
  Authors: Yang Chen, Yicheng Zhu, Tao Li, Zilin Bian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.04412v1.pdf)  
  Keywords: autonomous driving, camera motion, camera trajectory, controllable, driving, dynamics, physical, physics, trajectory, video generation, video synthesis  
- **[OmniVR: Joint Video-Audio Conditional Generation for Restoring Degraded Historical Films](https://arxiv.org/abs/2608.04224v1)**  
  Authors: Xin Lu, Zihao Fan, Mingchen Zhong, Jie Huang, Xueyang Fu, Zheng-Jun Zha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.04224v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xin1u.github.io/OminiVR_PAGE)  
  Keywords: architecture, audio-video generation, benchmark, dit, film, i2v, image to video, image-to-video, joint audio-video, long video, temporal consistency, video generation, video restoration, video-to-audio  
- **[SUV: Future Scene Understanding as Video Generation for End-to-End Driving](https://arxiv.org/abs/2608.03084v1)**  
  Authors: Yibo Yuan, Jiacheng Fu, Jiangtong Zhu, Yi Li, Jianhua Han, Meng Tian, Zhuohan Liu, Zhiwei Xiong, Hang Xu, Jianwu Fang, Jianru Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.03084v1.pdf)  
  Keywords: benchmark, driving, dynamics, trajectory, video foundation model, video generation  
- **[UniMoCa: Unifying Motion and Camera Controls as Visual Proxies for Faithful Human Video Generation](https://arxiv.org/abs/2608.01944v1)**  
  Authors: Liming Tan, Ye Chen, Hao Zhang, Lirong Qian, Feifei Li, Bingbing Ni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01944v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://tanliming-daniel.github.io/UniMoCa)  
  Keywords: camera control, camera trajectory, driving, human motion, i2v, identity, motion control, temporal consistency, trajectory, video generation  
- **[MiniWorld: Democratizing the Training of Video World Models from Scratch](https://arxiv.org/abs/2608.01127v2)**  
  Authors: Yian Zhao, Ruochong Zheng, Hongcan Guo, Yu Yan, Jian Zhang, Jie Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01127v2.pdf)  
  Keywords: autoregressive, autoregressive video, denoising, diffusion transformer, distillation, dynamics, efficient, embodied, flow matching, interactive, simulation, streaming, video diffusion, video diffusion transformer, video generation  
- **[FlexComposer: Unified Video Compositing from Images to Dynamic Footage with Flexible Trajectory Control](https://arxiv.org/abs/2607.29627v1)**  
  Authors: Songchun Zhang, Sitong Guo, Xianghao Kong, Pengwei Liu, Yuwei Guo, Lvmin Zhang, Anyi Rao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.29627v1.pdf)  
  Keywords: cinematic, dynamics, motion control, simulation, temporal consistency, trajectory  

### Architecture & Efficiency

*Showing the latest 50 out of 388 papers*

- **[EmoWorld: A Decoupled Affective Field for Controllable Emotional Video Generation](https://arxiv.org/abs/2608.06231v1)**  
  Authors: Bingyuan Wang, Baistan Zhyldyzbekov, Kunyu Feng, Zeyu Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.06231v1.pdf)  
  Keywords: camera-conditioned, controllable, denoising, diffusion transformer, dit, flow matching, image to video, image-to-video, text to video, text-to-video, video diffusion, video diffusion transformer, video dit, video generation  
- **[Sample-Adaptive Latent Rewards for Uncertainty-Guided Diffusion Post-Training](https://arxiv.org/abs/2608.06125v1)**  
  Authors: Rui Li, Yuanzhi Liang, Ke Hao, Ziqiao Weng, Haibin Huang, Chi Zhang, XueLong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.06125v1.pdf)  
  Keywords: denoising, efficient, trajectory, video diffusion  
- **[Adaptive-WAM: Quality-Guided Early-Exit Planning from Intermediate Video-Diffusion Features](https://arxiv.org/abs/2608.06008v1)**  
  Authors: Sining Ang, Yuguang Yang, Yan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.06008v1.pdf)  
  Keywords: autonomous driving, denoising, diffusion model, diffusion transformer, dit, driving, trajectory, video denoising, video diffusion, video generation, video synthesis, video world model, world model  
- **[Vorch-Omni: Multi-Task Orchestration of Sight and Sound](https://arxiv.org/abs/2608.05803v1)**  
  Authors: Vorch Team, Xiaoyu Chen, Yang Ding, Cong Han, Menglin Han, Yuxin Hong, Jiebo Hou, Zequn Jie, Xiang Li, Jing Liu, Qi Liu, Yulei Lu, Siyuan Luo, Lin Ma, Xin Ma, Yinlong Qian, Peng Shi, Fang Wan, Siqi Wang, Yaohui Wang, Yaole Wang, Yidi Wu, Siqian Yang, Mingyu Yin, Haoran Yu, Gang Yue, Lisai Zhang, Yuting Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05803v1.pdf)  
  Keywords: audio-driven, audio-visual generation, diffusion transformer, flow matching, sound, text to video, text-to-video  
- **[Vorch-Director: Interactive World Story Model via Noise-Aware Error Rectification](https://arxiv.org/abs/2608.05776v1)**  
  Authors: Lisai Zhang, Yidi Wu, Qi Liu, Xin Ma, Yang Ding, Gang Yue, Siqian Yang, Jingyuan Chen, Lin Ma, Yaohui Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05776v1.pdf)  
  Keywords: audio-visual generation, autoregressive, benchmark, denoising, diffusion transformer, efficient, flow matching, identity, interactive, long video, reference-guided, video generation  
- **[Vorch-Streamer: Extending Human Audio-Visual Generation to Real-Time Long-Form Streaming](https://arxiv.org/abs/2608.05663v1)**  
  Authors: Menglin Han, Yang Ding, Yulei Lu, Haoran Yu, Xin Ma, Junyi Chen, Zhangkai Ni, Lin Ma, Yaohui Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05663v1.pdf)  
  Keywords: audio-video generation, audio-visual generation, avatar, denoising, distillation, identity, long-form, streaming, video generation  
- **[Multimodal Spatiotemporal Atmospheric Data Assimilation with Latent Video Flow-matching](https://arxiv.org/abs/2608.05103v2)**  
  Authors: Dibyajyoti Chakraborty, Romit Maulik  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05103v2.pdf)  
  Keywords: flow matching, latent video, trajectory, video flow matching  
- **[HelloWorld: Enabling Socially Interactive Characters in Video World Models](https://arxiv.org/abs/2608.05070v1)**  
  Authors: Liangyang Ouyang, Ruicong Liu, Xuangeng Chu, Kaipeng Zhang, Yoichi Sato  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05070v1.pdf) | [![GitHub](https://img.shields.io/github/stars/AlayaLab/HelloWorld?style=social)](https://github.com/AlayaLab/HelloWorld)  
  Keywords: benchmark, camera motion, distillation, dit, evaluation, interactive, video generation, video world model, world model  
- **[In-Context Forcing: Uncovering Context Effects in Autoregressive Video Diffusion](https://arxiv.org/abs/2608.05237v1)**  
  Authors: Lingxiao Yang, Liu Liu, Moran Li, Han Feng, Wenjian Cao, Jiangning Zhang, Ye Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05237v1.pdf)  
  Keywords: acceleration, autoregressive, autoregressive video, denoising, dynamics, temporal consistency, video diffusion  
- **[MobileWAM: Bridging World Action Models to Mobile Manipulation with Chain-of-Foresight](https://arxiv.org/abs/2608.04657v2)**  
  Authors: Zehua Fan, Junjie He, Wenxuan Song, Xi Wang, Wenqi Lyu, Linge Zhao, Fuhao Li, Zihan You, Yifei Yang, Kaiming Xu, Qi Jiang, Yue Jiang, Haoang Li, Cheng Chi, Feng Gao, Bailin Li, Yan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.04657v2.pdf)  
  Keywords: architecture, denoising, diffusion transformer, dynamics, robot learning, video diffusion, video diffusion transformer, video generation  

### Audio & Multi-modal

*Showing the latest 50 out of 62 papers*

- **[Vorch-Omni: Multi-Task Orchestration of Sight and Sound](https://arxiv.org/abs/2608.05803v1)**  
  Authors: Vorch Team, Xiaoyu Chen, Yang Ding, Cong Han, Menglin Han, Yuxin Hong, Jiebo Hou, Zequn Jie, Xiang Li, Jing Liu, Qi Liu, Yulei Lu, Siyuan Luo, Lin Ma, Xin Ma, Yinlong Qian, Peng Shi, Fang Wan, Siqi Wang, Yaohui Wang, Yaole Wang, Yidi Wu, Siqian Yang, Mingyu Yin, Haoran Yu, Gang Yue, Lisai Zhang, Yuting Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05803v1.pdf)  
  Keywords: audio-driven, audio-visual generation, diffusion transformer, flow matching, sound, text to video, text-to-video  
- **[Vorch-Director: Interactive World Story Model via Noise-Aware Error Rectification](https://arxiv.org/abs/2608.05776v1)**  
  Authors: Lisai Zhang, Yidi Wu, Qi Liu, Xin Ma, Yang Ding, Gang Yue, Siqian Yang, Jingyuan Chen, Lin Ma, Yaohui Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05776v1.pdf)  
  Keywords: audio-visual generation, autoregressive, benchmark, denoising, diffusion transformer, efficient, flow matching, identity, interactive, long video, reference-guided, video generation  
- **[Vorch-Streamer: Extending Human Audio-Visual Generation to Real-Time Long-Form Streaming](https://arxiv.org/abs/2608.05663v1)**  
  Authors: Menglin Han, Yang Ding, Yulei Lu, Haoran Yu, Xin Ma, Junyi Chen, Zhangkai Ni, Lin Ma, Yaohui Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05663v1.pdf)  
  Keywords: audio-video generation, audio-visual generation, avatar, denoising, distillation, identity, long-form, streaming, video generation  
- **[OmniVR: Joint Video-Audio Conditional Generation for Restoring Degraded Historical Films](https://arxiv.org/abs/2608.04224v1)**  
  Authors: Xin Lu, Zihao Fan, Mingchen Zhong, Jie Huang, Xueyang Fu, Zheng-Jun Zha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.04224v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xin1u.github.io/OminiVR_PAGE)  
  Keywords: architecture, audio-video generation, benchmark, dit, film, i2v, image to video, image-to-video, joint audio-video, long video, temporal consistency, video generation, video restoration, video-to-audio  
- **[EchoCache: Energy-Guided Cross-Modal Caching for Efficient Audio-Driven Video Generation](https://arxiv.org/abs/2608.02474v1)**  
  Authors: Jiayu Chen, Xiaoyu Wu, Rongshan Gao, Maoliang Li, Zihao Zheng, Xinhao Sun, Hailong Zou, Guojie Luo, Xiang Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.02474v1.pdf) | [![GitHub](https://img.shields.io/github/stars/IF-LAB-PKU/EchoCache?style=social)](https://github.com/IF-LAB-PKU/EchoCache)  
  Keywords: audio-driven, benchmark, denoising, efficient, video generation  
- **[AcoustiTrace: When Plausible Sound Violates Physics](https://arxiv.org/abs/2608.02035v1)**  
  Authors: Shiyang Li, Yuewen Cao, Yihao Liu, Yuandong Pu, Baochang Zhang, Xiaofei Li, Changqing Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.02035v1.pdf)  
  Keywords: audio-video generation, benchmark, evaluation, physical, physics, sound, video generation  
- **[LeapTalk: Breaking the Latency-Quality Trade-off in Talking Head Generation](https://arxiv.org/abs/2608.00079v1)**  
  Authors: Rongxiang Zhang, Songhua Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.00079v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zhangrongxiang.github.io/leaptalk-page)  
  Keywords: audio-driven, autoregressive, distillation, identity, long-form, streaming, talking head, video generation  
- **[Ripple: Real-Time Streaming Audio-Video Generation With Cross-Modal Recurrent Memory](https://arxiv.org/abs/2607.26818v1)**  
  Authors: Yanbo Ding, Zhizhi Guo, Quanyue Song, Yishan He, Zhixiang He, Yongxiang Li, Yali Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.26818v1.pdf)  
  Keywords: audio-video generation, distillation, efficient, joint audio-video, long video, long-form, streaming, video generation  
- **[TaoMate: Anchor-Guided Memory Bridging Evolving and Reference States for Real-Time Audio-Video Digital Human Generation](https://arxiv.org/abs/2607.24359v1)**  
  Authors: Qijun Gan, Chenwei Zhang, Meiguang Jin, Junfeng Ma, Qiu Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.24359v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://taoliveaigc.github.io/TaoMate)  
  Keywords: audio-video generation, autoregressive, denoising, digital human, distillation, joint audio-video, long-form, long-form video, video generation  
- **[AptAvatar: Fast and Vivid Long-Form Audio-Driven Video Generation for Production-Ready Avatars](https://arxiv.org/abs/2607.24013v2)**  
  Authors: Hengyuan Zhang, Jingna Sun, Meiguang Jin, Junfeng Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.24013v2.pdf) | [![GitHub](https://img.shields.io/github/stars/TaoLiveAIGC/AptAvatar?style=social)](https://github.com/TaoLiveAIGC/AptAvatar)  
  Keywords: acceleration, audio-driven, audio-driven avatar, avatar, distillation, efficient, identity, long-form, trajectory, video generation  

### Controllable Generation

*Showing the latest 50 out of 327 papers*

- **[EmoWorld: A Decoupled Affective Field for Controllable Emotional Video Generation](https://arxiv.org/abs/2608.06231v1)**  
  Authors: Bingyuan Wang, Baistan Zhyldyzbekov, Kunyu Feng, Zeyu Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.06231v1.pdf)  
  Keywords: camera-conditioned, controllable, denoising, diffusion transformer, dit, flow matching, image to video, image-to-video, text to video, text-to-video, video diffusion, video diffusion transformer, video dit, video generation  
- **[Sample-Adaptive Latent Rewards for Uncertainty-Guided Diffusion Post-Training](https://arxiv.org/abs/2608.06125v1)**  
  Authors: Rui Li, Yuanzhi Liang, Ke Hao, Ziqiao Weng, Haibin Huang, Chi Zhang, XueLong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.06125v1.pdf)  
  Keywords: denoising, efficient, trajectory, video diffusion  
- **[Adaptive-WAM: Quality-Guided Early-Exit Planning from Intermediate Video-Diffusion Features](https://arxiv.org/abs/2608.06008v1)**  
  Authors: Sining Ang, Yuguang Yang, Yan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.06008v1.pdf)  
  Keywords: autonomous driving, denoising, diffusion model, diffusion transformer, dit, driving, trajectory, video denoising, video diffusion, video generation, video synthesis, video world model, world model  
- **[GAUGE: A Measurement-Grounded Benchmark for Physical Fidelity in Simulation Engines and Video World Models](https://arxiv.org/abs/2608.05948v1)**  
  Authors: Shuai Wang, Yaxin Feng, Xuekun Jiang, Shihan Tian, Ningyu Yan, Xing Shen, Chaoyang Lyu, Hui Wang, Yunsong Zhou, Hanqing Wang, Jiangmiao Pang, Yang Xiang, Xing Gao, Chunhua Shen, Weinan Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05948v1.pdf)  
  Keywords: benchmark, embodied, evaluation, image to video, image-to-video, physical, physics, simulation, trajectory  
- **[Vorch-IR: Long-Form Unified Multimodal Identity Replacement Video Generation](https://arxiv.org/abs/2608.05648v1)**  
  Authors: Yaole Wang, Xiaoyu Chen, Xin Ma, Yang Ding, Gang Yue, Jingjing Chen, Lin Ma, Yaohui Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05648v1.pdf)  
  Keywords: autoregressive, driving, evaluation, human evaluation, identity, layout, long-form, minute-long, video generation  
- **[Multimodal Spatiotemporal Atmospheric Data Assimilation with Latent Video Flow-matching](https://arxiv.org/abs/2608.05103v2)**  
  Authors: Dibyajyoti Chakraborty, Romit Maulik  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05103v2.pdf)  
  Keywords: flow matching, latent video, trajectory, video flow matching  
- **[HelloWorld: Enabling Socially Interactive Characters in Video World Models](https://arxiv.org/abs/2608.05070v1)**  
  Authors: Liangyang Ouyang, Ruicong Liu, Xuangeng Chu, Kaipeng Zhang, Yoichi Sato  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05070v1.pdf) | [![GitHub](https://img.shields.io/github/stars/AlayaLab/HelloWorld?style=social)](https://github.com/AlayaLab/HelloWorld)  
  Keywords: benchmark, camera motion, distillation, dit, evaluation, interactive, video generation, video world model, world model  
- **[UniWorld-View: Large-Baseline View Synthesis via Video Diffusion Models](https://arxiv.org/abs/2608.04701v1)**  
  Authors: Haiyang Zhou, Wangbo Yu, Chaoran Feng, Xunyu Zhou, Yonghong Tian, Li Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.04701v1.pdf)  
  Keywords: benchmark, camera control, controllable, novel view, video diffusion  
- **[muSync-GS: Physics-Synchronized Driving Video Synthesis for Weather and Geometric Road Hazards](https://arxiv.org/abs/2608.04412v1)**  
  Authors: Yang Chen, Yicheng Zhu, Tao Li, Zilin Bian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.04412v1.pdf)  
  Keywords: autonomous driving, camera motion, camera trajectory, controllable, driving, dynamics, physical, physics, trajectory, video generation, video synthesis  
- **[SUV: Future Scene Understanding as Video Generation for End-to-End Driving](https://arxiv.org/abs/2608.03084v1)**  
  Authors: Yibo Yuan, Jiacheng Fu, Jiangtong Zhu, Yi Li, Jianhua Han, Meng Tian, Zhuohan Liu, Zhiwei Xiong, Hang Xu, Jianwu Fang, Jianru Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.03084v1.pdf)  
  Keywords: benchmark, driving, dynamics, trajectory, video foundation model, video generation  

### Human & Character Animation

*Showing the latest 50 out of 69 papers*

- **[UniVVT: A Unified End-to-End Framework for High-Fidelity Video Virtual Try-on](https://arxiv.org/abs/2608.05745v1)**  
  Authors: Yushe Cao, Shikun Feng, Fei Shen, Haikuo Peng, Jianqiang Xia, Yiheng Zhu, Dianxi Shi, Chun Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05745v1.pdf)  
  Keywords: dynamics, identity, video generation, video inpainting, virtual try-on  
- **[Vorch-Streamer: Extending Human Audio-Visual Generation to Real-Time Long-Form Streaming](https://arxiv.org/abs/2608.05663v1)**  
  Authors: Menglin Han, Yang Ding, Yulei Lu, Haoran Yu, Xin Ma, Junyi Chen, Zhangkai Ni, Lin Ma, Yaohui Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05663v1.pdf)  
  Keywords: audio-video generation, audio-visual generation, avatar, denoising, distillation, identity, long-form, streaming, video generation  
- **[UniMoCa: Unifying Motion and Camera Controls as Visual Proxies for Faithful Human Video Generation](https://arxiv.org/abs/2608.01944v1)**  
  Authors: Liming Tan, Ye Chen, Hao Zhang, Lirong Qian, Feifei Li, Bingbing Ni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01944v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://tanliming-daniel.github.io/UniMoCa)  
  Keywords: camera control, camera trajectory, driving, human motion, i2v, identity, motion control, temporal consistency, trajectory, video generation  
- **[ReGenVC: End-to-End Real-Time Generative Video Coding at Ultra-Low Bitrate](https://arxiv.org/abs/2607.28144v1)**  
  Authors: Zheyuan Zhang, Johnson Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.28144v1.pdf)  
  Keywords: diffusion transformer, distillation, interactive, one-shot, talking head  
- **[LeapTalk: Breaking the Latency-Quality Trade-off in Talking Head Generation](https://arxiv.org/abs/2608.00079v1)**  
  Authors: Rongxiang Zhang, Songhua Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.00079v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zhangrongxiang.github.io/leaptalk-page)  
  Keywords: audio-driven, autoregressive, distillation, identity, long-form, streaming, talking head, video generation  
- **[TaoMate: Anchor-Guided Memory Bridging Evolving and Reference States for Real-Time Audio-Video Digital Human Generation](https://arxiv.org/abs/2607.24359v1)**  
  Authors: Qijun Gan, Chenwei Zhang, Meiguang Jin, Junfeng Ma, Qiu Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.24359v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://taoliveaigc.github.io/TaoMate)  
  Keywords: audio-video generation, autoregressive, denoising, digital human, distillation, joint audio-video, long-form, long-form video, video generation  
- **[ViDS: Video Diffusion Shader using 3D Face Tracking](https://arxiv.org/abs/2607.24124v1)**  
  Authors: Wenbo Ji, Davide Davoli, Zhe Chen, Liam Schoneveld, Matthias Nießner, Jiapeng Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.24124v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://fusheng-ji.github.io/ViDS)  
  Keywords: autoregressive, diffusion model, driving, identity, identity-preserving, portrait animation, video diffusion  
- **[AptAvatar: Fast and Vivid Long-Form Audio-Driven Video Generation for Production-Ready Avatars](https://arxiv.org/abs/2607.24013v2)**  
  Authors: Hengyuan Zhang, Jingna Sun, Meiguang Jin, Junfeng Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.24013v2.pdf) | [![GitHub](https://img.shields.io/github/stars/TaoLiveAIGC/AptAvatar?style=social)](https://github.com/TaoLiveAIGC/AptAvatar)  
  Keywords: acceleration, audio-driven, audio-driven avatar, avatar, distillation, efficient, identity, long-form, trajectory, video generation  
- **[fMRI2Face: A Full-HD fMRI-Video Dataset and Geometry-Guided Neural Decoding Framework for Dynamic Human Face Reconstruction](https://arxiv.org/abs/2607.22302v1)**  
  Authors: Jingyang Huo, Xiangru Huang, Chentao Shen, Yikai Wang, Yun Wang, Jianxiong Gao, Shihao Jin, Yanwei Fu, Jianfeng Feng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.22302v1.pdf)  
  Keywords: benchmark, controllable, digital human, dynamics, identity, video diffusion  
- **[Learning Explicit Physical Parameter Control and Benchmarking for Video Generation](https://arxiv.org/abs/2607.18924v1)**  
  Authors: Yanxun Li, Hao Wen, Bingze Song, Jiashu Zhu, Aiming Hao, Chubin Chen, Jintao Chen, Jiahong Wu, Xiangxiang Chu, Miao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.18924v1.pdf)  
  Keywords: benchmark, body motion, controllable, diffusion model, dynamics, image to video, image-to-video, physical, physical consistency, physics, simulation, video diffusion, video generation, world simulation  

### Image-to-Video Generation

*Showing the latest 50 out of 99 papers*

- **[EmoWorld: A Decoupled Affective Field for Controllable Emotional Video Generation](https://arxiv.org/abs/2608.06231v1)**  
  Authors: Bingyuan Wang, Baistan Zhyldyzbekov, Kunyu Feng, Zeyu Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.06231v1.pdf)  
  Keywords: camera-conditioned, controllable, denoising, diffusion transformer, dit, flow matching, image to video, image-to-video, text to video, text-to-video, video diffusion, video diffusion transformer, video dit, video generation  
- **[GAUGE: A Measurement-Grounded Benchmark for Physical Fidelity in Simulation Engines and Video World Models](https://arxiv.org/abs/2608.05948v1)**  
  Authors: Shuai Wang, Yaxin Feng, Xuekun Jiang, Shihan Tian, Ningyu Yan, Xing Shen, Chaoyang Lyu, Hui Wang, Yunsong Zhou, Hanqing Wang, Jiangmiao Pang, Yang Xiang, Xing Gao, Chunhua Shen, Weinan Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05948v1.pdf)  
  Keywords: benchmark, embodied, evaluation, image to video, image-to-video, physical, physics, simulation, trajectory  
- **[OmniVR: Joint Video-Audio Conditional Generation for Restoring Degraded Historical Films](https://arxiv.org/abs/2608.04224v1)**  
  Authors: Xin Lu, Zihao Fan, Mingchen Zhong, Jie Huang, Xueyang Fu, Zheng-Jun Zha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.04224v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xin1u.github.io/OminiVR_PAGE)  
  Keywords: architecture, audio-video generation, benchmark, dit, film, i2v, image to video, image-to-video, joint audio-video, long video, temporal consistency, video generation, video restoration, video-to-audio  
- **[SPADE: An Input-Adaptive Sparse Attention Engine for Fast Video Diffusion Models Inference](https://arxiv.org/abs/2608.03335v1)**  
  Authors: Shanghao Liu, Renze Chen, Size Zheng, Yuanqiang Liu, Yun, Liang, Hailong Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.03335v1.pdf) | [![GitHub](https://img.shields.io/github/stars/6somehow/DAC-SPADE?style=social)](https://github.com/6somehow/DAC-SPADE)  
  Keywords: image to video, image-to-video, sparse attention, text to video, text-to-video, video diffusion, video generation  
- **[Token Radius Attention for Efficient Video Generation](https://arxiv.org/abs/2608.02504v1)**  
  Authors: Jiayu Chen, Zhikun Jiang, Maoliang Li, Jiayi Luo, Jiawei Yang, Zihao Zheng, Hengyi Zhang, Guojie Luo, Xiang Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.02504v1.pdf) | [![GitHub](https://img.shields.io/github/stars/IF-LAB-PKU/Token-Radius-Attention?style=social)](https://github.com/IF-LAB-PKU/Token-Radius-Attention)  
  Keywords: efficient, i2v, t2v, video diffusion, video generation  
- **[UniMoCa: Unifying Motion and Camera Controls as Visual Proxies for Faithful Human Video Generation](https://arxiv.org/abs/2608.01944v1)**  
  Authors: Liming Tan, Ye Chen, Hao Zhang, Lirong Qian, Feifei Li, Bingbing Ni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01944v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://tanliming-daniel.github.io/UniMoCa)  
  Keywords: camera control, camera trajectory, driving, human motion, i2v, identity, motion control, temporal consistency, trajectory, video generation  
- **[DreamTraj: Generating 6-DoF Object Trajectories by Reading Unrendered Video Diffusion Latents](https://arxiv.org/abs/2608.00486v1)**  
  Authors: Tongsheng Ding, Zhen Luo, Yixuan Yang, Boyu Wang, Luyang Xie, Jinyu Yang, Feng Zheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.00486v1.pdf)  
  Keywords: denoising, diffusion model, flow matching, image to video, image-to-video, trajectory, video diffusion  
- **[Video Models as Native 4D Renderers: World-Grounded Conditioning from Animated Mesh](https://arxiv.org/abs/2608.00094v2)**  
  Authors: Junhao Chen, Mingjin Chen, Henghaofan Zhang, Minglin Chen, Liaoyuan Fan, Boran Zhang, Saining Zhang, Mingze Sun, Hao Zhao, Ruqi Huang, Zhihao Li, Yufei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.00094v2.pdf)  
  Keywords: benchmark, camera control, camera motion, camera trajectory, image to video, image-to-video, reference-guided, trajectory, video diffusion  
- **[Visko Orbis 1.0: A Live Model for Real-Time Interactive Long Video Generation](https://arxiv.org/abs/2607.26694v1)**  
  Authors: Xiangbo Gao, Siyuan Yang, Ping He, Mingyang Wu, Yuheng Wu, Yushen Zuo, Jiongze Yu, Ryan Cui, Hongyuan Hua, Devin Ma, Xiao Jin, Yubo Yuan, Qing Yin, Jie Yang, Zhengzhong Tu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.26694v1.pdf)  
  Keywords: image to video, image-to-video, interactive, long video, long-form, streaming, style, text to video, text-to-video, video generation  
- **[Wonder: Video World Model Done Better](https://arxiv.org/abs/2607.26037v1)**  
  Authors: Jiacong Xu, Hanwen Jiang, Zhixin Shu, Kalyan Sunkavalli, Vishal M. Patel, Yiqun Mei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.26037v1.pdf)  
  Keywords: camera motion, controllable, distillation, dynamics, efficient, image to video, image-to-video, sparse attention, style, video generation, video world model, world model  

### Long Video Generation

*Showing the latest 50 out of 268 papers*

- **[Diff-VF: Training-free High-quality Long Video Generation via Diffusion Model](https://arxiv.org/abs/2608.05976v1)**  
  Authors: Haoning Yang, Xinyuan Chen, Yaohui Wang, Guo Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05976v1.pdf)  
  Keywords: diffusion model, evaluation, long video, video diffusion, video enhancement, video generation  
- **[Vorch-Director: Interactive World Story Model via Noise-Aware Error Rectification](https://arxiv.org/abs/2608.05776v1)**  
  Authors: Lisai Zhang, Yidi Wu, Qi Liu, Xin Ma, Yang Ding, Gang Yue, Siqian Yang, Jingyuan Chen, Lin Ma, Yaohui Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05776v1.pdf)  
  Keywords: audio-visual generation, autoregressive, benchmark, denoising, diffusion transformer, efficient, flow matching, identity, interactive, long video, reference-guided, video generation  
- **[Vorch-Streamer: Extending Human Audio-Visual Generation to Real-Time Long-Form Streaming](https://arxiv.org/abs/2608.05663v1)**  
  Authors: Menglin Han, Yang Ding, Yulei Lu, Haoran Yu, Xin Ma, Junyi Chen, Zhangkai Ni, Lin Ma, Yaohui Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05663v1.pdf)  
  Keywords: audio-video generation, audio-visual generation, avatar, denoising, distillation, identity, long-form, streaming, video generation  
- **[Vorch-IR: Long-Form Unified Multimodal Identity Replacement Video Generation](https://arxiv.org/abs/2608.05648v1)**  
  Authors: Yaole Wang, Xiaoyu Chen, Xin Ma, Yang Ding, Gang Yue, Jingjing Chen, Lin Ma, Yaohui Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05648v1.pdf)  
  Keywords: autoregressive, driving, evaluation, human evaluation, identity, layout, long-form, minute-long, video generation  
- **[In-Context Forcing: Uncovering Context Effects in Autoregressive Video Diffusion](https://arxiv.org/abs/2608.05237v1)**  
  Authors: Lingxiao Yang, Liu Liu, Moran Li, Han Feng, Wenjian Cao, Jiangning Zhang, Ye Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05237v1.pdf)  
  Keywords: acceleration, autoregressive, autoregressive video, denoising, dynamics, temporal consistency, video diffusion  
- **[MetaVideoAgent: Automated Video-Agent Evolution for Long-Form Video Understanding](https://arxiv.org/abs/2608.04587v1)**  
  Authors: Benlei Cui, Ruize Wang, Junjie Li, Jinhao Chen, Longtao Huang, Yinghao Chen, Yuwen Zhai, Jingqun Tang, Ruijian Jia, Weiwei Wu, Pengfei Sun, Haiwen Hong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.04587v1.pdf)  
  Keywords: long video, long-form, long-form video, text to video, text-to-video  
- **[OmniVR: Joint Video-Audio Conditional Generation for Restoring Degraded Historical Films](https://arxiv.org/abs/2608.04224v1)**  
  Authors: Xin Lu, Zihao Fan, Mingchen Zhong, Jie Huang, Xueyang Fu, Zheng-Jun Zha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.04224v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xin1u.github.io/OminiVR_PAGE)  
  Keywords: architecture, audio-video generation, benchmark, dit, film, i2v, image to video, image-to-video, joint audio-video, long video, temporal consistency, video generation, video restoration, video-to-audio  
- **[JoyAI-Video-Edit: Real-Time Open-Ended Video Editing with Autoregressive Diffusion](https://arxiv.org/abs/2608.03974v1)**  
  Authors: Yicheng Xiao, Wenxun Dai, Xinran Qin, Lin Song, Maoquan Zhang, Hang Xu, Yukang Chen, Yitong Li, Guohui Zhang, Yuan Zhang, Xuying Zhang, Tommy Zhang, Jianlong Yuan, Peihao Li, Shuai Lu, Siming Fu, Chuyang Zhao, Xin Han, Jie Huang, Wenbo Li, Guoqing Ma, Wei Huang, Xiaojuan Qi, Haoyang Huang, Nan Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.03974v1.pdf) | [![GitHub](https://img.shields.io/github/stars/jd-opensource/JoyAI-Video-Edit?style=social)](https://github.com/jd-opensource/JoyAI-Video-Edit)  
  Keywords: autoregressive, distillation, streaming, temporal consistency, video editing  
- **[UniMoCa: Unifying Motion and Camera Controls as Visual Proxies for Faithful Human Video Generation](https://arxiv.org/abs/2608.01944v1)**  
  Authors: Liming Tan, Ye Chen, Hao Zhang, Lirong Qian, Feifei Li, Bingbing Ni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01944v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://tanliming-daniel.github.io/UniMoCa)  
  Keywords: camera control, camera trajectory, driving, human motion, i2v, identity, motion control, temporal consistency, trajectory, video generation  
- **[MiniWorld: Democratizing the Training of Video World Models from Scratch](https://arxiv.org/abs/2608.01127v2)**  
  Authors: Yian Zhao, Ruochong Zheng, Hongcan Guo, Yu Yan, Jian Zhang, Jie Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01127v2.pdf)  
  Keywords: autoregressive, autoregressive video, denoising, diffusion transformer, distillation, dynamics, efficient, embodied, flow matching, interactive, simulation, streaming, video diffusion, video diffusion transformer, video generation  

### Personalization & Customization

*Showing the latest 50 out of 183 papers*

- **[Vorch-Director: Interactive World Story Model via Noise-Aware Error Rectification](https://arxiv.org/abs/2608.05776v1)**  
  Authors: Lisai Zhang, Yidi Wu, Qi Liu, Xin Ma, Yang Ding, Gang Yue, Siqian Yang, Jingyuan Chen, Lin Ma, Yaohui Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05776v1.pdf)  
  Keywords: audio-visual generation, autoregressive, benchmark, denoising, diffusion transformer, efficient, flow matching, identity, interactive, long video, reference-guided, video generation  
- **[UniVVT: A Unified End-to-End Framework for High-Fidelity Video Virtual Try-on](https://arxiv.org/abs/2608.05745v1)**  
  Authors: Yushe Cao, Shikun Feng, Fei Shen, Haikuo Peng, Jianqiang Xia, Yiheng Zhu, Dianxi Shi, Chun Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05745v1.pdf)  
  Keywords: dynamics, identity, video generation, video inpainting, virtual try-on  
- **[Vorch-Streamer: Extending Human Audio-Visual Generation to Real-Time Long-Form Streaming](https://arxiv.org/abs/2608.05663v1)**  
  Authors: Menglin Han, Yang Ding, Yulei Lu, Haoran Yu, Xin Ma, Junyi Chen, Zhangkai Ni, Lin Ma, Yaohui Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05663v1.pdf)  
  Keywords: audio-video generation, audio-visual generation, avatar, denoising, distillation, identity, long-form, streaming, video generation  
- **[Vorch-IR: Long-Form Unified Multimodal Identity Replacement Video Generation](https://arxiv.org/abs/2608.05648v1)**  
  Authors: Yaole Wang, Xiaoyu Chen, Xin Ma, Yang Ding, Gang Yue, Jingjing Chen, Lin Ma, Yaohui Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05648v1.pdf)  
  Keywords: autoregressive, driving, evaluation, human evaluation, identity, layout, long-form, minute-long, video generation  
- **[UniMoCa: Unifying Motion and Camera Controls as Visual Proxies for Faithful Human Video Generation](https://arxiv.org/abs/2608.01944v1)**  
  Authors: Liming Tan, Ye Chen, Hao Zhang, Lirong Qian, Feifei Li, Bingbing Ni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01944v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://tanliming-daniel.github.io/UniMoCa)  
  Keywords: camera control, camera trajectory, driving, human motion, i2v, identity, motion control, temporal consistency, trajectory, video generation  
- **[ProWorld: Progress-Aware Hyperbolic World Models for Long-Horizon Visual Goal Reaching](https://arxiv.org/abs/2608.01926v1)**  
  Authors: Zihan Liu, Yuzhe Zhuang, Yuanzu Li, Wanshuang Gou, Jiahong Liu, Min Zhou, Menglin Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01926v1.pdf)  
  Keywords: dynamics, style, visual world model, world model  
- **[Video Models as Native 4D Renderers: World-Grounded Conditioning from Animated Mesh](https://arxiv.org/abs/2608.00094v2)**  
  Authors: Junhao Chen, Mingjin Chen, Henghaofan Zhang, Minglin Chen, Liaoyuan Fan, Boran Zhang, Saining Zhang, Mingze Sun, Hao Zhao, Ruqi Huang, Zhihao Li, Yufei Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.00094v2.pdf)  
  Keywords: benchmark, camera control, camera motion, camera trajectory, image to video, image-to-video, reference-guided, trajectory, video diffusion  
- **[ReGenVC: End-to-End Real-Time Generative Video Coding at Ultra-Low Bitrate](https://arxiv.org/abs/2607.28144v1)**  
  Authors: Zheyuan Zhang, Johnson Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.28144v1.pdf)  
  Keywords: diffusion transformer, distillation, interactive, one-shot, talking head  
- **[LeapTalk: Breaking the Latency-Quality Trade-off in Talking Head Generation](https://arxiv.org/abs/2608.00079v1)**  
  Authors: Rongxiang Zhang, Songhua Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.00079v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zhangrongxiang.github.io/leaptalk-page)  
  Keywords: audio-driven, autoregressive, distillation, identity, long-form, streaming, talking head, video generation  
- **[TPD: Temporal Prior Decoupling for Text-to-Video Diffusion Models](https://arxiv.org/abs/2607.26706v1)**  
  Authors: Taewon Kang, Matthias Zwicker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.26706v1.pdf)  
  Keywords: concept, text to video, text-to-video, trajectory, video diffusion  

### Physical Understanding

*Showing the latest 50 out of 316 papers*

- **[GAUGE: A Measurement-Grounded Benchmark for Physical Fidelity in Simulation Engines and Video World Models](https://arxiv.org/abs/2608.05948v1)**  
  Authors: Shuai Wang, Yaxin Feng, Xuekun Jiang, Shihan Tian, Ningyu Yan, Xing Shen, Chaoyang Lyu, Hui Wang, Yunsong Zhou, Hanqing Wang, Jiangmiao Pang, Yang Xiang, Xing Gao, Chunhua Shen, Weinan Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05948v1.pdf)  
  Keywords: benchmark, embodied, evaluation, image to video, image-to-video, physical, physics, simulation, trajectory  
- **[Robust-WAM: Bridging Generative Pretraining and Semantic Foresight in World-Action Models](https://arxiv.org/abs/2608.05903v1)**  
  Authors: Haodong Yan, Junfeng Li, Junjie He, Zhide Zhong, MingMing Yu, Wenxuan Song, Jiaguan Zhu, Yangyang Zheng, Yuqiao Du, Jiadi You, Yingjie Cai, Xu Yan, Guanyi Zhao, Bingbing Liu, Haoang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05903v1.pdf)  
  Keywords: dynamics, simulation, video generation  
- **[UniVVT: A Unified End-to-End Framework for High-Fidelity Video Virtual Try-on](https://arxiv.org/abs/2608.05745v1)**  
  Authors: Yushe Cao, Shikun Feng, Fei Shen, Haikuo Peng, Jianqiang Xia, Yiheng Zhu, Dianxi Shi, Chun Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05745v1.pdf)  
  Keywords: dynamics, identity, video generation, video inpainting, virtual try-on  
- **[In-Context Forcing: Uncovering Context Effects in Autoregressive Video Diffusion](https://arxiv.org/abs/2608.05237v1)**  
  Authors: Lingxiao Yang, Liu Liu, Moran Li, Han Feng, Wenjian Cao, Jiangning Zhang, Ye Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05237v1.pdf)  
  Keywords: acceleration, autoregressive, autoregressive video, denoising, dynamics, temporal consistency, video diffusion  
- **[MobileWAM: Bridging World Action Models to Mobile Manipulation with Chain-of-Foresight](https://arxiv.org/abs/2608.04657v2)**  
  Authors: Zehua Fan, Junjie He, Wenxuan Song, Xi Wang, Wenqi Lyu, Linge Zhao, Fuhao Li, Zihan You, Yifei Yang, Kaiming Xu, Qi Jiang, Yue Jiang, Haoang Li, Cheng Chi, Feng Gao, Bailin Li, Yan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.04657v2.pdf)  
  Keywords: architecture, denoising, diffusion transformer, dynamics, robot learning, video diffusion, video diffusion transformer, video generation  
- **[muSync-GS: Physics-Synchronized Driving Video Synthesis for Weather and Geometric Road Hazards](https://arxiv.org/abs/2608.04412v1)**  
  Authors: Yang Chen, Yicheng Zhu, Tao Li, Zilin Bian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.04412v1.pdf)  
  Keywords: autonomous driving, camera motion, camera trajectory, controllable, driving, dynamics, physical, physics, trajectory, video generation, video synthesis  
- **[CrossScope: A Role-Asymmetric World Model for Joint Dual-Scope Surgical Video Prediction](https://arxiv.org/abs/2608.03211v1)**  
  Authors: Wanhao Liu, Jinsong Lin, Rulin Zhou, Chi Kit Ng, Wenbin Pan, Zhiqing Tang, Dongyue Li, Liwei Luo, Yanshen Wu, Panshuo Li, Zhiyong Xiong, Huxin Gao, Tamas Haidegger, Hongliang Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.03211v1.pdf)  
  Keywords: benchmark, dynamics, video generation, video prediction, world model  
- **[SUV: Future Scene Understanding as Video Generation for End-to-End Driving](https://arxiv.org/abs/2608.03084v1)**  
  Authors: Yibo Yuan, Jiacheng Fu, Jiangtong Zhu, Yi Li, Jianhua Han, Meng Tian, Zhuohan Liu, Zhiwei Xiong, Hang Xu, Jianwu Fang, Jianru Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.03084v1.pdf)  
  Keywords: benchmark, driving, dynamics, trajectory, video foundation model, video generation  
- **[AcoustiTrace: When Plausible Sound Violates Physics](https://arxiv.org/abs/2608.02035v1)**  
  Authors: Shiyang Li, Yuewen Cao, Yihao Liu, Yuandong Pu, Baochang Zhang, Xiaofei Li, Changqing Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.02035v1.pdf)  
  Keywords: audio-video generation, benchmark, evaluation, physical, physics, sound, video generation  
- **[CultureVidBench: Benchmarking Cultural Understanding in Text-to-Video Generation](https://arxiv.org/abs/2608.01942v1)**  
  Authors: Xianjing Han, Yuhan Su, Yang Deng, Dong Ma, Wee Peng Tay, Bin Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01942v1.pdf)  
  Keywords: benchmark, physical, physical plausibility, t2v, text to video, text-to-video, video generation  

### Surveys & Benchmarks

*Showing the latest 50 out of 292 papers*

- **[Diff-VF: Training-free High-quality Long Video Generation via Diffusion Model](https://arxiv.org/abs/2608.05976v1)**  
  Authors: Haoning Yang, Xinyuan Chen, Yaohui Wang, Guo Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05976v1.pdf)  
  Keywords: diffusion model, evaluation, long video, video diffusion, video enhancement, video generation  
- **[GAUGE: A Measurement-Grounded Benchmark for Physical Fidelity in Simulation Engines and Video World Models](https://arxiv.org/abs/2608.05948v1)**  
  Authors: Shuai Wang, Yaxin Feng, Xuekun Jiang, Shihan Tian, Ningyu Yan, Xing Shen, Chaoyang Lyu, Hui Wang, Yunsong Zhou, Hanqing Wang, Jiangmiao Pang, Yang Xiang, Xing Gao, Chunhua Shen, Weinan Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05948v1.pdf)  
  Keywords: benchmark, embodied, evaluation, image to video, image-to-video, physical, physics, simulation, trajectory  
- **[Vorch-Director: Interactive World Story Model via Noise-Aware Error Rectification](https://arxiv.org/abs/2608.05776v1)**  
  Authors: Lisai Zhang, Yidi Wu, Qi Liu, Xin Ma, Yang Ding, Gang Yue, Siqian Yang, Jingyuan Chen, Lin Ma, Yaohui Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05776v1.pdf)  
  Keywords: audio-visual generation, autoregressive, benchmark, denoising, diffusion transformer, efficient, flow matching, identity, interactive, long video, reference-guided, video generation  
- **[Vorch-IR: Long-Form Unified Multimodal Identity Replacement Video Generation](https://arxiv.org/abs/2608.05648v1)**  
  Authors: Yaole Wang, Xiaoyu Chen, Xin Ma, Yang Ding, Gang Yue, Jingjing Chen, Lin Ma, Yaohui Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05648v1.pdf)  
  Keywords: autoregressive, driving, evaluation, human evaluation, identity, layout, long-form, minute-long, video generation  
- **[VideoArgus: Agentic Rubric-Grounded Unified Evaluation for Video Generation and Editing](https://arxiv.org/abs/2608.05485v1)**  
  Authors: Ziyun Zeng, Zixuan Wang, Yongsheng Yu, Hang Hua, Jiebo Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05485v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zzzmyyzeng.github.io/VideoArgus)  
  Keywords: benchmark, evaluation, video generation  
- **[HelloWorld: Enabling Socially Interactive Characters in Video World Models](https://arxiv.org/abs/2608.05070v1)**  
  Authors: Liangyang Ouyang, Ruicong Liu, Xuangeng Chu, Kaipeng Zhang, Yoichi Sato  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05070v1.pdf) | [![GitHub](https://img.shields.io/github/stars/AlayaLab/HelloWorld?style=social)](https://github.com/AlayaLab/HelloWorld)  
  Keywords: benchmark, camera motion, distillation, dit, evaluation, interactive, video generation, video world model, world model  
- **[OmniEdit-Bench: A Comprehensive Benchmark for Instruction-based Video Editing](https://arxiv.org/abs/2608.05049v1)**  
  Authors: Chenxuan Miao, Yutong Feng, Yi Lu, Yunfeng Yan, Donglian Qi, Shiwei Zhang, Yu Liu, Xi Chen, Hengshuang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05049v1.pdf)  
  Keywords: benchmark, evaluation, instruction-based video editing, video editing  
- **[Reading Between the Frames: Interpreting Implicit and Non-literal Meaning in Social Media Videos](https://arxiv.org/abs/2608.04939v1)**  
  Authors: Yang Wang, Yanan Ma, Yiqi Liu, Zi Yan Chang, Chi-Li Chen, Chia-Yi Hsiao, Tyler Loakman, Aline Villavicencio, Chenghao Xiao, Chenghua Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.04939v1.pdf)  
  Keywords: benchmark, text to video, text-to-video  
- **[UniWorld-View: Large-Baseline View Synthesis via Video Diffusion Models](https://arxiv.org/abs/2608.04701v1)**  
  Authors: Haiyang Zhou, Wangbo Yu, Chaoran Feng, Xunyu Zhou, Yonghong Tian, Li Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.04701v1.pdf)  
  Keywords: benchmark, camera control, controllable, novel view, video diffusion  
- **[OmniVR: Joint Video-Audio Conditional Generation for Restoring Degraded Historical Films](https://arxiv.org/abs/2608.04224v1)**  
  Authors: Xin Lu, Zihao Fan, Mingchen Zhong, Jie Huang, Xueyang Fu, Zheng-Jun Zha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.04224v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xin1u.github.io/OminiVR_PAGE)  
  Keywords: architecture, audio-video generation, benchmark, dit, film, i2v, image to video, image-to-video, joint audio-video, long video, temporal consistency, video generation, video restoration, video-to-audio  

### Text-to-Video Generation

*Showing the latest 50 out of 135 papers*

- **[EmoWorld: A Decoupled Affective Field for Controllable Emotional Video Generation](https://arxiv.org/abs/2608.06231v1)**  
  Authors: Bingyuan Wang, Baistan Zhyldyzbekov, Kunyu Feng, Zeyu Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.06231v1.pdf)  
  Keywords: camera-conditioned, controllable, denoising, diffusion transformer, dit, flow matching, image to video, image-to-video, text to video, text-to-video, video diffusion, video diffusion transformer, video dit, video generation  
- **[Vorch-Omni: Multi-Task Orchestration of Sight and Sound](https://arxiv.org/abs/2608.05803v1)**  
  Authors: Vorch Team, Xiaoyu Chen, Yang Ding, Cong Han, Menglin Han, Yuxin Hong, Jiebo Hou, Zequn Jie, Xiang Li, Jing Liu, Qi Liu, Yulei Lu, Siyuan Luo, Lin Ma, Xin Ma, Yinlong Qian, Peng Shi, Fang Wan, Siqi Wang, Yaohui Wang, Yaole Wang, Yidi Wu, Siqian Yang, Mingyu Yin, Haoran Yu, Gang Yue, Lisai Zhang, Yuting Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05803v1.pdf)  
  Keywords: audio-driven, audio-visual generation, diffusion transformer, flow matching, sound, text to video, text-to-video  
- **[LC-GRPO: Bridging Train-Inference Gap for Flow-Based GRPO with Langevin Correction](https://arxiv.org/abs/2608.05600v1)**  
  Authors: Yingqing Guo, Hui Yuan, Zijian He, Mengdi Wang, Zheng Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05600v1.pdf)  
  Keywords: text to video, text-to-video  
- **[Reading Between the Frames: Interpreting Implicit and Non-literal Meaning in Social Media Videos](https://arxiv.org/abs/2608.04939v1)**  
  Authors: Yang Wang, Yanan Ma, Yiqi Liu, Zi Yan Chang, Chi-Li Chen, Chia-Yi Hsiao, Tyler Loakman, Aline Villavicencio, Chenghao Xiao, Chenghua Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.04939v1.pdf)  
  Keywords: benchmark, text to video, text-to-video  
- **[MetaVideoAgent: Automated Video-Agent Evolution for Long-Form Video Understanding](https://arxiv.org/abs/2608.04587v1)**  
  Authors: Benlei Cui, Ruize Wang, Junjie Li, Jinhao Chen, Longtao Huang, Yinghao Chen, Yuwen Zhai, Jingqun Tang, Ruijian Jia, Weiwei Wu, Pengfei Sun, Haiwen Hong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.04587v1.pdf)  
  Keywords: long video, long-form, long-form video, text to video, text-to-video  
- **[SPADE: An Input-Adaptive Sparse Attention Engine for Fast Video Diffusion Models Inference](https://arxiv.org/abs/2608.03335v1)**  
  Authors: Shanghao Liu, Renze Chen, Size Zheng, Yuanqiang Liu, Yun, Liang, Hailong Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.03335v1.pdf) | [![GitHub](https://img.shields.io/github/stars/6somehow/DAC-SPADE?style=social)](https://github.com/6somehow/DAC-SPADE)  
  Keywords: image to video, image-to-video, sparse attention, text to video, text-to-video, video diffusion, video generation  
- **[CAPE-T2V: Captioner-Anchored Prompt Enhancement toward Two-Sided Conditioning Alignment in Text-to-Video Generation](https://arxiv.org/abs/2608.03046v1)**  
  Authors: Yizhuo Jia, Jingyun Hua, Yuanxing Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.03046v1.pdf) | [![GitHub](https://img.shields.io/github/stars/yizzz927/CAPE-T2V?style=social)](https://github.com/yizzz927/CAPE-T2V)  
  Keywords: dit, t2v, text to video, text-to-video, video generation  
- **[Toward Uncertainty Quantification in Modern Art](https://arxiv.org/abs/2608.04038v1)**  
  Authors: Tirtho Roy, Ushashi Bhattacharjee, Showrav Kumar Saha, Sayantan Chakraborty, Koushik Howlader, Tanusree Bhattacharjee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.04038v1.pdf)  
  Keywords: text to video, text-to-video  
- **[Token Radius Attention for Efficient Video Generation](https://arxiv.org/abs/2608.02504v1)**  
  Authors: Jiayu Chen, Zhikun Jiang, Maoliang Li, Jiayi Luo, Jiawei Yang, Zihao Zheng, Hengyi Zhang, Guojie Luo, Xiang Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.02504v1.pdf) | [![GitHub](https://img.shields.io/github/stars/IF-LAB-PKU/Token-Radius-Attention?style=social)](https://github.com/IF-LAB-PKU/Token-Radius-Attention)  
  Keywords: efficient, i2v, t2v, video diffusion, video generation  
- **[CultureVidBench: Benchmarking Cultural Understanding in Text-to-Video Generation](https://arxiv.org/abs/2608.01942v1)**  
  Authors: Xianjing Han, Yuhan Su, Yang Deng, Dong Ma, Wee Peng Tay, Bin Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01942v1.pdf)  
  Keywords: benchmark, physical, physical plausibility, t2v, text to video, text-to-video, video generation  

### Video Editing

*Showing the latest 50 out of 107 papers*

- **[OmniEdit-Bench: A Comprehensive Benchmark for Instruction-based Video Editing](https://arxiv.org/abs/2608.05049v1)**  
  Authors: Chenxuan Miao, Yutong Feng, Yi Lu, Yunfeng Yan, Donglian Qi, Shiwei Zhang, Yu Liu, Xi Chen, Hengshuang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05049v1.pdf)  
  Keywords: benchmark, evaluation, instruction-based video editing, video editing  
- **[JoyAI-Video-Edit: Real-Time Open-Ended Video Editing with Autoregressive Diffusion](https://arxiv.org/abs/2608.03974v1)**  
  Authors: Yicheng Xiao, Wenxun Dai, Xinran Qin, Lin Song, Maoquan Zhang, Hang Xu, Yukang Chen, Yitong Li, Guohui Zhang, Yuan Zhang, Xuying Zhang, Tommy Zhang, Jianlong Yuan, Peihao Li, Shuai Lu, Siming Fu, Chuyang Zhao, Xin Han, Jie Huang, Wenbo Li, Guoqing Ma, Wei Huang, Xiaojuan Qi, Haoyang Huang, Nan Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.03974v1.pdf) | [![GitHub](https://img.shields.io/github/stars/jd-opensource/JoyAI-Video-Edit?style=social)](https://github.com/jd-opensource/JoyAI-Video-Edit)  
  Keywords: autoregressive, distillation, streaming, temporal consistency, video editing  
- **[Crayotter: Learning Long-Horizon Video Editing Agents via Group-Relative Preference Backpropagation](https://arxiv.org/abs/2608.02694v1)**  
  Authors: Lecheng Yan, Jianze Lin, Yichong Zhang, Ben Pan, Wenxi Li, Chenyang Lyu, Liting Zhou, Cathal Gurrin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.02694v1.pdf) | [![GitHub](https://img.shields.io/github/stars/idwts/Crayotter?style=social)](https://github.com/idwts/Crayotter)  
  Keywords: evaluation, human evaluation, video editing  
- **[CoT-Edit: Let CoT Guide Instruction Video Editing](https://arxiv.org/abs/2608.01113v1)**  
  Authors: Sen Liang, Fengbin Guan, Youliang Zhang, Xin Li, Zhibo Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01113v1.pdf) | [![GitHub](https://img.shields.io/github/stars/flying-sky999/CoT-Edit?style=social)](https://github.com/flying-sky999/CoT-Edit)  
  Keywords: instruction-based video editing, physical, video editing  
- **[ChordVideo: One-Step, Training-Free, Temporally Consistent Video Editing via Low-Energy Transport](https://arxiv.org/abs/2608.00769v1)**  
  Authors: Zhiqiang Lao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.00769v1.pdf)  
  Keywords: temporal consistency, video editing  
- **[Explicit Layer Modeling for Video Object Insertion and Layer Decomposition](https://arxiv.org/abs/2607.25802v2)**  
  Authors: Kyujin Han, Seungjoo Shin, Sunghyun Cho  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.25802v2.pdf)  
  Keywords: denoising, video editing  
- **[MEDit-Bench: A Dataset for Evaluating Message-Driven Narrative Video Editing](https://arxiv.org/abs/2607.25300v1)**  
  Authors: Katsuya Ogata, Zongshang Pang, Mayu Otani, Yuta Nakashima  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.25300v1.pdf)  
  Keywords: benchmark, evaluation, long-form, video editing  
- **[CameraAnything: Refilming Videos with Arbitrary Camera Control](https://arxiv.org/abs/2607.24591v1)**  
  Authors: Yixuan Li, Yanhong Zeng, Ka Leong Cheng, Jiayi Zhu, Hanlin Wang, Wen Wang, Yihao Meng, Hao Ouyang, Qiuyu Wang, Yue Yu, ZiDong Wang, Yiyuan Zhang, Yujun Shen, Dahua Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.24591v1.pdf)  
  Keywords: camera control, cinematic, outpainting, video editing  
- **[EgoPlay: Event-Triggered Video Editing for Egocentric Streams](https://arxiv.org/abs/2607.24560v1)**  
  Authors: Jinjie Mai, Gordon Guocheng Qian, Willi Menapace, Arpit Sahni, Chaoyang Wang, Ashkan Mirzaei, Runjia Li, Sergey Tulyakov, Bernard Ghanem, Peter Wonka, Rameen Abdal  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.24560v1.pdf)  
  Keywords: benchmark, diffusion transformer, evaluation, v2v, video diffusion, video editing, video to video, video-to-video  
- **[ID-V2V: Identity-Preserving Video Restylization](https://arxiv.org/abs/2607.22830v1)**  
  Authors: Yuancheng Xu, Mingming He, Pablo Salamanca, Li Ma, Yash Kant, Emmett Steven, Paul Debevec, Ning Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.22830v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Eyeline-Labs/ID-V2V?style=social)](https://github.com/Eyeline-Labs/ID-V2V)  
  Keywords: creative, identity, identity-preserving, keyframe, style, v2v, video restylization, video synthesis, video to video, video-to-video  

### Video Inpainting & Completion

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
- **[ImageWAM: Do World Action Models Really Need Video Generation, or Just Image Editing?](https://arxiv.org/abs/2606.19531v1)**  
  Authors: Yuyang Zhang, Wenyao Zhang, Zekun Qi, He Zhang, Haitao Lin, Jingbo Zhang, Yao Mu, Xiaokang Yang, Wenjun Zeng, Xin Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.19531v1.pdf)  
  Keywords: denoising, flow matching, video generation, video prediction  
- **[R2RDreamer: 3D-aware Data Augmentation for Spatially-generalized 2D Manipulation Policies](https://arxiv.org/abs/2606.17040v1)**  
  Authors: Xiuwei Xu, Haowen Sun, Angyuan Ma, Yiwei Zhang, Zhenyu Wu, Xiaofeng Wang, Bingyao Yu, Zheng Zhu, Jie Zhou, Jiwen Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.17040v1.pdf)  
  Keywords: 3d-aware, controllable, image to video, image-to-video, simulation, style, video completion  
- **[MemoryVAM: Integrating Memory into Video Action Model for Robot Manipulation](https://arxiv.org/abs/2606.20679v1)**  
  Authors: Yuxin Jiang, Chang Yu, Yunuo Chen, Xiang Feng, Yin Yang, Nishank Gite, Chenfanfu Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.20679v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://MemoryVAM.github.io)  
  Keywords: diffusion transformer, dit, video prediction, video world model, world model  
- **[OmniGen-AR: AutoRegressive Any-to-Image Generation](https://arxiv.org/abs/2606.09156v1)**  
  Authors: Junke Wang, Xun Wang, Qiushan Guo, Peize Sun, Weilin Huang, Zuxuan Wu, Yu-Gang Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.09156v1.pdf)  
  Keywords: autoregressive, benchmark, frame prediction, text to video, text-to-video, video generation  
- **[Detecting Temporally Localized Manipulations in Authentic Video Streams](https://arxiv.org/abs/2606.07090v1)**  
  Authors: Okan Umur, Ali Emre Güşlü, Ibrahim Delibasoglu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.07090v1.pdf) | [![GitHub](https://img.shields.io/github/stars/OkanUmur/temporally-localized-video-manipulation-detection?style=social)](https://github.com/OkanUmur/temporally-localized-video-manipulation-detection)  
  Keywords: benchmark, video editing, video inpainting, video manipulation  

### Video Super-Resolution & Enhancement

*Showing the latest 50 out of 148 papers*

- **[EmoWorld: A Decoupled Affective Field for Controllable Emotional Video Generation](https://arxiv.org/abs/2608.06231v1)**  
  Authors: Bingyuan Wang, Baistan Zhyldyzbekov, Kunyu Feng, Zeyu Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.06231v1.pdf)  
  Keywords: camera-conditioned, controllable, denoising, diffusion transformer, dit, flow matching, image to video, image-to-video, text to video, text-to-video, video diffusion, video diffusion transformer, video dit, video generation  
- **[Sample-Adaptive Latent Rewards for Uncertainty-Guided Diffusion Post-Training](https://arxiv.org/abs/2608.06125v1)**  
  Authors: Rui Li, Yuanzhi Liang, Ke Hao, Ziqiao Weng, Haibin Huang, Chi Zhang, XueLong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.06125v1.pdf)  
  Keywords: denoising, efficient, trajectory, video diffusion  
- **[Adaptive-WAM: Quality-Guided Early-Exit Planning from Intermediate Video-Diffusion Features](https://arxiv.org/abs/2608.06008v1)**  
  Authors: Sining Ang, Yuguang Yang, Yan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.06008v1.pdf)  
  Keywords: autonomous driving, denoising, diffusion model, diffusion transformer, dit, driving, trajectory, video denoising, video diffusion, video generation, video synthesis, video world model, world model  
- **[Diff-VF: Training-free High-quality Long Video Generation via Diffusion Model](https://arxiv.org/abs/2608.05976v1)**  
  Authors: Haoning Yang, Xinyuan Chen, Yaohui Wang, Guo Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05976v1.pdf)  
  Keywords: diffusion model, evaluation, long video, video diffusion, video enhancement, video generation  
- **[Vorch-Director: Interactive World Story Model via Noise-Aware Error Rectification](https://arxiv.org/abs/2608.05776v1)**  
  Authors: Lisai Zhang, Yidi Wu, Qi Liu, Xin Ma, Yang Ding, Gang Yue, Siqian Yang, Jingyuan Chen, Lin Ma, Yaohui Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05776v1.pdf)  
  Keywords: audio-visual generation, autoregressive, benchmark, denoising, diffusion transformer, efficient, flow matching, identity, interactive, long video, reference-guided, video generation  
- **[Vorch-Streamer: Extending Human Audio-Visual Generation to Real-Time Long-Form Streaming](https://arxiv.org/abs/2608.05663v1)**  
  Authors: Menglin Han, Yang Ding, Yulei Lu, Haoran Yu, Xin Ma, Junyi Chen, Zhangkai Ni, Lin Ma, Yaohui Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05663v1.pdf)  
  Keywords: audio-video generation, audio-visual generation, avatar, denoising, distillation, identity, long-form, streaming, video generation  
- **[In-Context Forcing: Uncovering Context Effects in Autoregressive Video Diffusion](https://arxiv.org/abs/2608.05237v1)**  
  Authors: Lingxiao Yang, Liu Liu, Moran Li, Han Feng, Wenjian Cao, Jiangning Zhang, Ye Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05237v1.pdf)  
  Keywords: acceleration, autoregressive, autoregressive video, denoising, dynamics, temporal consistency, video diffusion  
- **[MobileWAM: Bridging World Action Models to Mobile Manipulation with Chain-of-Foresight](https://arxiv.org/abs/2608.04657v2)**  
  Authors: Zehua Fan, Junjie He, Wenxuan Song, Xi Wang, Wenqi Lyu, Linge Zhao, Fuhao Li, Zihan You, Yifei Yang, Kaiming Xu, Qi Jiang, Yue Jiang, Haoang Li, Cheng Chi, Feng Gao, Bailin Li, Yan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.04657v2.pdf)  
  Keywords: architecture, denoising, diffusion transformer, dynamics, robot learning, video diffusion, video diffusion transformer, video generation  
- **[OmniVR: Joint Video-Audio Conditional Generation for Restoring Degraded Historical Films](https://arxiv.org/abs/2608.04224v1)**  
  Authors: Xin Lu, Zihao Fan, Mingchen Zhong, Jie Huang, Xueyang Fu, Zheng-Jun Zha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.04224v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xin1u.github.io/OminiVR_PAGE)  
  Keywords: architecture, audio-video generation, benchmark, dit, film, i2v, image to video, image-to-video, joint audio-video, long video, temporal consistency, video generation, video restoration, video-to-audio  
- **[EchoCache: Energy-Guided Cross-Modal Caching for Efficient Audio-Driven Video Generation](https://arxiv.org/abs/2608.02474v1)**  
  Authors: Jiayu Chen, Xiaoyu Wu, Rongshan Gao, Maoliang Li, Zihao Zheng, Xinhao Sun, Hailong Zou, Guojie Luo, Xiang Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.02474v1.pdf) | [![GitHub](https://img.shields.io/github/stars/IF-LAB-PKU/EchoCache?style=social)](https://github.com/IF-LAB-PKU/EchoCache)  
  Keywords: audio-driven, benchmark, denoising, efficient, video generation  

### World Models & Simulation

*Showing the latest 50 out of 253 papers*

- **[Adaptive-WAM: Quality-Guided Early-Exit Planning from Intermediate Video-Diffusion Features](https://arxiv.org/abs/2608.06008v1)**  
  Authors: Sining Ang, Yuguang Yang, Yan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.06008v1.pdf)  
  Keywords: autonomous driving, denoising, diffusion model, diffusion transformer, dit, driving, trajectory, video denoising, video diffusion, video generation, video synthesis, video world model, world model  
- **[GAUGE: A Measurement-Grounded Benchmark for Physical Fidelity in Simulation Engines and Video World Models](https://arxiv.org/abs/2608.05948v1)**  
  Authors: Shuai Wang, Yaxin Feng, Xuekun Jiang, Shihan Tian, Ningyu Yan, Xing Shen, Chaoyang Lyu, Hui Wang, Yunsong Zhou, Hanqing Wang, Jiangmiao Pang, Yang Xiang, Xing Gao, Chunhua Shen, Weinan Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05948v1.pdf)  
  Keywords: benchmark, embodied, evaluation, image to video, image-to-video, physical, physics, simulation, trajectory  
- **[Robust-WAM: Bridging Generative Pretraining and Semantic Foresight in World-Action Models](https://arxiv.org/abs/2608.05903v1)**  
  Authors: Haodong Yan, Junfeng Li, Junjie He, Zhide Zhong, MingMing Yu, Wenxuan Song, Jiaguan Zhu, Yangyang Zheng, Yuqiao Du, Jiadi You, Yingjie Cai, Xu Yan, Guanyi Zhao, Bingbing Liu, Haoang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05903v1.pdf)  
  Keywords: dynamics, simulation, video generation  
- **[Vorch-Director: Interactive World Story Model via Noise-Aware Error Rectification](https://arxiv.org/abs/2608.05776v1)**  
  Authors: Lisai Zhang, Yidi Wu, Qi Liu, Xin Ma, Yang Ding, Gang Yue, Siqian Yang, Jingyuan Chen, Lin Ma, Yaohui Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05776v1.pdf)  
  Keywords: audio-visual generation, autoregressive, benchmark, denoising, diffusion transformer, efficient, flow matching, identity, interactive, long video, reference-guided, video generation  
- **[HelloWorld: Enabling Socially Interactive Characters in Video World Models](https://arxiv.org/abs/2608.05070v1)**  
  Authors: Liangyang Ouyang, Ruicong Liu, Xuangeng Chu, Kaipeng Zhang, Yoichi Sato  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05070v1.pdf) | [![GitHub](https://img.shields.io/github/stars/AlayaLab/HelloWorld?style=social)](https://github.com/AlayaLab/HelloWorld)  
  Keywords: benchmark, camera motion, distillation, dit, evaluation, interactive, video generation, video world model, world model  
- **[CrossScope: A Role-Asymmetric World Model for Joint Dual-Scope Surgical Video Prediction](https://arxiv.org/abs/2608.03211v1)**  
  Authors: Wanhao Liu, Jinsong Lin, Rulin Zhou, Chi Kit Ng, Wenbin Pan, Zhiqing Tang, Dongyue Li, Liwei Luo, Yanshen Wu, Panshuo Li, Zhiyong Xiong, Huxin Gao, Tamas Haidegger, Hongliang Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.03211v1.pdf)  
  Keywords: benchmark, dynamics, video generation, video prediction, world model  
- **[ProWorld: Progress-Aware Hyperbolic World Models for Long-Horizon Visual Goal Reaching](https://arxiv.org/abs/2608.01926v1)**  
  Authors: Zihan Liu, Yuzhe Zhuang, Yuanzu Li, Wanshuang Gou, Jiahong Liu, Min Zhou, Menglin Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01926v1.pdf)  
  Keywords: dynamics, style, visual world model, world model  
- **[EndoWAM: A Grounded World-Action Model for Generalizable Endoscopic Navigation](https://arxiv.org/abs/2608.01221v1)**  
  Authors: Jinsong Lin, Zikang Pan, Wanhao Liu, Chi Kit Ng, Liangjing Shao, Zihang Yu, Ziyu Wang, Yin Wang, Jiaxi Wang, Jeremy Yuen-Chun Teoh, Zhiyong Xiong, Huxin Gao, Hongliang Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01221v1.pdf)  
  Keywords: denoising, diffusion transformer, dynamics, video world model, world model  
- **[MiniWorld: Democratizing the Training of Video World Models from Scratch](https://arxiv.org/abs/2608.01127v2)**  
  Authors: Yian Zhao, Ruochong Zheng, Hongcan Guo, Yu Yan, Jian Zhang, Jie Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.01127v2.pdf)  
  Keywords: autoregressive, autoregressive video, denoising, diffusion transformer, distillation, dynamics, efficient, embodied, flow matching, interactive, simulation, streaming, video diffusion, video diffusion transformer, video generation  
- **[FlexComposer: Unified Video Compositing from Images to Dynamic Footage with Flexible Trajectory Control](https://arxiv.org/abs/2607.29627v1)**  
  Authors: Songchun Zhang, Sitong Guo, Xianghao Kong, Pengwei Liu, Yuwei Guo, Lvmin Zhang, Anyi Rao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.29627v1.pdf)  
  Keywords: cinematic, dynamics, motion control, simulation, temporal consistency, trajectory  



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
