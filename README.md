# Awesome Video Diffusions [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Video Diffusion Models and Video Generation. Content is automatically updated daily.

> Last Update: 2026-05-05 02:46:15

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

- [3D-aware Video Generation](#3d-aware-video-generation) (25 papers) - Video generation with 3D awareness, multi-view consistency, and 4D content creation
- [Applications](#applications) (48 papers) - Domain-specific applications of video diffusion models
- [Architecture & Efficiency](#architecture-&-efficiency) (352 papers) - Architectural innovations (DiT, UNet), flow matching, and training/inference efficiency
- [Audio & Multi-modal](#audio-&-multi-modal) (33 papers) - Audio-driven and multi-modal conditioned video generation
- [Controllable Generation](#controllable-generation) (133 papers) - Controllable video generation with motion, camera, pose, or layout guidance
- [Human & Character Animation](#human-&-character-animation) (28 papers) - Human-centric video generation including talking heads, dance, and character animation
- [Image-to-Video Generation](#image-to-video-generation) (37 papers) - Methods for animating still images into videos
- [Long Video Generation](#long-video-generation) (109 papers) - Generating temporally consistent long-form videos beyond short clips
- [Personalization & Customization](#personalization-&-customization) (83 papers) - Personalized video generation with custom subjects, identities, or styles
- [Physical Understanding](#physical-understanding) (144 papers) - Physics-aware video generation and dynamics modeling
- [Surveys & Benchmarks](#surveys-&-benchmarks) (212 papers) - Survey papers, benchmarks, and evaluation metrics for video generation
- [Text-to-Video Generation](#text-to-video-generation) (58 papers) - Foundation models and methods for generating videos from text prompts
- [Video Editing](#video-editing) (25 papers) - Diffusion-based video editing, style transfer, and manipulation
- [Video Inpainting & Completion](#video-inpainting-&-completion) (7 papers) - Video inpainting, completion, outpainting, and temporal prediction
- [Video Super-Resolution & Enhancement](#video-super-resolution-&-enhancement) (63 papers) - Video quality improvement, upscaling, restoration, and frame interpolation
- [World Models & Simulation](#world-models-&-simulation) (101 papers) - Video generation as world simulators and interactive environment generation



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
  Keywords: dit, novel view, distillation, diffusion model, video diffusion  
- **[MultiWorld: Scalable Multi-Agent Multi-View Video World Models](https://arxiv.org/abs/2604.18564v2)**  
  Authors: Haoyu Wu, Jiwen Yu, Yingtian Zou, Xihui Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.18564v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://multi-world.github.io)  
  Keywords: world model, action-conditioned, dit, multi-view video, dynamics, video generation  
- **[ArtifactWorld: Scaling 3D Gaussian Splatting Artifact Restoration via Video Generation Models](https://arxiv.org/abs/2604.12251v1)**  
  Authors: Xinliang Wang, Yifeng Shi, Zhenyu Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.12251v1.pdf)  
  Keywords: video generation, novel view, video diffusion  
- **[Rays as Pixels: Learning A Joint Distribution of Videos and Camera Trajectories](https://arxiv.org/abs/2604.09429v3)**  
  Authors: Wonbong Jang, Shikun Liu, Soubhik Sanyal, Juan Camilo Perez, Kam Woh Ng, Sanskar Agrawal, Juan-Manuel Perez-Rua, Yiannis Douratsos, Tao Xiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.09429v3.pdf)  
  Keywords: dit, novel view, diffusion model, trajectory, video generation, video diffusion  
- **[Novel View Synthesis as Video Completion](https://arxiv.org/abs/2604.08500v1)**  
  Authors: Qi Wu, Khiem Vuong, Minsik Jeon, Srinivasa Narasimhan, Deva Ramanan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08500v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://frame-crafter.github.io)  
  Keywords: video completion, novel view, diffusion model, benchmark, video diffusion  
- **[Multi-View Video Diffusion Policy: A 3D Spatio-Temporal-Aware Video Action Model](https://arxiv.org/abs/2604.03181v1)**  
  Authors: Peiyan Li, Yixiang Chen, Yuan Xu, Jiabing Yang, Xiangnan Wu, Jun Guo, Nan Sun, Long Qian, Xinghang Li, Xin Xiao, Jing Liu, Nianfeng Liu, Tao Kong, Yan Huang, Liang Wang, Tieniu Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.03181v1.pdf)  
  Keywords: efficient, dit, multi-view video, dynamics, video diffusion  
- **[Control-DINO: Feature Space Conditioning for Controllable Image-to-Video Diffusion](https://arxiv.org/abs/2604.01761v1)**  
  Authors: Edoardo A. Dominici, Thomas Deixelberger, Konstantinos Vardis, Markus Steinberger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01761v1.pdf)  
  Keywords: controllable, simulation, dit, video diffusion, novel view, diffusion model, style, architecture, image-to-video  
- **[HVG-3D: Bridging Real and Simulation Domains for 3D-Conditional Hand-Object Interaction Video Synthesis](https://arxiv.org/abs/2604.03305v1)**  
  Authors: Mingjin Chen, Junhao Chen, Zhaoxin Fan, Yujian Lee, Zichen Dang, Lili Wang, Yawen Cui, Lap-Pui Chau, Yi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.03305v1.pdf)  
  Keywords: simulation, dit, video synthesis, video generation, 3d-aware, architecture  
- **[I3DM: Implicit 3D-aware Memory Retrieval and Injection for Consistent Video Scene Generation](https://arxiv.org/abs/2603.23413v1)**  
  Authors: Jia Li, Han Yan, Yihang Chen, Siqi Li, Xibin Song, Yifu Wang, Jianfei Cai, Tien-Tsin Wong, Pan Ji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23413v1.pdf)  
  Keywords: dit, camera control, novel view, 3d-aware, video generation  
- **[GO-Renderer: Generative Object Rendering with 3D-aware Controllable Video Diffusion Models](https://arxiv.org/abs/2603.23246v1)**  
  Authors: Zekai Gu, Shuoxuan Feng, Yansong Wang, Hanzhuo Huang, Zhongshuo Du, Chengfeng Zhao, Chengwei Ren, Peng Wang, Yuan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23246v1.pdf)  
  Keywords: controllable, efficient, dit, 3d-aware, diffusion model, video diffusion  

### Applications

- **[TMD-Bench: A Multi-Level Evaluation Paradigm for Music-Dance Co-Generation](https://arxiv.org/abs/2605.01809v1)**  
  Authors: Xiaoda Yang, Majun Zhang, Changhao Pan, Nick Huang, Yang Yuguang, Fan Zhuo, Pengfei Zhou, Jin Zhou, Sizhe Shan, Shan Yang, Miles Yang, Yang You, Zhou Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.01809v1.pdf)  
  Keywords: interactive, creative, video synthesis, evaluation, physical, benchmark  
- **[Physically Native World Models: A Hamiltonian Perspective on Generative World Modeling](https://arxiv.org/abs/2605.00412v1)**  
  Authors: Sen Cui, Jingheng Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.00412v1.pdf)  
  Keywords: controllable, world model, dynamics, robotics, physical, trajectory, autonomous driving  
- **[AesRM: Improving Video Aesthetics with Expert-Level Feedback](https://arxiv.org/abs/2604.28078v1)**  
  Authors: Yujin Han, Yujie Wei, Yefei He, Xinyu Liu, Tianle Li, Zichao Yu, Andi Han, Shiwei Zhang, Tingyu Weng, Difan Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.28078v1.pdf)  
  Keywords: efficient, concept, dit, evaluation, benchmark, video generation, film  
- **[World Model for Robot Learning: A Comprehensive Survey](https://arxiv.org/abs/2605.00080v1)**  
  Authors: Bohan Hou, Gen Li, Jindou Jia, Tuo An, Xinying Guo, Sicong Leng, Haoran Geng, Yanjie Ze, Tatsuya Harada, Philip Torr, Oier Mees, Marc Pollefeys, Zhuang Liu, Jiajun Wu, Pieter Abbeel, Jitendra Malik, Yilun Du, Jianfei Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.00080v1.pdf)  
  Keywords: controllable, world model, simulation, autonomous driving, evaluation, architecture, survey, benchmark, video generation  
- **[Robot Learning from Human Videos: A Survey](https://arxiv.org/abs/2604.27621v1)**  
  Authors: Junyi Ma, Erhang Zhang, Haoran Yang, Ditao Li, Chenyang Xu, Guangming Wang, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.27621v1.pdf) | [![GitHub](https://img.shields.io/github/stars/IRMVLab/awesome-robot-learning-from-human-videos?style=social)](https://github.com/IRMVLab/awesome-robot-learning-from-human-videos)  
  Keywords: robotics, survey, dit, video generation  
- **[Learning from the Unseen: Generative Data Augmentation for Geometric-Semantic Accident Anticipation](https://arxiv.org/abs/2605.00051v1)**  
  Authors: Yanchen Guan, Haicheng Liao, Chengyue Wang, Xingcheng Liu, Jiaxun Zhang, Keqiang Li, Zhenning Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.00051v1.pdf)  
  Keywords: dit, video synthesis, evaluation, benchmark, autonomous driving  
- **[DepthPilot: From Controllability to Interpretability in Colonoscopy Video Generation](https://arxiv.org/abs/2604.26232v1)**  
  Authors: Junhu Fu, Ke Chen, Weidong Guo, Shuyu Liang, Jie Xu, Chen Ma, Kehao Wang, Shengli Lin, Zeju Li, Yuanyuan Wang, Yi Guo, Shuo Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.26232v1.pdf)  
  Keywords: controllable, world model, efficient, denoising, evaluation, medical, dynamics, physical, benchmark, video generation  
- **[HFS-TriNet: A Three-Branch Collaborative Feature Learning Network for Prostate Cancer Classification from TRUS Videos](https://arxiv.org/abs/2604.22388v1)**  
  Authors: Xu Lu, Qianhong Peng, Qihao Zhou, Shaopeng Liu, Xiuqin Ye, Chuan Yang, Yuan Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.22388v1.pdf)  
  Keywords: sound, medical, denoising, temporal consistency  
- **[Seeing Fast and Slow: Learning the Flow of Time in Videos](https://arxiv.org/abs/2604.21931v1)**  
  Authors: Yen-Siang Wu, Rundong Luo, Jingsen Zhu, Tao Tu, Ali Farhadi, Matthew Wallingford, Yu-Chiang Frank Wang, Steve Marschner, Wei-Chiu Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21931v1.pdf)  
  Keywords: controllable, concept, dit, super-resolution, video generation, film  
- **[KD-CVG: A Knowledge-Driven Approach for Creative Video Generation](https://arxiv.org/abs/2604.21362v1)**  
  Authors: Linkai Liu, Wei Feng, Xi Zhao, Shen Zhang, Xingye Chen, Zheng Zhang, Jingjing Lv, Junjie Shen, Ching Law, Yuchen Zhou, Zipeng Guo, Chao Gou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21362v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kdcvg.github.io/KDCVG)  
  Keywords: creative, advertising, video generation, text-to-video, t2v  

### Architecture & Efficiency

*Showing the latest 50 out of 352 papers*

- **[Video Generation with Predictive Latents](https://arxiv.org/abs/2605.02134v1)**  
  Authors: Yian Zhao, Feng Wang, Qiushan Guo, Chang Liu, Xiangyang Ji, Jian Zhang, Jie Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.02134v1.pdf)  
  Keywords: world model, latent video, video generation, dynamics  
- **[Exploring Data-Free LoRA Transferability for Video Diffusion Models](https://arxiv.org/abs/2605.01929v1)**  
  Authors: Yuchen Wang, Wenliang Zhong, Lichen Bai, Zikai Zhou, Shitong Shao, Bojun Cheng, Shuo Chen, Shuo Yang, Zeke Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.01929v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Noahwangyuchen/CASA?style=social)](https://github.com/Noahwangyuchen/CASA)  
  Keywords: dit, video diffusion, distillation, diffusion model, style  
- **[Motion-Aware Caching for Efficient Autoregressive Video Generation](https://arxiv.org/abs/2605.01725v1)**  
  Authors: Jing Xu, Yuexiao Ma, Songwei Liu, Xuzhe Zheng, Shiwei Liu, Chenqian Yan, Xiawu Zheng, Rongrong Ji, Fei Chao, Xing Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.01725v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ywlq/MotionCache?style=social)](https://github.com/ywlq/MotionCache)  
  Keywords: long video, autoregressive, efficient, denoising, video synthesis, dynamics, video generation  
- **[SignVerse-2M: A Two-Million-Clip Pose-Native Universe of 25+ Sign Languages](https://arxiv.org/abs/2605.01720v1)**  
  Authors: Sen Fang, Hongbin Zhong, Yanxin Zhang, Dimitris N. Metaxas  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.01720v1.pdf)  
  Keywords: pose-guided, dit, evaluation, video generation, style  
- **[Video Active Perception: Effective Inference-Time Long-Form Video Understanding with Vision-Language Models](https://arxiv.org/abs/2605.01662v1)**  
  Authors: Martin Q. Ma, Willis Guo, Aditya Agrawal, Ankit Gupta, Paul Pu Liang, Ruslan Salakhutdinov, Louis-Philippe Morency  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.01662v1.pdf)  
  Keywords: efficient, dit, video generation, long-form  
- **[Omni-Fake: Benchmarking Unified Multimodal Social Media Deepfake Detection](https://arxiv.org/abs/2605.01638v1)**  
  Authors: Tianxiao Li, Zhenglin Huang, Haiquan Wen, Yiwei He, Xinze Li, Bingyu Zhu, Wuhui Duan, Congang Chen, Zeyu Fu, Yi Dong, Baoyuan Wu, Jason Li, Guangliang Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.01638v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://tianxiao1201.github.io/omni-fake-project-page)  
  Keywords: benchmark, dit, talking head  
- **[Quaternion Nonlinear Transform-Induced Nuclear Norm for Low-Rank Tensor Completion](https://arxiv.org/abs/2605.01467v1)**  
  Authors: Biswarup Karmakar, Ratikanta Behera  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.01467v1.pdf)  
  Keywords: efficient, benchmark, video inpainting  
- **[UniVidX: A Unified Multimodal Framework for Versatile Video Generation via Diffusion Priors](https://arxiv.org/abs/2605.00658v1)**  
  Authors: Houyuan Chen, Hong Li, Xianghao Kong, Tianrui Zhu, Shaocong Xu, Weiqing Xiao, Yuwei Guo, Chongjie Ye, Lvmin Zhang, Hao Zhao, Anyi Rao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.00658v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://houyuanchen111.github.io/UniVidX.github.io)  
  Keywords: dit, diffusion model, video generation, video diffusion  
- **[PhyCo: Learning Controllable Physical Priors for Generative Motion](https://arxiv.org/abs/2604.28169v1)**  
  Authors: Sriram Narayanan, Ziyu Jiang, Srinivasa Narasimhan, Manmohan Chandraker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.28169v1.pdf)  
  Keywords: controllable, simulation, physics, dit, physical, diffusion model, benchmark, video generation, video diffusion  
- **[AesRM: Improving Video Aesthetics with Expert-Level Feedback](https://arxiv.org/abs/2604.28078v1)**  
  Authors: Yujin Han, Yujie Wei, Yefei He, Xinyu Liu, Tianle Li, Zichao Yu, Andi Han, Shiwei Zhang, Tingyu Weng, Difan Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.28078v1.pdf)  
  Keywords: efficient, concept, dit, evaluation, benchmark, video generation, film  

### Audio & Multi-modal

- **[Divide and Conquer: Decoupled Representation Alignment for Multimodal World Models](https://arxiv.org/abs/2605.01896v1)**  
  Authors: Junyuan Xiao, Dingkang Liang, Xin Zhou, Yixuan Ye, Tongtong Su, Guangmo Yi, Bin Xia, Qiang Lyu, Shurui Shi, Jun Huang, Jianlou Si, Wenming Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.01896v1.pdf)  
  Keywords: world model, multi-modal, diffusion model, video generation  
- **[Lucid-XR: An Extended-Reality Data Engine for Robotic Manipulation](https://arxiv.org/abs/2605.00244v1)**  
  Authors: Yajvan Ravan, Adam Rashid, Alan Yu, Kai McClennen, Gio Huh, Kevin Yang, Zhutian Yang, Qinxi Yu, Xiaolong Wang, Phillip Isola, Ge Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.00244v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lucidxr.github.io)  
  Keywords: simulation, evaluation, multi-modal, physics, video generation  
- **[CineAGI: Character-Consistent Movie Creation through LLM-Orchestrated Multi-Modal Generation and Cross-Scene Integration](https://arxiv.org/abs/2604.23579v1)**  
  Authors: Tianyidan Xie, Zhentao Huang, Mingjie Wang, Xin Huang, Jun Zhou, Minglun Gong, Zili Yi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.23579v1.pdf)  
  Keywords: identity, multi-modal, video generation  
- **[EAD-Net: Emotion-Aware Talking Head Generation with Spatial Refinement and Temporal Coherence](https://arxiv.org/abs/2604.23325v1)**  
  Authors: Yahui Li, Yinfeng Yu, Liejun Wang, Shengjie Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.23325v1.pdf)  
  Keywords: long video, dit, multi-modal, talking head, video generation, temporal consistency  
- **[HFS-TriNet: A Three-Branch Collaborative Feature Learning Network for Prostate Cancer Classification from TRUS Videos](https://arxiv.org/abs/2604.22388v1)**  
  Authors: Xu Lu, Qianhong Peng, Qihao Zhou, Shaopeng Liu, Xiuqin Ye, Chuan Yang, Yuan Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.22388v1.pdf)  
  Keywords: sound, medical, denoising, temporal consistency  
- **[DocPrune:Efficient Document Question Answering via Background, Question, and Comprehension-aware Token Pruning](https://arxiv.org/abs/2604.22281v1)**  
  Authors: Joonmyung Choi, Sanghyeok Lee, Jongha Kim, Sehyung Kim, Dohwan Ko, Jihyung Kil, Hyunwoo J. Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.22281v1.pdf)  
  Keywords: efficient, multi-modal, dit  
- **[MMControl: Unified Multi-Modal Control for Joint Audio-Video Generation](https://arxiv.org/abs/2604.19679v2)**  
  Authors: Liyang Li, Wen Wang, Canyu Zhao, Tianjian Feng, Zhiyue Zhao, Hao Chen, Chunhua Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19679v2.pdf)  
  Keywords: controllable, dit, layout, diffusion transformer, identity, multi-modal, video generation, video diffusion  
- **[Attention-based Multi-modal Deep Learning Model of Spatio-temporal Crop Yield Prediction with Satellite, Soil and Climate Data](https://arxiv.org/abs/2604.19217v1)**  
  Authors: Gopal Krishna Shyam, Ila Chandrakar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19217v1.pdf)  
  Keywords: architecture, multi-modal, dit  
- **[OmniHuman: A Large-scale Dataset and Benchmark for Human-Centric Video Generation](https://arxiv.org/abs/2604.18326v1)**  
  Authors: Lei Zhu, Xing Cai, Yingjie Chen, Yiheng Li, Binxin Yang, Hao Liu, Jie Chen, Chen Li, Jing LYu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.18326v1.pdf)  
  Keywords: video synthesis, evaluation, physical, multi-modal, benchmark, video generation  
- **[TurboTalk: Progressive Distillation for One-Step Audio-Driven Talking Avatar Generation](https://arxiv.org/abs/2604.14580v1)**  
  Authors: Xiangyu Liu, Feng Gao, Xiaomei Zhang, Yong Zhang, Xiaoming Wei, Zhen Lei, Xiangyu Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.14580v1.pdf)  
  Keywords: denoising, avatar, distillation, audio-driven, diffusion model, video diffusion  

### Controllable Generation

*Showing the latest 50 out of 133 papers*

- **[TrajShield: Trajectory-Level Safety Mediation for Defending Text-to-Video Models Against Jailbreak Attacks](https://arxiv.org/abs/2605.01761v1)**  
  Authors: Quanchen Zou, Nizhang Li, Wenxin Zhang, Jiaye Lin, Yangchen Zeng, Xiangzheng Zhang, Zonghao Ying  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.01761v1.pdf)  
  Keywords: trajectory, text-to-video, t2v  
- **[SignVerse-2M: A Two-Million-Clip Pose-Native Universe of 25+ Sign Languages](https://arxiv.org/abs/2605.01720v1)**  
  Authors: Sen Fang, Hongbin Zhong, Yanxin Zhang, Dimitris N. Metaxas  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.01720v1.pdf)  
  Keywords: pose-guided, dit, evaluation, video generation, style  
- **[Valley3: Scaling Omni Foundation Models for E-commerce](https://arxiv.org/abs/2605.01278v1)**  
  Authors: Zeyu Chen, Guanghao Zhou, Qixiang Yin, Ziwang Zhao, Huanjin Yao, Pengjiu Xia, Min Yang, Cen Chen, Minghui Qiu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.01278v1.pdf)  
  Keywords: controllable, benchmark  
- **[Physically Native World Models: A Hamiltonian Perspective on Generative World Modeling](https://arxiv.org/abs/2605.00412v1)**  
  Authors: Sen Cui, Jingheng Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.00412v1.pdf)  
  Keywords: controllable, world model, dynamics, robotics, physical, trajectory, autonomous driving  
- **[PhyCo: Learning Controllable Physical Priors for Generative Motion](https://arxiv.org/abs/2604.28169v1)**  
  Authors: Sriram Narayanan, Ziyu Jiang, Srinivasa Narasimhan, Manmohan Chandraker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.28169v1.pdf)  
  Keywords: controllable, simulation, physics, dit, physical, diffusion model, benchmark, video generation, video diffusion  
- **[World Model for Robot Learning: A Comprehensive Survey](https://arxiv.org/abs/2605.00080v1)**  
  Authors: Bohan Hou, Gen Li, Jindou Jia, Tuo An, Xinying Guo, Sicong Leng, Haoran Geng, Yanjie Ze, Tatsuya Harada, Philip Torr, Oier Mees, Marc Pollefeys, Zhuang Liu, Jiajun Wu, Pieter Abbeel, Jitendra Malik, Yilun Du, Jianfei Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.00080v1.pdf)  
  Keywords: controllable, world model, simulation, autonomous driving, evaluation, architecture, survey, benchmark, video generation  
- **[DepthPilot: From Controllability to Interpretability in Colonoscopy Video Generation](https://arxiv.org/abs/2604.26232v1)**  
  Authors: Junhu Fu, Ke Chen, Weidong Guo, Shuyu Liang, Jie Xu, Chen Ma, Kehao Wang, Shengli Lin, Zeju Li, Yuanyuan Wang, Yi Guo, Shuo Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.26232v1.pdf)  
  Keywords: controllable, world model, efficient, denoising, evaluation, medical, dynamics, physical, benchmark, video generation  
- **[PhysLayer: Language-Guided Layered Animation with Depth-Aware Physics](https://arxiv.org/abs/2604.23574v1)**  
  Authors: Tianyidan Xie, Zhentao Huang, Mingjie Wang, Xin Huang, Jun Zhou, Minglun Gong, Zili Yi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.23574v1.pdf)  
  Keywords: controllable, simulation, video synthesis, evaluation, dynamics, physical, image animation, physics, video generation, image-to-video  
- **[Seeing Fast and Slow: Learning the Flow of Time in Videos](https://arxiv.org/abs/2604.21931v1)**  
  Authors: Yen-Siang Wu, Rundong Luo, Jingsen Zhu, Tao Tu, Ali Farhadi, Matthew Wallingford, Yu-Chiang Frank Wang, Steve Marschner, Wei-Chiu Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21931v1.pdf)  
  Keywords: controllable, concept, dit, super-resolution, video generation, film  
- **[WorldMark: A Unified Benchmark Suite for Interactive Video World Models](https://arxiv.org/abs/2604.21686v1)**  
  Authors: Xiaojie Xu, Zhengyuan Lin, Kang He, Yukang Feng, Xiaofeng Mao, Yuanyang Yin, Kaipeng Zhang, Yongtao Ge  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21686v1.pdf)  
  Keywords: world model, interactive, dit, evaluation, style, trajectory, benchmark, video generation, image-to-video  

### Human & Character Animation

- **[Omni-Fake: Benchmarking Unified Multimodal Social Media Deepfake Detection](https://arxiv.org/abs/2605.01638v1)**  
  Authors: Tianxiao Li, Zhenglin Huang, Haiquan Wen, Yiwei He, Xinze Li, Bingyu Zhu, Wuhui Duan, Congang Chen, Zeyu Fu, Yi Dong, Baoyuan Wu, Jason Li, Guangliang Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.01638v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://tianxiao1201.github.io/omni-fake-project-page)  
  Keywords: benchmark, dit, talking head  
- **[Generate Your Talking Avatar from Video Reference](https://arxiv.org/abs/2604.27918v1)**  
  Authors: Zujin Guo, Zhenhui Ye, Yi Ren, Yuanming Li, Ce Chen, Zhibin Hong, Chen Change Loy  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.27918v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://www.heygen.com/research)  
  Keywords: dit, avatar, identity, benchmark, image-to-video  
- **[HuM-Eval: A Coarse-to-Fine Framework for Human-Centric Video Evaluation](https://arxiv.org/abs/2604.25361v1)**  
  Authors: Bingzi Zhang, Kaisi Guan, Ruihua Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.25361v1.pdf)  
  Keywords: evaluation, text-to-video, human motion, benchmark, video generation  
- **[Talker-T2AV: Joint Talking Audio-Video Generation with Autoregressive Diffusion Modeling](https://arxiv.org/abs/2604.23586v1)**  
  Authors: Zhen Ye, Xu Tan, Aoxiong Yin, Hongzhan Lin, Guangyan Zhang, Peiwen Sun, Yiming Li, Chi-Min Chan, Wei Ye, Shikun Zhang, Wei Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.23586v1.pdf)  
  Keywords: autoregressive, denoising, diffusion transformer, diffusion model, talking head, benchmark, video generation  
- **[EAD-Net: Emotion-Aware Talking Head Generation with Spatial Refinement and Temporal Coherence](https://arxiv.org/abs/2604.23325v1)**  
  Authors: Yahui Li, Yinfeng Yu, Liejun Wang, Shengjie Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.23325v1.pdf)  
  Keywords: long video, dit, multi-modal, talking head, video generation, temporal consistency  
- **[Agentic AI for Personalized Physiotherapy: A Multi-Agent Framework for Generative Video Training and Real-Time Pose Correction](https://arxiv.org/abs/2604.21154v1)**  
  Authors: Abhishek Dharmaratnakar, Srivaths Ranganathan, Anushree Sinha, Debanshu Das  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21154v1.pdf)  
  Keywords: video synthesis, evaluation, avatar, medical, architecture, video generation  
- **[HumanScore: Benchmarking Human Motions in Generated Videos](https://arxiv.org/abs/2604.20157v1)**  
  Authors: Yusu Fang, Tiange Xiang, Tian Tan, Narayan Schuetz, Scott Delp, Li Fei-Fei, Ehsan Adeli  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.20157v1.pdf)  
  Keywords: video generation, dynamics, physical, human motion, benchmark, architecture  
- **[Prompt-to-Gesture: Measuring the Capabilities of Image-to-Video Deictic Gesture Generation](https://arxiv.org/abs/2604.14953v1)**  
  Authors: Hassan Ali, Doreen Jirak, Luca Müller, Stefan Wermter  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.14953v1.pdf)  
  Keywords: dit, video generation, gesture, image-to-video  
- **[TurboTalk: Progressive Distillation for One-Step Audio-Driven Talking Avatar Generation](https://arxiv.org/abs/2604.14580v1)**  
  Authors: Xiangyu Liu, Feng Gao, Xiaomei Zhang, Yong Zhang, Xiaoming Wei, Zhen Lei, Xiangyu Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.14580v1.pdf)  
  Keywords: denoising, avatar, distillation, audio-driven, diffusion model, video diffusion  
- **[Beyond Monologue: Interactive Talking-Listening Avatar Generation with Conversational Audio Context-Aware Kernels](https://arxiv.org/abs/2604.10367v1)**  
  Authors: Yuzhe Weng, Haotian Wang, Xinyi Yu, Xiaoyan Wu, Haoran Xu, Shan He, Jun Du  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.10367v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://warmcongee.github.io/beyond-monologue)  
  Keywords: interactive, avatar, dynamics, audio-driven, physical, video generation  

### Image-to-Video Generation

- **[Generate Your Talking Avatar from Video Reference](https://arxiv.org/abs/2604.27918v1)**  
  Authors: Zujin Guo, Zhenhui Ye, Yi Ren, Yuanming Li, Ce Chen, Zhibin Hong, Chen Change Loy  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.27918v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://www.heygen.com/research)  
  Keywords: dit, avatar, identity, benchmark, image-to-video  
- **[PhysLayer: Language-Guided Layered Animation with Depth-Aware Physics](https://arxiv.org/abs/2604.23574v1)**  
  Authors: Tianyidan Xie, Zhentao Huang, Mingjie Wang, Xin Huang, Jun Zhou, Minglun Gong, Zili Yi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.23574v1.pdf)  
  Keywords: controllable, simulation, video synthesis, evaluation, dynamics, physical, image animation, physics, video generation, image-to-video  
- **[WorldMark: A Unified Benchmark Suite for Interactive Video World Models](https://arxiv.org/abs/2604.21686v1)**  
  Authors: Xiaojie Xu, Zhengyuan Lin, Kang He, Yukang Feng, Xiaofeng Mao, Yuanyang Yin, Kaipeng Zhang, Yongtao Ge  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21686v1.pdf)  
  Keywords: world model, interactive, dit, evaluation, style, trajectory, benchmark, video generation, image-to-video  
- **[CityRAG: Stepping Into a City via Spatially-Grounded Video Generation](https://arxiv.org/abs/2604.19741v1)**  
  Authors: Gene Chou, Charles Herrmann, Kyle Genova, Boyang Deng, Songyou Peng, Bharath Hariharan, Jason Y. Zhang, Noah Snavely, Philipp Henzler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19741v1.pdf)  
  Keywords: i2v, simulation, dit, autonomous driving, video generation, robotics, physical, t2v  
- **[TS-Attn: Temporal-wise Separable Attention for Multi-Event Video Generation](https://arxiv.org/abs/2604.19473v1)**  
  Authors: Hongyu Zhang, Yufan Deng, Zilin Pan, Peng-Tao Jiang, Bo Li, Qibin Hou, Zhiyang Dou, Zhen Dong, Daquan Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19473v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Hong-yu-Zhang/TS-Attn?style=social)](https://github.com/Hong-yu-Zhang/TS-Attn)  
  Keywords: image-to-video, dit, video generation, text-to-video, t2v, temporal consistency  
- **[AnimationBench: Are Video Models Good at Character-Centric Animation?](https://arxiv.org/abs/2604.15299v1)**  
  Authors: Leyi Wu, Pengjun Fang, Kai Sun, Yazhou Xing, Yinwei Wu, Songsong Wang, Ziqi Huang, Dan Zhou, Yingqing He, Ying-Cong Chen, Qifeng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.15299v1.pdf)  
  Keywords: i2v, evaluation, style, benchmark, video generation, image-to-video  
- **[Flow of Truth: Proactive Temporal Forensics for Image-to-Video Generation](https://arxiv.org/abs/2604.15003v1)**  
  Authors: Yuzhuo Chen, Zehua Ma, Han Fang, Hengyi Wang, Guanjie Wang, Weiming Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.15003v1.pdf)  
  Keywords: i2v, creative, dit, video generation, image-to-video  
- **[Prompt-to-Gesture: Measuring the Capabilities of Image-to-Video Deictic Gesture Generation](https://arxiv.org/abs/2604.14953v1)**  
  Authors: Hassan Ali, Doreen Jirak, Luca Müller, Stefan Wermter  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.14953v1.pdf)  
  Keywords: dit, video generation, gesture, image-to-video  
- **[ARGen: Affect-Reinforced Generative Augmentation towards Vision-based Dynamic Emotion Perception](https://arxiv.org/abs/2604.12255v1)**  
  Authors: Huanzhen Wang, Ziheng Zhou, Jiaqi Song, Li He, Yunshi Lan, Yan Wang, Wenqiang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.12255v1.pdf)  
  Keywords: image-to-video, dynamics, dit, video diffusion  
- **[Immune2V: Image Immunization Against Dual-Stream Image-to-Video Generation](https://arxiv.org/abs/2604.10837v1)**  
  Authors: Zeqian Long, Ozgur Kara, Haotian Xue, Yongxin Chen, James M. Rehg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.10837v1.pdf)  
  Keywords: i2v, dit, trajectory, video generation, image-to-video  

### Long Video Generation

*Showing the latest 50 out of 109 papers*

- **[Motion-Aware Caching for Efficient Autoregressive Video Generation](https://arxiv.org/abs/2605.01725v1)**  
  Authors: Jing Xu, Yuexiao Ma, Songwei Liu, Xuzhe Zheng, Shiwei Liu, Chenqian Yan, Xiawu Zheng, Rongrong Ji, Fei Chao, Xing Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.01725v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ywlq/MotionCache?style=social)](https://github.com/ywlq/MotionCache)  
  Keywords: long video, autoregressive, efficient, denoising, video synthesis, dynamics, video generation  
- **[Video Active Perception: Effective Inference-Time Long-Form Video Understanding with Vision-Language Models](https://arxiv.org/abs/2605.01662v1)**  
  Authors: Martin Q. Ma, Willis Guo, Aditya Agrawal, Ankit Gupta, Paul Pu Liang, Ruslan Salakhutdinov, Louis-Philippe Morency  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.01662v1.pdf)  
  Keywords: efficient, dit, video generation, long-form  
- **[ABC: Any-Subset Autoregression via Non-Markovian Diffusion Bridges in Continuous Time and Space](https://arxiv.org/abs/2604.27443v1)**  
  Authors: Gabe Guo, Thanawat Sornwanee, Lutong Hao, Elon Litman, Stefano Ermon, Jose Blanchet  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.27443v1.pdf)  
  Keywords: autoregressive, denoising, dit, dynamics, physical, diffusion model, video generation  
- **[Mutual Forcing: Dual-Mode Self-Evolution for Fast Autoregressive Audio-Video Character Generation](https://arxiv.org/abs/2604.25819v1)**  
  Authors: Yupeng Zhou, Lianghua Huang, Zhifan Wu, Jiabao Wang, Yupeng Shi, Biao Jiang, Daquan Zhou, Yu Liu, Ming-Ming Cheng, Qibin Hou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.25819v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://mutualforcing.github.io)  
  Keywords: autoregressive, dit, distillation, streaming, video generation  
- **[FCMBench-Video: Benchmarking Document Video Intelligence](https://arxiv.org/abs/2604.25186v2)**  
  Authors: Runze Cui, Fangxin Shang, Yehui Yang, Qing Yang, Yanwu Xu, Tao Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.25186v2.pdf)  
  Keywords: evaluation, benchmark, dit, long-form  
- **[Talker-T2AV: Joint Talking Audio-Video Generation with Autoregressive Diffusion Modeling](https://arxiv.org/abs/2604.23586v1)**  
  Authors: Zhen Ye, Xu Tan, Aoxiong Yin, Hongzhan Lin, Guangyan Zhang, Peiwen Sun, Yiming Li, Chi-Min Chan, Wei Ye, Shikun Zhang, Wei Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.23586v1.pdf)  
  Keywords: autoregressive, denoising, diffusion transformer, diffusion model, talking head, benchmark, video generation  
- **[EAD-Net: Emotion-Aware Talking Head Generation with Spatial Refinement and Temporal Coherence](https://arxiv.org/abs/2604.23325v1)**  
  Authors: Yahui Li, Yinfeng Yu, Liejun Wang, Shengjie Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.23325v1.pdf)  
  Keywords: long video, dit, multi-modal, talking head, video generation, temporal consistency  
- **[HFS-TriNet: A Three-Branch Collaborative Feature Learning Network for Prostate Cancer Classification from TRUS Videos](https://arxiv.org/abs/2604.22388v1)**  
  Authors: Xu Lu, Qianhong Peng, Qihao Zhou, Shaopeng Liu, Xiuqin Ye, Chuan Yang, Yuan Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.22388v1.pdf)  
  Keywords: sound, medical, denoising, temporal consistency  
- **[Exploring the Role of Synthetic Data Augmentation in Controllable Human-Centric Video Generation](https://arxiv.org/abs/2604.21291v1)**  
  Authors: Yuanchen Fei, Yude Zou, Zejian Kang, Ming Li, Jiaying Zhou, Xiangru Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21291v1.pdf)  
  Keywords: controllable, efficient, video synthesis, identity, video generation, temporal consistency  
- **[Sparse Forcing: Native Trainable Sparse Attention for Real-time Autoregressive Diffusion Video Generation](https://arxiv.org/abs/2604.21221v1)**  
  Authors: Boxun Xu, Yuming Du, Zichang Liu, Siyu Yang, Ziyang Jiang, Siqi Yan, Rajasi Saha, Albert Pumarola, Wenchen Wang, Peng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21221v1.pdf)  
  Keywords: autoregressive, efficient, text-to-video, diffusion model, video generation, video diffusion  

### Personalization & Customization

*Showing the latest 50 out of 83 papers*

- **[Exploring Data-Free LoRA Transferability for Video Diffusion Models](https://arxiv.org/abs/2605.01929v1)**  
  Authors: Yuchen Wang, Wenliang Zhong, Lichen Bai, Zikai Zhou, Shitong Shao, Bojun Cheng, Shuo Chen, Shuo Yang, Zeke Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.01929v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Noahwangyuchen/CASA?style=social)](https://github.com/Noahwangyuchen/CASA)  
  Keywords: dit, video diffusion, distillation, diffusion model, style  
- **[SignVerse-2M: A Two-Million-Clip Pose-Native Universe of 25+ Sign Languages](https://arxiv.org/abs/2605.01720v1)**  
  Authors: Sen Fang, Hongbin Zhong, Yanxin Zhang, Dimitris N. Metaxas  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.01720v1.pdf)  
  Keywords: pose-guided, dit, evaluation, video generation, style  
- **[AesRM: Improving Video Aesthetics with Expert-Level Feedback](https://arxiv.org/abs/2604.28078v1)**  
  Authors: Yujin Han, Yujie Wei, Yefei He, Xinyu Liu, Tianle Li, Zichao Yu, Andi Han, Shiwei Zhang, Tingyu Weng, Difan Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.28078v1.pdf)  
  Keywords: efficient, concept, dit, evaluation, benchmark, video generation, film  
- **[Generate Your Talking Avatar from Video Reference](https://arxiv.org/abs/2604.27918v1)**  
  Authors: Zujin Guo, Zhenhui Ye, Yi Ren, Yuanming Li, Ce Chen, Zhibin Hong, Chen Change Loy  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.27918v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://www.heygen.com/research)  
  Keywords: dit, avatar, identity, benchmark, image-to-video  
- **[MuSS: A Large-Scale Dataset and Cinematic Narrative Benchmark for Multi-Shot Subject-to-Video Generation](https://arxiv.org/abs/2604.23789v1)**  
  Authors: Haojie Zhang, Di Wu, Bingyan Liu, Linjie Zhong, Yuancheng Wei, Xingsong Ye, Nanqing Liu, Yaling Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.23789v1.pdf)  
  Keywords: benchmark, identity, video generation  
- **[CineAGI: Character-Consistent Movie Creation through LLM-Orchestrated Multi-Modal Generation and Cross-Scene Integration](https://arxiv.org/abs/2604.23579v1)**  
  Authors: Tianyidan Xie, Zhentao Huang, Mingjie Wang, Xin Huang, Jun Zhou, Minglun Gong, Zili Yi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.23579v1.pdf)  
  Keywords: identity, multi-modal, video generation  
- **[Seeing Fast and Slow: Learning the Flow of Time in Videos](https://arxiv.org/abs/2604.21931v1)**  
  Authors: Yen-Siang Wu, Rundong Luo, Jingsen Zhu, Tao Tu, Ali Farhadi, Matthew Wallingford, Yu-Chiang Frank Wang, Steve Marschner, Wei-Chiu Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21931v1.pdf)  
  Keywords: controllable, concept, dit, super-resolution, video generation, film  
- **[WorldMark: A Unified Benchmark Suite for Interactive Video World Models](https://arxiv.org/abs/2604.21686v1)**  
  Authors: Xiaojie Xu, Zhengyuan Lin, Kang He, Yukang Feng, Xiaofeng Mao, Yuanyang Yin, Kaipeng Zhang, Yongtao Ge  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21686v1.pdf)  
  Keywords: world model, interactive, dit, evaluation, style, trajectory, benchmark, video generation, image-to-video  
- **[Exploring the Role of Synthetic Data Augmentation in Controllable Human-Centric Video Generation](https://arxiv.org/abs/2604.21291v1)**  
  Authors: Yuanchen Fei, Yude Zou, Zejian Kang, Ming Li, Jiaying Zhou, Xiangru Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21291v1.pdf)  
  Keywords: controllable, efficient, video synthesis, identity, video generation, temporal consistency  
- **[AttentionBender: Manipulating Cross-Attention in Video Diffusion Transformers as a Creative Probe](https://arxiv.org/abs/2604.20936v1)**  
  Authors: Adam Cole, Mick Grierson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.20936v1.pdf)  
  Keywords: creative, dit, video diffusion, diffusion transformer, video generation, style  

### Physical Understanding

*Showing the latest 50 out of 144 papers*

- **[Video Generation with Predictive Latents](https://arxiv.org/abs/2605.02134v1)**  
  Authors: Yian Zhao, Feng Wang, Qiushan Guo, Chang Liu, Xiangyang Ji, Jian Zhang, Jie Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.02134v1.pdf)  
  Keywords: world model, latent video, video generation, dynamics  
- **[TMD-Bench: A Multi-Level Evaluation Paradigm for Music-Dance Co-Generation](https://arxiv.org/abs/2605.01809v1)**  
  Authors: Xiaoda Yang, Majun Zhang, Changhao Pan, Nick Huang, Yang Yuguang, Fan Zhuo, Pengfei Zhou, Jin Zhou, Sizhe Shan, Shan Yang, Miles Yang, Yang You, Zhou Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.01809v1.pdf)  
  Keywords: interactive, creative, video synthesis, evaluation, physical, benchmark  
- **[Motion-Aware Caching for Efficient Autoregressive Video Generation](https://arxiv.org/abs/2605.01725v1)**  
  Authors: Jing Xu, Yuexiao Ma, Songwei Liu, Xuzhe Zheng, Shiwei Liu, Chenqian Yan, Xiawu Zheng, Rongrong Ji, Fei Chao, Xing Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.01725v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ywlq/MotionCache?style=social)](https://github.com/ywlq/MotionCache)  
  Keywords: long video, autoregressive, efficient, denoising, video synthesis, dynamics, video generation  
- **[Physically Native World Models: A Hamiltonian Perspective on Generative World Modeling](https://arxiv.org/abs/2605.00412v1)**  
  Authors: Sen Cui, Jingheng Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.00412v1.pdf)  
  Keywords: controllable, world model, dynamics, robotics, physical, trajectory, autonomous driving  
- **[Lucid-XR: An Extended-Reality Data Engine for Robotic Manipulation](https://arxiv.org/abs/2605.00244v1)**  
  Authors: Yajvan Ravan, Adam Rashid, Alan Yu, Kai McClennen, Gio Huh, Kevin Yang, Zhutian Yang, Qinxi Yu, Xiaolong Wang, Phillip Isola, Ge Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.00244v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lucidxr.github.io)  
  Keywords: simulation, evaluation, multi-modal, physics, video generation  
- **[PhyCo: Learning Controllable Physical Priors for Generative Motion](https://arxiv.org/abs/2604.28169v1)**  
  Authors: Sriram Narayanan, Ziyu Jiang, Srinivasa Narasimhan, Manmohan Chandraker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.28169v1.pdf)  
  Keywords: controllable, simulation, physics, dit, physical, diffusion model, benchmark, video generation, video diffusion  
- **[ABC: Any-Subset Autoregression via Non-Markovian Diffusion Bridges in Continuous Time and Space](https://arxiv.org/abs/2604.27443v1)**  
  Authors: Gabe Guo, Thanawat Sornwanee, Lutong Hao, Elon Litman, Stefano Ermon, Jose Blanchet  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.27443v1.pdf)  
  Keywords: autoregressive, denoising, dit, dynamics, physical, diffusion model, video generation  
- **[DepthPilot: From Controllability to Interpretability in Colonoscopy Video Generation](https://arxiv.org/abs/2604.26232v1)**  
  Authors: Junhu Fu, Ke Chen, Weidong Guo, Shuyu Liang, Jie Xu, Chen Ma, Kehao Wang, Shengli Lin, Zeju Li, Yuanyuan Wang, Yi Guo, Shuo Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.26232v1.pdf)  
  Keywords: controllable, world model, efficient, denoising, evaluation, medical, dynamics, physical, benchmark, video generation  
- **[PhysLayer: Language-Guided Layered Animation with Depth-Aware Physics](https://arxiv.org/abs/2604.23574v1)**  
  Authors: Tianyidan Xie, Zhentao Huang, Mingjie Wang, Xin Huang, Jun Zhou, Minglun Gong, Zili Yi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.23574v1.pdf)  
  Keywords: controllable, simulation, video synthesis, evaluation, dynamics, physical, image animation, physics, video generation, image-to-video  
- **[Agentic World Modeling: Foundations, Capabilities, Laws, and Beyond](https://arxiv.org/abs/2604.22748v1)**  
  Authors: Meng Chu, Xuan Billy Zhang, Kevin Qinghong Lin, Lingdong Kong, Jize Zhang, Teng Tu, Weijian Ma, Ziqi Huang, Senqiao Yang, Wei Huang, Yeying Jin, Zhefan Rao, Jinhui Ye, Xinyu Lin, Xichen Zhang, Qisheng Hu, Shuai Yang, Leyang Shen, Wei Chow, Yifei Dong, Fengyi Wu, Quanyu Long, Bin Xia, Shaozuo Yu, Mingkang Zhu, Wenhu Zhang, Jiehui Huang, Haokun Gui, Haoxuan Che, Long Chen, Qifeng Chen, Wenxuan Zhang, Wenya Wang, Xiaojuan Qi, Yang Deng, Yanwei Li, Mike Zheng Shou, Zhi-Qi Cheng, See-Kiong Ng, Ziwei Liu, Philip Torr, Jiaya Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.22748v1.pdf)  
  Keywords: world model, simulation, action-conditioned, dit, evaluation, dynamics, physical, video generation  

### Surveys & Benchmarks

*Showing the latest 50 out of 212 papers*

- **[TMD-Bench: A Multi-Level Evaluation Paradigm for Music-Dance Co-Generation](https://arxiv.org/abs/2605.01809v1)**  
  Authors: Xiaoda Yang, Majun Zhang, Changhao Pan, Nick Huang, Yang Yuguang, Fan Zhuo, Pengfei Zhou, Jin Zhou, Sizhe Shan, Shan Yang, Miles Yang, Yang You, Zhou Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.01809v1.pdf)  
  Keywords: interactive, creative, video synthesis, evaluation, physical, benchmark  
- **[SignVerse-2M: A Two-Million-Clip Pose-Native Universe of 25+ Sign Languages](https://arxiv.org/abs/2605.01720v1)**  
  Authors: Sen Fang, Hongbin Zhong, Yanxin Zhang, Dimitris N. Metaxas  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.01720v1.pdf)  
  Keywords: pose-guided, dit, evaluation, video generation, style  
- **[Omni-Fake: Benchmarking Unified Multimodal Social Media Deepfake Detection](https://arxiv.org/abs/2605.01638v1)**  
  Authors: Tianxiao Li, Zhenglin Huang, Haiquan Wen, Yiwei He, Xinze Li, Bingyu Zhu, Wuhui Duan, Congang Chen, Zeyu Fu, Yi Dong, Baoyuan Wu, Jason Li, Guangliang Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.01638v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://tianxiao1201.github.io/omni-fake-project-page)  
  Keywords: benchmark, dit, talking head  
- **[Quaternion Nonlinear Transform-Induced Nuclear Norm for Low-Rank Tensor Completion](https://arxiv.org/abs/2605.01467v1)**  
  Authors: Biswarup Karmakar, Ratikanta Behera  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.01467v1.pdf)  
  Keywords: efficient, benchmark, video inpainting  
- **[Valley3: Scaling Omni Foundation Models for E-commerce](https://arxiv.org/abs/2605.01278v1)**  
  Authors: Zeyu Chen, Guanghao Zhou, Qixiang Yin, Ziwang Zhao, Huanjin Yao, Pengjiu Xia, Min Yang, Cen Chen, Minghui Qiu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.01278v1.pdf)  
  Keywords: controllable, benchmark  
- **[Lucid-XR: An Extended-Reality Data Engine for Robotic Manipulation](https://arxiv.org/abs/2605.00244v1)**  
  Authors: Yajvan Ravan, Adam Rashid, Alan Yu, Kai McClennen, Gio Huh, Kevin Yang, Zhutian Yang, Qinxi Yu, Xiaolong Wang, Phillip Isola, Ge Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.00244v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lucidxr.github.io)  
  Keywords: simulation, evaluation, multi-modal, physics, video generation  
- **[PhyCo: Learning Controllable Physical Priors for Generative Motion](https://arxiv.org/abs/2604.28169v1)**  
  Authors: Sriram Narayanan, Ziyu Jiang, Srinivasa Narasimhan, Manmohan Chandraker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.28169v1.pdf)  
  Keywords: controllable, simulation, physics, dit, physical, diffusion model, benchmark, video generation, video diffusion  
- **[AesRM: Improving Video Aesthetics with Expert-Level Feedback](https://arxiv.org/abs/2604.28078v1)**  
  Authors: Yujin Han, Yujie Wei, Yefei He, Xinyu Liu, Tianle Li, Zichao Yu, Andi Han, Shiwei Zhang, Tingyu Weng, Difan Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.28078v1.pdf)  
  Keywords: efficient, concept, dit, evaluation, benchmark, video generation, film  
- **[World Model for Robot Learning: A Comprehensive Survey](https://arxiv.org/abs/2605.00080v1)**  
  Authors: Bohan Hou, Gen Li, Jindou Jia, Tuo An, Xinying Guo, Sicong Leng, Haoran Geng, Yanjie Ze, Tatsuya Harada, Philip Torr, Oier Mees, Marc Pollefeys, Zhuang Liu, Jiajun Wu, Pieter Abbeel, Jitendra Malik, Yilun Du, Jianfei Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.00080v1.pdf)  
  Keywords: controllable, world model, simulation, autonomous driving, evaluation, architecture, survey, benchmark, video generation  
- **[Generate Your Talking Avatar from Video Reference](https://arxiv.org/abs/2604.27918v1)**  
  Authors: Zujin Guo, Zhenhui Ye, Yi Ren, Yuanming Li, Ce Chen, Zhibin Hong, Chen Change Loy  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.27918v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://www.heygen.com/research)  
  Keywords: dit, avatar, identity, benchmark, image-to-video  

### Text-to-Video Generation

*Showing the latest 50 out of 58 papers*

- **[TrajShield: Trajectory-Level Safety Mediation for Defending Text-to-Video Models Against Jailbreak Attacks](https://arxiv.org/abs/2605.01761v1)**  
  Authors: Quanchen Zou, Nizhang Li, Wenxin Zhang, Jiaye Lin, Yangchen Zeng, Xiangzheng Zhang, Zonghao Ying  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.01761v1.pdf)  
  Keywords: trajectory, text-to-video, t2v  
- **[HuM-Eval: A Coarse-to-Fine Framework for Human-Centric Video Evaluation](https://arxiv.org/abs/2604.25361v1)**  
  Authors: Bingzi Zhang, Kaisi Guan, Ruihua Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.25361v1.pdf)  
  Keywords: evaluation, text-to-video, human motion, benchmark, video generation  
- **[World-R1: Reinforcing 3D Constraints for Text-to-Video Generation](https://arxiv.org/abs/2604.24764v1)**  
  Authors: Weijie Wang, Xiaoxuan He, Youping Gu, Yifan Yang, Zeyu Zhang, Yefei He, Yanbo Ding, Xirui Hu, Donny Y. Chen, Zhiyuan He, Yuqing Yang, Bohan Zhuang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.24764v1.pdf)  
  Keywords: simulation, dit, evaluation, architecture, text-to-video, video generation  
- **[BRITE: A Benchmark for Reliable and Interpretable T2V Evaluation on Implausible Scenarios](https://arxiv.org/abs/2605.00873v1)**  
  Authors: Advait Tilak, Jiwon Choi, Nazifa Mouli, Wei Le  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.00873v1.pdf)  
  Keywords: evaluation, benchmark, text-to-video, t2v  
- **[KD-CVG: A Knowledge-Driven Approach for Creative Video Generation](https://arxiv.org/abs/2604.21362v1)**  
  Authors: Linkai Liu, Wei Feng, Xi Zhao, Shen Zhang, Xingye Chen, Zheng Zhang, Jingjing Lv, Junjie Shen, Ching Law, Yuchen Zhou, Zipeng Guo, Chao Gou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21362v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kdcvg.github.io/KDCVG)  
  Keywords: creative, advertising, video generation, text-to-video, t2v  
- **[Sparse Forcing: Native Trainable Sparse Attention for Real-time Autoregressive Diffusion Video Generation](https://arxiv.org/abs/2604.21221v1)**  
  Authors: Boxun Xu, Yuming Du, Zichang Liu, Siyu Yang, Ziyang Jiang, Siqi Yan, Rajasi Saha, Albert Pumarola, Wenchen Wang, Peng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21221v1.pdf)  
  Keywords: autoregressive, efficient, text-to-video, diffusion model, video generation, video diffusion  
- **[CityRAG: Stepping Into a City via Spatially-Grounded Video Generation](https://arxiv.org/abs/2604.19741v1)**  
  Authors: Gene Chou, Charles Herrmann, Kyle Genova, Boyang Deng, Songyou Peng, Bharath Hariharan, Jason Y. Zhang, Noah Snavely, Philipp Henzler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19741v1.pdf)  
  Keywords: i2v, simulation, dit, autonomous driving, video generation, robotics, physical, t2v  
- **[TS-Attn: Temporal-wise Separable Attention for Multi-Event Video Generation](https://arxiv.org/abs/2604.19473v1)**  
  Authors: Hongyu Zhang, Yufan Deng, Zilin Pan, Peng-Tao Jiang, Bo Li, Qibin Hou, Zhiyang Dou, Zhen Dong, Daquan Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19473v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Hong-yu-Zhang/TS-Attn?style=social)](https://github.com/Hong-yu-Zhang/TS-Attn)  
  Keywords: image-to-video, dit, video generation, text-to-video, t2v, temporal consistency  
- **[FlowC2S: Flowing from Current to Succeeding Frames for Fast and Memory-Efficient Video Continuation](https://arxiv.org/abs/2604.17625v1)**  
  Authors: Hovhannes Margaryan, Quentin Bammey, Christian Sandor  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.17625v1.pdf)  
  Keywords: evaluation, text-to-video, efficient  
- **[Generative Refinement Networks for Visual Synthesis](https://arxiv.org/abs/2604.13030v1)**  
  Authors: Jian Han, Jinlai Liu, Jiahuan Wang, Bingyue Peng, Zehuan Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.13030v1.pdf)  
  Keywords: autoregressive, efficient, dit, text-to-video, diffusion model, benchmark, video generation  

### Video Editing

- **[Latent Inter-Frame Pruning: A Training-Free Method Bridging Traditional Video Compression and Modern Diffusion Transformers for Efficient Generation](https://arxiv.org/abs/2604.23858v1)**  
  Authors: Dennis Menn, Chih-Hsien Chou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.23858v1.pdf)  
  Keywords: efficient, dit, video editing, diffusion transformer, diffusion model, video generation  
- **[LIVE: Leveraging Image Manipulation Priors for Instruction-based Video Editing](https://arxiv.org/abs/2604.17021v1)**  
  Authors: Weicheng Wang, Zhicheng Zhang, Zhongqi Zhang, Juncheng Zhou, Yongjie Zhu, Wenyu Qin, Meng Wang, Pengfei Wan, Jufeng Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.17021v1.pdf)  
  Keywords: dit, evaluation, video editing, benchmark, video generation  
- **[UniEditBench: A Unified and Cost-Effective Benchmark for Image and Video Editing via Distilled MLLMs](https://arxiv.org/abs/2604.15871v1)**  
  Authors: Lifan Jiang, Tianrun Wu, Yuhang Pei, Chenyang Wang, Boxi Wu, Deng Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.15871v1.pdf) | [![GitHub](https://img.shields.io/github/stars/wesar1/UniEditBench?style=social)](https://github.com/wesar1/UniEditBench)  
  Keywords: evaluation, benchmark, dit, video editing  
- **[Empowering Video Translation using Multimodal Large Language Models](https://arxiv.org/abs/2604.11283v1)**  
  Authors: Bingzheng QU, Kehai Chen, Xuefeng Bai, Min Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.11283v1.pdf)  
  Keywords: controllable, dit, survey, identity, video translation  
- **[Rein3D: Reinforced 3D Indoor Scene Generation with Panoramic Video Diffusion Models](https://arxiv.org/abs/2604.10578v2)**  
  Authors: Dehui Wang, Congsheng Xu, Rong Wei, Yue Shi, Shoufa Chen, Dingxiang Luo, Tianshuo Yang, Xiaokang Yang, Wei Sui, Yusen Qin, Rui Tang, Yao Mu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.10578v2.pdf)  
  Keywords: video-to-video, diffusion model, super-resolution, video diffusion  
- **[InsEdit: Towards Instruction-based Visual Editing via Data-Efficient Video Diffusion Models Adaptation](https://arxiv.org/abs/2604.08646v1)**  
  Authors: Zhefan Rao, Bin Zou, Haoxuan Che, Xuanhua He, Chong Hou Choi, Yanheng Li, Rui Liu, Qifeng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08646v1.pdf)  
  Keywords: efficient, dit, video editing, architecture, diffusion model, benchmark, video generation, video diffusion  
- **[Lighting-grounded Video Generation with Renderer-based Agent Reasoning](https://arxiv.org/abs/2604.07966v1)**  
  Authors: Ziqi Cai, Taoyu Yang, Zheng Chang, Si Li, Han Jiang, Shuchen Weng, Boxin Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07966v1.pdf)  
  Keywords: controllable, video-to-video, dit, video synthesis, temporal consistency, video diffusion, layout, film, diffusion model, trajectory, video generation, image-to-video  
- **[ImVideoEdit: Image-learning Video Editing via 2D Spatial Difference Attention Blocks](https://arxiv.org/abs/2604.07958v2)**  
  Authors: Jiayang Xu, Fan Zhuo, Majun Zhang, Changhao Pan, Zehan Wang, Siyu Chen, Xiaoda Yang, Tao Jin, Zhou Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07958v2.pdf)  
  Keywords: efficient, dit, video editing, dynamics, temporal consistency  
- **[Evolution of Video Generative Foundations](https://arxiv.org/abs/2604.06339v1)**  
  Authors: Teng Hu, Jiangning Zhang, Hongrui Huang, Ran Yi, Zihan Su, Jieyu Weng, Zhucun Xue, Lizhuang Ma, Ming-Hsuan Yang, Dacheng Tao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06339v1.pdf) | [![GitHub](https://img.shields.io/github/stars/sjtuplayer/Awesome-Video-Foundations?style=social)](https://github.com/sjtuplayer/Awesome-Video-Foundations)  
  Keywords: world model, simulation, dit, autonomous driving, video editing, dynamics, survey, diffusion model, education, video generation  
- **[UENR-600K: A Large-Scale Physically Grounded Dataset for Nighttime Video Deraining](https://arxiv.org/abs/2604.04402v1)**  
  Authors: Pei Yang, Hai Ci, Beibei Lin, Yiren Song, Mike Zheng Shou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04402v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://showlab.github.io/UENR-600K)  
  Keywords: video-to-video, benchmark, video generation, physical  

### Video Inpainting & Completion

- **[Quaternion Nonlinear Transform-Induced Nuclear Norm for Low-Rank Tensor Completion](https://arxiv.org/abs/2605.01467v1)**  
  Authors: Biswarup Karmakar, Ratikanta Behera  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.01467v1.pdf)  
  Keywords: efficient, benchmark, video inpainting  
- **[LMGenDrive: Bridging Multimodal Understanding and Generative World Modeling for End-to-End Driving](https://arxiv.org/abs/2604.08719v1)**  
  Authors: Hao Shao, Letian Wang, Yang Zhou, Yuxuan Hu, Zhuofan Zong, Steven L. Waslander, Wei Zhan, Hongsheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08719v1.pdf)  
  Keywords: autoregressive, world model, autonomous driving, video prediction, benchmark, video generation  
- **[Novel View Synthesis as Video Completion](https://arxiv.org/abs/2604.08500v1)**  
  Authors: Qi Wu, Khiem Vuong, Minsik Jeon, Srinivasa Narasimhan, Deva Ramanan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08500v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://frame-crafter.github.io)  
  Keywords: video completion, novel view, diffusion model, benchmark, video diffusion  
- **[SEM-ROVER: Semantic Voxel-Guided Diffusion for Large-Scale Driving Scene Generation](https://arxiv.org/abs/2604.06113v1)**  
  Authors: Hiba Dahmani, Nathan Piasco, Moussab Bennehar, Luis Roldão, Dzmitry Tsishkou, Laurent Caraffa, Jean-Philippe Tarel, Roland Brémond  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06113v1.pdf)  
  Keywords: outpainting, diffusion model, dit  
- **[ChopGrad: Pixel-Wise Losses for Latent Video Diffusion via Truncated Backpropagation](https://arxiv.org/abs/2603.17812v2)**  
  Authors: Dmitriy Rivkin, Parker Ewen, Lili Gao, Julian Ost, Stefanie Walz, Rasika Kangutkar, Mario Bijelic, Felix Heide  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17812v2.pdf)  
  Keywords: video enhancement, efficient, latent video, video inpainting, dit, super-resolution, diffusion model, video generation, video diffusion  
- **[ConfCtrl: Enabling Precise Camera Control in Video Diffusion via Confidence-Aware Interpolation](https://arxiv.org/abs/2603.09819v1)**  
  Authors: Liudi Yang, George Eskandar, Fengyi Shen, Mohammad Altillawi, Yang Bai, Chi Zhang, Ziyuan Liu, Abhinav Valada  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09819v1.pdf)  
  Keywords: dit, camera control, novel view, diffusion model, video interpolation, video diffusion  
- **[Pinterest Canvas: Large-Scale Image Generation at Pinterest](https://arxiv.org/abs/2603.06453v1)**  
  Authors: Yu Wang, Eric Tzeng, Raymond Shiau, Jie Yang, Dmitry Kislyuk, Charles Rosenberg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06453v1.pdf)  
  Keywords: dit, outpainting, diffusion model, video generation, image-to-video  

### Video Super-Resolution & Enhancement

*Showing the latest 50 out of 63 papers*

- **[Motion-Aware Caching for Efficient Autoregressive Video Generation](https://arxiv.org/abs/2605.01725v1)**  
  Authors: Jing Xu, Yuexiao Ma, Songwei Liu, Xuzhe Zheng, Shiwei Liu, Chenqian Yan, Xiawu Zheng, Rongrong Ji, Fei Chao, Xing Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.01725v1.pdf) | [![GitHub](https://img.shields.io/github/stars/ywlq/MotionCache?style=social)](https://github.com/ywlq/MotionCache)  
  Keywords: long video, autoregressive, efficient, denoising, video synthesis, dynamics, video generation  
- **[ABC: Any-Subset Autoregression via Non-Markovian Diffusion Bridges in Continuous Time and Space](https://arxiv.org/abs/2604.27443v1)**  
  Authors: Gabe Guo, Thanawat Sornwanee, Lutong Hao, Elon Litman, Stefano Ermon, Jose Blanchet  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.27443v1.pdf)  
  Keywords: autoregressive, denoising, dit, dynamics, physical, diffusion model, video generation  
- **[Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising](https://arxiv.org/abs/2604.26694v1)**  
  Authors: Jun Guo, Qiwei Li, Peiyan Li, Zilong Chen, Nan Sun, Yifei Su, Heyun Wang, Yuan Zhang, Xinghang Li, Huaping Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.26694v1.pdf)  
  Keywords: world model, efficient, denoising, diffusion transformer, diffusion model, benchmark, video diffusion  
- **[MetaSR: Content-Adaptive Metadata Orchestration for Generative Super-Resolution](https://arxiv.org/abs/2604.26244v1)**  
  Authors: Jiaqi Guo, Mingzhen Li, Haohong Wang, Aggelos K. Katsaggelos  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.26244v1.pdf)  
  Keywords: efficient, dit, diffusion transformer, distillation, super-resolution  
- **[DepthPilot: From Controllability to Interpretability in Colonoscopy Video Generation](https://arxiv.org/abs/2604.26232v1)**  
  Authors: Junhu Fu, Ke Chen, Weidong Guo, Shuyu Liang, Jie Xu, Chen Ma, Kehao Wang, Shengli Lin, Zeju Li, Yuanyuan Wang, Yi Guo, Shuo Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.26232v1.pdf)  
  Keywords: controllable, world model, efficient, denoising, evaluation, medical, dynamics, physical, benchmark, video generation  
- **[Talker-T2AV: Joint Talking Audio-Video Generation with Autoregressive Diffusion Modeling](https://arxiv.org/abs/2604.23586v1)**  
  Authors: Zhen Ye, Xu Tan, Aoxiong Yin, Hongzhan Lin, Guangyan Zhang, Peiwen Sun, Yiming Li, Chi-Min Chan, Wei Ye, Shikun Zhang, Wei Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.23586v1.pdf)  
  Keywords: autoregressive, denoising, diffusion transformer, diffusion model, talking head, benchmark, video generation  
- **[BurstGP: Enhancing Raw Burst Image Super Resolution with Generative Priors](https://arxiv.org/abs/2604.23508v1)**  
  Authors: Dong Huo, Tristan Aumentado-Armstrong, Samrudhdhi B. Rangrej, Maitreya Suin, Angela Ning Ye, Zhiming Hu, Amanpreet Walia, Amirhossein Kazerouni, Konstantinos G. Derpanis, Iqbal Mohomed, Alex Levinshtein  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.23508v1.pdf)  
  Keywords: dit, diffusion model, super-resolution  
- **[HFS-TriNet: A Three-Branch Collaborative Feature Learning Network for Prostate Cancer Classification from TRUS Videos](https://arxiv.org/abs/2604.22388v1)**  
  Authors: Xu Lu, Qianhong Peng, Qihao Zhou, Shaopeng Liu, Xiuqin Ye, Chuan Yang, Yuan Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.22388v1.pdf)  
  Keywords: sound, medical, denoising, temporal consistency  
- **[Seeing Fast and Slow: Learning the Flow of Time in Videos](https://arxiv.org/abs/2604.21931v1)**  
  Authors: Yen-Siang Wu, Rundong Luo, Jingsen Zhu, Tao Tu, Ali Farhadi, Matthew Wallingford, Yu-Chiang Frank Wang, Steve Marschner, Wei-Chiu Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21931v1.pdf)  
  Keywords: controllable, concept, dit, super-resolution, video generation, film  
- **[X-Cache: Cross-Chunk Block Caching for Few-Step Autoregressive World Models Inference](https://arxiv.org/abs/2604.20289v1)**  
  Authors: Yixiao Zeng, Jianlei Zheng, Chaoda Zheng, Shijia Chen, Mingdian Liu, Tongping Liu, Tengwei Luo, Yu Zhang, Boyang Wang, Linkun Xu, Siyuan Lu, Bo Tian, Xianming Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.20289v1.pdf)  
  Keywords: controllable, autoregressive, world model, interactive, simulation, action-conditioned, denoising, dit, autonomous driving, evaluation, acceleration, video generation, video diffusion  

### World Models & Simulation

*Showing the latest 50 out of 101 papers*

- **[Video Generation with Predictive Latents](https://arxiv.org/abs/2605.02134v1)**  
  Authors: Yian Zhao, Feng Wang, Qiushan Guo, Chang Liu, Xiangyang Ji, Jian Zhang, Jie Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.02134v1.pdf)  
  Keywords: world model, latent video, video generation, dynamics  
- **[Divide and Conquer: Decoupled Representation Alignment for Multimodal World Models](https://arxiv.org/abs/2605.01896v1)**  
  Authors: Junyuan Xiao, Dingkang Liang, Xin Zhou, Yixuan Ye, Tongtong Su, Guangmo Yi, Bin Xia, Qiang Lyu, Shurui Shi, Jun Huang, Jianlou Si, Wenming Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.01896v1.pdf)  
  Keywords: world model, multi-modal, diffusion model, video generation  
- **[TMD-Bench: A Multi-Level Evaluation Paradigm for Music-Dance Co-Generation](https://arxiv.org/abs/2605.01809v1)**  
  Authors: Xiaoda Yang, Majun Zhang, Changhao Pan, Nick Huang, Yang Yuguang, Fan Zhuo, Pengfei Zhou, Jin Zhou, Sizhe Shan, Shan Yang, Miles Yang, Yang You, Zhou Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.01809v1.pdf)  
  Keywords: interactive, creative, video synthesis, evaluation, physical, benchmark  
- **[Physically Native World Models: A Hamiltonian Perspective on Generative World Modeling](https://arxiv.org/abs/2605.00412v1)**  
  Authors: Sen Cui, Jingheng Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.00412v1.pdf)  
  Keywords: controllable, world model, dynamics, robotics, physical, trajectory, autonomous driving  
- **[Lucid-XR: An Extended-Reality Data Engine for Robotic Manipulation](https://arxiv.org/abs/2605.00244v1)**  
  Authors: Yajvan Ravan, Adam Rashid, Alan Yu, Kai McClennen, Gio Huh, Kevin Yang, Zhutian Yang, Qinxi Yu, Xiaolong Wang, Phillip Isola, Ge Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.00244v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lucidxr.github.io)  
  Keywords: simulation, evaluation, multi-modal, physics, video generation  
- **[PhyCo: Learning Controllable Physical Priors for Generative Motion](https://arxiv.org/abs/2604.28169v1)**  
  Authors: Sriram Narayanan, Ziyu Jiang, Srinivasa Narasimhan, Manmohan Chandraker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.28169v1.pdf)  
  Keywords: controllable, simulation, physics, dit, physical, diffusion model, benchmark, video generation, video diffusion  
- **[World Model for Robot Learning: A Comprehensive Survey](https://arxiv.org/abs/2605.00080v1)**  
  Authors: Bohan Hou, Gen Li, Jindou Jia, Tuo An, Xinying Guo, Sicong Leng, Haoran Geng, Yanjie Ze, Tatsuya Harada, Philip Torr, Oier Mees, Marc Pollefeys, Zhuang Liu, Jiajun Wu, Pieter Abbeel, Jitendra Malik, Yilun Du, Jianfei Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.00080v1.pdf)  
  Keywords: controllable, world model, simulation, autonomous driving, evaluation, architecture, survey, benchmark, video generation  
- **[Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising](https://arxiv.org/abs/2604.26694v1)**  
  Authors: Jun Guo, Qiwei Li, Peiyan Li, Zilong Chen, Nan Sun, Yifei Su, Heyun Wang, Yuan Zhang, Xinghang Li, Huaping Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.26694v1.pdf)  
  Keywords: world model, efficient, denoising, diffusion transformer, diffusion model, benchmark, video diffusion  
- **[DepthPilot: From Controllability to Interpretability in Colonoscopy Video Generation](https://arxiv.org/abs/2604.26232v1)**  
  Authors: Junhu Fu, Ke Chen, Weidong Guo, Shuyu Liang, Jie Xu, Chen Ma, Kehao Wang, Shengli Lin, Zeju Li, Yuanyuan Wang, Yi Guo, Shuo Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.26232v1.pdf)  
  Keywords: controllable, world model, efficient, denoising, evaluation, medical, dynamics, physical, benchmark, video generation  
- **[Benchmarking and Improving GUI Agents in High-Dynamic Environments](https://arxiv.org/abs/2604.25380v1)**  
  Authors: Enqi Liu, Liyuan Pan, Zhi Gao, Yan Yang, Chenrui Shi, Yang Liu, Jingrong Wu, Qing Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.25380v1.pdf)  
  Keywords: benchmark, action-conditioned, dit  



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
