# Awesome Video Diffusions [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Video Diffusion Models and Video Generation. Content is automatically updated daily.

> Last Update: 2026-02-24 02:08:52

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
- [Applications](#applications) (58 papers) - Domain-specific applications of video diffusion models
- [Architecture & Efficiency](#architecture-&-efficiency) (371 papers) - Architectural innovations (DiT, UNet), flow matching, and training/inference efficiency
- [Audio & Multi-modal](#audio-&-multi-modal) (37 papers) - Audio-driven and multi-modal conditioned video generation
- [Controllable Generation](#controllable-generation) (118 papers) - Controllable video generation with motion, camera, pose, or layout guidance
- [Human & Character Animation](#human-&-character-animation) (34 papers) - Human-centric video generation including talking heads, dance, and character animation
- [Image-to-Video Generation](#image-to-video-generation) (39 papers) - Methods for animating still images into videos
- [Long Video Generation](#long-video-generation) (126 papers) - Generating temporally consistent long-form videos beyond short clips
- [Personalization & Customization](#personalization-&-customization) (92 papers) - Personalized video generation with custom subjects, identities, or styles
- [Physical Understanding](#physical-understanding) (131 papers) - Physics-aware video generation and dynamics modeling
- [Surveys & Benchmarks](#surveys-&-benchmarks) (197 papers) - Survey papers, benchmarks, and evaluation metrics for video generation
- [Text-to-Video Generation](#text-to-video-generation) (71 papers) - Foundation models and methods for generating videos from text prompts
- [Video Editing](#video-editing) (40 papers) - Diffusion-based video editing, style transfer, and manipulation
- [Video Inpainting & Completion](#video-inpainting-&-completion) (8 papers) - Video inpainting, completion, outpainting, and temporal prediction
- [Video Super-Resolution & Enhancement](#video-super-resolution-&-enhancement) (58 papers) - Video quality improvement, upscaling, restoration, and frame interpolation
- [World Models & Simulation](#world-models-&-simulation) (101 papers) - Video generation as world simulators and interactive environment generation



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3D-aware Video Generation

- **[A Single Image and Multimodality Is All You Need for Novel View Synthesis](https://arxiv.org/abs/2602.17909v1)**  
  Authors: Amirhosein Javadi, Chi-Shiang Gau, Konstantinos D. Polyzos, Tara Javidi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.17909v1.pdf)  
  Keywords: efficient, novel view, dit, video generation  
- **[VideoNeuMat: Neural Material Extraction from Generative Video Models](https://arxiv.org/abs/2602.07272v1)**  
  Authors: Bowen Xue, Saeed Hadadan, Zheng Zeng, Fabrice Rousselle, Zahra Montazeri, Milos Hasan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.07272v1.pdf)  
  Keywords: novel view, video diffusion, dit, diffusion model  
- **[CineScene: Implicit 3D as Effective Scene Representation for Cinematic Video Generation](https://arxiv.org/abs/2602.06959v1)**  
  Authors: Kaiyi Huang, Yukun Huang, Yu Li, Jianhong Bai, Xintao Wang, Zinan Lin, Xuefei Ning, Jiwen Yu, Pengfei Wan, Yu Wang, Xihui Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06959v1.pdf)  
  Keywords: text-to-video, dit, trajectory, video synthesis, physical, video generation, 3d-aware  
- **[SkeletonGaussian: Editable 4D Generation through Gaussian Skeletonization](https://arxiv.org/abs/2602.04271v1)**  
  Authors: Lifan Wu, Ruijie Zhu, Yubo Ai, Tianzhu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.04271v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wusar.github.io/projects/skeletongaussian)  
  Keywords: 4d generation, dit  
- **[3D-Aware Implicit Motion Control for View-Adaptive Human Video Generation](https://arxiv.org/abs/2602.03796v2)**  
  Authors: Zhixue Fang, Xu He, Songlin Tang, Haoxian Zhang, Qingfeng Li, Xiaoqiang Liu, Pengfei Wan, Kun Gai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03796v2.pdf)  
  Keywords: dit, motion control, dynamics, human motion, video generation, camera control, 3d-aware  
- **[FreeFix: Boosting 3D Gaussian Splatting via Fine-Tuning-Free Diffusion Models](https://arxiv.org/abs/2601.20857v1)**  
  Authors: Hongyu Zhou, Zisen Shao, Sheng Miao, Pan Wang, Dongfeng Bai, Bingbing Liu, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.20857v1.pdf)  
  Keywords: novel view, video diffusion, dit, diffusion model  
- **[AnyView: Synthesizing Any Novel View in Dynamic Scenes](https://arxiv.org/abs/2601.16982v1)**  
  Authors: Basile Van Hoorick, Dian Chen, Shun Iwase, Pavel Tokmakov, Muhammad Zubair Irshad, Igor Vasiljevic, Swati Gupta, Fangzhou Cheng, Sergey Zakharov, Vitor Campagnolo Guizilini  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.16982v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://tri-ml.github.io/AnyView)  
  Keywords: temporal consistency, novel view, benchmark, video generation  
- **[Memory-V2V: Augmenting Video-to-Video Diffusion Models with Memory](https://arxiv.org/abs/2601.16296v1)**  
  Authors: Dohun Lee, Chun-Hao Paul Huang, Xuelin Chen, Jong Chul Ye, Duygu Ceylan, Hyeonho Jeong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.16296v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://dohunlee1.github.io/MemoryV2V)  
  Keywords: dit, long video, video-to-video, novel view, diffusion model, video editing, video diffusion  
- **[GR3EN: Generative Relighting for 3D Environments](https://arxiv.org/abs/2601.16272v2)**  
  Authors: Xiaoyan Xing, Philipp Henzler, Junhwa Hur, Runze Li, Jonathan T. Barron, Pratul P. Srinivasan, Dor Verbin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.16272v2.pdf)  
  Keywords: dit, video-to-video, novel view, diffusion model, video diffusion, controllable  
- **[CamPilot: Improving Camera Control in Video Diffusion Model with Efficient Camera Reward Feedback](https://arxiv.org/abs/2601.16214v1)**  
  Authors: Wenhang Ge, Guibao Shen, Jiawei Feng, Luozhou Wang, Hao Lu, Xingye Tian, Xin Tao, Ying-Cong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.16214v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://a-bigbao.github.io/CamPilot)  
  Keywords: efficient, camera control, novel view, benchmark, diffusion model, video diffusion  

### Applications

*Showing the latest 50 out of 58 papers*

- **[VideoSketcher: Video Models Prior Enable Versatile Sequential Sketch Generation](https://arxiv.org/abs/2602.15819v1)**  
  Authors: Hui Ren, Yuval Alaluf, Omer Bar Tal, Alexander Schwing, Antonio Torralba, Yael Vinker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.15819v1.pdf)  
  Keywords: efficient, style, text-to-video, creative, dit, interactive, autoregressive, diffusion model, video diffusion  
- **[Beyond End-to-End Video Models: An LLM-Based Multi-Agent System for Educational Video Generation](https://arxiv.org/abs/2602.11790v1)**  
  Authors: Lingyong Yan, Jiulong Wu, Dong Xie, Weixian Shi, Deguo Xia, Jizhou Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.11790v1.pdf)  
  Keywords: education, dit, video generation  
- **[Ctrl&Shift: High-Quality Geometry-Aware Object Manipulation in Visual Generation](https://arxiv.org/abs/2602.11440v1)**  
  Authors: Penghui Ruan, Bojia Zi, Xianbiao Qi, Youze Huang, Rong Xiao, Pichao Wang, Jiannong Cao, Yuhui Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.11440v1.pdf)  
  Keywords: creative, dit, identity, film, controllable  
- **[VideoWorld 2: Learning Transferable Knowledge from Real-world Videos](https://arxiv.org/abs/2602.10102v1)**  
  Authors: Zhongwei Ren, Yunchao Wei, Xiao Yu, Guixun Luo, Yao Zhao, Bingyi Kang, Jiashi Feng, Xiaojie Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.10102v1.pdf)  
  Keywords: robotics, dynamics, video generation, autoregressive, diffusion model, video diffusion  
- **[AUHead: Realistic Emotional Talking Head Generation via Action Units Control](https://arxiv.org/abs/2602.09534v1)**  
  Authors: Jiayi Lyu, Leigang Qu, Wenjing Zhang, Hanyu Jiang, Kai Liu, Zhenglin Zhou, Xiaobo Xia, Jian Xue, Tat-Seng Chua  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.09534v1.pdf) | [![GitHub](https://img.shields.io/github/stars/laura990501/AUHead_ICLR?style=social)](https://github.com/laura990501/AUHead_ICLR)  
  Keywords: motion control, dit, interactive, talking head, video generation, identity, benchmark, diffusion model, avatar, film, controllable  
- **[PISCO: Precise Video Instance Insertion with Sparse Control](https://arxiv.org/abs/2602.08277v1)**  
  Authors: Xiangbo Gao, Renjie Li, Xinghao Chen, Yuheng Wu, Suofei Feng, Qing Yin, Zhengzhong Tu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.08277v1.pdf)  
  Keywords: film, dit, dynamics, physical, video generation, benchmark, diffusion model, video editing, video diffusion, controllable  
- **[Action-to-Action Flow Matching](https://arxiv.org/abs/2602.07322v1)**  
  Authors: Jindou Jia, Gen Li, Xiangyu Chen, Tuo An, Yuxuan Hu, Jingliang Li, Xinying Guo, Jianfei Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.07322v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lorenzo-0-0.github.io/A2A_Flow_Matching)  
  Keywords: robotics, dit, fast inference, dynamics, flow matching, physical, video generation, denoising  
- **[Driving with DINO: Vision Foundation Features as a Unified Bridge for Sim-to-Real Generation in Autonomous Driving](https://arxiv.org/abs/2602.06159v2)**  
  Authors: Xuyang Chen, Conglang Zhang, Chuanheng Fu, Zihao Yang, Kaixuan Zhou, Yizhi Zhang, Jianan He, Yanfeng Zhang, Mingwei Sun, Zengmao Wang, Zhen Dong, Xiaoxiao Long, Liqiu Meng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06159v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://albertchen98.github.io/DwD-project)  
  Keywords: simulation, video generation, autonomous driving, video diffusion, controllable  
- **[LSA: Localized Semantic Alignment for Enhancing Temporal Consistency in Traffic Video Generation](https://arxiv.org/abs/2602.05966v1)**  
  Authors: Mirlan Karimov, Teodora Spasojevic, Markus Braun, Julian Wiederer, Vasileios Belagiannis, Marc Pollefeys  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.05966v1.pdf)  
  Keywords: dit, evaluation, video generation, autonomous driving, temporal consistency, controllable  
- **[Reliable and Responsible Foundation Models: A Comprehensive Survey](https://arxiv.org/abs/2602.08145v1)**  
  Authors: Xinyu Yang, Junlin Han, Rishi Bommasani, Jinqi Luo, Wenjie Qu, Wangchunshu Zhou, Adel Bibi, Xiyao Wang, Jaehong Yoon, Elias Stengel-Eskin, Shengbang Tong, Lingfeng Shen, Rafael Rafailov, Runjia Li, Zhaoyang Wang, Yiyang Zhou, Chenhang Cui, Yu Wang, Wenhao Zheng, Huichi Zhou, Jindong Gu, Zhaorun Chen, Peng Xia, Tony Lee, Thomas Zollo, Vikash Sehwag, Jixuan Leng, Jiuhai Chen, Yuxin Wen, Huan Zhang, Zhun Deng, Linjun Zhang, Pavel Izmailov, Pang Wei Koh, Yulia Tsvetkov, Andrew Wilson, Jiaheng Zhang, James Zou, Cihang Xie, Hao Wang, Philip Torr, Julian McAuley, David Alvarez-Melis, Florian Tramèr, Kaidi Xu, Suman Jana, Chris Callison-Burch, Rene Vidal, Filippos Kokkinos, Mohit Bansal, Beidi Chen, Huaxiu Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.08145v1.pdf)  
  Keywords: survey, dit, education  

### Architecture & Efficiency

*Showing the latest 50 out of 371 papers*

- **[UniE2F: A Unified Diffusion Framework for Event-to-Frame Reconstruction with Video Foundation Models](https://arxiv.org/abs/2602.19202v1)**  
  Authors: Gang Xu, Zhiyu Zhu, Junhui Hou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.19202v1.pdf) | [![GitHub](https://img.shields.io/github/stars/CS-GangXu/UniE2F?style=social)](https://github.com/CS-GangXu/UniE2F)  
  Keywords: dit, physical, frame interpolation, diffusion model, video diffusion  
- **[JavisDiT++: Unified Modeling and Optimization for Joint Audio-Video Generation](https://arxiv.org/abs/2602.19163v1)**  
  Authors: Kai Liu, Yanhao Zheng, Kai Wang, Shengqiong Wu, Rongjunchen Zhang, Jiebo Luo, Dimitrios Hatzinakos, Ziwei Liu, Hao Fei, Tat-Seng Chua  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.19163v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://JavisVerse.github.io/JavisDiT2-page)  
  Keywords: t2v, dit, evaluation, sound, video generation  
- **[Flash-VAED: Plug-and-Play VAE Decoders for Efficient Video Generation](https://arxiv.org/abs/2602.19161v1)**  
  Authors: Lunjie Zhu, Yushi Huang, Xingtong Ge, Yufei Xue, Zhening Liu, Yumeng Zhang, Zehong Lin, Jun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.19161v1.pdf)  
  Keywords: efficient, diffusion transformer, video synthesis, video generation, acceleration, distillation, diffusion model  
- **[RoboCurate: Harnessing Diversity with Action-Verified Neural Trajectory for Robot Learning](https://arxiv.org/abs/2602.18742v1)**  
  Authors: Seungku Kim, Suhyeok Jang, Byungjun Yoon, Dongyoung Kim, John Won, Jinwoo Shin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.18742v1.pdf)  
  Keywords: dit, trajectory, physical, simulation, video-to-video  
- **[Generated Reality: Human-centric World Simulation using Interactive Video Generation with Hand and Camera Control](https://arxiv.org/abs/2602.18422v1)**  
  Authors: Linxi Xie, Lisong C. Sun, Ashley Neall, Tong Wu, Shengqu Cai, Gordon Wetzstein  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.18422v1.pdf)  
  Keywords: diffusion transformer, dit, interactive, video generation, simulation, camera control, diffusion model, world model, video diffusion  
- **[Predict to Skip: Linear Multistep Feature Forecasting for Efficient Diffusion Transformers](https://arxiv.org/abs/2602.18093v1)**  
  Authors: Hanshuai Cui, Zhiqing Tang, Qianli Ma, Zhi Yao, Weijia Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.18093v1.pdf)  
  Keywords: efficient, diffusion transformer, dit, dynamics, trajectory, video generation, acceleration, denoising  
- **[A Single Image and Multimodality Is All You Need for Novel View Synthesis](https://arxiv.org/abs/2602.17909v1)**  
  Authors: Amirhosein Javadi, Chi-Shiang Gau, Konstantinos D. Polyzos, Tara Javidi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.17909v1.pdf)  
  Keywords: efficient, novel view, dit, video generation  
- **[DDiT: Dynamic Patch Scheduling for Efficient Diffusion Transformers](https://arxiv.org/abs/2602.16968v1)**  
  Authors: Dahye Kim, Deepti Ghadiyaram, Raghudeep Gadde  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.16968v1.pdf)  
  Keywords: efficient, diffusion transformer, dit, video generation, denoising  
- **[Xray-Visual Models: Scaling Vision models on Industry Scale Data](https://arxiv.org/abs/2602.16918v1)**  
  Authors: Shlok Mishra, Tsung-Yu Lin, Linda Wang, Hongli Xu, Yimin Liu, Michael Hsu, Chaitanya Ahuja, Hao Yuan, Jianpeng Cheng, Hong-You Chen, Haoyuan Xu, Chao Li, Abhijeet Awasthi, Jihye Moon, Don Husa, Michael Ge, Sumedha Singla, Arkabandhu Chowdhury, Phong Dingh, Satya Narayan Shukla, Yonghuan Yang, David Jacobs, Qi Guo, Jun Xiao, Xiangjun Fan, Aashu Singh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.16918v1.pdf)  
  Keywords: architecture, style, efficient, benchmark  
- **[VideoSketcher: Video Models Prior Enable Versatile Sequential Sketch Generation](https://arxiv.org/abs/2602.15819v1)**  
  Authors: Hui Ren, Yuval Alaluf, Omer Bar Tal, Alexander Schwing, Antonio Torralba, Yael Vinker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.15819v1.pdf)  
  Keywords: efficient, style, text-to-video, creative, dit, interactive, autoregressive, diffusion model, video diffusion  

### Audio & Multi-modal

- **[JavisDiT++: Unified Modeling and Optimization for Joint Audio-Video Generation](https://arxiv.org/abs/2602.19163v1)**  
  Authors: Kai Liu, Yanhao Zheng, Kai Wang, Shengqiong Wu, Rongjunchen Zhang, Jiebo Luo, Dimitrios Hatzinakos, Ziwei Liu, Hao Fei, Tat-Seng Chua  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.19163v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://JavisVerse.github.io/JavisDiT2-page)  
  Keywords: t2v, dit, evaluation, sound, video generation  
- **[EchoTorrent: Towards Swift, Sustained, and Streaming Multi-Modal Video Generation](https://arxiv.org/abs/2602.13669v1)**  
  Authors: Rang Meng, Weipeng Wu, Yingjie Yin, Yuming Li, Chenguang Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.13669v1.pdf)  
  Keywords: architecture, video generation, autoregressive, streaming, multi-modal, identity, temporal consistency  
- **[DreamID-Omni: Unified Framework for Controllable Human-Centric Audio-Video Generation](https://arxiv.org/abs/2602.12160v1)**  
  Authors: Xu Guo, Fulong Ye, Qichao Sun, Liyang Chen, Bingchuan Li, Pengze Zhang, Jiawei Liu, Songtao Zhao, Qian He, Xiangwang Hou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.12160v1.pdf)  
  Keywords: diffusion transformer, dit, video generation, identity, audio-driven, video editing, controllable  
- **[TiFRe: Text-guided Video Frame Reduction for Efficient Video Multi-modal Large Language Models](https://arxiv.org/abs/2602.08861v1)**  
  Authors: Xiangtian Zheng, Zishuo Wang, Yuxin Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.08861v1.pdf)  
  Keywords: style, multi-modal, efficient  
- **[VideoVeritas: AI-Generated Video Detection via Perception Pretext Reinforcement Learning](https://arxiv.org/abs/2602.08828v1)**  
  Authors: Hao Tan, Jun Lan, Senyuan Shi, Zichang Tan, Zijian Yu, Huijia Zhu, Weiqiang Wang, Jun Wan, Zhen Lei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.08828v1.pdf)  
  Keywords: multi-modal, evaluation, benchmark, video generation  
- **[MOVA: Towards Scalable and Synchronized Video-Audio Generation](https://arxiv.org/abs/2602.08794v2)**  
  Authors: SII-OpenMOSS Team, :, Donghua Yu, Mingshu Chen, Qi Chen, Qi Luo, Qianyi Wu, Qinyuan Cheng, Ruixiao Li, Tianyi Liang, Wenbo Zhang, Wenming Tu, Xiangyu Peng, Yang Gao, Yanru Huo, Ying Zhu, Yinze Luo, Yiyang Zhang, Yuerong Song, Zhe Xu, Zhiyu Zhang, Chenchen Yang, Cheng Chang, Chushu Zhou, Hanfu Chen, Hongnan Ma, Jiaxi Li, Jingqi Tong, Junxi Liu, Ke Chen, Shimin Li, Shiqi Jiang, Songlin Wang, Wei Jiang, Zhaoye Fei, Zhiyuan Ning, Chunguo Li, Chenhui Li, Ziwei He, Zengfeng Huang, Xie Chen, Xipeng Qiu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.08794v2.pdf)  
  Keywords: efficient, t2v, architecture, text to video, sound  
- **[T2VTree: User-Centered Visual Analytics for Agent-Assisted Thought-to-Video Authoring](https://arxiv.org/abs/2602.08368v1)**  
  Authors: Zhuoyun Zheng, Yu Dong, Gaorong Liang, Guan Li, Guihua Shan, Shiyu Cheng, Dong Tian, Jianlong Zhou, Jie Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.08368v1.pdf) | [![GitHub](https://img.shields.io/github/stars/tezuka0210/T2VTree?style=social)](https://github.com/tezuka0210/T2VTree)  
  Keywords: multi-modal, t2v, dit, video generation  
- **[SoulX-FlashHead: Oracle-guided Generation of Infinite Real-time Streaming Talking Heads](https://arxiv.org/abs/2602.07449v3)**  
  Authors: Tan Yu, Qian Qiao, Le Shen, Ke Zhou, Jincheng Hu, Dian Sheng, Bo Hu, Haoming Qin, Jun Gao, Changhai Zhou, Shunshun Yin, Siyuan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.07449v3.pdf)  
  Keywords: talking head, physical, video generation, autoregressive, streaming, identity, distillation, benchmark, audio-driven  
- **[Meta Engine: A Unified Semantic Query Engine on Heterogeneous LLM-Based Query Systems](https://arxiv.org/abs/2602.01701v1)**  
  Authors: Ruyu Li, Tinghui Zhang, Haodi Ma, Daisy Zhe Wang, Yifan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.01701v1.pdf)  
  Keywords: architecture, multi-modal, evaluation, dit  
- **[Omni-Judge: Can Omni-LLMs Serve as Human-Aligned Judges for Text-Conditioned Audio-Video Generation?](https://arxiv.org/abs/2602.01623v1)**  
  Authors: Susan Liang, Chao Huang, Filippos Bellos, Yolo Yunlong Tang, Qianxiang Shen, Jing Bi, Luchuan Song, Zeliang Zhang, Jason Corso, Chenliang Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.01623v1.pdf)  
  Keywords: text-to-video, dit, evaluation, physical, video generation, multi-modal  

### Controllable Generation

*Showing the latest 50 out of 118 papers*

- **[RoboCurate: Harnessing Diversity with Action-Verified Neural Trajectory for Robot Learning](https://arxiv.org/abs/2602.18742v1)**  
  Authors: Seungku Kim, Suhyeok Jang, Byungjun Yoon, Dongyoung Kim, John Won, Jinwoo Shin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.18742v1.pdf)  
  Keywords: dit, trajectory, physical, simulation, video-to-video  
- **[Generated Reality: Human-centric World Simulation using Interactive Video Generation with Hand and Camera Control](https://arxiv.org/abs/2602.18422v1)**  
  Authors: Linxi Xie, Lisong C. Sun, Ashley Neall, Tong Wu, Shengqu Cai, Gordon Wetzstein  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.18422v1.pdf)  
  Keywords: diffusion transformer, dit, interactive, video generation, simulation, camera control, diffusion model, world model, video diffusion  
- **[Predict to Skip: Linear Multistep Feature Forecasting for Efficient Diffusion Transformers](https://arxiv.org/abs/2602.18093v1)**  
  Authors: Hanshuai Cui, Zhiqing Tang, Qianli Ma, Zhi Yao, Weijia Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.18093v1.pdf)  
  Keywords: efficient, diffusion transformer, dit, dynamics, trajectory, video generation, acceleration, denoising  
- **[Factored Latent Action World Models](https://arxiv.org/abs/2602.16229v1)**  
  Authors: Zizhao Wang, Chang Shi, Jiaheng Hu, Kevin Rohling, Roberto Martín-Martín, Amy Zhang, Peter Stone  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.16229v1.pdf)  
  Keywords: dynamics, simulation, video generation, world model, controllable  
- **[AnchorWeave: World-Consistent Video Generation with Retrieved Local Spatial Memories](https://arxiv.org/abs/2602.14941v1)**  
  Authors: Zun Wang, Han Lin, Jaehong Yoon, Jaemin Cho, Yue Zhang, Mohit Bansal  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.14941v1.pdf)  
  Keywords: trajectory, dit, controllable, video generation  
- **[DCDM: Divide-and-Conquer Diffusion Models for Consistency-Preserving Video Generation](https://arxiv.org/abs/2602.13637v1)**  
  Authors: Haoyu Zhao, Yuang Zhang, Junqi Cheng, Jiaxi Gu, Zenghui Lu, Peng Shu, Zuxuan Wu, Yu-Gang Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.13637v1.pdf)  
  Keywords: diffusion transformer, motion control, video generation, identity, diffusion model  
- **[FlexAM: Flexible Appearance-Motion Decomposition for Versatile Video Generation Control](https://arxiv.org/abs/2602.13185v1)**  
  Authors: Mingzhi Sheng, Zekai Gu, Peng Li, Cheng Lin, Hao-Xiang Guo, Ying-Cong Chen, Yuan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.13185v1.pdf)  
  Keywords: dit, dynamics, video generation, camera control, i2v  
- **[VimRAG: Navigating Massive Visual Context in Retrieval-Augmented Generation via Multimodal Memory Graph](https://arxiv.org/abs/2602.12735v1)**  
  Authors: Qiuchen Wang, Shihang Wang, Yu Zeng, Qiang Zhang, Fanrui Zhang, Zhuoning Guo, Bosi Zhang, Wenxuan Huang, Lin Chen, Zehui Chen, Pengjun Xie, Ruixue Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.12735v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Alibaba-NLP/VRAG?style=social)](https://github.com/Alibaba-NLP/VRAG)  
  Keywords: trajectory, dit, benchmark  
- **[Dual-Granularity Contrastive Reward via Generated Episodic Guidance for Efficient Embodied RL](https://arxiv.org/abs/2602.12636v1)**  
  Authors: Xin Liu, Yixuan Li, Yuhui Chen, Yuxing Qin, Haoran Li, Dongbin Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.12636v1.pdf)  
  Keywords: trajectory, efficient, simulation, video generation  
- **[DreamID-Omni: Unified Framework for Controllable Human-Centric Audio-Video Generation](https://arxiv.org/abs/2602.12160v1)**  
  Authors: Xu Guo, Fulong Ye, Qichao Sun, Liyang Chen, Bingchuan Li, Pengze Zhang, Jiawei Liu, Songtao Zhao, Qian He, Xiangwang Hou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.12160v1.pdf)  
  Keywords: diffusion transformer, dit, video generation, identity, audio-driven, video editing, controllable  

### Human & Character Animation

- **[Ani3DHuman: Photorealistic 3D Human Animation with Self-guided Stochastic Sampling](https://arxiv.org/abs/2602.19089v1)**  
  Authors: Qi Sun, Can Wang, Jiaxiang Shang, Yingchun Liu, Jing Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.19089v1.pdf) | [![GitHub](https://img.shields.io/github/stars/qiisun/ani3dhuman?style=social)](https://github.com/qiisun/ani3dhuman)  
  Keywords: dynamics, human animation, identity, diffusion model, video diffusion  
- **[HairWeaver: Few-Shot Photorealistic Hair Motion Synthesis with Sim-to-Real Guided Video Diffusion](https://arxiv.org/abs/2602.11117v1)**  
  Authors: Di Chang, Ji Hou, Aljaz Bozic, Assaf Neuberger, Felix Juefei-Xu, Olivier Maury, Gene Wei-Chin Lin, Tuur Stuyck, Doug Roble, Mohammad Soleymani, Stephane Grabli  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.11117v1.pdf)  
  Keywords: dit, dynamics, evaluation, human motion, video diffusion  
- **[Hand2World: Autoregressive Egocentric Interaction Generation via Free-Space Hand Gestures](https://arxiv.org/abs/2602.09600v2)**  
  Authors: Yuxi Wang, Wenqi Ouyang, Tianyi Wei, Yi Dong, Zhiqi Shen, Xingang Pan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.09600v2.pdf)  
  Keywords: dit, gesture, interactive, dynamics, video generation, camera control, autoregressive, benchmark, diffusion model, world model  
- **[AUHead: Realistic Emotional Talking Head Generation via Action Units Control](https://arxiv.org/abs/2602.09534v1)**  
  Authors: Jiayi Lyu, Leigang Qu, Wenjing Zhang, Hanyu Jiang, Kai Liu, Zhenglin Zhou, Xiaobo Xia, Jian Xue, Tat-Seng Chua  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.09534v1.pdf) | [![GitHub](https://img.shields.io/github/stars/laura990501/AUHead_ICLR?style=social)](https://github.com/laura990501/AUHead_ICLR)  
  Keywords: motion control, dit, interactive, talking head, video generation, identity, benchmark, diffusion model, avatar, film, controllable  
- **[SoulX-FlashHead: Oracle-guided Generation of Infinite Real-time Streaming Talking Heads](https://arxiv.org/abs/2602.07449v3)**  
  Authors: Tan Yu, Qian Qiao, Le Shen, Ke Zhou, Jincheng Hu, Dian Sheng, Bo Hu, Haoming Qin, Jun Gao, Changhai Zhou, Shunshun Yin, Siyuan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.07449v3.pdf)  
  Keywords: talking head, physical, video generation, autoregressive, streaming, identity, distillation, benchmark, audio-driven  
- **[From Blurry to Believable: Enhancing Low-quality Talking Heads with 3D Generative Priors](https://arxiv.org/abs/2602.06122v1)**  
  Authors: Ding-Jiun Huang, Yuanhao Wang, Shao-Ji Yuan, Albert Mosella-Montoro, Francisco Vicente Carrasco, Cheng Zhang, Fernando De la Torre  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06122v1.pdf)  
  Keywords: dynamics, talking head, super-resolution, identity, avatar, temporal consistency  
- **[ShapeGaussian: High-Fidelity 4D Human Reconstruction in Monocular Videos via Vision Priors](https://arxiv.org/abs/2602.05572v1)**  
  Authors: Zhenxiao Liang, Ning Zhang, Youbao Tang, Ruei-Sung Lin, Qixing Huang, Peng Chang, Jing Xiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.05572v1.pdf)  
  Keywords: human motion  
- **[3D-Aware Implicit Motion Control for View-Adaptive Human Video Generation](https://arxiv.org/abs/2602.03796v2)**  
  Authors: Zhixue Fang, Xu He, Songlin Tang, Haoxian Zhang, Qingfeng Li, Xiaoqiang Liu, Pengfei Wan, Kun Gai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03796v2.pdf)  
  Keywords: dit, motion control, dynamics, human motion, video generation, camera control, 3d-aware  
- **[VRGaussianAvatar: Integrating 3D Gaussian Avatars into VR](https://arxiv.org/abs/2602.01674v1)**  
  Authors: Hail Song, Boram Yoon, Seokhwan Yang, Seoyoung Kang, Hyunjeong Kim, Henning Metzmacher, Woontack Woo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.01674v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vrgaussianavatar.github.io)  
  Keywords: interactive, avatar  
- **[Making Avatars Interact: Towards Text-Driven Human-Object Interaction for Controllable Talking Avatars](https://arxiv.org/abs/2602.01538v1)**  
  Authors: Youliang Zhang, Zhengguang Zhou, Zhentao Yu, Ziyao Huang, Teng Hu, Sen Liang, Guozhen Zhang, Ziqiao Peng, Shunkai Li, Yi Chen, Zixiang Zhou, Yuan Zhou, Qinglin Lu, Xiu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.01538v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://interactavatar.github.io)  
  Keywords: dit, video synthesis, human motion, video generation, benchmark, avatar, controllable  

### Image-to-Video Generation

- **[Frame2Freq: Spectral Adapters for Fine-Grained Video Understanding](https://arxiv.org/abs/2602.18977v1)**  
  Authors: Thinesh Thiyakesan Ponbagavathi, Constantin Seibold, Alina Roitberg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.18977v1.pdf) | [![GitHub](https://img.shields.io/github/stars/th-nesh/Frame2Freq?style=social)](https://github.com/th-nesh/Frame2Freq)  
  Keywords: image-to-video, dynamics  
- **[FlexAM: Flexible Appearance-Motion Decomposition for Versatile Video Generation Control](https://arxiv.org/abs/2602.13185v1)**  
  Authors: Mingzhi Sheng, Zekai Gu, Peng Li, Cheng Lin, Hao-Xiang Guo, Ying-Cong Chen, Yuan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.13185v1.pdf)  
  Keywords: dit, dynamics, video generation, camera control, i2v  
- **[Motion Prior Distillation in Time Reversal Sampling for Generative Inbetweening](https://arxiv.org/abs/2602.12679v2)**  
  Authors: Wooseok Jeon, Seunghyun Shin, Dongmin Shin, Hae-Gon Jeon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.12679v2.pdf)  
  Keywords: image-to-video, dit, evaluation, distillation, benchmark, diffusion model, i2v, denoising  
- **[ConsID-Gen: View-Consistent and Identity-Preserving Image-to-Video Generation](https://arxiv.org/abs/2602.10113v1)**  
  Authors: Mingyang Wu, Ashirbad Mishra, Soumik Dey, Shuo Xing, Naveen Ravipati, Hansi Wu, Binbin Li, Zhengzhong Tu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.10113v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://myangwu.github.io/ConsID-Gen)  
  Keywords: image-to-video, diffusion transformer, text-to-video, dit, evaluation, video generation, identity, benchmark, i2v  
- **[Monocular Normal Estimation via Shading Sequence Estimation](https://arxiv.org/abs/2602.09929v2)**  
  Authors: Zongrui Li, Xinhua Ma, Minghui Hu, Yunqing Zhao, Yingchen Yu, Qian Zheng, Chang Liu, Xudong Jiang, Song Bai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.09929v2.pdf)  
  Keywords: image-to-video, dit, benchmark  
- **[Tele-Omni: a Unified Multimodal Framework for Video Generation and Editing](https://arxiv.org/abs/2602.09609v1)**  
  Authors: Jialun Liu, Yukuo Ma, Xiao Cao, Tian Li, Gonghu Shang, Haibin Huang, Chi Zhang, Xuelong Li, Cong Liu, Junqi Liu, Jiakui Hu, Robby T. Tan, Shiwen Zhang, Liying Yang, Xiaoyan Yang, Qizhen Weng, Xiangzhen Chang, Yuanzhi Liang, Yifan Xu, Zhiyong Huang, Zuoxin Li, Xuelong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.09609v1.pdf)  
  Keywords: image-to-video, text-to-video, dit, video synthesis, video generation, video editing  
- **[ReRoPE: Repurposing RoPE for Relative Camera Control](https://arxiv.org/abs/2602.08068v1)**  
  Authors: Chunyang Li, Yuanbo Yang, Jiahao Shao, Hongyu Zhou, Katja Schwarz, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.08068v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://sisyphe-lee.github.io/ReRoPE)  
  Keywords: image-to-video, efficient, interactive, video generation, simulation, video-to-video, camera control, diffusion model, i2v, video diffusion, controllable  
- **[RISE-Video: Can Video Generators Decode Implicit World Rules?](https://arxiv.org/abs/2602.05986v1)**  
  Authors: Mingxin Liu, Shuran Ma, Shibei Meng, Xiangyu Zhao, Zicheng Zhang, Shaofeng Zhang, Zhihang Zhong, Peixian Chen, Haoyu Cao, Xing Sun, Haodong Duan, Xue Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.05986v1.pdf)  
  Keywords: image-to-video, dynamics, evaluation, physical, i2v, benchmark, temporal consistency  
- **[FSVideo: Fast Speed Video Diffusion Model in a Highly-Compressed Latent Space](https://arxiv.org/abs/2602.02092v1)**  
  Authors: FSVideo Team, Qingyu Chen, Zhiyuan Fang, Haibin Huang, Xinwei Huang, Tong Jin, Minxuan Lin, Bo Liu, Celong Liu, Chongyang Ma, Xing Mei, Xiaohui Shen, Yaojie Shen, Fuwen Tan, Angtian Wang, Xiao Yang, Yiding Yang, Jiamin Yuan, Lingxi Zhang, Yuxin Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.02092v1.pdf)  
  Keywords: image-to-video, diffusion transformer, dit, architecture, diffusion model, i2v, video diffusion  
- **[Grounding Generated Videos in Feasible Plans via World Models](https://arxiv.org/abs/2602.01960v1)**  
  Authors: Christos Ziakas, Amir Bar, Alessandra Russo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.01960v1.pdf)  
  Keywords: image-to-video, dit, dynamics, trajectory, action-conditioned, physical, simulation, temporal consistency, world model  

### Long Video Generation

*Showing the latest 50 out of 126 papers*

- **[VideoSketcher: Video Models Prior Enable Versatile Sequential Sketch Generation](https://arxiv.org/abs/2602.15819v1)**  
  Authors: Hui Ren, Yuval Alaluf, Omer Bar Tal, Alexander Schwing, Antonio Torralba, Yael Vinker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.15819v1.pdf)  
  Keywords: efficient, style, text-to-video, creative, dit, interactive, autoregressive, diffusion model, video diffusion  
- **[World Action Models are Zero-shot Policies](https://arxiv.org/abs/2602.15922v1)**  
  Authors: Seonghyeon Ye, Yunhao Ge, Kaiyuan Zheng, Shenyuan Gao, Sihyun Yu, George Kurian, Suneel Indupuru, You Liang Tan, Chuning Zhu, Jiannan Xiang, Ayaan Malik, Kyungmin Lee, William Liang, Nadun Ranawaka, Jiasheng Gu, Yinzhen Xu, Guanzhi Wang, Fengyuan Hu, Avnish Narayan, Johan Bjorck, Jing Wang, Gwanghyun Kim, Dantong Niu, Ruijie Zheng, Yuqi Xie, Jimmy Wu, Qi Wang, Ryan Julian, Danfei Xu, Yilun Du, Yevgen Chebotar, Scott Reed, Jan Kautz, Yuke Zhu, Linxi "Jim" Fan, Joel Jang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.15922v1.pdf)  
  Keywords: dynamics, physical, autoregressive, diffusion model, video diffusion  
- **[Consistency-Preserving Diverse Video Generation](https://arxiv.org/abs/2602.15287v1)**  
  Authors: Xinshuang Liu, Runfa Blark Li, Truong Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.15287v1.pdf)  
  Keywords: temporal consistency, text-to-video, video generation  
- **[Adapting VACE for Real-Time Autoregressive Video Diffusion](https://arxiv.org/abs/2602.14381v1)**  
  Authors: Ryan Fosdick  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.14381v1.pdf) | [![GitHub](https://img.shields.io/github/stars/daydreamlive/scope?style=social)](https://github.com/daydreamlive/scope)  
  Keywords: dit, video generation, autoregressive, streaming, video diffusion  
- **[Train Short, Inference Long: Training-free Horizon Extension for Autoregressive Video Generation](https://arxiv.org/abs/2602.14027v2)**  
  Authors: Jia Li, Xiaomeng Fu, Xurui Peng, Weifeng Chen, Youwei Zheng, Tianyu Zhao, Jiexi Wang, Fangmin Chen, Xing Wang, Hayden Kwok-Hay So  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.14027v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ga-lee.github.io/FLEX_demo.) | [![Demo](https://img.shields.io/badge/-Demo-brightgreen)](https://ga-lee.github.io/FLEX_demo)  
  Keywords: long video, evaluation, video synthesis, video generation, autoregressive, diffusion model, video diffusion  
- **[High-Fidelity Causal Video Diffusion Models for Real-Time Ultra-Low-Bitrate Semantic Communication](https://arxiv.org/abs/2602.13837v1)**  
  Authors: Cem Eteke, Batuhan Tosun, Alexander Griessel, Wolfgang Kellerer, Eckehard Steinbach  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.13837v1.pdf)  
  Keywords: efficient, evaluation, video generation, distillation, diffusion model, temporal consistency, video diffusion  
- **[EchoTorrent: Towards Swift, Sustained, and Streaming Multi-Modal Video Generation](https://arxiv.org/abs/2602.13669v1)**  
  Authors: Rang Meng, Weipeng Wu, Yingjie Yin, Yuming Li, Chenguang Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.13669v1.pdf)  
  Keywords: architecture, video generation, autoregressive, streaming, multi-modal, identity, temporal consistency  
- **[MonarchRT: Efficient Attention for Real-Time Video Generation](https://arxiv.org/abs/2602.12271v1)**  
  Authors: Krish Agarwal, Zhuoming Chen, Cheng Luo, Yongqi Chen, Haizhong Zheng, Xun Huang, Atri Rudra, Beidi Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.12271v1.pdf)  
  Keywords: efficient, diffusion transformer, video generation, autoregressive, diffusion model, video diffusion, denoising  
- **[Light4D: Training-Free Extreme Viewpoint 4D Video Relighting](https://arxiv.org/abs/2602.11769v1)**  
  Authors: Zhenghuang Wu, Kang Chen, Zeyu Zhang, Hao Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.11769v1.pdf) | [![GitHub](https://img.shields.io/github/stars/AIGeeksGroup/Light4D?style=social)](https://github.com/AIGeeksGroup/Light4D) | [![Project](https://img.shields.io/badge/-Project-blue)](https://aigeeksgroup.github.io/Light4D)  
  Keywords: temporal consistency, architecture  
- **[Flow caching for autoregressive video generation](https://arxiv.org/abs/2602.10825v1)**  
  Authors: Yuexiao Ma, Xuzhe Zheng, Jing Xu, Xiwei Xu, Feng Ling, Xiawu Zheng, Huafeng Kuang, Huixia Li, Xing Wang, Xuefeng Xiao, Fei Chao, Rongrong Ji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.10825v1.pdf) | [![GitHub](https://img.shields.io/github/stars/mikeallen39/FlowCache?style=social)](https://github.com/mikeallen39/FlowCache)  
  Keywords: efficient, dit, architecture, long video, video synthesis, video generation, autoregressive, benchmark, diffusion model, video diffusion, denoising  

### Personalization & Customization

*Showing the latest 50 out of 92 papers*

- **[Ani3DHuman: Photorealistic 3D Human Animation with Self-guided Stochastic Sampling](https://arxiv.org/abs/2602.19089v1)**  
  Authors: Qi Sun, Can Wang, Jiaxiang Shang, Yingchun Liu, Jing Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.19089v1.pdf) | [![GitHub](https://img.shields.io/github/stars/qiisun/ani3dhuman?style=social)](https://github.com/qiisun/ani3dhuman)  
  Keywords: dynamics, human animation, identity, diffusion model, video diffusion  
- **[EA-Swin: An Embedding-Agnostic Swin Transformer for AI-Generated Video Detection](https://arxiv.org/abs/2602.17260v1)**  
  Authors: Hung Mai, Loi Dinh, Duc Hai Nguyen, Dat Do, Luong Doan, Khanh Nguyen Quoc, Huan Vu, Phong Ho, Naeem Ul Islam, Tuan Do  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.17260v1.pdf)  
  Keywords: style, evaluation, benchmark  
- **[Xray-Visual Models: Scaling Vision models on Industry Scale Data](https://arxiv.org/abs/2602.16918v1)**  
  Authors: Shlok Mishra, Tsung-Yu Lin, Linda Wang, Hongli Xu, Yimin Liu, Michael Hsu, Chaitanya Ahuja, Hao Yuan, Jianpeng Cheng, Hong-You Chen, Haoyuan Xu, Chao Li, Abhijeet Awasthi, Jihye Moon, Don Husa, Michael Ge, Sumedha Singla, Arkabandhu Chowdhury, Phong Dingh, Satya Narayan Shukla, Yonghuan Yang, David Jacobs, Qi Guo, Jun Xiao, Xiangjun Fan, Aashu Singh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.16918v1.pdf)  
  Keywords: architecture, style, efficient, benchmark  
- **[VideoSketcher: Video Models Prior Enable Versatile Sequential Sketch Generation](https://arxiv.org/abs/2602.15819v1)**  
  Authors: Hui Ren, Yuval Alaluf, Omer Bar Tal, Alexander Schwing, Antonio Torralba, Yael Vinker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.15819v1.pdf)  
  Keywords: efficient, style, text-to-video, creative, dit, interactive, autoregressive, diffusion model, video diffusion  
- **[EchoTorrent: Towards Swift, Sustained, and Streaming Multi-Modal Video Generation](https://arxiv.org/abs/2602.13669v1)**  
  Authors: Rang Meng, Weipeng Wu, Yingjie Yin, Yuming Li, Chenguang Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.13669v1.pdf)  
  Keywords: architecture, video generation, autoregressive, streaming, multi-modal, identity, temporal consistency  
- **[DCDM: Divide-and-Conquer Diffusion Models for Consistency-Preserving Video Generation](https://arxiv.org/abs/2602.13637v1)**  
  Authors: Haoyu Zhao, Yuang Zhang, Junqi Cheng, Jiaxi Gu, Zenghui Lu, Peng Shu, Zuxuan Wu, Yu-Gang Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.13637v1.pdf)  
  Keywords: diffusion transformer, motion control, video generation, identity, diffusion model  
- **[DreamID-Omni: Unified Framework for Controllable Human-Centric Audio-Video Generation](https://arxiv.org/abs/2602.12160v1)**  
  Authors: Xu Guo, Fulong Ye, Qichao Sun, Liyang Chen, Bingchuan Li, Pengze Zhang, Jiawei Liu, Songtao Zhao, Qian He, Xiangwang Hou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.12160v1.pdf)  
  Keywords: diffusion transformer, dit, video generation, identity, audio-driven, video editing, controllable  
- **[OmniCustom: Sync Audio-Video Customization Via Joint Audio-Video Generation Model](https://arxiv.org/abs/2602.12304v1)**  
  Authors: Maomao Li, Zhen Li, Kaipeng Zhang, Guosheng Yin, Zhifeng Li, Dong Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.12304v1.pdf)  
  Keywords: dit, flow matching, video generation, identity, customization  
- **[Ctrl&Shift: High-Quality Geometry-Aware Object Manipulation in Visual Generation](https://arxiv.org/abs/2602.11440v1)**  
  Authors: Penghui Ruan, Bojia Zi, Xianbiao Qi, Youze Huang, Rong Xiao, Pichao Wang, Jiannong Cao, Yuhui Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.11440v1.pdf)  
  Keywords: creative, dit, identity, film, controllable  
- **[ConsID-Gen: View-Consistent and Identity-Preserving Image-to-Video Generation](https://arxiv.org/abs/2602.10113v1)**  
  Authors: Mingyang Wu, Ashirbad Mishra, Soumik Dey, Shuo Xing, Naveen Ravipati, Hansi Wu, Binbin Li, Zhengzhong Tu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.10113v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://myangwu.github.io/ConsID-Gen)  
  Keywords: image-to-video, diffusion transformer, text-to-video, dit, evaluation, video generation, identity, benchmark, i2v  

### Physical Understanding

*Showing the latest 50 out of 131 papers*

- **[UniE2F: A Unified Diffusion Framework for Event-to-Frame Reconstruction with Video Foundation Models](https://arxiv.org/abs/2602.19202v1)**  
  Authors: Gang Xu, Zhiyu Zhu, Junhui Hou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.19202v1.pdf) | [![GitHub](https://img.shields.io/github/stars/CS-GangXu/UniE2F?style=social)](https://github.com/CS-GangXu/UniE2F)  
  Keywords: dit, physical, frame interpolation, diffusion model, video diffusion  
- **[Ani3DHuman: Photorealistic 3D Human Animation with Self-guided Stochastic Sampling](https://arxiv.org/abs/2602.19089v1)**  
  Authors: Qi Sun, Can Wang, Jiaxiang Shang, Yingchun Liu, Jing Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.19089v1.pdf) | [![GitHub](https://img.shields.io/github/stars/qiisun/ani3dhuman?style=social)](https://github.com/qiisun/ani3dhuman)  
  Keywords: dynamics, human animation, identity, diffusion model, video diffusion  
- **[Frame2Freq: Spectral Adapters for Fine-Grained Video Understanding](https://arxiv.org/abs/2602.18977v1)**  
  Authors: Thinesh Thiyakesan Ponbagavathi, Constantin Seibold, Alina Roitberg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.18977v1.pdf) | [![GitHub](https://img.shields.io/github/stars/th-nesh/Frame2Freq?style=social)](https://github.com/th-nesh/Frame2Freq)  
  Keywords: image-to-video, dynamics  
- **[RoboCurate: Harnessing Diversity with Action-Verified Neural Trajectory for Robot Learning](https://arxiv.org/abs/2602.18742v1)**  
  Authors: Seungku Kim, Suhyeok Jang, Byungjun Yoon, Dongyoung Kim, John Won, Jinwoo Shin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.18742v1.pdf)  
  Keywords: dit, trajectory, physical, simulation, video-to-video  
- **[Predict to Skip: Linear Multistep Feature Forecasting for Efficient Diffusion Transformers](https://arxiv.org/abs/2602.18093v1)**  
  Authors: Hanshuai Cui, Zhiqing Tang, Qianli Ma, Zhi Yao, Weijia Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.18093v1.pdf)  
  Keywords: efficient, diffusion transformer, dit, dynamics, trajectory, video generation, acceleration, denoising  
- **[Factored Latent Action World Models](https://arxiv.org/abs/2602.16229v1)**  
  Authors: Zizhao Wang, Chang Shi, Jiaheng Hu, Kevin Rohling, Roberto Martín-Martín, Amy Zhang, Peter Stone  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.16229v1.pdf)  
  Keywords: dynamics, simulation, video generation, world model, controllable  
- **[World Action Models are Zero-shot Policies](https://arxiv.org/abs/2602.15922v1)**  
  Authors: Seonghyeon Ye, Yunhao Ge, Kaiyuan Zheng, Shenyuan Gao, Sihyun Yu, George Kurian, Suneel Indupuru, You Liang Tan, Chuning Zhu, Jiannan Xiang, Ayaan Malik, Kyungmin Lee, William Liang, Nadun Ranawaka, Jiasheng Gu, Yinzhen Xu, Guanzhi Wang, Fengyuan Hu, Avnish Narayan, Johan Bjorck, Jing Wang, Gwanghyun Kim, Dantong Niu, Ruijie Zheng, Yuqi Xie, Jimmy Wu, Qi Wang, Ryan Julian, Danfei Xu, Yilun Du, Yevgen Chebotar, Scott Reed, Jan Kautz, Yuke Zhu, Linxi "Jim" Fan, Joel Jang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.15922v1.pdf)  
  Keywords: dynamics, physical, autoregressive, diffusion model, video diffusion  
- **[Integrating Affordances and Attention models for Short-Term Object Interaction Anticipation](https://arxiv.org/abs/2602.14837v1)**  
  Authors: Lorenzo Mur Labadia, Ruben Martinez-Cantin, Jose J. Guerrero, Giovanni M. Farinella, Antonino Furnari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.14837v1.pdf)  
  Keywords: physical, architecture  
- **[FlexAM: Flexible Appearance-Motion Decomposition for Versatile Video Generation Control](https://arxiv.org/abs/2602.13185v1)**  
  Authors: Mingzhi Sheng, Zekai Gu, Peng Li, Cheng Lin, Hao-Xiang Guo, Ying-Cong Chen, Yuan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.13185v1.pdf)  
  Keywords: dit, dynamics, video generation, camera control, i2v  
- **[SurfPhase: 3D Interfacial Dynamics in Two-Phase Flows from Sparse Videos](https://arxiv.org/abs/2602.11154v1)**  
  Authors: Yue Gao, Hong-Xing Yu, Sanghyeon Chang, Qianxi Fu, Bo Zhu, Yoonjin Won, Juan Carlos Niebles, Jiajun Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.11154v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yuegao.me/SurfPhase)  
  Keywords: dynamics, video diffusion, diffusion model  

### Surveys & Benchmarks

*Showing the latest 50 out of 197 papers*

- **[JavisDiT++: Unified Modeling and Optimization for Joint Audio-Video Generation](https://arxiv.org/abs/2602.19163v1)**  
  Authors: Kai Liu, Yanhao Zheng, Kai Wang, Shengqiong Wu, Rongjunchen Zhang, Jiebo Luo, Dimitrios Hatzinakos, Ziwei Liu, Hao Fei, Tat-Seng Chua  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.19163v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://JavisVerse.github.io/JavisDiT2-page)  
  Keywords: t2v, dit, evaluation, sound, video generation  
- **[VQPP: Video Query Performance Prediction Benchmark](https://arxiv.org/abs/2602.17814v1)**  
  Authors: Adrian Catalin Lutu, Eduard Poesina, Radu Tudor Ionescu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.17814v1.pdf) | [![GitHub](https://img.shields.io/github/stars/AdrianLutu/VQPP?style=social)](https://github.com/AdrianLutu/VQPP)  
  Keywords: text-to-video, benchmark  
- **[EA-Swin: An Embedding-Agnostic Swin Transformer for AI-Generated Video Detection](https://arxiv.org/abs/2602.17260v1)**  
  Authors: Hung Mai, Loi Dinh, Duc Hai Nguyen, Dat Do, Luong Doan, Khanh Nguyen Quoc, Huan Vu, Phong Ho, Naeem Ul Islam, Tuan Do  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.17260v1.pdf)  
  Keywords: style, evaluation, benchmark  
- **[Xray-Visual Models: Scaling Vision models on Industry Scale Data](https://arxiv.org/abs/2602.16918v1)**  
  Authors: Shlok Mishra, Tsung-Yu Lin, Linda Wang, Hongli Xu, Yimin Liu, Michael Hsu, Chaitanya Ahuja, Hao Yuan, Jianpeng Cheng, Hong-You Chen, Haoyuan Xu, Chao Li, Abhijeet Awasthi, Jihye Moon, Don Husa, Michael Ge, Sumedha Singla, Arkabandhu Chowdhury, Phong Dingh, Satya Narayan Shukla, Yonghuan Yang, David Jacobs, Qi Guo, Jun Xiao, Xiangjun Fan, Aashu Singh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.16918v1.pdf)  
  Keywords: architecture, style, efficient, benchmark  
- **[When Test-Time Guidance Is Enough: Fast Image and Video Editing with Diffusion Guidance](https://arxiv.org/abs/2602.14157v1)**  
  Authors: Ahmed Ghorbel, Badr Moufad, Navid Bagheri Shouraki, Alain Oliviero Durmus, Thomas Hirtz, Eric Moulines, Jimmy Olsson, Yazid Janati  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.14157v1.pdf)  
  Keywords: dit, evaluation, video editing, benchmark  
- **[Train Short, Inference Long: Training-free Horizon Extension for Autoregressive Video Generation](https://arxiv.org/abs/2602.14027v2)**  
  Authors: Jia Li, Xiaomeng Fu, Xurui Peng, Weifeng Chen, Youwei Zheng, Tianyu Zhao, Jiexi Wang, Fangmin Chen, Xing Wang, Hayden Kwok-Hay So  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.14027v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ga-lee.github.io/FLEX_demo.) | [![Demo](https://img.shields.io/badge/-Demo-brightgreen)](https://ga-lee.github.io/FLEX_demo)  
  Keywords: long video, evaluation, video synthesis, video generation, autoregressive, diffusion model, video diffusion  
- **[High-Fidelity Causal Video Diffusion Models for Real-Time Ultra-Low-Bitrate Semantic Communication](https://arxiv.org/abs/2602.13837v1)**  
  Authors: Cem Eteke, Batuhan Tosun, Alexander Griessel, Wolfgang Kellerer, Eckehard Steinbach  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.13837v1.pdf)  
  Keywords: efficient, evaluation, video generation, distillation, diffusion model, temporal consistency, video diffusion  
- **[VimRAG: Navigating Massive Visual Context in Retrieval-Augmented Generation via Multimodal Memory Graph](https://arxiv.org/abs/2602.12735v1)**  
  Authors: Qiuchen Wang, Shihang Wang, Yu Zeng, Qiang Zhang, Fanrui Zhang, Zhuoning Guo, Bosi Zhang, Wenxuan Huang, Lin Chen, Zehui Chen, Pengjun Xie, Ruixue Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.12735v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Alibaba-NLP/VRAG?style=social)](https://github.com/Alibaba-NLP/VRAG)  
  Keywords: trajectory, dit, benchmark  
- **[AdaCorrection: Adaptive Offset Cache Correction for Accurate Diffusion Transformers](https://arxiv.org/abs/2602.13357v1)**  
  Authors: Dong Liu, Yanxuan Yu, Ben Lengerich, Ying Nian Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.13357v1.pdf)  
  Keywords: efficient, diffusion transformer, dit, video generation, acceleration, benchmark, video diffusion, denoising  
- **[Motion Prior Distillation in Time Reversal Sampling for Generative Inbetweening](https://arxiv.org/abs/2602.12679v2)**  
  Authors: Wooseok Jeon, Seunghyun Shin, Dongmin Shin, Hae-Gon Jeon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.12679v2.pdf)  
  Keywords: image-to-video, dit, evaluation, distillation, benchmark, diffusion model, i2v, denoising  

### Text-to-Video Generation

*Showing the latest 50 out of 71 papers*

- **[JavisDiT++: Unified Modeling and Optimization for Joint Audio-Video Generation](https://arxiv.org/abs/2602.19163v1)**  
  Authors: Kai Liu, Yanhao Zheng, Kai Wang, Shengqiong Wu, Rongjunchen Zhang, Jiebo Luo, Dimitrios Hatzinakos, Ziwei Liu, Hao Fei, Tat-Seng Chua  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.19163v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://JavisVerse.github.io/JavisDiT2-page)  
  Keywords: t2v, dit, evaluation, sound, video generation  
- **[VQPP: Video Query Performance Prediction Benchmark](https://arxiv.org/abs/2602.17814v1)**  
  Authors: Adrian Catalin Lutu, Eduard Poesina, Radu Tudor Ionescu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.17814v1.pdf) | [![GitHub](https://img.shields.io/github/stars/AdrianLutu/VQPP?style=social)](https://github.com/AdrianLutu/VQPP)  
  Keywords: text-to-video, benchmark  
- **[CHAI: CacHe Attention Inference for text2video](https://arxiv.org/abs/2602.16132v1)**  
  Authors: Joel Mathew Cherian, Ashutosh Muralidhara Bharadwaj, Vima Gupta, Anand Padmanabha Iyer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.16132v1.pdf)  
  Keywords: text-to-video, t2v, diffusion model, video diffusion, denoising  
- **[VideoSketcher: Video Models Prior Enable Versatile Sequential Sketch Generation](https://arxiv.org/abs/2602.15819v1)**  
  Authors: Hui Ren, Yuval Alaluf, Omer Bar Tal, Alexander Schwing, Antonio Torralba, Yael Vinker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.15819v1.pdf)  
  Keywords: efficient, style, text-to-video, creative, dit, interactive, autoregressive, diffusion model, video diffusion  
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
  Keywords: image-to-video, diffusion transformer, text-to-video, dit, evaluation, video generation, identity, benchmark, i2v  
- **[Tele-Omni: a Unified Multimodal Framework for Video Generation and Editing](https://arxiv.org/abs/2602.09609v1)**  
  Authors: Jialun Liu, Yukuo Ma, Xiao Cao, Tian Li, Gonghu Shang, Haibin Huang, Chi Zhang, Xuelong Li, Cong Liu, Junqi Liu, Jiakui Hu, Robby T. Tan, Shiwen Zhang, Liying Yang, Xiaoyan Yang, Qizhen Weng, Xiangzhen Chang, Yuanzhi Liang, Yifan Xu, Zhiyong Huang, Zuoxin Li, Xuelong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.09609v1.pdf)  
  Keywords: image-to-video, text-to-video, dit, video synthesis, video generation, video editing  
- **[Omni-Video 2: Scaling MLLM-Conditioned Diffusion for Unified Video Generation and Editing](https://arxiv.org/abs/2602.08820v1)**  
  Authors: Hao Yang, Zhiyu Tan, Jia Gong, Luozheng Qin, Hesen Chen, Xiaomeng Yang, Yuqing Sun, Yuetan Lin, Mengping Yang, Hao Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.08820v1.pdf)  
  Keywords: efficient, text-to-video, dit, video generation, benchmark, diffusion model, video editing, video diffusion  
- **[MOVA: Towards Scalable and Synchronized Video-Audio Generation](https://arxiv.org/abs/2602.08794v2)**  
  Authors: SII-OpenMOSS Team, :, Donghua Yu, Mingshu Chen, Qi Chen, Qi Luo, Qianyi Wu, Qinyuan Cheng, Ruixiao Li, Tianyi Liang, Wenbo Zhang, Wenming Tu, Xiangyu Peng, Yang Gao, Yanru Huo, Ying Zhu, Yinze Luo, Yiyang Zhang, Yuerong Song, Zhe Xu, Zhiyu Zhang, Chenchen Yang, Cheng Chang, Chushu Zhou, Hanfu Chen, Hongnan Ma, Jiaxi Li, Jingqi Tong, Junxi Liu, Ke Chen, Shimin Li, Shiqi Jiang, Songlin Wang, Wei Jiang, Zhaoye Fei, Zhiyuan Ning, Chunguo Li, Chenhui Li, Ziwei He, Zengfeng Huang, Xie Chen, Xipeng Qiu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.08794v2.pdf)  
  Keywords: efficient, t2v, architecture, text to video, sound  

### Video Editing

- **[RoboCurate: Harnessing Diversity with Action-Verified Neural Trajectory for Robot Learning](https://arxiv.org/abs/2602.18742v1)**  
  Authors: Seungku Kim, Suhyeok Jang, Byungjun Yoon, Dongyoung Kim, John Won, Jinwoo Shin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.18742v1.pdf)  
  Keywords: dit, trajectory, physical, simulation, video-to-video  
- **[When Test-Time Guidance Is Enough: Fast Image and Video Editing with Diffusion Guidance](https://arxiv.org/abs/2602.14157v1)**  
  Authors: Ahmed Ghorbel, Badr Moufad, Navid Bagheri Shouraki, Alain Oliviero Durmus, Thomas Hirtz, Eric Moulines, Jimmy Olsson, Yazid Janati  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.14157v1.pdf)  
  Keywords: dit, evaluation, video editing, benchmark  
- **[DreamID-Omni: Unified Framework for Controllable Human-Centric Audio-Video Generation](https://arxiv.org/abs/2602.12160v1)**  
  Authors: Xu Guo, Fulong Ye, Qichao Sun, Liyang Chen, Bingchuan Li, Pengze Zhang, Jiawei Liu, Songtao Zhao, Qian He, Xiangwang Hou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.12160v1.pdf)  
  Keywords: diffusion transformer, dit, video generation, identity, audio-driven, video editing, controllable  
- **[Tele-Omni: a Unified Multimodal Framework for Video Generation and Editing](https://arxiv.org/abs/2602.09609v1)**  
  Authors: Jialun Liu, Yukuo Ma, Xiao Cao, Tian Li, Gonghu Shang, Haibin Huang, Chi Zhang, Xuelong Li, Cong Liu, Junqi Liu, Jiakui Hu, Robby T. Tan, Shiwen Zhang, Liying Yang, Xiaoyan Yang, Qizhen Weng, Xiangzhen Chang, Yuanzhi Liang, Yifan Xu, Zhiyong Huang, Zuoxin Li, Xuelong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.09609v1.pdf)  
  Keywords: image-to-video, text-to-video, dit, video synthesis, video generation, video editing  
- **[Omni-Video 2: Scaling MLLM-Conditioned Diffusion for Unified Video Generation and Editing](https://arxiv.org/abs/2602.08820v1)**  
  Authors: Hao Yang, Zhiyu Tan, Jia Gong, Luozheng Qin, Hesen Chen, Xiaomeng Yang, Yuqing Sun, Yuetan Lin, Mengping Yang, Hao Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.08820v1.pdf)  
  Keywords: efficient, text-to-video, dit, video generation, benchmark, diffusion model, video editing, video diffusion  
- **[PISCO: Precise Video Instance Insertion with Sparse Control](https://arxiv.org/abs/2602.08277v1)**  
  Authors: Xiangbo Gao, Renjie Li, Xinghao Chen, Yuheng Wu, Suofei Feng, Qing Yin, Zhengzhong Tu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.08277v1.pdf)  
  Keywords: film, dit, dynamics, physical, video generation, benchmark, diffusion model, video editing, video diffusion, controllable  
- **[ReRoPE: Repurposing RoPE for Relative Camera Control](https://arxiv.org/abs/2602.08068v1)**  
  Authors: Chunyang Li, Yuanbo Yang, Jiahao Shao, Hongyu Zhou, Katja Schwarz, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.08068v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://sisyphe-lee.github.io/ReRoPE)  
  Keywords: image-to-video, efficient, interactive, video generation, simulation, video-to-video, camera control, diffusion model, i2v, video diffusion, controllable  
- **[RFDM: Residual Flow Diffusion Model for Efficient Causal Video Editing](https://arxiv.org/abs/2602.06871v1)**  
  Authors: Mohammadreza Salehi, Mehdi Noroozi, Luca Morreale, Ruchika Chavhan, Malcolm Chadwick, Alberto Gil Ramos, Abhinav Mehrotra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06871v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://smsd75.github.io/RFDM_page)  
  Keywords: efficient, style, dit, video generation, video-to-video, autoregressive, benchmark, diffusion model, video editing, denoising  
- **[Continuous Control of Editing Models via Adaptive-Origin Guidance](https://arxiv.org/abs/2602.03826v1)**  
  Authors: Alon Wolf, Chen Katzir, Kfir Aberman, Or Patashnik  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03826v1.pdf)  
  Keywords: identity, video editing, dit, video manipulation  
- **[ProxyImg: Towards Highly-Controllable Image Representation via Hierarchical Disentangled Proxy Embedding](https://arxiv.org/abs/2602.01881v1)**  
  Authors: Ye Chen, Yupeng Zhu, Xiongzhen Zhang, Zhewen Wan, Yingzhe Li, Wenjun Zhang, Bingbing Ni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.01881v1.pdf)  
  Keywords: efficient, dit, interactive, dynamics, physical, physics, benchmark, temporal consistency, video editing, controllable  

### Video Inpainting & Completion

- **[Learning Physics-Grounded 4D Dynamics with Neural Gaussian Force Fields](https://arxiv.org/abs/2602.00148v2)**  
  Authors: Shiqian Li, Ruihong Shen, Junfeng Ni, Chang Pan, Chi Zhang, Yixin Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.00148v2.pdf)  
  Keywords: video prediction, interactive, dynamics, evaluation, physical, video generation, simulation, physics, world model  
- **[DriveLaW:Unifying Planning and Video Generation in a Latent Driving World](https://arxiv.org/abs/2512.23421v2)**  
  Authors: Tianze Xia, Yongkang Li, Lijun Zhou, Jingfeng Yao, Kaixin Xiong, Haiyang Sun, Bing Wang, Kun Ma, Guang Chen, Hangjun Ye, Wenyu Liu, Xinggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.23421v2.pdf)  
  Keywords: video prediction, architecture, trajectory, video generation, benchmark, autonomous driving, world model  
- **[Autoregressive Flow Matching for Motion Prediction](https://arxiv.org/abs/2512.22688v1)**  
  Authors: Johnathan Xie, Stefan Stojanov, Cristobal Eyzaguirre, Daniel L. K. Yamins, Jiajun Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.22688v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Johnathan-Xie/arfm-motion-prediction?style=social)](https://github.com/Johnathan-Xie/arfm-motion-prediction)  
  Keywords: video prediction, robotics, dit, human motion, flow matching, video generation, autoregressive, benchmark  
- **[Over++: Generative Video Compositing for Layer Interaction Effects](https://arxiv.org/abs/2512.19661v1)**  
  Authors: Luchao Qi, Jiaye Wu, Jun Myeong Choi, Cary Phillips, Roni Sengupta, Dan B Goldman  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.19661v1.pdf)  
  Keywords: video inpainting, dit  
- **[Vidarc: Embodied Video Diffusion Model for Closed-loop Control](https://arxiv.org/abs/2512.17661v1)**  
  Authors: Yao Feng, Chendong Xiang, Xinyi Mao, Hengkai Tan, Zuyue Zhang, Shuhe Huang, Kaiwen Zheng, Haitian Liu, Hang Su, Jun Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.17661v1.pdf)  
  Keywords: video prediction, dynamics, physical, autoregressive, diffusion model, video diffusion  
- **[Flowception: Temporally Expansive Flow Matching for Video Generation](https://arxiv.org/abs/2512.11438v1)**  
  Authors: Tariq Berrada Ifriqi, John Nguyen, Karteek Alahari, Jakob Verbeek, Ricky T. Q. Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.11438v1.pdf)  
  Keywords: image-to-video, efficient, flow matching, video generation, autoregressive, video interpolation, denoising  
- **[Astra: General Interactive World Model with Autoregressive Denoising](https://arxiv.org/abs/2512.08931v3)**  
  Authors: Yixuan Zhu, Jiaqi Feng, Wenzhao Zheng, Yuan Gao, Xin Tao, Pengfei Wan, Jie Zhou, Jiwen Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.08931v3.pdf)  
  Keywords: video prediction, diffusion transformer, architecture, interactive, video generation, camera control, autoregressive, streaming, autonomous driving, world model, denoising  
- **[InverseCrafter: Efficient Video ReCapture as a Latent Domain Inverse Problem](https://arxiv.org/abs/2512.05672v1)**  
  Authors: Yeobin Hong, Suhyeon Lee, Hyungjin Chung, Jong Chul Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.05672v1.pdf) | [![GitHub](https://img.shields.io/github/stars/yeobinhong/InverseCrafter?style=social)](https://github.com/yeobinhong/InverseCrafter)  
  Keywords: efficient, dit, video inpainting, video generation, camera control, 4d generation, novel view, diffusion model, video diffusion, controllable  

### Video Super-Resolution & Enhancement

*Showing the latest 50 out of 58 papers*

- **[UniE2F: A Unified Diffusion Framework for Event-to-Frame Reconstruction with Video Foundation Models](https://arxiv.org/abs/2602.19202v1)**  
  Authors: Gang Xu, Zhiyu Zhu, Junhui Hou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.19202v1.pdf) | [![GitHub](https://img.shields.io/github/stars/CS-GangXu/UniE2F?style=social)](https://github.com/CS-GangXu/UniE2F)  
  Keywords: dit, physical, frame interpolation, diffusion model, video diffusion  
- **[Predict to Skip: Linear Multistep Feature Forecasting for Efficient Diffusion Transformers](https://arxiv.org/abs/2602.18093v1)**  
  Authors: Hanshuai Cui, Zhiqing Tang, Qianli Ma, Zhi Yao, Weijia Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.18093v1.pdf)  
  Keywords: efficient, diffusion transformer, dit, dynamics, trajectory, video generation, acceleration, denoising  
- **[DDiT: Dynamic Patch Scheduling for Efficient Diffusion Transformers](https://arxiv.org/abs/2602.16968v1)**  
  Authors: Dahye Kim, Deepti Ghadiyaram, Raghudeep Gadde  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.16968v1.pdf)  
  Keywords: efficient, diffusion transformer, dit, video generation, denoising  
- **[CHAI: CacHe Attention Inference for text2video](https://arxiv.org/abs/2602.16132v1)**  
  Authors: Joel Mathew Cherian, Ashutosh Muralidhara Bharadwaj, Vima Gupta, Anand Padmanabha Iyer  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.16132v1.pdf)  
  Keywords: text-to-video, t2v, diffusion model, video diffusion, denoising  
- **[AdaCorrection: Adaptive Offset Cache Correction for Accurate Diffusion Transformers](https://arxiv.org/abs/2602.13357v1)**  
  Authors: Dong Liu, Yanxuan Yu, Ben Lengerich, Ying Nian Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.13357v1.pdf)  
  Keywords: efficient, diffusion transformer, dit, video generation, acceleration, benchmark, video diffusion, denoising  
- **[Motion Prior Distillation in Time Reversal Sampling for Generative Inbetweening](https://arxiv.org/abs/2602.12679v2)**  
  Authors: Wooseok Jeon, Seunghyun Shin, Dongmin Shin, Hae-Gon Jeon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.12679v2.pdf)  
  Keywords: image-to-video, dit, evaluation, distillation, benchmark, diffusion model, i2v, denoising  
- **[MonarchRT: Efficient Attention for Real-Time Video Generation](https://arxiv.org/abs/2602.12271v1)**  
  Authors: Krish Agarwal, Zhuoming Chen, Cheng Luo, Yongqi Chen, Haizhong Zheng, Xun Huang, Atri Rudra, Beidi Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.12271v1.pdf)  
  Keywords: efficient, diffusion transformer, video generation, autoregressive, diffusion model, video diffusion, denoising  
- **[FastFlow: Accelerating The Generative Flow Matching Models with Bandit Inference](https://arxiv.org/abs/2602.11105v1)**  
  Authors: Divya Jyoti Bajpai, Dhruv Bhardwaj, Soumya Roy, Tejas Duseja, Harsh Agarwal, Aashay Sandansing, Manjesh Kumar Hanawal  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.11105v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Div290/FastFlow?style=social)](https://github.com/Div290/FastFlow)  
  Keywords: efficient, dit, trajectory, flow matching, video generation, acceleration, distillation, denoising  
- **[Flow caching for autoregressive video generation](https://arxiv.org/abs/2602.10825v1)**  
  Authors: Yuexiao Ma, Xuzhe Zheng, Jing Xu, Xiwei Xu, Feng Ling, Xiawu Zheng, Huafeng Kuang, Huixia Li, Xing Wang, Xuefeng Xiao, Fei Chao, Rongrong Ji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.10825v1.pdf) | [![GitHub](https://img.shields.io/github/stars/mikeallen39/FlowCache?style=social)](https://github.com/mikeallen39/FlowCache)  
  Keywords: efficient, dit, architecture, long video, video synthesis, video generation, autoregressive, benchmark, diffusion model, video diffusion, denoising  
- **[Causality in Video Diffusers is Separable from Denoising](https://arxiv.org/abs/2602.10095v1)**  
  Authors: Xingjian Bai, Guande He, Zhengqi Li, Eli Shechtman, Xun Huang, Zongze Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.10095v1.pdf)  
  Keywords: architecture, trajectory, autoregressive, benchmark, diffusion model, denoising  

### World Models & Simulation

*Showing the latest 50 out of 101 papers*

- **[RoboCurate: Harnessing Diversity with Action-Verified Neural Trajectory for Robot Learning](https://arxiv.org/abs/2602.18742v1)**  
  Authors: Seungku Kim, Suhyeok Jang, Byungjun Yoon, Dongyoung Kim, John Won, Jinwoo Shin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.18742v1.pdf)  
  Keywords: dit, trajectory, physical, simulation, video-to-video  
- **[Generated Reality: Human-centric World Simulation using Interactive Video Generation with Hand and Camera Control](https://arxiv.org/abs/2602.18422v1)**  
  Authors: Linxi Xie, Lisong C. Sun, Ashley Neall, Tong Wu, Shengqu Cai, Gordon Wetzstein  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.18422v1.pdf)  
  Keywords: diffusion transformer, dit, interactive, video generation, simulation, camera control, diffusion model, world model, video diffusion  
- **[Factored Latent Action World Models](https://arxiv.org/abs/2602.16229v1)**  
  Authors: Zizhao Wang, Chang Shi, Jiaheng Hu, Kevin Rohling, Roberto Martín-Martín, Amy Zhang, Peter Stone  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.16229v1.pdf)  
  Keywords: dynamics, simulation, video generation, world model, controllable  
- **[VideoSketcher: Video Models Prior Enable Versatile Sequential Sketch Generation](https://arxiv.org/abs/2602.15819v1)**  
  Authors: Hui Ren, Yuval Alaluf, Omer Bar Tal, Alexander Schwing, Antonio Torralba, Yael Vinker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.15819v1.pdf)  
  Keywords: efficient, style, text-to-video, creative, dit, interactive, autoregressive, diffusion model, video diffusion  
- **[Dual-Granularity Contrastive Reward via Generated Episodic Guidance for Efficient Embodied RL](https://arxiv.org/abs/2602.12636v1)**  
  Authors: Xin Liu, Yixuan Li, Yuhui Chen, Yuxing Qin, Haoran Li, Dongbin Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.12636v1.pdf)  
  Keywords: trajectory, efficient, simulation, video generation  
- **[Chatting with Images for Introspective Visual Thinking](https://arxiv.org/abs/2602.11073v2)**  
  Authors: Junfei Wu, Jian Guan, Qiang Liu, Shu Wu, Liang Wang, Wei Wu, Tieniu Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.11073v2.pdf)  
  Keywords: interactive, benchmark  
- **[ArtisanGS: Interactive Tools for Gaussian Splat Selection with AI and Human in the Loop](https://arxiv.org/abs/2602.10173v1)**  
  Authors: Clement Fuji Tsang, Anita Hu, Or Perel, Carsten Kolve, Maria Shugrina  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.10173v1.pdf)  
  Keywords: dit, interactive, simulation, physics, diffusion model, video diffusion, controllable  
- **[Hand2World: Autoregressive Egocentric Interaction Generation via Free-Space Hand Gestures](https://arxiv.org/abs/2602.09600v2)**  
  Authors: Yuxi Wang, Wenqi Ouyang, Tianyi Wei, Yi Dong, Zhiqi Shen, Xingang Pan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.09600v2.pdf)  
  Keywords: dit, gesture, interactive, dynamics, video generation, camera control, autoregressive, benchmark, diffusion model, world model  
- **[AUHead: Realistic Emotional Talking Head Generation via Action Units Control](https://arxiv.org/abs/2602.09534v1)**  
  Authors: Jiayi Lyu, Leigang Qu, Wenjing Zhang, Hanyu Jiang, Kai Liu, Zhenglin Zhou, Xiaobo Xia, Jian Xue, Tat-Seng Chua  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.09534v1.pdf) | [![GitHub](https://img.shields.io/github/stars/laura990501/AUHead_ICLR?style=social)](https://github.com/laura990501/AUHead_ICLR)  
  Keywords: motion control, dit, interactive, talking head, video generation, identity, benchmark, diffusion model, avatar, film, controllable  
- **[WorldCompass: Reinforcement Learning for Long-Horizon World Models](https://arxiv.org/abs/2602.09022v1)**  
  Authors: Zehan Wang, Tengfei Wang, Haiyu Zhang, Xuhui Zuo, Junta Wu, Haoyuan Wang, Wenqiang Sun, Zhenwei Wang, Chenjie Cao, Hengshuang Zhao, Chunchao Guo, Zhou Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.09022v1.pdf)  
  Keywords: efficient, interactive, evaluation, video generation, autoregressive, world model  



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
