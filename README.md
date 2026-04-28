# Awesome Video Diffusions [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Video Diffusion Models and Video Generation. Content is automatically updated daily.

> Last Update: 2026-04-28 02:56:20

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
- [Applications](#applications) (45 papers) - Domain-specific applications of video diffusion models
- [Architecture & Efficiency](#architecture-&-efficiency) (349 papers) - Architectural innovations (DiT, UNet), flow matching, and training/inference efficiency
- [Audio & Multi-modal](#audio-&-multi-modal) (34 papers) - Audio-driven and multi-modal conditioned video generation
- [Controllable Generation](#controllable-generation) (136 papers) - Controllable video generation with motion, camera, pose, or layout guidance
- [Human & Character Animation](#human-&-character-animation) (27 papers) - Human-centric video generation including talking heads, dance, and character animation
- [Image-to-Video Generation](#image-to-video-generation) (42 papers) - Methods for animating still images into videos
- [Long Video Generation](#long-video-generation) (111 papers) - Generating temporally consistent long-form videos beyond short clips
- [Personalization & Customization](#personalization-&-customization) (85 papers) - Personalized video generation with custom subjects, identities, or styles
- [Physical Understanding](#physical-understanding) (147 papers) - Physics-aware video generation and dynamics modeling
- [Surveys & Benchmarks](#surveys-&-benchmarks) (205 papers) - Survey papers, benchmarks, and evaluation metrics for video generation
- [Text-to-Video Generation](#text-to-video-generation) (58 papers) - Foundation models and methods for generating videos from text prompts
- [Video Editing](#video-editing) (30 papers) - Diffusion-based video editing, style transfer, and manipulation
- [Video Inpainting & Completion](#video-inpainting-&-completion) (6 papers) - Video inpainting, completion, outpainting, and temporal prediction
- [Video Super-Resolution & Enhancement](#video-super-resolution-&-enhancement) (62 papers) - Video quality improvement, upscaling, restoration, and frame interpolation
- [World Models & Simulation](#world-models-&-simulation) (97 papers) - Video generation as world simulators and interactive environment generation



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3D-aware Video Generation

- **[AnyRecon: Arbitrary-View 3D Reconstruction with Video Diffusion Model](https://arxiv.org/abs/2604.19747v1)**  
  Authors: Yutian Chen, Shi Guo, Renbiao Jin, Tianshuo Yang, Xin Cai, Yawen Luo, Mingxin Yang, Mulin Yu, Linning Xu, Tianfan Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19747v1.pdf)  
  Keywords: video diffusion, diffusion model, novel view, dit, distillation  
- **[MultiWorld: Scalable Multi-Agent Multi-View Video World Models](https://arxiv.org/abs/2604.18564v2)**  
  Authors: Haoyu Wu, Jiwen Yu, Yingtian Zou, Xihui Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.18564v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://multi-world.github.io)  
  Keywords: video generation, world model, dit, dynamics, multi-view video, action-conditioned  
- **[ArtifactWorld: Scaling 3D Gaussian Splatting Artifact Restoration via Video Generation Models](https://arxiv.org/abs/2604.12251v1)**  
  Authors: Xinliang Wang, Yifeng Shi, Zhenyu Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.12251v1.pdf)  
  Keywords: video generation, video diffusion, novel view  
- **[Rays as Pixels: Learning A Joint Distribution of Videos and Camera Trajectories](https://arxiv.org/abs/2604.09429v3)**  
  Authors: Wonbong Jang, Shikun Liu, Soubhik Sanyal, Juan Camilo Perez, Kam Woh Ng, Sanskar Agrawal, Juan-Manuel Perez-Rua, Yiannis Douratsos, Tao Xiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.09429v3.pdf)  
  Keywords: video diffusion, video generation, diffusion model, novel view, dit, trajectory  
- **[Novel View Synthesis as Video Completion](https://arxiv.org/abs/2604.08500v1)**  
  Authors: Qi Wu, Khiem Vuong, Minsik Jeon, Srinivasa Narasimhan, Deva Ramanan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08500v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://frame-crafter.github.io)  
  Keywords: video diffusion, benchmark, video completion, diffusion model, novel view  
- **[Multi-View Video Diffusion Policy: A 3D Spatio-Temporal-Aware Video Action Model](https://arxiv.org/abs/2604.03181v1)**  
  Authors: Peiyan Li, Yixiang Chen, Yuan Xu, Jiabing Yang, Xiangnan Wu, Jun Guo, Nan Sun, Long Qian, Xinghang Li, Xin Xiao, Jing Liu, Nianfeng Liu, Tao Kong, Yan Huang, Liang Wang, Tieniu Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.03181v1.pdf)  
  Keywords: video diffusion, multi-view video, dit, dynamics, efficient  
- **[Control-DINO: Feature Space Conditioning for Controllable Image-to-Video Diffusion](https://arxiv.org/abs/2604.01761v1)**  
  Authors: Edoardo A. Dominici, Thomas Deixelberger, Konstantinos Vardis, Markus Steinberger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01761v1.pdf)  
  Keywords: controllable, video diffusion, simulation, diffusion model, novel view, image-to-video, architecture, style, dit  
- **[HVG-3D: Bridging Real and Simulation Domains for 3D-Conditional Hand-Object Interaction Video Synthesis](https://arxiv.org/abs/2604.03305v1)**  
  Authors: Mingjin Chen, Junhao Chen, Zhaoxin Fan, Yujian Lee, Zichen Dang, Lili Wang, Yawen Cui, Lap-Pui Chau, Yi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.03305v1.pdf)  
  Keywords: simulation, video generation, 3d-aware, video synthesis, architecture, dit  
- **[I3DM: Implicit 3D-aware Memory Retrieval and Injection for Consistent Video Scene Generation](https://arxiv.org/abs/2603.23413v1)**  
  Authors: Jia Li, Han Yan, Yihang Chen, Siqi Li, Xibin Song, Yifu Wang, Jianfei Cai, Tien-Tsin Wong, Pan Ji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23413v1.pdf)  
  Keywords: video generation, 3d-aware, novel view, camera control, dit  
- **[GO-Renderer: Generative Object Rendering with 3D-aware Controllable Video Diffusion Models](https://arxiv.org/abs/2603.23246v1)**  
  Authors: Zekai Gu, Shuoxuan Feng, Yansong Wang, Hanzhuo Huang, Zhongshuo Du, Chengfeng Zhao, Chengwei Ren, Peng Wang, Yuan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23246v1.pdf)  
  Keywords: controllable, video diffusion, 3d-aware, diffusion model, dit, efficient  

### Applications

- **[HFS-TriNet: A Three-Branch Collaborative Feature Learning Network for Prostate Cancer Classification from TRUS Videos](https://arxiv.org/abs/2604.22388v1)**  
  Authors: Xu Lu, Qianhong Peng, Qihao Zhou, Shaopeng Liu, Xiuqin Ye, Chuan Yang, Yuan Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.22388v1.pdf)  
  Keywords: medical, sound, temporal consistency, denoising  
- **[Seeing Fast and Slow: Learning the Flow of Time in Videos](https://arxiv.org/abs/2604.21931v1)**  
  Authors: Yen-Siang Wu, Rundong Luo, Jingsen Zhu, Tao Tu, Ali Farhadi, Matthew Wallingford, Yu-Chiang Frank Wang, Steve Marschner, Wei-Chiu Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21931v1.pdf)  
  Keywords: controllable, concept, super-resolution, film, video generation, dit  
- **[KD-CVG: A Knowledge-Driven Approach for Creative Video Generation](https://arxiv.org/abs/2604.21362v1)**  
  Authors: Linkai Liu, Wei Feng, Xi Zhao, Shen Zhang, Xingye Chen, Zheng Zhang, Jingjing Lv, Junjie Shen, Ching Law, Yuchen Zhou, Zipeng Guo, Chao Gou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21362v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kdcvg.github.io/KDCVG)  
  Keywords: text-to-video, video generation, creative, t2v, advertising  
- **[Agentic AI for Personalized Physiotherapy: A Multi-Agent Framework for Generative Video Training and Real-Time Pose Correction](https://arxiv.org/abs/2604.21154v1)**  
  Authors: Abhishek Dharmaratnakar, Srivaths Ranganathan, Anushree Sinha, Debanshu Das  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21154v1.pdf)  
  Keywords: video generation, avatar, video synthesis, architecture, evaluation, medical  
- **[AttentionBender: Manipulating Cross-Attention in Video Diffusion Transformers as a Creative Probe](https://arxiv.org/abs/2604.20936v1)**  
  Authors: Adam Cole, Mick Grierson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.20936v1.pdf)  
  Keywords: video diffusion, video generation, style, dit, creative, diffusion transformer  
- **[Building a Precise Video Language with Human-AI Oversight](https://arxiv.org/abs/2604.21718v2)**  
  Authors: Zhiqiu Lin, Chancharik Mitra, Siyuan Cen, Isaac Li, Yuhan Huang, Yu Tong Tiffany Ling, Hewei Wang, Irene Pi, Shihang Zhu, Ryan Rao, George Liu, Jiaxi Li, Ruojin Li, Yili Han, Yilun Du, Deva Ramanan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21718v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://linzhiqiu.github.io/papers/chai)  
  Keywords: benchmark, film, video generation, dit, dynamics  
- **[X-Cache: Cross-Chunk Block Caching for Few-Step Autoregressive World Models Inference](https://arxiv.org/abs/2604.20289v1)**  
  Authors: Yixiao Zeng, Jianlei Zheng, Chaoda Zheng, Shijia Chen, Mingdian Liu, Tongping Liu, Tengwei Luo, Yu Zhang, Boyang Wang, Linkun Xu, Siyuan Lu, Bo Tian, Xianming Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.20289v1.pdf)  
  Keywords: controllable, video diffusion, interactive, simulation, video generation, autonomous driving, autoregressive, world model, acceleration, evaluation, denoising, dit, action-conditioned  
- **[CityRAG: Stepping Into a City via Spatially-Grounded Video Generation](https://arxiv.org/abs/2604.19741v1)**  
  Authors: Gene Chou, Charles Herrmann, Kyle Genova, Boyang Deng, Songyou Peng, Bharath Hariharan, Jason Y. Zhang, Noah Snavely, Philipp Henzler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19741v1.pdf)  
  Keywords: simulation, video generation, autonomous driving, robotics, i2v, t2v, physical, dit  
- **[CoInteract: Physically-Consistent Human-Object Interaction Video Synthesis via Spatially-Structured Co-Generation](https://arxiv.org/abs/2604.19636v1)**  
  Authors: Xiangyang Luo, Xiaozhe Xin, Tao Feng, Xu Guo, Meiguang Jin, Junfeng Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19636v1.pdf)  
  Keywords: diffusion model, video synthesis, dit, physical, diffusion transformer, advertising  
- **[AutoAWG: Adverse Weather Generation with Adaptive Multi-Controls for Automotive Videos](https://arxiv.org/abs/2604.18993v1)**  
  Authors: Jiagao Hu, Daiguo Zhou, Danzhen Fu, Fuhao Li, Zepeng Wang, Fei Wang, Wenhua Liao, Jiayi Xie, Haiyang Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.18993v1.pdf) | [![GitHub](https://img.shields.io/github/stars/higherhu/AutoAWG?style=social)](https://github.com/higherhu/AutoAWG)  
  Keywords: controllable, video generation, autonomous driving, temporal consistency, style, dit  

### Architecture & Efficiency

*Showing the latest 50 out of 349 papers*

- **[Latent Inter-Frame Pruning: A Training-Free Method Bridging Traditional Video Compression and Modern Diffusion Transformers for Efficient Generation](https://arxiv.org/abs/2604.23858v1)**  
  Authors: Dennis Menn, Chih-Hsien Chou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.23858v1.pdf)  
  Keywords: efficient, video editing, video generation, diffusion model, dit, diffusion transformer  
- **[BurstGP: Enhancing Raw Burst Image Super Resolution with Generative Priors](https://arxiv.org/abs/2604.23508v1)**  
  Authors: Dong Huo, Tristan Aumentado-Armstrong, Samrudhdhi B. Rangrej, Maitreya Suin, Angela Ning Ye, Zhiming Hu, Amanpreet Walia, Amirhossein Kazerouni, Konstantinos G. Derpanis, Iqbal Mohomed, Alex Levinshtein  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.23508v1.pdf)  
  Keywords: diffusion model, super-resolution, dit  
- **[EAD-Net: Emotion-Aware Talking Head Generation with Spatial Refinement and Temporal Coherence](https://arxiv.org/abs/2604.23325v1)**  
  Authors: Yahui Li, Yinfeng Yu, Liejun Wang, Shengjie Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.23325v1.pdf)  
  Keywords: long video, video generation, talking head, temporal consistency, multi-modal, dit  
- **[Agentic World Modeling: Foundations, Capabilities, Laws, and Beyond](https://arxiv.org/abs/2604.22748v1)**  
  Authors: Meng Chu, Xuan Billy Zhang, Kevin Qinghong Lin, Lingdong Kong, Jize Zhang, Teng Tu, Weijian Ma, Ziqi Huang, Senqiao Yang, Wei Huang, Yeying Jin, Zhefan Rao, Jinhui Ye, Xinyu Lin, Xichen Zhang, Qisheng Hu, Shuai Yang, Leyang Shen, Wei Chow, Yifei Dong, Fengyi Wu, Quanyu Long, Bin Xia, Shaozuo Yu, Mingkang Zhu, Wenhu Zhang, Jiehui Huang, Haokun Gui, Haoxuan Che, Long Chen, Qifeng Chen, Wenxuan Zhang, Wenya Wang, Xiaojuan Qi, Yang Deng, Yanwei Li, Mike Zheng Shou, Zhi-Qi Cheng, See-Kiong Ng, Ziwei Liu, Philip Torr, Jiaya Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.22748v1.pdf)  
  Keywords: simulation, video generation, world model, evaluation, dit, physical, dynamics, action-conditioned  
- **[DocPrune:Efficient Document Question Answering via Background, Question, and Comprehension-aware Token Pruning](https://arxiv.org/abs/2604.22281v1)**  
  Authors: Joonmyung Choi, Sanghyeok Lee, Jongha Kim, Sehyung Kim, Dohwan Ko, Jihyung Kil, Hyunwoo J. Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.22281v1.pdf)  
  Keywords: efficient, multi-modal, dit  
- **[Seeing Fast and Slow: Learning the Flow of Time in Videos](https://arxiv.org/abs/2604.21931v1)**  
  Authors: Yen-Siang Wu, Rundong Luo, Jingsen Zhu, Tao Tu, Ali Farhadi, Matthew Wallingford, Yu-Chiang Frank Wang, Steve Marschner, Wei-Chiu Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21931v1.pdf)  
  Keywords: controllable, concept, super-resolution, film, video generation, dit  
- **[WorldMark: A Unified Benchmark Suite for Interactive Video World Models](https://arxiv.org/abs/2604.21686v1)**  
  Authors: Xiaojie Xu, Zhengyuan Lin, Kang He, Yukang Feng, Xiaofeng Mao, Yuanyang Yin, Kaipeng Zhang, Yongtao Ge  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21686v1.pdf)  
  Keywords: interactive, benchmark, video generation, world model, image-to-video, evaluation, style, dit, trajectory  
- **[Exploring the Role of Synthetic Data Augmentation in Controllable Human-Centric Video Generation](https://arxiv.org/abs/2604.21291v1)**  
  Authors: Yuanchen Fei, Yude Zou, Zejian Kang, Ming Li, Jiaying Zhou, Xiangru Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21291v1.pdf)  
  Keywords: controllable, video generation, video synthesis, temporal consistency, efficient, identity  
- **[Sparse Forcing: Native Trainable Sparse Attention for Real-time Autoregressive Diffusion Video Generation](https://arxiv.org/abs/2604.21221v1)**  
  Authors: Boxun Xu, Yuming Du, Zichang Liu, Siyu Yang, Ziyang Jiang, Siqi Yan, Rajasi Saha, Albert Pumarola, Wenchen Wang, Peng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21221v1.pdf)  
  Keywords: video diffusion, text-to-video, video generation, diffusion model, autoregressive, efficient  
- **[Agentic AI for Personalized Physiotherapy: A Multi-Agent Framework for Generative Video Training and Real-Time Pose Correction](https://arxiv.org/abs/2604.21154v1)**  
  Authors: Abhishek Dharmaratnakar, Srivaths Ranganathan, Anushree Sinha, Debanshu Das  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21154v1.pdf)  
  Keywords: video generation, avatar, video synthesis, architecture, evaluation, medical  

### Audio & Multi-modal

- **[CineAGI: Character-Consistent Movie Creation through LLM-Orchestrated Multi-Modal Generation and Cross-Scene Integration](https://arxiv.org/abs/2604.23579v1)**  
  Authors: Tianyidan Xie, Zhentao Huang, Mingjie Wang, Xin Huang, Jun Zhou, Minglun Gong, Zili Yi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.23579v1.pdf)  
  Keywords: video generation, identity, multi-modal  
- **[EAD-Net: Emotion-Aware Talking Head Generation with Spatial Refinement and Temporal Coherence](https://arxiv.org/abs/2604.23325v1)**  
  Authors: Yahui Li, Yinfeng Yu, Liejun Wang, Shengjie Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.23325v1.pdf)  
  Keywords: long video, video generation, talking head, temporal consistency, multi-modal, dit  
- **[HFS-TriNet: A Three-Branch Collaborative Feature Learning Network for Prostate Cancer Classification from TRUS Videos](https://arxiv.org/abs/2604.22388v1)**  
  Authors: Xu Lu, Qianhong Peng, Qihao Zhou, Shaopeng Liu, Xiuqin Ye, Chuan Yang, Yuan Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.22388v1.pdf)  
  Keywords: medical, sound, temporal consistency, denoising  
- **[DocPrune:Efficient Document Question Answering via Background, Question, and Comprehension-aware Token Pruning](https://arxiv.org/abs/2604.22281v1)**  
  Authors: Joonmyung Choi, Sanghyeok Lee, Jongha Kim, Sehyung Kim, Dohwan Ko, Jihyung Kil, Hyunwoo J. Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.22281v1.pdf)  
  Keywords: efficient, multi-modal, dit  
- **[MMControl: Unified Multi-Modal Control for Joint Audio-Video Generation](https://arxiv.org/abs/2604.19679v2)**  
  Authors: Liyang Li, Wen Wang, Canyu Zhao, Tianjian Feng, Zhiyue Zhao, Hao Chen, Chunhua Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19679v2.pdf)  
  Keywords: controllable, video diffusion, video generation, layout, multi-modal, dit, diffusion transformer, identity  
- **[Attention-based Multi-modal Deep Learning Model of Spatio-temporal Crop Yield Prediction with Satellite, Soil and Climate Data](https://arxiv.org/abs/2604.19217v1)**  
  Authors: Gopal Krishna Shyam, Ila Chandrakar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19217v1.pdf)  
  Keywords: architecture, multi-modal, dit  
- **[OmniHuman: A Large-scale Dataset and Benchmark for Human-Centric Video Generation](https://arxiv.org/abs/2604.18326v1)**  
  Authors: Lei Zhu, Xing Cai, Yingjie Chen, Yiheng Li, Binxin Yang, Hao Liu, Jie Chen, Chen Li, Jing LYu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.18326v1.pdf)  
  Keywords: benchmark, video generation, video synthesis, multi-modal, evaluation, physical  
- **[TurboTalk: Progressive Distillation for One-Step Audio-Driven Talking Avatar Generation](https://arxiv.org/abs/2604.14580v1)**  
  Authors: Xiangyu Liu, Feng Gao, Xiaomei Zhang, Yong Zhang, Xiaoming Wei, Zhen Lei, Xiangyu Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.14580v1.pdf)  
  Keywords: video diffusion, diffusion model, avatar, audio-driven, denoising, distillation  
- **[Seedance 2.0: Advancing Video Generation for World Complexity](https://arxiv.org/abs/2604.14148v1)**  
  Authors: Team Seedance, De Chen, Liyang Chen, Xin Chen, Ying Chen, Zhuo Chen, Zhuowei Chen, Feng Cheng, Tianheng Cheng, Yufeng Cheng, Mojie Chi, Xuyan Chi, Jian Cong, Qinpeng Cui, Fei Ding, Qide Dong, Yujiao Du, Haojie Duanmu, Junliang Fan, Jiarui Fang, Jing Fang, Zetao Fang, Chengjian Feng, Yu Gao, Diandian Gu, Dong Guo, Hanzhong Guo, Qiushan Guo, Boyang Hao, Hongxiang Hao, Haoxun He, Jiaao He, Qian He, Tuyen Hoang, Heng Hu, Ruoqing Hu, Yuxiang Hu, Jiancheng Huang, Weilin Huang, Zhaoyang Huang, Zhongyi Huang, Jishuo Jin, Ming Jing, Ashley Kim, Shanshan Lao, Yichong Leng, Bingchuan Li, Gen Li, Haifeng Li, Huixia Li, Jiashi Li, Ming Li, Xiaojie Li, Xingxing Li, Yameng Li, Yiying Li, Yu Li, Yueyan Li, Chao Liang, Han Liang, Jianzhong Liang, Ying Liang, Wang Liao, J. H. Lien, Shanchuan Lin, Xi Lin, Feng Ling, Yue Ling, Fangfang Liu, Jiawei Liu, Jihao Liu, Jingtuo Liu, Shu Liu, Sichao Liu, Wei Liu, Xue Liu, Zuxi Liu, Ruijie Lu, Lecheng Lyu, Jingting Ma, Tianxiang Ma, Xiaonan Nie, Jingzhe Ning, Junjie Pan, Xitong Pan, Ronggui Peng, Xueqiong Qu, Yuxi Ren, Yuchen Shen, Guang Shi, Lei Shi, Yinglong Song, Fan Sun, Li Sun, Renfei Sun, Wenjing Tang, Boyang Tao, Zirui Tao, Dongliang Wang, Feng Wang, Hulin Wang, Ke Wang, Qingyi Wang, Rui Wang, Shuai Wang, Shulei Wang, Weichen Wang, Xuanda Wang, Yanhui Wang, Yue Wang, Yuping Wang, Yuxuan Wang, Zijie Wang, Ziyu Wang, Guoqiang Wei, Meng Wei, Di Wu, Guohong Wu, Hanjie Wu, Huachao Wu, Jian Wu, Jie Wu, Ruolan Wu, Shaojin Wu, Xiaohu Wu, Xinglong Wu, Yonghui Wu, Ruiqi Xia, Xin Xia, Xuefeng Xiao, Shuang Xu, Bangbang Yang, Jiaqi Yang, Runkai Yang, Tao Yang, Yihang Yang, Zhixian Yang, Ziyan Yang, Fulong Ye, Bingqian Yi, Xing Yin, Yongbin You, Linxiao Yuan, Weihong Zeng, Xuejiao Zeng, Yan Zeng, Siyu Zhai, Zhonghua Zhai, Bowen Zhang, Chenlin Zhang, Heng Zhang, Jun Zhang, Manlin Zhang, Peiyuan Zhang, Shuo Zhang, Xiaohe Zhang, Xiaoying Zhang, Xinyan Zhang, Xinyi Zhang, Yichi Zhang, Zixiang Zhang, Haiyu Zhao, Huating Zhao, Liming Zhao, Yian Zhao, Guangcong Zheng, Jianbin Zheng, Xiaozheng Zheng, Zerong Zheng, Kuan Zhu, Feilong Zuo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.14148v1.pdf)  
  Keywords: video generation, architecture, evaluation, multi-modal, dit, creative, efficient  
- **[HY-World 2.0: A Multi-Modal World Model for Reconstructing, Generating, and Simulating 3D Worlds](https://arxiv.org/abs/2604.14268v1)**  
  Authors: Team HY-World, Chenjie Cao, Xuhui Zuo, Zhenwei Wang, Yisu Zhang, Junta Wu, Zhenyang Liu, Yuning Gong, Yang Liu, Bo Yuan, Chao Zhang, Coopers Li, Dongyuan Guo, Fan Yang, Haiyu Zhang, Hang Cao, Jianchen Zhu, Jiaxin Lin, Jie Xiao, Jihong Zhang, Junlin Yu, Lei Wang, Lifu Wang, Lilin Wang, Linus, Minghui Chen, Peng He, Penghao Zhao, Qi Chen, Rui Chen, Rui Shao, Sicong Liu, Wangchen Qin, Xiaochuan Niu, Xiang Yuan, Yi Sun, Yifei Tang, Yifu Sun, Yihang Lian, Yonghao Tan, Yuhong Liu, Yuyang Yin, Zhiyuan Min, Tengfei Wang, Chunchao Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.14268v1.pdf)  
  Keywords: interactive, benchmark, efficient, world model, architecture, multi-modal, trajectory  

### Controllable Generation

*Showing the latest 50 out of 136 papers*

- **[PhysLayer: Language-Guided Layered Animation with Depth-Aware Physics](https://arxiv.org/abs/2604.23574v1)**  
  Authors: Tianyidan Xie, Zhentao Huang, Mingjie Wang, Xin Huang, Jun Zhou, Minglun Gong, Zili Yi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.23574v1.pdf)  
  Keywords: controllable, simulation, physics, video generation, image animation, video synthesis, image-to-video, evaluation, physical, dynamics  
- **[Seeing Fast and Slow: Learning the Flow of Time in Videos](https://arxiv.org/abs/2604.21931v1)**  
  Authors: Yen-Siang Wu, Rundong Luo, Jingsen Zhu, Tao Tu, Ali Farhadi, Matthew Wallingford, Yu-Chiang Frank Wang, Steve Marschner, Wei-Chiu Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21931v1.pdf)  
  Keywords: controllable, concept, super-resolution, film, video generation, dit  
- **[WorldMark: A Unified Benchmark Suite for Interactive Video World Models](https://arxiv.org/abs/2604.21686v1)**  
  Authors: Xiaojie Xu, Zhengyuan Lin, Kang He, Yukang Feng, Xiaofeng Mao, Yuanyang Yin, Kaipeng Zhang, Yongtao Ge  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21686v1.pdf)  
  Keywords: interactive, benchmark, video generation, world model, image-to-video, evaluation, style, dit, trajectory  
- **[Exploring the Role of Synthetic Data Augmentation in Controllable Human-Centric Video Generation](https://arxiv.org/abs/2604.21291v1)**  
  Authors: Yuanchen Fei, Yude Zou, Zejian Kang, Ming Li, Jiaying Zhou, Xiangru Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21291v1.pdf)  
  Keywords: controllable, video generation, video synthesis, temporal consistency, efficient, identity  
- **[X-Cache: Cross-Chunk Block Caching for Few-Step Autoregressive World Models Inference](https://arxiv.org/abs/2604.20289v1)**  
  Authors: Yixiao Zeng, Jianlei Zheng, Chaoda Zheng, Shijia Chen, Mingdian Liu, Tongping Liu, Tengwei Luo, Yu Zhang, Boyang Wang, Linkun Xu, Siyuan Lu, Bo Tian, Xianming Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.20289v1.pdf)  
  Keywords: controllable, video diffusion, interactive, simulation, video generation, autonomous driving, autoregressive, world model, acceleration, evaluation, denoising, dit, action-conditioned  
- **[ReImagine: Rethinking Controllable High-Quality Human Video Generation via Image-First Synthesis](https://arxiv.org/abs/2604.19720v1)**  
  Authors: Zhengwentai Sun, Keru Zheng, Chenghong Li, Hongjie Liao, Xihe Yang, Heyuan Li, Yihao Zhi, Shuliang Ning, Shuguang Cui, Xiaoguang Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19720v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Taited/ReImagine?style=social)](https://github.com/Taited/ReImagine)  
  Keywords: controllable, video diffusion, video generation, diffusion model, video synthesis, temporal consistency  
- **[MMControl: Unified Multi-Modal Control for Joint Audio-Video Generation](https://arxiv.org/abs/2604.19679v2)**  
  Authors: Liyang Li, Wen Wang, Canyu Zhao, Tianjian Feng, Zhiyue Zhao, Hao Chen, Chunhua Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19679v2.pdf)  
  Keywords: controllable, video diffusion, video generation, layout, multi-modal, dit, diffusion transformer, identity  
- **[Learning to Credit the Right Steps: Objective-aware Process Optimization for Visual Generation](https://arxiv.org/abs/2604.19234v2)**  
  Authors: Rui Li, Ke Hao, Yuanzhi Liang, Haibin Huang, Chi Zhang, Yun Gu, XueLong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19234v2.pdf)  
  Keywords: denoising, video generation, evaluation, dit, trajectory  
- **[AutoAWG: Adverse Weather Generation with Adaptive Multi-Controls for Automotive Videos](https://arxiv.org/abs/2604.18993v1)**  
  Authors: Jiagao Hu, Daiguo Zhou, Danzhen Fu, Fuhao Li, Zepeng Wang, Fei Wang, Wenhua Liao, Jiayi Xie, Haiyang Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.18993v1.pdf) | [![GitHub](https://img.shields.io/github/stars/higherhu/AutoAWG?style=social)](https://github.com/higherhu/AutoAWG)  
  Keywords: controllable, video generation, autonomous driving, temporal consistency, style, dit  
- **[ViPS: Video-informed Pose Spaces for Auto-Rigged Meshes](https://arxiv.org/abs/2604.17623v2)**  
  Authors: Honglin Chen, Karran Pandey, Rundi Wu, Matheus Gadelha, Yannick Hold-Geoffroy, Ayush Tewari, Niloy J. Mitra, Changxi Zheng, Paul Guerrero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.17623v2.pdf)  
  Keywords: controllable, video diffusion, diffusion model, evaluation, dit, physical  

### Human & Character Animation

- **[Talker-T2AV: Joint Talking Audio-Video Generation with Autoregressive Diffusion Modeling](https://arxiv.org/abs/2604.23586v1)**  
  Authors: Zhen Ye, Xu Tan, Aoxiong Yin, Hongzhan Lin, Guangyan Zhang, Peiwen Sun, Yiming Li, Chi-Min Chan, Wei Ye, Shikun Zhang, Wei Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.23586v1.pdf)  
  Keywords: benchmark, video generation, diffusion model, autoregressive, talking head, denoising, diffusion transformer  
- **[EAD-Net: Emotion-Aware Talking Head Generation with Spatial Refinement and Temporal Coherence](https://arxiv.org/abs/2604.23325v1)**  
  Authors: Yahui Li, Yinfeng Yu, Liejun Wang, Shengjie Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.23325v1.pdf)  
  Keywords: long video, video generation, talking head, temporal consistency, multi-modal, dit  
- **[Agentic AI for Personalized Physiotherapy: A Multi-Agent Framework for Generative Video Training and Real-Time Pose Correction](https://arxiv.org/abs/2604.21154v1)**  
  Authors: Abhishek Dharmaratnakar, Srivaths Ranganathan, Anushree Sinha, Debanshu Das  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21154v1.pdf)  
  Keywords: video generation, avatar, video synthesis, architecture, evaluation, medical  
- **[HumanScore: Benchmarking Human Motions in Generated Videos](https://arxiv.org/abs/2604.20157v1)**  
  Authors: Yusu Fang, Tiange Xiang, Tian Tan, Narayan Schuetz, Scott Delp, Li Fei-Fei, Ehsan Adeli  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.20157v1.pdf)  
  Keywords: benchmark, video generation, human motion, architecture, physical, dynamics  
- **[Prompt-to-Gesture: Measuring the Capabilities of Image-to-Video Deictic Gesture Generation](https://arxiv.org/abs/2604.14953v1)**  
  Authors: Hassan Ali, Doreen Jirak, Luca Müller, Stefan Wermter  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.14953v1.pdf)  
  Keywords: video generation, gesture, dit, image-to-video  
- **[TurboTalk: Progressive Distillation for One-Step Audio-Driven Talking Avatar Generation](https://arxiv.org/abs/2604.14580v1)**  
  Authors: Xiangyu Liu, Feng Gao, Xiaomei Zhang, Yong Zhang, Xiaoming Wei, Zhen Lei, Xiangyu Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.14580v1.pdf)  
  Keywords: video diffusion, diffusion model, avatar, audio-driven, denoising, distillation  
- **[Beyond Monologue: Interactive Talking-Listening Avatar Generation with Conversational Audio Context-Aware Kernels](https://arxiv.org/abs/2604.10367v1)**  
  Authors: Yuzhe Weng, Haotian Wang, Xinyi Yu, Xiaoyan Wu, Haoran Xu, Shan He, Jun Du  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.10367v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://warmcongee.github.io/beyond-monologue)  
  Keywords: interactive, video generation, avatar, audio-driven, physical, dynamics  
- **[HumANDiff: Articulated Noise Diffusion for Motion-Consistent Human Video Generation](https://arxiv.org/abs/2604.05961v1)**  
  Authors: Tao Hu, Varun Jampani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.05961v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://taohuumd.github.io/projects/HumANDiff)  
  Keywords: controllable, video diffusion, physics, motion control, video generation, diffusion model, human motion, video synthesis, image-to-video, architecture, style, dit, physical, dynamics  
- **[Vanast: Virtual Try-On with Human Image Animation via Synthetic Triplet Supervision](https://arxiv.org/abs/2604.04934v1)**  
  Authors: Hyunsoo Cha, Wonjung Woo, Byungjun Kim, Hanbyul Joo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04934v1.pdf)  
  Keywords: video diffusion, image animation, virtual try-on, architecture, human animation, diffusion transformer, identity  
- **[DynaVid: Learning to Generate Highly Dynamic Videos using Synthetic Motion Data](https://arxiv.org/abs/2604.01666v1)**  
  Authors: Wonjoon Jin, Jiyun Won, Janghyeok Han, Qi Dai, Chong Luo, Seung-Hwan Baek, Sunghyun Cho  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01666v1.pdf)  
  Keywords: video diffusion, motion control, diffusion model, human motion, video synthesis, dit  

### Image-to-Video Generation

- **[PhysLayer: Language-Guided Layered Animation with Depth-Aware Physics](https://arxiv.org/abs/2604.23574v1)**  
  Authors: Tianyidan Xie, Zhentao Huang, Mingjie Wang, Xin Huang, Jun Zhou, Minglun Gong, Zili Yi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.23574v1.pdf)  
  Keywords: controllable, simulation, physics, video generation, image animation, video synthesis, image-to-video, evaluation, physical, dynamics  
- **[WorldMark: A Unified Benchmark Suite for Interactive Video World Models](https://arxiv.org/abs/2604.21686v1)**  
  Authors: Xiaojie Xu, Zhengyuan Lin, Kang He, Yukang Feng, Xiaofeng Mao, Yuanyang Yin, Kaipeng Zhang, Yongtao Ge  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21686v1.pdf)  
  Keywords: interactive, benchmark, video generation, world model, image-to-video, evaluation, style, dit, trajectory  
- **[CityRAG: Stepping Into a City via Spatially-Grounded Video Generation](https://arxiv.org/abs/2604.19741v1)**  
  Authors: Gene Chou, Charles Herrmann, Kyle Genova, Boyang Deng, Songyou Peng, Bharath Hariharan, Jason Y. Zhang, Noah Snavely, Philipp Henzler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19741v1.pdf)  
  Keywords: simulation, video generation, autonomous driving, robotics, i2v, t2v, physical, dit  
- **[TS-Attn: Temporal-wise Separable Attention for Multi-Event Video Generation](https://arxiv.org/abs/2604.19473v1)**  
  Authors: Hongyu Zhang, Yufan Deng, Zilin Pan, Peng-Tao Jiang, Bo Li, Qibin Hou, Zhiyang Dou, Zhen Dong, Daquan Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19473v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Hong-yu-Zhang/TS-Attn?style=social)](https://github.com/Hong-yu-Zhang/TS-Attn)  
  Keywords: text-to-video, video generation, temporal consistency, image-to-video, t2v, dit  
- **[AnimationBench: Are Video Models Good at Character-Centric Animation?](https://arxiv.org/abs/2604.15299v1)**  
  Authors: Leyi Wu, Pengjun Fang, Kai Sun, Yazhou Xing, Yinwei Wu, Songsong Wang, Ziqi Huang, Dan Zhou, Yingqing He, Ying-Cong Chen, Qifeng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.15299v1.pdf)  
  Keywords: benchmark, video generation, image-to-video, evaluation, i2v, style  
- **[Flow of Truth: Proactive Temporal Forensics for Image-to-Video Generation](https://arxiv.org/abs/2604.15003v1)**  
  Authors: Yuzhuo Chen, Zehua Ma, Han Fang, Hengyi Wang, Guanjie Wang, Weiming Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.15003v1.pdf)  
  Keywords: video generation, image-to-video, creative, dit, i2v  
- **[Prompt-to-Gesture: Measuring the Capabilities of Image-to-Video Deictic Gesture Generation](https://arxiv.org/abs/2604.14953v1)**  
  Authors: Hassan Ali, Doreen Jirak, Luca Müller, Stefan Wermter  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.14953v1.pdf)  
  Keywords: video generation, gesture, dit, image-to-video  
- **[ARGen: Affect-Reinforced Generative Augmentation towards Vision-based Dynamic Emotion Perception](https://arxiv.org/abs/2604.12255v1)**  
  Authors: Huanzhen Wang, Ziheng Zhou, Jiaqi Song, Li He, Yunshi Lan, Yan Wang, Wenqiang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.12255v1.pdf)  
  Keywords: dynamics, video diffusion, dit, image-to-video  
- **[Immune2V: Image Immunization Against Dual-Stream Image-to-Video Generation](https://arxiv.org/abs/2604.10837v1)**  
  Authors: Zeqian Long, Ozgur Kara, Haotian Xue, Yongxin Chen, James M. Rehg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.10837v1.pdf)  
  Keywords: video generation, image-to-video, i2v, dit, trajectory  
- **[Lighting-grounded Video Generation with Renderer-based Agent Reasoning](https://arxiv.org/abs/2604.07966v1)**  
  Authors: Ziqi Cai, Taoyu Yang, Zheng Chang, Si Li, Han Jiang, Shuchen Weng, Boxin Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07966v1.pdf)  
  Keywords: controllable, video diffusion, film, video generation, diffusion model, video synthesis, temporal consistency, image-to-video, layout, video-to-video, dit, trajectory  

### Long Video Generation

*Showing the latest 50 out of 111 papers*

- **[Talker-T2AV: Joint Talking Audio-Video Generation with Autoregressive Diffusion Modeling](https://arxiv.org/abs/2604.23586v1)**  
  Authors: Zhen Ye, Xu Tan, Aoxiong Yin, Hongzhan Lin, Guangyan Zhang, Peiwen Sun, Yiming Li, Chi-Min Chan, Wei Ye, Shikun Zhang, Wei Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.23586v1.pdf)  
  Keywords: benchmark, video generation, diffusion model, autoregressive, talking head, denoising, diffusion transformer  
- **[EAD-Net: Emotion-Aware Talking Head Generation with Spatial Refinement and Temporal Coherence](https://arxiv.org/abs/2604.23325v1)**  
  Authors: Yahui Li, Yinfeng Yu, Liejun Wang, Shengjie Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.23325v1.pdf)  
  Keywords: long video, video generation, talking head, temporal consistency, multi-modal, dit  
- **[HFS-TriNet: A Three-Branch Collaborative Feature Learning Network for Prostate Cancer Classification from TRUS Videos](https://arxiv.org/abs/2604.22388v1)**  
  Authors: Xu Lu, Qianhong Peng, Qihao Zhou, Shaopeng Liu, Xiuqin Ye, Chuan Yang, Yuan Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.22388v1.pdf)  
  Keywords: medical, sound, temporal consistency, denoising  
- **[Exploring the Role of Synthetic Data Augmentation in Controllable Human-Centric Video Generation](https://arxiv.org/abs/2604.21291v1)**  
  Authors: Yuanchen Fei, Yude Zou, Zejian Kang, Ming Li, Jiaying Zhou, Xiangru Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21291v1.pdf)  
  Keywords: controllable, video generation, video synthesis, temporal consistency, efficient, identity  
- **[Sparse Forcing: Native Trainable Sparse Attention for Real-time Autoregressive Diffusion Video Generation](https://arxiv.org/abs/2604.21221v1)**  
  Authors: Boxun Xu, Yuming Du, Zichang Liu, Siyu Yang, Ziyang Jiang, Siqi Yan, Rajasi Saha, Albert Pumarola, Wenchen Wang, Peng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21221v1.pdf)  
  Keywords: video diffusion, text-to-video, video generation, diffusion model, autoregressive, efficient  
- **[DynamicRad: Content-Adaptive Sparse Attention for Long Video Diffusion](https://arxiv.org/abs/2604.20470v1)**  
  Authors: Yongji Long, Shijun Liang, Jintao Li, Yun Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.20470v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Adamlong3/DynamicRad?style=social)](https://github.com/Adamlong3/DynamicRad)  
  Keywords: long video, dynamics, video diffusion, physics  
- **[X-Cache: Cross-Chunk Block Caching for Few-Step Autoregressive World Models Inference](https://arxiv.org/abs/2604.20289v1)**  
  Authors: Yixiao Zeng, Jianlei Zheng, Chaoda Zheng, Shijia Chen, Mingdian Liu, Tongping Liu, Tengwei Luo, Yu Zhang, Boyang Wang, Linkun Xu, Siyuan Lu, Bo Tian, Xianming Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.20289v1.pdf)  
  Keywords: controllable, video diffusion, interactive, simulation, video generation, autonomous driving, autoregressive, world model, acceleration, evaluation, denoising, dit, action-conditioned  
- **[ReImagine: Rethinking Controllable High-Quality Human Video Generation via Image-First Synthesis](https://arxiv.org/abs/2604.19720v1)**  
  Authors: Zhengwentai Sun, Keru Zheng, Chenghong Li, Hongjie Liao, Xihe Yang, Heyuan Li, Yihao Zhi, Shuliang Ning, Shuguang Cui, Xiaoguang Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19720v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Taited/ReImagine?style=social)](https://github.com/Taited/ReImagine)  
  Keywords: controllable, video diffusion, video generation, diffusion model, video synthesis, temporal consistency  
- **[TS-Attn: Temporal-wise Separable Attention for Multi-Event Video Generation](https://arxiv.org/abs/2604.19473v1)**  
  Authors: Hongyu Zhang, Yufan Deng, Zilin Pan, Peng-Tao Jiang, Bo Li, Qibin Hou, Zhiyang Dou, Zhen Dong, Daquan Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19473v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Hong-yu-Zhang/TS-Attn?style=social)](https://github.com/Hong-yu-Zhang/TS-Attn)  
  Keywords: text-to-video, video generation, temporal consistency, image-to-video, t2v, dit  
- **[AutoAWG: Adverse Weather Generation with Adaptive Multi-Controls for Automotive Videos](https://arxiv.org/abs/2604.18993v1)**  
  Authors: Jiagao Hu, Daiguo Zhou, Danzhen Fu, Fuhao Li, Zepeng Wang, Fei Wang, Wenhua Liao, Jiayi Xie, Haiyang Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.18993v1.pdf) | [![GitHub](https://img.shields.io/github/stars/higherhu/AutoAWG?style=social)](https://github.com/higherhu/AutoAWG)  
  Keywords: controllable, video generation, autonomous driving, temporal consistency, style, dit  

### Personalization & Customization

*Showing the latest 50 out of 85 papers*

- **[MuSS: A Large-Scale Dataset and Cinematic Narrative Benchmark for Multi-Shot Subject-to-Video Generation](https://arxiv.org/abs/2604.23789v1)**  
  Authors: Haojie Zhang, Di Wu, Bingyan Liu, Linjie Zhong, Yuancheng Wei, Xingsong Ye, Nanqing Liu, Yaling Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.23789v1.pdf)  
  Keywords: video generation, identity, benchmark  
- **[CineAGI: Character-Consistent Movie Creation through LLM-Orchestrated Multi-Modal Generation and Cross-Scene Integration](https://arxiv.org/abs/2604.23579v1)**  
  Authors: Tianyidan Xie, Zhentao Huang, Mingjie Wang, Xin Huang, Jun Zhou, Minglun Gong, Zili Yi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.23579v1.pdf)  
  Keywords: video generation, identity, multi-modal  
- **[Seeing Fast and Slow: Learning the Flow of Time in Videos](https://arxiv.org/abs/2604.21931v1)**  
  Authors: Yen-Siang Wu, Rundong Luo, Jingsen Zhu, Tao Tu, Ali Farhadi, Matthew Wallingford, Yu-Chiang Frank Wang, Steve Marschner, Wei-Chiu Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21931v1.pdf)  
  Keywords: controllable, concept, super-resolution, film, video generation, dit  
- **[WorldMark: A Unified Benchmark Suite for Interactive Video World Models](https://arxiv.org/abs/2604.21686v1)**  
  Authors: Xiaojie Xu, Zhengyuan Lin, Kang He, Yukang Feng, Xiaofeng Mao, Yuanyang Yin, Kaipeng Zhang, Yongtao Ge  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21686v1.pdf)  
  Keywords: interactive, benchmark, video generation, world model, image-to-video, evaluation, style, dit, trajectory  
- **[Exploring the Role of Synthetic Data Augmentation in Controllable Human-Centric Video Generation](https://arxiv.org/abs/2604.21291v1)**  
  Authors: Yuanchen Fei, Yude Zou, Zejian Kang, Ming Li, Jiaying Zhou, Xiangru Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21291v1.pdf)  
  Keywords: controllable, video generation, video synthesis, temporal consistency, efficient, identity  
- **[AttentionBender: Manipulating Cross-Attention in Video Diffusion Transformers as a Creative Probe](https://arxiv.org/abs/2604.20936v1)**  
  Authors: Adam Cole, Mick Grierson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.20936v1.pdf)  
  Keywords: video diffusion, video generation, style, dit, creative, diffusion transformer  
- **[MMControl: Unified Multi-Modal Control for Joint Audio-Video Generation](https://arxiv.org/abs/2604.19679v2)**  
  Authors: Liyang Li, Wen Wang, Canyu Zhao, Tianjian Feng, Zhiyue Zhao, Hao Chen, Chunhua Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19679v2.pdf)  
  Keywords: controllable, video diffusion, video generation, layout, multi-modal, dit, diffusion transformer, identity  
- **[AutoAWG: Adverse Weather Generation with Adaptive Multi-Controls for Automotive Videos](https://arxiv.org/abs/2604.18993v1)**  
  Authors: Jiagao Hu, Daiguo Zhou, Danzhen Fu, Fuhao Li, Zepeng Wang, Fei Wang, Wenhua Liao, Jiayi Xie, Haiyang Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.18993v1.pdf) | [![GitHub](https://img.shields.io/github/stars/higherhu/AutoAWG?style=social)](https://github.com/higherhu/AutoAWG)  
  Keywords: controllable, video generation, autonomous driving, temporal consistency, style, dit  
- **[DreamShot: Personalized Storyboard Synthesis with Video Diffusion Prior](https://arxiv.org/abs/2604.17195v1)**  
  Authors: Junjia Huang, Binbin Yang, Pengxiang Yan, Jiyang Liu, Bin Xia, Zhao Wang, Yitong Wang, Liang Lin, Guanbin Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.17195v1.pdf)  
  Keywords: controllable, video diffusion, diffusion model, temporal consistency, dit, identity  
- **[AnimationBench: Are Video Models Good at Character-Centric Animation?](https://arxiv.org/abs/2604.15299v1)**  
  Authors: Leyi Wu, Pengjun Fang, Kai Sun, Yazhou Xing, Yinwei Wu, Songsong Wang, Ziqi Huang, Dan Zhou, Yingqing He, Ying-Cong Chen, Qifeng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.15299v1.pdf)  
  Keywords: benchmark, video generation, image-to-video, evaluation, i2v, style  

### Physical Understanding

*Showing the latest 50 out of 147 papers*

- **[PhysLayer: Language-Guided Layered Animation with Depth-Aware Physics](https://arxiv.org/abs/2604.23574v1)**  
  Authors: Tianyidan Xie, Zhentao Huang, Mingjie Wang, Xin Huang, Jun Zhou, Minglun Gong, Zili Yi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.23574v1.pdf)  
  Keywords: controllable, simulation, physics, video generation, image animation, video synthesis, image-to-video, evaluation, physical, dynamics  
- **[Agentic World Modeling: Foundations, Capabilities, Laws, and Beyond](https://arxiv.org/abs/2604.22748v1)**  
  Authors: Meng Chu, Xuan Billy Zhang, Kevin Qinghong Lin, Lingdong Kong, Jize Zhang, Teng Tu, Weijian Ma, Ziqi Huang, Senqiao Yang, Wei Huang, Yeying Jin, Zhefan Rao, Jinhui Ye, Xinyu Lin, Xichen Zhang, Qisheng Hu, Shuai Yang, Leyang Shen, Wei Chow, Yifei Dong, Fengyi Wu, Quanyu Long, Bin Xia, Shaozuo Yu, Mingkang Zhu, Wenhu Zhang, Jiehui Huang, Haokun Gui, Haoxuan Che, Long Chen, Qifeng Chen, Wenxuan Zhang, Wenya Wang, Xiaojuan Qi, Yang Deng, Yanwei Li, Mike Zheng Shou, Zhi-Qi Cheng, See-Kiong Ng, Ziwei Liu, Philip Torr, Jiaya Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.22748v1.pdf)  
  Keywords: simulation, video generation, world model, evaluation, dit, physical, dynamics, action-conditioned  
- **[Can Multimodal Large Language Models Truly Understand Small Objects?](https://arxiv.org/abs/2604.22884v1)**  
  Authors: Fujun Han, Junan Chen, Xintong Zhu, Jingqi Ye, Xuanjie Mao, Tao Chen, Peng Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.22884v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Hanfj-X/SOU?style=social)](https://github.com/Hanfj-X/SOU)  
  Keywords: benchmark, evaluation, physics  
- **[DeVI: Physics-based Dexterous Human-Object Interaction via Synthetic Video Imitation](https://arxiv.org/abs/2604.20841v1)**  
  Authors: Hyeonwoo Kim, Jeonghwan Kim, Kyungwon Cho, Hanbyul Joo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.20841v1.pdf)  
  Keywords: physical, physics, dit  
- **[DynamicRad: Content-Adaptive Sparse Attention for Long Video Diffusion](https://arxiv.org/abs/2604.20470v1)**  
  Authors: Yongji Long, Shijun Liang, Jintao Li, Yun Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.20470v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Adamlong3/DynamicRad?style=social)](https://github.com/Adamlong3/DynamicRad)  
  Keywords: long video, dynamics, video diffusion, physics  
- **[Building a Precise Video Language with Human-AI Oversight](https://arxiv.org/abs/2604.21718v2)**  
  Authors: Zhiqiu Lin, Chancharik Mitra, Siyuan Cen, Isaac Li, Yuhan Huang, Yu Tong Tiffany Ling, Hewei Wang, Irene Pi, Shihang Zhu, Ryan Rao, George Liu, Jiaxi Li, Ruojin Li, Yili Han, Yilun Du, Deva Ramanan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21718v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://linzhiqiu.github.io/papers/chai)  
  Keywords: benchmark, film, video generation, dit, dynamics  
- **[HumanScore: Benchmarking Human Motions in Generated Videos](https://arxiv.org/abs/2604.20157v1)**  
  Authors: Yusu Fang, Tiange Xiang, Tian Tan, Narayan Schuetz, Scott Delp, Li Fei-Fei, Ehsan Adeli  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.20157v1.pdf)  
  Keywords: benchmark, video generation, human motion, architecture, physical, dynamics  
- **[CityRAG: Stepping Into a City via Spatially-Grounded Video Generation](https://arxiv.org/abs/2604.19741v1)**  
  Authors: Gene Chou, Charles Herrmann, Kyle Genova, Boyang Deng, Songyou Peng, Bharath Hariharan, Jason Y. Zhang, Noah Snavely, Philipp Henzler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19741v1.pdf)  
  Keywords: simulation, video generation, autonomous driving, robotics, i2v, t2v, physical, dit  
- **[UniT: Toward a Unified Physical Language for Human-to-Humanoid Policy Learning and World Modeling](https://arxiv.org/abs/2604.19734v1)**  
  Authors: Boyu Chen, Yi Chen, Lu Qiu, Jerry Bai, Yuying Ge, Yixiao Ge  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19734v1.pdf)  
  Keywords: benchmark, simulation, video generation, world model, dit, physical, dynamics  
- **[CoInteract: Physically-Consistent Human-Object Interaction Video Synthesis via Spatially-Structured Co-Generation](https://arxiv.org/abs/2604.19636v1)**  
  Authors: Xiangyang Luo, Xiaozhe Xin, Tao Feng, Xu Guo, Meiguang Jin, Junfeng Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19636v1.pdf)  
  Keywords: diffusion model, video synthesis, dit, physical, diffusion transformer, advertising  

### Surveys & Benchmarks

*Showing the latest 50 out of 205 papers*

- **[MuSS: A Large-Scale Dataset and Cinematic Narrative Benchmark for Multi-Shot Subject-to-Video Generation](https://arxiv.org/abs/2604.23789v1)**  
  Authors: Haojie Zhang, Di Wu, Bingyan Liu, Linjie Zhong, Yuancheng Wei, Xingsong Ye, Nanqing Liu, Yaling Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.23789v1.pdf)  
  Keywords: video generation, identity, benchmark  
- **[Talker-T2AV: Joint Talking Audio-Video Generation with Autoregressive Diffusion Modeling](https://arxiv.org/abs/2604.23586v1)**  
  Authors: Zhen Ye, Xu Tan, Aoxiong Yin, Hongzhan Lin, Guangyan Zhang, Peiwen Sun, Yiming Li, Chi-Min Chan, Wei Ye, Shikun Zhang, Wei Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.23586v1.pdf)  
  Keywords: benchmark, video generation, diffusion model, autoregressive, talking head, denoising, diffusion transformer  
- **[PhysLayer: Language-Guided Layered Animation with Depth-Aware Physics](https://arxiv.org/abs/2604.23574v1)**  
  Authors: Tianyidan Xie, Zhentao Huang, Mingjie Wang, Xin Huang, Jun Zhou, Minglun Gong, Zili Yi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.23574v1.pdf)  
  Keywords: controllable, simulation, physics, video generation, image animation, video synthesis, image-to-video, evaluation, physical, dynamics  
- **[Agentic World Modeling: Foundations, Capabilities, Laws, and Beyond](https://arxiv.org/abs/2604.22748v1)**  
  Authors: Meng Chu, Xuan Billy Zhang, Kevin Qinghong Lin, Lingdong Kong, Jize Zhang, Teng Tu, Weijian Ma, Ziqi Huang, Senqiao Yang, Wei Huang, Yeying Jin, Zhefan Rao, Jinhui Ye, Xinyu Lin, Xichen Zhang, Qisheng Hu, Shuai Yang, Leyang Shen, Wei Chow, Yifei Dong, Fengyi Wu, Quanyu Long, Bin Xia, Shaozuo Yu, Mingkang Zhu, Wenhu Zhang, Jiehui Huang, Haokun Gui, Haoxuan Che, Long Chen, Qifeng Chen, Wenxuan Zhang, Wenya Wang, Xiaojuan Qi, Yang Deng, Yanwei Li, Mike Zheng Shou, Zhi-Qi Cheng, See-Kiong Ng, Ziwei Liu, Philip Torr, Jiaya Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.22748v1.pdf)  
  Keywords: simulation, video generation, world model, evaluation, dit, physical, dynamics, action-conditioned  
- **[Can Multimodal Large Language Models Truly Understand Small Objects?](https://arxiv.org/abs/2604.22884v1)**  
  Authors: Fujun Han, Junan Chen, Xintong Zhu, Jingqi Ye, Xuanjie Mao, Tao Chen, Peng Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.22884v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Hanfj-X/SOU?style=social)](https://github.com/Hanfj-X/SOU)  
  Keywords: benchmark, evaluation, physics  
- **[Context Unrolling in Omni Models](https://arxiv.org/abs/2604.21921v1)**  
  Authors: Ceyuan Yang, Zhijie Lin, Yang Zhao, Fei Xiao, Hao He, Qi Zhao, Chaorui Deng, Kunchang Li, Zihan Ding, Yuwei Guo, Fuyun Wang, Fangqi Zhu, Xiaonan Nie, Shenhan Zhu, Shanchuan Lin, Hongsheng Li, Weilin Huang, Guang Shi, Haoqi Fan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21921v1.pdf)  
  Keywords: benchmark  
- **[WorldMark: A Unified Benchmark Suite for Interactive Video World Models](https://arxiv.org/abs/2604.21686v1)**  
  Authors: Xiaojie Xu, Zhengyuan Lin, Kang He, Yukang Feng, Xiaofeng Mao, Yuanyang Yin, Kaipeng Zhang, Yongtao Ge  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21686v1.pdf)  
  Keywords: interactive, benchmark, video generation, world model, image-to-video, evaluation, style, dit, trajectory  
- **[Agentic AI for Personalized Physiotherapy: A Multi-Agent Framework for Generative Video Training and Real-Time Pose Correction](https://arxiv.org/abs/2604.21154v1)**  
  Authors: Abhishek Dharmaratnakar, Srivaths Ranganathan, Anushree Sinha, Debanshu Das  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21154v1.pdf)  
  Keywords: video generation, avatar, video synthesis, architecture, evaluation, medical  
- **[Building a Precise Video Language with Human-AI Oversight](https://arxiv.org/abs/2604.21718v2)**  
  Authors: Zhiqiu Lin, Chancharik Mitra, Siyuan Cen, Isaac Li, Yuhan Huang, Yu Tong Tiffany Ling, Hewei Wang, Irene Pi, Shihang Zhu, Ryan Rao, George Liu, Jiaxi Li, Ruojin Li, Yili Han, Yilun Du, Deva Ramanan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21718v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://linzhiqiu.github.io/papers/chai)  
  Keywords: benchmark, film, video generation, dit, dynamics  
- **[SignDATA: Data Pipeline for Sign Language Translation](https://arxiv.org/abs/2604.20357v1)**  
  Authors: Kuanwei Chen, Tingyi Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.20357v1.pdf) | [![GitHub](https://img.shields.io/github/stars/balaboom123/signdata-slt?style=social)](https://github.com/balaboom123/signdata-slt)  
  Keywords: video generation, evaluation  

### Text-to-Video Generation

*Showing the latest 50 out of 58 papers*

- **[KD-CVG: A Knowledge-Driven Approach for Creative Video Generation](https://arxiv.org/abs/2604.21362v1)**  
  Authors: Linkai Liu, Wei Feng, Xi Zhao, Shen Zhang, Xingye Chen, Zheng Zhang, Jingjing Lv, Junjie Shen, Ching Law, Yuchen Zhou, Zipeng Guo, Chao Gou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21362v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kdcvg.github.io/KDCVG)  
  Keywords: text-to-video, video generation, creative, t2v, advertising  
- **[Sparse Forcing: Native Trainable Sparse Attention for Real-time Autoregressive Diffusion Video Generation](https://arxiv.org/abs/2604.21221v1)**  
  Authors: Boxun Xu, Yuming Du, Zichang Liu, Siyu Yang, Ziyang Jiang, Siqi Yan, Rajasi Saha, Albert Pumarola, Wenchen Wang, Peng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21221v1.pdf)  
  Keywords: video diffusion, text-to-video, video generation, diffusion model, autoregressive, efficient  
- **[CityRAG: Stepping Into a City via Spatially-Grounded Video Generation](https://arxiv.org/abs/2604.19741v1)**  
  Authors: Gene Chou, Charles Herrmann, Kyle Genova, Boyang Deng, Songyou Peng, Bharath Hariharan, Jason Y. Zhang, Noah Snavely, Philipp Henzler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19741v1.pdf)  
  Keywords: simulation, video generation, autonomous driving, robotics, i2v, t2v, physical, dit  
- **[TS-Attn: Temporal-wise Separable Attention for Multi-Event Video Generation](https://arxiv.org/abs/2604.19473v1)**  
  Authors: Hongyu Zhang, Yufan Deng, Zilin Pan, Peng-Tao Jiang, Bo Li, Qibin Hou, Zhiyang Dou, Zhen Dong, Daquan Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19473v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Hong-yu-Zhang/TS-Attn?style=social)](https://github.com/Hong-yu-Zhang/TS-Attn)  
  Keywords: text-to-video, video generation, temporal consistency, image-to-video, t2v, dit  
- **[FlowC2S: Flowing from Current to Succeeding Frames for Fast and Memory-Efficient Video Continuation](https://arxiv.org/abs/2604.17625v1)**  
  Authors: Hovhannes Margaryan, Quentin Bammey, Christian Sandor  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.17625v1.pdf)  
  Keywords: efficient, evaluation, text-to-video  
- **[Generative Refinement Networks for Visual Synthesis](https://arxiv.org/abs/2604.13030v1)**  
  Authors: Jian Han, Jinlai Liu, Jiahuan Wang, Bingyue Peng, Zehuan Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.13030v1.pdf)  
  Keywords: benchmark, text-to-video, video generation, diffusion model, autoregressive, dit, efficient  
- **[VideoFlexTok: Flexible-Length Coarse-to-Fine Video Tokenization](https://arxiv.org/abs/2604.12887v1)**  
  Authors: Andrei Atanov, Jesse Allardice, Roman Bachmann, Oğuzhan Fatih Kar, R Devon Hjelm, David Griffiths, Peter Fu, Afshin Dehghan, Amir Zamir  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.12887v1.pdf)  
  Keywords: video generation, efficient, long video, text-to-video  
- **[Motif-Video 2B: Technical Report](https://arxiv.org/abs/2604.16503v1)**  
  Authors: Junghwan Lim, Wai Ting Cheung, Minsu Ha, Beomgyu Kim, Taewhan Kim, Haesol Lee, Dongpin Oh, Jeesoo Lee, Taehyun Kim, Minjae Kim, Sungmin Lee, Hyeyeon Cho, Dahye Choi, Jaeheui Her, Jaeyeon Huh, Hanbin Jung, Changjin Kang, Dongseok Kim, Jangwoong Kim, Youngrok Kim, Hyukjin Kweon, Hongjoo Lee, Jeongdoo Lee, Junhyeok Lee, Eunhwan Park, Yeongjae Park, Bokki Ryu, Dongjoo Weon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.16503v1.pdf)  
  Keywords: video generation, efficient, temporal consistency, text-to-video  
- **[When Numbers Speak: Aligning Textual Numerals and Visual Instances in Text-to-Video Diffusion Models](https://arxiv.org/abs/2604.08546v1)**  
  Authors: Zhengyang Sun, Yu Chen, Xin Zhou, Xiaofan Li, Xiwu Chen, Dingkang Liang, Xiang Bai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08546v1.pdf) | [![GitHub](https://img.shields.io/github/stars/H-EmbodVis/NUMINA?style=social)](https://github.com/H-EmbodVis/NUMINA)  
  Keywords: video diffusion, text-to-video, diffusion model, video synthesis, temporal consistency, layout  
- **[SceneScribe-1M: A Large-Scale Video Dataset with Comprehensive Geometric and Semantic Annotations](https://arxiv.org/abs/2604.07990v2)**  
  Authors: Yunnan Wang, Kecheng Zheng, Jianyuan Wang, Minghao Chen, David Novotny, Christian Rupprecht, Yinghao Xu, Xing Zhu, Wenjun Zeng, Xin Jin, Yujun Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07990v2.pdf)  
  Keywords: controllable, benchmark, text-to-video, video generation, video synthesis, camera control, multi-modal  

### Video Editing

- **[Latent Inter-Frame Pruning: A Training-Free Method Bridging Traditional Video Compression and Modern Diffusion Transformers for Efficient Generation](https://arxiv.org/abs/2604.23858v1)**  
  Authors: Dennis Menn, Chih-Hsien Chou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.23858v1.pdf)  
  Keywords: efficient, video editing, video generation, diffusion model, dit, diffusion transformer  
- **[LIVE: Leveraging Image Manipulation Priors for Instruction-based Video Editing](https://arxiv.org/abs/2604.17021v1)**  
  Authors: Weicheng Wang, Zhicheng Zhang, Zhongqi Zhang, Juncheng Zhou, Yongjie Zhu, Wenyu Qin, Meng Wang, Pengfei Wan, Jufeng Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.17021v1.pdf)  
  Keywords: benchmark, video editing, video generation, evaluation, dit  
- **[UniEditBench: A Unified and Cost-Effective Benchmark for Image and Video Editing via Distilled MLLMs](https://arxiv.org/abs/2604.15871v1)**  
  Authors: Lifan Jiang, Tianrun Wu, Yuhang Pei, Chenyang Wang, Boxi Wu, Deng Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.15871v1.pdf) | [![GitHub](https://img.shields.io/github/stars/wesar1/UniEditBench?style=social)](https://github.com/wesar1/UniEditBench)  
  Keywords: dit, benchmark, evaluation, video editing  
- **[Empowering Video Translation using Multimodal Large Language Models](https://arxiv.org/abs/2604.11283v1)**  
  Authors: Bingzheng QU, Kehai Chen, Xuefeng Bai, Min Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.11283v1.pdf)  
  Keywords: controllable, video translation, dit, survey, identity  
- **[Rein3D: Reinforced 3D Indoor Scene Generation with Panoramic Video Diffusion Models](https://arxiv.org/abs/2604.10578v2)**  
  Authors: Dehui Wang, Congsheng Xu, Rong Wei, Yue Shi, Shoufa Chen, Dingxiang Luo, Tianshuo Yang, Xiaokang Yang, Wei Sui, Yusen Qin, Rui Tang, Yao Mu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.10578v2.pdf)  
  Keywords: diffusion model, video-to-video, video diffusion, super-resolution  
- **[InsEdit: Towards Instruction-based Visual Editing via Data-Efficient Video Diffusion Models Adaptation](https://arxiv.org/abs/2604.08646v1)**  
  Authors: Zhefan Rao, Bin Zou, Haoxuan Che, Xuanhua He, Chong Hou Choi, Yanheng Li, Rui Liu, Qifeng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08646v1.pdf)  
  Keywords: video diffusion, benchmark, video editing, video generation, diffusion model, architecture, dit, efficient  
- **[Lighting-grounded Video Generation with Renderer-based Agent Reasoning](https://arxiv.org/abs/2604.07966v1)**  
  Authors: Ziqi Cai, Taoyu Yang, Zheng Chang, Si Li, Han Jiang, Shuchen Weng, Boxin Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07966v1.pdf)  
  Keywords: controllable, video diffusion, film, video generation, diffusion model, video synthesis, temporal consistency, image-to-video, layout, video-to-video, dit, trajectory  
- **[ImVideoEdit: Image-learning Video Editing via 2D Spatial Difference Attention Blocks](https://arxiv.org/abs/2604.07958v2)**  
  Authors: Jiayang Xu, Fan Zhuo, Majun Zhang, Changhao Pan, Zehan Wang, Siyu Chen, Xiaoda Yang, Tao Jin, Zhou Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07958v2.pdf)  
  Keywords: video editing, temporal consistency, dit, dynamics, efficient  
- **[Evolution of Video Generative Foundations](https://arxiv.org/abs/2604.06339v1)**  
  Authors: Teng Hu, Jiangning Zhang, Hongrui Huang, Ran Yi, Zihan Su, Jieyu Weng, Zhucun Xue, Lizhuang Ma, Ming-Hsuan Yang, Dacheng Tao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06339v1.pdf) | [![GitHub](https://img.shields.io/github/stars/sjtuplayer/Awesome-Video-Foundations?style=social)](https://github.com/sjtuplayer/Awesome-Video-Foundations)  
  Keywords: simulation, video editing, video generation, diffusion model, autonomous driving, world model, education, dit, dynamics, survey  
- **[UENR-600K: A Large-Scale Physically Grounded Dataset for Nighttime Video Deraining](https://arxiv.org/abs/2604.04402v1)**  
  Authors: Pei Yang, Hai Ci, Beibei Lin, Yiren Song, Mike Zheng Shou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04402v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://showlab.github.io/UENR-600K)  
  Keywords: video generation, video-to-video, benchmark, physical  

### Video Inpainting & Completion

- **[LMGenDrive: Bridging Multimodal Understanding and Generative World Modeling for End-to-End Driving](https://arxiv.org/abs/2604.08719v1)**  
  Authors: Hao Shao, Letian Wang, Yang Zhou, Yuxuan Hu, Zhuofan Zong, Steven L. Waslander, Wei Zhan, Hongsheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08719v1.pdf)  
  Keywords: benchmark, video generation, autonomous driving, autoregressive, world model, video prediction  
- **[Novel View Synthesis as Video Completion](https://arxiv.org/abs/2604.08500v1)**  
  Authors: Qi Wu, Khiem Vuong, Minsik Jeon, Srinivasa Narasimhan, Deva Ramanan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08500v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://frame-crafter.github.io)  
  Keywords: video diffusion, benchmark, video completion, diffusion model, novel view  
- **[SEM-ROVER: Semantic Voxel-Guided Diffusion for Large-Scale Driving Scene Generation](https://arxiv.org/abs/2604.06113v1)**  
  Authors: Hiba Dahmani, Nathan Piasco, Moussab Bennehar, Luis Roldão, Dzmitry Tsishkou, Laurent Caraffa, Jean-Philippe Tarel, Roland Brémond  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06113v1.pdf)  
  Keywords: diffusion model, outpainting, dit  
- **[ChopGrad: Pixel-Wise Losses for Latent Video Diffusion via Truncated Backpropagation](https://arxiv.org/abs/2603.17812v2)**  
  Authors: Dmitriy Rivkin, Parker Ewen, Lili Gao, Julian Ost, Stefanie Walz, Rasika Kangutkar, Mario Bijelic, Felix Heide  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17812v2.pdf)  
  Keywords: super-resolution, video diffusion, video generation, diffusion model, latent video, dit, efficient, video inpainting, video enhancement  
- **[ConfCtrl: Enabling Precise Camera Control in Video Diffusion via Confidence-Aware Interpolation](https://arxiv.org/abs/2603.09819v1)**  
  Authors: Liudi Yang, George Eskandar, Fengyi Shen, Mohammad Altillawi, Yang Bai, Chi Zhang, Ziyuan Liu, Abhinav Valada  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09819v1.pdf)  
  Keywords: video diffusion, diffusion model, novel view, camera control, dit, video interpolation  
- **[Pinterest Canvas: Large-Scale Image Generation at Pinterest](https://arxiv.org/abs/2603.06453v1)**  
  Authors: Yu Wang, Eric Tzeng, Raymond Shiau, Jie Yang, Dmitry Kislyuk, Charles Rosenberg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06453v1.pdf)  
  Keywords: outpainting, video generation, diffusion model, image-to-video, dit  

### Video Super-Resolution & Enhancement

*Showing the latest 50 out of 62 papers*

- **[Talker-T2AV: Joint Talking Audio-Video Generation with Autoregressive Diffusion Modeling](https://arxiv.org/abs/2604.23586v1)**  
  Authors: Zhen Ye, Xu Tan, Aoxiong Yin, Hongzhan Lin, Guangyan Zhang, Peiwen Sun, Yiming Li, Chi-Min Chan, Wei Ye, Shikun Zhang, Wei Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.23586v1.pdf)  
  Keywords: benchmark, video generation, diffusion model, autoregressive, talking head, denoising, diffusion transformer  
- **[BurstGP: Enhancing Raw Burst Image Super Resolution with Generative Priors](https://arxiv.org/abs/2604.23508v1)**  
  Authors: Dong Huo, Tristan Aumentado-Armstrong, Samrudhdhi B. Rangrej, Maitreya Suin, Angela Ning Ye, Zhiming Hu, Amanpreet Walia, Amirhossein Kazerouni, Konstantinos G. Derpanis, Iqbal Mohomed, Alex Levinshtein  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.23508v1.pdf)  
  Keywords: diffusion model, super-resolution, dit  
- **[HFS-TriNet: A Three-Branch Collaborative Feature Learning Network for Prostate Cancer Classification from TRUS Videos](https://arxiv.org/abs/2604.22388v1)**  
  Authors: Xu Lu, Qianhong Peng, Qihao Zhou, Shaopeng Liu, Xiuqin Ye, Chuan Yang, Yuan Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.22388v1.pdf)  
  Keywords: medical, sound, temporal consistency, denoising  
- **[Seeing Fast and Slow: Learning the Flow of Time in Videos](https://arxiv.org/abs/2604.21931v1)**  
  Authors: Yen-Siang Wu, Rundong Luo, Jingsen Zhu, Tao Tu, Ali Farhadi, Matthew Wallingford, Yu-Chiang Frank Wang, Steve Marschner, Wei-Chiu Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21931v1.pdf)  
  Keywords: controllable, concept, super-resolution, film, video generation, dit  
- **[X-Cache: Cross-Chunk Block Caching for Few-Step Autoregressive World Models Inference](https://arxiv.org/abs/2604.20289v1)**  
  Authors: Yixiao Zeng, Jianlei Zheng, Chaoda Zheng, Shijia Chen, Mingdian Liu, Tongping Liu, Tengwei Luo, Yu Zhang, Boyang Wang, Linkun Xu, Siyuan Lu, Bo Tian, Xianming Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.20289v1.pdf)  
  Keywords: controllable, video diffusion, interactive, simulation, video generation, autonomous driving, autoregressive, world model, acceleration, evaluation, denoising, dit, action-conditioned  
- **[Learning to Credit the Right Steps: Objective-aware Process Optimization for Visual Generation](https://arxiv.org/abs/2604.19234v2)**  
  Authors: Rui Li, Ke Hao, Yuanzhi Liang, Haibin Huang, Chi Zhang, Yun Gu, XueLong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19234v2.pdf)  
  Keywords: denoising, video generation, evaluation, dit, trajectory  
- **[Trustworthy Endoscopic Super-Resolution](https://arxiv.org/abs/2604.18001v1)**  
  Authors: Julio Silva-Rodríguez, Ender Konukoglu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.18001v1.pdf)  
  Keywords: super-resolution, efficient  
- **[Speculative Decoding for Autoregressive Video Generation](https://arxiv.org/abs/2604.17397v1)**  
  Authors: Yuezhou Hu, Jintao Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.17397v1.pdf)  
  Keywords: video diffusion, video generation, autoregressive, video synthesis, acceleration, streaming, denoising, distillation, dit  
- **[Efficient Video Diffusion Models: Advancements and Challenges](https://arxiv.org/abs/2604.15911v1)**  
  Authors: Shitong Shao, Lichen Bai, Pengfei Wan, James Kwok, Zeke Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.15911v1.pdf)  
  Keywords: video diffusion, efficient, diffusion model, video synthesis, acceleration, evaluation, denoising, distillation, trajectory, survey  
- **[TurboTalk: Progressive Distillation for One-Step Audio-Driven Talking Avatar Generation](https://arxiv.org/abs/2604.14580v1)**  
  Authors: Xiangyu Liu, Feng Gao, Xiaomei Zhang, Yong Zhang, Xiaoming Wei, Zhen Lei, Xiangyu Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.14580v1.pdf)  
  Keywords: video diffusion, diffusion model, avatar, audio-driven, denoising, distillation  

### World Models & Simulation

*Showing the latest 50 out of 97 papers*

- **[PhysLayer: Language-Guided Layered Animation with Depth-Aware Physics](https://arxiv.org/abs/2604.23574v1)**  
  Authors: Tianyidan Xie, Zhentao Huang, Mingjie Wang, Xin Huang, Jun Zhou, Minglun Gong, Zili Yi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.23574v1.pdf)  
  Keywords: controllable, simulation, physics, video generation, image animation, video synthesis, image-to-video, evaluation, physical, dynamics  
- **[Agentic World Modeling: Foundations, Capabilities, Laws, and Beyond](https://arxiv.org/abs/2604.22748v1)**  
  Authors: Meng Chu, Xuan Billy Zhang, Kevin Qinghong Lin, Lingdong Kong, Jize Zhang, Teng Tu, Weijian Ma, Ziqi Huang, Senqiao Yang, Wei Huang, Yeying Jin, Zhefan Rao, Jinhui Ye, Xinyu Lin, Xichen Zhang, Qisheng Hu, Shuai Yang, Leyang Shen, Wei Chow, Yifei Dong, Fengyi Wu, Quanyu Long, Bin Xia, Shaozuo Yu, Mingkang Zhu, Wenhu Zhang, Jiehui Huang, Haokun Gui, Haoxuan Che, Long Chen, Qifeng Chen, Wenxuan Zhang, Wenya Wang, Xiaojuan Qi, Yang Deng, Yanwei Li, Mike Zheng Shou, Zhi-Qi Cheng, See-Kiong Ng, Ziwei Liu, Philip Torr, Jiaya Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.22748v1.pdf)  
  Keywords: simulation, video generation, world model, evaluation, dit, physical, dynamics, action-conditioned  
- **[WorldMark: A Unified Benchmark Suite for Interactive Video World Models](https://arxiv.org/abs/2604.21686v1)**  
  Authors: Xiaojie Xu, Zhengyuan Lin, Kang He, Yukang Feng, Xiaofeng Mao, Yuanyang Yin, Kaipeng Zhang, Yongtao Ge  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21686v1.pdf)  
  Keywords: interactive, benchmark, video generation, world model, image-to-video, evaluation, style, dit, trajectory  
- **[X-Cache: Cross-Chunk Block Caching for Few-Step Autoregressive World Models Inference](https://arxiv.org/abs/2604.20289v1)**  
  Authors: Yixiao Zeng, Jianlei Zheng, Chaoda Zheng, Shijia Chen, Mingdian Liu, Tongping Liu, Tengwei Luo, Yu Zhang, Boyang Wang, Linkun Xu, Siyuan Lu, Bo Tian, Xianming Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.20289v1.pdf)  
  Keywords: controllable, video diffusion, interactive, simulation, video generation, autonomous driving, autoregressive, world model, acceleration, evaluation, denoising, dit, action-conditioned  
- **[CityRAG: Stepping Into a City via Spatially-Grounded Video Generation](https://arxiv.org/abs/2604.19741v1)**  
  Authors: Gene Chou, Charles Herrmann, Kyle Genova, Boyang Deng, Songyou Peng, Bharath Hariharan, Jason Y. Zhang, Noah Snavely, Philipp Henzler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19741v1.pdf)  
  Keywords: simulation, video generation, autonomous driving, robotics, i2v, t2v, physical, dit  
- **[UniT: Toward a Unified Physical Language for Human-to-Humanoid Policy Learning and World Modeling](https://arxiv.org/abs/2604.19734v1)**  
  Authors: Boyu Chen, Yi Chen, Lu Qiu, Jerry Bai, Yuying Ge, Yixiao Ge  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19734v1.pdf)  
  Keywords: benchmark, simulation, video generation, world model, dit, physical, dynamics  
- **[How Far Are Video Models from True Multimodal Reasoning?](https://arxiv.org/abs/2604.19193v1)**  
  Authors: Xiaotian Zhang, Jianhui Wei, Yuan Wang, Jie Tan, Yichen Li, Yan Zhang, Ziyi Chen, Daoan Zhang, Dezhi YU, Wei Xu, Songtao Jiang, Zuozhu Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19193v1.pdf)  
  Keywords: interactive, benchmark, simulation, video generation, evaluation, physical, physical simulation  
- **[RoboWM-Bench: A Benchmark for Evaluating World Models in Robotic Manipulation](https://arxiv.org/abs/2604.19092v1)**  
  Authors: Feng Jiang, Yang Chen, Kyle Xu, Yuchen Liu, Haifeng Wang, Zhenhao Shen, Jasper Lu, Shengze Huang, Yuanfei Wang, Chen Xie, Ruihai Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19092v1.pdf)  
  Keywords: benchmark, video generation, world model, evaluation, physical, dynamics  
- **[MultiWorld: Scalable Multi-Agent Multi-View Video World Models](https://arxiv.org/abs/2604.18564v2)**  
  Authors: Haoyu Wu, Jiwen Yu, Yingtian Zou, Xihui Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.18564v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://multi-world.github.io)  
  Keywords: video generation, world model, dit, dynamics, multi-view video, action-conditioned  
- **[WebCompass: Towards Multimodal Web Coding Evaluation for Code Language Models](https://arxiv.org/abs/2604.18224v1)**  
  Authors: Xinping Lei, Xinyu Che, Junqi Xiong, Chenchen Zhang, Yukai Huang, Chenyu Zhou, Haoyang Huang, Minghao Liu, Letian Zhu, Hongyi Ye, Jinhua Hao, Ken Deng, Zizheng Zhan, Han Li, Dailin Li, Yifan Yao, Ming Sun, Zhaoxiang Zhang, Jiaheng Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.18224v1.pdf)  
  Keywords: interactive, benchmark, evaluation, dit  



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
