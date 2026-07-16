# Awesome Video Diffusions [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Video Diffusion Models and Video Generation. Content is automatically updated daily.

> Last Update: 2026-07-16 08:12:04

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

- [3D-aware Video Generation](#3d-aware-video-generation) (84 papers) - Video generation with 3D awareness, multi-view consistency, and 4D content creation
- [Applications](#applications) (176 papers) - Domain-specific applications of video diffusion models
- [Architecture & Efficiency](#architecture-&-efficiency) (1254 papers) - Architectural innovations (DiT, UNet), flow matching, and training/inference efficiency
- [Audio & Multi-modal](#audio-&-multi-modal) (109 papers) - Audio-driven and multi-modal conditioned video generation
- [Controllable Generation](#controllable-generation) (449 papers) - Controllable video generation with motion, camera, pose, or layout guidance
- [Human & Character Animation](#human-&-character-animation) (94 papers) - Human-centric video generation including talking heads, dance, and character animation
- [Image-to-Video Generation](#image-to-video-generation) (150 papers) - Methods for animating still images into videos
- [Long Video Generation](#long-video-generation) (420 papers) - Generating temporally consistent long-form videos beyond short clips
- [Personalization & Customization](#personalization-&-customization) (303 papers) - Personalized video generation with custom subjects, identities, or styles
- [Physical Understanding](#physical-understanding) (502 papers) - Physics-aware video generation and dynamics modeling
- [Surveys & Benchmarks](#surveys-&-benchmarks) (746 papers) - Survey papers, benchmarks, and evaluation metrics for video generation
- [Text-to-Video Generation](#text-to-video-generation) (228 papers) - Foundation models and methods for generating videos from text prompts
- [Video Editing](#video-editing) (113 papers) - Diffusion-based video editing, style transfer, and manipulation
- [Video Inpainting & Completion](#video-inpainting-&-completion) (30 papers) - Video inpainting, completion, outpainting, and temporal prediction
- [Video Super-Resolution & Enhancement](#video-super-resolution-&-enhancement) (226 papers) - Video quality improvement, upscaling, restoration, and frame interpolation
- [World Models & Simulation](#world-models-&-simulation) (381 papers) - Video generation as world simulators and interactive environment generation



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3D-aware Video Generation

*Showing the latest 50 out of 84 papers*

- **[Delving into the Temporal Challenges of Unified Video Protection Against Image-to-Video and Fine-Tuning-based Customization](https://arxiv.org/abs/2607.13336v1)**  
  Authors: Yuxin Huang, Ziming Hong, Mingming Gong, Wanyu Wang, Jing Zhang, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.13336v1.pdf)  
  Keywords: 3d video, customization, diffusion model, dit, identity, image-to-video, video diffusion, video generation  
- **[4D Human-Scene Reconstruction from Low-Overlap Captures](https://arxiv.org/abs/2607.09125v1)**  
  Authors: Minhyuk Hwang, Sangmin Kim, Seunguk Do, Daneul Kim, Jaesik Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.09125v1.pdf)  
  Keywords: diffusion model, identity, novel view, trajectory, video diffusion  
- **[SoccerNet 2026 Challenges Results](https://arxiv.org/abs/2607.07320v1)**  
  Authors: Anthony Cioppa, Silvio Giancola, Håkan Ardö, Mohamad Dalal, Jan Held, Jérémie Ochin, Jiayuan Rao, Karen Sanchez, Renaud Vandeghen, Artur Xarles, Olivier Barnich, Albert Clapés, Mathieu Delvaux, Sergio Escalera, Bernard Ghanem, Cédric Hons, Antoine Houet, Sotiris Manitsaris, Tom Michel, Pierre Miralles, Thomas B. Moeslund, Mikael Nilsson, Bogdan Stanciulescu, Marc Van Droogenbroeck, Yanfeng Wang, Weidi Xie, Faisal Altawijri, Mohamed Atef, Semen Budennyy, Vasiliy Chelpanov, Puhua Chen, Yixin Chen, Lechao Cheng, Jianling Chu, Ju-Seong Do, Oleg Durygin, Omar Fetouh, Mirco Fuchs, Youssef Ghallab, Falguni Ghosh, Wonjun Heo, Yufeng Hu, Weixuan Huang, Phuong-Linh Huynh-Ha, Matvey Isupov, Yangguang Ji, Siyuan Jiang, Zhenxiang Jiang, Wonyong Jo, Ho-Young Jung, SeongHeon Kang, MinJae Kim, Youngseon Kim, Jakub Komosa, Artem Konshin, Trung-Hoang Le, Jongmin Lee, Lingling Li, Litao Li, Vadim Linkov, Fang Liu, Haoxuan Ma, Shun Makino, Ismail Mathkour, Konstantin Mitin, Mikhail Moiseev, Takumi Nagaya, Yuki Nakamura, Thanh-Khoi Nguyen, Hoang-Phuc Nguyen, Trong-Thuan Nguyen, Christian Orduz, Kwanyong Park, Fabian Perez, Parthsarthi Rawat, SuHyun Rim, Hoover Rueda-Chacón, Atom Scott, Minori Sugimura, Yuyang Sun, Shengeng Tang, Minh-Triet Tran, Ikuma Uchida, Juan Vanegas, Thanh-Nhan Vo, Jiangtao Wang, Yaxiong Wang, Xiaogang Wang, Ruifeng Wang, Rio Watanabe, Jiali Wen, Yongliang Wu, Di Yang, Xu Yang, Zhuo Yang, Xinyu Ye, Yibo Yu, Zihan Zhai, Yu Zhang, Zhenyu Zhao, Zhun Zhong, Yixi Zhou, Xingyu Zhu, Wenbo Zhu, Julian Ziegler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.07320v1.pdf)  
  Keywords: benchmark, dit, evaluation, novel view  
- **[MV-Forcing: Long Multi-View Video Generation via 4D-Grounded Spatio-Temporal Self-Forcing](https://arxiv.org/abs/2607.05376v1)**  
  Authors: Gal Fiebelman, Hadar Averbuch-Elor, Sagie Benaim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.05376v1.pdf)  
  Keywords: autoregressive, denoising, diffusion model, distillation, multi-view video, video diffusion, video generation  
- **[HandsOnWorld: Unconstrained Egocentric Video Generation with Camera-Disentangled Hand Control](https://arxiv.org/abs/2607.02075v1)**  
  Authors: Yushuo Chen, Xiaoyu Shi, Xiaoshi Wu, Xintao Wang, Pengfei Wan, Yebin Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.02075v1.pdf)  
  Keywords: 3d-aware, video generation  
- **[NeoMap: Training-free Novel-View Synthesis from Single Images and Videos](https://arxiv.org/abs/2607.01962v1)**  
  Authors: Jinxi Li, Tianyi Zhang, Yafei Yang, Zihui Zhang, Peng Huang, Koon Wing Macgyver Lin, Bo Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.01962v1.pdf)  
  Keywords: benchmark, denoising, dit, novel view, video synthesis  
- **[RayPE: Ray-Space Positional Encoding for 3D-Aware Video Generation](https://arxiv.org/abs/2606.27345v2)**  
  Authors: Minghao Yin, Jiahao Lu, Wenbo Hu, Wang Zhao, Shan Ying, Kai Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.27345v2.pdf)  
  Keywords: 3d-aware, camera control, diffusion transformer, dit, identity, video diffusion, video generation  
- **[Follow Your Track: Precise Skeleton Animation Controlled by 3D Trajectories](https://arxiv.org/abs/2606.25344v1)**  
  Authors: Yueting Liu, Yanqin Jiang, Nian Liu, Jingmen Zhou, Zhengjun Zha, Weiming Hu, Jin Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.25344v1.pdf)  
  Keywords: 4d generation, body motion, dit, efficient, temporal consistency, trajectory  
- **[OmniDrive: An LLM-Choreographed Multi-Agent World Model with Unified Latent Co-Compression for Multi-View Driving Video Generation](https://arxiv.org/abs/2606.17536v1)**  
  Authors: Zijie Meng, Yufei Liu, Chengqian Ma, Zhiyu Li, Jiyuan Liu, Wenhua Nie, Bingcai Wei, Shuqin Chen, Weichen Xu, Jiquan Yuan, Miao Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.17536v1.pdf)  
  Keywords: autonomous driving, controllable, dit, layout, multi-view video, video generation, world model  
- **[R2RDreamer: 3D-aware Data Augmentation for Spatially-generalized 2D Manipulation Policies](https://arxiv.org/abs/2606.17040v1)**  
  Authors: Xiuwei Xu, Haowen Sun, Angyuan Ma, Yiwei Zhang, Zhenyu Wu, Xiaofeng Wang, Bingyao Yu, Zheng Zhu, Jie Zhou, Jiwen Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.17040v1.pdf)  
  Keywords: 3d-aware, controllable, dit, image-to-video, simulation, style, video completion  

### Applications

*Showing the latest 50 out of 176 papers*

- **[Cyclone: Diffusion Model for Cycle-Consistent Weather Editing from Unpaired Driving Data](https://arxiv.org/abs/2607.13927v1)**  
  Authors: Thang-Anh-Quan Nguyen, Moussab Bennehar, Luis Guillermo Roldao Jimenez, Nathan Piasco, Dzmitry Tsishkou, Laurent Caraffa, Jean-Philippe Tarel, Roland Brémond  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.13927v1.pdf)  
  Keywords: autonomous driving, diffusion model, dit, physics, video diffusion  
- **[ABot-3DWorld 0: A Universal World Model to Explore Any 3D Space](https://arxiv.org/abs/2607.11673v2)**  
  Authors: Mingchao Sun, Luyang Tang, Yu Liu, Xu Yan, Zhan Li, Yunwei Zhang, Fei Yu, Zengye Ge, Yumin Liu, Jiacheng Zhang, Yongchang Zhang, Jiawei Zhang, Zhicheng Liu, Zhongxu Sun, Tianjian Ouyang, Wenzheng Chen, Shixing Yang, Nianfei Fan, Guodong Sun, Huan Li, Zheng Zhou, Yongze Li, Yingliang Peng, Mengmeng Du, Yuan Liu, Haozhe Shi, Chunnuo Gong, Chengzhen Yu, Chunxue Jia, Yang Liu, Shiying Zeng, Junnan Lai, Hang Zhang, Ning Guo, Baoquan Chen, Mu Xu, Hongyu Pan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.11673v2.pdf)  
  Keywords: creative, efficient, trajectory, world model  
- **[Xiaomi-Robotics-U0: Unified Embodied Synthesis with World Foundation Model](https://arxiv.org/abs/2607.11643v1)**  
  Authors: Xinghang Li, Jun Guo, Qiwei Li, Long Qian, Hang Lai, Yueze Wang, Hongyu Yan, Jiahang Cao, Xi Chen, Jingen Qu, Jiaxi Song, Nan Sun, Hanye Zhao, Futeng Liu, Wanli Peng, Heyun Wang, Yunhong Wang, Caoyu Xia, Jack Zhao, Diyun Xiang, Hangjun Ye, Heng Qu, Huaping Liu, Jason Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.11643v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://robotics.xiaomi.com/xiaomi-robotics-u0.html)  
  Keywords: autoregressive, controllable, dit, dynamics, evaluation, robotics, video generation, world model  
- **[Validate the Dream Before You Trust Its Verdict: Admissibility for World-Model Simulators](https://arxiv.org/abs/2607.07196v1)**  
  Authors: Christian Oefinger, Finn Rasmus Schäfer, Korbinian Moller, Mattia Piccinini, Johannes Betz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.07196v1.pdf)  
  Keywords: autonomous driving, dit, robotics, simulation, world model  
- **[Point as Skeleton: Accumulated Point Cloud Enhanced Autoregressive Generation for Closed-Loop Autonomous Driving Simulation](https://arxiv.org/abs/2607.06516v1)**  
  Authors: Songbur Wong, Xiaosong Jia, Junqi You, Bo Zhang, Pei Xu, Renqiu Xia, Yuping Qiu, Shaofeng Zhang, Zelin Zhao, Xuechao Yan, Yuchen Zhou, Yurui Chen, Wen Guo, Hang Xu, Junchi Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.06516v1.pdf) | [![GitHub](https://img.shields.io/github/stars/krauwu/point-as-skeleton?style=social)](https://github.com/krauwu/point-as-skeleton)  
  Keywords: autonomous driving, autoregressive, dit, simulation, video generation  
- **[A Definition and Roadmap for World Models](https://arxiv.org/abs/2607.06401v1)**  
  Authors: Xinyuan Chen, Haoyu Guo, Shi Guo, Bingqi Jiang, Chunhua Shen, Xing Shen, Tianfan Xue, Yufei Xue, Mulin Yu, Weinan Zhang, Bin Zhao, Bowen Zhou, Ming Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.06401v1.pdf)  
  Keywords: concept, dynamics, physical, robotics, video generation, world model  
- **[Benchmarking the Robustness of Autonomous Driving to Environmental Illusions: A Lane Perception Perspective](https://arxiv.org/abs/2607.05783v1)**  
  Authors: Tianyuan Zhang, Xianglong Liu, Aishan Liu, Lu Wang, Yitong Zhang, Peng Yue, Mingchuan Zhang, Siyuan Liang, Dacheng Tao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.05783v1.pdf)  
  Keywords: autonomous driving, benchmark, controllable, dit, evaluation, simulation  
- **[SpheRoPE: Zero-Shot Optimization-Free 360 Panorama Generation with Spherical RoPE](https://arxiv.org/abs/2606.32033v1)**  
  Authors: Or Hirschorn, Aaron Olender, Eli Alshan, Ianir Ideses, Lior Fritz, Sagie Benaim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.32033v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://orhir.github.io/SpheRoPE)  
  Keywords: creative, diffusion transformer  
- **[World Narrative Model for Highly Controllable Video Generation: A Paradigm Shift from Pixel Sampling to Physical World Orchestration](https://arxiv.org/abs/2606.31946v2)**  
  Authors: Ye Chen, Xuanhong Chen, Yupeng Zhu, Liming Tan, Zhewen Wan, Yuxuan Xiong, Tielong Wang, Jinfan Liu, Wuze Zhang, Xiongzhen Zhang, Feifei Li, Xianglin Luo, Zhehan Zhao, Zhifan Zhang, Laisheng Kou, Zhujin Liang, Yugang Chen, Muchun Chen, Xu Miao, Yijing Zhang, Xiaojie Sheng, Qiang Hu, Jialiang Chen, Weimin Zhang, Wenjun Zhang, Bingbing Ni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.31946v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://glassroom.sjtu.edu.cn/WNM)  
  Keywords: controllable, dit, efficient, film, layout, physical, video generation  
- **[InfiniVerse: Occupancy Guided Unbounded Scene Generation for Autonomous Driving](https://arxiv.org/abs/2606.31109v1)**  
  Authors: Xiaoyu Ye, Leheng Li, Xinyu Ji, Yingjie Cai, Hongda He, Xu Yan, Guanyi Zhao, Ying-Cong Chen, Bingbing Liu, Shuguang Cui, Zhen Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.31109v1.pdf)  
  Keywords: autonomous driving, autoregressive, benchmark, controllable, diffusion model, dit, evaluation, video diffusion  

### Architecture & Efficiency

*Showing the latest 50 out of 1254 papers*

- **[VideoRAE: Taming Video Foundation Models for Generative Modeling via Representation Autoencoders](https://arxiv.org/abs/2607.14088v1)**  
  Authors: Zhihao Xie, Junfeng Wu, Xinting Hu, Junchao Huang, Li Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.14088v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zhxie0117.github.io/VideoRAE)  
  Keywords: autoregressive, diffusion transformer, dit, text-to-video  
- **[From Pixels to States: Rethinking Interactive World Models as Game Engines](https://arxiv.org/abs/2607.14076v1)**  
  Authors: Zhen Li, Zian Meng, Shuwei Shi, Mingliang Zhai, Jiaming Tan, Chuanhao Li, Kaipeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.14076v1.pdf)  
  Keywords: dit, dynamics, interactive, world model  
- **[Cyclone: Diffusion Model for Cycle-Consistent Weather Editing from Unpaired Driving Data](https://arxiv.org/abs/2607.13927v1)**  
  Authors: Thang-Anh-Quan Nguyen, Moussab Bennehar, Luis Guillermo Roldao Jimenez, Nathan Piasco, Dzmitry Tsishkou, Laurent Caraffa, Jean-Philippe Tarel, Roland Brémond  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.13927v1.pdf)  
  Keywords: autonomous driving, diffusion model, dit, physics, video diffusion  
- **[Kaleido: Algorithm-Hardware Co-Design for Video Diffusion Transformers by Exploiting Latent Space Correlations](https://arxiv.org/abs/2607.13770v1)**  
  Authors: Wenxuan Miao, Haosong Liu, Weiming Hu, Zihan Liu, Aiyue Chen, Jianlin Yu, Yiwu Yao, Yiming Gan, Jieru Zhao, Jingwen Leng, Minyi Guo, Yu Feng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.13770v1.pdf)  
  Keywords: acceleration, diffusion transformer, dit, efficient, evaluation, video diffusion  
- **[VGIF-Score: Interpretable and Diagnostic Evaluation of Spatio-Temporal Instruction Following in Video Generation](https://arxiv.org/abs/2607.13527v1)**  
  Authors: Songyu Xu, Xin Wang, Qiang Chen, Xinran Wang, Muxi Diao, Yuxuan Zhang, Kongming Liang, Rui Lin, Zhanyu Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.13527v1.pdf) | [![GitHub](https://img.shields.io/github/stars/PRIS-CV/VGIF-SCORE?style=social)](https://github.com/PRIS-CV/VGIF-SCORE)  
  Keywords: benchmark, dit, evaluation, physics, video generation  
- **[Bring Music The Horizon: Music-Driven 360$^\circ$ Video Generation](https://arxiv.org/abs/2607.13471v1)**  
  Authors: Kai Hsu Tsai, Yong Wei Fu, Hung I Yang, Yu-Chih Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.13471v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://etoile-et-toi-mp3.github.io/BMTH_Project_Page)  
  Keywords: dit, dynamics, image-to-video, music video, sound, trajectory, video generation  
- **[Delving into the Temporal Challenges of Unified Video Protection Against Image-to-Video and Fine-Tuning-based Customization](https://arxiv.org/abs/2607.13336v1)**  
  Authors: Yuxin Huang, Ziming Hong, Mingming Gong, Wanyu Wang, Jing Zhang, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.13336v1.pdf)  
  Keywords: 3d video, customization, diffusion model, dit, identity, image-to-video, video diffusion, video generation  
- **[Continuously Evolving Deepfake Detection: An Architecture and Public-Benchmark Evaluation of a Dynamic Detection System](https://arxiv.org/abs/2607.13234v1)**  
  Authors: Ken Jon Miyachi, Dylan Uys  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.13234v1.pdf)  
  Keywords: architecture, benchmark, dit, evaluation  
- **[Text2Sign: A Single-GPU Diffusion Baseline for Text-to-Sign Language Video Generation](https://arxiv.org/abs/2607.13164v1)**  
  Authors: Ruize Xia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.13164v1.pdf) | [![GitHub](https://img.shields.io/github/stars/xiaruize0911/text2sign?style=social)](https://github.com/xiaruize0911/text2sign)  
  Keywords: denoising, diffusion model, dit, evaluation, style, temporal consistency, video diffusion, video generation  
- **[ACID: Adaptive Caching for vIDeo generation](https://arxiv.org/abs/2607.12358v1)**  
  Authors: Om Agrawal, Saurabh Agarwal, Aditya Akella  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.12358v1.pdf)  
  Keywords: acceleration, denoising, diffusion model, dit, evaluation, video diffusion, video generation  

### Audio & Multi-modal

*Showing the latest 50 out of 109 papers*

- **[Bring Music The Horizon: Music-Driven 360$^\circ$ Video Generation](https://arxiv.org/abs/2607.13471v1)**  
  Authors: Kai Hsu Tsai, Yong Wei Fu, Hung I Yang, Yu-Chih Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.13471v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://etoile-et-toi-mp3.github.io/BMTH_Project_Page)  
  Keywords: dit, dynamics, image-to-video, music video, sound, trajectory, video generation  
- **[HumanForge: A Human-Centric Deepfake Video Benchmark with Multi-Agent Forgery Rationales](https://arxiv.org/abs/2607.08705v1)**  
  Authors: Wenbo Xu, Zhimin Chen, Xiaojie Liang, Hengrui Liu, Wei Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.08705v1.pdf)  
  Keywords: benchmark, diffusion model, dit, multi-modal, text-to-video, video diffusion, video synthesis  
- **[AVTok: 1D Unified Tokenization for Holistic Audio-Video Generation](https://arxiv.org/abs/2606.30811v1)**  
  Authors: Kien T. Pham, I Chieh Chen, Qifeng Chen, Long Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30811v1.pdf)  
  Keywords: architecture, audio-to-video, dit, efficient, sound, video generation  
- **[TRUST: Efficient Abdominal Trauma Recognition via Image-to-Ultrasound-Video Transfer Learning](https://arxiv.org/abs/2606.27777v1)**  
  Authors: Enguang Wang, Hao Zhou, Shuo Gao, Tuo Liu, Guangquan Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.27777v1.pdf)  
  Keywords: dit, dynamics, efficient, image-to-video, sound  
- **[PhyEditBench: A Real-World Multi-Stage Benchmark for Physics-Aware Image Editing](https://arxiv.org/abs/2606.26551v2)**  
  Authors: Shengbin Guo, Shaokang He, Chaoyue Meng, Shengpeng Xiao, Xunzhi Xiang, Shaofeng Zhang, Qi Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.26551v2.pdf) | [![GitHub](https://img.shields.io/github/stars/Previsior/PhyEditBench?style=social)](https://github.com/Previsior/PhyEditBench)  
  Keywords: benchmark, dit, dynamics, evaluation, multi-modal, physical, physics, physics-aware, video generation  
- **[Wan-Streamer v0.1: End-to-end Real-time Interactive Foundation Models](https://arxiv.org/abs/2606.25041v3)**  
  Authors: Lianghua Huang, Zhi-Fan Wu, Wei Wang, Yupeng Shi, Mengyang Feng, Junjie He, Chen-Wei Xie, Yu Liu, Jingren Zhou, Ang Wang, Bang Zhang, Baole Ai, Chen Liang, Cheng Yu, Chongyang Zhong, Jinwei Qi, Kai Zhu, Pandeng Li, Peng Zhang, Wenyuan Zhang, Xinhua Cheng, Yitong Huang, Yun Zheng, Yuzheng Wang, Zoubin Bi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.25041v3.pdf)  
  Keywords: audio-driven, avatar, interactive, streaming  
- **[InteractiveAvatar: Real-Time Streaming Video Generation for Consistent and Intent-Aware Avatars](https://arxiv.org/abs/2606.22905v2)**  
  Authors: Quanyue Song, Yishan He, Yanfei Zhang, Shihao Cheng, Zhixiang He, Zhizhi Guo, Chi Zhang, Xuelong Li, Caigui Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.22905v2.pdf)  
  Keywords: audio-driven, autoregressive, avatar, distillation, interactive, streaming, temporal consistency, video generation  
- **[T-MOR: Learning Motion-Aware Skeleton Representations for Human Action Recognition](https://arxiv.org/abs/2606.21607v1)**  
  Authors: Di Yang, Mahmoud Ali, Quan Kong, Gianpiero Francesca, Francois Bremond  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.21607v1.pdf)  
  Keywords: benchmark, dit, human motion, multi-modal, physical  
- **[PermaVid: Consistent Video Generation Across Edits via Disentangled Context Memory](https://arxiv.org/abs/2606.16449v2)**  
  Authors: Shuai Yang, Bingjie Gao, Ziwei Liu, Jiaqi Wang, Dahua Lin, Tong Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.16449v2.pdf)  
  Keywords: dit, layout, multi-modal, video generation  
- **[ReFree: Towards Realistic Co-Speech Video Generation via Reward-Free RL and Multilevel Speech Guidance](https://arxiv.org/abs/2606.13304v1)**  
  Authors: Salaheldin Mohamed, M. Hamza Mughal, Rishabh Dabral, Christian Theobalt  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.13304v1.pdf)  
  Keywords: evaluation, speech-driven, video generation  

### Controllable Generation

*Showing the latest 50 out of 449 papers*

- **[Bring Music The Horizon: Music-Driven 360$^\circ$ Video Generation](https://arxiv.org/abs/2607.13471v1)**  
  Authors: Kai Hsu Tsai, Yong Wei Fu, Hung I Yang, Yu-Chih Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.13471v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://etoile-et-toi-mp3.github.io/BMTH_Project_Page)  
  Keywords: dit, dynamics, image-to-video, music video, sound, trajectory, video generation  
- **[FlowWAM: Optical Flow as a Unified Action Representation for World Action Models](https://arxiv.org/abs/2607.13017v1)**  
  Authors: Yixiang Chen, Peiyan Li, Yuan Xu, Qisen Ma, Jiabing Yang, Kai Wang, Jianhua Yang, Dong An, He Guan, Gaoteng Liu, Jianlou Si, Jun Huang, Jing Liu, Nianfeng Liu, Yan Huang, Liang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.13017v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://flow-wam.github.io)  
  Keywords: trajectory, video generation, world model  
- **[ABot-3DWorld 0: A Universal World Model to Explore Any 3D Space](https://arxiv.org/abs/2607.11673v2)**  
  Authors: Mingchao Sun, Luyang Tang, Yu Liu, Xu Yan, Zhan Li, Yunwei Zhang, Fei Yu, Zengye Ge, Yumin Liu, Jiacheng Zhang, Yongchang Zhang, Jiawei Zhang, Zhicheng Liu, Zhongxu Sun, Tianjian Ouyang, Wenzheng Chen, Shixing Yang, Nianfei Fan, Guodong Sun, Huan Li, Zheng Zhou, Yongze Li, Yingliang Peng, Mengmeng Du, Yuan Liu, Haozhe Shi, Chunnuo Gong, Chengzhen Yu, Chunxue Jia, Yang Liu, Shiying Zeng, Junnan Lai, Hang Zhang, Ning Guo, Baoquan Chen, Mu Xu, Hongyu Pan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.11673v2.pdf)  
  Keywords: creative, efficient, trajectory, world model  
- **[Xiaomi-Robotics-U0: Unified Embodied Synthesis with World Foundation Model](https://arxiv.org/abs/2607.11643v1)**  
  Authors: Xinghang Li, Jun Guo, Qiwei Li, Long Qian, Hang Lai, Yueze Wang, Hongyu Yan, Jiahang Cao, Xi Chen, Jingen Qu, Jiaxi Song, Nan Sun, Hanye Zhao, Futeng Liu, Wanli Peng, Heyun Wang, Yunhong Wang, Caoyu Xia, Jack Zhao, Diyun Xiang, Hangjun Ye, Heng Qu, Huaping Liu, Jason Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.11643v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://robotics.xiaomi.com/xiaomi-robotics-u0.html)  
  Keywords: autoregressive, controllable, dit, dynamics, evaluation, robotics, video generation, world model  
- **[Controlling Motion Transfer in Diffusion Transformers via Attention Heads](https://arxiv.org/abs/2607.11081v1)**  
  Authors: Sunyoung Jung, Jiwoo Park, Yoonseok Choi, Kyobin Choo, Ming-Hsuan Yang, Seong Jae Hwang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.11081v1.pdf)  
  Keywords: controllable, diffusion transformer, dit, video generation  
- **[Is Energy Guidance All You Need? Training-Free Norm Injection for Driving World Models](https://arxiv.org/abs/2607.10781v1)**  
  Authors: Xiyan Su, Frank Diermeyer, Markus Lienkamp  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.10781v1.pdf)  
  Keywords: controllable, dit, layout, trajectory, world model  
- **[GenVid2Robot: From Video Generation to Robot Manipulation via Rigid-Geometric Consistency](https://arxiv.org/abs/2607.09191v1)**  
  Authors: Haohui Huang, Xi Yuan, Panpan Liao, Tao Teng, Chenguang Yang, Jing Guo, Yi Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.09191v1.pdf)  
  Keywords: dit, physical, trajectory, video generation  
- **[4D Human-Scene Reconstruction from Low-Overlap Captures](https://arxiv.org/abs/2607.09125v1)**  
  Authors: Minhyuk Hwang, Sangmin Kim, Seunguk Do, Daneul Kim, Jaesik Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.09125v1.pdf)  
  Keywords: diffusion model, identity, novel view, trajectory, video diffusion  
- **[OPSD-V: On-Policy Self-Distillation for Post-Training Few-Step Autoregressive Video Generators](https://arxiv.org/abs/2607.08766v1)**  
  Authors: Hongyu Liu, Chun Wang, Feng Gao, Xuanhua He, Yue Ma, Ziyu Wan, Yong Zhang, Xiaoming Wei, Qifeng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.08766v1.pdf)  
  Keywords: autoregressive, denoising, diffusion model, distillation, dit, dynamics, long video, trajectory, video diffusion  
- **[LightCrafter: PBR-Conditioned Video Diffusion Refinement for Controllable and Consistent Relighting](https://arxiv.org/abs/2607.08016v2)**  
  Authors: Zixin Guo, Yehonathan Litman, Yifeng He, John Miller, Chuhan Chen, Deva Ramanan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.08016v2.pdf)  
  Keywords: benchmark, concept, controllable, diffusion model, dit, long-form, physical, temporal consistency, video diffusion, video generation, video translation, video-to-video  

### Human & Character Animation

*Showing the latest 50 out of 94 papers*

- **[Wan-Dancer: A Hierarchical Framework for Minute-scale Coherent Music-to-Dance Generation](https://arxiv.org/abs/2607.09581v2)**  
  Authors: Mingyang Huang, Peng Zhang, Li Hu, Guangyuan Wang, Bang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.09581v2.pdf)  
  Keywords: dance generation, diffusion model, dit, identity, long-form, video synthesis  
- **[Behavior Foundations for Quadruped Robots: ABot-C0 Technical Report](https://arxiv.org/abs/2607.07370v2)**  
  Authors: Xufeng Zhao, Fuzhi Yang, Jianhui Chen, Li Gao, Zhang Meng, Jie Gao, Yao Zheng, Congyang Zhao, Tianxiong Lv, Menglin Yang, Minqi Gu, Yaru Zhao, Wenyu Liu, Honglin Han, Shihui Su, Zixiao Tang, Liu Liu, Mu Xu, Yang Cai, Wenbin Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.07370v2.pdf)  
  Keywords: dit, efficient, human motion, motion control, physical, style  
- **[ProxyPose: 6-DoF Pose Tracking via Video-to-Video Translation](https://arxiv.org/abs/2607.06555v1)**  
  Authors: Ruihang Zhang, Felix Taubner, Pooja Ravi, Kiriakos N. Kutulakos, David B. Lindell  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.06555v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ruihangzhang97.github.io/proxypose)  
  Keywords: body motion, diffusion model, dit, identity, trajectory, video diffusion, video translation, video-to-video  
- **[VendorBench-100: A Unified Cross-Paradigm Benchmark for Deepfake Image Detection](https://arxiv.org/abs/2607.06254v1)**  
  Authors: Sharayu N. Deshmukh, Md Rashidunnabi, Nelton Tiago Gemo, Kurundkar G. D., Mahamune M. R., Nilesh K. Deshmukh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.06254v1.pdf) | [![GitHub](https://img.shields.io/github/stars/sharayu-20/vendorbench-100?style=social)](https://github.com/sharayu-20/vendorbench-100)  
  Keywords: avatar, benchmark, dit, efficient, evaluation, text-to-video  
- **[3D Scene-Adaptive Trajectory-Controllable Human Image Animation with Camera Movement](https://arxiv.org/abs/2606.30514v2)**  
  Authors: Deyin Liu, Jicheng Xu, Lin Yuanbo Wu, Xiaowei Zhao, Xiatian Zhu, Zhe Jin, Anjan Dutta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30514v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://robinhood256100.github.io/web-disp)  
  Keywords: benchmark, camera control, controllable, dit, human motion, image animation, trajectory, video generation  
- **[OmniDance: Multimodal Driven Dance Video Generation with Large-scale Internet Data](https://arxiv.org/abs/2606.30019v1)**  
  Authors: Kaixing Yang, Jiashu Zhu, Xulong Tang, Ziqiao Peng, Xiangyue Zhang, Chubin Chen, Puwei Wang, Jiahong Wu, Xiangxiang Chu, Hongyan Liu, Jun He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30019v1.pdf) | [![GitHub](https://img.shields.io/github/stars/AMAP-ML/OmniDance?style=social)](https://github.com/AMAP-ML/OmniDance)  
  Keywords: architecture, dit, dynamics, human motion, i2v, video generation  
- **[EMOSH: Expressive Motion and Shape Disentanglement for Human Animation](https://arxiv.org/abs/2606.28026v1)**  
  Authors: Dongbin Zhang, Hao Liu, Binquan Dai, Kangjie Chen, Chuming Wang, Chen Li, Jing Lyu, Haoqian Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.28026v1.pdf)  
  Keywords: avatar, controllable, dit, gesture, human animation, identity, video generation  
- **[Directing the World: Fast Autoregressive Video Generation with Compositional Human-Camera Control](https://arxiv.org/abs/2606.27964v1)**  
  Authors: Haoyuan Wang, Yabo Chen, Haibin Huang, Chi Zhang, Xuelong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.27964v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://whydahuzi.github.io/Directing-the-World.github.io)  
  Keywords: autoregressive, camera control, controllable, dynamics, human motion, interactive, motion control, trajectory, video generation, world model  
- **[Follow Your Track: Precise Skeleton Animation Controlled by 3D Trajectories](https://arxiv.org/abs/2606.25344v1)**  
  Authors: Yueting Liu, Yanqin Jiang, Nian Liu, Jingmen Zhou, Zhengjun Zha, Weiming Hu, Jin Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.25344v1.pdf)  
  Keywords: 4d generation, body motion, dit, efficient, temporal consistency, trajectory  
- **[Wan-Streamer v0.1: End-to-end Real-time Interactive Foundation Models](https://arxiv.org/abs/2606.25041v3)**  
  Authors: Lianghua Huang, Zhi-Fan Wu, Wei Wang, Yupeng Shi, Mengyang Feng, Junjie He, Chen-Wei Xie, Yu Liu, Jingren Zhou, Ang Wang, Bang Zhang, Baole Ai, Chen Liang, Cheng Yu, Chongyang Zhong, Jinwei Qi, Kai Zhu, Pandeng Li, Peng Zhang, Wenyuan Zhang, Xinhua Cheng, Yitong Huang, Yun Zheng, Yuzheng Wang, Zoubin Bi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.25041v3.pdf)  
  Keywords: audio-driven, avatar, interactive, streaming  

### Image-to-Video Generation

*Showing the latest 50 out of 150 papers*

- **[Bring Music The Horizon: Music-Driven 360$^\circ$ Video Generation](https://arxiv.org/abs/2607.13471v1)**  
  Authors: Kai Hsu Tsai, Yong Wei Fu, Hung I Yang, Yu-Chih Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.13471v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://etoile-et-toi-mp3.github.io/BMTH_Project_Page)  
  Keywords: dit, dynamics, image-to-video, music video, sound, trajectory, video generation  
- **[Delving into the Temporal Challenges of Unified Video Protection Against Image-to-Video and Fine-Tuning-based Customization](https://arxiv.org/abs/2607.13336v1)**  
  Authors: Yuxin Huang, Ziming Hong, Mingming Gong, Wanyu Wang, Jing Zhang, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.13336v1.pdf)  
  Keywords: 3d video, customization, diffusion model, dit, identity, image-to-video, video diffusion, video generation  
- **[AU-Guided Synthetic Video Generation for Micro-Expression Recognition](https://arxiv.org/abs/2607.10860v1)**  
  Authors: Pei-Sze Tan, Sailaja Rajanala, Yee-Fan Tan, Raphael C. -W. Phan, Huey-Fang Ong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.10860v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kirito-blade.github.io/me-vlm)  
  Keywords: architecture, dit, image-to-video, video generation  
- **[OpenCoF: Learning to Reason Through Video Generation](https://arxiv.org/abs/2607.08763v1)**  
  Authors: Xinyan Chen, Ziyu Guo, Renrui Zhang, Dongzhi Jiang, Hongsheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.08763v1.pdf)  
  Keywords: benchmark, denoising, i2v, video generation  
- **[CineMobile: On-Device Image-to-Video Diffusion for Cinematic Camera Motion Generation](https://arxiv.org/abs/2607.03803v1)**  
  Authors: Xuyao Huang, Zelai Deng, Xu Wang, Xizhong Xiao, Zhijie Deng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.03803v1.pdf)  
  Keywords: architecture, denoising, diffusion transformer, distillation, dit, efficient, image-to-video, video diffusion, video generation  
- **[OrbitQuant: Data-Agnostic Quantization for Image and Video Diffusion Transformers](https://arxiv.org/abs/2607.02461v1)**  
  Authors: Donghyun Lee, Jitesh Chavan, Duy Nguyen, Sam Huang, Liming Jiang, Priyadarshini Panda, Timo Mertens, Saurabh Shukla  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.02461v1.pdf)  
  Keywords: diffusion transformer, dit, image to video, video diffusion, video generation  
- **[QWERTY: Training-Free Motion Control via Query-Warped Video Diffusion Transformers](https://arxiv.org/abs/2607.01869v1)**  
  Authors: Kyobin Choo, Youngmin Kim, Hyunkyung Han, Geunrip Park, Chanyoung Kim, Sunyoung Jung, Seong Jae Hwang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.01869v1.pdf)  
  Keywords: diffusion model, diffusion transformer, dit, image-to-video, motion control, trajectory, video diffusion  
- **[Anti-Prompt: Image Protection against Text-Guided Image-to-Video Generation](https://arxiv.org/abs/2607.01499v2)**  
  Authors: Yeonghwan Song, Chanhui Lee, Jinsoo Park, Jeany Son  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.01499v2.pdf)  
  Keywords: architecture, denoising, dit, evaluation, i2v, image-to-video, temporal consistency, video generation  
- **[TrajLoc: Trajectory-Attention Localization for Multi-Object Motion Control](https://arxiv.org/abs/2607.00861v1)**  
  Authors: Omer Sela, Inbar Huberman-Spiegelglas, Michael Rotman, Sagie Benaim, Avi Ben-Cohen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.00861v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://sela-omer.github.io/traj-loc)  
  Keywords: dit, evaluation, i2v, identity, image-to-video, motion control, trajectory  
- **[3D Scene-Adaptive Trajectory-Controllable Human Image Animation with Camera Movement](https://arxiv.org/abs/2606.30514v2)**  
  Authors: Deyin Liu, Jicheng Xu, Lin Yuanbo Wu, Xiaowei Zhao, Xiatian Zhu, Zhe Jin, Anjan Dutta  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.30514v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://robinhood256100.github.io/web-disp)  
  Keywords: benchmark, camera control, controllable, dit, human motion, image animation, trajectory, video generation  

### Long Video Generation

*Showing the latest 50 out of 420 papers*

- **[VideoRAE: Taming Video Foundation Models for Generative Modeling via Representation Autoencoders](https://arxiv.org/abs/2607.14088v1)**  
  Authors: Zhihao Xie, Junfeng Wu, Xinting Hu, Junchao Huang, Li Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.14088v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zhxie0117.github.io/VideoRAE)  
  Keywords: autoregressive, diffusion transformer, dit, text-to-video  
- **[Text2Sign: A Single-GPU Diffusion Baseline for Text-to-Sign Language Video Generation](https://arxiv.org/abs/2607.13164v1)**  
  Authors: Ruize Xia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.13164v1.pdf) | [![GitHub](https://img.shields.io/github/stars/xiaruize0911/text2sign?style=social)](https://github.com/xiaruize0911/text2sign)  
  Keywords: denoising, diffusion model, dit, evaluation, style, temporal consistency, video diffusion, video generation  
- **[The Seriality Gap in Video Diffusion Models](https://arxiv.org/abs/2607.13031v1)**  
  Authors: Jorge Diaz Chao, Konpat Preechakul, Yuxi Liu, Yutong Bai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.13031v1.pdf)  
  Keywords: autoregressive, denoising, diffusion model, dynamics, simulation, video diffusion, video prediction  
- **[WanToFight: Real-Time Generative Game Engine for Multi-Player Combat Interaction](https://arxiv.org/abs/2607.12592v1)**  
  Authors: Li Hu, Guangyuan Wang, Peng Zhang, Bang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.12592v1.pdf)  
  Keywords: autoregressive, diffusion transformer, identity, physical, streaming, video diffusion  
- **[Cycle-World: Mitigating Error Accumulation in Long-term Video World Models via Reverse-Prediction Cycle Consistency](https://arxiv.org/abs/2607.11836v1)**  
  Authors: Zihan Su, Teng Hu, Jiangning Zhang, Ruiyan Wang, Ran Yi, Lizhuang Ma, Dacheng Tao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.11836v1.pdf)  
  Keywords: autoregressive, benchmark, diffusion model, efficient, temporal consistency, video generation, video synthesis, world model  
- **[Xiaomi-Robotics-U0: Unified Embodied Synthesis with World Foundation Model](https://arxiv.org/abs/2607.11643v1)**  
  Authors: Xinghang Li, Jun Guo, Qiwei Li, Long Qian, Hang Lai, Yueze Wang, Hongyu Yan, Jiahang Cao, Xi Chen, Jingen Qu, Jiaxi Song, Nan Sun, Hanye Zhao, Futeng Liu, Wanli Peng, Heyun Wang, Yunhong Wang, Caoyu Xia, Jack Zhao, Diyun Xiang, Hangjun Ye, Heng Qu, Huaping Liu, Jason Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.11643v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://robotics.xiaomi.com/xiaomi-robotics-u0.html)  
  Keywords: autoregressive, controllable, dit, dynamics, evaluation, robotics, video generation, world model  
- **[Wan-Dancer: A Hierarchical Framework for Minute-scale Coherent Music-to-Dance Generation](https://arxiv.org/abs/2607.09581v2)**  
  Authors: Mingyang Huang, Peng Zhang, Li Hu, Guangyuan Wang, Bang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.09581v2.pdf)  
  Keywords: dance generation, diffusion model, dit, identity, long-form, video synthesis  
- **[Spectral Origins of the Self-Correction Blind Spot in Autoregressive Generation](https://arxiv.org/abs/2607.09803v1)**  
  Authors: Ingrid Petrova, Luan Vejsiu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.09803v1.pdf)  
  Keywords: autoregressive, dit, video generation  
- **[LongE2V: Long-Horizon Event-based Video Reconstruction, Prediction, and Frame Interpolation with Video Diffusion Models](https://arxiv.org/abs/2607.08770v1)**  
  Authors: Cheng-De Fan, Chun-Wei Tuan Mu, Chen-Wei Chang, Chin-Yang Lin, Kun-Ru Wu, Yu-Chee Tseng, Yu-Lun Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.08770v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://cdfan0627.github.io/LongE2V-page)  
  Keywords: autoregressive, benchmark, diffusion model, frame interpolation, video diffusion  
- **[OPSD-V: On-Policy Self-Distillation for Post-Training Few-Step Autoregressive Video Generators](https://arxiv.org/abs/2607.08766v1)**  
  Authors: Hongyu Liu, Chun Wang, Feng Gao, Xuanhua He, Yue Ma, Ziyu Wan, Yong Zhang, Xiaoming Wei, Qifeng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.08766v1.pdf)  
  Keywords: autoregressive, denoising, diffusion model, distillation, dit, dynamics, long video, trajectory, video diffusion  

### Personalization & Customization

*Showing the latest 50 out of 303 papers*

- **[Delving into the Temporal Challenges of Unified Video Protection Against Image-to-Video and Fine-Tuning-based Customization](https://arxiv.org/abs/2607.13336v1)**  
  Authors: Yuxin Huang, Ziming Hong, Mingming Gong, Wanyu Wang, Jing Zhang, Tongliang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.13336v1.pdf)  
  Keywords: 3d video, customization, diffusion model, dit, identity, image-to-video, video diffusion, video generation  
- **[Text2Sign: A Single-GPU Diffusion Baseline for Text-to-Sign Language Video Generation](https://arxiv.org/abs/2607.13164v1)**  
  Authors: Ruize Xia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.13164v1.pdf) | [![GitHub](https://img.shields.io/github/stars/xiaruize0911/text2sign?style=social)](https://github.com/xiaruize0911/text2sign)  
  Keywords: denoising, diffusion model, dit, evaluation, style, temporal consistency, video diffusion, video generation  
- **[WanToFight: Real-Time Generative Game Engine for Multi-Player Combat Interaction](https://arxiv.org/abs/2607.12592v1)**  
  Authors: Li Hu, Guangyuan Wang, Peng Zhang, Bang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.12592v1.pdf)  
  Keywords: autoregressive, diffusion transformer, identity, physical, streaming, video diffusion  
- **[SymbOmni: Evolving Agentic Omni Models via Symbolic Concept Learning](https://arxiv.org/abs/2607.12042v1)**  
  Authors: Jinxiu Liu, Jianru Li, Tanqing Kuang, Xuanming Liu, Kangfu Mei, Yandong Wen, Weiyang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.12042v1.pdf)  
  Keywords: benchmark, concept, efficient, interactive, video synthesis  
- **[Wan-Dancer: A Hierarchical Framework for Minute-scale Coherent Music-to-Dance Generation](https://arxiv.org/abs/2607.09581v2)**  
  Authors: Mingyang Huang, Peng Zhang, Li Hu, Guangyuan Wang, Bang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.09581v2.pdf)  
  Keywords: dance generation, diffusion model, dit, identity, long-form, video synthesis  
- **[Generative Communications: Overview, Technologies, and Trends](https://arxiv.org/abs/2607.09183v1)**  
  Authors: Wenjun Zhang, Zhiyong Chen, Tong Wu, Guo Lu, Li Song, Feng Yang, Meixia Tao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.09183v1.pdf)  
  Keywords: architecture, concept, dit, efficient  
- **[4D Human-Scene Reconstruction from Low-Overlap Captures](https://arxiv.org/abs/2607.09125v1)**  
  Authors: Minhyuk Hwang, Sangmin Kim, Seunguk Do, Daneul Kim, Jaesik Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.09125v1.pdf)  
  Keywords: diffusion model, identity, novel view, trajectory, video diffusion  
- **[Applying JEPA-Style Predictive Learning to JA4-Derived Network Fingerprints](https://arxiv.org/abs/2607.08465v1)**  
  Authors: Javier Izquierdo, Aygul Zagidullina  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.08465v1.pdf)  
  Keywords: style  
- **[LightCrafter: PBR-Conditioned Video Diffusion Refinement for Controllable and Consistent Relighting](https://arxiv.org/abs/2607.08016v2)**  
  Authors: Zixin Guo, Yehonathan Litman, Yifeng He, John Miller, Chuhan Chen, Deva Ramanan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.08016v2.pdf)  
  Keywords: benchmark, concept, controllable, diffusion model, dit, long-form, physical, temporal consistency, video diffusion, video generation, video translation, video-to-video  
- **[Behavior Foundations for Quadruped Robots: ABot-C0 Technical Report](https://arxiv.org/abs/2607.07370v2)**  
  Authors: Xufeng Zhao, Fuzhi Yang, Jianhui Chen, Li Gao, Zhang Meng, Jie Gao, Yao Zheng, Congyang Zhao, Tianxiong Lv, Menglin Yang, Minqi Gu, Yaru Zhao, Wenyu Liu, Honglin Han, Shihui Su, Zixiao Tang, Liu Liu, Mu Xu, Yang Cai, Wenbin Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.07370v2.pdf)  
  Keywords: dit, efficient, human motion, motion control, physical, style  

### Physical Understanding

*Showing the latest 50 out of 502 papers*

- **[From Pixels to States: Rethinking Interactive World Models as Game Engines](https://arxiv.org/abs/2607.14076v1)**  
  Authors: Zhen Li, Zian Meng, Shuwei Shi, Mingliang Zhai, Jiaming Tan, Chuanhao Li, Kaipeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.14076v1.pdf)  
  Keywords: dit, dynamics, interactive, world model  
- **[Cyclone: Diffusion Model for Cycle-Consistent Weather Editing from Unpaired Driving Data](https://arxiv.org/abs/2607.13927v1)**  
  Authors: Thang-Anh-Quan Nguyen, Moussab Bennehar, Luis Guillermo Roldao Jimenez, Nathan Piasco, Dzmitry Tsishkou, Laurent Caraffa, Jean-Philippe Tarel, Roland Brémond  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.13927v1.pdf)  
  Keywords: autonomous driving, diffusion model, dit, physics, video diffusion  
- **[VGIF-Score: Interpretable and Diagnostic Evaluation of Spatio-Temporal Instruction Following in Video Generation](https://arxiv.org/abs/2607.13527v1)**  
  Authors: Songyu Xu, Xin Wang, Qiang Chen, Xinran Wang, Muxi Diao, Yuxuan Zhang, Kongming Liang, Rui Lin, Zhanyu Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.13527v1.pdf) | [![GitHub](https://img.shields.io/github/stars/PRIS-CV/VGIF-SCORE?style=social)](https://github.com/PRIS-CV/VGIF-SCORE)  
  Keywords: benchmark, dit, evaluation, physics, video generation  
- **[Bring Music The Horizon: Music-Driven 360$^\circ$ Video Generation](https://arxiv.org/abs/2607.13471v1)**  
  Authors: Kai Hsu Tsai, Yong Wei Fu, Hung I Yang, Yu-Chih Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.13471v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://etoile-et-toi-mp3.github.io/BMTH_Project_Page)  
  Keywords: dit, dynamics, image-to-video, music video, sound, trajectory, video generation  
- **[The Seriality Gap in Video Diffusion Models](https://arxiv.org/abs/2607.13031v1)**  
  Authors: Jorge Diaz Chao, Konpat Preechakul, Yuxi Liu, Yutong Bai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.13031v1.pdf)  
  Keywords: autoregressive, denoising, diffusion model, dynamics, simulation, video diffusion, video prediction  
- **[WanToFight: Real-Time Generative Game Engine for Multi-Player Combat Interaction](https://arxiv.org/abs/2607.12592v1)**  
  Authors: Li Hu, Guangyuan Wang, Peng Zhang, Bang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.12592v1.pdf)  
  Keywords: autoregressive, diffusion transformer, identity, physical, streaming, video diffusion  
- **[Xiaomi-Robotics-U0: Unified Embodied Synthesis with World Foundation Model](https://arxiv.org/abs/2607.11643v1)**  
  Authors: Xinghang Li, Jun Guo, Qiwei Li, Long Qian, Hang Lai, Yueze Wang, Hongyu Yan, Jiahang Cao, Xi Chen, Jingen Qu, Jiaxi Song, Nan Sun, Hanye Zhao, Futeng Liu, Wanli Peng, Heyun Wang, Yunhong Wang, Caoyu Xia, Jack Zhao, Diyun Xiang, Hangjun Ye, Heng Qu, Huaping Liu, Jason Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.11643v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://robotics.xiaomi.com/xiaomi-robotics-u0.html)  
  Keywords: autoregressive, controllable, dit, dynamics, evaluation, robotics, video generation, world model  
- **[GenVid2Robot: From Video Generation to Robot Manipulation via Rigid-Geometric Consistency](https://arxiv.org/abs/2607.09191v1)**  
  Authors: Haohui Huang, Xi Yuan, Panpan Liao, Tao Teng, Chenguang Yang, Jing Guo, Yi Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.09191v1.pdf)  
  Keywords: dit, physical, trajectory, video generation  
- **[Video Generation Models are General-Purpose Vision Learners](https://arxiv.org/abs/2607.09024v1)**  
  Authors: Letian Wang, Chuhan Zhang, Rishabh Kabra, Jasper Uijlings, Steven Waslander, Andrew Zisserman, Joao Carreira, Kaiming He, Misha Andriluka, Eduard Gabriel Bazavan, Andrei Zanfir, Cristian Sminchisescu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.09024v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://genception.github.io)  
  Keywords: physical, text-to-video, video generation  
- **[OPSD-V: On-Policy Self-Distillation for Post-Training Few-Step Autoregressive Video Generators](https://arxiv.org/abs/2607.08766v1)**  
  Authors: Hongyu Liu, Chun Wang, Feng Gao, Xuanhua He, Yue Ma, Ziyu Wan, Yong Zhang, Xiaoming Wei, Qifeng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.08766v1.pdf)  
  Keywords: autoregressive, denoising, diffusion model, distillation, dit, dynamics, long video, trajectory, video diffusion  

### Surveys & Benchmarks

*Showing the latest 50 out of 746 papers*

- **[Kaleido: Algorithm-Hardware Co-Design for Video Diffusion Transformers by Exploiting Latent Space Correlations](https://arxiv.org/abs/2607.13770v1)**  
  Authors: Wenxuan Miao, Haosong Liu, Weiming Hu, Zihan Liu, Aiyue Chen, Jianlin Yu, Yiwu Yao, Yiming Gan, Jieru Zhao, Jingwen Leng, Minyi Guo, Yu Feng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.13770v1.pdf)  
  Keywords: acceleration, diffusion transformer, dit, efficient, evaluation, video diffusion  
- **[VGIF-Score: Interpretable and Diagnostic Evaluation of Spatio-Temporal Instruction Following in Video Generation](https://arxiv.org/abs/2607.13527v1)**  
  Authors: Songyu Xu, Xin Wang, Qiang Chen, Xinran Wang, Muxi Diao, Yuxuan Zhang, Kongming Liang, Rui Lin, Zhanyu Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.13527v1.pdf) | [![GitHub](https://img.shields.io/github/stars/PRIS-CV/VGIF-SCORE?style=social)](https://github.com/PRIS-CV/VGIF-SCORE)  
  Keywords: benchmark, dit, evaluation, physics, video generation  
- **[Continuously Evolving Deepfake Detection: An Architecture and Public-Benchmark Evaluation of a Dynamic Detection System](https://arxiv.org/abs/2607.13234v1)**  
  Authors: Ken Jon Miyachi, Dylan Uys  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.13234v1.pdf)  
  Keywords: architecture, benchmark, dit, evaluation  
- **[Text2Sign: A Single-GPU Diffusion Baseline for Text-to-Sign Language Video Generation](https://arxiv.org/abs/2607.13164v1)**  
  Authors: Ruize Xia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.13164v1.pdf) | [![GitHub](https://img.shields.io/github/stars/xiaruize0911/text2sign?style=social)](https://github.com/xiaruize0911/text2sign)  
  Keywords: denoising, diffusion model, dit, evaluation, style, temporal consistency, video diffusion, video generation  
- **[ACID: Adaptive Caching for vIDeo generation](https://arxiv.org/abs/2607.12358v1)**  
  Authors: Om Agrawal, Saurabh Agarwal, Aditya Akella  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.12358v1.pdf)  
  Keywords: acceleration, denoising, diffusion model, dit, evaluation, video diffusion, video generation  
- **[MobileSAM2: Lightweight Segment Anything for Spatial Intelligence](https://arxiv.org/abs/2607.12297v1)**  
  Authors: Kai Jiang, Jiaxing Huang, Jingyi Zhang, Weiying Xie, Yunsong Li, Yufei Wang, Aoran Xiao, Dacheng Tao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.12297v1.pdf)  
  Keywords: architecture, benchmark, distillation  
- **[SymbOmni: Evolving Agentic Omni Models via Symbolic Concept Learning](https://arxiv.org/abs/2607.12042v1)**  
  Authors: Jinxiu Liu, Jianru Li, Tanqing Kuang, Xuanming Liu, Kangfu Mei, Yandong Wen, Weiyang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.12042v1.pdf)  
  Keywords: benchmark, concept, efficient, interactive, video synthesis  
- **[Cycle-World: Mitigating Error Accumulation in Long-term Video World Models via Reverse-Prediction Cycle Consistency](https://arxiv.org/abs/2607.11836v1)**  
  Authors: Zihan Su, Teng Hu, Jiangning Zhang, Ruiyan Wang, Ran Yi, Lizhuang Ma, Dacheng Tao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.11836v1.pdf)  
  Keywords: autoregressive, benchmark, diffusion model, efficient, temporal consistency, video generation, video synthesis, world model  
- **[Xiaomi-Robotics-U0: Unified Embodied Synthesis with World Foundation Model](https://arxiv.org/abs/2607.11643v1)**  
  Authors: Xinghang Li, Jun Guo, Qiwei Li, Long Qian, Hang Lai, Yueze Wang, Hongyu Yan, Jiahang Cao, Xi Chen, Jingen Qu, Jiaxi Song, Nan Sun, Hanye Zhao, Futeng Liu, Wanli Peng, Heyun Wang, Yunhong Wang, Caoyu Xia, Jack Zhao, Diyun Xiang, Hangjun Ye, Heng Qu, Huaping Liu, Jason Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.11643v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://robotics.xiaomi.com/xiaomi-robotics-u0.html)  
  Keywords: autoregressive, controllable, dit, dynamics, evaluation, robotics, video generation, world model  
- **[Prompting-MammAlps: Fine-Grained Text-to-Video Retrieval for Camera-Trap Data](https://arxiv.org/abs/2607.09876v1)**  
  Authors: Valentin Gabeff, Baptiste Maquignaz, Jennifer Shan, Sepideh Mamooler, Gencer Sumbul, Blair Costelloe, Devis Tuia, Alexander Mathis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.09876v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://cnai.epfl.ch/prompting-mammalps)  
  Keywords: benchmark, text-to-video  

### Text-to-Video Generation

*Showing the latest 50 out of 228 papers*

- **[VideoRAE: Taming Video Foundation Models for Generative Modeling via Representation Autoencoders](https://arxiv.org/abs/2607.14088v1)**  
  Authors: Zhihao Xie, Junfeng Wu, Xinting Hu, Junchao Huang, Li Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.14088v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zhxie0117.github.io/VideoRAE)  
  Keywords: autoregressive, diffusion transformer, dit, text-to-video  
- **[Prompting-MammAlps: Fine-Grained Text-to-Video Retrieval for Camera-Trap Data](https://arxiv.org/abs/2607.09876v1)**  
  Authors: Valentin Gabeff, Baptiste Maquignaz, Jennifer Shan, Sepideh Mamooler, Gencer Sumbul, Blair Costelloe, Devis Tuia, Alexander Mathis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.09876v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://cnai.epfl.ch/prompting-mammalps)  
  Keywords: benchmark, text-to-video  
- **[Video Generation Models are General-Purpose Vision Learners](https://arxiv.org/abs/2607.09024v1)**  
  Authors: Letian Wang, Chuhan Zhang, Rishabh Kabra, Jasper Uijlings, Steven Waslander, Andrew Zisserman, Joao Carreira, Kaiming He, Misha Andriluka, Eduard Gabriel Bazavan, Andrei Zanfir, Cristian Sminchisescu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.09024v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://genception.github.io)  
  Keywords: physical, text-to-video, video generation  
- **[HumanForge: A Human-Centric Deepfake Video Benchmark with Multi-Agent Forgery Rationales](https://arxiv.org/abs/2607.08705v1)**  
  Authors: Wenbo Xu, Zhimin Chen, Xiaojie Liang, Hengrui Liu, Wei Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.08705v1.pdf)  
  Keywords: benchmark, diffusion model, dit, multi-modal, text-to-video, video diffusion, video synthesis  
- **[Prompt-Adapter Context Routing for Parameter-Efficient Multi-Shot Long Video Extrapolation](https://arxiv.org/abs/2607.06481v1)**  
  Authors: Anna Córdoba, Adam Puente Tercero, Nerea Angulo Hijo, Mar Linares Tercero, Julia Barrientos, Ainhoa Miranda, Jesús Olivera  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.06481v1.pdf)  
  Keywords: benchmark, controllable, diffusion transformer, dit, efficient, identity, long video, streaming, style, text-to-video, video diffusion  
- **[FADRA: Frequency-Aware Diffusion with Residual Adaptation for Video Face Restoration](https://arxiv.org/abs/2607.06389v1)**  
  Authors: Jin Jiang, Jia Wang, Panwen Hu, Weiran Zhao, Shengcai Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.06389v1.pdf)  
  Keywords: diffusion model, efficient, temporal consistency, text-to-video, video diffusion  
- **[VendorBench-100: A Unified Cross-Paradigm Benchmark for Deepfake Image Detection](https://arxiv.org/abs/2607.06254v1)**  
  Authors: Sharayu N. Deshmukh, Md Rashidunnabi, Nelton Tiago Gemo, Kurundkar G. D., Mahamune M. R., Nilesh K. Deshmukh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.06254v1.pdf) | [![GitHub](https://img.shields.io/github/stars/sharayu-20/vendorbench-100?style=social)](https://github.com/sharayu-20/vendorbench-100)  
  Keywords: avatar, benchmark, dit, efficient, evaluation, text-to-video  
- **[Enhancing Video Physical Consistency via Role-aware Joint Training and Modality-decoupled Denoising](https://arxiv.org/abs/2607.04653v2)**  
  Authors: Guangting Zheng, Haojing Chen, Hao Li, Jingtao Zhang, Zhen Yang, Xiaosong Jia, Xue Yang, Shaofeng Zhang, Yanyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.04653v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://tom-zgt.github.io/VPT)  
  Keywords: benchmark, denoising, diffusion model, dynamics, physical, physics, t2v, video diffusion  
- **[Lights, Camera, Carbon: Architectural Scaling Laws for Video Generation Energy Consumption](https://arxiv.org/abs/2607.04553v1)**  
  Authors: Nidhal Jegham, Boris Gamazaychikov, Sasha Luccioni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.04553v1.pdf)  
  Keywords: architecture, benchmark, diffusion model, dit, efficient, t2v, text-to-video, video diffusion, video generation  
- **[HyperVAttention: Efficient Sparse Attention with Spatio-Temporal Clustering for Video Diffusion](https://arxiv.org/abs/2607.03012v1)**  
  Authors: Dongyeun Lee, Amir Zandieh, Vahab Mirrokni, Junmo Kim, Insu Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.03012v1.pdf)  
  Keywords: denoising, diffusion transformer, dit, efficient, text-to-video, video diffusion, video generation  

### Video Editing

*Showing the latest 50 out of 113 papers*

- **[LightCrafter: PBR-Conditioned Video Diffusion Refinement for Controllable and Consistent Relighting](https://arxiv.org/abs/2607.08016v2)**  
  Authors: Zixin Guo, Yehonathan Litman, Yifeng He, John Miller, Chuhan Chen, Deva Ramanan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.08016v2.pdf)  
  Keywords: benchmark, concept, controllable, diffusion model, dit, long-form, physical, temporal consistency, video diffusion, video generation, video translation, video-to-video  
- **[ProxyPose: 6-DoF Pose Tracking via Video-to-Video Translation](https://arxiv.org/abs/2607.06555v1)**  
  Authors: Ruihang Zhang, Felix Taubner, Pooja Ravi, Kiriakos N. Kutulakos, David B. Lindell  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.06555v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ruihangzhang97.github.io/proxypose)  
  Keywords: body motion, diffusion model, dit, identity, trajectory, video diffusion, video translation, video-to-video  
- **[Consistent and Editable: A Balanced Framework for Text-Guided Video Editing](https://arxiv.org/abs/2607.05056v1)**  
  Authors: Tao Jin, Li Xiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.05056v1.pdf)  
  Keywords: diffusion model, dit, temporal consistency, video editing  
- **[ProxyUp: Training-Free Proxy-Conditioned Video Generation for Controllable Dynamics](https://arxiv.org/abs/2607.03732v1)**  
  Authors: Zanwei Zhou, Jiazhong Cen, Jiemin Fang, Yumeng He, Chen Yang, Sikuang Li, Fanpeng Meng, Zhikuan Bao, Wei Shen, Qi Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.03732v1.pdf)  
  Keywords: controllable, dit, dynamics, physical, physics, simulation, video editing, video generation  
- **[LiveEdit: Towards Real-Time Diffusion-Based Streaming Video Editing](https://arxiv.org/abs/2606.26740v2)**  
  Authors: Xinyu Wang, Chongbo Zhao, Fangneng Zhan, Yue Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.26740v2.pdf)  
  Keywords: benchmark, distillation, dit, efficient, evaluation, interactive, streaming, video editing, video generation  
- **[Vera: A Layered Diffusion Model for Content-Preserving Video Editing](https://arxiv.org/abs/2606.23610v1)**  
  Authors: Hongkai Zheng, Ta-Ying Cheng, Benjamin Klein, Yisong Yue, Zhuoning Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.23610v1.pdf)  
  Keywords: architecture, benchmark, creative, diffusion model, dit, dynamics, text-to-video, video diffusion, video editing, video generation  
- **[SteerVTE: Seamless Video Text Editing with Style and Glyph Control](https://arxiv.org/abs/2606.23254v1)**  
  Authors: Kai Zeng, Moran Li, Zhengwei Wang, Yingchen Yu, Yiheng Lin, Ruichuan An, Ming Lu, Qi She, Wentao Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.23254v1.pdf)  
  Keywords: diffusion model, diffusion transformer, dit, image to video, style, video diffusion, video editing  
- **[Generative Relightable Avatars](https://arxiv.org/abs/2606.22718v1)**  
  Authors: Kunwar Maheep Singh, Christian Theobalt, Rishabh Dabral  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.22718v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vcai.mpi-inf.mpg.de/projects/GRA)  
  Keywords: avatar, controllable, diffusion model, dynamics, evaluation, long video, physical, physics, video diffusion, video-to-video  
- **[ReGenHuman: Re-Generating Human Appearances for Realistic Full-Body Video Anonymization](https://arxiv.org/abs/2606.14972v1)**  
  Authors: Adam Sun, Eshaan Barkataki, Arnold Milstein, Gordon Wetzstein, Ehsan Adeli  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.14972v1.pdf)  
  Keywords: dit, identity, video diffusion, video-to-video  
- **[Lip Forcing: Few-Step Autoregressive Diffusion for Real-time Lip Synchronization](https://arxiv.org/abs/2606.11180v1)**  
  Authors: Paul Hyunbin Cho, Jinhyuk Jang, SeokYoung Lee, Joungbin Lee, Siyoon Jin, Heeseong Shin, Jung Yi, Yunjin Park, Chulmin Park, Seungryong Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.11180v1.pdf)  
  Keywords: autoregressive, denoising, diffusion model, dit, streaming, trajectory, video diffusion, video-to-video  

### Video Inpainting & Completion

- **[The Seriality Gap in Video Diffusion Models](https://arxiv.org/abs/2607.13031v1)**  
  Authors: Jorge Diaz Chao, Konpat Preechakul, Yuxi Liu, Yutong Bai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.13031v1.pdf)  
  Keywords: autoregressive, denoising, diffusion model, dynamics, simulation, video diffusion, video prediction  
- **[Video Generation Models Are Inherent Lighting Estimators](https://arxiv.org/abs/2607.04674v1)**  
  Authors: Ziqi Cai, Shuchen Weng, Kaiqi Liu, Zifeng Wang, Zhiquan Zhang, Minggui Teng, Han Jiang, Boxin Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.04674v1.pdf)  
  Keywords: diffusion model, efficient, physical, video diffusion, video generation, video inpainting  
- **[ImageWAM: Do World Action Models Really Need Video Generation, or Just Image Editing?](https://arxiv.org/abs/2606.19531v1)**  
  Authors: Yuyang Zhang, Wenyao Zhang, Zekun Qi, He Zhang, Haitao Lin, Jingbo Zhang, Yao Mu, Xiaokang Yang, Wenjun Zeng, Xin Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.19531v1.pdf)  
  Keywords: denoising, dit, video generation, video prediction, world model  
- **[R2RDreamer: 3D-aware Data Augmentation for Spatially-generalized 2D Manipulation Policies](https://arxiv.org/abs/2606.17040v1)**  
  Authors: Xiuwei Xu, Haowen Sun, Angyuan Ma, Yiwei Zhang, Zhenyu Wu, Xiaofeng Wang, Bingyao Yu, Zheng Zhu, Jie Zhou, Jiwen Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.17040v1.pdf)  
  Keywords: 3d-aware, controllable, dit, image-to-video, simulation, style, video completion  
- **[PointAction: 3D Points as Universal Action Representations for Robot Control](https://arxiv.org/abs/2606.03943v1)**  
  Authors: Mutian Tong, Han Jiang, Qiao Feng, Lingjie Liu, Jiatao Gu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.03943v1.pdf)  
  Keywords: 4d generation, diffusion model, dynamics, simulation, video diffusion, video generation, video prediction  
- **[World Models: A Comprehensive Survey of Architectures, Methodologies, Reasoning Paradigms, and Applications](https://arxiv.org/abs/2606.00133v1)**  
  Authors: Arif Hassan Zidan, Yi Pan, Hanqi Jiang, Ruiyu Yan, Wei Ruan, Zihao Wu, Lifeng Chen, Weihang You, Xinliang Li, Bowen Chen, Huawen Hu, Peilong Wang, Sizhuang Liu, Jing Zhang, Siyuan Li, Zhengliang Liu, Yu Bao, Lin Zhao, Lichao Sun, Dajiang Zhu, Xiang Li, Jinglei Lv, Quanzheng Li, Wei Liu, Tianming Liu, Wei Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2606.00133v1.pdf)  
  Keywords: architecture, autonomous driving, benchmark, dynamics, education, evaluation, interactive, medical, physics, robotics, survey, video generation, video prediction, world model  
- **[Full-4D: Generating Full-Scope 4D Scenes from a Single-View Video](https://arxiv.org/abs/2605.25500v1)**  
  Authors: Tingxi Chen, Ke Hao, Yabo Chen, Zhengxue Cheng, Rong Xie, Li Song, Haibin Huang, Chi Zhang, Xuelong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.25500v1.pdf)  
  Keywords: 4d generation, diffusion model, distillation, dit, flow matching, interactive, multi-view video, physical, video diffusion, video interpolation, video synthesis  
- **[CRONOS: Benchmarking Counterfactual Physical Consistency in Video Models](https://arxiv.org/abs/2605.23699v1)**  
  Authors: León Begiristain, Olaf Dünkel, Adam Kortylewski  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.23699v1.pdf)  
  Keywords: benchmark, dit, dynamics, evaluation, physical, video prediction, world model  
- **[GEM-4D: Geometry-Enhanced Video World Models for Robot Manipulation](https://arxiv.org/abs/2605.22882v3)**  
  Authors: Kaichen Zhou, Yuzhen Chen, Fangneng Zhan, Hang Hua, Grace Chen, Xinhai Chang, Ao Qu, Yilun Du, Zhuang Liu, Paul Pu Liang, Mengyu Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.22882v3.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gem-4d.github.io)  
  Keywords: architecture, dit, dynamics, physical, simulation, video prediction, world model  
- **[Goodbye Drift: Anchored Tree Sampling for Long-Horizon Video-to-Video Generation](https://arxiv.org/abs/2605.20476v1)**  
  Authors: Matthew Bendel, Stephen W. Bailey, Mithilesh Vaidya, Sumukh Badam, Xingzhe He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.20476v1.pdf)  
  Keywords: autoregressive, distillation, dit, outpainting, style, t2v, video generation, video-to-video  

### Video Super-Resolution & Enhancement

*Showing the latest 50 out of 226 papers*

- **[Text2Sign: A Single-GPU Diffusion Baseline for Text-to-Sign Language Video Generation](https://arxiv.org/abs/2607.13164v1)**  
  Authors: Ruize Xia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.13164v1.pdf) | [![GitHub](https://img.shields.io/github/stars/xiaruize0911/text2sign?style=social)](https://github.com/xiaruize0911/text2sign)  
  Keywords: denoising, diffusion model, dit, evaluation, style, temporal consistency, video diffusion, video generation  
- **[The Seriality Gap in Video Diffusion Models](https://arxiv.org/abs/2607.13031v1)**  
  Authors: Jorge Diaz Chao, Konpat Preechakul, Yuxi Liu, Yutong Bai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.13031v1.pdf)  
  Keywords: autoregressive, denoising, diffusion model, dynamics, simulation, video diffusion, video prediction  
- **[ACID: Adaptive Caching for vIDeo generation](https://arxiv.org/abs/2607.12358v1)**  
  Authors: Om Agrawal, Saurabh Agarwal, Aditya Akella  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.12358v1.pdf)  
  Keywords: acceleration, denoising, diffusion model, dit, evaluation, video diffusion, video generation  
- **[LongE2V: Long-Horizon Event-based Video Reconstruction, Prediction, and Frame Interpolation with Video Diffusion Models](https://arxiv.org/abs/2607.08770v1)**  
  Authors: Cheng-De Fan, Chun-Wei Tuan Mu, Chen-Wei Chang, Chin-Yang Lin, Kun-Ru Wu, Yu-Chee Tseng, Yu-Lun Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.08770v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://cdfan0627.github.io/LongE2V-page)  
  Keywords: autoregressive, benchmark, diffusion model, frame interpolation, video diffusion  
- **[OPSD-V: On-Policy Self-Distillation for Post-Training Few-Step Autoregressive Video Generators](https://arxiv.org/abs/2607.08766v1)**  
  Authors: Hongyu Liu, Chun Wang, Feng Gao, Xuanhua He, Yue Ma, Ziyu Wan, Yong Zhang, Xiaoming Wei, Qifeng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.08766v1.pdf)  
  Keywords: autoregressive, denoising, diffusion model, distillation, dit, dynamics, long video, trajectory, video diffusion  
- **[OpenCoF: Learning to Reason Through Video Generation](https://arxiv.org/abs/2607.08763v1)**  
  Authors: Xinyan Chen, Ziyu Guo, Renrui Zhang, Dongzhi Jiang, Hongsheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.08763v1.pdf)  
  Keywords: benchmark, denoising, i2v, video generation  
- **[Dynamic-in-Few-Step: Unifying Dynamic Computation and Few-Step Distillation for Efficient Video Generation](https://arxiv.org/abs/2607.06631v1)**  
  Authors: Yu Cheng, Siyue Yao, Zhongang Qi, Shanyan Guan, Wei Li, Fajie Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.06631v1.pdf)  
  Keywords: acceleration, architecture, denoising, diffusion model, distillation, efficient, video diffusion, video generation  
- **[MV-Forcing: Long Multi-View Video Generation via 4D-Grounded Spatio-Temporal Self-Forcing](https://arxiv.org/abs/2607.05376v1)**  
  Authors: Gal Fiebelman, Hadar Averbuch-Elor, Sagie Benaim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.05376v1.pdf)  
  Keywords: autoregressive, denoising, diffusion model, distillation, multi-view video, video diffusion, video generation  
- **[Enhancing Video Physical Consistency via Role-aware Joint Training and Modality-decoupled Denoising](https://arxiv.org/abs/2607.04653v2)**  
  Authors: Guangting Zheng, Haojing Chen, Hao Li, Jingtao Zhang, Zhen Yang, Xiaosong Jia, Xue Yang, Shaofeng Zhang, Yanyong Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.04653v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://tom-zgt.github.io/VPT)  
  Keywords: benchmark, denoising, diffusion model, dynamics, physical, physics, t2v, video diffusion  
- **[CineMobile: On-Device Image-to-Video Diffusion for Cinematic Camera Motion Generation](https://arxiv.org/abs/2607.03803v1)**  
  Authors: Xuyao Huang, Zelai Deng, Xu Wang, Xizhong Xiao, Zhijie Deng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.03803v1.pdf)  
  Keywords: architecture, denoising, diffusion transformer, distillation, dit, efficient, image-to-video, video diffusion, video generation  

### World Models & Simulation

*Showing the latest 50 out of 381 papers*

- **[From Pixels to States: Rethinking Interactive World Models as Game Engines](https://arxiv.org/abs/2607.14076v1)**  
  Authors: Zhen Li, Zian Meng, Shuwei Shi, Mingliang Zhai, Jiaming Tan, Chuanhao Li, Kaipeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.14076v1.pdf)  
  Keywords: dit, dynamics, interactive, world model  
- **[The Seriality Gap in Video Diffusion Models](https://arxiv.org/abs/2607.13031v1)**  
  Authors: Jorge Diaz Chao, Konpat Preechakul, Yuxi Liu, Yutong Bai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.13031v1.pdf)  
  Keywords: autoregressive, denoising, diffusion model, dynamics, simulation, video diffusion, video prediction  
- **[FlowWAM: Optical Flow as a Unified Action Representation for World Action Models](https://arxiv.org/abs/2607.13017v1)**  
  Authors: Yixiang Chen, Peiyan Li, Yuan Xu, Qisen Ma, Jiabing Yang, Kai Wang, Jianhua Yang, Dong An, He Guan, Gaoteng Liu, Jianlou Si, Jun Huang, Jing Liu, Nianfeng Liu, Yan Huang, Liang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.13017v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://flow-wam.github.io)  
  Keywords: trajectory, video generation, world model  
- **[SymbOmni: Evolving Agentic Omni Models via Symbolic Concept Learning](https://arxiv.org/abs/2607.12042v1)**  
  Authors: Jinxiu Liu, Jianru Li, Tanqing Kuang, Xuanming Liu, Kangfu Mei, Yandong Wen, Weiyang Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.12042v1.pdf)  
  Keywords: benchmark, concept, efficient, interactive, video synthesis  
- **[Cycle-World: Mitigating Error Accumulation in Long-term Video World Models via Reverse-Prediction Cycle Consistency](https://arxiv.org/abs/2607.11836v1)**  
  Authors: Zihan Su, Teng Hu, Jiangning Zhang, Ruiyan Wang, Ran Yi, Lizhuang Ma, Dacheng Tao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.11836v1.pdf)  
  Keywords: autoregressive, benchmark, diffusion model, efficient, temporal consistency, video generation, video synthesis, world model  
- **[ABot-3DWorld 0: A Universal World Model to Explore Any 3D Space](https://arxiv.org/abs/2607.11673v2)**  
  Authors: Mingchao Sun, Luyang Tang, Yu Liu, Xu Yan, Zhan Li, Yunwei Zhang, Fei Yu, Zengye Ge, Yumin Liu, Jiacheng Zhang, Yongchang Zhang, Jiawei Zhang, Zhicheng Liu, Zhongxu Sun, Tianjian Ouyang, Wenzheng Chen, Shixing Yang, Nianfei Fan, Guodong Sun, Huan Li, Zheng Zhou, Yongze Li, Yingliang Peng, Mengmeng Du, Yuan Liu, Haozhe Shi, Chunnuo Gong, Chengzhen Yu, Chunxue Jia, Yang Liu, Shiying Zeng, Junnan Lai, Hang Zhang, Ning Guo, Baoquan Chen, Mu Xu, Hongyu Pan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.11673v2.pdf)  
  Keywords: creative, efficient, trajectory, world model  
- **[Xiaomi-Robotics-U0: Unified Embodied Synthesis with World Foundation Model](https://arxiv.org/abs/2607.11643v1)**  
  Authors: Xinghang Li, Jun Guo, Qiwei Li, Long Qian, Hang Lai, Yueze Wang, Hongyu Yan, Jiahang Cao, Xi Chen, Jingen Qu, Jiaxi Song, Nan Sun, Hanye Zhao, Futeng Liu, Wanli Peng, Heyun Wang, Yunhong Wang, Caoyu Xia, Jack Zhao, Diyun Xiang, Hangjun Ye, Heng Qu, Huaping Liu, Jason Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.11643v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://robotics.xiaomi.com/xiaomi-robotics-u0.html)  
  Keywords: autoregressive, controllable, dit, dynamics, evaluation, robotics, video generation, world model  
- **[Is Energy Guidance All You Need? Training-Free Norm Injection for Driving World Models](https://arxiv.org/abs/2607.10781v1)**  
  Authors: Xiyan Su, Frank Diermeyer, Markus Lienkamp  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.10781v1.pdf)  
  Keywords: controllable, dit, layout, trajectory, world model  
- **[Unlocking Temporal Generalization in Hamiltonian Video Dynamics Models](https://arxiv.org/abs/2607.07763v1)**  
  Authors: Eli Laird, Corey Clark  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.07763v1.pdf)  
  Keywords: dynamics, physical, video generation, world model  
- **[Validate the Dream Before You Trust Its Verdict: Admissibility for World-Model Simulators](https://arxiv.org/abs/2607.07196v1)**  
  Authors: Christian Oefinger, Finn Rasmus Schäfer, Korbinian Moller, Mattia Piccinini, Johannes Betz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2607.07196v1.pdf)  
  Keywords: autonomous driving, dit, robotics, simulation, world model  



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
