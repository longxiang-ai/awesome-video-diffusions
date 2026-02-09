# Awesome Video Diffusions [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Video Diffusion Models and Video Generation. Content is automatically updated daily.

> Last Update: 2026-02-09 16:15:02

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
- [Applications](#applications) (53 papers) - Domain-specific applications of video diffusion models
- [Architecture & Efficiency](#architecture-&-efficiency) (369 papers) - Architectural innovations (DiT, UNet), flow matching, and training/inference efficiency
- [Audio & Multi-modal](#audio-&-multi-modal) (37 papers) - Audio-driven and multi-modal conditioned video generation
- [Controllable Generation](#controllable-generation) (118 papers) - Controllable video generation with motion, camera, pose, or layout guidance
- [Human & Character Animation](#human-&-character-animation) (33 papers) - Human-centric video generation including talking heads, dance, and character animation
- [Image-to-Video Generation](#image-to-video-generation) (43 papers) - Methods for animating still images into videos
- [Long Video Generation](#long-video-generation) (123 papers) - Generating temporally consistent long-form videos beyond short clips
- [Personalization & Customization](#personalization-&-customization) (90 papers) - Personalized video generation with custom subjects, identities, or styles
- [Physical Understanding](#physical-understanding) (134 papers) - Physics-aware video generation and dynamics modeling
- [Surveys & Benchmarks](#surveys-&-benchmarks) (202 papers) - Survey papers, benchmarks, and evaluation metrics for video generation
- [Text-to-Video Generation](#text-to-video-generation) (76 papers) - Foundation models and methods for generating videos from text prompts
- [Video Editing](#video-editing) (43 papers) - Diffusion-based video editing, style transfer, and manipulation
- [Video Inpainting & Completion](#video-inpainting-&-completion) (11 papers) - Video inpainting, completion, outpainting, and temporal prediction
- [Video Super-Resolution & Enhancement](#video-super-resolution-&-enhancement) (61 papers) - Video quality improvement, upscaling, restoration, and frame interpolation
- [World Models & Simulation](#world-models-&-simulation) (100 papers) - Video generation as world simulators and interactive environment generation



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3D-aware Video Generation

- **[CineScene: Implicit 3D as Effective Scene Representation for Cinematic Video Generation](https://arxiv.org/abs/2602.06959v1)**  
  Authors: Kaiyi Huang, Yukun Huang, Yu Li, Jianhong Bai, Xintao Wang, Zinan Lin, Xuefei Ning, Jiwen Yu, Pengfei Wan, Yu Wang, Xihui Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06959v1.pdf)  
  Keywords: 3d-aware, physical, text-to-video, trajectory, dit, video synthesis, video generation  
- **[SkeletonGaussian: Editable 4D Generation through Gaussian Skeletonization](https://arxiv.org/abs/2602.04271v1)**  
  Authors: Lifan Wu, Ruijie Zhu, Yubo Ai, Tianzhu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.04271v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wusar.github.io/projects/skeletongaussian)  
  Keywords: dit, 4d generation  
- **[3D-Aware Implicit Motion Control for View-Adaptive Human Video Generation](https://arxiv.org/abs/2602.03796v1)**  
  Authors: Zhixue Fang, Xu He, Songlin Tang, Haoxian Zhang, Qingfeng Li, Xiaoqiang Liu, Pengfei Wan, Kun Gai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03796v1.pdf)  
  Keywords: motion control, human motion, dynamics, camera control, dit, 3d-aware, video generation  
- **[FreeFix: Boosting 3D Gaussian Splatting via Fine-Tuning-Free Diffusion Models](https://arxiv.org/abs/2601.20857v1)**  
  Authors: Hongyu Zhou, Zisen Shao, Sheng Miao, Pan Wang, Dongfeng Bai, Bingbing Liu, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.20857v1.pdf)  
  Keywords: dit, diffusion model, novel view, video diffusion  
- **[AnyView: Synthesizing Any Novel View in Dynamic Scenes](https://arxiv.org/abs/2601.16982v1)**  
  Authors: Basile Van Hoorick, Dian Chen, Shun Iwase, Pavel Tokmakov, Muhammad Zubair Irshad, Igor Vasiljevic, Swati Gupta, Fangzhou Cheng, Sergey Zakharov, Vitor Campagnolo Guizilini  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.16982v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://tri-ml.github.io/AnyView)  
  Keywords: benchmark, novel view, temporal consistency, video generation  
- **[Memory-V2V: Augmenting Video-to-Video Diffusion Models with Memory](https://arxiv.org/abs/2601.16296v1)**  
  Authors: Dohun Lee, Chun-Hao Paul Huang, Xuelin Chen, Jong Chul Ye, Duygu Ceylan, Hyeonho Jeong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.16296v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://dohunlee1.github.io/MemoryV2V)  
  Keywords: video-to-video, video editing, diffusion model, novel view, video diffusion, dit, long video  
- **[GR3EN: Generative Relighting for 3D Environments](https://arxiv.org/abs/2601.16272v2)**  
  Authors: Xiaoyan Xing, Philipp Henzler, Junhwa Hur, Runze Li, Jonathan T. Barron, Pratul P. Srinivasan, Dor Verbin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.16272v2.pdf)  
  Keywords: controllable, video-to-video, diffusion model, novel view, video diffusion, dit  
- **[CamPilot: Improving Camera Control in Video Diffusion Model with Efficient Camera Reward Feedback](https://arxiv.org/abs/2601.16214v1)**  
  Authors: Wenhang Ge, Guibao Shen, Jiawei Feng, Luozhou Wang, Hao Lu, Xingye Tian, Xin Tao, Ying-Cong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.16214v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://a-bigbao.github.io/CamPilot)  
  Keywords: benchmark, efficient, video diffusion, diffusion model, novel view, camera control  
- **[Rotate Your Character: Revisiting Video Diffusion Models for High-Quality 3D Character Generation](https://arxiv.org/abs/2601.05722v1)**  
  Authors: Jin Wang, Jianxiang Lu, Comi Chen, Guangzheng Xu, Haoyu Yang, Peng Chen, Na Zhang, Yifan Xu, Longhuang Wu, Shuai Shao, Qinglin Lu, Ping Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.05722v1.pdf)  
  Keywords: controllable, image-to-video, diffusion model, novel view, video diffusion, dit, video generation  
- **[RoboVIP: Multi-View Video Generation with Visual Identity Prompting Augments Robot Manipulation](https://arxiv.org/abs/2601.05241v1)**  
  Authors: Boyang Wang, Haoran Zhang, Shujie Zhang, Jinkun Hao, Mingda Jia, Qi Lv, Yucheng Mao, Zhaoyang Lyu, Jia Zeng, Xudong Xu, Jiangmiao Pang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.05241v1.pdf)  
  Keywords: simulation, physical, diffusion model, identity, multi-view video, dit, robotics, video generation  

### Applications

*Showing the latest 50 out of 53 papers*

- **[Driving with DINO: Vision Foundation Features as a Unified Bridge for Sim-to-Real Generation in Autonomous Driving](https://arxiv.org/abs/2602.06159v1)**  
  Authors: Xuyang Chen, Conglang Zhang, Chuanheng Fu, Zihao Yang, Kaixuan Zhou, Yizhi Zhang, Jianan He, Yanfeng Zhang, Mingwei Sun, Zengmao Wang, Zhen Dong, Xiaoxiao Long, Liqiu Meng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06159v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://albertchen98.github.io/DwD-project)  
  Keywords: autonomous driving, controllable, simulation, video diffusion, video generation  
- **[LSA: Localized Semantic Alignment for Enhancing Temporal Consistency in Traffic Video Generation](https://arxiv.org/abs/2602.05966v1)**  
  Authors: Mirlan Karimov, Teodora Spasojevic, Markus Braun, Julian Wiederer, Vasileios Belagiannis, Marc Pollefeys  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.05966v1.pdf)  
  Keywords: evaluation, autonomous driving, controllable, temporal consistency, dit, video generation  
- **[PrevizWhiz: Combining Rough 3D Scenes and 2D Video to Guide Generative Video Previsualization](https://arxiv.org/abs/2602.03838v1)**  
  Authors: Erzhen Hu, Frederik Brudy, David Ledo, George Fitzmaurice, Fraser Anderson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03838v1.pdf)  
  Keywords: dit, film, creative  
- **[BridgeV2W: Bridging Video Generation Models to Embodied World Models via Embodiment Masks](https://arxiv.org/abs/2602.03793v1)**  
  Authors: Yixiang Chen, Peiyan Li, Jiabing Yang, Keji He, Xiangnan Wu, Yuan Xu, Kai Wang, Jing Liu, Nianfeng Liu, Yan Huang, Liang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03793v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://BridgeV2W.github.io)  
  Keywords: evaluation, style, world model, architecture, dit, robotics, video generation  
- **[InstaDrive: Instance-Aware Driving World Models for Realistic and Consistent Video Generation](https://arxiv.org/abs/2602.03242v1)**  
  Authors: Zhuoran Yang, Xi Guo, Chenjing Ding, Chiyu Wang, Wei Wu, Yanyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03242v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://shanpoyang654.github.io/InstaDrive/page.html)  
  Keywords: evaluation, autonomous driving, world model, temporal consistency, identity, dit, video generation  
- **[ConsisDrive: Identity-Preserving Driving World Models for Video Generation by Instance Mask](https://arxiv.org/abs/2602.03213v2)**  
  Authors: Zhuoran Yang, Yanyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03213v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://shanpoyang654.github.io/ConsisDrive/page.html)  
  Keywords: autonomous driving, world model, temporal consistency, identity, trajectory, video generation  
- **[The Script is All You Need: An Agentic Framework for Long-Horizon Dialogue-to-Cinematic Video Generation](https://arxiv.org/abs/2601.17737v2)**  
  Authors: Chenyu Mu, Xin He, Qu Yang, Wanshun Chen, Jiadi Yao, Huang Liu, Zihao Yi, Bo Zhao, Xingyu Chen, Ruotian Ma, Fanghua Ye, Erkun Yang, Cheng Deng, Zhaopeng Tu, Xiaolong Li, Linus  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.17737v2.pdf)  
  Keywords: long-form, evaluation, creative, benchmark, film, concept, video generation  
- **[Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning](https://arxiv.org/abs/2601.16163v1)**  
  Authors: Moo Jin Kim, Yihuai Gao, Tsung-Yi Lin, Yen-Chen Lin, Yunhao Ge, Grace Lam, Percy Liang, Shuran Song, Ming-Yu Liu, Chelsea Finn, Jinwei Gu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.16163v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://research.nvidia.com/labs/dir/cosmos-policy)  
  Keywords: evaluation, simulation, benchmark, physical, world model, dit, robotics, video generation  
- **[From Generative Engines to Actionable Simulators: The Imperative of Physical Grounding in World Models](https://arxiv.org/abs/2601.15533v1)**  
  Authors: Zhikang Chen, Tingting Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.15533v1.pdf)  
  Keywords: evaluation, physical, survey, world model, dynamics, medical, video generation  
- **[Rethinking Video Generation Model for the Embodied World](https://arxiv.org/abs/2601.15282v1)**  
  Authors: Yufan Deng, Zilin Pan, Hongyu Zhang, Xiaojie Li, Ruoqing Hu, Yufei Ding, Yiming Zou, Yan Zeng, Daquan Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.15282v1.pdf)  
  Keywords: evaluation, physical, benchmark, efficient, robotics, video generation  

### Architecture & Efficiency

*Showing the latest 50 out of 369 papers*

- **[CineScene: Implicit 3D as Effective Scene Representation for Cinematic Video Generation](https://arxiv.org/abs/2602.06959v1)**  
  Authors: Kaiyi Huang, Yukun Huang, Yu Li, Jianhong Bai, Xintao Wang, Zinan Lin, Xuefei Ning, Jiwen Yu, Pengfei Wan, Yu Wang, Xihui Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06959v1.pdf)  
  Keywords: 3d-aware, physical, text-to-video, trajectory, dit, video synthesis, video generation  
- **[RFDM: Residual Flow Diffusion Model for Efficient Causal Video Editing](https://arxiv.org/abs/2602.06871v1)**  
  Authors: Mohammadreza Salehi, Mehdi Noroozi, Luca Morreale, Ruchika Chavhan, Malcolm Chadwick, Alberto Gil Ramos, Abhinav Mehrotra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06871v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://smsd75.github.io/RFDM_page)  
  Keywords: style, denoising, benchmark, autoregressive, video-to-video, efficient, video editing, diffusion model, dit, video generation  
- **[DiTS: Multimodal Diffusion Transformers Are Time Series Forecasters](https://arxiv.org/abs/2602.06597v1)**  
  Authors: Haoran Zhang, Haixuan Liu, Yong Liu, Yunzhong Qiu, Yuxuan Wang, Jianmin Wang, Mingsheng Long  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06597v1.pdf)  
  Keywords: diffusion transformer, benchmark, autoregressive, architecture, dit, video generation  
- **[Bridging the Indoor-Outdoor Gap: Vision-Centric Instruction-Guided Embodied Navigation for the Last Meters](https://arxiv.org/abs/2602.06427v1)**  
  Authors: Yuxiang Zhao, Yirong Yang, Yanqing Zhu, Yanfen Shen, Chiyu Wang, Zhining Gu, Pei Shi, Wei Guo, Mu Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06427v1.pdf)  
  Keywords: trajectory, dit, video synthesis  
- **[Context Forcing: Consistent Autoregressive Video Generation with Long Context](https://arxiv.org/abs/2602.06028v1)**  
  Authors: Shuo Chen, Cong Wei, Sun Sun, Ping Nie, Kai Zhou, Ge Zhang, Ming-Hsuan Yang, Wenhu Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06028v1.pdf)  
  Keywords: evaluation, streaming, autoregressive, architecture, long video, video generation  
- **[LSA: Localized Semantic Alignment for Enhancing Temporal Consistency in Traffic Video Generation](https://arxiv.org/abs/2602.05966v1)**  
  Authors: Mirlan Karimov, Teodora Spasojevic, Markus Braun, Julian Wiederer, Vasileios Belagiannis, Marc Pollefeys  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.05966v1.pdf)  
  Keywords: evaluation, autonomous driving, controllable, temporal consistency, dit, video generation  
- **[DisCa: Accelerating Video Diffusion Transformers with Distillation-Compatible Learnable Feature Caching](https://arxiv.org/abs/2602.05449v2)**  
  Authors: Chang Zou, Changlin Li, Yang Li, Patrol Li, Jianbing Wu, Xiao He, Songtao Liu, Zhao Zhong, Kailin Huang, Linfeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.05449v2.pdf)  
  Keywords: distillation, diffusion transformer, acceleration, diffusion model, video diffusion, dit, video generation  
- **[Stable Velocity: A Variance Perspective on Flow Matching](https://arxiv.org/abs/2602.05435v1)**  
  Authors: Donglin Yang, Yongxing Zhang, Xin Yu, Liang Hou, Xin Tao, Pengfei Wan, Xiaojuan Qi, Renjie Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.05435v1.pdf) | [![GitHub](https://img.shields.io/github/stars/linYDTHU/StableVelocity?style=social)](https://github.com/linYDTHU/StableVelocity)  
  Keywords: acceleration, text-to-video, dynamics, dit, flow matching  
- **[FlashBlock: Attention Caching for Efficient Long-Context Block Diffusion](https://arxiv.org/abs/2602.05305v2)**  
  Authors: Zhuokun Chen, Jianfei Cai, Bohan Zhuang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.05305v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://caesarhhh.github.io/FlashBlock)  
  Keywords: long-form, long video, efficient, video generation  
- **[GT-SVJ: Generative-Transformer-Based Self-Supervised Video Judge For Efficient Video Reward Modeling](https://arxiv.org/abs/2602.05202v1)**  
  Authors: Shivanshu Shekhar, Uttaran Bhattacharya, Raghavendra Addanki, Mehrab Tanjim, Somdeb Sarkhel, Tong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.05202v1.pdf)  
  Keywords: evaluation, dynamics, efficient, video generation  

### Audio & Multi-modal

- **[Meta Engine: A Unified Semantic Query Engine on Heterogeneous LLM-Based Query Systems](https://arxiv.org/abs/2602.01701v1)**  
  Authors: Ruyu Li, Tinghui Zhang, Haodi Ma, Daisy Zhe Wang, Yifan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.01701v1.pdf)  
  Keywords: multi-modal, evaluation, architecture, dit  
- **[Omni-Judge: Can Omni-LLMs Serve as Human-Aligned Judges for Text-Conditioned Audio-Video Generation?](https://arxiv.org/abs/2602.01623v1)**  
  Authors: Susan Liang, Chao Huang, Filippos Bellos, Yolo Yunlong Tang, Qianxiang Shen, Jing Bi, Luchuan Song, Zeliang Zhang, Jason Corso, Chenliang Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.01623v1.pdf)  
  Keywords: evaluation, physical, multi-modal, text-to-video, dit, video generation  
- **[JUST-DUB-IT: Video Dubbing via Joint Audio-Visual Diffusion](https://arxiv.org/abs/2601.22143v1)**  
  Authors: Anthony Chen, Naomi Ken Korem, Tavi Halperin, Matan Ben Yosef, Urska Jelercic, Ofir Bibi, Or Patashnik, Daniel Cohen-Or  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.22143v1.pdf)  
  Keywords: sound, video-to-video, multi-modal, dynamics, diffusion model, identity, video diffusion, dit  
- **[EditYourself: Audio-Driven Generation and Manipulation of Talking Head Videos with Diffusion Transformers](https://arxiv.org/abs/2601.22127v1)**  
  Authors: John Flynn, Wolfgang Paier, Dimitar Dinev, Sam Nhut Nguyen, Hayk Poghosyan, Manuel Toribio, Sandipan Banerjee, Guy Gafni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.22127v1.pdf)  
  Keywords: human motion, audio-driven, diffusion transformer, video-to-video, diffusion model, talking head, identity, video diffusion, dit  
- **[Exploring Talking Head Models With Adjacent Frame Prior for Speech-Preserving Facial Expression Manipulation](https://arxiv.org/abs/2601.12876v1)**  
  Authors: Zhenxuan Lu, Zhihua Xu, Zhijing Yang, Feng Gao, Yongyi Lu, Keze Wang, Tianshui Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.12876v1.pdf)  
  Keywords: evaluation, audio-driven, talking head  
- **[AI-based System for Transforming text and sound to Educational Videos](https://arxiv.org/abs/2601.17022v1)**  
  Authors: M. E. ElAlami, S. M. Khater, M. El. R. Rehan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.17022v1.pdf)  
  Keywords: sound, interactive, diffusion model, education, dit, video generation  
- **[ATATA: One Algorithm to Align Them All](https://arxiv.org/abs/2601.11194v1)**  
  Authors: Boyi Pang, Savva Ignatyev, Vladimir Ippolitov, Ramil Khafizov, Yurii Melnik, Oleg Voynov, Maksim Nakhodnov, Aibek Alanov, Xiaopeng Fan, Peter Wonka, Evgeny Burnaev  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.11194v1.pdf)  
  Keywords: distillation, multi-modal, rectified flow, dit, video generation  
- **[Perception Test 2025: Challenge Summary and a Unified VQA Extension](https://arxiv.org/abs/2601.06287v1)**  
  Authors: Joseph Heyward, Nikhil Pathasarathy, Tyler Zhu, Aravindh Mahendran, João Carreira, Dima Damen, Andrew Zisserman, Viorica Pătrăucean  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.06287v1.pdf)  
  Keywords: sound, benchmark, dit, long video, video generation  
- **[From Understanding to Engagement: Personalized pharmacy Video Clips via Vision Language Models (VLMs)](https://arxiv.org/abs/2601.05059v1)**  
  Authors: Suyash Mishra, Qiang Li, Srikanth Patil, Anubhav Girdhar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.05059v1.pdf)  
  Keywords: evaluation, benchmark, personalization, efficient, multi-modal, education, dit, long video  
- **[Investigating the Viability of Employing Multi-modal Large Language Models in the Context of Audio Deepfake Detection](https://arxiv.org/abs/2601.00777v1)**  
  Authors: Akanksha Chuchra, Shukesh Reddy, Sudeepta Mishra, Abhijit Das, Abhinav Dhall  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.00777v1.pdf)  
  Keywords: multi-modal, evaluation  

### Controllable Generation

*Showing the latest 50 out of 118 papers*

- **[CineScene: Implicit 3D as Effective Scene Representation for Cinematic Video Generation](https://arxiv.org/abs/2602.06959v1)**  
  Authors: Kaiyi Huang, Yukun Huang, Yu Li, Jianhong Bai, Xintao Wang, Zinan Lin, Xuefei Ning, Jiwen Yu, Pengfei Wan, Yu Wang, Xihui Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06959v1.pdf)  
  Keywords: 3d-aware, physical, text-to-video, trajectory, dit, video synthesis, video generation  
- **[Bridging the Indoor-Outdoor Gap: Vision-Centric Instruction-Guided Embodied Navigation for the Last Meters](https://arxiv.org/abs/2602.06427v1)**  
  Authors: Yuxiang Zhao, Yirong Yang, Yanqing Zhu, Yanfen Shen, Chiyu Wang, Zhining Gu, Pei Shi, Wei Guo, Mu Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06427v1.pdf)  
  Keywords: trajectory, dit, video synthesis  
- **[Driving with DINO: Vision Foundation Features as a Unified Bridge for Sim-to-Real Generation in Autonomous Driving](https://arxiv.org/abs/2602.06159v1)**  
  Authors: Xuyang Chen, Conglang Zhang, Chuanheng Fu, Zihao Yang, Kaixuan Zhou, Yizhi Zhang, Jianan He, Yanfeng Zhang, Mingwei Sun, Zengmao Wang, Zhen Dong, Xiaoxiao Long, Liqiu Meng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06159v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://albertchen98.github.io/DwD-project)  
  Keywords: autonomous driving, controllable, simulation, video diffusion, video generation  
- **[LSA: Localized Semantic Alignment for Enhancing Temporal Consistency in Traffic Video Generation](https://arxiv.org/abs/2602.05966v1)**  
  Authors: Mirlan Karimov, Teodora Spasojevic, Markus Braun, Julian Wiederer, Vasileios Belagiannis, Marc Pollefeys  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.05966v1.pdf)  
  Keywords: evaluation, autonomous driving, controllable, temporal consistency, dit, video generation  
- **[Pathwise Test-Time Correction for Autoregressive Long Video Generation](https://arxiv.org/abs/2602.05871v1)**  
  Authors: Xunzhi Xiang, Zixuan Duan, Guiyu Zhang, Haiyu Zhang, Zhe Gao, Junta Wu, Shaofeng Zhang, Tengfei Wang, Qi Fan, Chunchao Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.05871v1.pdf)  
  Keywords: long video, benchmark, autoregressive, diffusion model, trajectory, video synthesis, video generation  
- **[Sparse Video Generation Propels Real-World Beyond-the-View Vision-Language Navigation](https://arxiv.org/abs/2602.05827v1)**  
  Authors: Hai Zhang, Siqi Liang, Li Chen, Yuxian Li, Yukuan Xu, Yichao Zhong, Fu Zhang, Hongyang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.05827v1.pdf)  
  Keywords: trajectory, video generation  
- **[3D-Aware Implicit Motion Control for View-Adaptive Human Video Generation](https://arxiv.org/abs/2602.03796v1)**  
  Authors: Zhixue Fang, Xu He, Songlin Tang, Haoxian Zhang, Qingfeng Li, Xiaoqiang Liu, Pengfei Wan, Kun Gai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03796v1.pdf)  
  Keywords: motion control, human motion, dynamics, camera control, dit, 3d-aware, video generation  
- **[ConsisDrive: Identity-Preserving Driving World Models for Video Generation by Instance Mask](https://arxiv.org/abs/2602.03213v2)**  
  Authors: Zhuoran Yang, Yanyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03213v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://shanpoyang654.github.io/ConsisDrive/page.html)  
  Keywords: autonomous driving, world model, temporal consistency, identity, trajectory, video generation  
- **[Quant VideoGen: Auto-Regressive Long Video Generation via 2-Bit KV-Cache Quantization](https://arxiv.org/abs/2602.02958v1)**  
  Authors: Haocheng Xi, Shuo Yang, Yilong Zhao, Muyang Li, Han Cai, Xingyang Li, Yujun Lin, Zhuoyang Zhang, Jintao Zhang, Xiuyu Li, Zhiying Xu, Jun Wu, Chenfeng Xu, Ion Stoica, Song Han, Kurt Keutzer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.02958v1.pdf)  
  Keywords: layout, benchmark, autoregressive, diffusion model, identity, video diffusion, long video, video generation  
- **[Grounding Generated Videos in Feasible Plans via World Models](https://arxiv.org/abs/2602.01960v1)**  
  Authors: Christos Ziakas, Amir Bar, Alessandra Russo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.01960v1.pdf)  
  Keywords: simulation, physical, image-to-video, world model, temporal consistency, dynamics, trajectory, dit, action-conditioned  

### Human & Character Animation

- **[From Blurry to Believable: Enhancing Low-quality Talking Heads with 3D Generative Priors](https://arxiv.org/abs/2602.06122v1)**  
  Authors: Ding-Jiun Huang, Yuanhao Wang, Shao-Ji Yuan, Albert Mosella-Montoro, Francisco Vicente Carrasco, Cheng Zhang, Fernando De la Torre  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06122v1.pdf)  
  Keywords: super-resolution, temporal consistency, talking head, identity, dynamics, avatar  
- **[ShapeGaussian: High-Fidelity 4D Human Reconstruction in Monocular Videos via Vision Priors](https://arxiv.org/abs/2602.05572v1)**  
  Authors: Zhenxiao Liang, Ning Zhang, Youbao Tang, Ruei-Sung Lin, Qixing Huang, Peng Chang, Jing Xiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.05572v1.pdf)  
  Keywords: human motion  
- **[3D-Aware Implicit Motion Control for View-Adaptive Human Video Generation](https://arxiv.org/abs/2602.03796v1)**  
  Authors: Zhixue Fang, Xu He, Songlin Tang, Haoxian Zhang, Qingfeng Li, Xiaoqiang Liu, Pengfei Wan, Kun Gai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03796v1.pdf)  
  Keywords: motion control, human motion, dynamics, camera control, dit, 3d-aware, video generation  
- **[VRGaussianAvatar: Integrating 3D Gaussian Avatars into VR](https://arxiv.org/abs/2602.01674v1)**  
  Authors: Hail Song, Boram Yoon, Seokhwan Yang, Seoyoung Kang, Hyunjeong Kim, Henning Metzmacher, Woontack Woo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.01674v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vrgaussianavatar.github.io)  
  Keywords: interactive, avatar  
- **[Making Avatars Interact: Towards Text-Driven Human-Object Interaction for Controllable Talking Avatars](https://arxiv.org/abs/2602.01538v1)**  
  Authors: Youliang Zhang, Zhengguang Zhou, Zhentao Yu, Ziyao Huang, Teng Hu, Sen Liang, Guozhen Zhang, Ziqiao Peng, Shunkai Li, Yi Chen, Zixiang Zhou, Yuan Zhou, Qinglin Lu, Xiu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.01538v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://interactavatar.github.io)  
  Keywords: human motion, controllable, benchmark, dit, video synthesis, avatar, video generation  
- **[EditYourself: Audio-Driven Generation and Manipulation of Talking Head Videos with Diffusion Transformers](https://arxiv.org/abs/2601.22127v1)**  
  Authors: John Flynn, Wolfgang Paier, Dimitar Dinev, Sam Nhut Nguyen, Hayk Poghosyan, Manuel Toribio, Sandipan Banerjee, Guy Gafni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.22127v1.pdf)  
  Keywords: human motion, audio-driven, diffusion transformer, video-to-video, diffusion model, talking head, identity, video diffusion, dit  
- **[SkyReels-V3 Technique Report](https://arxiv.org/abs/2601.17323v2)**  
  Authors: Debang Li, Zhengcong Fei, Tuanhui Li, Yikun Dou, Zheng Chen, Jiangping Yang, Mingyuan Fan, Jingtao Xu, Jiahua Wang, Baoxuan Gu, Mingshan Chang, Wenjing Cai, Yuqiang Xie, Binjie Mao, Youqiang Zhang, Nuo Pang, Hao Zhang, Yuzhe Jin, Zhiheng Xu, Dixuan Lin, Guibin Chen, Yahui Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.17323v2.pdf) | [![GitHub](https://img.shields.io/github/stars/SkyworkAI/SkyReels-V3?style=social)](https://github.com/SkyworkAI/SkyReels-V3)  
  Keywords: evaluation, diffusion transformer, video-to-video, temporal consistency, world model, architecture, identity, dit, video synthesis, avatar, video generation  
- **[Exploring Talking Head Models With Adjacent Frame Prior for Speech-Preserving Facial Expression Manipulation](https://arxiv.org/abs/2601.12876v1)**  
  Authors: Zhenxuan Lu, Zhihua Xu, Zhijing Yang, Feng Gao, Yongyi Lu, Keze Wang, Tianshui Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.12876v1.pdf)  
  Keywords: evaluation, audio-driven, talking head  
- **[PhysRVG: Physics-Aware Unified Reinforcement Learning for Video Generative Models](https://arxiv.org/abs/2601.11087v1)**  
  Authors: Qiyuan Zhang, Biao Gong, Shuai Tan, Zheng Zhang, Yujun Shen, Xing Zhu, Yuyuan Li, Kelu Yao, Chunhua Shen, Changqing Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.11087v1.pdf)  
  Keywords: denoising, simulation, benchmark, physical, body motion, concept, physics, dit, physics-aware, video generation  
- **[Human detectors are surprisingly powerful reward models](https://arxiv.org/abs/2601.14037v2)**  
  Authors: Kumar Ashutosh, XuDong Wang, Xi Yin, Kristen Grauman, Adam Polyak, Ishan Misra, Rohit Girdhar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.14037v2.pdf)  
  Keywords: physical, dit, human motion, video generation  

### Image-to-Video Generation

- **[RISE-Video: Can Video Generators Decode Implicit World Rules?](https://arxiv.org/abs/2602.05986v1)**  
  Authors: Mingxin Liu, Shuran Ma, Shibei Meng, Xiangyu Zhao, Zicheng Zhang, Shaofeng Zhang, Zhihang Zhong, Peixian Chen, Haoyu Cao, Xing Sun, Haodong Duan, Xue Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.05986v1.pdf)  
  Keywords: evaluation, benchmark, physical, image-to-video, temporal consistency, dynamics, i2v  
- **[FSVideo: Fast Speed Video Diffusion Model in a Highly-Compressed Latent Space](https://arxiv.org/abs/2602.02092v1)**  
  Authors: FSVideo Team, Qingyu Chen, Zhiyuan Fang, Haibin Huang, Xinwei Huang, Tong Jin, Minxuan Lin, Bo Liu, Celong Liu, Chongyang Ma, Xing Mei, Xiaohui Shen, Yaojie Shen, Fuwen Tan, Angtian Wang, Xiao Yang, Yiding Yang, Jiamin Yuan, Lingxi Zhang, Yuxin Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.02092v1.pdf)  
  Keywords: diffusion transformer, image-to-video, architecture, diffusion model, video diffusion, i2v, dit  
- **[Grounding Generated Videos in Feasible Plans via World Models](https://arxiv.org/abs/2602.01960v1)**  
  Authors: Christos Ziakas, Amir Bar, Alessandra Russo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.01960v1.pdf)  
  Keywords: simulation, physical, image-to-video, world model, temporal consistency, dynamics, trajectory, dit, action-conditioned  
- **[PLACID: Identity-Preserving Multi-Object Compositing via Video Diffusion with Synthetic Trajectories](https://arxiv.org/abs/2602.00267v1)**  
  Authors: Gemma Canet Tarrés, Manel Baradad, Francesc Moreno-Noguer, Yumeng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.00267v1.pdf)  
  Keywords: evaluation, layout, image-to-video, diffusion model, identity, video diffusion, i2v  
- **[Zero-Shot Video Restoration and Enhancement with Assistance of Video Diffusion Models](https://arxiv.org/abs/2601.21922v1)**  
  Authors: Cong Cao, Huanjing Yue, Shangbin Xie, Xin Liu, Jingyu Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.21922v1.pdf)  
  Keywords: image-to-video, temporal consistency, text-to-video, diffusion model, video diffusion, video restoration  
- **[MV-S2V: Multi-View Subject-Consistent Video Generation](https://arxiv.org/abs/2601.17756v2)**  
  Authors: Ziyang Song, Xinyu Gong, Bangya Liu, Zelin Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.17756v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://szy-young.github.io/mv-s2v)  
  Keywords: i2v, dit, subject-driven, video generation  
- **[Moaw: Unleashing Motion Awareness for Video Diffusion Models](https://arxiv.org/abs/2601.12761v1)**  
  Authors: Tianqi Zhang, Ziyi Wang, Wenzhao Zheng, Weiliang Chen, Yuanhui Huang, Zhengyang Huang, Jie Zhou, Jiwen Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.12761v1.pdf)  
  Keywords: controllable, image-to-video, diffusion model, video diffusion, dit, video generation  
- **[Tuning-free Visual Effect Transfer across Videos](https://arxiv.org/abs/2601.07833v3)**  
  Authors: Maxwell Jones, Rameen Abdal, Or Patashnik, Ruslan Salakhutdinov, Sergey Tulyakov, Jun-Yan Zhu, Kuan-Chieh Jackson Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.07833v3.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://tuningfreevisualeffects-maker.github.io/Tuning-free-Visual-Effect-Transfer-across-Videos-Project-Page)  
  Keywords: video-to-video, image-to-video, text-to-video, dynamics, dit  
- **[Focal Guidance: Unlocking Controllability from Semantic-Weak Layers in Video Diffusion Models](https://arxiv.org/abs/2601.07287v1)**  
  Authors: Yuanyang Yin, Yufan Deng, Shenghai Yuan, Kaipeng Zhang, Xiao Yang, Feng Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.07287v1.pdf)  
  Keywords: evaluation, diffusion transformer, denoising, benchmark, image-to-video, diffusion model, video diffusion, i2v, dit  
- **[TAGRPO: Boosting GRPO on Image-to-Video Generation with Direct Trajectory Alignment](https://arxiv.org/abs/2601.05729v1)**  
  Authors: Jin Wang, Jianxiang Lu, Guangzheng Xu, Comi Chen, Haoyu Yang, Linqing Wang, Peng Chen, Mingtao Chen, Zhichao Hu, Longhuang Wu, Shuai Shao, Qinglin Lu, Ping Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.05729v1.pdf)  
  Keywords: image-to-video, trajectory, text-to-video, i2v, flow matching, video generation  

### Long Video Generation

*Showing the latest 50 out of 123 papers*

- **[RFDM: Residual Flow Diffusion Model for Efficient Causal Video Editing](https://arxiv.org/abs/2602.06871v1)**  
  Authors: Mohammadreza Salehi, Mehdi Noroozi, Luca Morreale, Ruchika Chavhan, Malcolm Chadwick, Alberto Gil Ramos, Abhinav Mehrotra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06871v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://smsd75.github.io/RFDM_page)  
  Keywords: style, denoising, benchmark, autoregressive, video-to-video, efficient, video editing, diffusion model, dit, video generation  
- **[DiTS: Multimodal Diffusion Transformers Are Time Series Forecasters](https://arxiv.org/abs/2602.06597v1)**  
  Authors: Haoran Zhang, Haixuan Liu, Yong Liu, Yunzhong Qiu, Yuxuan Wang, Jianmin Wang, Mingsheng Long  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06597v1.pdf)  
  Keywords: diffusion transformer, benchmark, autoregressive, architecture, dit, video generation  
- **[From Blurry to Believable: Enhancing Low-quality Talking Heads with 3D Generative Priors](https://arxiv.org/abs/2602.06122v1)**  
  Authors: Ding-Jiun Huang, Yuanhao Wang, Shao-Ji Yuan, Albert Mosella-Montoro, Francisco Vicente Carrasco, Cheng Zhang, Fernando De la Torre  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06122v1.pdf)  
  Keywords: super-resolution, temporal consistency, talking head, identity, dynamics, avatar  
- **[Context Forcing: Consistent Autoregressive Video Generation with Long Context](https://arxiv.org/abs/2602.06028v1)**  
  Authors: Shuo Chen, Cong Wei, Sun Sun, Ping Nie, Kai Zhou, Ge Zhang, Ming-Hsuan Yang, Wenhu Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06028v1.pdf)  
  Keywords: evaluation, streaming, autoregressive, architecture, long video, video generation  
- **[RISE-Video: Can Video Generators Decode Implicit World Rules?](https://arxiv.org/abs/2602.05986v1)**  
  Authors: Mingxin Liu, Shuran Ma, Shibei Meng, Xiangyu Zhao, Zicheng Zhang, Shaofeng Zhang, Zhihang Zhong, Peixian Chen, Haoyu Cao, Xing Sun, Haodong Duan, Xue Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.05986v1.pdf)  
  Keywords: evaluation, benchmark, physical, image-to-video, temporal consistency, dynamics, i2v  
- **[LSA: Localized Semantic Alignment for Enhancing Temporal Consistency in Traffic Video Generation](https://arxiv.org/abs/2602.05966v1)**  
  Authors: Mirlan Karimov, Teodora Spasojevic, Markus Braun, Julian Wiederer, Vasileios Belagiannis, Marc Pollefeys  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.05966v1.pdf)  
  Keywords: evaluation, autonomous driving, controllable, temporal consistency, dit, video generation  
- **[Pathwise Test-Time Correction for Autoregressive Long Video Generation](https://arxiv.org/abs/2602.05871v1)**  
  Authors: Xunzhi Xiang, Zixuan Duan, Guiyu Zhang, Haiyu Zhang, Zhe Gao, Junta Wu, Shaofeng Zhang, Tengfei Wang, Qi Fan, Chunchao Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.05871v1.pdf)  
  Keywords: long video, benchmark, autoregressive, diffusion model, trajectory, video synthesis, video generation  
- **[FlashBlock: Attention Caching for Efficient Long-Context Block Diffusion](https://arxiv.org/abs/2602.05305v2)**  
  Authors: Zhuokun Chen, Jianfei Cai, Bohan Zhuang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.05305v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://caesarhhh.github.io/FlashBlock)  
  Keywords: long-form, long video, efficient, video generation  
- **[Light Forcing: Accelerating Autoregressive Video Diffusion via Sparse Attention](https://arxiv.org/abs/2602.04789v1)**  
  Authors: Chengtao Lv, Yumeng Shi, Yushi Huang, Ruihao Gong, Shen Ren, Wenya Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.04789v1.pdf) | [![GitHub](https://img.shields.io/github/stars/chengtao-lv/LightForcing?style=social)](https://github.com/chengtao-lv/LightForcing)  
  Keywords: autoregressive, efficient, video diffusion, dit, video generation  
- **[InstaDrive: Instance-Aware Driving World Models for Realistic and Consistent Video Generation](https://arxiv.org/abs/2602.03242v1)**  
  Authors: Zhuoran Yang, Xi Guo, Chenjing Ding, Chiyu Wang, Wei Wu, Yanyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03242v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://shanpoyang654.github.io/InstaDrive/page.html)  
  Keywords: evaluation, autonomous driving, world model, temporal consistency, identity, dit, video generation  

### Personalization & Customization

*Showing the latest 50 out of 90 papers*

- **[RFDM: Residual Flow Diffusion Model for Efficient Causal Video Editing](https://arxiv.org/abs/2602.06871v1)**  
  Authors: Mohammadreza Salehi, Mehdi Noroozi, Luca Morreale, Ruchika Chavhan, Malcolm Chadwick, Alberto Gil Ramos, Abhinav Mehrotra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06871v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://smsd75.github.io/RFDM_page)  
  Keywords: style, denoising, benchmark, autoregressive, video-to-video, efficient, video editing, diffusion model, dit, video generation  
- **[From Blurry to Believable: Enhancing Low-quality Talking Heads with 3D Generative Priors](https://arxiv.org/abs/2602.06122v1)**  
  Authors: Ding-Jiun Huang, Yuanhao Wang, Shao-Ji Yuan, Albert Mosella-Montoro, Francisco Vicente Carrasco, Cheng Zhang, Fernando De la Torre  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06122v1.pdf)  
  Keywords: super-resolution, temporal consistency, talking head, identity, dynamics, avatar  
- **[Continuous Control of Editing Models via Adaptive-Origin Guidance](https://arxiv.org/abs/2602.03826v1)**  
  Authors: Alon Wolf, Chen Katzir, Kfir Aberman, Or Patashnik  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03826v1.pdf)  
  Keywords: video manipulation, video editing, dit, identity  
- **[BridgeV2W: Bridging Video Generation Models to Embodied World Models via Embodiment Masks](https://arxiv.org/abs/2602.03793v1)**  
  Authors: Yixiang Chen, Peiyan Li, Jiabing Yang, Keji He, Xiangnan Wu, Yuan Xu, Kai Wang, Jing Liu, Nianfeng Liu, Yan Huang, Liang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03793v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://BridgeV2W.github.io)  
  Keywords: evaluation, style, world model, architecture, dit, robotics, video generation  
- **[InstaDrive: Instance-Aware Driving World Models for Realistic and Consistent Video Generation](https://arxiv.org/abs/2602.03242v1)**  
  Authors: Zhuoran Yang, Xi Guo, Chenjing Ding, Chiyu Wang, Wei Wu, Yanyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03242v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://shanpoyang654.github.io/InstaDrive/page.html)  
  Keywords: evaluation, autonomous driving, world model, temporal consistency, identity, dit, video generation  
- **[ConsisDrive: Identity-Preserving Driving World Models for Video Generation by Instance Mask](https://arxiv.org/abs/2602.03213v2)**  
  Authors: Zhuoran Yang, Yanyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03213v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://shanpoyang654.github.io/ConsisDrive/page.html)  
  Keywords: autonomous driving, world model, temporal consistency, identity, trajectory, video generation  
- **[Quant VideoGen: Auto-Regressive Long Video Generation via 2-Bit KV-Cache Quantization](https://arxiv.org/abs/2602.02958v1)**  
  Authors: Haocheng Xi, Shuo Yang, Yilong Zhao, Muyang Li, Han Cai, Xingyang Li, Yujun Lin, Zhuoyang Zhang, Jintao Zhang, Xiuyu Li, Zhiying Xu, Jun Wu, Chenfeng Xu, Ion Stoica, Song Han, Kurt Keutzer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.02958v1.pdf)  
  Keywords: layout, benchmark, autoregressive, diffusion model, identity, video diffusion, long video, video generation  
- **[Thinking with Comics: Enhancing Multimodal Reasoning through Structured Visual Storytelling](https://arxiv.org/abs/2602.02453v2)**  
  Authors: Andong Chen, Wenxin Zhu, Qiuyu Ding, Yuchen Song, Muyun Yang, Tiejun Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.02453v2.pdf)  
  Keywords: efficient, style  
- **[Unified Personalized Reward Model for Vision Generation](https://arxiv.org/abs/2602.02380v1)**  
  Authors: Yibin Wang, Yuhang Zang, Feng Han, Jiazi Bu, Yujie Zhou, Cheng Jin, Jiaqi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.02380v1.pdf)  
  Keywords: evaluation, video synthesis, style  
- **[MTAVG-Bench: A Comprehensive Benchmark for Evaluating Multi-Talker Dialogue-Centric Audio-Video Generation](https://arxiv.org/abs/2602.00607v1)**  
  Authors: Yang-Hao Zhou, Haitian Li, Rexar Lin, Heyan Huang, Jinxing Zhou, Changsen Yuan, Tian Lan, Ziqin Zhou, Yudong Li, Jiajun Xu, Jingyun Liao, Yi-Ming Cheng, Xuefeng Chen, Xian-Ling Mao, Yousheng Feng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.00607v1.pdf)  
  Keywords: identity, benchmark, evaluation, video generation  

### Physical Understanding

*Showing the latest 50 out of 134 papers*

- **[CineScene: Implicit 3D as Effective Scene Representation for Cinematic Video Generation](https://arxiv.org/abs/2602.06959v1)**  
  Authors: Kaiyi Huang, Yukun Huang, Yu Li, Jianhong Bai, Xintao Wang, Zinan Lin, Xuefei Ning, Jiwen Yu, Pengfei Wan, Yu Wang, Xihui Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06959v1.pdf)  
  Keywords: 3d-aware, physical, text-to-video, trajectory, dit, video synthesis, video generation  
- **[From Blurry to Believable: Enhancing Low-quality Talking Heads with 3D Generative Priors](https://arxiv.org/abs/2602.06122v1)**  
  Authors: Ding-Jiun Huang, Yuanhao Wang, Shao-Ji Yuan, Albert Mosella-Montoro, Francisco Vicente Carrasco, Cheng Zhang, Fernando De la Torre  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06122v1.pdf)  
  Keywords: super-resolution, temporal consistency, talking head, identity, dynamics, avatar  
- **[RISE-Video: Can Video Generators Decode Implicit World Rules?](https://arxiv.org/abs/2602.05986v1)**  
  Authors: Mingxin Liu, Shuran Ma, Shibei Meng, Xiangyu Zhao, Zicheng Zhang, Shaofeng Zhang, Zhihang Zhong, Peixian Chen, Haoyu Cao, Xing Sun, Haodong Duan, Xue Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.05986v1.pdf)  
  Keywords: evaluation, benchmark, physical, image-to-video, temporal consistency, dynamics, i2v  
- **[Stable Velocity: A Variance Perspective on Flow Matching](https://arxiv.org/abs/2602.05435v1)**  
  Authors: Donglin Yang, Yongxing Zhang, Xin Yu, Liang Hou, Xin Tao, Pengfei Wan, Xiaojuan Qi, Renjie Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.05435v1.pdf) | [![GitHub](https://img.shields.io/github/stars/linYDTHU/StableVelocity?style=social)](https://github.com/linYDTHU/StableVelocity)  
  Keywords: acceleration, text-to-video, dynamics, dit, flow matching  
- **[GT-SVJ: Generative-Transformer-Based Self-Supervised Video Judge For Efficient Video Reward Modeling](https://arxiv.org/abs/2602.05202v1)**  
  Authors: Shivanshu Shekhar, Uttaran Bhattacharya, Raghavendra Addanki, Mehrab Tanjim, Somdeb Sarkhel, Tong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.05202v1.pdf)  
  Keywords: evaluation, dynamics, efficient, video generation  
- **[Euphonium: Steering Video Flow Matching via Process Reward Gradient Guided Stochastic Dynamics](https://arxiv.org/abs/2602.04928v2)**  
  Authors: Ruizhe Zhong, Jiesong Lian, Xiaoyue Mi, Zixiang Zhou, Yuan Zhou, Qinglin Lu, Junchi Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.04928v2.pdf) | [![GitHub](https://img.shields.io/github/stars/zerzerzerz/Euphonium?style=social)](https://github.com/zerzerzerz/Euphonium)  
  Keywords: distillation, efficient, text-to-video, dynamics, dit, flow matching, video generation  
- **[WIND: Weather Inverse Diffusion for Zero-Shot Atmospheric Modeling](https://arxiv.org/abs/2602.03924v1)**  
  Authors: Michael Aich, Andreas Fürst, Florian Sestak, Carlos Ruiz-Gonzalez, Niklas Boers, Johannes Brandstetter  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03924v1.pdf)  
  Keywords: physical, efficient, dynamics, diffusion model, video diffusion, dit  
- **[3D-Aware Implicit Motion Control for View-Adaptive Human Video Generation](https://arxiv.org/abs/2602.03796v1)**  
  Authors: Zhixue Fang, Xu He, Songlin Tang, Haoxian Zhang, Qingfeng Li, Xiaoqiang Liu, Pengfei Wan, Kun Gai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03796v1.pdf)  
  Keywords: motion control, human motion, dynamics, camera control, dit, 3d-aware, video generation  
- **[Phaedra: Learning High-Fidelity Discrete Tokenization for the Physical Science](https://arxiv.org/abs/2602.03915v1)**  
  Authors: Levi Lingsch, Georgios Kissas, Johannes Jakubik, Siddhartha Mishra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03915v1.pdf)  
  Keywords: physical, simulation, physical simulation, efficient, dit, video generation  
- **[Grounding Generated Videos in Feasible Plans via World Models](https://arxiv.org/abs/2602.01960v1)**  
  Authors: Christos Ziakas, Amir Bar, Alessandra Russo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.01960v1.pdf)  
  Keywords: simulation, physical, image-to-video, world model, temporal consistency, dynamics, trajectory, dit, action-conditioned  

### Surveys & Benchmarks

*Showing the latest 50 out of 202 papers*

- **[RFDM: Residual Flow Diffusion Model for Efficient Causal Video Editing](https://arxiv.org/abs/2602.06871v1)**  
  Authors: Mohammadreza Salehi, Mehdi Noroozi, Luca Morreale, Ruchika Chavhan, Malcolm Chadwick, Alberto Gil Ramos, Abhinav Mehrotra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06871v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://smsd75.github.io/RFDM_page)  
  Keywords: style, denoising, benchmark, autoregressive, video-to-video, efficient, video editing, diffusion model, dit, video generation  
- **[DiTS: Multimodal Diffusion Transformers Are Time Series Forecasters](https://arxiv.org/abs/2602.06597v1)**  
  Authors: Haoran Zhang, Haixuan Liu, Yong Liu, Yunzhong Qiu, Yuxuan Wang, Jianmin Wang, Mingsheng Long  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06597v1.pdf)  
  Keywords: diffusion transformer, benchmark, autoregressive, architecture, dit, video generation  
- **[Context Forcing: Consistent Autoregressive Video Generation with Long Context](https://arxiv.org/abs/2602.06028v1)**  
  Authors: Shuo Chen, Cong Wei, Sun Sun, Ping Nie, Kai Zhou, Ge Zhang, Ming-Hsuan Yang, Wenhu Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06028v1.pdf)  
  Keywords: evaluation, streaming, autoregressive, architecture, long video, video generation  
- **[RISE-Video: Can Video Generators Decode Implicit World Rules?](https://arxiv.org/abs/2602.05986v1)**  
  Authors: Mingxin Liu, Shuran Ma, Shibei Meng, Xiangyu Zhao, Zicheng Zhang, Shaofeng Zhang, Zhihang Zhong, Peixian Chen, Haoyu Cao, Xing Sun, Haodong Duan, Xue Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.05986v1.pdf)  
  Keywords: evaluation, benchmark, physical, image-to-video, temporal consistency, dynamics, i2v  
- **[LSA: Localized Semantic Alignment for Enhancing Temporal Consistency in Traffic Video Generation](https://arxiv.org/abs/2602.05966v1)**  
  Authors: Mirlan Karimov, Teodora Spasojevic, Markus Braun, Julian Wiederer, Vasileios Belagiannis, Marc Pollefeys  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.05966v1.pdf)  
  Keywords: evaluation, autonomous driving, controllable, temporal consistency, dit, video generation  
- **[Pathwise Test-Time Correction for Autoregressive Long Video Generation](https://arxiv.org/abs/2602.05871v1)**  
  Authors: Xunzhi Xiang, Zixuan Duan, Guiyu Zhang, Haiyu Zhang, Zhe Gao, Junta Wu, Shaofeng Zhang, Tengfei Wang, Qi Fan, Chunchao Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.05871v1.pdf)  
  Keywords: long video, benchmark, autoregressive, diffusion model, trajectory, video synthesis, video generation  
- **[GT-SVJ: Generative-Transformer-Based Self-Supervised Video Judge For Efficient Video Reward Modeling](https://arxiv.org/abs/2602.05202v1)**  
  Authors: Shivanshu Shekhar, Uttaran Bhattacharya, Raghavendra Addanki, Mehrab Tanjim, Somdeb Sarkhel, Tong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.05202v1.pdf)  
  Keywords: evaluation, dynamics, efficient, video generation  
- **[Reinforced Attention Learning](https://arxiv.org/abs/2602.04884v1)**  
  Authors: Bangzheng Li, Jianmo Ni, Chen Qu, Ian Miao, Liu Yang, Xingyu Fu, Muhao Chen, Derek Zhiyuan Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.04884v1.pdf)  
  Keywords: benchmark, distillation  
- **[VTok: A Unified Video Tokenizer with Decoupled Spatial-Temporal Latents](https://arxiv.org/abs/2602.04202v1)**  
  Authors: Feng Wang, Yichun Shi, Ceyuan Yang, Qiushan Guo, Jingxiang Sun, Alan Yuille, Peng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.04202v1.pdf)  
  Keywords: benchmark, text-to-video, evaluation, video generation  
- **[BridgeV2W: Bridging Video Generation Models to Embodied World Models via Embodiment Masks](https://arxiv.org/abs/2602.03793v1)**  
  Authors: Yixiang Chen, Peiyan Li, Jiabing Yang, Keji He, Xiangnan Wu, Yuan Xu, Kai Wang, Jing Liu, Nianfeng Liu, Yan Huang, Liang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03793v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://BridgeV2W.github.io)  
  Keywords: evaluation, style, world model, architecture, dit, robotics, video generation  

### Text-to-Video Generation

*Showing the latest 50 out of 76 papers*

- **[CineScene: Implicit 3D as Effective Scene Representation for Cinematic Video Generation](https://arxiv.org/abs/2602.06959v1)**  
  Authors: Kaiyi Huang, Yukun Huang, Yu Li, Jianhong Bai, Xintao Wang, Zinan Lin, Xuefei Ning, Jiwen Yu, Pengfei Wan, Yu Wang, Xihui Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06959v1.pdf)  
  Keywords: 3d-aware, physical, text-to-video, trajectory, dit, video synthesis, video generation  
- **[Stable Velocity: A Variance Perspective on Flow Matching](https://arxiv.org/abs/2602.05435v1)**  
  Authors: Donglin Yang, Yongxing Zhang, Xin Yu, Liang Hou, Xin Tao, Pengfei Wan, Xiaojuan Qi, Renjie Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.05435v1.pdf) | [![GitHub](https://img.shields.io/github/stars/linYDTHU/StableVelocity?style=social)](https://github.com/linYDTHU/StableVelocity)  
  Keywords: acceleration, text-to-video, dynamics, dit, flow matching  
- **[Euphonium: Steering Video Flow Matching via Process Reward Gradient Guided Stochastic Dynamics](https://arxiv.org/abs/2602.04928v2)**  
  Authors: Ruizhe Zhong, Jiesong Lian, Xiaoyue Mi, Zixiang Zhou, Yuan Zhou, Qinglin Lu, Junchi Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.04928v2.pdf) | [![GitHub](https://img.shields.io/github/stars/zerzerzerz/Euphonium?style=social)](https://github.com/zerzerzerz/Euphonium)  
  Keywords: distillation, efficient, text-to-video, dynamics, dit, flow matching, video generation  
- **[VTok: A Unified Video Tokenizer with Decoupled Spatial-Temporal Latents](https://arxiv.org/abs/2602.04202v1)**  
  Authors: Feng Wang, Yichun Shi, Ceyuan Yang, Qiushan Guo, Jingxiang Sun, Alan Yuille, Peng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.04202v1.pdf)  
  Keywords: benchmark, text-to-video, evaluation, video generation  
- **[RANKVIDEO: Reasoning Reranking for Text-to-Video Retrieval](https://arxiv.org/abs/2602.02444v2)**  
  Authors: Tyler Skow, Alexander Martin, Benjamin Van Durme, Rama Chellappa, Reno Kriz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.02444v2.pdf)  
  Keywords: benchmark, text-to-video, efficient, distillation  
- **[PISCES: Annotation-free Text-to-Video Post-Training via Optimal Transport-Aligned Rewards](https://arxiv.org/abs/2602.01624v1)**  
  Authors: Minh-Quan Le, Gaurav Mittal, Cheng Zhao, David Gu, Dimitris Samaras, Mei Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.01624v1.pdf)  
  Keywords: t2v, text-to-video, temporal consistency, video generation  
- **[Omni-Judge: Can Omni-LLMs Serve as Human-Aligned Judges for Text-Conditioned Audio-Video Generation?](https://arxiv.org/abs/2602.01623v1)**  
  Authors: Susan Liang, Chao Huang, Filippos Bellos, Yolo Yunlong Tang, Qianxiang Shen, Jing Bi, Luchuan Song, Zeliang Zhang, Jason Corso, Chenliang Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.01623v1.pdf)  
  Keywords: evaluation, physical, multi-modal, text-to-video, dit, video generation  
- **[Zero-Shot Video Restoration and Enhancement with Assistance of Video Diffusion Models](https://arxiv.org/abs/2601.21922v1)**  
  Authors: Cong Cao, Huanjing Yue, Shangbin Xie, Xin Liu, Jingyu Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.21922v1.pdf)  
  Keywords: image-to-video, temporal consistency, text-to-video, diffusion model, video diffusion, video restoration  
- **[Generative Recall, Dense Reranking: Learning Multi-View Semantic IDs for Efficient Text-to-Video Retrieval](https://arxiv.org/abs/2601.21193v1)**  
  Authors: Zecheng Zhao, Zhi Chen, Zi Huang, Shazia Sadiq, Tong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.21193v1.pdf)  
  Keywords: benchmark, text-to-video, efficient  
- **[FAIRT2V: Training-Free Debiasing for Text-to-Video Diffusion Models](https://arxiv.org/abs/2601.20791v1)**  
  Authors: Haonan Zhong, Wei Song, Tingxu Han, Maurice Pagnucco, Jingling Xue, Yang Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.20791v1.pdf)  
  Keywords: t2v, evaluation, denoising, text-to-video, diffusion model, identity, video diffusion, video generation  

### Video Editing

- **[RFDM: Residual Flow Diffusion Model for Efficient Causal Video Editing](https://arxiv.org/abs/2602.06871v1)**  
  Authors: Mohammadreza Salehi, Mehdi Noroozi, Luca Morreale, Ruchika Chavhan, Malcolm Chadwick, Alberto Gil Ramos, Abhinav Mehrotra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06871v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://smsd75.github.io/RFDM_page)  
  Keywords: style, denoising, benchmark, autoregressive, video-to-video, efficient, video editing, diffusion model, dit, video generation  
- **[Continuous Control of Editing Models via Adaptive-Origin Guidance](https://arxiv.org/abs/2602.03826v1)**  
  Authors: Alon Wolf, Chen Katzir, Kfir Aberman, Or Patashnik  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03826v1.pdf)  
  Keywords: video manipulation, video editing, dit, identity  
- **[ProxyImg: Towards Highly-Controllable Image Representation via Hierarchical Disentangled Proxy Embedding](https://arxiv.org/abs/2602.01881v1)**  
  Authors: Ye Chen, Yupeng Zhu, Xiongzhen Zhang, Zhewen Wan, Yingzhe Li, Wenjun Zhang, Bingbing Ni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.01881v1.pdf)  
  Keywords: controllable, benchmark, physical, physics, temporal consistency, efficient, video editing, interactive, dynamics, dit  
- **[JUST-DUB-IT: Video Dubbing via Joint Audio-Visual Diffusion](https://arxiv.org/abs/2601.22143v1)**  
  Authors: Anthony Chen, Naomi Ken Korem, Tavi Halperin, Matan Ben Yosef, Urska Jelercic, Ofir Bibi, Or Patashnik, Daniel Cohen-Or  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.22143v1.pdf)  
  Keywords: sound, video-to-video, multi-modal, dynamics, diffusion model, identity, video diffusion, dit  
- **[EditYourself: Audio-Driven Generation and Manipulation of Talking Head Videos with Diffusion Transformers](https://arxiv.org/abs/2601.22127v1)**  
  Authors: John Flynn, Wolfgang Paier, Dimitar Dinev, Sam Nhut Nguyen, Hayk Poghosyan, Manuel Toribio, Sandipan Banerjee, Guy Gafni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.22127v1.pdf)  
  Keywords: human motion, audio-driven, diffusion transformer, video-to-video, diffusion model, talking head, identity, video diffusion, dit  
- **[TeleStyle: Content-Preserving Style Transfer in Images and Videos](https://arxiv.org/abs/2601.20175v1)**  
  Authors: Shiwen Zhang, Xiaoyan Yang, Bojia Zi, Haibin Huang, Chi Zhang, Xuelong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.20175v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Tele-AI/TeleStyle?style=social)](https://github.com/Tele-AI/TeleStyle)  
  Keywords: evaluation, diffusion transformer, video-to-video, temporal consistency, customization, dit, style  
- **[VC-Bench: Pioneering the Video Connecting Benchmark with a Dataset and Evaluation Metrics](https://arxiv.org/abs/2601.19236v1)**  
  Authors: Zhiyu Yin, Zhipeng Liu, Kehai Chen, Lemao Liu, Jin Liu, Hong-Dong Li, Yang Xiang, Min Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.19236v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://anonymous.4open.science/r/VC-Bench-1B67)  
  Keywords: evaluation, benchmark, video editing, dit, video generation  
- **[Beyond Rigid: Benchmarking Non-Rigid Video Editing](https://arxiv.org/abs/2601.18340v1)**  
  Authors: Bingzheng Qu, Kehai Chen, Xuefeng Bai, Jun Yu, Min Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.18340v1.pdf)  
  Keywords: evaluation, denoising, benchmark, physical, physics, temporal consistency, text-driven video, video editing, dynamics, dit, physics-aware  
- **[SkyReels-V3 Technique Report](https://arxiv.org/abs/2601.17323v2)**  
  Authors: Debang Li, Zhengcong Fei, Tuanhui Li, Yikun Dou, Zheng Chen, Jiangping Yang, Mingyuan Fan, Jingtao Xu, Jiahua Wang, Baoxuan Gu, Mingshan Chang, Wenjing Cai, Yuqiang Xie, Binjie Mao, Youqiang Zhang, Nuo Pang, Hao Zhang, Yuzhe Jin, Zhiheng Xu, Dixuan Lin, Guibin Chen, Yahui Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.17323v2.pdf) | [![GitHub](https://img.shields.io/github/stars/SkyworkAI/SkyReels-V3?style=social)](https://github.com/SkyworkAI/SkyReels-V3)  
  Keywords: evaluation, diffusion transformer, video-to-video, temporal consistency, world model, architecture, identity, dit, video synthesis, avatar, video generation  
- **[Memory-V2V: Augmenting Video-to-Video Diffusion Models with Memory](https://arxiv.org/abs/2601.16296v1)**  
  Authors: Dohun Lee, Chun-Hao Paul Huang, Xuelin Chen, Jong Chul Ye, Duygu Ceylan, Hyeonho Jeong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.16296v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://dohunlee1.github.io/MemoryV2V)  
  Keywords: video-to-video, video editing, diffusion model, novel view, video diffusion, dit, long video  

### Video Inpainting & Completion

- **[Learning Physics-Grounded 4D Dynamics with Neural Gaussian Force Fields](https://arxiv.org/abs/2602.00148v1)**  
  Authors: Shiqian Li, Ruihong Shen, Junfeng Ni, Chang Pan, Chi Zhang, Yixin Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.00148v1.pdf)  
  Keywords: evaluation, simulation, physical, physics, world model, interactive, dynamics, video prediction, video generation  
- **[DriveLaW:Unifying Planning and Video Generation in a Latent Driving World](https://arxiv.org/abs/2512.23421v2)**  
  Authors: Tianze Xia, Yongkang Li, Lijun Zhou, Jingfeng Yao, Kaixin Xiong, Haiyang Sun, Bing Wang, Kun Ma, Guang Chen, Hangjun Ye, Wenyu Liu, Xinggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.23421v2.pdf)  
  Keywords: autonomous driving, benchmark, world model, architecture, trajectory, video prediction, video generation  
- **[Autoregressive Flow Matching for Motion Prediction](https://arxiv.org/abs/2512.22688v1)**  
  Authors: Johnathan Xie, Stefan Stojanov, Cristobal Eyzaguirre, Daniel L. K. Yamins, Jiajun Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.22688v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Johnathan-Xie/arfm-motion-prediction?style=social)](https://github.com/Johnathan-Xie/arfm-motion-prediction)  
  Keywords: human motion, benchmark, autoregressive, robotics, dit, video prediction, flow matching, video generation  
- **[Over++: Generative Video Compositing for Layer Interaction Effects](https://arxiv.org/abs/2512.19661v1)**  
  Authors: Luchao Qi, Jiaye Wu, Jun Myeong Choi, Cary Phillips, Roni Sengupta, Dan B Goldman  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.19661v1.pdf)  
  Keywords: dit, video inpainting  
- **[Vidarc: Embodied Video Diffusion Model for Closed-loop Control](https://arxiv.org/abs/2512.17661v1)**  
  Authors: Yao Feng, Chendong Xiang, Xinyi Mao, Hengkai Tan, Zuyue Zhang, Shuhe Huang, Kaiwen Zheng, Haitian Liu, Hang Su, Jun Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.17661v1.pdf)  
  Keywords: physical, autoregressive, dynamics, diffusion model, video diffusion, video prediction  
- **[Flowception: Temporally Expansive Flow Matching for Video Generation](https://arxiv.org/abs/2512.11438v1)**  
  Authors: Tariq Berrada Ifriqi, John Nguyen, Karteek Alahari, Jakob Verbeek, Ricky T. Q. Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.11438v1.pdf)  
  Keywords: video interpolation, denoising, autoregressive, image-to-video, efficient, flow matching, video generation  
- **[Astra: General Interactive World Model with Autoregressive Denoising](https://arxiv.org/abs/2512.08931v3)**  
  Authors: Yixuan Zhu, Jiaqi Feng, Wenzhao Zheng, Yuan Gao, Xin Tao, Pengfei Wan, Jie Zhou, Jiwen Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.08931v3.pdf)  
  Keywords: autonomous driving, streaming, diffusion transformer, denoising, autoregressive, world model, architecture, interactive, camera control, video prediction, video generation  
- **[InverseCrafter: Efficient Video ReCapture as a Latent Domain Inverse Problem](https://arxiv.org/abs/2512.05672v1)**  
  Authors: Yeobin Hong, Suhyeon Lee, Hyungjin Chung, Jong Chul Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.05672v1.pdf) | [![GitHub](https://img.shields.io/github/stars/yeobinhong/InverseCrafter?style=social)](https://github.com/yeobinhong/InverseCrafter)  
  Keywords: video inpainting, controllable, efficient, video diffusion, 4d generation, diffusion model, novel view, camera control, dit, video generation  
- **[Beyond Boundary Frames: Audio-Visual Semantic Guidance for Context-Aware Video Interpolation](https://arxiv.org/abs/2512.03590v1)**  
  Authors: Yuchen Deng, Xiuyang Wu, Hai-Tao Zheng, Jie Wang, Feidiao Yang, Yuxing Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.03590v1.pdf)  
  Keywords: dit, frame interpolation, video interpolation  
- **[LoVoRA: Text-guided and Mask-free Video Object Removal and Addition with Learnable Object-aware Localization](https://arxiv.org/abs/2512.02933v2)**  
  Authors: Zhihan Xiao, Lin Liu, Yixin Gao, Xiaopeng Zhang, Haoxuan Che, Songping Mai, Qi Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02933v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://cz-5f.github.io/LoVoRA.github.io)  
  Keywords: evaluation, video translation, video inpainting, image-to-video, temporal consistency, video editing, dit  

### Video Super-Resolution & Enhancement

*Showing the latest 50 out of 61 papers*

- **[RFDM: Residual Flow Diffusion Model for Efficient Causal Video Editing](https://arxiv.org/abs/2602.06871v1)**  
  Authors: Mohammadreza Salehi, Mehdi Noroozi, Luca Morreale, Ruchika Chavhan, Malcolm Chadwick, Alberto Gil Ramos, Abhinav Mehrotra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06871v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://smsd75.github.io/RFDM_page)  
  Keywords: style, denoising, benchmark, autoregressive, video-to-video, efficient, video editing, diffusion model, dit, video generation  
- **[From Blurry to Believable: Enhancing Low-quality Talking Heads with 3D Generative Priors](https://arxiv.org/abs/2602.06122v1)**  
  Authors: Ding-Jiun Huang, Yuanhao Wang, Shao-Ji Yuan, Albert Mosella-Montoro, Francisco Vicente Carrasco, Cheng Zhang, Fernando De la Torre  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06122v1.pdf)  
  Keywords: super-resolution, temporal consistency, talking head, identity, dynamics, avatar  
- **[Tiled Prompts: Overcoming Prompt Underspecification in Image and Video Super-Resolution](https://arxiv.org/abs/2602.03342v1)**  
  Authors: Bryan Sangwoo Kim, Jonghyun Park, Jong Chul Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03342v1.pdf)  
  Keywords: super-resolution, dit, diffusion model  
- **[GPD: Guided Progressive Distillation for Fast and High-Quality Video Generation](https://arxiv.org/abs/2602.01814v1)**  
  Authors: Xiao Liang, Yunzhu Zhang, Linchao Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.01814v1.pdf)  
  Keywords: distillation, denoising, diffusion model, dynamics, video generation  
- **[FlowCast: Trajectory Forecasting for Scalable Zero-Cost Speculative Flow Matching](https://arxiv.org/abs/2602.01329v1)**  
  Authors: Divya Jyoti Bajpai, Shubham Agarwal, Apoorv Saxena, Kuldeep Kulkarni, Subrata Mitra, Manjesh Kumar Hanawal  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.01329v1.pdf)  
  Keywords: evaluation, distillation, denoising, acceleration, interactive, trajectory, dit, flow matching, video generation  
- **[VideoGPA: Distilling Geometry Priors for 3D-Consistent Video Generation](https://arxiv.org/abs/2601.23286v1)**  
  Authors: Hongyang Du, Junjie Ye, Xiaoyan Cong, Runhao Li, Jingcheng Ni, Aman Agarwal, Zeqi Zhou, Zekun Li, Randall Balestriero, Yue Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.23286v1.pdf)  
  Keywords: denoising, physical, efficient, diffusion model, video diffusion, video generation  
- **[Zero-Shot Video Restoration and Enhancement with Assistance of Video Diffusion Models](https://arxiv.org/abs/2601.21922v1)**  
  Authors: Cong Cao, Huanjing Yue, Shangbin Xie, Xin Liu, Jingyu Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.21922v1.pdf)  
  Keywords: image-to-video, temporal consistency, text-to-video, diffusion model, video diffusion, video restoration  
- **[FAIRT2V: Training-Free Debiasing for Text-to-Video Diffusion Models](https://arxiv.org/abs/2601.20791v1)**  
  Authors: Haonan Zhong, Wei Song, Tingxu Han, Maurice Pagnucco, Jingling Xue, Yang Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.20791v1.pdf)  
  Keywords: t2v, evaluation, denoising, text-to-video, diffusion model, identity, video diffusion, video generation  
- **[Efficient Autoregressive Video Diffusion with Dummy Head](https://arxiv.org/abs/2601.20499v1)**  
  Authors: Hang Guo, Zhaoyang Jia, Jiahao Li, Bin Li, Yuanhao Cai, Jiangshan Wang, Yawei Li, Yan Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.20499v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://csguoh.github.io/project/DummyForcing)  
  Keywords: denoising, autoregressive, efficient, diffusion model, video diffusion, dit, video generation  
- **[Self-Refining Video Sampling](https://arxiv.org/abs/2601.18577v1)**  
  Authors: Sangwon Jang, Taekyung Ki, Jaehyeong Jo, Saining Xie, Jaehong Yoon, Sung Ju Hwang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.18577v1.pdf)  
  Keywords: denoising, physical, physics, dynamics, dit  

### World Models & Simulation

*Showing the latest 50 out of 100 papers*

- **[Driving with DINO: Vision Foundation Features as a Unified Bridge for Sim-to-Real Generation in Autonomous Driving](https://arxiv.org/abs/2602.06159v1)**  
  Authors: Xuyang Chen, Conglang Zhang, Chuanheng Fu, Zihao Yang, Kaixuan Zhou, Yizhi Zhang, Jianan He, Yanfeng Zhang, Mingwei Sun, Zengmao Wang, Zhen Dong, Xiaoxiao Long, Liqiu Meng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06159v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://albertchen98.github.io/DwD-project)  
  Keywords: autonomous driving, controllable, simulation, video diffusion, video generation  
- **[BridgeV2W: Bridging Video Generation Models to Embodied World Models via Embodiment Masks](https://arxiv.org/abs/2602.03793v1)**  
  Authors: Yixiang Chen, Peiyan Li, Jiabing Yang, Keji He, Xiangnan Wu, Yuan Xu, Kai Wang, Jing Liu, Nianfeng Liu, Yan Huang, Liang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03793v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://BridgeV2W.github.io)  
  Keywords: evaluation, style, world model, architecture, dit, robotics, video generation  
- **[Phaedra: Learning High-Fidelity Discrete Tokenization for the Physical Science](https://arxiv.org/abs/2602.03915v1)**  
  Authors: Levi Lingsch, Georgios Kissas, Johannes Jakubik, Siddhartha Mishra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03915v1.pdf)  
  Keywords: physical, simulation, physical simulation, efficient, dit, video generation  
- **[InstaDrive: Instance-Aware Driving World Models for Realistic and Consistent Video Generation](https://arxiv.org/abs/2602.03242v1)**  
  Authors: Zhuoran Yang, Xi Guo, Chenjing Ding, Chiyu Wang, Wei Wu, Yanyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03242v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://shanpoyang654.github.io/InstaDrive/page.html)  
  Keywords: evaluation, autonomous driving, world model, temporal consistency, identity, dit, video generation  
- **[ConsisDrive: Identity-Preserving Driving World Models for Video Generation by Instance Mask](https://arxiv.org/abs/2602.03213v2)**  
  Authors: Zhuoran Yang, Yanyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03213v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://shanpoyang654.github.io/ConsisDrive/page.html)  
  Keywords: autonomous driving, world model, temporal consistency, identity, trajectory, video generation  
- **[Causal Forcing: Autoregressive Diffusion Distillation Done Right for High-Quality Real-Time Interactive Video Generation](https://arxiv.org/abs/2602.02214v2)**  
  Authors: Hongzhou Zhu, Min Zhao, Guande He, Hang Su, Chongxuan Li, Jun Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.02214v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://thu-ml.github.io/CausalForcing.github.io)  
  Keywords: distillation, autoregressive, interactive, diffusion model, video diffusion, dit, video generation  
- **[Grounding Generated Videos in Feasible Plans via World Models](https://arxiv.org/abs/2602.01960v1)**  
  Authors: Christos Ziakas, Amir Bar, Alessandra Russo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.01960v1.pdf)  
  Keywords: simulation, physical, image-to-video, world model, temporal consistency, dynamics, trajectory, dit, action-conditioned  
- **[ProxyImg: Towards Highly-Controllable Image Representation via Hierarchical Disentangled Proxy Embedding](https://arxiv.org/abs/2602.01881v1)**  
  Authors: Ye Chen, Yupeng Zhu, Xiongzhen Zhang, Zhewen Wan, Yingzhe Li, Wenjun Zhang, Bingbing Ni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.01881v1.pdf)  
  Keywords: controllable, benchmark, physical, physics, temporal consistency, efficient, video editing, interactive, dynamics, dit  
- **[Fast Autoregressive Video Diffusion and World Models with Temporal Cache Compression and Sparse Attention](https://arxiv.org/abs/2602.01801v1)**  
  Authors: Dvir Samuel, Issar Tzachor, Matan Levy, Micahel Green, Gal Chechik, Rami Ben-Ari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.01801v1.pdf)  
  Keywords: long-form, streaming, autoregressive, world model, diffusion model, interactive, video diffusion  
- **[FastPhysGS: Accelerating Physics-based Dynamic 3DGS Simulation via Interior Completion and Adaptive Optimization](https://arxiv.org/abs/2602.01723v1)**  
  Authors: Yikun Ma, Yiqing Li, Jingwen Ye, Zhongkai Wu, Weidong Zhang, Lin Gao, Zhi Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.01723v1.pdf)  
  Keywords: simulation, physical, physical simulation, physics, efficient, dynamics, diffusion model, video diffusion, dit  



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
