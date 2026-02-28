# Awesome Video Diffusions [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Video Diffusion Models and Video Generation. Content is automatically updated daily.

> Last Update: 2026-02-28 01:55:38

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
- [Applications](#applications) (58 papers) - Domain-specific applications of video diffusion models
- [Architecture & Efficiency](#architecture-&-efficiency) (368 papers) - Architectural innovations (DiT, UNet), flow matching, and training/inference efficiency
- [Audio & Multi-modal](#audio-&-multi-modal) (36 papers) - Audio-driven and multi-modal conditioned video generation
- [Controllable Generation](#controllable-generation) (119 papers) - Controllable video generation with motion, camera, pose, or layout guidance
- [Human & Character Animation](#human-&-character-animation) (33 papers) - Human-centric video generation including talking heads, dance, and character animation
- [Image-to-Video Generation](#image-to-video-generation) (43 papers) - Methods for animating still images into videos
- [Long Video Generation](#long-video-generation) (123 papers) - Generating temporally consistent long-form videos beyond short clips
- [Personalization & Customization](#personalization-&-customization) (91 papers) - Personalized video generation with custom subjects, identities, or styles
- [Physical Understanding](#physical-understanding) (129 papers) - Physics-aware video generation and dynamics modeling
- [Surveys & Benchmarks](#surveys-&-benchmarks) (194 papers) - Survey papers, benchmarks, and evaluation metrics for video generation
- [Text-to-Video Generation](#text-to-video-generation) (70 papers) - Foundation models and methods for generating videos from text prompts
- [Video Editing](#video-editing) (40 papers) - Diffusion-based video editing, style transfer, and manipulation
- [Video Inpainting & Completion](#video-inpainting-&-completion) (7 papers) - Video inpainting, completion, outpainting, and temporal prediction
- [Video Super-Resolution & Enhancement](#video-super-resolution-&-enhancement) (57 papers) - Video quality improvement, upscaling, restoration, and frame interpolation
- [World Models & Simulation](#world-models-&-simulation) (100 papers) - Video generation as world simulators and interactive environment generation



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3D-aware Video Generation

- **[BetterScene: 3D Scene Synthesis with Representation-Aligned Generative Model](https://arxiv.org/abs/2602.22596v1)**  
  Authors: Yuci Han, Charles Toth, John E. Anderson, William J. Shuart, Alper Yilmaz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.22596v1.pdf)  
  Keywords: dit, novel view, video diffusion, diffusion model  
- **[Geometry-as-context: Modulating Explicit 3D in Scene-consistent Video Generation to Geometry Context](https://arxiv.org/abs/2602.21929v1)**  
  Authors: JiaKui Hu, Jialun Liu, Liying Yang, Xinliang Zhang, Kaiwen Li, Shuang Zeng, Yuanwei Li, Haibin Huang, Chi Zhang, Yanye Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21929v1.pdf)  
  Keywords: video generation, autoregressive, novel view, camera control, trajectory  
- **[RAYNOVA: Scale-Temporal Autoregressive World Modeling in Ray Space](https://arxiv.org/abs/2602.20685v2)**  
  Authors: Yichen Xie, Chensheng Peng, Mazen Abdelfattah, Yihan Hu, Jiezhi Yang, Eric Higgins, Ryan Brigden, Masayoshi Tomizuka, Wei Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20685v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://raynova-ai.github.io)  
  Keywords: video generation, multi-view video, dit, autoregressive, novel view, physical, world model  
- **[A Single Image and Multimodality Is All You Need for Novel View Synthesis](https://arxiv.org/abs/2602.17909v1)**  
  Authors: Amirhosein Javadi, Chi-Shiang Gau, Konstantinos D. Polyzos, Tara Javidi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.17909v1.pdf)  
  Keywords: efficient, novel view, video generation, dit  
- **[VideoNeuMat: Neural Material Extraction from Generative Video Models](https://arxiv.org/abs/2602.07272v1)**  
  Authors: Bowen Xue, Saeed Hadadan, Zheng Zeng, Fabrice Rousselle, Zahra Montazeri, Milos Hasan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.07272v1.pdf)  
  Keywords: dit, novel view, video diffusion, diffusion model  
- **[CineScene: Implicit 3D as Effective Scene Representation for Cinematic Video Generation](https://arxiv.org/abs/2602.06959v1)**  
  Authors: Kaiyi Huang, Yukun Huang, Yu Li, Jianhong Bai, Xintao Wang, Zinan Lin, Xuefei Ning, Jiwen Yu, Pengfei Wan, Yu Wang, Xihui Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06959v1.pdf)  
  Keywords: video generation, 3d-aware, text-to-video, video synthesis, dit, physical, trajectory  
- **[SkeletonGaussian: Editable 4D Generation through Gaussian Skeletonization](https://arxiv.org/abs/2602.04271v1)**  
  Authors: Lifan Wu, Ruijie Zhu, Yubo Ai, Tianzhu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.04271v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wusar.github.io/projects/skeletongaussian)  
  Keywords: dit, 4d generation  
- **[3D-Aware Implicit Motion Control for View-Adaptive Human Video Generation](https://arxiv.org/abs/2602.03796v2)**  
  Authors: Zhixue Fang, Xu He, Songlin Tang, Haoxian Zhang, Qingfeng Li, Xiaoqiang Liu, Pengfei Wan, Kun Gai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03796v2.pdf)  
  Keywords: dynamics, video generation, 3d-aware, human motion, motion control, dit, camera control  
- **[FreeFix: Boosting 3D Gaussian Splatting via Fine-Tuning-Free Diffusion Models](https://arxiv.org/abs/2601.20857v1)**  
  Authors: Hongyu Zhou, Zisen Shao, Sheng Miao, Pan Wang, Dongfeng Bai, Bingbing Liu, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.20857v1.pdf)  
  Keywords: dit, novel view, video diffusion, diffusion model  
- **[AnyView: Synthesizing Any Novel View in Dynamic Scenes](https://arxiv.org/abs/2601.16982v1)**  
  Authors: Basile Van Hoorick, Dian Chen, Shun Iwase, Pavel Tokmakov, Muhammad Zubair Irshad, Igor Vasiljevic, Swati Gupta, Fangzhou Cheng, Sergey Zakharov, Vitor Campagnolo Guizilini  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.16982v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://tri-ml.github.io/AnyView)  
  Keywords: benchmark, novel view, video generation, temporal consistency  

### Applications

*Showing the latest 50 out of 58 papers*

- **[HorizonForge: Driving Scene Editing with Any Trajectories and Any Vehicles](https://arxiv.org/abs/2602.21333v1)**  
  Authors: Yifan Wang, Francesco Pittaluga, Zaid Tasneem, Chenyu You, Manmohan Chandraker, Ziyu Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21333v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://horizonforge.github.io)  
  Keywords: autonomous driving, video diffusion, benchmark, temporal consistency, dit, evaluation, simulation, trajectory, controllable  
- **[GA-Drive: Geometry-Appearance Decoupled Modeling for Free-viewpoint Driving Scene Generatio](https://arxiv.org/abs/2602.20673v1)**  
  Authors: Hao Zhang, Lue Fan, Qitai Wang, Wenbo Li, Zehuan Wu, Lewei Lu, Zhaoxiang Zhang, Hongsheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20673v1.pdf)  
  Keywords: diffusion model, autonomous driving, video diffusion, video editing, dit, video-to-video, simulation, trajectory  
- **[3DSPA: A 3D Semantic Point Autoencoder for Evaluating Video Realism](https://arxiv.org/abs/2602.20354v1)**  
  Authors: Bhavik Chandna, Kelsey R. Allen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20354v1.pdf) | [![GitHub](https://img.shields.io/github/stars/TheProParadox/3dspa_code?style=social)](https://github.com/TheProParadox/3dspa_code)  
  Keywords: film, video generation, robotics, benchmark, temporal consistency, evaluation, physical, trajectory  
- **[PedaCo-Gen: Scaffolding Pedagogical Agency in Human-AI Collaborative Video Authoring](https://arxiv.org/abs/2602.19623v1)**  
  Authors: Injun Baek, Yearim Kim, Nojun Kwak  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.19623v1.pdf)  
  Keywords: interactive, education, text-to-video, t2v, dit  
- **[VideoSketcher: Video Models Prior Enable Versatile Sequential Sketch Generation](https://arxiv.org/abs/2602.15819v1)**  
  Authors: Hui Ren, Yuval Alaluf, Omer Bar Tal, Alexander Schwing, Antonio Torralba, Yael Vinker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.15819v1.pdf)  
  Keywords: interactive, diffusion model, text-to-video, efficient, style, video diffusion, dit, autoregressive, creative  
- **[Beyond End-to-End Video Models: An LLM-Based Multi-Agent System for Educational Video Generation](https://arxiv.org/abs/2602.11790v1)**  
  Authors: Lingyong Yan, Jiulong Wu, Dong Xie, Weixian Shi, Deguo Xia, Jizhou Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.11790v1.pdf)  
  Keywords: dit, education, video generation  
- **[Ctrl&Shift: High-Quality Geometry-Aware Object Manipulation in Visual Generation](https://arxiv.org/abs/2602.11440v1)**  
  Authors: Penghui Ruan, Bojia Zi, Xianbiao Qi, Youze Huang, Rong Xiao, Pichao Wang, Jiannong Cao, Yuhui Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.11440v1.pdf)  
  Keywords: film, dit, identity, creative, controllable  
- **[VideoWorld 2: Learning Transferable Knowledge from Real-world Videos](https://arxiv.org/abs/2602.10102v1)**  
  Authors: Zhongwei Ren, Yunchao Wei, Xiao Yu, Guixun Luo, Yao Zhao, Bingyi Kang, Jiashi Feng, Xiaojie Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.10102v1.pdf)  
  Keywords: dynamics, video generation, diffusion model, robotics, video diffusion, autoregressive  
- **[AUHead: Realistic Emotional Talking Head Generation via Action Units Control](https://arxiv.org/abs/2602.09534v1)**  
  Authors: Jiayi Lyu, Leigang Qu, Wenjing Zhang, Hanyu Jiang, Kai Liu, Zhenglin Zhou, Xiaobo Xia, Jian Xue, Tat-Seng Chua  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.09534v1.pdf) | [![GitHub](https://img.shields.io/github/stars/laura990501/AUHead_ICLR?style=social)](https://github.com/laura990501/AUHead_ICLR)  
  Keywords: interactive, video generation, diffusion model, film, talking head, avatar, benchmark, motion control, dit, identity, controllable  
- **[PISCO: Precise Video Instance Insertion with Sparse Control](https://arxiv.org/abs/2602.08277v1)**  
  Authors: Xiangbo Gao, Renjie Li, Xinghao Chen, Yuheng Wu, Suofei Feng, Qing Yin, Zhengzhong Tu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.08277v1.pdf)  
  Keywords: dynamics, film, video generation, diffusion model, video diffusion, benchmark, video editing, dit, physical, controllable  

### Architecture & Efficiency

*Showing the latest 50 out of 368 papers*

- **[ColoDiff: Integrating Dynamic Consistency With Content Awareness for Colonoscopy Video Generation](https://arxiv.org/abs/2602.23203v1)**  
  Authors: Junhu Fu, Shuyu Liang, Wutong Li, Chen Ma, Peng Huang, Kehao Wang, Ke Chen, Shengli Lin, Pinghong Zhou, Zeju Li, Yuanyuan Wang, Yi Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.23203v1.pdf)  
  Keywords: dynamics, video generation, diffusion model, temporal consistency, dit, controllable  
- **[Uni-Animator: Towards Unified Visual Colorization](https://arxiv.org/abs/2602.23191v1)**  
  Authors: Xinyuan Chen, Yao Xu, Shaowen Wang, Pengjie Song, Bowen Deng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.23191v1.pdf)  
  Keywords: temporal consistency, dit, diffusion transformer, physical  
- **[The Trinity of Consistency as a Defining Principle for General World Models](https://arxiv.org/abs/2602.23152v1)**  
  Authors: Jingxuan Wei, Siyuan Li, Yuhang Xu, Zheng Sun, Junjie Jiang, Hexuan Jin, Caijun Jia, Honghao He, Xinglong Xu, Xi bai, Chang Yu, Yumou Liu, Junnan Zhu, Xuanhe Zhou, Jintao Chen, Xiaobin Hu, Shancheng Pang, Bihui Yu, Ran He, Zhen Lei, Stan Z. Li, Conghui He, Shuicheng Yan, Cheng Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.23152v1.pdf)  
  Keywords: dynamics, video generation, physical, benchmark, temporal consistency, evaluation, world simulator, world model, architecture, concept, trajectory  
- **[UCM: Unifying Camera Control and Memory with Time-aware Positional Encoding Warping for World Models](https://arxiv.org/abs/2602.22960v1)**  
  Authors: Tianxing Xu, Zixuan Wang, Guangyuan Wang, Li Hu, Zhongyi Zhang, Peng Zhang, Bang Zhang, Song-Hai Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.22960v1.pdf)  
  Keywords: interactive, video generation, efficient, benchmark, diffusion transformer, camera control, world model  
- **[Denoising as Path Planning: Training-Free Acceleration of Diffusion Models with DPCache](https://arxiv.org/abs/2602.22654v1)**  
  Authors: Bowen Cui, Yuanbin Wang, Huajiang Xu, Biaolong Chen, Aixi Zhang, Hao Jiang, Zhengzheng Jin, Xu Liu, Pipei Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.22654v1.pdf) | [![GitHub](https://img.shields.io/github/stars/argsss/DPCache?style=social)](https://github.com/argsss/DPCache)  
  Keywords: video generation, diffusion model, efficient, denoising, dit, acceleration, trajectory  
- **[BetterScene: 3D Scene Synthesis with Representation-Aligned Generative Model](https://arxiv.org/abs/2602.22596v1)**  
  Authors: Yuci Han, Charles Toth, John E. Anderson, William J. Shuart, Alper Yilmaz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.22596v1.pdf)  
  Keywords: dit, novel view, video diffusion, diffusion model  
- **[Flow Matching is Adaptive to Manifold Structures](https://arxiv.org/abs/2602.22486v1)**  
  Authors: Shivam Kumar, Yixin Wang, Lizhen Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.22486v1.pdf)  
  Keywords: flow matching, simulation, video generation  
- **[Solaris: Building a Multiplayer Video World Model in Minecraft](https://arxiv.org/abs/2602.22208v2)**  
  Authors: Georgy Savva, Oscar Michel, Daohan Lu, Suppakit Waiwitlikhit, Timothy Meehan, Dhairya Mishra, Srivats Poddar, Jack Lu, Saining Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.22208v2.pdf)  
  Keywords: video generation, efficient, dit, evaluation, action-conditioned, architecture, world model  
- **[UniVBench: Towards Unified Evaluation for Video Foundation Models](https://arxiv.org/abs/2602.21835v1)**  
  Authors: Jianhui Wei, Xiaotian Zhang, Yichen Li, Yuan Wang, Yan Zhang, Ziyi Chen, Zhihang Tang, Wei Xu, Zuozhu Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21835v1.pdf)  
  Keywords: video generation, benchmark, dit, video editing, evaluation  
- **[SkyReels-V4: Multi-modal Video-Audio Generation, Inpainting and Editing model](https://arxiv.org/abs/2602.21818v2)**  
  Authors: Guibin Chen, Dixuan Lin, Jiangping Yang, Youqiang Zhang, Zhengcong Fei, Debang Li, Sheng Chen, Chaofeng Ao, Nuo Pang, Yiming Wang, Yikun Dou, Zheng Chen, Mingyuan Fan, Tuanhui Li, Mingshan Chang, Hao Zhang, Xiaopeng Sun, Jingtao Xu, Yuqiang Xie, Jiahua Wang, Zhiheng Xu, Weiming Xiong, Yuzhe Jin, Baoxuan Gu, Binjie Mao, Yunjie Yu, Jujie He, Yuhao Feng, Shiwen Tu, Chaojie Wang, Rui Yan, Wei Shen, Jingchen Wu, Peng Zhao, Xuanyue Zhong, Zhuangzhuang Liu, Kaifei Wang, Fuxiang Zhang, Weikai Xu, Wenyan Liu, Binglu Zhang, Yu Shen, Tianhui Xiong, Bin Peng, Liang Zeng, Xuchen Song, Haoxiang Guo, Peiyu Wang, Max W. Y. Lam, Chien-Hung Liu, Yahui Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21818v2.pdf)  
  Keywords: video generation, style, sound, image to video, video editing, dit, diffusion transformer, architecture, frame interpolation, multi-modal, super-resolution  

### Audio & Multi-modal

- **[SkyReels-V4: Multi-modal Video-Audio Generation, Inpainting and Editing model](https://arxiv.org/abs/2602.21818v2)**  
  Authors: Guibin Chen, Dixuan Lin, Jiangping Yang, Youqiang Zhang, Zhengcong Fei, Debang Li, Sheng Chen, Chaofeng Ao, Nuo Pang, Yiming Wang, Yikun Dou, Zheng Chen, Mingyuan Fan, Tuanhui Li, Mingshan Chang, Hao Zhang, Xiaopeng Sun, Jingtao Xu, Yuqiang Xie, Jiahua Wang, Zhiheng Xu, Weiming Xiong, Yuzhe Jin, Baoxuan Gu, Binjie Mao, Yunjie Yu, Jujie He, Yuhao Feng, Shiwen Tu, Chaojie Wang, Rui Yan, Wei Shen, Jingchen Wu, Peng Zhao, Xuanyue Zhong, Zhuangzhuang Liu, Kaifei Wang, Fuxiang Zhang, Weikai Xu, Wenyan Liu, Binglu Zhang, Yu Shen, Tianhui Xiong, Bin Peng, Liang Zeng, Xuchen Song, Haoxiang Guo, Peiyu Wang, Max W. Y. Lam, Chien-Hung Liu, Yahui Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21818v2.pdf)  
  Keywords: video generation, style, sound, image to video, video editing, dit, diffusion transformer, architecture, frame interpolation, multi-modal, super-resolution  
- **[JavisDiT++: Unified Modeling and Optimization for Joint Audio-Video Generation](https://arxiv.org/abs/2602.19163v1)**  
  Authors: Kai Liu, Yanhao Zheng, Kai Wang, Shengqiong Wu, Rongjunchen Zhang, Jiebo Luo, Dimitrios Hatzinakos, Ziwei Liu, Hao Fei, Tat-Seng Chua  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.19163v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://JavisVerse.github.io/JavisDiT2-page)  
  Keywords: video generation, t2v, sound, dit, evaluation  
- **[EchoTorrent: Towards Swift, Sustained, and Streaming Multi-Modal Video Generation](https://arxiv.org/abs/2602.13669v1)**  
  Authors: Rang Meng, Weipeng Wu, Yingjie Yin, Yuming Li, Chenguang Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.13669v1.pdf)  
  Keywords: video generation, streaming, temporal consistency, identity, autoregressive, multi-modal, architecture  
- **[DreamID-Omni: Unified Framework for Controllable Human-Centric Audio-Video Generation](https://arxiv.org/abs/2602.12160v1)**  
  Authors: Xu Guo, Fulong Ye, Qichao Sun, Liyang Chen, Bingchuan Li, Pengze Zhang, Jiawei Liu, Songtao Zhao, Qian He, Xiangwang Hou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.12160v1.pdf)  
  Keywords: video generation, video editing, dit, diffusion transformer, identity, audio-driven, controllable  
- **[TiFRe: Text-guided Video Frame Reduction for Efficient Video Multi-modal Large Language Models](https://arxiv.org/abs/2602.08861v1)**  
  Authors: Xiangtian Zheng, Zishuo Wang, Yuxin Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.08861v1.pdf)  
  Keywords: efficient, style, multi-modal  
- **[VideoVeritas: AI-Generated Video Detection via Perception Pretext Reinforcement Learning](https://arxiv.org/abs/2602.08828v1)**  
  Authors: Hao Tan, Jun Lan, Senyuan Shi, Zichang Tan, Zijian Yu, Huijia Zhu, Weiqiang Wang, Jun Wan, Zhen Lei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.08828v1.pdf)  
  Keywords: benchmark, evaluation, video generation, multi-modal  
- **[MOVA: Towards Scalable and Synchronized Video-Audio Generation](https://arxiv.org/abs/2602.08794v2)**  
  Authors: SII-OpenMOSS Team, :, Donghua Yu, Mingshu Chen, Qi Chen, Qi Luo, Qianyi Wu, Qinyuan Cheng, Ruixiao Li, Tianyi Liang, Wenbo Zhang, Wenming Tu, Xiangyu Peng, Yang Gao, Yanru Huo, Ying Zhu, Yinze Luo, Yiyang Zhang, Yuerong Song, Zhe Xu, Zhiyu Zhang, Chenchen Yang, Cheng Chang, Chushu Zhou, Hanfu Chen, Hongnan Ma, Jiaxi Li, Jingqi Tong, Junxi Liu, Ke Chen, Shimin Li, Shiqi Jiang, Songlin Wang, Wei Jiang, Zhaoye Fei, Zhiyuan Ning, Chunguo Li, Chenhui Li, Ziwei He, Zengfeng Huang, Xie Chen, Xipeng Qiu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.08794v2.pdf)  
  Keywords: efficient, t2v, sound, text to video, architecture  
- **[T2VTree: User-Centered Visual Analytics for Agent-Assisted Thought-to-Video Authoring](https://arxiv.org/abs/2602.08368v1)**  
  Authors: Zhuoyun Zheng, Yu Dong, Gaorong Liang, Guan Li, Guihua Shan, Shiyu Cheng, Dong Tian, Jianlong Zhou, Jie Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.08368v1.pdf) | [![GitHub](https://img.shields.io/github/stars/tezuka0210/T2VTree?style=social)](https://github.com/tezuka0210/T2VTree)  
  Keywords: dit, t2v, multi-modal, video generation  
- **[SoulX-FlashHead: Oracle-guided Generation of Infinite Real-time Streaming Talking Heads](https://arxiv.org/abs/2602.07449v3)**  
  Authors: Tan Yu, Qian Qiao, Le Shen, Ke Zhou, Jincheng Hu, Dian Sheng, Bo Hu, Haoming Qin, Jun Gao, Changhai Zhou, Shunshun Yin, Siyuan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.07449v3.pdf)  
  Keywords: video generation, streaming, talking head, distillation, benchmark, identity, autoregressive, audio-driven, physical  
- **[Meta Engine: A Unified Semantic Query Engine on Heterogeneous LLM-Based Query Systems](https://arxiv.org/abs/2602.01701v1)**  
  Authors: Ruyu Li, Tinghui Zhang, Haodi Ma, Daisy Zhe Wang, Yifan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.01701v1.pdf)  
  Keywords: architecture, dit, evaluation, multi-modal  

### Controllable Generation

*Showing the latest 50 out of 119 papers*

- **[ColoDiff: Integrating Dynamic Consistency With Content Awareness for Colonoscopy Video Generation](https://arxiv.org/abs/2602.23203v1)**  
  Authors: Junhu Fu, Shuyu Liang, Wutong Li, Chen Ma, Peng Huang, Kehao Wang, Ke Chen, Shengli Lin, Pinghong Zhou, Zeju Li, Yuanyuan Wang, Yi Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.23203v1.pdf)  
  Keywords: dynamics, video generation, diffusion model, temporal consistency, dit, controllable  
- **[The Trinity of Consistency as a Defining Principle for General World Models](https://arxiv.org/abs/2602.23152v1)**  
  Authors: Jingxuan Wei, Siyuan Li, Yuhang Xu, Zheng Sun, Junjie Jiang, Hexuan Jin, Caijun Jia, Honghao He, Xinglong Xu, Xi bai, Chang Yu, Yumou Liu, Junnan Zhu, Xuanhe Zhou, Jintao Chen, Xiaobin Hu, Shancheng Pang, Bihui Yu, Ran He, Zhen Lei, Stan Z. Li, Conghui He, Shuicheng Yan, Cheng Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.23152v1.pdf)  
  Keywords: dynamics, video generation, physical, benchmark, temporal consistency, evaluation, world simulator, world model, architecture, concept, trajectory  
- **[UCM: Unifying Camera Control and Memory with Time-aware Positional Encoding Warping for World Models](https://arxiv.org/abs/2602.22960v1)**  
  Authors: Tianxing Xu, Zixuan Wang, Guangyuan Wang, Li Hu, Zhongyi Zhang, Peng Zhang, Bang Zhang, Song-Hai Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.22960v1.pdf)  
  Keywords: interactive, video generation, efficient, benchmark, diffusion transformer, camera control, world model  
- **[Denoising as Path Planning: Training-Free Acceleration of Diffusion Models with DPCache](https://arxiv.org/abs/2602.22654v1)**  
  Authors: Bowen Cui, Yuanbin Wang, Huajiang Xu, Biaolong Chen, Aixi Zhang, Hao Jiang, Zhengzheng Jin, Xu Liu, Pipei Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.22654v1.pdf) | [![GitHub](https://img.shields.io/github/stars/argsss/DPCache?style=social)](https://github.com/argsss/DPCache)  
  Keywords: video generation, diffusion model, efficient, denoising, dit, acceleration, trajectory  
- **[Geometry-as-context: Modulating Explicit 3D in Scene-consistent Video Generation to Geometry Context](https://arxiv.org/abs/2602.21929v1)**  
  Authors: JiaKui Hu, Jialun Liu, Liying Yang, Xinliang Zhang, Kaiwen Li, Shuang Zeng, Yuanwei Li, Haibin Huang, Chi Zhang, Yanye Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21929v1.pdf)  
  Keywords: video generation, autoregressive, novel view, camera control, trajectory  
- **[MultiAnimate: Pose-Guided Image Animation Made Extensible](https://arxiv.org/abs/2602.21581v1)**  
  Authors: Yingcheng Hu, Haowen Gong, Chuanguang Yang, Zhulin An, Yongjun Xu, Songhua Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21581v1.pdf)  
  Keywords: image animation, video generation, dit, diffusion transformer, identity, pose-guided  
- **[Towards Controllable Video Synthesis of Routine and Rare OR Events](https://arxiv.org/abs/2602.21365v1)**  
  Authors: Dominik Schneider, Lalithkumar Seenivasan, Sampath Rapuri, Vishalroshan Anil, Aiza Maksutova, Yiqing Shen, Jan Emily Mangulabnan, Hao Ding, Jose L. Porras, Masaru Ishii, Mathias Unberath  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21365v1.pdf)  
  Keywords: diffusion model, video diffusion, video synthesis, dit, controllable  
- **[HorizonForge: Driving Scene Editing with Any Trajectories and Any Vehicles](https://arxiv.org/abs/2602.21333v1)**  
  Authors: Yifan Wang, Francesco Pittaluga, Zaid Tasneem, Chenyu You, Manmohan Chandraker, Ziyu Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21333v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://horizonforge.github.io)  
  Keywords: autonomous driving, video diffusion, benchmark, temporal consistency, dit, evaluation, simulation, trajectory, controllable  
- **[GA-Drive: Geometry-Appearance Decoupled Modeling for Free-viewpoint Driving Scene Generatio](https://arxiv.org/abs/2602.20673v1)**  
  Authors: Hao Zhang, Lue Fan, Qitai Wang, Wenbo Li, Zehuan Wu, Lewei Lu, Zhaoxiang Zhang, Hongsheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20673v1.pdf)  
  Keywords: diffusion model, autonomous driving, video diffusion, video editing, dit, video-to-video, simulation, trajectory  
- **[3DSPA: A 3D Semantic Point Autoencoder for Evaluating Video Realism](https://arxiv.org/abs/2602.20354v1)**  
  Authors: Bhavik Chandna, Kelsey R. Allen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20354v1.pdf) | [![GitHub](https://img.shields.io/github/stars/TheProParadox/3dspa_code?style=social)](https://github.com/TheProParadox/3dspa_code)  
  Keywords: film, video generation, robotics, benchmark, temporal consistency, evaluation, physical, trajectory  

### Human & Character Animation

- **[BigMaQ: A Big Macaque Motion and Animation Dataset Bridging Image and 3D Pose Representations](https://arxiv.org/abs/2602.19874v1)**  
  Authors: Lucas Martini, Alexander Lappe, Anna Bognár, Rufin Vogels, Martin A. Giese  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.19874v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://martinivis.github.io/BigMaQ)  
  Keywords: benchmark, dynamics, avatar  
- **[Ani3DHuman: Photorealistic 3D Human Animation with Self-guided Stochastic Sampling](https://arxiv.org/abs/2602.19089v1)**  
  Authors: Qi Sun, Can Wang, Jiaxiang Shang, Yingchun Liu, Jing Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.19089v1.pdf) | [![GitHub](https://img.shields.io/github/stars/qiisun/ani3dhuman?style=social)](https://github.com/qiisun/ani3dhuman)  
  Keywords: dynamics, diffusion model, human animation, video diffusion, identity  
- **[HairWeaver: Few-Shot Photorealistic Hair Motion Synthesis with Sim-to-Real Guided Video Diffusion](https://arxiv.org/abs/2602.11117v1)**  
  Authors: Di Chang, Ji Hou, Aljaz Bozic, Assaf Neuberger, Felix Juefei-Xu, Olivier Maury, Gene Wei-Chin Lin, Tuur Stuyck, Doug Roble, Mohammad Soleymani, Stephane Grabli  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.11117v1.pdf)  
  Keywords: dynamics, human motion, video diffusion, dit, evaluation  
- **[Hand2World: Autoregressive Egocentric Interaction Generation via Free-Space Hand Gestures](https://arxiv.org/abs/2602.09600v2)**  
  Authors: Yuxi Wang, Wenqi Ouyang, Tianyi Wei, Yi Dong, Zhiqi Shen, Xingang Pan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.09600v2.pdf)  
  Keywords: dynamics, interactive, video generation, diffusion model, benchmark, dit, world model, autoregressive, camera control, gesture  
- **[AUHead: Realistic Emotional Talking Head Generation via Action Units Control](https://arxiv.org/abs/2602.09534v1)**  
  Authors: Jiayi Lyu, Leigang Qu, Wenjing Zhang, Hanyu Jiang, Kai Liu, Zhenglin Zhou, Xiaobo Xia, Jian Xue, Tat-Seng Chua  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.09534v1.pdf) | [![GitHub](https://img.shields.io/github/stars/laura990501/AUHead_ICLR?style=social)](https://github.com/laura990501/AUHead_ICLR)  
  Keywords: interactive, video generation, diffusion model, film, talking head, avatar, benchmark, motion control, dit, identity, controllable  
- **[SoulX-FlashHead: Oracle-guided Generation of Infinite Real-time Streaming Talking Heads](https://arxiv.org/abs/2602.07449v3)**  
  Authors: Tan Yu, Qian Qiao, Le Shen, Ke Zhou, Jincheng Hu, Dian Sheng, Bo Hu, Haoming Qin, Jun Gao, Changhai Zhou, Shunshun Yin, Siyuan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.07449v3.pdf)  
  Keywords: video generation, streaming, talking head, distillation, benchmark, identity, autoregressive, audio-driven, physical  
- **[From Blurry to Believable: Enhancing Low-quality Talking Heads with 3D Generative Priors](https://arxiv.org/abs/2602.06122v1)**  
  Authors: Ding-Jiun Huang, Yuanhao Wang, Shao-Ji Yuan, Albert Mosella-Montoro, Francisco Vicente Carrasco, Cheng Zhang, Fernando De la Torre  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06122v1.pdf)  
  Keywords: dynamics, talking head, avatar, temporal consistency, identity, super-resolution  
- **[ShapeGaussian: High-Fidelity 4D Human Reconstruction in Monocular Videos via Vision Priors](https://arxiv.org/abs/2602.05572v1)**  
  Authors: Zhenxiao Liang, Ning Zhang, Youbao Tang, Ruei-Sung Lin, Qixing Huang, Peng Chang, Jing Xiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.05572v1.pdf)  
  Keywords: human motion  
- **[3D-Aware Implicit Motion Control for View-Adaptive Human Video Generation](https://arxiv.org/abs/2602.03796v2)**  
  Authors: Zhixue Fang, Xu He, Songlin Tang, Haoxian Zhang, Qingfeng Li, Xiaoqiang Liu, Pengfei Wan, Kun Gai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03796v2.pdf)  
  Keywords: dynamics, video generation, 3d-aware, human motion, motion control, dit, camera control  
- **[VRGaussianAvatar: Integrating 3D Gaussian Avatars into VR](https://arxiv.org/abs/2602.01674v1)**  
  Authors: Hail Song, Boram Yoon, Seokhwan Yang, Seoyoung Kang, Hyunjeong Kim, Henning Metzmacher, Woontack Woo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.01674v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vrgaussianavatar.github.io)  
  Keywords: interactive, avatar  

### Image-to-Video Generation

- **[SkyReels-V4: Multi-modal Video-Audio Generation, Inpainting and Editing model](https://arxiv.org/abs/2602.21818v2)**  
  Authors: Guibin Chen, Dixuan Lin, Jiangping Yang, Youqiang Zhang, Zhengcong Fei, Debang Li, Sheng Chen, Chaofeng Ao, Nuo Pang, Yiming Wang, Yikun Dou, Zheng Chen, Mingyuan Fan, Tuanhui Li, Mingshan Chang, Hao Zhang, Xiaopeng Sun, Jingtao Xu, Yuqiang Xie, Jiahua Wang, Zhiheng Xu, Weiming Xiong, Yuzhe Jin, Baoxuan Gu, Binjie Mao, Yunjie Yu, Jujie He, Yuhao Feng, Shiwen Tu, Chaojie Wang, Rui Yan, Wei Shen, Jingchen Wu, Peng Zhao, Xuanyue Zhong, Zhuangzhuang Liu, Kaifei Wang, Fuxiang Zhang, Weikai Xu, Wenyan Liu, Binglu Zhang, Yu Shen, Tianhui Xiong, Bin Peng, Liang Zeng, Xuchen Song, Haoxiang Guo, Peiyu Wang, Max W. Y. Lam, Chien-Hung Liu, Yahui Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21818v2.pdf)  
  Keywords: video generation, style, sound, image to video, video editing, dit, diffusion transformer, architecture, frame interpolation, multi-modal, super-resolution  
- **[MultiAnimate: Pose-Guided Image Animation Made Extensible](https://arxiv.org/abs/2602.21581v1)**  
  Authors: Yingcheng Hu, Haowen Gong, Chuanguang Yang, Zhulin An, Yongjun Xu, Songhua Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21581v1.pdf)  
  Keywords: image animation, video generation, dit, diffusion transformer, identity, pose-guided  
- **[Human Video Generation from a Single Image with 3D Pose and View Control](https://arxiv.org/abs/2602.21188v1)**  
  Authors: Tiantian Wang, Chun-Han Yao, Tao Hu, Mallikarjun Byrasandra Ramalinga Reddy, Ming-Hsuan Yang, Varun Jampani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21188v1.pdf)  
  Keywords: video generation, image-to-video, diffusion model, video diffusion, video synthesis, latent video  
- **[VII: Visual Instruction Injection for Jailbreaking Image-to-Video Generation Models](https://arxiv.org/abs/2602.20999v1)**  
  Authors: Bowen Zheng, Yongli Xiang, Ziming Hong, Zerong Lin, Chaojian Yu, Tongliang Liu, Xinge You  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20999v1.pdf)  
  Keywords: i2v, video generation, image-to-video, dit  
- **[AnimeAgent: Is the Multi-Agent via Image-to-Video models a Good Disney Storytelling Artist?](https://arxiv.org/abs/2602.20664v1)**  
  Authors: Hailong Yan, Shice Liu, Tao Wang, Xiangtao Zhang, Yijie Zhong, Jinwei Chen, Le Zhang, Bo Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20664v1.pdf)  
  Keywords: benchmark, i2v, image-to-video, diffusion model  
- **[Frame2Freq: Spectral Adapters for Fine-Grained Video Understanding](https://arxiv.org/abs/2602.18977v1)**  
  Authors: Thinesh Thiyakesan Ponbagavathi, Constantin Seibold, Alina Roitberg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.18977v1.pdf) | [![GitHub](https://img.shields.io/github/stars/th-nesh/Frame2Freq?style=social)](https://github.com/th-nesh/Frame2Freq)  
  Keywords: dynamics, image-to-video  
- **[FlexAM: Flexible Appearance-Motion Decomposition for Versatile Video Generation Control](https://arxiv.org/abs/2602.13185v1)**  
  Authors: Mingzhi Sheng, Zekai Gu, Peng Li, Cheng Lin, Hao-Xiang Guo, Ying-Cong Chen, Yuan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.13185v1.pdf)  
  Keywords: dynamics, video generation, dit, i2v, camera control  
- **[Motion Prior Distillation in Time Reversal Sampling for Generative Inbetweening](https://arxiv.org/abs/2602.12679v2)**  
  Authors: Wooseok Jeon, Seunghyun Shin, Dongmin Shin, Hae-Gon Jeon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.12679v2.pdf)  
  Keywords: image-to-video, diffusion model, denoising, distillation, benchmark, dit, evaluation, i2v  
- **[ConsID-Gen: View-Consistent and Identity-Preserving Image-to-Video Generation](https://arxiv.org/abs/2602.10113v1)**  
  Authors: Mingyang Wu, Ashirbad Mishra, Soumik Dey, Shuo Xing, Naveen Ravipati, Hansi Wu, Binbin Li, Zhengzhong Tu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.10113v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://myangwu.github.io/ConsID-Gen)  
  Keywords: video generation, image-to-video, text-to-video, benchmark, dit, diffusion transformer, evaluation, i2v, identity  
- **[Monocular Normal Estimation via Shading Sequence Estimation](https://arxiv.org/abs/2602.09929v3)**  
  Authors: Zongrui Li, Xinhua Ma, Minghui Hu, Yunqing Zhao, Yingchen Yu, Qian Zheng, Chang Liu, Xudong Jiang, Song Bai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.09929v3.pdf)  
  Keywords: benchmark, dit, image-to-video  

### Long Video Generation

*Showing the latest 50 out of 123 papers*

- **[ColoDiff: Integrating Dynamic Consistency With Content Awareness for Colonoscopy Video Generation](https://arxiv.org/abs/2602.23203v1)**  
  Authors: Junhu Fu, Shuyu Liang, Wutong Li, Chen Ma, Peng Huang, Kehao Wang, Ke Chen, Shengli Lin, Pinghong Zhou, Zeju Li, Yuanyuan Wang, Yi Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.23203v1.pdf)  
  Keywords: dynamics, video generation, diffusion model, temporal consistency, dit, controllable  
- **[Uni-Animator: Towards Unified Visual Colorization](https://arxiv.org/abs/2602.23191v1)**  
  Authors: Xinyuan Chen, Yao Xu, Shaowen Wang, Pengjie Song, Bowen Deng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.23191v1.pdf)  
  Keywords: temporal consistency, dit, diffusion transformer, physical  
- **[The Trinity of Consistency as a Defining Principle for General World Models](https://arxiv.org/abs/2602.23152v1)**  
  Authors: Jingxuan Wei, Siyuan Li, Yuhang Xu, Zheng Sun, Junjie Jiang, Hexuan Jin, Caijun Jia, Honghao He, Xinglong Xu, Xi bai, Chang Yu, Yumou Liu, Junnan Zhu, Xuanhe Zhou, Jintao Chen, Xiaobin Hu, Shancheng Pang, Bihui Yu, Ran He, Zhen Lei, Stan Z. Li, Conghui He, Shuicheng Yan, Cheng Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.23152v1.pdf)  
  Keywords: dynamics, video generation, physical, benchmark, temporal consistency, evaluation, world simulator, world model, architecture, concept, trajectory  
- **[Geometry-as-context: Modulating Explicit 3D in Scene-consistent Video Generation to Geometry Context](https://arxiv.org/abs/2602.21929v1)**  
  Authors: JiaKui Hu, Jialun Liu, Liying Yang, Xinliang Zhang, Kaiwen Li, Shuang Zeng, Yuanwei Li, Haibin Huang, Chi Zhang, Yanye Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21929v1.pdf)  
  Keywords: video generation, autoregressive, novel view, camera control, trajectory  
- **[HorizonForge: Driving Scene Editing with Any Trajectories and Any Vehicles](https://arxiv.org/abs/2602.21333v1)**  
  Authors: Yifan Wang, Francesco Pittaluga, Zaid Tasneem, Chenyu You, Manmohan Chandraker, Ziyu Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21333v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://horizonforge.github.io)  
  Keywords: autonomous driving, video diffusion, benchmark, temporal consistency, dit, evaluation, simulation, trajectory, controllable  
- **[RAYNOVA: Scale-Temporal Autoregressive World Modeling in Ray Space](https://arxiv.org/abs/2602.20685v2)**  
  Authors: Yichen Xie, Chensheng Peng, Mazen Abdelfattah, Yihan Hu, Jiezhi Yang, Eric Higgins, Ryan Brigden, Masayoshi Tomizuka, Wei Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20685v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://raynova-ai.github.io)  
  Keywords: video generation, multi-view video, dit, autoregressive, novel view, physical, world model  
- **[3DSPA: A 3D Semantic Point Autoencoder for Evaluating Video Realism](https://arxiv.org/abs/2602.20354v1)**  
  Authors: Bhavik Chandna, Kelsey R. Allen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20354v1.pdf) | [![GitHub](https://img.shields.io/github/stars/TheProParadox/3dspa_code?style=social)](https://github.com/TheProParadox/3dspa_code)  
  Keywords: film, video generation, robotics, benchmark, temporal consistency, evaluation, physical, trajectory  
- **[VideoSketcher: Video Models Prior Enable Versatile Sequential Sketch Generation](https://arxiv.org/abs/2602.15819v1)**  
  Authors: Hui Ren, Yuval Alaluf, Omer Bar Tal, Alexander Schwing, Antonio Torralba, Yael Vinker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.15819v1.pdf)  
  Keywords: interactive, diffusion model, text-to-video, efficient, style, video diffusion, dit, autoregressive, creative  
- **[World Action Models are Zero-shot Policies](https://arxiv.org/abs/2602.15922v1)**  
  Authors: Seonghyeon Ye, Yunhao Ge, Kaiyuan Zheng, Shenyuan Gao, Sihyun Yu, George Kurian, Suneel Indupuru, You Liang Tan, Chuning Zhu, Jiannan Xiang, Ayaan Malik, Kyungmin Lee, William Liang, Nadun Ranawaka, Jiasheng Gu, Yinzhen Xu, Guanzhi Wang, Fengyuan Hu, Avnish Narayan, Johan Bjorck, Jing Wang, Gwanghyun Kim, Dantong Niu, Ruijie Zheng, Yuqi Xie, Jimmy Wu, Qi Wang, Ryan Julian, Danfei Xu, Yilun Du, Yevgen Chebotar, Scott Reed, Jan Kautz, Yuke Zhu, Linxi "Jim" Fan, Joel Jang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.15922v1.pdf)  
  Keywords: dynamics, diffusion model, video diffusion, autoregressive, physical  
- **[Consistency-Preserving Diverse Video Generation](https://arxiv.org/abs/2602.15287v1)**  
  Authors: Xinshuang Liu, Runfa Blark Li, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.15287v1.pdf)  
  Keywords: temporal consistency, text-to-video, video generation  

### Personalization & Customization

*Showing the latest 50 out of 91 papers*

- **[The Trinity of Consistency as a Defining Principle for General World Models](https://arxiv.org/abs/2602.23152v1)**  
  Authors: Jingxuan Wei, Siyuan Li, Yuhang Xu, Zheng Sun, Junjie Jiang, Hexuan Jin, Caijun Jia, Honghao He, Xinglong Xu, Xi bai, Chang Yu, Yumou Liu, Junnan Zhu, Xuanhe Zhou, Jintao Chen, Xiaobin Hu, Shancheng Pang, Bihui Yu, Ran He, Zhen Lei, Stan Z. Li, Conghui He, Shuicheng Yan, Cheng Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.23152v1.pdf)  
  Keywords: dynamics, video generation, physical, benchmark, temporal consistency, evaluation, world simulator, world model, architecture, concept, trajectory  
- **[SkyReels-V4: Multi-modal Video-Audio Generation, Inpainting and Editing model](https://arxiv.org/abs/2602.21818v2)**  
  Authors: Guibin Chen, Dixuan Lin, Jiangping Yang, Youqiang Zhang, Zhengcong Fei, Debang Li, Sheng Chen, Chaofeng Ao, Nuo Pang, Yiming Wang, Yikun Dou, Zheng Chen, Mingyuan Fan, Tuanhui Li, Mingshan Chang, Hao Zhang, Xiaopeng Sun, Jingtao Xu, Yuqiang Xie, Jiahua Wang, Zhiheng Xu, Weiming Xiong, Yuzhe Jin, Baoxuan Gu, Binjie Mao, Yunjie Yu, Jujie He, Yuhao Feng, Shiwen Tu, Chaojie Wang, Rui Yan, Wei Shen, Jingchen Wu, Peng Zhao, Xuanyue Zhong, Zhuangzhuang Liu, Kaifei Wang, Fuxiang Zhang, Weikai Xu, Wenyan Liu, Binglu Zhang, Yu Shen, Tianhui Xiong, Bin Peng, Liang Zeng, Xuchen Song, Haoxiang Guo, Peiyu Wang, Max W. Y. Lam, Chien-Hung Liu, Yahui Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21818v2.pdf)  
  Keywords: video generation, style, sound, image to video, video editing, dit, diffusion transformer, architecture, frame interpolation, multi-modal, super-resolution  
- **[MultiAnimate: Pose-Guided Image Animation Made Extensible](https://arxiv.org/abs/2602.21581v1)**  
  Authors: Yingcheng Hu, Haowen Gong, Chuanguang Yang, Zhulin An, Yongjun Xu, Songhua Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21581v1.pdf)  
  Keywords: image animation, video generation, dit, diffusion transformer, identity, pose-guided  
- **[Hierarchic-EEG2Text: Assessing EEG-To-Text Decoding across Hierarchical Abstraction Levels](https://arxiv.org/abs/2602.20932v1)**  
  Authors: Anupam Sharma, Harish Katti, Prajwal Singh, Shanmuganathan Raman, Krishna Miyapuram  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20932v1.pdf)  
  Keywords: architecture, dynamics, concept  
- **[Ani3DHuman: Photorealistic 3D Human Animation with Self-guided Stochastic Sampling](https://arxiv.org/abs/2602.19089v1)**  
  Authors: Qi Sun, Can Wang, Jiaxiang Shang, Yingchun Liu, Jing Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.19089v1.pdf) | [![GitHub](https://img.shields.io/github/stars/qiisun/ani3dhuman?style=social)](https://github.com/qiisun/ani3dhuman)  
  Keywords: dynamics, diffusion model, human animation, video diffusion, identity  
- **[EA-Swin: An Embedding-Agnostic Swin Transformer for AI-Generated Video Detection](https://arxiv.org/abs/2602.17260v1)**  
  Authors: Hung Mai, Loi Dinh, Duc Hai Nguyen, Dat Do, Luong Doan, Khanh Nguyen Quoc, Huan Vu, Phong Ho, Naeem Ul Islam, Tuan Do  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.17260v1.pdf)  
  Keywords: benchmark, style, evaluation  
- **[Xray-Visual Models: Scaling Vision models on Industry Scale Data](https://arxiv.org/abs/2602.16918v1)**  
  Authors: Shlok Mishra, Tsung-Yu Lin, Linda Wang, Hongli Xu, Yimin Liu, Michael Hsu, Chaitanya Ahuja, Hao Yuan, Jianpeng Cheng, Hong-You Chen, Haoyuan Xu, Chao Li, Abhijeet Awasthi, Jihye Moon, Don Husa, Michael Ge, Sumedha Singla, Arkabandhu Chowdhury, Phong Dingh, Satya Narayan Shukla, Yonghuan Yang, David Jacobs, Qi Guo, Jun Xiao, Xiangjun Fan, Aashu Singh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.16918v1.pdf)  
  Keywords: benchmark, efficient, style, architecture  
- **[VideoSketcher: Video Models Prior Enable Versatile Sequential Sketch Generation](https://arxiv.org/abs/2602.15819v1)**  
  Authors: Hui Ren, Yuval Alaluf, Omer Bar Tal, Alexander Schwing, Antonio Torralba, Yael Vinker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.15819v1.pdf)  
  Keywords: interactive, diffusion model, text-to-video, efficient, style, video diffusion, dit, autoregressive, creative  
- **[EchoTorrent: Towards Swift, Sustained, and Streaming Multi-Modal Video Generation](https://arxiv.org/abs/2602.13669v1)**  
  Authors: Rang Meng, Weipeng Wu, Yingjie Yin, Yuming Li, Chenguang Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.13669v1.pdf)  
  Keywords: video generation, streaming, temporal consistency, identity, autoregressive, multi-modal, architecture  
- **[DCDM: Divide-and-Conquer Diffusion Models for Consistency-Preserving Video Generation](https://arxiv.org/abs/2602.13637v1)**  
  Authors: Haoyu Zhao, Yuang Zhang, Junqi Cheng, Jiaxi Gu, Zenghui Lu, Peng Shu, Zuxuan Wu, Yu-Gang Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.13637v1.pdf)  
  Keywords: video generation, diffusion model, motion control, diffusion transformer, identity  

### Physical Understanding

*Showing the latest 50 out of 129 papers*

- **[ColoDiff: Integrating Dynamic Consistency With Content Awareness for Colonoscopy Video Generation](https://arxiv.org/abs/2602.23203v1)**  
  Authors: Junhu Fu, Shuyu Liang, Wutong Li, Chen Ma, Peng Huang, Kehao Wang, Ke Chen, Shengli Lin, Pinghong Zhou, Zeju Li, Yuanyuan Wang, Yi Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.23203v1.pdf)  
  Keywords: dynamics, video generation, diffusion model, temporal consistency, dit, controllable  
- **[Uni-Animator: Towards Unified Visual Colorization](https://arxiv.org/abs/2602.23191v1)**  
  Authors: Xinyuan Chen, Yao Xu, Shaowen Wang, Pengjie Song, Bowen Deng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.23191v1.pdf)  
  Keywords: temporal consistency, dit, diffusion transformer, physical  
- **[The Trinity of Consistency as a Defining Principle for General World Models](https://arxiv.org/abs/2602.23152v1)**  
  Authors: Jingxuan Wei, Siyuan Li, Yuhang Xu, Zheng Sun, Junjie Jiang, Hexuan Jin, Caijun Jia, Honghao He, Xinglong Xu, Xi bai, Chang Yu, Yumou Liu, Junnan Zhu, Xuanhe Zhou, Jintao Chen, Xiaobin Hu, Shancheng Pang, Bihui Yu, Ran He, Zhen Lei, Stan Z. Li, Conghui He, Shuicheng Yan, Cheng Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.23152v1.pdf)  
  Keywords: dynamics, video generation, physical, benchmark, temporal consistency, evaluation, world simulator, world model, architecture, concept, trajectory  
- **[Hierarchic-EEG2Text: Assessing EEG-To-Text Decoding across Hierarchical Abstraction Levels](https://arxiv.org/abs/2602.20932v1)**  
  Authors: Anupam Sharma, Harish Katti, Prajwal Singh, Shanmuganathan Raman, Krishna Miyapuram  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20932v1.pdf)  
  Keywords: architecture, dynamics, concept  
- **[RAYNOVA: Scale-Temporal Autoregressive World Modeling in Ray Space](https://arxiv.org/abs/2602.20685v2)**  
  Authors: Yichen Xie, Chensheng Peng, Mazen Abdelfattah, Yihan Hu, Jiezhi Yang, Eric Higgins, Ryan Brigden, Masayoshi Tomizuka, Wei Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20685v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://raynova-ai.github.io)  
  Keywords: video generation, multi-view video, dit, autoregressive, novel view, physical, world model  
- **[LESA: Learnable Stage-Aware Predictors for Diffusion Model Acceleration](https://arxiv.org/abs/2602.20497v1)**  
  Authors: Peiliang Cai, Jiacheng Liu, Haowen Xu, Xinyu Wang, Chang Zou, Linfeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20497v1.pdf)  
  Keywords: dynamics, video generation, diffusion model, text-to-video, denoising, video synthesis, dit, diffusion transformer, acceleration, architecture  
- **[3DSPA: A 3D Semantic Point Autoencoder for Evaluating Video Realism](https://arxiv.org/abs/2602.20354v1)**  
  Authors: Bhavik Chandna, Kelsey R. Allen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20354v1.pdf) | [![GitHub](https://img.shields.io/github/stars/TheProParadox/3dspa_code?style=social)](https://github.com/TheProParadox/3dspa_code)  
  Keywords: film, video generation, robotics, benchmark, temporal consistency, evaluation, physical, trajectory  
- **[NovaPlan: Zero-Shot Long-Horizon Manipulation via Closed-Loop Video Language Planning](https://arxiv.org/abs/2602.20119v1)**  
  Authors: Jiahui Fu, Junyu Nan, Lingfeng Sun, Hongyu Li, Jianing Qian, Jennifer L. Barry, Kris Kitani, George Konidaris  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20119v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://nova-plan.github.io)  
  Keywords: benchmark, video generation, physical  
- **[BigMaQ: A Big Macaque Motion and Animation Dataset Bridging Image and 3D Pose Representations](https://arxiv.org/abs/2602.19874v1)**  
  Authors: Lucas Martini, Alexander Lappe, Anna Bognár, Rufin Vogels, Martin A. Giese  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.19874v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://martinivis.github.io/BigMaQ)  
  Keywords: benchmark, dynamics, avatar  
- **[UniE2F: A Unified Diffusion Framework for Event-to-Frame Reconstruction with Video Foundation Models](https://arxiv.org/abs/2602.19202v1)**  
  Authors: Gang Xu, Zhiyu Zhu, Junhui Hou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.19202v1.pdf) | [![GitHub](https://img.shields.io/github/stars/CS-GangXu/UniE2F?style=social)](https://github.com/CS-GangXu/UniE2F)  
  Keywords: diffusion model, video diffusion, dit, frame interpolation, physical  

### Surveys & Benchmarks

*Showing the latest 50 out of 194 papers*

- **[The Trinity of Consistency as a Defining Principle for General World Models](https://arxiv.org/abs/2602.23152v1)**  
  Authors: Jingxuan Wei, Siyuan Li, Yuhang Xu, Zheng Sun, Junjie Jiang, Hexuan Jin, Caijun Jia, Honghao He, Xinglong Xu, Xi bai, Chang Yu, Yumou Liu, Junnan Zhu, Xuanhe Zhou, Jintao Chen, Xiaobin Hu, Shancheng Pang, Bihui Yu, Ran He, Zhen Lei, Stan Z. Li, Conghui He, Shuicheng Yan, Cheng Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.23152v1.pdf)  
  Keywords: dynamics, video generation, physical, benchmark, temporal consistency, evaluation, world simulator, world model, architecture, concept, trajectory  
- **[UCM: Unifying Camera Control and Memory with Time-aware Positional Encoding Warping for World Models](https://arxiv.org/abs/2602.22960v1)**  
  Authors: Tianxing Xu, Zixuan Wang, Guangyuan Wang, Li Hu, Zhongyi Zhang, Peng Zhang, Bang Zhang, Song-Hai Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.22960v1.pdf)  
  Keywords: interactive, video generation, efficient, benchmark, diffusion transformer, camera control, world model  
- **[SPATIALALIGN: Aligning Dynamic Spatial Relationships in Video Generation](https://arxiv.org/abs/2602.22745v1)**  
  Authors: Fengming Liu, Tat-Jen Cham, Chuanxia Zheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.22745v1.pdf)  
  Keywords: text-to-video, t2v, evaluation, video generation  
- **[Solaris: Building a Multiplayer Video World Model in Minecraft](https://arxiv.org/abs/2602.22208v2)**  
  Authors: Georgy Savva, Oscar Michel, Daohan Lu, Suppakit Waiwitlikhit, Timothy Meehan, Dhairya Mishra, Srivats Poddar, Jack Lu, Saining Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.22208v2.pdf)  
  Keywords: video generation, efficient, dit, evaluation, action-conditioned, architecture, world model  
- **[UniVBench: Towards Unified Evaluation for Video Foundation Models](https://arxiv.org/abs/2602.21835v1)**  
  Authors: Jianhui Wei, Xiaotian Zhang, Yichen Li, Yuan Wang, Yan Zhang, Ziyi Chen, Zhihang Tang, Wei Xu, Zuozhu Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21835v1.pdf)  
  Keywords: video generation, benchmark, dit, video editing, evaluation  
- **[HorizonForge: Driving Scene Editing with Any Trajectories and Any Vehicles](https://arxiv.org/abs/2602.21333v1)**  
  Authors: Yifan Wang, Francesco Pittaluga, Zaid Tasneem, Chenyu You, Manmohan Chandraker, Ziyu Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21333v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://horizonforge.github.io)  
  Keywords: autonomous driving, video diffusion, benchmark, temporal consistency, dit, evaluation, simulation, trajectory, controllable  
- **[AnimeAgent: Is the Multi-Agent via Image-to-Video models a Good Disney Storytelling Artist?](https://arxiv.org/abs/2602.20664v1)**  
  Authors: Hailong Yan, Shice Liu, Tao Wang, Xiangtao Zhang, Yijie Zhong, Jinwei Chen, Le Zhang, Bo Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20664v1.pdf)  
  Keywords: benchmark, i2v, image-to-video, diffusion model  
- **[3DSPA: A 3D Semantic Point Autoencoder for Evaluating Video Realism](https://arxiv.org/abs/2602.20354v1)**  
  Authors: Bhavik Chandna, Kelsey R. Allen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20354v1.pdf) | [![GitHub](https://img.shields.io/github/stars/TheProParadox/3dspa_code?style=social)](https://github.com/TheProParadox/3dspa_code)  
  Keywords: film, video generation, robotics, benchmark, temporal consistency, evaluation, physical, trajectory  
- **[NovaPlan: Zero-Shot Long-Horizon Manipulation via Closed-Loop Video Language Planning](https://arxiv.org/abs/2602.20119v1)**  
  Authors: Jiahui Fu, Junyu Nan, Lingfeng Sun, Hongyu Li, Jianing Qian, Jennifer L. Barry, Kris Kitani, George Konidaris  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20119v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://nova-plan.github.io)  
  Keywords: benchmark, video generation, physical  
- **[BigMaQ: A Big Macaque Motion and Animation Dataset Bridging Image and 3D Pose Representations](https://arxiv.org/abs/2602.19874v1)**  
  Authors: Lucas Martini, Alexander Lappe, Anna Bognár, Rufin Vogels, Martin A. Giese  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.19874v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://martinivis.github.io/BigMaQ)  
  Keywords: benchmark, dynamics, avatar  

### Text-to-Video Generation

*Showing the latest 50 out of 70 papers*

- **[SPATIALALIGN: Aligning Dynamic Spatial Relationships in Video Generation](https://arxiv.org/abs/2602.22745v1)**  
  Authors: Fengming Liu, Tat-Jen Cham, Chuanxia Zheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.22745v1.pdf)  
  Keywords: text-to-video, t2v, evaluation, video generation  
- **[LESA: Learnable Stage-Aware Predictors for Diffusion Model Acceleration](https://arxiv.org/abs/2602.20497v1)**  
  Authors: Peiliang Cai, Jiacheng Liu, Haowen Xu, Xinyu Wang, Chang Zou, Linfeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20497v1.pdf)  
  Keywords: dynamics, video generation, diffusion model, text-to-video, denoising, video synthesis, dit, diffusion transformer, acceleration, architecture  
- **[PedaCo-Gen: Scaffolding Pedagogical Agency in Human-AI Collaborative Video Authoring](https://arxiv.org/abs/2602.19623v1)**  
  Authors: Injun Baek, Yearim Kim, Nojun Kwak  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.19623v1.pdf)  
  Keywords: interactive, education, text-to-video, t2v, dit  
- **[JavisDiT++: Unified Modeling and Optimization for Joint Audio-Video Generation](https://arxiv.org/abs/2602.19163v1)**  
  Authors: Kai Liu, Yanhao Zheng, Kai Wang, Shengqiong Wu, Rongjunchen Zhang, Jiebo Luo, Dimitrios Hatzinakos, Ziwei Liu, Hao Fei, Tat-Seng Chua  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.19163v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://JavisVerse.github.io/JavisDiT2-page)  
  Keywords: video generation, t2v, sound, dit, evaluation  
- **[VQPP: Video Query Performance Prediction Benchmark](https://arxiv.org/abs/2602.17814v1)**  
  Authors: Adrian Catalin Lutu, Eduard Poesina, Radu Tudor Ionescu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.17814v1.pdf) | [![GitHub](https://img.shields.io/github/stars/AdrianLutu/VQPP?style=social)](https://github.com/AdrianLutu/VQPP)  
  Keywords: benchmark, text-to-video  
- **[CHAI: CacHe Attention Inference for text2video](https://arxiv.org/abs/2602.16132v1)**  
  Authors: Joel Mathew Cherian, Ashutosh Muralidhara Bharadwaj, Vima Gupta, Anand Padmanabha Iyer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.16132v1.pdf)  
  Keywords: diffusion model, denoising, text-to-video, t2v, video diffusion  
- **[VideoSketcher: Video Models Prior Enable Versatile Sequential Sketch Generation](https://arxiv.org/abs/2602.15819v1)**  
  Authors: Hui Ren, Yuval Alaluf, Omer Bar Tal, Alexander Schwing, Antonio Torralba, Yael Vinker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.15819v1.pdf)  
  Keywords: interactive, diffusion model, text-to-video, efficient, style, video diffusion, dit, autoregressive, creative  
- **[Consistency-Preserving Diverse Video Generation](https://arxiv.org/abs/2602.15287v1)**  
  Authors: Xinshuang Liu, Runfa Blark Li, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.15287v1.pdf)  
  Keywords: temporal consistency, text-to-video, video generation  
- **[ReTracing: An Archaeological Approach Through Body, Machine, and Generative Systems](https://arxiv.org/abs/2602.11242v1)**  
  Authors: Yitong Wang, Yue Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.11242v1.pdf)  
  Keywords: text-to-video  
- **[ConsID-Gen: View-Consistent and Identity-Preserving Image-to-Video Generation](https://arxiv.org/abs/2602.10113v1)**  
  Authors: Mingyang Wu, Ashirbad Mishra, Soumik Dey, Shuo Xing, Naveen Ravipati, Hansi Wu, Binbin Li, Zhengzhong Tu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.10113v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://myangwu.github.io/ConsID-Gen)  
  Keywords: video generation, image-to-video, text-to-video, benchmark, dit, diffusion transformer, evaluation, i2v, identity  

### Video Editing

- **[UniVBench: Towards Unified Evaluation for Video Foundation Models](https://arxiv.org/abs/2602.21835v1)**  
  Authors: Jianhui Wei, Xiaotian Zhang, Yichen Li, Yuan Wang, Yan Zhang, Ziyi Chen, Zhihang Tang, Wei Xu, Zuozhu Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21835v1.pdf)  
  Keywords: video generation, benchmark, dit, video editing, evaluation  
- **[SkyReels-V4: Multi-modal Video-Audio Generation, Inpainting and Editing model](https://arxiv.org/abs/2602.21818v2)**  
  Authors: Guibin Chen, Dixuan Lin, Jiangping Yang, Youqiang Zhang, Zhengcong Fei, Debang Li, Sheng Chen, Chaofeng Ao, Nuo Pang, Yiming Wang, Yikun Dou, Zheng Chen, Mingyuan Fan, Tuanhui Li, Mingshan Chang, Hao Zhang, Xiaopeng Sun, Jingtao Xu, Yuqiang Xie, Jiahua Wang, Zhiheng Xu, Weiming Xiong, Yuzhe Jin, Baoxuan Gu, Binjie Mao, Yunjie Yu, Jujie He, Yuhao Feng, Shiwen Tu, Chaojie Wang, Rui Yan, Wei Shen, Jingchen Wu, Peng Zhao, Xuanyue Zhong, Zhuangzhuang Liu, Kaifei Wang, Fuxiang Zhang, Weikai Xu, Wenyan Liu, Binglu Zhang, Yu Shen, Tianhui Xiong, Bin Peng, Liang Zeng, Xuchen Song, Haoxiang Guo, Peiyu Wang, Max W. Y. Lam, Chien-Hung Liu, Yahui Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21818v2.pdf)  
  Keywords: video generation, style, sound, image to video, video editing, dit, diffusion transformer, architecture, frame interpolation, multi-modal, super-resolution  
- **[GA-Drive: Geometry-Appearance Decoupled Modeling for Free-viewpoint Driving Scene Generatio](https://arxiv.org/abs/2602.20673v1)**  
  Authors: Hao Zhang, Lue Fan, Qitai Wang, Wenbo Li, Zehuan Wu, Lewei Lu, Zhaoxiang Zhang, Hongsheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20673v1.pdf)  
  Keywords: diffusion model, autonomous driving, video diffusion, video editing, dit, video-to-video, simulation, trajectory  
- **[PropFly: Learning to Propagate via On-the-Fly Supervision from Pre-trained Video Diffusion Models](https://arxiv.org/abs/2602.20583v1)**  
  Authors: Wonyong Seo, Jaeho Moon, Jaehyup Lee, Soo Ye Kim, Munchurl Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20583v1.pdf)  
  Keywords: flow matching, diffusion model, video diffusion, video editing, dit  
- **[RoboCurate: Harnessing Diversity with Action-Verified Neural Trajectory for Robot Learning](https://arxiv.org/abs/2602.18742v1)**  
  Authors: Seungku Kim, Suhyeok Jang, Byungjun Yoon, Dongyoung Kim, John Won, Jinwoo Shin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.18742v1.pdf)  
  Keywords: dit, video-to-video, simulation, physical, trajectory  
- **[When Test-Time Guidance Is Enough: Fast Image and Video Editing with Diffusion Guidance](https://arxiv.org/abs/2602.14157v1)**  
  Authors: Ahmed Ghorbel, Badr Moufad, Navid Bagheri Shouraki, Alain Oliviero Durmus, Thomas Hirtz, Eric Moulines, Jimmy Olsson, Yazid Janati  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.14157v1.pdf)  
  Keywords: benchmark, dit, evaluation, video editing  
- **[DreamID-Omni: Unified Framework for Controllable Human-Centric Audio-Video Generation](https://arxiv.org/abs/2602.12160v1)**  
  Authors: Xu Guo, Fulong Ye, Qichao Sun, Liyang Chen, Bingchuan Li, Pengze Zhang, Jiawei Liu, Songtao Zhao, Qian He, Xiangwang Hou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.12160v1.pdf)  
  Keywords: video generation, video editing, dit, diffusion transformer, identity, audio-driven, controllable  
- **[Tele-Omni: a Unified Multimodal Framework for Video Generation and Editing](https://arxiv.org/abs/2602.09609v2)**  
  Authors: Jialun Liu, Tian Li, Xiao Cao, Yukuo Ma, Gonghu Shang, Haibin Huang, Chi Zhang, Xiangzhen Chang, Zhiyong Huang, Jiakui Hu, Zuoxin Li, Yuanzhi Liang, Cong Liu, Junqi Liu, Robby T. Tan, Haitong Tang, Qizhen Weng, Yifan Xu, Liying Yang, Xiaoyan Yang, Peng Yu, Shiwen Zhang, Xuelong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.09609v2.pdf)  
  Keywords: video generation, image-to-video, text-to-video, video synthesis, video editing, dit  
- **[Omni-Video 2: Scaling MLLM-Conditioned Diffusion for Unified Video Generation and Editing](https://arxiv.org/abs/2602.08820v1)**  
  Authors: Hao Yang, Zhiyu Tan, Jia Gong, Luozheng Qin, Hesen Chen, Xiaomeng Yang, Yuqing Sun, Yuetan Lin, Mengping Yang, Hao Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.08820v1.pdf)  
  Keywords: video generation, diffusion model, text-to-video, efficient, video diffusion, benchmark, video editing, dit  
- **[PISCO: Precise Video Instance Insertion with Sparse Control](https://arxiv.org/abs/2602.08277v1)**  
  Authors: Xiangbo Gao, Renjie Li, Xinghao Chen, Yuheng Wu, Suofei Feng, Qing Yin, Zhengzhong Tu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.08277v1.pdf)  
  Keywords: dynamics, film, video generation, diffusion model, video diffusion, benchmark, video editing, dit, physical, controllable  

### Video Inpainting & Completion

- **[Learning Physics-Grounded 4D Dynamics with Neural Gaussian Force Fields](https://arxiv.org/abs/2602.00148v2)**  
  Authors: Shiqian Li, Ruihong Shen, Junfeng Ni, Chang Pan, Chi Zhang, Yixin Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.00148v2.pdf)  
  Keywords: dynamics, interactive, video generation, video prediction, physics, evaluation, simulation, physical, world model  
- **[DriveLaW:Unifying Planning and Video Generation in a Latent Driving World](https://arxiv.org/abs/2512.23421v2)**  
  Authors: Tianze Xia, Yongkang Li, Lijun Zhou, Jingfeng Yao, Kaixin Xiong, Haiyang Sun, Bing Wang, Kun Ma, Guang Chen, Hangjun Ye, Wenyu Liu, Xinggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.23421v2.pdf)  
  Keywords: trajectory, video generation, autonomous driving, video prediction, benchmark, architecture, world model  
- **[Autoregressive Flow Matching for Motion Prediction](https://arxiv.org/abs/2512.22688v1)**  
  Authors: Johnathan Xie, Stefan Stojanov, Cristobal Eyzaguirre, Daniel L. K. Yamins, Jiajun Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.22688v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Johnathan-Xie/arfm-motion-prediction?style=social)](https://github.com/Johnathan-Xie/arfm-motion-prediction)  
  Keywords: flow matching, video generation, video prediction, human motion, robotics, benchmark, dit, autoregressive  
- **[Over++: Generative Video Compositing for Layer Interaction Effects](https://arxiv.org/abs/2512.19661v1)**  
  Authors: Luchao Qi, Jiaye Wu, Jun Myeong Choi, Cary Phillips, Roni Sengupta, Dan B Goldman  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.19661v1.pdf)  
  Keywords: dit, video inpainting  
- **[Vidarc: Embodied Video Diffusion Model for Closed-loop Control](https://arxiv.org/abs/2512.17661v1)**  
  Authors: Yao Feng, Chendong Xiang, Xinyi Mao, Hengkai Tan, Zuyue Zhang, Shuhe Huang, Kaiwen Zheng, Haitian Liu, Hang Su, Jun Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.17661v1.pdf)  
  Keywords: dynamics, diffusion model, video prediction, video diffusion, autoregressive, physical  
- **[Flowception: Temporally Expansive Flow Matching for Video Generation](https://arxiv.org/abs/2512.11438v1)**  
  Authors: Tariq Berrada Ifriqi, John Nguyen, Karteek Alahari, Jakob Verbeek, Ricky T. Q. Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.11438v1.pdf)  
  Keywords: flow matching, video generation, image-to-video, denoising, efficient, autoregressive, video interpolation  
- **[Astra: General Interactive World Model with Autoregressive Denoising](https://arxiv.org/abs/2512.08931v3)**  
  Authors: Yixuan Zhu, Jiaqi Feng, Wenzhao Zheng, Yuan Gao, Xin Tao, Pengfei Wan, Jie Zhou, Jiwen Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.08931v3.pdf)  
  Keywords: interactive, video generation, autonomous driving, streaming, video prediction, denoising, diffusion transformer, autoregressive, architecture, camera control, world model  

### Video Super-Resolution & Enhancement

*Showing the latest 50 out of 57 papers*

- **[Denoising as Path Planning: Training-Free Acceleration of Diffusion Models with DPCache](https://arxiv.org/abs/2602.22654v1)**  
  Authors: Bowen Cui, Yuanbin Wang, Huajiang Xu, Biaolong Chen, Aixi Zhang, Hao Jiang, Zhengzheng Jin, Xu Liu, Pipei Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.22654v1.pdf) | [![GitHub](https://img.shields.io/github/stars/argsss/DPCache?style=social)](https://github.com/argsss/DPCache)  
  Keywords: video generation, diffusion model, efficient, denoising, dit, acceleration, trajectory  
- **[SkyReels-V4: Multi-modal Video-Audio Generation, Inpainting and Editing model](https://arxiv.org/abs/2602.21818v2)**  
  Authors: Guibin Chen, Dixuan Lin, Jiangping Yang, Youqiang Zhang, Zhengcong Fei, Debang Li, Sheng Chen, Chaofeng Ao, Nuo Pang, Yiming Wang, Yikun Dou, Zheng Chen, Mingyuan Fan, Tuanhui Li, Mingshan Chang, Hao Zhang, Xiaopeng Sun, Jingtao Xu, Yuqiang Xie, Jiahua Wang, Zhiheng Xu, Weiming Xiong, Yuzhe Jin, Baoxuan Gu, Binjie Mao, Yunjie Yu, Jujie He, Yuhao Feng, Shiwen Tu, Chaojie Wang, Rui Yan, Wei Shen, Jingchen Wu, Peng Zhao, Xuanyue Zhong, Zhuangzhuang Liu, Kaifei Wang, Fuxiang Zhang, Weikai Xu, Wenyan Liu, Binglu Zhang, Yu Shen, Tianhui Xiong, Bin Peng, Liang Zeng, Xuchen Song, Haoxiang Guo, Peiyu Wang, Max W. Y. Lam, Chien-Hung Liu, Yahui Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21818v2.pdf)  
  Keywords: video generation, style, sound, image to video, video editing, dit, diffusion transformer, architecture, frame interpolation, multi-modal, super-resolution  
- **[LESA: Learnable Stage-Aware Predictors for Diffusion Model Acceleration](https://arxiv.org/abs/2602.20497v1)**  
  Authors: Peiliang Cai, Jiacheng Liu, Haowen Xu, Xinyu Wang, Chang Zou, Linfeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20497v1.pdf)  
  Keywords: dynamics, video generation, diffusion model, text-to-video, denoising, video synthesis, dit, diffusion transformer, acceleration, architecture  
- **[UniE2F: A Unified Diffusion Framework for Event-to-Frame Reconstruction with Video Foundation Models](https://arxiv.org/abs/2602.19202v1)**  
  Authors: Gang Xu, Zhiyu Zhu, Junhui Hou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.19202v1.pdf) | [![GitHub](https://img.shields.io/github/stars/CS-GangXu/UniE2F?style=social)](https://github.com/CS-GangXu/UniE2F)  
  Keywords: diffusion model, video diffusion, dit, frame interpolation, physical  
- **[Predict to Skip: Linear Multistep Feature Forecasting for Efficient Diffusion Transformers](https://arxiv.org/abs/2602.18093v1)**  
  Authors: Hanshuai Cui, Zhiqing Tang, Qianli Ma, Zhi Yao, Weijia Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.18093v1.pdf)  
  Keywords: dynamics, video generation, denoising, efficient, dit, diffusion transformer, acceleration, trajectory  
- **[DDiT: Dynamic Patch Scheduling for Efficient Diffusion Transformers](https://arxiv.org/abs/2602.16968v1)**  
  Authors: Dahye Kim, Deepti Ghadiyaram, Raghudeep Gadde  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.16968v1.pdf)  
  Keywords: video generation, denoising, efficient, dit, diffusion transformer  
- **[CHAI: CacHe Attention Inference for text2video](https://arxiv.org/abs/2602.16132v1)**  
  Authors: Joel Mathew Cherian, Ashutosh Muralidhara Bharadwaj, Vima Gupta, Anand Padmanabha Iyer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.16132v1.pdf)  
  Keywords: diffusion model, denoising, text-to-video, t2v, video diffusion  
- **[AdaCorrection: Adaptive Offset Cache Correction for Accurate Diffusion Transformers](https://arxiv.org/abs/2602.13357v1)**  
  Authors: Dong Liu, Yanxuan Yu, Ben Lengerich, Ying Nian Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.13357v1.pdf)  
  Keywords: video generation, denoising, efficient, video diffusion, benchmark, dit, diffusion transformer, acceleration  
- **[Motion Prior Distillation in Time Reversal Sampling for Generative Inbetweening](https://arxiv.org/abs/2602.12679v2)**  
  Authors: Wooseok Jeon, Seunghyun Shin, Dongmin Shin, Hae-Gon Jeon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.12679v2.pdf)  
  Keywords: image-to-video, diffusion model, denoising, distillation, benchmark, dit, evaluation, i2v  
- **[MonarchRT: Efficient Attention for Real-Time Video Generation](https://arxiv.org/abs/2602.12271v1)**  
  Authors: Krish Agarwal, Zhuoming Chen, Cheng Luo, Yongqi Chen, Haizhong Zheng, Xun Huang, Atri Rudra, Beidi Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.12271v1.pdf)  
  Keywords: video generation, diffusion model, denoising, efficient, video diffusion, diffusion transformer, autoregressive  

### World Models & Simulation

*Showing the latest 50 out of 100 papers*

- **[The Trinity of Consistency as a Defining Principle for General World Models](https://arxiv.org/abs/2602.23152v1)**  
  Authors: Jingxuan Wei, Siyuan Li, Yuhang Xu, Zheng Sun, Junjie Jiang, Hexuan Jin, Caijun Jia, Honghao He, Xinglong Xu, Xi bai, Chang Yu, Yumou Liu, Junnan Zhu, Xuanhe Zhou, Jintao Chen, Xiaobin Hu, Shancheng Pang, Bihui Yu, Ran He, Zhen Lei, Stan Z. Li, Conghui He, Shuicheng Yan, Cheng Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.23152v1.pdf)  
  Keywords: dynamics, video generation, physical, benchmark, temporal consistency, evaluation, world simulator, world model, architecture, concept, trajectory  
- **[UCM: Unifying Camera Control and Memory with Time-aware Positional Encoding Warping for World Models](https://arxiv.org/abs/2602.22960v1)**  
  Authors: Tianxing Xu, Zixuan Wang, Guangyuan Wang, Li Hu, Zhongyi Zhang, Peng Zhang, Bang Zhang, Song-Hai Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.22960v1.pdf)  
  Keywords: interactive, video generation, efficient, benchmark, diffusion transformer, camera control, world model  
- **[Flow Matching is Adaptive to Manifold Structures](https://arxiv.org/abs/2602.22486v1)**  
  Authors: Shivam Kumar, Yixin Wang, Lizhen Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.22486v1.pdf)  
  Keywords: flow matching, simulation, video generation  
- **[Solaris: Building a Multiplayer Video World Model in Minecraft](https://arxiv.org/abs/2602.22208v2)**  
  Authors: Georgy Savva, Oscar Michel, Daohan Lu, Suppakit Waiwitlikhit, Timothy Meehan, Dhairya Mishra, Srivats Poddar, Jack Lu, Saining Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.22208v2.pdf)  
  Keywords: video generation, efficient, dit, evaluation, action-conditioned, architecture, world model  
- **[HorizonForge: Driving Scene Editing with Any Trajectories and Any Vehicles](https://arxiv.org/abs/2602.21333v1)**  
  Authors: Yifan Wang, Francesco Pittaluga, Zaid Tasneem, Chenyu You, Manmohan Chandraker, Ziyu Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.21333v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://horizonforge.github.io)  
  Keywords: autonomous driving, video diffusion, benchmark, temporal consistency, dit, evaluation, simulation, trajectory, controllable  
- **[RAYNOVA: Scale-Temporal Autoregressive World Modeling in Ray Space](https://arxiv.org/abs/2602.20685v2)**  
  Authors: Yichen Xie, Chensheng Peng, Mazen Abdelfattah, Yihan Hu, Jiezhi Yang, Eric Higgins, Ryan Brigden, Masayoshi Tomizuka, Wei Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20685v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://raynova-ai.github.io)  
  Keywords: video generation, multi-view video, dit, autoregressive, novel view, physical, world model  
- **[GA-Drive: Geometry-Appearance Decoupled Modeling for Free-viewpoint Driving Scene Generatio](https://arxiv.org/abs/2602.20673v1)**  
  Authors: Hao Zhang, Lue Fan, Qitai Wang, Wenbo Li, Zehuan Wu, Lewei Lu, Zhaoxiang Zhang, Hongsheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.20673v1.pdf)  
  Keywords: diffusion model, autonomous driving, video diffusion, video editing, dit, video-to-video, simulation, trajectory  
- **[PedaCo-Gen: Scaffolding Pedagogical Agency in Human-AI Collaborative Video Authoring](https://arxiv.org/abs/2602.19623v1)**  
  Authors: Injun Baek, Yearim Kim, Nojun Kwak  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.19623v1.pdf)  
  Keywords: interactive, education, text-to-video, t2v, dit  
- **[RoboCurate: Harnessing Diversity with Action-Verified Neural Trajectory for Robot Learning](https://arxiv.org/abs/2602.18742v1)**  
  Authors: Seungku Kim, Suhyeok Jang, Byungjun Yoon, Dongyoung Kim, John Won, Jinwoo Shin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.18742v1.pdf)  
  Keywords: dit, video-to-video, simulation, physical, trajectory  
- **[Generated Reality: Human-centric World Simulation using Interactive Video Generation with Hand and Camera Control](https://arxiv.org/abs/2602.18422v1)**  
  Authors: Linxi Xie, Lisong C. Sun, Ashley Neall, Tong Wu, Shengqu Cai, Gordon Wetzstein  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.18422v1.pdf)  
  Keywords: interactive, video generation, diffusion model, video diffusion, dit, diffusion transformer, simulation, camera control, world model  



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
