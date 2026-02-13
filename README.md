# Awesome Video Diffusions [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Video Diffusion Models and Video Generation. Content is automatically updated daily.

> Last Update: 2026-02-13 02:23:24

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
- [Applications](#applications) (59 papers) - Domain-specific applications of video diffusion models
- [Architecture & Efficiency](#architecture-&-efficiency) (368 papers) - Architectural innovations (DiT, UNet), flow matching, and training/inference efficiency
- [Audio & Multi-modal](#audio-&-multi-modal) (40 papers) - Audio-driven and multi-modal conditioned video generation
- [Controllable Generation](#controllable-generation) (118 papers) - Controllable video generation with motion, camera, pose, or layout guidance
- [Human & Character Animation](#human-&-character-animation) (37 papers) - Human-centric video generation including talking heads, dance, and character animation
- [Image-to-Video Generation](#image-to-video-generation) (42 papers) - Methods for animating still images into videos
- [Long Video Generation](#long-video-generation) (124 papers) - Generating temporally consistent long-form videos beyond short clips
- [Personalization & Customization](#personalization-&-customization) (89 papers) - Personalized video generation with custom subjects, identities, or styles
- [Physical Understanding](#physical-understanding) (137 papers) - Physics-aware video generation and dynamics modeling
- [Surveys & Benchmarks](#surveys-&-benchmarks) (206 papers) - Survey papers, benchmarks, and evaluation metrics for video generation
- [Text-to-Video Generation](#text-to-video-generation) (73 papers) - Foundation models and methods for generating videos from text prompts
- [Video Editing](#video-editing) (42 papers) - Diffusion-based video editing, style transfer, and manipulation
- [Video Inpainting & Completion](#video-inpainting-&-completion) (10 papers) - Video inpainting, completion, outpainting, and temporal prediction
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

- **[VideoNeuMat: Neural Material Extraction from Generative Video Models](https://arxiv.org/abs/2602.07272v1)**  
  Authors: Bowen Xue, Saeed Hadadan, Zheng Zeng, Fabrice Rousselle, Zahra Montazeri, Milos Hasan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.07272v1.pdf)  
  Keywords: dit, video diffusion, novel view, diffusion model  
- **[CineScene: Implicit 3D as Effective Scene Representation for Cinematic Video Generation](https://arxiv.org/abs/2602.06959v1)**  
  Authors: Kaiyi Huang, Yukun Huang, Yu Li, Jianhong Bai, Xintao Wang, Zinan Lin, Xuefei Ning, Jiwen Yu, Pengfei Wan, Yu Wang, Xihui Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06959v1.pdf)  
  Keywords: text-to-video, trajectory, dit, 3d-aware, video generation, physical, video synthesis  
- **[SkeletonGaussian: Editable 4D Generation through Gaussian Skeletonization](https://arxiv.org/abs/2602.04271v1)**  
  Authors: Lifan Wu, Ruijie Zhu, Yubo Ai, Tianzhu Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.04271v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wusar.github.io/projects/skeletongaussian)  
  Keywords: dit, 4d generation  
- **[3D-Aware Implicit Motion Control for View-Adaptive Human Video Generation](https://arxiv.org/abs/2602.03796v1)**  
  Authors: Zhixue Fang, Xu He, Songlin Tang, Haoxian Zhang, Qingfeng Li, Xiaoqiang Liu, Pengfei Wan, Kun Gai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03796v1.pdf)  
  Keywords: 3d-aware, dit, human motion, video generation, motion control, dynamics, camera control  
- **[FreeFix: Boosting 3D Gaussian Splatting via Fine-Tuning-Free Diffusion Models](https://arxiv.org/abs/2601.20857v1)**  
  Authors: Hongyu Zhou, Zisen Shao, Sheng Miao, Pan Wang, Dongfeng Bai, Bingbing Liu, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.20857v1.pdf)  
  Keywords: dit, video diffusion, novel view, diffusion model  
- **[AnyView: Synthesizing Any Novel View in Dynamic Scenes](https://arxiv.org/abs/2601.16982v1)**  
  Authors: Basile Van Hoorick, Dian Chen, Shun Iwase, Pavel Tokmakov, Muhammad Zubair Irshad, Igor Vasiljevic, Swati Gupta, Fangzhou Cheng, Sergey Zakharov, Vitor Campagnolo Guizilini  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.16982v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://tri-ml.github.io/AnyView)  
  Keywords: novel view, benchmark, video generation, temporal consistency  
- **[Memory-V2V: Augmenting Video-to-Video Diffusion Models with Memory](https://arxiv.org/abs/2601.16296v1)**  
  Authors: Dohun Lee, Chun-Hao Paul Huang, Xuelin Chen, Jong Chul Ye, Duygu Ceylan, Hyeonho Jeong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.16296v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://dohunlee1.github.io/MemoryV2V)  
  Keywords: novel view, video diffusion, long video, dit, diffusion model, video-to-video, video editing  
- **[GR3EN: Generative Relighting for 3D Environments](https://arxiv.org/abs/2601.16272v2)**  
  Authors: Xiaoyan Xing, Philipp Henzler, Junhwa Hur, Runze Li, Jonathan T. Barron, Pratul P. Srinivasan, Dor Verbin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.16272v2.pdf)  
  Keywords: novel view, controllable, video diffusion, dit, diffusion model, video-to-video  
- **[CamPilot: Improving Camera Control in Video Diffusion Model with Efficient Camera Reward Feedback](https://arxiv.org/abs/2601.16214v1)**  
  Authors: Wenhang Ge, Guibao Shen, Jiawei Feng, Luozhou Wang, Hao Lu, Xingye Tian, Xin Tao, Ying-Cong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.16214v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://a-bigbao.github.io/CamPilot)  
  Keywords: novel view, video diffusion, benchmark, diffusion model, efficient, camera control  
- **[Rotate Your Character: Revisiting Video Diffusion Models for High-Quality 3D Character Generation](https://arxiv.org/abs/2601.05722v1)**  
  Authors: Jin Wang, Jianxiang Lu, Comi Chen, Guangzheng Xu, Haoyu Yang, Peng Chen, Na Zhang, Yifan Xu, Longhuang Wu, Shuai Shao, Qinglin Lu, Ping Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.05722v1.pdf)  
  Keywords: novel view, controllable, video diffusion, image-to-video, dit, video generation, diffusion model  

### Applications

*Showing the latest 50 out of 59 papers*

- **[Beyond End-to-End Video Models: An LLM-Based Multi-Agent System for Educational Video Generation](https://arxiv.org/abs/2602.11790v1)**  
  Authors: Lingyong Yan, Jiulong Wu, Dong Xie, Weixian Shi, Deguo Xia, Jizhou Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.11790v1.pdf)  
  Keywords: dit, video generation, education  
- **[Ctrl&Shift: High-Quality Geometry-Aware Object Manipulation in Visual Generation](https://arxiv.org/abs/2602.11440v1)**  
  Authors: Penghui Ruan, Bojia Zi, Xianbiao Qi, Youze Huang, Rong Xiao, Pichao Wang, Jiannong Cao, Yuhui Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.11440v1.pdf)  
  Keywords: controllable, dit, identity, creative, film  
- **[VideoWorld 2: Learning Transferable Knowledge from Real-world Videos](https://arxiv.org/abs/2602.10102v1)**  
  Authors: Zhongwei Ren, Yunchao Wei, Xiao Yu, Guixun Luo, Yao Zhao, Bingyi Kang, Jiashi Feng, Xiaojie Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.10102v1.pdf)  
  Keywords: video diffusion, robotics, video generation, diffusion model, dynamics, autoregressive  
- **[AUHead: Realistic Emotional Talking Head Generation via Action Units Control](https://arxiv.org/abs/2602.09534v1)**  
  Authors: Jiayi Lyu, Leigang Qu, Wenjing Zhang, Hanyu Jiang, Kai Liu, Zhenglin Zhou, Xiaobo Xia, Jian Xue, Tat-Seng Chua  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.09534v1.pdf) | [![GitHub](https://img.shields.io/github/stars/laura990501/AUHead_ICLR?style=social)](https://github.com/laura990501/AUHead_ICLR)  
  Keywords: controllable, dit, benchmark, video generation, identity, diffusion model, motion control, talking head, interactive, avatar, film  
- **[PISCO: Precise Video Instance Insertion with Sparse Control](https://arxiv.org/abs/2602.08277v1)**  
  Authors: Xiangbo Gao, Renjie Li, Xinghao Chen, Yuheng Wu, Suofei Feng, Qing Yin, Zhengzhong Tu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.08277v1.pdf)  
  Keywords: controllable, video diffusion, dit, benchmark, video generation, diffusion model, physical, dynamics, film, video editing  
- **[Action-to-Action Flow Matching](https://arxiv.org/abs/2602.07322v1)**  
  Authors: Jindou Jia, Gen Li, Xiangyu Chen, Tuo An, Yuxuan Hu, Jingliang Li, Xinying Guo, Jianfei Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.07322v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lorenzo-0-0.github.io/A2A_Flow_Matching)  
  Keywords: denoising, dit, robotics, video generation, fast inference, physical, dynamics, flow matching  
- **[Driving with DINO: Vision Foundation Features as a Unified Bridge for Sim-to-Real Generation in Autonomous Driving](https://arxiv.org/abs/2602.06159v2)**  
  Authors: Xuyang Chen, Conglang Zhang, Chuanheng Fu, Zihao Yang, Kaixuan Zhou, Yizhi Zhang, Jianan He, Yanfeng Zhang, Mingwei Sun, Zengmao Wang, Zhen Dong, Xiaoxiao Long, Liqiu Meng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06159v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://albertchen98.github.io/DwD-project)  
  Keywords: controllable, video diffusion, simulation, video generation, autonomous driving  
- **[LSA: Localized Semantic Alignment for Enhancing Temporal Consistency in Traffic Video Generation](https://arxiv.org/abs/2602.05966v1)**  
  Authors: Mirlan Karimov, Teodora Spasojevic, Markus Braun, Julian Wiederer, Vasileios Belagiannis, Marc Pollefeys  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.05966v1.pdf)  
  Keywords: controllable, dit, video generation, evaluation, autonomous driving, temporal consistency  
- **[Reliable and Responsible Foundation Models: A Comprehensive Survey](https://arxiv.org/abs/2602.08145v1)**  
  Authors: Xinyu Yang, Junlin Han, Rishi Bommasani, Jinqi Luo, Wenjie Qu, Wangchunshu Zhou, Adel Bibi, Xiyao Wang, Jaehong Yoon, Elias Stengel-Eskin, Shengbang Tong, Lingfeng Shen, Rafael Rafailov, Runjia Li, Zhaoyang Wang, Yiyang Zhou, Chenhang Cui, Yu Wang, Wenhao Zheng, Huichi Zhou, Jindong Gu, Zhaorun Chen, Peng Xia, Tony Lee, Thomas Zollo, Vikash Sehwag, Jixuan Leng, Jiuhai Chen, Yuxin Wen, Huan Zhang, Zhun Deng, Linjun Zhang, Pavel Izmailov, Pang Wei Koh, Yulia Tsvetkov, Andrew Wilson, Jiaheng Zhang, James Zou, Cihang Xie, Hao Wang, Philip Torr, Julian McAuley, David Alvarez-Melis, Florian Tramèr, Kaidi Xu, Suman Jana, Chris Callison-Burch, Rene Vidal, Filippos Kokkinos, Mohit Bansal, Beidi Chen, Huaxiu Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.08145v1.pdf)  
  Keywords: dit, survey, education  
- **[PrevizWhiz: Combining Rough 3D Scenes and 2D Video to Guide Generative Video Previsualization](https://arxiv.org/abs/2602.03838v1)**  
  Authors: Erzhen Hu, Frederik Brudy, David Ledo, George Fitzmaurice, Fraser Anderson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03838v1.pdf)  
  Keywords: dit, film, creative  

### Architecture & Efficiency

*Showing the latest 50 out of 368 papers*

- **[Beyond End-to-End Video Models: An LLM-Based Multi-Agent System for Educational Video Generation](https://arxiv.org/abs/2602.11790v1)**  
  Authors: Lingyong Yan, Jiulong Wu, Dong Xie, Weixian Shi, Deguo Xia, Jizhou Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.11790v1.pdf)  
  Keywords: dit, video generation, education  
- **[Light4D: Training-Free Extreme Viewpoint 4D Video Relighting](https://arxiv.org/abs/2602.11769v1)**  
  Authors: Zhenghuang Wu, Kang Chen, Zeyu Zhang, Hao Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.11769v1.pdf) | [![GitHub](https://img.shields.io/github/stars/AIGeeksGroup/Light4D?style=social)](https://github.com/AIGeeksGroup/Light4D) | [![Project](https://img.shields.io/badge/-Project-blue)](https://aigeeksgroup.github.io/Light4D)  
  Keywords: temporal consistency, architecture  
- **[A Large Language Model for Disaster Structural Reconnaissance Summarization](https://arxiv.org/abs/2602.11588v1)**  
  Authors: Yuqing Gao, Guanren Zhou, Khalid M. Mosalam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.11588v1.pdf)  
  Keywords: dit, evaluation  
- **[LUVE : Latent-Cascaded Ultra-High-Resolution Video Generation with Dual Frequency Experts](https://arxiv.org/abs/2602.11564v1)**  
  Authors: Chen Zhao, Jiawei Chen, Hongyu Li, Zhuoliang Kang, Shilin Lu, Xiaoming Wei, Kai Zhang, Jian Yang, Ying Tai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.11564v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://unicornanrocinu.github.io/LUVE_web)  
  Keywords: video diffusion, video generation, architecture, diffusion model  
- **[Ctrl&Shift: High-Quality Geometry-Aware Object Manipulation in Visual Generation](https://arxiv.org/abs/2602.11440v1)**  
  Authors: Penghui Ruan, Bojia Zi, Xianbiao Qi, Youze Huang, Rong Xiao, Pichao Wang, Jiannong Cao, Yuhui Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.11440v1.pdf)  
  Keywords: controllable, dit, identity, creative, film  
- **[HairWeaver: Few-Shot Photorealistic Hair Motion Synthesis with Sim-to-Real Guided Video Diffusion](https://arxiv.org/abs/2602.11117v1)**  
  Authors: Di Chang, Ji Hou, Aljaz Bozic, Assaf Neuberger, Felix Juefei-Xu, Olivier Maury, Gene Wei-Chin Lin, Tuur Stuyck, Doug Roble, Mohammad Soleymani, Stephane Grabli  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.11117v1.pdf)  
  Keywords: video diffusion, dit, human motion, evaluation, dynamics  
- **[FastFlow: Accelerating The Generative Flow Matching Models with Bandit Inference](https://arxiv.org/abs/2602.11105v1)**  
  Authors: Divya Jyoti Bajpai, Dhruv Bhardwaj, Soumya Roy, Tejas Duseja, Harsh Agarwal, Aashay Sandansing, Manjesh Kumar Hanawal  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.11105v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Div290/FastFlow?style=social)](https://github.com/Div290/FastFlow)  
  Keywords: denoising, distillation, trajectory, dit, video generation, efficient, acceleration, flow matching  
- **[Flow caching for autoregressive video generation](https://arxiv.org/abs/2602.10825v1)**  
  Authors: Yuexiao Ma, Xuzhe Zheng, Jing Xu, Xiwei Xu, Feng Ling, Xiawu Zheng, Huafeng Kuang, Huixia Li, Xing Wang, Xuefeng Xiao, Fei Chao, Rongrong Ji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.10825v1.pdf) | [![GitHub](https://img.shields.io/github/stars/mikeallen39/FlowCache?style=social)](https://github.com/mikeallen39/FlowCache)  
  Keywords: denoising, video diffusion, long video, dit, benchmark, video generation, diffusion model, architecture, video synthesis, autoregressive, efficient  
- **[ConsID-Gen: View-Consistent and Identity-Preserving Image-to-Video Generation](https://arxiv.org/abs/2602.10113v1)**  
  Authors: Mingyang Wu, Ashirbad Mishra, Soumik Dey, Shuo Xing, Naveen Ravipati, Hansi Wu, Binbin Li, Zhengzhong Tu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.10113v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://myangwu.github.io/ConsID-Gen)  
  Keywords: text-to-video, image-to-video, dit, benchmark, i2v, video generation, evaluation, diffusion transformer, identity  
- **[Causality in Video Diffusers is Separable from Denoising](https://arxiv.org/abs/2602.10095v1)**  
  Authors: Xingjian Bai, Guande He, Zhengqi Li, Eli Shechtman, Xun Huang, Zongze Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.10095v1.pdf)  
  Keywords: denoising, trajectory, benchmark, diffusion model, architecture, autoregressive  

### Audio & Multi-modal

- **[TiFRe: Text-guided Video Frame Reduction for Efficient Video Multi-modal Large Language Models](https://arxiv.org/abs/2602.08861v1)**  
  Authors: Xiangtian Zheng, Zishuo Wang, Yuxin Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.08861v1.pdf)  
  Keywords: multi-modal, style, efficient  
- **[VideoVeritas: AI-Generated Video Detection via Perception Pretext Reinforcement Learning](https://arxiv.org/abs/2602.08828v1)**  
  Authors: Hao Tan, Jun Lan, Senyuan Shi, Zichang Tan, Zijian Yu, Huijia Zhu, Weiqiang Wang, Jun Wan, Zhen Lei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.08828v1.pdf)  
  Keywords: benchmark, video generation, multi-modal, evaluation  
- **[MOVA: Towards Scalable and Synchronized Video-Audio Generation](https://arxiv.org/abs/2602.08794v2)**  
  Authors: SII-OpenMOSS Team, :, Donghua Yu, Mingshu Chen, Qi Chen, Qi Luo, Qianyi Wu, Qinyuan Cheng, Ruixiao Li, Tianyi Liang, Wenbo Zhang, Wenming Tu, Xiangyu Peng, Yang Gao, Yanru Huo, Ying Zhu, Yinze Luo, Yiyang Zhang, Yuerong Song, Zhe Xu, Zhiyu Zhang, Chenchen Yang, Cheng Chang, Chushu Zhou, Hanfu Chen, Hongnan Ma, Jiaxi Li, Jingqi Tong, Junxi Liu, Ke Chen, Shimin Li, Shiqi Jiang, Songlin Wang, Wei Jiang, Zhaoye Fei, Zhiyuan Ning, Chunguo Li, Chenhui Li, Ziwei He, Zengfeng Huang, Xie Chen, Xipeng Qiu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.08794v2.pdf)  
  Keywords: t2v, sound, architecture, efficient, text to video  
- **[T2VTree: User-Centered Visual Analytics for Agent-Assisted Thought-to-Video Authoring](https://arxiv.org/abs/2602.08368v1)**  
  Authors: Zhuoyun Zheng, Yu Dong, Gaorong Liang, Guan Li, Guihua Shan, Shiyu Cheng, Dong Tian, Jianlong Zhou, Jie Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.08368v1.pdf) | [![GitHub](https://img.shields.io/github/stars/tezuka0210/T2VTree?style=social)](https://github.com/tezuka0210/T2VTree)  
  Keywords: t2v, multi-modal, video generation, dit  
- **[SoulX-FlashHead: Oracle-guided Generation of Infinite Real-time Streaming Talking Heads](https://arxiv.org/abs/2602.07449v3)**  
  Authors: Tan Yu, Qian Qiao, Le Shen, Ke Zhou, Jincheng Hu, Dian Sheng, Bo Hu, Haoming Qin, Jun Gao, Changhai Zhou, Shunshun Yin, Siyuan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.07449v3.pdf)  
  Keywords: audio-driven, streaming, distillation, benchmark, video generation, identity, talking head, physical, autoregressive  
- **[Meta Engine: A Unified Semantic Query Engine on Heterogeneous LLM-Based Query Systems](https://arxiv.org/abs/2602.01701v1)**  
  Authors: Ruyu Li, Tinghui Zhang, Haodi Ma, Daisy Zhe Wang, Yifan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.01701v1.pdf)  
  Keywords: dit, multi-modal, architecture, evaluation  
- **[Omni-Judge: Can Omni-LLMs Serve as Human-Aligned Judges for Text-Conditioned Audio-Video Generation?](https://arxiv.org/abs/2602.01623v1)**  
  Authors: Susan Liang, Chao Huang, Filippos Bellos, Yolo Yunlong Tang, Qianxiang Shen, Jing Bi, Luchuan Song, Zeliang Zhang, Jason Corso, Chenliang Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.01623v1.pdf)  
  Keywords: text-to-video, dit, video generation, evaluation, physical, multi-modal  
- **[JUST-DUB-IT: Video Dubbing via Joint Audio-Visual Diffusion](https://arxiv.org/abs/2601.22143v1)**  
  Authors: Anthony Chen, Naomi Ken Korem, Tavi Halperin, Matan Ben Yosef, Urska Jelercic, Ofir Bibi, Or Patashnik, Daniel Cohen-Or  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.22143v1.pdf)  
  Keywords: video diffusion, dit, identity, diffusion model, sound, dynamics, multi-modal, video-to-video  
- **[EditYourself: Audio-Driven Generation and Manipulation of Talking Head Videos with Diffusion Transformers](https://arxiv.org/abs/2601.22127v1)**  
  Authors: John Flynn, Wolfgang Paier, Dimitar Dinev, Sam Nhut Nguyen, Hayk Poghosyan, Manuel Toribio, Sandipan Banerjee, Guy Gafni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.22127v1.pdf)  
  Keywords: video diffusion, audio-driven, dit, human motion, diffusion transformer, identity, diffusion model, talking head, video-to-video  
- **[Exploring Talking Head Models With Adjacent Frame Prior for Speech-Preserving Facial Expression Manipulation](https://arxiv.org/abs/2601.12876v1)**  
  Authors: Zhenxuan Lu, Zhihua Xu, Zhijing Yang, Feng Gao, Yongyi Lu, Keze Wang, Tianshui Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.12876v1.pdf)  
  Keywords: audio-driven, talking head, evaluation  

### Controllable Generation

*Showing the latest 50 out of 118 papers*

- **[Ctrl&Shift: High-Quality Geometry-Aware Object Manipulation in Visual Generation](https://arxiv.org/abs/2602.11440v1)**  
  Authors: Penghui Ruan, Bojia Zi, Xianbiao Qi, Youze Huang, Rong Xiao, Pichao Wang, Jiannong Cao, Yuhui Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.11440v1.pdf)  
  Keywords: controllable, dit, identity, creative, film  
- **[FastFlow: Accelerating The Generative Flow Matching Models with Bandit Inference](https://arxiv.org/abs/2602.11105v1)**  
  Authors: Divya Jyoti Bajpai, Dhruv Bhardwaj, Soumya Roy, Tejas Duseja, Harsh Agarwal, Aashay Sandansing, Manjesh Kumar Hanawal  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.11105v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Div290/FastFlow?style=social)](https://github.com/Div290/FastFlow)  
  Keywords: denoising, distillation, trajectory, dit, video generation, efficient, acceleration, flow matching  
- **[Causality in Video Diffusers is Separable from Denoising](https://arxiv.org/abs/2602.10095v1)**  
  Authors: Xingjian Bai, Guande He, Zhengqi Li, Eli Shechtman, Xun Huang, Zongze Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.10095v1.pdf)  
  Keywords: denoising, trajectory, benchmark, diffusion model, architecture, autoregressive  
- **[ArtisanGS: Interactive Tools for Gaussian Splat Selection with AI and Human in the Loop](https://arxiv.org/abs/2602.10173v1)**  
  Authors: Clement Fuji Tsang, Anita Hu, Or Perel, Carsten Kolve, Maria Shugrina  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.10173v1.pdf)  
  Keywords: controllable, video diffusion, simulation, physics, dit, diffusion model, interactive  
- **[Free-GVC: Towards Training-Free Extreme Generative Video Compression with Temporal Coherence](https://arxiv.org/abs/2602.09868v1)**  
  Authors: Xiaoyue Ling, Chuqin Zhou, Chunyi Li, Yunuo Chen, Yuan Tian, Guo Lu, Wenjun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.09868v1.pdf)  
  Keywords: dit, video diffusion, video generation, trajectory  
- **[Hand2World: Autoregressive Egocentric Interaction Generation via Free-Space Hand Gestures](https://arxiv.org/abs/2602.09600v1)**  
  Authors: Yuxi Wang, Wenqi Ouyang, Tianyi Wei, Yi Dong, Zhiqi Shen, Xingang Pan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.09600v1.pdf)  
  Keywords: gesture, dit, benchmark, video generation, diffusion model, world model, interactive, dynamics, autoregressive, camera control  
- **[AUHead: Realistic Emotional Talking Head Generation via Action Units Control](https://arxiv.org/abs/2602.09534v1)**  
  Authors: Jiayi Lyu, Leigang Qu, Wenjing Zhang, Hanyu Jiang, Kai Liu, Zhenglin Zhou, Xiaobo Xia, Jian Xue, Tat-Seng Chua  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.09534v1.pdf) | [![GitHub](https://img.shields.io/github/stars/laura990501/AUHead_ICLR?style=social)](https://github.com/laura990501/AUHead_ICLR)  
  Keywords: controllable, dit, benchmark, video generation, identity, diffusion model, motion control, talking head, interactive, avatar, film  
- **[Rethinking Global Text Conditioning in Diffusion Transformers](https://arxiv.org/abs/2602.09268v1)**  
  Authors: Nikita Starodubcev, Daniil Pakhomov, Zongze Wu, Ilya Drobyshevskiy, Yuchen Liu, Zhonghao Wang, Yuqian Zhou, Zhe Lin, Dmitry Baranchuk  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.09268v1.pdf)  
  Keywords: controllable, dit, video generation, diffusion transformer, diffusion model  
- **[PISCO: Precise Video Instance Insertion with Sparse Control](https://arxiv.org/abs/2602.08277v1)**  
  Authors: Xiangbo Gao, Renjie Li, Xinghao Chen, Yuheng Wu, Suofei Feng, Qing Yin, Zhengzhong Tu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.08277v1.pdf)  
  Keywords: controllable, video diffusion, dit, benchmark, video generation, diffusion model, physical, dynamics, film, video editing  
- **[ReRoPE: Repurposing RoPE for Relative Camera Control](https://arxiv.org/abs/2602.08068v1)**  
  Authors: Chunyang Li, Yuanbo Yang, Jiahao Shao, Hongyu Zhou, Katja Schwarz, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.08068v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://sisyphe-lee.github.io/ReRoPE)  
  Keywords: controllable, video diffusion, simulation, image-to-video, i2v, video generation, diffusion model, interactive, efficient, video-to-video, camera control  

### Human & Character Animation

- **[HairWeaver: Few-Shot Photorealistic Hair Motion Synthesis with Sim-to-Real Guided Video Diffusion](https://arxiv.org/abs/2602.11117v1)**  
  Authors: Di Chang, Ji Hou, Aljaz Bozic, Assaf Neuberger, Felix Juefei-Xu, Olivier Maury, Gene Wei-Chin Lin, Tuur Stuyck, Doug Roble, Mohammad Soleymani, Stephane Grabli  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.11117v1.pdf)  
  Keywords: video diffusion, dit, human motion, evaluation, dynamics  
- **[Hand2World: Autoregressive Egocentric Interaction Generation via Free-Space Hand Gestures](https://arxiv.org/abs/2602.09600v1)**  
  Authors: Yuxi Wang, Wenqi Ouyang, Tianyi Wei, Yi Dong, Zhiqi Shen, Xingang Pan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.09600v1.pdf)  
  Keywords: gesture, dit, benchmark, video generation, diffusion model, world model, interactive, dynamics, autoregressive, camera control  
- **[AUHead: Realistic Emotional Talking Head Generation via Action Units Control](https://arxiv.org/abs/2602.09534v1)**  
  Authors: Jiayi Lyu, Leigang Qu, Wenjing Zhang, Hanyu Jiang, Kai Liu, Zhenglin Zhou, Xiaobo Xia, Jian Xue, Tat-Seng Chua  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.09534v1.pdf) | [![GitHub](https://img.shields.io/github/stars/laura990501/AUHead_ICLR?style=social)](https://github.com/laura990501/AUHead_ICLR)  
  Keywords: controllable, dit, benchmark, video generation, identity, diffusion model, motion control, talking head, interactive, avatar, film  
- **[SoulX-FlashHead: Oracle-guided Generation of Infinite Real-time Streaming Talking Heads](https://arxiv.org/abs/2602.07449v3)**  
  Authors: Tan Yu, Qian Qiao, Le Shen, Ke Zhou, Jincheng Hu, Dian Sheng, Bo Hu, Haoming Qin, Jun Gao, Changhai Zhou, Shunshun Yin, Siyuan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.07449v3.pdf)  
  Keywords: audio-driven, streaming, distillation, benchmark, video generation, identity, talking head, physical, autoregressive  
- **[From Blurry to Believable: Enhancing Low-quality Talking Heads with 3D Generative Priors](https://arxiv.org/abs/2602.06122v1)**  
  Authors: Ding-Jiun Huang, Yuanhao Wang, Shao-Ji Yuan, Albert Mosella-Montoro, Francisco Vicente Carrasco, Cheng Zhang, Fernando De la Torre  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06122v1.pdf)  
  Keywords: super-resolution, identity, talking head, dynamics, avatar, temporal consistency  
- **[ShapeGaussian: High-Fidelity 4D Human Reconstruction in Monocular Videos via Vision Priors](https://arxiv.org/abs/2602.05572v1)**  
  Authors: Zhenxiao Liang, Ning Zhang, Youbao Tang, Ruei-Sung Lin, Qixing Huang, Peng Chang, Jing Xiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.05572v1.pdf)  
  Keywords: human motion  
- **[3D-Aware Implicit Motion Control for View-Adaptive Human Video Generation](https://arxiv.org/abs/2602.03796v1)**  
  Authors: Zhixue Fang, Xu He, Songlin Tang, Haoxian Zhang, Qingfeng Li, Xiaoqiang Liu, Pengfei Wan, Kun Gai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03796v1.pdf)  
  Keywords: 3d-aware, dit, human motion, video generation, motion control, dynamics, camera control  
- **[VRGaussianAvatar: Integrating 3D Gaussian Avatars into VR](https://arxiv.org/abs/2602.01674v1)**  
  Authors: Hail Song, Boram Yoon, Seokhwan Yang, Seoyoung Kang, Hyunjeong Kim, Henning Metzmacher, Woontack Woo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.01674v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vrgaussianavatar.github.io)  
  Keywords: avatar, interactive  
- **[Making Avatars Interact: Towards Text-Driven Human-Object Interaction for Controllable Talking Avatars](https://arxiv.org/abs/2602.01538v1)**  
  Authors: Youliang Zhang, Zhengguang Zhou, Zhentao Yu, Ziyao Huang, Teng Hu, Sen Liang, Guozhen Zhang, Ziqiao Peng, Shunkai Li, Yi Chen, Zixiang Zhou, Yuan Zhou, Qinglin Lu, Xiu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.01538v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://interactavatar.github.io)  
  Keywords: controllable, dit, benchmark, human motion, video generation, video synthesis, avatar  
- **[EditYourself: Audio-Driven Generation and Manipulation of Talking Head Videos with Diffusion Transformers](https://arxiv.org/abs/2601.22127v1)**  
  Authors: John Flynn, Wolfgang Paier, Dimitar Dinev, Sam Nhut Nguyen, Hayk Poghosyan, Manuel Toribio, Sandipan Banerjee, Guy Gafni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.22127v1.pdf)  
  Keywords: video diffusion, audio-driven, dit, human motion, diffusion transformer, identity, diffusion model, talking head, video-to-video  

### Image-to-Video Generation

- **[ConsID-Gen: View-Consistent and Identity-Preserving Image-to-Video Generation](https://arxiv.org/abs/2602.10113v1)**  
  Authors: Mingyang Wu, Ashirbad Mishra, Soumik Dey, Shuo Xing, Naveen Ravipati, Hansi Wu, Binbin Li, Zhengzhong Tu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.10113v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://myangwu.github.io/ConsID-Gen)  
  Keywords: text-to-video, image-to-video, dit, benchmark, i2v, video generation, evaluation, diffusion transformer, identity  
- **[Monocular Normal Estimation via Shading Sequence Estimation](https://arxiv.org/abs/2602.09929v2)**  
  Authors: Zongrui Li, Xinhua Ma, Minghui Hu, Yunqing Zhao, Yingchen Yu, Qian Zheng, Chang Liu, Xudong Jiang, Song Bai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.09929v2.pdf)  
  Keywords: dit, benchmark, image-to-video  
- **[Tele-Omni: a Unified Multimodal Framework for Video Generation and Editing](https://arxiv.org/abs/2602.09609v1)**  
  Authors: Jialun Liu, Yukuo Ma, Xiao Cao, Tian Li, Gonghu Shang, Haibin Huang, Chi Zhang, Xuelong Li, Cong Liu, Junqi Liu, Jiakui Hu, Robby T. Tan, Shiwen Zhang, Liying Yang, Xiaoyan Yang, Qizhen Weng, Xiangzhen Chang, Yuanzhi Liang, Yifan Xu, Zhiyong Huang, Zuoxin Li, Xuelong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.09609v1.pdf)  
  Keywords: text-to-video, image-to-video, dit, video generation, video synthesis, video editing  
- **[ReRoPE: Repurposing RoPE for Relative Camera Control](https://arxiv.org/abs/2602.08068v1)**  
  Authors: Chunyang Li, Yuanbo Yang, Jiahao Shao, Hongyu Zhou, Katja Schwarz, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.08068v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://sisyphe-lee.github.io/ReRoPE)  
  Keywords: controllable, video diffusion, simulation, image-to-video, i2v, video generation, diffusion model, interactive, efficient, video-to-video, camera control  
- **[RISE-Video: Can Video Generators Decode Implicit World Rules?](https://arxiv.org/abs/2602.05986v1)**  
  Authors: Mingxin Liu, Shuran Ma, Shibei Meng, Xiangyu Zhao, Zicheng Zhang, Shaofeng Zhang, Zhihang Zhong, Peixian Chen, Haoyu Cao, Xing Sun, Haodong Duan, Xue Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.05986v1.pdf)  
  Keywords: image-to-video, benchmark, i2v, evaluation, physical, dynamics, temporal consistency  
- **[FSVideo: Fast Speed Video Diffusion Model in a Highly-Compressed Latent Space](https://arxiv.org/abs/2602.02092v1)**  
  Authors: FSVideo Team, Qingyu Chen, Zhiyuan Fang, Haibin Huang, Xinwei Huang, Tong Jin, Minxuan Lin, Bo Liu, Celong Liu, Chongyang Ma, Xing Mei, Xiaohui Shen, Yaojie Shen, Fuwen Tan, Angtian Wang, Xiao Yang, Yiding Yang, Jiamin Yuan, Lingxi Zhang, Yuxin Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.02092v1.pdf)  
  Keywords: video diffusion, image-to-video, dit, i2v, diffusion transformer, diffusion model, architecture  
- **[Grounding Generated Videos in Feasible Plans via World Models](https://arxiv.org/abs/2602.01960v1)**  
  Authors: Christos Ziakas, Amir Bar, Alessandra Russo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.01960v1.pdf)  
  Keywords: simulation, image-to-video, trajectory, dit, action-conditioned, world model, physical, dynamics, temporal consistency  
- **[PLACID: Identity-Preserving Multi-Object Compositing via Video Diffusion with Synthetic Trajectories](https://arxiv.org/abs/2602.00267v1)**  
  Authors: Gemma Canet Tarrés, Manel Baradad, Francesc Moreno-Noguer, Yumeng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.00267v1.pdf)  
  Keywords: video diffusion, image-to-video, i2v, evaluation, layout, identity, diffusion model  
- **[Zero-Shot Video Restoration and Enhancement with Assistance of Video Diffusion Models](https://arxiv.org/abs/2601.21922v1)**  
  Authors: Cong Cao, Huanjing Yue, Shangbin Xie, Xin Liu, Jingyu Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.21922v1.pdf)  
  Keywords: video diffusion, text-to-video, video restoration, image-to-video, diffusion model, temporal consistency  
- **[MV-S2V: Multi-View Subject-Consistent Video Generation](https://arxiv.org/abs/2601.17756v2)**  
  Authors: Ziyang Song, Xinyu Gong, Bangya Liu, Zelin Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.17756v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://szy-young.github.io/mv-s2v)  
  Keywords: dit, i2v, video generation, subject-driven  

### Long Video Generation

*Showing the latest 50 out of 124 papers*

- **[Light4D: Training-Free Extreme Viewpoint 4D Video Relighting](https://arxiv.org/abs/2602.11769v1)**  
  Authors: Zhenghuang Wu, Kang Chen, Zeyu Zhang, Hao Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.11769v1.pdf) | [![GitHub](https://img.shields.io/github/stars/AIGeeksGroup/Light4D?style=social)](https://github.com/AIGeeksGroup/Light4D) | [![Project](https://img.shields.io/badge/-Project-blue)](https://aigeeksgroup.github.io/Light4D)  
  Keywords: temporal consistency, architecture  
- **[Flow caching for autoregressive video generation](https://arxiv.org/abs/2602.10825v1)**  
  Authors: Yuexiao Ma, Xuzhe Zheng, Jing Xu, Xiwei Xu, Feng Ling, Xiawu Zheng, Huafeng Kuang, Huixia Li, Xing Wang, Xuefeng Xiao, Fei Chao, Rongrong Ji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.10825v1.pdf) | [![GitHub](https://img.shields.io/github/stars/mikeallen39/FlowCache?style=social)](https://github.com/mikeallen39/FlowCache)  
  Keywords: denoising, video diffusion, long video, dit, benchmark, video generation, diffusion model, architecture, video synthesis, autoregressive, efficient  
- **[VideoWorld 2: Learning Transferable Knowledge from Real-world Videos](https://arxiv.org/abs/2602.10102v1)**  
  Authors: Zhongwei Ren, Yunchao Wei, Xiao Yu, Guixun Luo, Yao Zhao, Bingyi Kang, Jiashi Feng, Xiaojie Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.10102v1.pdf)  
  Keywords: video diffusion, robotics, video generation, diffusion model, dynamics, autoregressive  
- **[Causality in Video Diffusers is Separable from Denoising](https://arxiv.org/abs/2602.10095v1)**  
  Authors: Xingjian Bai, Guande He, Zhengqi Li, Eli Shechtman, Xun Huang, Zongze Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.10095v1.pdf)  
  Keywords: denoising, trajectory, benchmark, diffusion model, architecture, autoregressive  
- **[Hand2World: Autoregressive Egocentric Interaction Generation via Free-Space Hand Gestures](https://arxiv.org/abs/2602.09600v1)**  
  Authors: Yuxi Wang, Wenqi Ouyang, Tianyi Wei, Yi Dong, Zhiqi Shen, Xingang Pan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.09600v1.pdf)  
  Keywords: gesture, dit, benchmark, video generation, diffusion model, world model, interactive, dynamics, autoregressive, camera control  
- **[WorldCompass: Reinforcement Learning for Long-Horizon World Models](https://arxiv.org/abs/2602.09022v1)**  
  Authors: Zehan Wang, Tengfei Wang, Haiyu Zhang, Xuhui Zuo, Junta Wu, Haoyuan Wang, Wenqiang Sun, Zhenwei Wang, Chenjie Cao, Hengshuang Zhao, Chunchao Guo, Zhou Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.09022v1.pdf)  
  Keywords: video generation, evaluation, world model, interactive, efficient, autoregressive  
- **[Rolling Sink: Bridging Limited-Horizon Training and Open-Ended Testing in Autoregressive Video Diffusion](https://arxiv.org/abs/2602.07775v1)**  
  Authors: Haodong Li, Shaoteng Liu, Zhe Lin, Manmohan Chandraker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.07775v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rolling-sink.github.io)  
  Keywords: video diffusion, diffusion model, video synthesis, autoregressive, temporal consistency  
- **[SoulX-FlashHead: Oracle-guided Generation of Infinite Real-time Streaming Talking Heads](https://arxiv.org/abs/2602.07449v3)**  
  Authors: Tan Yu, Qian Qiao, Le Shen, Ke Zhou, Jincheng Hu, Dian Sheng, Bo Hu, Haoming Qin, Jun Gao, Changhai Zhou, Shunshun Yin, Siyuan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.07449v3.pdf)  
  Keywords: audio-driven, streaming, distillation, benchmark, video generation, identity, talking head, physical, autoregressive  
- **[RFDM: Residual Flow Diffusion Model for Efficient Causal Video Editing](https://arxiv.org/abs/2602.06871v1)**  
  Authors: Mohammadreza Salehi, Mehdi Noroozi, Luca Morreale, Ruchika Chavhan, Malcolm Chadwick, Alberto Gil Ramos, Abhinav Mehrotra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06871v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://smsd75.github.io/RFDM_page)  
  Keywords: denoising, style, dit, benchmark, video generation, diffusion model, efficient, autoregressive, video-to-video, video editing  
- **[DiTS: Multimodal Diffusion Transformers Are Time Series Forecasters](https://arxiv.org/abs/2602.06597v1)**  
  Authors: Haoran Zhang, Haixuan Liu, Yong Liu, Yunzhong Qiu, Yuxuan Wang, Jianmin Wang, Mingsheng Long  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06597v1.pdf)  
  Keywords: dit, benchmark, video generation, diffusion transformer, architecture, autoregressive  

### Personalization & Customization

*Showing the latest 50 out of 89 papers*

- **[Ctrl&Shift: High-Quality Geometry-Aware Object Manipulation in Visual Generation](https://arxiv.org/abs/2602.11440v1)**  
  Authors: Penghui Ruan, Bojia Zi, Xianbiao Qi, Youze Huang, Rong Xiao, Pichao Wang, Jiannong Cao, Yuhui Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.11440v1.pdf)  
  Keywords: controllable, dit, identity, creative, film  
- **[ConsID-Gen: View-Consistent and Identity-Preserving Image-to-Video Generation](https://arxiv.org/abs/2602.10113v1)**  
  Authors: Mingyang Wu, Ashirbad Mishra, Soumik Dey, Shuo Xing, Naveen Ravipati, Hansi Wu, Binbin Li, Zhengzhong Tu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.10113v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://myangwu.github.io/ConsID-Gen)  
  Keywords: text-to-video, image-to-video, dit, benchmark, i2v, video generation, evaluation, diffusion transformer, identity  
- **[AUHead: Realistic Emotional Talking Head Generation via Action Units Control](https://arxiv.org/abs/2602.09534v1)**  
  Authors: Jiayi Lyu, Leigang Qu, Wenjing Zhang, Hanyu Jiang, Kai Liu, Zhenglin Zhou, Xiaobo Xia, Jian Xue, Tat-Seng Chua  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.09534v1.pdf) | [![GitHub](https://img.shields.io/github/stars/laura990501/AUHead_ICLR?style=social)](https://github.com/laura990501/AUHead_ICLR)  
  Keywords: controllable, dit, benchmark, video generation, identity, diffusion model, motion control, talking head, interactive, avatar, film  
- **[TiFRe: Text-guided Video Frame Reduction for Efficient Video Multi-modal Large Language Models](https://arxiv.org/abs/2602.08861v1)**  
  Authors: Xiangtian Zheng, Zishuo Wang, Yuxin Peng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.08861v1.pdf)  
  Keywords: multi-modal, style, efficient  
- **[ALIVE: Animate Your World with Lifelike Audio-Video Generation](https://arxiv.org/abs/2602.08682v2)**  
  Authors: Ying Guo, Qijun Gan, Yifu Zhang, Jinlai Liu, Yifei Hu, Pan Xie, Dongjun Qian, Yu Zhang, Ruiqi Li, Yuqi Zhang, Ruibiao Lu, Xiaofeng Mei, Bo Han, Xiang Yin, Bingyue Peng, Zehuan Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.08682v2.pdf) | [![GitHub](https://img.shields.io/github/stars/FoundationVision/Alive?style=social)](https://github.com/FoundationVision/Alive)  
  Keywords: text-to-video, style, t2v, benchmark, dit, video generation, architecture, efficient  
- **[IM-Animation: An Implicit Motion Representation for Identity-decoupled Character Animation](https://arxiv.org/abs/2602.07498v1)**  
  Authors: Zhufeng Xu, Xuan Gao, Feng-Lin Liu, Haoxian Zhang, Zhixue Fang, Yu-Kun Lai, Xiaoqiang Liu, Pengfei Wan, Lin Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.07498v1.pdf)  
  Keywords: identity, video diffusion, diffusion model  
- **[SoulX-FlashHead: Oracle-guided Generation of Infinite Real-time Streaming Talking Heads](https://arxiv.org/abs/2602.07449v3)**  
  Authors: Tan Yu, Qian Qiao, Le Shen, Ke Zhou, Jincheng Hu, Dian Sheng, Bo Hu, Haoming Qin, Jun Gao, Changhai Zhou, Shunshun Yin, Siyuan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.07449v3.pdf)  
  Keywords: audio-driven, streaming, distillation, benchmark, video generation, identity, talking head, physical, autoregressive  
- **[RFDM: Residual Flow Diffusion Model for Efficient Causal Video Editing](https://arxiv.org/abs/2602.06871v1)**  
  Authors: Mohammadreza Salehi, Mehdi Noroozi, Luca Morreale, Ruchika Chavhan, Malcolm Chadwick, Alberto Gil Ramos, Abhinav Mehrotra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06871v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://smsd75.github.io/RFDM_page)  
  Keywords: denoising, style, dit, benchmark, video generation, diffusion model, efficient, autoregressive, video-to-video, video editing  
- **[From Blurry to Believable: Enhancing Low-quality Talking Heads with 3D Generative Priors](https://arxiv.org/abs/2602.06122v1)**  
  Authors: Ding-Jiun Huang, Yuanhao Wang, Shao-Ji Yuan, Albert Mosella-Montoro, Francisco Vicente Carrasco, Cheng Zhang, Fernando De la Torre  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06122v1.pdf)  
  Keywords: super-resolution, identity, talking head, dynamics, avatar, temporal consistency  
- **[Continuous Control of Editing Models via Adaptive-Origin Guidance](https://arxiv.org/abs/2602.03826v1)**  
  Authors: Alon Wolf, Chen Katzir, Kfir Aberman, Or Patashnik  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03826v1.pdf)  
  Keywords: dit, identity, video editing, video manipulation  

### Physical Understanding

*Showing the latest 50 out of 137 papers*

- **[SurfPhase: 3D Interfacial Dynamics in Two-Phase Flows from Sparse Videos](https://arxiv.org/abs/2602.11154v1)**  
  Authors: Yue Gao, Hong-Xing Yu, Sanghyeon Chang, Qianxi Fu, Bo Zhu, Yoonjin Won, Juan Carlos Niebles, Jiajun Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.11154v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yuegao.me/SurfPhase)  
  Keywords: video diffusion, dynamics, diffusion model  
- **[HairWeaver: Few-Shot Photorealistic Hair Motion Synthesis with Sim-to-Real Guided Video Diffusion](https://arxiv.org/abs/2602.11117v1)**  
  Authors: Di Chang, Ji Hou, Aljaz Bozic, Assaf Neuberger, Felix Juefei-Xu, Olivier Maury, Gene Wei-Chin Lin, Tuur Stuyck, Doug Roble, Mohammad Soleymani, Stephane Grabli  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.11117v1.pdf)  
  Keywords: video diffusion, dit, human motion, evaluation, dynamics  
- **[TwiFF (Think With Future Frames): A Large-Scale Dataset for Dynamic Visual Reasoning](https://arxiv.org/abs/2602.10675v1)**  
  Authors: Junhua Liu, Zhangcheng Wang, Zhike Han, Ningli Wang, Guotao Liang, Kun Kuang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.10675v1.pdf) | [![GitHub](https://img.shields.io/github/stars/LiuJunhua02/TwiFF?style=social)](https://github.com/LiuJunhua02/TwiFF)  
  Keywords: benchmark, video generation, evaluation, dynamics  
- **[VideoWorld 2: Learning Transferable Knowledge from Real-world Videos](https://arxiv.org/abs/2602.10102v1)**  
  Authors: Zhongwei Ren, Yunchao Wei, Xiao Yu, Guixun Luo, Yao Zhao, Bingyi Kang, Jiashi Feng, Xiaojie Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.10102v1.pdf)  
  Keywords: video diffusion, robotics, video generation, diffusion model, dynamics, autoregressive  
- **[ArtisanGS: Interactive Tools for Gaussian Splat Selection with AI and Human in the Loop](https://arxiv.org/abs/2602.10173v1)**  
  Authors: Clement Fuji Tsang, Anita Hu, Or Perel, Carsten Kolve, Maria Shugrina  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.10173v1.pdf)  
  Keywords: controllable, video diffusion, simulation, physics, dit, diffusion model, interactive  
- **[AdaTSQ: Pushing the Pareto Frontier of Diffusion Transformers via Temporal-Sensitivity Quantization](https://arxiv.org/abs/2602.09883v1)**  
  Authors: Shaoqiu Zhang, Zizhong Ding, Kaicheng Yang, Junyi Wu, Xianglong Yan, Xi Li, Bingnan Duan, Jianping Fang, Yulun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.09883v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Qiushao-E/AdaTSQ?style=social)](https://github.com/Qiushao-E/AdaTSQ)  
  Keywords: dit, video generation, dynamics, diffusion transformer  
- **[Hand2World: Autoregressive Egocentric Interaction Generation via Free-Space Hand Gestures](https://arxiv.org/abs/2602.09600v1)**  
  Authors: Yuxi Wang, Wenqi Ouyang, Tianyi Wei, Yi Dong, Zhiqi Shen, Xingang Pan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.09600v1.pdf)  
  Keywords: gesture, dit, benchmark, video generation, diffusion model, world model, interactive, dynamics, autoregressive, camera control  
- **[WorldArena: A Unified Benchmark for Evaluating Perception and Functional Utility of Embodied World Models](https://arxiv.org/abs/2602.08971v2)**  
  Authors: Yu Shang, Zhuohang Li, Yiding Ma, Weikang Su, Xin Jin, Ziyou Wang, Lei Jin, Xin Zhang, Yinzhou Tang, Haisheng Su, Chen Gao, Wei Wu, Xihui Liu, Dhruv Shah, Zhaoxiang Zhang, Zhibo Chen, Jun Zhu, Yonghong Tian, Tat-Seng Chua, Wenwu Zhu, Yong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.08971v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://world-arena.ai)  
  Keywords: dit, benchmark, video generation, action-conditioned, evaluation, world model, dynamics  
- **[PISCO: Precise Video Instance Insertion with Sparse Control](https://arxiv.org/abs/2602.08277v1)**  
  Authors: Xiangbo Gao, Renjie Li, Xinghao Chen, Yuheng Wu, Suofei Feng, Qing Yin, Zhengzhong Tu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.08277v1.pdf)  
  Keywords: controllable, video diffusion, dit, benchmark, video generation, diffusion model, physical, dynamics, film, video editing  
- **[SoulX-FlashHead: Oracle-guided Generation of Infinite Real-time Streaming Talking Heads](https://arxiv.org/abs/2602.07449v3)**  
  Authors: Tan Yu, Qian Qiao, Le Shen, Ke Zhou, Jincheng Hu, Dian Sheng, Bo Hu, Haoming Qin, Jun Gao, Changhai Zhou, Shunshun Yin, Siyuan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.07449v3.pdf)  
  Keywords: audio-driven, streaming, distillation, benchmark, video generation, identity, talking head, physical, autoregressive  

### Surveys & Benchmarks

*Showing the latest 50 out of 206 papers*

- **[A Large Language Model for Disaster Structural Reconnaissance Summarization](https://arxiv.org/abs/2602.11588v1)**  
  Authors: Yuqing Gao, Guanren Zhou, Khalid M. Mosalam  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.11588v1.pdf)  
  Keywords: dit, evaluation  
- **[HairWeaver: Few-Shot Photorealistic Hair Motion Synthesis with Sim-to-Real Guided Video Diffusion](https://arxiv.org/abs/2602.11117v1)**  
  Authors: Di Chang, Ji Hou, Aljaz Bozic, Assaf Neuberger, Felix Juefei-Xu, Olivier Maury, Gene Wei-Chin Lin, Tuur Stuyck, Doug Roble, Mohammad Soleymani, Stephane Grabli  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.11117v1.pdf)  
  Keywords: video diffusion, dit, human motion, evaluation, dynamics  
- **[GameDevBench: Evaluating Agentic Capabilities Through Game Development](https://arxiv.org/abs/2602.11103v1)**  
  Authors: Wayne Chi, Yixiong Fang, Arnav Yayavaram, Siddharth Yayavaram, Seth Karten, Qiuhong Anna Wei, Runkun Chen, Alexander Wang, Valerie Chen, Ameet Talwalkar, Chris Donahue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.11103v1.pdf)  
  Keywords: benchmark, evaluation  
- **[Chatting with Images for Introspective Visual Thinking](https://arxiv.org/abs/2602.11073v1)**  
  Authors: Junfei Wu, Jian Guan, Qiang Liu, Shu Wu, Liang Wang, Wei Wu, Tienie Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.11073v1.pdf)  
  Keywords: benchmark, interactive  
- **[Flow caching for autoregressive video generation](https://arxiv.org/abs/2602.10825v1)**  
  Authors: Yuexiao Ma, Xuzhe Zheng, Jing Xu, Xiwei Xu, Feng Ling, Xiawu Zheng, Huafeng Kuang, Huixia Li, Xing Wang, Xuefeng Xiao, Fei Chao, Rongrong Ji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.10825v1.pdf) | [![GitHub](https://img.shields.io/github/stars/mikeallen39/FlowCache?style=social)](https://github.com/mikeallen39/FlowCache)  
  Keywords: denoising, video diffusion, long video, dit, benchmark, video generation, diffusion model, architecture, video synthesis, autoregressive, efficient  
- **[TwiFF (Think With Future Frames): A Large-Scale Dataset for Dynamic Visual Reasoning](https://arxiv.org/abs/2602.10675v1)**  
  Authors: Junhua Liu, Zhangcheng Wang, Zhike Han, Ningli Wang, Guotao Liang, Kun Kuang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.10675v1.pdf) | [![GitHub](https://img.shields.io/github/stars/LiuJunhua02/TwiFF?style=social)](https://github.com/LiuJunhua02/TwiFF)  
  Keywords: benchmark, video generation, evaluation, dynamics  
- **[ConsID-Gen: View-Consistent and Identity-Preserving Image-to-Video Generation](https://arxiv.org/abs/2602.10113v1)**  
  Authors: Mingyang Wu, Ashirbad Mishra, Soumik Dey, Shuo Xing, Naveen Ravipati, Hansi Wu, Binbin Li, Zhengzhong Tu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.10113v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://myangwu.github.io/ConsID-Gen)  
  Keywords: text-to-video, image-to-video, dit, benchmark, i2v, video generation, evaluation, diffusion transformer, identity  
- **[Causality in Video Diffusers is Separable from Denoising](https://arxiv.org/abs/2602.10095v1)**  
  Authors: Xingjian Bai, Guande He, Zhengqi Li, Eli Shechtman, Xun Huang, Zongze Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.10095v1.pdf)  
  Keywords: denoising, trajectory, benchmark, diffusion model, architecture, autoregressive  
- **[Monocular Normal Estimation via Shading Sequence Estimation](https://arxiv.org/abs/2602.09929v2)**  
  Authors: Zongrui Li, Xinhua Ma, Minghui Hu, Yunqing Zhao, Yingchen Yu, Qian Zheng, Chang Liu, Xudong Jiang, Song Bai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.09929v2.pdf)  
  Keywords: dit, benchmark, image-to-video  
- **[Hand2World: Autoregressive Egocentric Interaction Generation via Free-Space Hand Gestures](https://arxiv.org/abs/2602.09600v1)**  
  Authors: Yuxi Wang, Wenqi Ouyang, Tianyi Wei, Yi Dong, Zhiqi Shen, Xingang Pan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.09600v1.pdf)  
  Keywords: gesture, dit, benchmark, video generation, diffusion model, world model, interactive, dynamics, autoregressive, camera control  

### Text-to-Video Generation

*Showing the latest 50 out of 73 papers*

- **[ReTracing: An Archaeological Approach Through Body, Machine, and Generative Systems](https://arxiv.org/abs/2602.11242v1)**  
  Authors: Yitong Wang, Yue Yao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.11242v1.pdf)  
  Keywords: text-to-video  
- **[ConsID-Gen: View-Consistent and Identity-Preserving Image-to-Video Generation](https://arxiv.org/abs/2602.10113v1)**  
  Authors: Mingyang Wu, Ashirbad Mishra, Soumik Dey, Shuo Xing, Naveen Ravipati, Hansi Wu, Binbin Li, Zhengzhong Tu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.10113v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://myangwu.github.io/ConsID-Gen)  
  Keywords: text-to-video, image-to-video, dit, benchmark, i2v, video generation, evaluation, diffusion transformer, identity  
- **[Tele-Omni: a Unified Multimodal Framework for Video Generation and Editing](https://arxiv.org/abs/2602.09609v1)**  
  Authors: Jialun Liu, Yukuo Ma, Xiao Cao, Tian Li, Gonghu Shang, Haibin Huang, Chi Zhang, Xuelong Li, Cong Liu, Junqi Liu, Jiakui Hu, Robby T. Tan, Shiwen Zhang, Liying Yang, Xiaoyan Yang, Qizhen Weng, Xiangzhen Chang, Yuanzhi Liang, Yifan Xu, Zhiyong Huang, Zuoxin Li, Xuelong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.09609v1.pdf)  
  Keywords: text-to-video, image-to-video, dit, video generation, video synthesis, video editing  
- **[Omni-Video 2: Scaling MLLM-Conditioned Diffusion for Unified Video Generation and Editing](https://arxiv.org/abs/2602.08820v1)**  
  Authors: Hao Yang, Zhiyu Tan, Jia Gong, Luozheng Qin, Hesen Chen, Xiaomeng Yang, Yuqing Sun, Yuetan Lin, Mengping Yang, Hao Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.08820v1.pdf)  
  Keywords: video diffusion, text-to-video, dit, benchmark, video generation, diffusion model, efficient, video editing  
- **[MOVA: Towards Scalable and Synchronized Video-Audio Generation](https://arxiv.org/abs/2602.08794v2)**  
  Authors: SII-OpenMOSS Team, :, Donghua Yu, Mingshu Chen, Qi Chen, Qi Luo, Qianyi Wu, Qinyuan Cheng, Ruixiao Li, Tianyi Liang, Wenbo Zhang, Wenming Tu, Xiangyu Peng, Yang Gao, Yanru Huo, Ying Zhu, Yinze Luo, Yiyang Zhang, Yuerong Song, Zhe Xu, Zhiyu Zhang, Chenchen Yang, Cheng Chang, Chushu Zhou, Hanfu Chen, Hongnan Ma, Jiaxi Li, Jingqi Tong, Junxi Liu, Ke Chen, Shimin Li, Shiqi Jiang, Songlin Wang, Wei Jiang, Zhaoye Fei, Zhiyuan Ning, Chunguo Li, Chenhui Li, Ziwei He, Zengfeng Huang, Xie Chen, Xipeng Qiu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.08794v2.pdf)  
  Keywords: t2v, sound, architecture, efficient, text to video  
- **[ALIVE: Animate Your World with Lifelike Audio-Video Generation](https://arxiv.org/abs/2602.08682v2)**  
  Authors: Ying Guo, Qijun Gan, Yifu Zhang, Jinlai Liu, Yifei Hu, Pan Xie, Dongjun Qian, Yu Zhang, Ruiqi Li, Yuqi Zhang, Ruibiao Lu, Xiaofeng Mei, Bo Han, Xiang Yin, Bingyue Peng, Zehuan Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.08682v2.pdf) | [![GitHub](https://img.shields.io/github/stars/FoundationVision/Alive?style=social)](https://github.com/FoundationVision/Alive)  
  Keywords: text-to-video, style, t2v, benchmark, dit, video generation, architecture, efficient  
- **[T2VTree: User-Centered Visual Analytics for Agent-Assisted Thought-to-Video Authoring](https://arxiv.org/abs/2602.08368v1)**  
  Authors: Zhuoyun Zheng, Yu Dong, Gaorong Liang, Guan Li, Guihua Shan, Shiyu Cheng, Dong Tian, Jianlong Zhou, Jie Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.08368v1.pdf) | [![GitHub](https://img.shields.io/github/stars/tezuka0210/T2VTree?style=social)](https://github.com/tezuka0210/T2VTree)  
  Keywords: t2v, multi-modal, video generation, dit  
- **[CineScene: Implicit 3D as Effective Scene Representation for Cinematic Video Generation](https://arxiv.org/abs/2602.06959v1)**  
  Authors: Kaiyi Huang, Yukun Huang, Yu Li, Jianhong Bai, Xintao Wang, Zinan Lin, Xuefei Ning, Jiwen Yu, Pengfei Wan, Yu Wang, Xihui Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06959v1.pdf)  
  Keywords: text-to-video, trajectory, dit, 3d-aware, video generation, physical, video synthesis  
- **[Stable Velocity: A Variance Perspective on Flow Matching](https://arxiv.org/abs/2602.05435v1)**  
  Authors: Donglin Yang, Yongxing Zhang, Xin Yu, Liang Hou, Xin Tao, Pengfei Wan, Xiaojuan Qi, Renjie Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.05435v1.pdf) | [![GitHub](https://img.shields.io/github/stars/linYDTHU/StableVelocity?style=social)](https://github.com/linYDTHU/StableVelocity)  
  Keywords: text-to-video, dit, dynamics, acceleration, flow matching  
- **[Euphonium: Steering Video Flow Matching via Process Reward Gradient Guided Stochastic Dynamics](https://arxiv.org/abs/2602.04928v2)**  
  Authors: Ruizhe Zhong, Jiesong Lian, Xiaoyue Mi, Zixiang Zhou, Yuan Zhou, Qinglin Lu, Junchi Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.04928v2.pdf) | [![GitHub](https://img.shields.io/github/stars/zerzerzerz/Euphonium?style=social)](https://github.com/zerzerzerz/Euphonium)  
  Keywords: text-to-video, distillation, dit, video generation, dynamics, efficient, flow matching  

### Video Editing

- **[Tele-Omni: a Unified Multimodal Framework for Video Generation and Editing](https://arxiv.org/abs/2602.09609v1)**  
  Authors: Jialun Liu, Yukuo Ma, Xiao Cao, Tian Li, Gonghu Shang, Haibin Huang, Chi Zhang, Xuelong Li, Cong Liu, Junqi Liu, Jiakui Hu, Robby T. Tan, Shiwen Zhang, Liying Yang, Xiaoyan Yang, Qizhen Weng, Xiangzhen Chang, Yuanzhi Liang, Yifan Xu, Zhiyong Huang, Zuoxin Li, Xuelong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.09609v1.pdf)  
  Keywords: text-to-video, image-to-video, dit, video generation, video synthesis, video editing  
- **[Omni-Video 2: Scaling MLLM-Conditioned Diffusion for Unified Video Generation and Editing](https://arxiv.org/abs/2602.08820v1)**  
  Authors: Hao Yang, Zhiyu Tan, Jia Gong, Luozheng Qin, Hesen Chen, Xiaomeng Yang, Yuqing Sun, Yuetan Lin, Mengping Yang, Hao Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.08820v1.pdf)  
  Keywords: video diffusion, text-to-video, dit, benchmark, video generation, diffusion model, efficient, video editing  
- **[PISCO: Precise Video Instance Insertion with Sparse Control](https://arxiv.org/abs/2602.08277v1)**  
  Authors: Xiangbo Gao, Renjie Li, Xinghao Chen, Yuheng Wu, Suofei Feng, Qing Yin, Zhengzhong Tu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.08277v1.pdf)  
  Keywords: controllable, video diffusion, dit, benchmark, video generation, diffusion model, physical, dynamics, film, video editing  
- **[ReRoPE: Repurposing RoPE for Relative Camera Control](https://arxiv.org/abs/2602.08068v1)**  
  Authors: Chunyang Li, Yuanbo Yang, Jiahao Shao, Hongyu Zhou, Katja Schwarz, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.08068v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://sisyphe-lee.github.io/ReRoPE)  
  Keywords: controllable, video diffusion, simulation, image-to-video, i2v, video generation, diffusion model, interactive, efficient, video-to-video, camera control  
- **[RFDM: Residual Flow Diffusion Model for Efficient Causal Video Editing](https://arxiv.org/abs/2602.06871v1)**  
  Authors: Mohammadreza Salehi, Mehdi Noroozi, Luca Morreale, Ruchika Chavhan, Malcolm Chadwick, Alberto Gil Ramos, Abhinav Mehrotra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06871v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://smsd75.github.io/RFDM_page)  
  Keywords: denoising, style, dit, benchmark, video generation, diffusion model, efficient, autoregressive, video-to-video, video editing  
- **[Continuous Control of Editing Models via Adaptive-Origin Guidance](https://arxiv.org/abs/2602.03826v1)**  
  Authors: Alon Wolf, Chen Katzir, Kfir Aberman, Or Patashnik  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03826v1.pdf)  
  Keywords: dit, identity, video editing, video manipulation  
- **[ProxyImg: Towards Highly-Controllable Image Representation via Hierarchical Disentangled Proxy Embedding](https://arxiv.org/abs/2602.01881v1)**  
  Authors: Ye Chen, Yupeng Zhu, Xiongzhen Zhang, Zhewen Wan, Yingzhe Li, Wenjun Zhang, Bingbing Ni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.01881v1.pdf)  
  Keywords: controllable, physics, dit, benchmark, interactive, efficient, physical, temporal consistency, dynamics, video editing  
- **[JUST-DUB-IT: Video Dubbing via Joint Audio-Visual Diffusion](https://arxiv.org/abs/2601.22143v1)**  
  Authors: Anthony Chen, Naomi Ken Korem, Tavi Halperin, Matan Ben Yosef, Urska Jelercic, Ofir Bibi, Or Patashnik, Daniel Cohen-Or  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.22143v1.pdf)  
  Keywords: video diffusion, dit, identity, diffusion model, sound, dynamics, multi-modal, video-to-video  
- **[EditYourself: Audio-Driven Generation and Manipulation of Talking Head Videos with Diffusion Transformers](https://arxiv.org/abs/2601.22127v1)**  
  Authors: John Flynn, Wolfgang Paier, Dimitar Dinev, Sam Nhut Nguyen, Hayk Poghosyan, Manuel Toribio, Sandipan Banerjee, Guy Gafni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.22127v1.pdf)  
  Keywords: video diffusion, audio-driven, dit, human motion, diffusion transformer, identity, diffusion model, talking head, video-to-video  
- **[TeleStyle: Content-Preserving Style Transfer in Images and Videos](https://arxiv.org/abs/2601.20175v1)**  
  Authors: Shiwen Zhang, Xiaoyan Yang, Bojia Zi, Haibin Huang, Chi Zhang, Xuelong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.20175v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Tele-AI/TeleStyle?style=social)](https://github.com/Tele-AI/TeleStyle)  
  Keywords: style, dit, customization, evaluation, diffusion transformer, temporal consistency, video-to-video  

### Video Inpainting & Completion

- **[Learning Physics-Grounded 4D Dynamics with Neural Gaussian Force Fields](https://arxiv.org/abs/2602.00148v2)**  
  Authors: Shiqian Li, Ruihong Shen, Junfeng Ni, Chang Pan, Chi Zhang, Yixin Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.00148v2.pdf)  
  Keywords: simulation, physics, video generation, evaluation, video prediction, world model, interactive, physical, dynamics  
- **[DriveLaW:Unifying Planning and Video Generation in a Latent Driving World](https://arxiv.org/abs/2512.23421v2)**  
  Authors: Tianze Xia, Yongkang Li, Lijun Zhou, Jingfeng Yao, Kaixin Xiong, Haiyang Sun, Bing Wang, Kun Ma, Guang Chen, Hangjun Ye, Wenyu Liu, Xinggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.23421v2.pdf)  
  Keywords: trajectory, benchmark, video generation, video prediction, world model, architecture, autonomous driving  
- **[Autoregressive Flow Matching for Motion Prediction](https://arxiv.org/abs/2512.22688v1)**  
  Authors: Johnathan Xie, Stefan Stojanov, Cristobal Eyzaguirre, Daniel L. K. Yamins, Jiajun Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.22688v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Johnathan-Xie/arfm-motion-prediction?style=social)](https://github.com/Johnathan-Xie/arfm-motion-prediction)  
  Keywords: dit, benchmark, human motion, video generation, robotics, video prediction, autoregressive, flow matching  
- **[Over++: Generative Video Compositing for Layer Interaction Effects](https://arxiv.org/abs/2512.19661v1)**  
  Authors: Luchao Qi, Jiaye Wu, Jun Myeong Choi, Cary Phillips, Roni Sengupta, Dan B Goldman  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.19661v1.pdf)  
  Keywords: dit, video inpainting  
- **[Vidarc: Embodied Video Diffusion Model for Closed-loop Control](https://arxiv.org/abs/2512.17661v1)**  
  Authors: Yao Feng, Chendong Xiang, Xinyi Mao, Hengkai Tan, Zuyue Zhang, Shuhe Huang, Kaiwen Zheng, Haitian Liu, Hang Su, Jun Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.17661v1.pdf)  
  Keywords: video diffusion, video prediction, diffusion model, physical, dynamics, autoregressive  
- **[Flowception: Temporally Expansive Flow Matching for Video Generation](https://arxiv.org/abs/2512.11438v1)**  
  Authors: Tariq Berrada Ifriqi, John Nguyen, Karteek Alahari, Jakob Verbeek, Ricky T. Q. Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.11438v1.pdf)  
  Keywords: denoising, image-to-video, video generation, efficient, autoregressive, flow matching, video interpolation  
- **[Astra: General Interactive World Model with Autoregressive Denoising](https://arxiv.org/abs/2512.08931v3)**  
  Authors: Yixuan Zhu, Jiaqi Feng, Wenzhao Zheng, Yuan Gao, Xin Tao, Pengfei Wan, Jie Zhou, Jiwen Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.08931v3.pdf)  
  Keywords: denoising, streaming, video generation, diffusion transformer, video prediction, world model, interactive, architecture, autonomous driving, autoregressive, camera control  
- **[InverseCrafter: Efficient Video ReCapture as a Latent Domain Inverse Problem](https://arxiv.org/abs/2512.05672v1)**  
  Authors: Yeobin Hong, Suhyeon Lee, Hyungjin Chung, Jong Chul Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.05672v1.pdf) | [![GitHub](https://img.shields.io/github/stars/yeobinhong/InverseCrafter?style=social)](https://github.com/yeobinhong/InverseCrafter)  
  Keywords: novel view, controllable, video diffusion, video inpainting, dit, video generation, diffusion model, efficient, 4d generation, camera control  
- **[Beyond Boundary Frames: Audio-Visual Semantic Guidance for Context-Aware Video Interpolation](https://arxiv.org/abs/2512.03590v1)**  
  Authors: Yuchen Deng, Xiuyang Wu, Hai-Tao Zheng, Jie Wang, Feidiao Yang, Yuxing Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.03590v1.pdf)  
  Keywords: dit, frame interpolation, video interpolation  
- **[LoVoRA: Text-guided and Mask-free Video Object Removal and Addition with Learnable Object-aware Localization](https://arxiv.org/abs/2512.02933v2)**  
  Authors: Zhihan Xiao, Lin Liu, Yixin Gao, Xiaopeng Zhang, Haoxuan Che, Songping Mai, Qi Tian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2512.02933v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://cz-5f.github.io/LoVoRA.github.io)  
  Keywords: image-to-video, video inpainting, dit, evaluation, video translation, temporal consistency, video editing  

### Video Super-Resolution & Enhancement

*Showing the latest 50 out of 58 papers*

- **[FastFlow: Accelerating The Generative Flow Matching Models with Bandit Inference](https://arxiv.org/abs/2602.11105v1)**  
  Authors: Divya Jyoti Bajpai, Dhruv Bhardwaj, Soumya Roy, Tejas Duseja, Harsh Agarwal, Aashay Sandansing, Manjesh Kumar Hanawal  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.11105v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Div290/FastFlow?style=social)](https://github.com/Div290/FastFlow)  
  Keywords: denoising, distillation, trajectory, dit, video generation, efficient, acceleration, flow matching  
- **[Flow caching for autoregressive video generation](https://arxiv.org/abs/2602.10825v1)**  
  Authors: Yuexiao Ma, Xuzhe Zheng, Jing Xu, Xiwei Xu, Feng Ling, Xiawu Zheng, Huafeng Kuang, Huixia Li, Xing Wang, Xuefeng Xiao, Fei Chao, Rongrong Ji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.10825v1.pdf) | [![GitHub](https://img.shields.io/github/stars/mikeallen39/FlowCache?style=social)](https://github.com/mikeallen39/FlowCache)  
  Keywords: denoising, video diffusion, long video, dit, benchmark, video generation, diffusion model, architecture, video synthesis, autoregressive, efficient  
- **[Causality in Video Diffusers is Separable from Denoising](https://arxiv.org/abs/2602.10095v1)**  
  Authors: Xingjian Bai, Guande He, Zhengqi Li, Eli Shechtman, Xun Huang, Zongze Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.10095v1.pdf)  
  Keywords: denoising, trajectory, benchmark, diffusion model, architecture, autoregressive  
- **[Action-to-Action Flow Matching](https://arxiv.org/abs/2602.07322v1)**  
  Authors: Jindou Jia, Gen Li, Xiangyu Chen, Tuo An, Yuxuan Hu, Jingliang Li, Xinying Guo, Jianfei Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.07322v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lorenzo-0-0.github.io/A2A_Flow_Matching)  
  Keywords: denoising, dit, robotics, video generation, fast inference, physical, dynamics, flow matching  
- **[RFDM: Residual Flow Diffusion Model for Efficient Causal Video Editing](https://arxiv.org/abs/2602.06871v1)**  
  Authors: Mohammadreza Salehi, Mehdi Noroozi, Luca Morreale, Ruchika Chavhan, Malcolm Chadwick, Alberto Gil Ramos, Abhinav Mehrotra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06871v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://smsd75.github.io/RFDM_page)  
  Keywords: denoising, style, dit, benchmark, video generation, diffusion model, efficient, autoregressive, video-to-video, video editing  
- **[From Blurry to Believable: Enhancing Low-quality Talking Heads with 3D Generative Priors](https://arxiv.org/abs/2602.06122v1)**  
  Authors: Ding-Jiun Huang, Yuanhao Wang, Shao-Ji Yuan, Albert Mosella-Montoro, Francisco Vicente Carrasco, Cheng Zhang, Fernando De la Torre  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06122v1.pdf)  
  Keywords: super-resolution, identity, talking head, dynamics, avatar, temporal consistency  
- **[Tiled Prompts: Overcoming Prompt Underspecification in Image and Video Super-Resolution](https://arxiv.org/abs/2602.03342v1)**  
  Authors: Bryan Sangwoo Kim, Jonghyun Park, Jong Chul Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03342v1.pdf)  
  Keywords: dit, diffusion model, super-resolution  
- **[GPD: Guided Progressive Distillation for Fast and High-Quality Video Generation](https://arxiv.org/abs/2602.01814v1)**  
  Authors: Xiao Liang, Yunzhu Zhang, Linchao Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.01814v1.pdf)  
  Keywords: denoising, distillation, video generation, diffusion model, dynamics  
- **[FlowCast: Trajectory Forecasting for Scalable Zero-Cost Speculative Flow Matching](https://arxiv.org/abs/2602.01329v1)**  
  Authors: Divya Jyoti Bajpai, Shubham Agarwal, Apoorv Saxena, Kuldeep Kulkarni, Subrata Mitra, Manjesh Kumar Hanawal  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.01329v1.pdf)  
  Keywords: denoising, distillation, trajectory, dit, video generation, evaluation, interactive, acceleration, flow matching  
- **[VideoGPA: Distilling Geometry Priors for 3D-Consistent Video Generation](https://arxiv.org/abs/2601.23286v1)**  
  Authors: Hongyang Du, Junjie Ye, Xiaoyan Cong, Runhao Li, Jingcheng Ni, Aman Agarwal, Zeqi Zhou, Zekun Li, Randall Balestriero, Yue Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2601.23286v1.pdf)  
  Keywords: denoising, video diffusion, video generation, diffusion model, physical, efficient  

### World Models & Simulation

*Showing the latest 50 out of 101 papers*

- **[Chatting with Images for Introspective Visual Thinking](https://arxiv.org/abs/2602.11073v1)**  
  Authors: Junfei Wu, Jian Guan, Qiang Liu, Shu Wu, Liang Wang, Wei Wu, Tienie Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.11073v1.pdf)  
  Keywords: benchmark, interactive  
- **[ArtisanGS: Interactive Tools for Gaussian Splat Selection with AI and Human in the Loop](https://arxiv.org/abs/2602.10173v1)**  
  Authors: Clement Fuji Tsang, Anita Hu, Or Perel, Carsten Kolve, Maria Shugrina  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.10173v1.pdf)  
  Keywords: controllable, video diffusion, simulation, physics, dit, diffusion model, interactive  
- **[Hand2World: Autoregressive Egocentric Interaction Generation via Free-Space Hand Gestures](https://arxiv.org/abs/2602.09600v1)**  
  Authors: Yuxi Wang, Wenqi Ouyang, Tianyi Wei, Yi Dong, Zhiqi Shen, Xingang Pan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.09600v1.pdf)  
  Keywords: gesture, dit, benchmark, video generation, diffusion model, world model, interactive, dynamics, autoregressive, camera control  
- **[AUHead: Realistic Emotional Talking Head Generation via Action Units Control](https://arxiv.org/abs/2602.09534v1)**  
  Authors: Jiayi Lyu, Leigang Qu, Wenjing Zhang, Hanyu Jiang, Kai Liu, Zhenglin Zhou, Xiaobo Xia, Jian Xue, Tat-Seng Chua  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.09534v1.pdf) | [![GitHub](https://img.shields.io/github/stars/laura990501/AUHead_ICLR?style=social)](https://github.com/laura990501/AUHead_ICLR)  
  Keywords: controllable, dit, benchmark, video generation, identity, diffusion model, motion control, talking head, interactive, avatar, film  
- **[WorldCompass: Reinforcement Learning for Long-Horizon World Models](https://arxiv.org/abs/2602.09022v1)**  
  Authors: Zehan Wang, Tengfei Wang, Haiyu Zhang, Xuhui Zuo, Junta Wu, Haoyuan Wang, Wenqiang Sun, Zhenwei Wang, Chenjie Cao, Hengshuang Zhao, Chunchao Guo, Zhou Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.09022v1.pdf)  
  Keywords: video generation, evaluation, world model, interactive, efficient, autoregressive  
- **[WorldArena: A Unified Benchmark for Evaluating Perception and Functional Utility of Embodied World Models](https://arxiv.org/abs/2602.08971v2)**  
  Authors: Yu Shang, Zhuohang Li, Yiding Ma, Weikang Su, Xin Jin, Ziyou Wang, Lei Jin, Xin Zhang, Yinzhou Tang, Haisheng Su, Chen Gao, Wei Wu, Xihui Liu, Dhruv Shah, Zhaoxiang Zhang, Zhibo Chen, Jun Zhu, Yonghong Tian, Tat-Seng Chua, Wenwu Zhu, Yong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.08971v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://world-arena.ai)  
  Keywords: dit, benchmark, video generation, action-conditioned, evaluation, world model, dynamics  
- **[ReRoPE: Repurposing RoPE for Relative Camera Control](https://arxiv.org/abs/2602.08068v1)**  
  Authors: Chunyang Li, Yuanbo Yang, Jiahao Shao, Hongyu Zhou, Katja Schwarz, Yiyi Liao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.08068v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://sisyphe-lee.github.io/ReRoPE)  
  Keywords: controllable, video diffusion, simulation, image-to-video, i2v, video generation, diffusion model, interactive, efficient, video-to-video, camera control  
- **[Driving with DINO: Vision Foundation Features as a Unified Bridge for Sim-to-Real Generation in Autonomous Driving](https://arxiv.org/abs/2602.06159v2)**  
  Authors: Xuyang Chen, Conglang Zhang, Chuanheng Fu, Zihao Yang, Kaixuan Zhou, Yizhi Zhang, Jianan He, Yanfeng Zhang, Mingwei Sun, Zengmao Wang, Zhen Dong, Xiaoxiao Long, Liqiu Meng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.06159v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://albertchen98.github.io/DwD-project)  
  Keywords: controllable, video diffusion, simulation, video generation, autonomous driving  
- **[BridgeV2W: Bridging Video Generation Models to Embodied World Models via Embodiment Masks](https://arxiv.org/abs/2602.03793v1)**  
  Authors: Yixiang Chen, Peiyan Li, Jiabing Yang, Keji He, Xiangnan Wu, Yuan Xu, Kai Wang, Jing Liu, Nianfeng Liu, Yan Huang, Liang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03793v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://BridgeV2W.github.io)  
  Keywords: style, dit, robotics, video generation, evaluation, world model, architecture  
- **[Phaedra: Learning High-Fidelity Discrete Tokenization for the Physical Science](https://arxiv.org/abs/2602.03915v1)**  
  Authors: Levi Lingsch, Georgios Kissas, Johannes Jakubik, Siddhartha Mishra  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2602.03915v1.pdf)  
  Keywords: physical simulation, simulation, dit, video generation, physical, efficient  



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
