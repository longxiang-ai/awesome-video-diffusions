# Awesome Video Diffusions [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Video Diffusion Models and Video Generation. Content is automatically updated daily.

> Last Update: 2026-05-04 02:53:52

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
- [Applications](#applications) (48 papers) - Domain-specific applications of video diffusion models
- [Architecture & Efficiency](#architecture-&-efficiency) (354 papers) - Architectural innovations (DiT, UNet), flow matching, and training/inference efficiency
- [Audio & Multi-modal](#audio-&-multi-modal) (34 papers) - Audio-driven and multi-modal conditioned video generation
- [Controllable Generation](#controllable-generation) (135 papers) - Controllable video generation with motion, camera, pose, or layout guidance
- [Human & Character Animation](#human-&-character-animation) (27 papers) - Human-centric video generation including talking heads, dance, and character animation
- [Image-to-Video Generation](#image-to-video-generation) (41 papers) - Methods for animating still images into videos
- [Long Video Generation](#long-video-generation) (111 papers) - Generating temporally consistent long-form videos beyond short clips
- [Personalization & Customization](#personalization-&-customization) (83 papers) - Personalized video generation with custom subjects, identities, or styles
- [Physical Understanding](#physical-understanding) (141 papers) - Physics-aware video generation and dynamics modeling
- [Surveys & Benchmarks](#surveys-&-benchmarks) (209 papers) - Survey papers, benchmarks, and evaluation metrics for video generation
- [Text-to-Video Generation](#text-to-video-generation) (56 papers) - Foundation models and methods for generating videos from text prompts
- [Video Editing](#video-editing) (27 papers) - Diffusion-based video editing, style transfer, and manipulation
- [Video Inpainting & Completion](#video-inpainting-&-completion) (6 papers) - Video inpainting, completion, outpainting, and temporal prediction
- [Video Super-Resolution & Enhancement](#video-super-resolution-&-enhancement) (64 papers) - Video quality improvement, upscaling, restoration, and frame interpolation
- [World Models & Simulation](#world-models-&-simulation) (100 papers) - Video generation as world simulators and interactive environment generation



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
  Keywords: dit, distillation, video diffusion, diffusion model, novel view  
- **[MultiWorld: Scalable Multi-Agent Multi-View Video World Models](https://arxiv.org/abs/2604.18564v2)**  
  Authors: Haoyu Wu, Jiwen Yu, Yingtian Zou, Xihui Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.18564v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://multi-world.github.io)  
  Keywords: dynamics, world model, action-conditioned, video generation, dit, multi-view video  
- **[ArtifactWorld: Scaling 3D Gaussian Splatting Artifact Restoration via Video Generation Models](https://arxiv.org/abs/2604.12251v1)**  
  Authors: Xinliang Wang, Yifeng Shi, Zhenyu Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.12251v1.pdf)  
  Keywords: video generation, novel view, video diffusion  
- **[Rays as Pixels: Learning A Joint Distribution of Videos and Camera Trajectories](https://arxiv.org/abs/2604.09429v3)**  
  Authors: Wonbong Jang, Shikun Liu, Soubhik Sanyal, Juan Camilo Perez, Kam Woh Ng, Sanskar Agrawal, Juan-Manuel Perez-Rua, Yiannis Douratsos, Tao Xiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.09429v3.pdf)  
  Keywords: video generation, dit, video diffusion, diffusion model, novel view, trajectory  
- **[Novel View Synthesis as Video Completion](https://arxiv.org/abs/2604.08500v1)**  
  Authors: Qi Wu, Khiem Vuong, Minsik Jeon, Srinivasa Narasimhan, Deva Ramanan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08500v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://frame-crafter.github.io)  
  Keywords: diffusion model, benchmark, video diffusion, video completion, novel view  
- **[Multi-View Video Diffusion Policy: A 3D Spatio-Temporal-Aware Video Action Model](https://arxiv.org/abs/2604.03181v1)**  
  Authors: Peiyan Li, Yixiang Chen, Yuan Xu, Jiabing Yang, Xiangnan Wu, Jun Guo, Nan Sun, Long Qian, Xinghang Li, Xin Xiao, Jing Liu, Nianfeng Liu, Tao Kong, Yan Huang, Liang Wang, Tieniu Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.03181v1.pdf)  
  Keywords: dynamics, dit, video diffusion, efficient, multi-view video  
- **[Control-DINO: Feature Space Conditioning for Controllable Image-to-Video Diffusion](https://arxiv.org/abs/2604.01761v1)**  
  Authors: Edoardo A. Dominici, Thomas Deixelberger, Konstantinos Vardis, Markus Steinberger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01761v1.pdf)  
  Keywords: novel view, simulation, architecture, dit, style, video diffusion, diffusion model, controllable, image-to-video  
- **[HVG-3D: Bridging Real and Simulation Domains for 3D-Conditional Hand-Object Interaction Video Synthesis](https://arxiv.org/abs/2604.03305v1)**  
  Authors: Mingjin Chen, Junhao Chen, Zhaoxin Fan, Yujian Lee, Zichen Dang, Lili Wang, Yawen Cui, Lap-Pui Chau, Yi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.03305v1.pdf)  
  Keywords: 3d-aware, video generation, simulation, video synthesis, architecture, dit  
- **[I3DM: Implicit 3D-aware Memory Retrieval and Injection for Consistent Video Scene Generation](https://arxiv.org/abs/2603.23413v1)**  
  Authors: Jia Li, Han Yan, Yihang Chen, Siqi Li, Xibin Song, Yifu Wang, Jianfei Cai, Tien-Tsin Wong, Pan Ji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23413v1.pdf)  
  Keywords: 3d-aware, video generation, camera control, dit, novel view  
- **[GO-Renderer: Generative Object Rendering with 3D-aware Controllable Video Diffusion Models](https://arxiv.org/abs/2603.23246v1)**  
  Authors: Zekai Gu, Shuoxuan Feng, Yansong Wang, Hanzhuo Huang, Zhongshuo Du, Chengfeng Zhao, Chengwei Ren, Peng Wang, Yuan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23246v1.pdf)  
  Keywords: 3d-aware, dit, video diffusion, diffusion model, controllable, efficient  

### Applications

- **[Physically Native World Models: A Hamiltonian Perspective on Generative World Modeling](https://arxiv.org/abs/2605.00412v1)**  
  Authors: Sen Cui, Jingheng Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.00412v1.pdf)  
  Keywords: dynamics, world model, robotics, controllable, autonomous driving, physical, trajectory  
- **[AesRM: Improving Video Aesthetics with Expert-Level Feedback](https://arxiv.org/abs/2604.28078v1)**  
  Authors: Yujin Han, Yujie Wei, Yefei He, Xinyu Liu, Tianle Li, Zichao Yu, Andi Han, Shiwei Zhang, Tingyu Weng, Difan Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.28078v1.pdf)  
  Keywords: concept, benchmark, video generation, dit, evaluation, film, efficient  
- **[World Model for Robot Learning: A Comprehensive Survey](https://arxiv.org/abs/2605.00080v1)**  
  Authors: Bohan Hou, Gen Li, Jindou Jia, Tuo An, Xinying Guo, Sicong Leng, Haoran Geng, Yanjie Ze, Tatsuya Harada, Philip Torr, Oier Mees, Marc Pollefeys, Zhuang Liu, Jiajun Wu, Pieter Abbeel, Jitendra Malik, Yilun Du, Jianfei Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.00080v1.pdf)  
  Keywords: world model, benchmark, video generation, simulation, architecture, evaluation, survey, controllable, autonomous driving  
- **[Robot Learning from Human Videos: A Survey](https://arxiv.org/abs/2604.27621v1)**  
  Authors: Junyi Ma, Erhang Zhang, Haoran Yang, Ditao Li, Chenyang Xu, Guangming Wang, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.27621v1.pdf) | [![GitHub](https://img.shields.io/github/stars/IRMVLab/awesome-robot-learning-from-human-videos?style=social)](https://github.com/IRMVLab/awesome-robot-learning-from-human-videos)  
  Keywords: video generation, dit, robotics, survey  
- **[Learning from the Unseen: Generative Data Augmentation for Geometric-Semantic Accident Anticipation](https://arxiv.org/abs/2605.00051v1)**  
  Authors: Yanchen Guan, Haicheng Liao, Chengyue Wang, Xingcheng Liu, Jiaxun Zhang, Keqiang Li, Zhenning Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.00051v1.pdf)  
  Keywords: benchmark, video synthesis, dit, evaluation, autonomous driving  
- **[DepthPilot: From Controllability to Interpretability in Colonoscopy Video Generation](https://arxiv.org/abs/2604.26232v1)**  
  Authors: Junhu Fu, Ke Chen, Weidong Guo, Shuyu Liang, Jie Xu, Chen Ma, Kehao Wang, Shengli Lin, Zeju Li, Yuanyuan Wang, Yi Guo, Shuo Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.26232v1.pdf)  
  Keywords: dynamics, world model, denoising, benchmark, video generation, medical, evaluation, controllable, efficient, physical  
- **[HFS-TriNet: A Three-Branch Collaborative Feature Learning Network for Prostate Cancer Classification from TRUS Videos](https://arxiv.org/abs/2604.22388v1)**  
  Authors: Xu Lu, Qianhong Peng, Qihao Zhou, Shaopeng Liu, Xiuqin Ye, Chuan Yang, Yuan Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.22388v1.pdf)  
  Keywords: denoising, medical, temporal consistency, sound  
- **[Seeing Fast and Slow: Learning the Flow of Time in Videos](https://arxiv.org/abs/2604.21931v1)**  
  Authors: Yen-Siang Wu, Rundong Luo, Jingsen Zhu, Tao Tu, Ali Farhadi, Matthew Wallingford, Yu-Chiang Frank Wang, Steve Marschner, Wei-Chiu Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21931v1.pdf)  
  Keywords: concept, video generation, super-resolution, dit, controllable, film  
- **[KD-CVG: A Knowledge-Driven Approach for Creative Video Generation](https://arxiv.org/abs/2604.21362v1)**  
  Authors: Linkai Liu, Wei Feng, Xi Zhao, Shen Zhang, Xingye Chen, Zheng Zhang, Jingjing Lv, Junjie Shen, Ching Law, Yuchen Zhou, Zipeng Guo, Chao Gou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21362v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kdcvg.github.io/KDCVG)  
  Keywords: video generation, advertising, creative, t2v, text-to-video  
- **[Agentic AI for Personalized Physiotherapy: A Multi-Agent Framework for Generative Video Training and Real-Time Pose Correction](https://arxiv.org/abs/2604.21154v1)**  
  Authors: Abhishek Dharmaratnakar, Srivaths Ranganathan, Anushree Sinha, Debanshu Das  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21154v1.pdf)  
  Keywords: avatar, video generation, medical, video synthesis, architecture, evaluation  

### Architecture & Efficiency

*Showing the latest 50 out of 354 papers*

- **[UniVidX: A Unified Multimodal Framework for Versatile Video Generation via Diffusion Priors](https://arxiv.org/abs/2605.00658v1)**  
  Authors: Houyuan Chen, Hong Li, Xianghao Kong, Tianrui Zhu, Shaocong Xu, Weiqing Xiao, Yuwei Guo, Chongjie Ye, Lvmin Zhang, Hao Zhao, Anyi Rao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.00658v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://houyuanchen111.github.io/UniVidX.github.io)  
  Keywords: video generation, dit, video diffusion, diffusion model  
- **[PhyCo: Learning Controllable Physical Priors for Generative Motion](https://arxiv.org/abs/2604.28169v1)**  
  Authors: Sriram Narayanan, Ziyu Jiang, Srinivasa Narasimhan, Manmohan Chandraker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.28169v1.pdf)  
  Keywords: benchmark, video generation, simulation, dit, video diffusion, diffusion model, controllable, physics, physical  
- **[AesRM: Improving Video Aesthetics with Expert-Level Feedback](https://arxiv.org/abs/2604.28078v1)**  
  Authors: Yujin Han, Yujie Wei, Yefei He, Xinyu Liu, Tianle Li, Zichao Yu, Andi Han, Shiwei Zhang, Tingyu Weng, Difan Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.28078v1.pdf)  
  Keywords: concept, benchmark, video generation, dit, evaluation, film, efficient  
- **[World Model for Robot Learning: A Comprehensive Survey](https://arxiv.org/abs/2605.00080v1)**  
  Authors: Bohan Hou, Gen Li, Jindou Jia, Tuo An, Xinying Guo, Sicong Leng, Haoran Geng, Yanjie Ze, Tatsuya Harada, Philip Torr, Oier Mees, Marc Pollefeys, Zhuang Liu, Jiajun Wu, Pieter Abbeel, Jitendra Malik, Yilun Du, Jianfei Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.00080v1.pdf)  
  Keywords: world model, benchmark, video generation, simulation, architecture, evaluation, survey, controllable, autonomous driving  
- **[Generate Your Talking Avatar from Video Reference](https://arxiv.org/abs/2604.27918v1)**  
  Authors: Zujin Guo, Zhenhui Ye, Yi Ren, Yuanming Li, Ce Chen, Zhibin Hong, Chen Change Loy  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.27918v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://www.heygen.com/research)  
  Keywords: benchmark, avatar, dit, image-to-video, identity  
- **[Robot Learning from Human Videos: A Survey](https://arxiv.org/abs/2604.27621v1)**  
  Authors: Junyi Ma, Erhang Zhang, Haoran Yang, Ditao Li, Chenyang Xu, Guangming Wang, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.27621v1.pdf) | [![GitHub](https://img.shields.io/github/stars/IRMVLab/awesome-robot-learning-from-human-videos?style=social)](https://github.com/IRMVLab/awesome-robot-learning-from-human-videos)  
  Keywords: video generation, dit, robotics, survey  
- **[ABC: Any-Subset Autoregression via Non-Markovian Diffusion Bridges in Continuous Time and Space](https://arxiv.org/abs/2604.27443v1)**  
  Authors: Gabe Guo, Thanawat Sornwanee, Lutong Hao, Elon Litman, Stefano Ermon, Jose Blanchet  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.27443v1.pdf)  
  Keywords: dynamics, denoising, video generation, autoregressive, dit, diffusion model, physical  
- **[YOSE: You Only Select Essential Tokens for Efficient DiT-based Video Object Removal](https://arxiv.org/abs/2604.27322v1)**  
  Authors: Chenyang Wu, Lina Lei, Fan Li, Chun-Le Guo, Dehong Kong, Xinran Qin, Zhixin Wang, Ming-Ming Cheng, Chongyi Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.27322v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Wucy0519/YOSE-CVPR26?style=social)](https://github.com/Wucy0519/YOSE-CVPR26)  
  Keywords: acceleration, video generation, diffusion transformer, dit, efficient  
- **[AttriBE: Quantifying Attribute Expressivity in Body Embeddings for Recognition and Identification](https://arxiv.org/abs/2604.27218v1)**  
  Authors: Basudha Pal, Siyuan Huang, Anirudh Nanduri, Zhaoyang Wang, Rama Chellappa  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.27218v1.pdf)  
  Keywords: dit  
- **[Co-Evolving Policy Distillation](https://arxiv.org/abs/2604.27083v1)**  
  Authors: Naibin Gu, Chenxu Yang, Qingyi Si, Chuanyu Qin, Dingyu Yao, Peng Fu, Zheng Lin, Weiping Wang, Nan Duan, Jiaqi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.27083v1.pdf)  
  Keywords: distillation  

### Audio & Multi-modal

- **[Lucid-XR: An Extended-Reality Data Engine for Robotic Manipulation](https://arxiv.org/abs/2605.00244v1)**  
  Authors: Yajvan Ravan, Adam Rashid, Alan Yu, Kai McClennen, Gio Huh, Kevin Yang, Zhutian Yang, Qinxi Yu, Xiaolong Wang, Phillip Isola, Ge Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.00244v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lucidxr.github.io)  
  Keywords: video generation, simulation, multi-modal, evaluation, physics  
- **[CineAGI: Character-Consistent Movie Creation through LLM-Orchestrated Multi-Modal Generation and Cross-Scene Integration](https://arxiv.org/abs/2604.23579v1)**  
  Authors: Tianyidan Xie, Zhentao Huang, Mingjie Wang, Xin Huang, Jun Zhou, Minglun Gong, Zili Yi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.23579v1.pdf)  
  Keywords: video generation, multi-modal, identity  
- **[EAD-Net: Emotion-Aware Talking Head Generation with Spatial Refinement and Temporal Coherence](https://arxiv.org/abs/2604.23325v1)**  
  Authors: Yahui Li, Yinfeng Yu, Liejun Wang, Shengjie Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.23325v1.pdf)  
  Keywords: temporal consistency, video generation, long video, dit, talking head, multi-modal  
- **[HFS-TriNet: A Three-Branch Collaborative Feature Learning Network for Prostate Cancer Classification from TRUS Videos](https://arxiv.org/abs/2604.22388v1)**  
  Authors: Xu Lu, Qianhong Peng, Qihao Zhou, Shaopeng Liu, Xiuqin Ye, Chuan Yang, Yuan Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.22388v1.pdf)  
  Keywords: denoising, medical, temporal consistency, sound  
- **[DocPrune:Efficient Document Question Answering via Background, Question, and Comprehension-aware Token Pruning](https://arxiv.org/abs/2604.22281v1)**  
  Authors: Joonmyung Choi, Sanghyeok Lee, Jongha Kim, Sehyung Kim, Dohwan Ko, Jihyung Kil, Hyunwoo J. Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.22281v1.pdf)  
  Keywords: dit, multi-modal, efficient  
- **[MMControl: Unified Multi-Modal Control for Joint Audio-Video Generation](https://arxiv.org/abs/2604.19679v2)**  
  Authors: Liyang Li, Wen Wang, Canyu Zhao, Tianjian Feng, Zhiyue Zhao, Hao Chen, Chunhua Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19679v2.pdf)  
  Keywords: video generation, diffusion transformer, dit, layout, multi-modal, video diffusion, controllable, identity  
- **[Attention-based Multi-modal Deep Learning Model of Spatio-temporal Crop Yield Prediction with Satellite, Soil and Climate Data](https://arxiv.org/abs/2604.19217v1)**  
  Authors: Gopal Krishna Shyam, Ila Chandrakar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19217v1.pdf)  
  Keywords: dit, multi-modal, architecture  
- **[OmniHuman: A Large-scale Dataset and Benchmark for Human-Centric Video Generation](https://arxiv.org/abs/2604.18326v1)**  
  Authors: Lei Zhu, Xing Cai, Yingjie Chen, Yiheng Li, Binxin Yang, Hao Liu, Jie Chen, Chen Li, Jing LYu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.18326v1.pdf)  
  Keywords: benchmark, video generation, video synthesis, multi-modal, evaluation, physical  
- **[TurboTalk: Progressive Distillation for One-Step Audio-Driven Talking Avatar Generation](https://arxiv.org/abs/2604.14580v1)**  
  Authors: Xiangyu Liu, Feng Gao, Xiaomei Zhang, Yong Zhang, Xiaoming Wei, Zhen Lei, Xiangyu Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.14580v1.pdf)  
  Keywords: denoising, avatar, distillation, video diffusion, diffusion model, audio-driven  
- **[Seedance 2.0: Advancing Video Generation for World Complexity](https://arxiv.org/abs/2604.14148v1)**  
  Authors: Team Seedance, De Chen, Liyang Chen, Xin Chen, Ying Chen, Zhuo Chen, Zhuowei Chen, Feng Cheng, Tianheng Cheng, Yufeng Cheng, Mojie Chi, Xuyan Chi, Jian Cong, Qinpeng Cui, Fei Ding, Qide Dong, Yujiao Du, Haojie Duanmu, Junliang Fan, Jiarui Fang, Jing Fang, Zetao Fang, Chengjian Feng, Yu Gao, Diandian Gu, Dong Guo, Hanzhong Guo, Qiushan Guo, Boyang Hao, Hongxiang Hao, Haoxun He, Jiaao He, Qian He, Tuyen Hoang, Heng Hu, Ruoqing Hu, Yuxiang Hu, Jiancheng Huang, Weilin Huang, Zhaoyang Huang, Zhongyi Huang, Jishuo Jin, Ming Jing, Ashley Kim, Shanshan Lao, Yichong Leng, Bingchuan Li, Gen Li, Haifeng Li, Huixia Li, Jiashi Li, Ming Li, Xiaojie Li, Xingxing Li, Yameng Li, Yiying Li, Yu Li, Yueyan Li, Chao Liang, Han Liang, Jianzhong Liang, Ying Liang, Wang Liao, J. H. Lien, Shanchuan Lin, Xi Lin, Feng Ling, Yue Ling, Fangfang Liu, Jiawei Liu, Jihao Liu, Jingtuo Liu, Shu Liu, Sichao Liu, Wei Liu, Xue Liu, Zuxi Liu, Ruijie Lu, Lecheng Lyu, Jingting Ma, Tianxiang Ma, Xiaonan Nie, Jingzhe Ning, Junjie Pan, Xitong Pan, Ronggui Peng, Xueqiong Qu, Yuxi Ren, Yuchen Shen, Guang Shi, Lei Shi, Yinglong Song, Fan Sun, Li Sun, Renfei Sun, Wenjing Tang, Boyang Tao, Zirui Tao, Dongliang Wang, Feng Wang, Hulin Wang, Ke Wang, Qingyi Wang, Rui Wang, Shuai Wang, Shulei Wang, Weichen Wang, Xuanda Wang, Yanhui Wang, Yue Wang, Yuping Wang, Yuxuan Wang, Zijie Wang, Ziyu Wang, Guoqiang Wei, Meng Wei, Di Wu, Guohong Wu, Hanjie Wu, Huachao Wu, Jian Wu, Jie Wu, Ruolan Wu, Shaojin Wu, Xiaohu Wu, Xinglong Wu, Yonghui Wu, Ruiqi Xia, Xin Xia, Xuefeng Xiao, Shuang Xu, Bangbang Yang, Jiaqi Yang, Runkai Yang, Tao Yang, Yihang Yang, Zhixian Yang, Ziyan Yang, Fulong Ye, Bingqian Yi, Xing Yin, Yongbin You, Linxiao Yuan, Weihong Zeng, Xuejiao Zeng, Yan Zeng, Siyu Zhai, Zhonghua Zhai, Bowen Zhang, Chenlin Zhang, Heng Zhang, Jun Zhang, Manlin Zhang, Peiyuan Zhang, Shuo Zhang, Xiaohe Zhang, Xiaoying Zhang, Xinyan Zhang, Xinyi Zhang, Yichi Zhang, Zixiang Zhang, Haiyu Zhao, Huating Zhao, Liming Zhao, Yian Zhao, Guangcong Zheng, Jianbin Zheng, Xiaozheng Zheng, Zerong Zheng, Kuan Zhu, Feilong Zuo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.14148v1.pdf)  
  Keywords: video generation, creative, architecture, dit, multi-modal, evaluation, efficient  

### Controllable Generation

*Showing the latest 50 out of 135 papers*

- **[Physically Native World Models: A Hamiltonian Perspective on Generative World Modeling](https://arxiv.org/abs/2605.00412v1)**  
  Authors: Sen Cui, Jingheng Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.00412v1.pdf)  
  Keywords: dynamics, world model, robotics, controllable, autonomous driving, physical, trajectory  
- **[PhyCo: Learning Controllable Physical Priors for Generative Motion](https://arxiv.org/abs/2604.28169v1)**  
  Authors: Sriram Narayanan, Ziyu Jiang, Srinivasa Narasimhan, Manmohan Chandraker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.28169v1.pdf)  
  Keywords: benchmark, video generation, simulation, dit, video diffusion, diffusion model, controllable, physics, physical  
- **[World Model for Robot Learning: A Comprehensive Survey](https://arxiv.org/abs/2605.00080v1)**  
  Authors: Bohan Hou, Gen Li, Jindou Jia, Tuo An, Xinying Guo, Sicong Leng, Haoran Geng, Yanjie Ze, Tatsuya Harada, Philip Torr, Oier Mees, Marc Pollefeys, Zhuang Liu, Jiajun Wu, Pieter Abbeel, Jitendra Malik, Yilun Du, Jianfei Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.00080v1.pdf)  
  Keywords: world model, benchmark, video generation, simulation, architecture, evaluation, survey, controllable, autonomous driving  
- **[DepthPilot: From Controllability to Interpretability in Colonoscopy Video Generation](https://arxiv.org/abs/2604.26232v1)**  
  Authors: Junhu Fu, Ke Chen, Weidong Guo, Shuyu Liang, Jie Xu, Chen Ma, Kehao Wang, Shengli Lin, Zeju Li, Yuanyuan Wang, Yi Guo, Shuo Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.26232v1.pdf)  
  Keywords: dynamics, world model, denoising, benchmark, video generation, medical, evaluation, controllable, efficient, physical  
- **[PhysLayer: Language-Guided Layered Animation with Depth-Aware Physics](https://arxiv.org/abs/2604.23574v1)**  
  Authors: Tianyidan Xie, Zhentao Huang, Mingjie Wang, Xin Huang, Jun Zhou, Minglun Gong, Zili Yi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.23574v1.pdf)  
  Keywords: dynamics, video generation, simulation, video synthesis, image animation, evaluation, controllable, physics, image-to-video, physical  
- **[Seeing Fast and Slow: Learning the Flow of Time in Videos](https://arxiv.org/abs/2604.21931v1)**  
  Authors: Yen-Siang Wu, Rundong Luo, Jingsen Zhu, Tao Tu, Ali Farhadi, Matthew Wallingford, Yu-Chiang Frank Wang, Steve Marschner, Wei-Chiu Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21931v1.pdf)  
  Keywords: concept, video generation, super-resolution, dit, controllable, film  
- **[WorldMark: A Unified Benchmark Suite for Interactive Video World Models](https://arxiv.org/abs/2604.21686v1)**  
  Authors: Xiaojie Xu, Zhengyuan Lin, Kang He, Yukang Feng, Xiaofeng Mao, Yuanyang Yin, Kaipeng Zhang, Yongtao Ge  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21686v1.pdf)  
  Keywords: world model, interactive, benchmark, video generation, dit, evaluation, style, image-to-video, trajectory  
- **[Exploring the Role of Synthetic Data Augmentation in Controllable Human-Centric Video Generation](https://arxiv.org/abs/2604.21291v1)**  
  Authors: Yuanchen Fei, Yude Zou, Zejian Kang, Ming Li, Jiaying Zhou, Xiangru Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21291v1.pdf)  
  Keywords: temporal consistency, video generation, video synthesis, controllable, efficient, identity  
- **[X-Cache: Cross-Chunk Block Caching for Few-Step Autoregressive World Models Inference](https://arxiv.org/abs/2604.20289v1)**  
  Authors: Yixiao Zeng, Jianlei Zheng, Chaoda Zheng, Shijia Chen, Mingdian Liu, Tongping Liu, Tengwei Luo, Yu Zhang, Boyang Wang, Linkun Xu, Siyuan Lu, Bo Tian, Xianming Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.20289v1.pdf)  
  Keywords: world model, denoising, interactive, action-conditioned, video generation, simulation, acceleration, autoregressive, dit, evaluation, video diffusion, controllable, autonomous driving  
- **[ReImagine: Rethinking Controllable High-Quality Human Video Generation via Image-First Synthesis](https://arxiv.org/abs/2604.19720v1)**  
  Authors: Zhengwentai Sun, Keru Zheng, Chenghong Li, Hongjie Liao, Xihe Yang, Heyuan Li, Yihao Zhi, Shuliang Ning, Shuguang Cui, Xiaoguang Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19720v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Taited/ReImagine?style=social)](https://github.com/Taited/ReImagine)  
  Keywords: temporal consistency, video generation, video synthesis, video diffusion, diffusion model, controllable  

### Human & Character Animation

- **[Generate Your Talking Avatar from Video Reference](https://arxiv.org/abs/2604.27918v1)**  
  Authors: Zujin Guo, Zhenhui Ye, Yi Ren, Yuanming Li, Ce Chen, Zhibin Hong, Chen Change Loy  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.27918v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://www.heygen.com/research)  
  Keywords: benchmark, avatar, dit, image-to-video, identity  
- **[HuM-Eval: A Coarse-to-Fine Framework for Human-Centric Video Evaluation](https://arxiv.org/abs/2604.25361v1)**  
  Authors: Bingzi Zhang, Kaisi Guan, Ruihua Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.25361v1.pdf)  
  Keywords: text-to-video, benchmark, video generation, evaluation, human motion  
- **[Talker-T2AV: Joint Talking Audio-Video Generation with Autoregressive Diffusion Modeling](https://arxiv.org/abs/2604.23586v1)**  
  Authors: Zhen Ye, Xu Tan, Aoxiong Yin, Hongzhan Lin, Guangyan Zhang, Peiwen Sun, Yiming Li, Chi-Min Chan, Wei Ye, Shikun Zhang, Wei Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.23586v1.pdf)  
  Keywords: denoising, benchmark, video generation, diffusion transformer, autoregressive, talking head, diffusion model  
- **[EAD-Net: Emotion-Aware Talking Head Generation with Spatial Refinement and Temporal Coherence](https://arxiv.org/abs/2604.23325v1)**  
  Authors: Yahui Li, Yinfeng Yu, Liejun Wang, Shengjie Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.23325v1.pdf)  
  Keywords: temporal consistency, video generation, long video, dit, talking head, multi-modal  
- **[Agentic AI for Personalized Physiotherapy: A Multi-Agent Framework for Generative Video Training and Real-Time Pose Correction](https://arxiv.org/abs/2604.21154v1)**  
  Authors: Abhishek Dharmaratnakar, Srivaths Ranganathan, Anushree Sinha, Debanshu Das  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21154v1.pdf)  
  Keywords: avatar, video generation, medical, video synthesis, architecture, evaluation  
- **[HumanScore: Benchmarking Human Motions in Generated Videos](https://arxiv.org/abs/2604.20157v1)**  
  Authors: Yusu Fang, Tiange Xiang, Tian Tan, Narayan Schuetz, Scott Delp, Li Fei-Fei, Ehsan Adeli  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.20157v1.pdf)  
  Keywords: dynamics, benchmark, video generation, architecture, physical, human motion  
- **[Prompt-to-Gesture: Measuring the Capabilities of Image-to-Video Deictic Gesture Generation](https://arxiv.org/abs/2604.14953v1)**  
  Authors: Hassan Ali, Doreen Jirak, Luca Müller, Stefan Wermter  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.14953v1.pdf)  
  Keywords: video generation, dit, gesture, image-to-video  
- **[TurboTalk: Progressive Distillation for One-Step Audio-Driven Talking Avatar Generation](https://arxiv.org/abs/2604.14580v1)**  
  Authors: Xiangyu Liu, Feng Gao, Xiaomei Zhang, Yong Zhang, Xiaoming Wei, Zhen Lei, Xiangyu Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.14580v1.pdf)  
  Keywords: denoising, avatar, distillation, video diffusion, diffusion model, audio-driven  
- **[Beyond Monologue: Interactive Talking-Listening Avatar Generation with Conversational Audio Context-Aware Kernels](https://arxiv.org/abs/2604.10367v1)**  
  Authors: Yuzhe Weng, Haotian Wang, Xinyi Yu, Xiaoyan Wu, Haoran Xu, Shan He, Jun Du  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.10367v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://warmcongee.github.io/beyond-monologue)  
  Keywords: dynamics, interactive, avatar, video generation, audio-driven, physical  
- **[HumANDiff: Articulated Noise Diffusion for Motion-Consistent Human Video Generation](https://arxiv.org/abs/2604.05961v1)**  
  Authors: Tao Hu, Varun Jampani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.05961v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://taohuumd.github.io/projects/HumANDiff)  
  Keywords: dynamics, video generation, human motion, video synthesis, architecture, dit, motion control, style, video diffusion, diffusion model, controllable, physics, image-to-video, physical  

### Image-to-Video Generation

- **[Generate Your Talking Avatar from Video Reference](https://arxiv.org/abs/2604.27918v1)**  
  Authors: Zujin Guo, Zhenhui Ye, Yi Ren, Yuanming Li, Ce Chen, Zhibin Hong, Chen Change Loy  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.27918v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://www.heygen.com/research)  
  Keywords: benchmark, avatar, dit, image-to-video, identity  
- **[PhysLayer: Language-Guided Layered Animation with Depth-Aware Physics](https://arxiv.org/abs/2604.23574v1)**  
  Authors: Tianyidan Xie, Zhentao Huang, Mingjie Wang, Xin Huang, Jun Zhou, Minglun Gong, Zili Yi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.23574v1.pdf)  
  Keywords: dynamics, video generation, simulation, video synthesis, image animation, evaluation, controllable, physics, image-to-video, physical  
- **[WorldMark: A Unified Benchmark Suite for Interactive Video World Models](https://arxiv.org/abs/2604.21686v1)**  
  Authors: Xiaojie Xu, Zhengyuan Lin, Kang He, Yukang Feng, Xiaofeng Mao, Yuanyang Yin, Kaipeng Zhang, Yongtao Ge  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21686v1.pdf)  
  Keywords: world model, interactive, benchmark, video generation, dit, evaluation, style, image-to-video, trajectory  
- **[CityRAG: Stepping Into a City via Spatially-Grounded Video Generation](https://arxiv.org/abs/2604.19741v1)**  
  Authors: Gene Chou, Charles Herrmann, Kyle Genova, Boyang Deng, Songyou Peng, Bharath Hariharan, Jason Y. Zhang, Noah Snavely, Philipp Henzler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19741v1.pdf)  
  Keywords: robotics, video generation, simulation, i2v, dit, t2v, autonomous driving, physical  
- **[TS-Attn: Temporal-wise Separable Attention for Multi-Event Video Generation](https://arxiv.org/abs/2604.19473v1)**  
  Authors: Hongyu Zhang, Yufan Deng, Zilin Pan, Peng-Tao Jiang, Bo Li, Qibin Hou, Zhiyang Dou, Zhen Dong, Daquan Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19473v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Hong-yu-Zhang/TS-Attn?style=social)](https://github.com/Hong-yu-Zhang/TS-Attn)  
  Keywords: temporal consistency, video generation, dit, t2v, text-to-video, image-to-video  
- **[AnimationBench: Are Video Models Good at Character-Centric Animation?](https://arxiv.org/abs/2604.15299v1)**  
  Authors: Leyi Wu, Pengjun Fang, Kai Sun, Yazhou Xing, Yinwei Wu, Songsong Wang, Ziqi Huang, Dan Zhou, Yingqing He, Ying-Cong Chen, Qifeng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.15299v1.pdf)  
  Keywords: benchmark, video generation, i2v, evaluation, style, image-to-video  
- **[Flow of Truth: Proactive Temporal Forensics for Image-to-Video Generation](https://arxiv.org/abs/2604.15003v1)**  
  Authors: Yuzhuo Chen, Zehua Ma, Han Fang, Hengyi Wang, Guanjie Wang, Weiming Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.15003v1.pdf)  
  Keywords: video generation, i2v, creative, dit, image-to-video  
- **[Prompt-to-Gesture: Measuring the Capabilities of Image-to-Video Deictic Gesture Generation](https://arxiv.org/abs/2604.14953v1)**  
  Authors: Hassan Ali, Doreen Jirak, Luca Müller, Stefan Wermter  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.14953v1.pdf)  
  Keywords: video generation, dit, gesture, image-to-video  
- **[ARGen: Affect-Reinforced Generative Augmentation towards Vision-based Dynamic Emotion Perception](https://arxiv.org/abs/2604.12255v1)**  
  Authors: Huanzhen Wang, Ziheng Zhou, Jiaqi Song, Li He, Yunshi Lan, Yan Wang, Wenqiang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.12255v1.pdf)  
  Keywords: dynamics, dit, image-to-video, video diffusion  
- **[Immune2V: Image Immunization Against Dual-Stream Image-to-Video Generation](https://arxiv.org/abs/2604.10837v1)**  
  Authors: Zeqian Long, Ozgur Kara, Haotian Xue, Yongxin Chen, James M. Rehg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.10837v1.pdf)  
  Keywords: video generation, i2v, dit, image-to-video, trajectory  

### Long Video Generation

*Showing the latest 50 out of 111 papers*

- **[ABC: Any-Subset Autoregression via Non-Markovian Diffusion Bridges in Continuous Time and Space](https://arxiv.org/abs/2604.27443v1)**  
  Authors: Gabe Guo, Thanawat Sornwanee, Lutong Hao, Elon Litman, Stefano Ermon, Jose Blanchet  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.27443v1.pdf)  
  Keywords: dynamics, denoising, video generation, autoregressive, dit, diffusion model, physical  
- **[Mutual Forcing: Dual-Mode Self-Evolution for Fast Autoregressive Audio-Video Character Generation](https://arxiv.org/abs/2604.25819v1)**  
  Authors: Yupeng Zhou, Lianghua Huang, Zhifan Wu, Jiabao Wang, Yupeng Shi, Biao Jiang, Daquan Zhou, Yu Liu, Ming-Ming Cheng, Qibin Hou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.25819v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://mutualforcing.github.io)  
  Keywords: streaming, video generation, autoregressive, dit, distillation  
- **[FCMBench-Video: Benchmarking Document Video Intelligence](https://arxiv.org/abs/2604.25186v2)**  
  Authors: Runze Cui, Fangxin Shang, Yehui Yang, Qing Yang, Yanwu Xu, Tao Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.25186v2.pdf)  
  Keywords: dit, evaluation, long-form, benchmark  
- **[Talker-T2AV: Joint Talking Audio-Video Generation with Autoregressive Diffusion Modeling](https://arxiv.org/abs/2604.23586v1)**  
  Authors: Zhen Ye, Xu Tan, Aoxiong Yin, Hongzhan Lin, Guangyan Zhang, Peiwen Sun, Yiming Li, Chi-Min Chan, Wei Ye, Shikun Zhang, Wei Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.23586v1.pdf)  
  Keywords: denoising, benchmark, video generation, diffusion transformer, autoregressive, talking head, diffusion model  
- **[EAD-Net: Emotion-Aware Talking Head Generation with Spatial Refinement and Temporal Coherence](https://arxiv.org/abs/2604.23325v1)**  
  Authors: Yahui Li, Yinfeng Yu, Liejun Wang, Shengjie Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.23325v1.pdf)  
  Keywords: temporal consistency, video generation, long video, dit, talking head, multi-modal  
- **[HFS-TriNet: A Three-Branch Collaborative Feature Learning Network for Prostate Cancer Classification from TRUS Videos](https://arxiv.org/abs/2604.22388v1)**  
  Authors: Xu Lu, Qianhong Peng, Qihao Zhou, Shaopeng Liu, Xiuqin Ye, Chuan Yang, Yuan Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.22388v1.pdf)  
  Keywords: denoising, medical, temporal consistency, sound  
- **[Exploring the Role of Synthetic Data Augmentation in Controllable Human-Centric Video Generation](https://arxiv.org/abs/2604.21291v1)**  
  Authors: Yuanchen Fei, Yude Zou, Zejian Kang, Ming Li, Jiaying Zhou, Xiangru Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21291v1.pdf)  
  Keywords: temporal consistency, video generation, video synthesis, controllable, efficient, identity  
- **[Sparse Forcing: Native Trainable Sparse Attention for Real-time Autoregressive Diffusion Video Generation](https://arxiv.org/abs/2604.21221v1)**  
  Authors: Boxun Xu, Yuming Du, Zichang Liu, Siyu Yang, Ziyang Jiang, Siqi Yan, Rajasi Saha, Albert Pumarola, Wenchen Wang, Peng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21221v1.pdf)  
  Keywords: efficient, video generation, autoregressive, video diffusion, diffusion model, text-to-video  
- **[DynamicRad: Content-Adaptive Sparse Attention for Long Video Diffusion](https://arxiv.org/abs/2604.20470v1)**  
  Authors: Yongji Long, Shijun Liang, Jintao Li, Yun Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.20470v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Adamlong3/DynamicRad?style=social)](https://github.com/Adamlong3/DynamicRad)  
  Keywords: dynamics, physics, long video, video diffusion  
- **[X-Cache: Cross-Chunk Block Caching for Few-Step Autoregressive World Models Inference](https://arxiv.org/abs/2604.20289v1)**  
  Authors: Yixiao Zeng, Jianlei Zheng, Chaoda Zheng, Shijia Chen, Mingdian Liu, Tongping Liu, Tengwei Luo, Yu Zhang, Boyang Wang, Linkun Xu, Siyuan Lu, Bo Tian, Xianming Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.20289v1.pdf)  
  Keywords: world model, denoising, interactive, action-conditioned, video generation, simulation, acceleration, autoregressive, dit, evaluation, video diffusion, controllable, autonomous driving  

### Personalization & Customization

*Showing the latest 50 out of 83 papers*

- **[AesRM: Improving Video Aesthetics with Expert-Level Feedback](https://arxiv.org/abs/2604.28078v1)**  
  Authors: Yujin Han, Yujie Wei, Yefei He, Xinyu Liu, Tianle Li, Zichao Yu, Andi Han, Shiwei Zhang, Tingyu Weng, Difan Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.28078v1.pdf)  
  Keywords: concept, benchmark, video generation, dit, evaluation, film, efficient  
- **[Generate Your Talking Avatar from Video Reference](https://arxiv.org/abs/2604.27918v1)**  
  Authors: Zujin Guo, Zhenhui Ye, Yi Ren, Yuanming Li, Ce Chen, Zhibin Hong, Chen Change Loy  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.27918v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://www.heygen.com/research)  
  Keywords: benchmark, avatar, dit, image-to-video, identity  
- **[MuSS: A Large-Scale Dataset and Cinematic Narrative Benchmark for Multi-Shot Subject-to-Video Generation](https://arxiv.org/abs/2604.23789v1)**  
  Authors: Haojie Zhang, Di Wu, Bingyan Liu, Linjie Zhong, Yuancheng Wei, Xingsong Ye, Nanqing Liu, Yaling Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.23789v1.pdf)  
  Keywords: video generation, identity, benchmark  
- **[CineAGI: Character-Consistent Movie Creation through LLM-Orchestrated Multi-Modal Generation and Cross-Scene Integration](https://arxiv.org/abs/2604.23579v1)**  
  Authors: Tianyidan Xie, Zhentao Huang, Mingjie Wang, Xin Huang, Jun Zhou, Minglun Gong, Zili Yi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.23579v1.pdf)  
  Keywords: video generation, multi-modal, identity  
- **[Seeing Fast and Slow: Learning the Flow of Time in Videos](https://arxiv.org/abs/2604.21931v1)**  
  Authors: Yen-Siang Wu, Rundong Luo, Jingsen Zhu, Tao Tu, Ali Farhadi, Matthew Wallingford, Yu-Chiang Frank Wang, Steve Marschner, Wei-Chiu Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21931v1.pdf)  
  Keywords: concept, video generation, super-resolution, dit, controllable, film  
- **[WorldMark: A Unified Benchmark Suite for Interactive Video World Models](https://arxiv.org/abs/2604.21686v1)**  
  Authors: Xiaojie Xu, Zhengyuan Lin, Kang He, Yukang Feng, Xiaofeng Mao, Yuanyang Yin, Kaipeng Zhang, Yongtao Ge  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21686v1.pdf)  
  Keywords: world model, interactive, benchmark, video generation, dit, evaluation, style, image-to-video, trajectory  
- **[Exploring the Role of Synthetic Data Augmentation in Controllable Human-Centric Video Generation](https://arxiv.org/abs/2604.21291v1)**  
  Authors: Yuanchen Fei, Yude Zou, Zejian Kang, Ming Li, Jiaying Zhou, Xiangru Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21291v1.pdf)  
  Keywords: temporal consistency, video generation, video synthesis, controllable, efficient, identity  
- **[AttentionBender: Manipulating Cross-Attention in Video Diffusion Transformers as a Creative Probe](https://arxiv.org/abs/2604.20936v1)**  
  Authors: Adam Cole, Mick Grierson  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.20936v1.pdf)  
  Keywords: video generation, creative, diffusion transformer, dit, style, video diffusion  
- **[MMControl: Unified Multi-Modal Control for Joint Audio-Video Generation](https://arxiv.org/abs/2604.19679v2)**  
  Authors: Liyang Li, Wen Wang, Canyu Zhao, Tianjian Feng, Zhiyue Zhao, Hao Chen, Chunhua Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19679v2.pdf)  
  Keywords: video generation, diffusion transformer, dit, layout, multi-modal, video diffusion, controllable, identity  
- **[AutoAWG: Adverse Weather Generation with Adaptive Multi-Controls for Automotive Videos](https://arxiv.org/abs/2604.18993v1)**  
  Authors: Jiagao Hu, Daiguo Zhou, Danzhen Fu, Fuhao Li, Zepeng Wang, Fei Wang, Wenhua Liao, Jiayi Xie, Haiyang Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.18993v1.pdf) | [![GitHub](https://img.shields.io/github/stars/higherhu/AutoAWG?style=social)](https://github.com/higherhu/AutoAWG)  
  Keywords: temporal consistency, video generation, dit, style, controllable, autonomous driving  

### Physical Understanding

*Showing the latest 50 out of 141 papers*

- **[Physically Native World Models: A Hamiltonian Perspective on Generative World Modeling](https://arxiv.org/abs/2605.00412v1)**  
  Authors: Sen Cui, Jingheng Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.00412v1.pdf)  
  Keywords: dynamics, world model, robotics, controllable, autonomous driving, physical, trajectory  
- **[Lucid-XR: An Extended-Reality Data Engine for Robotic Manipulation](https://arxiv.org/abs/2605.00244v1)**  
  Authors: Yajvan Ravan, Adam Rashid, Alan Yu, Kai McClennen, Gio Huh, Kevin Yang, Zhutian Yang, Qinxi Yu, Xiaolong Wang, Phillip Isola, Ge Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.00244v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lucidxr.github.io)  
  Keywords: video generation, simulation, multi-modal, evaluation, physics  
- **[PhyCo: Learning Controllable Physical Priors for Generative Motion](https://arxiv.org/abs/2604.28169v1)**  
  Authors: Sriram Narayanan, Ziyu Jiang, Srinivasa Narasimhan, Manmohan Chandraker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.28169v1.pdf)  
  Keywords: benchmark, video generation, simulation, dit, video diffusion, diffusion model, controllable, physics, physical  
- **[ABC: Any-Subset Autoregression via Non-Markovian Diffusion Bridges in Continuous Time and Space](https://arxiv.org/abs/2604.27443v1)**  
  Authors: Gabe Guo, Thanawat Sornwanee, Lutong Hao, Elon Litman, Stefano Ermon, Jose Blanchet  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.27443v1.pdf)  
  Keywords: dynamics, denoising, video generation, autoregressive, dit, diffusion model, physical  
- **[DepthPilot: From Controllability to Interpretability in Colonoscopy Video Generation](https://arxiv.org/abs/2604.26232v1)**  
  Authors: Junhu Fu, Ke Chen, Weidong Guo, Shuyu Liang, Jie Xu, Chen Ma, Kehao Wang, Shengli Lin, Zeju Li, Yuanyuan Wang, Yi Guo, Shuo Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.26232v1.pdf)  
  Keywords: dynamics, world model, denoising, benchmark, video generation, medical, evaluation, controllable, efficient, physical  
- **[PhysLayer: Language-Guided Layered Animation with Depth-Aware Physics](https://arxiv.org/abs/2604.23574v1)**  
  Authors: Tianyidan Xie, Zhentao Huang, Mingjie Wang, Xin Huang, Jun Zhou, Minglun Gong, Zili Yi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.23574v1.pdf)  
  Keywords: dynamics, video generation, simulation, video synthesis, image animation, evaluation, controllable, physics, image-to-video, physical  
- **[Agentic World Modeling: Foundations, Capabilities, Laws, and Beyond](https://arxiv.org/abs/2604.22748v1)**  
  Authors: Meng Chu, Xuan Billy Zhang, Kevin Qinghong Lin, Lingdong Kong, Jize Zhang, Teng Tu, Weijian Ma, Ziqi Huang, Senqiao Yang, Wei Huang, Yeying Jin, Zhefan Rao, Jinhui Ye, Xinyu Lin, Xichen Zhang, Qisheng Hu, Shuai Yang, Leyang Shen, Wei Chow, Yifei Dong, Fengyi Wu, Quanyu Long, Bin Xia, Shaozuo Yu, Mingkang Zhu, Wenhu Zhang, Jiehui Huang, Haokun Gui, Haoxuan Che, Long Chen, Qifeng Chen, Wenxuan Zhang, Wenya Wang, Xiaojuan Qi, Yang Deng, Yanwei Li, Mike Zheng Shou, Zhi-Qi Cheng, See-Kiong Ng, Ziwei Liu, Philip Torr, Jiaya Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.22748v1.pdf)  
  Keywords: dynamics, world model, action-conditioned, video generation, simulation, dit, evaluation, physical  
- **[Can Multimodal Large Language Models Truly Understand Small Objects?](https://arxiv.org/abs/2604.22884v1)**  
  Authors: Fujun Han, Junan Chen, Xintong Zhu, Jingqi Ye, Xuanjie Mao, Tao Chen, Peng Ye  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.22884v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Hanfj-X/SOU?style=social)](https://github.com/Hanfj-X/SOU)  
  Keywords: physics, evaluation, benchmark  
- **[DeVI: Physics-based Dexterous Human-Object Interaction via Synthetic Video Imitation](https://arxiv.org/abs/2604.20841v1)**  
  Authors: Hyeonwoo Kim, Jeonghwan Kim, Kyungwon Cho, Hanbyul Joo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.20841v1.pdf)  
  Keywords: dit, physics, physical  
- **[DynamicRad: Content-Adaptive Sparse Attention for Long Video Diffusion](https://arxiv.org/abs/2604.20470v1)**  
  Authors: Yongji Long, Shijun Liang, Jintao Li, Yun Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.20470v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Adamlong3/DynamicRad?style=social)](https://github.com/Adamlong3/DynamicRad)  
  Keywords: dynamics, physics, long video, video diffusion  

### Surveys & Benchmarks

*Showing the latest 50 out of 209 papers*

- **[Lucid-XR: An Extended-Reality Data Engine for Robotic Manipulation](https://arxiv.org/abs/2605.00244v1)**  
  Authors: Yajvan Ravan, Adam Rashid, Alan Yu, Kai McClennen, Gio Huh, Kevin Yang, Zhutian Yang, Qinxi Yu, Xiaolong Wang, Phillip Isola, Ge Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.00244v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lucidxr.github.io)  
  Keywords: video generation, simulation, multi-modal, evaluation, physics  
- **[PhyCo: Learning Controllable Physical Priors for Generative Motion](https://arxiv.org/abs/2604.28169v1)**  
  Authors: Sriram Narayanan, Ziyu Jiang, Srinivasa Narasimhan, Manmohan Chandraker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.28169v1.pdf)  
  Keywords: benchmark, video generation, simulation, dit, video diffusion, diffusion model, controllable, physics, physical  
- **[AesRM: Improving Video Aesthetics with Expert-Level Feedback](https://arxiv.org/abs/2604.28078v1)**  
  Authors: Yujin Han, Yujie Wei, Yefei He, Xinyu Liu, Tianle Li, Zichao Yu, Andi Han, Shiwei Zhang, Tingyu Weng, Difan Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.28078v1.pdf)  
  Keywords: concept, benchmark, video generation, dit, evaluation, film, efficient  
- **[World Model for Robot Learning: A Comprehensive Survey](https://arxiv.org/abs/2605.00080v1)**  
  Authors: Bohan Hou, Gen Li, Jindou Jia, Tuo An, Xinying Guo, Sicong Leng, Haoran Geng, Yanjie Ze, Tatsuya Harada, Philip Torr, Oier Mees, Marc Pollefeys, Zhuang Liu, Jiajun Wu, Pieter Abbeel, Jitendra Malik, Yilun Du, Jianfei Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.00080v1.pdf)  
  Keywords: world model, benchmark, video generation, simulation, architecture, evaluation, survey, controllable, autonomous driving  
- **[Generate Your Talking Avatar from Video Reference](https://arxiv.org/abs/2604.27918v1)**  
  Authors: Zujin Guo, Zhenhui Ye, Yi Ren, Yuanming Li, Ce Chen, Zhibin Hong, Chen Change Loy  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.27918v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://www.heygen.com/research)  
  Keywords: benchmark, avatar, dit, image-to-video, identity  
- **[Robot Learning from Human Videos: A Survey](https://arxiv.org/abs/2604.27621v1)**  
  Authors: Junyi Ma, Erhang Zhang, Haoran Yang, Ditao Li, Chenyang Xu, Guangming Wang, Hesheng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.27621v1.pdf) | [![GitHub](https://img.shields.io/github/stars/IRMVLab/awesome-robot-learning-from-human-videos?style=social)](https://github.com/IRMVLab/awesome-robot-learning-from-human-videos)  
  Keywords: video generation, dit, robotics, survey  
- **[Learning from the Unseen: Generative Data Augmentation for Geometric-Semantic Accident Anticipation](https://arxiv.org/abs/2605.00051v1)**  
  Authors: Yanchen Guan, Haicheng Liao, Chengyue Wang, Xingcheng Liu, Jiaxun Zhang, Keqiang Li, Zhenning Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.00051v1.pdf)  
  Keywords: benchmark, video synthesis, dit, evaluation, autonomous driving  
- **[Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising](https://arxiv.org/abs/2604.26694v1)**  
  Authors: Jun Guo, Qiwei Li, Peiyan Li, Zilong Chen, Nan Sun, Yifei Su, Heyun Wang, Yuan Zhang, Xinghang Li, Huaping Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.26694v1.pdf)  
  Keywords: world model, denoising, benchmark, diffusion transformer, video diffusion, diffusion model, efficient  
- **[DepthPilot: From Controllability to Interpretability in Colonoscopy Video Generation](https://arxiv.org/abs/2604.26232v1)**  
  Authors: Junhu Fu, Ke Chen, Weidong Guo, Shuyu Liang, Jie Xu, Chen Ma, Kehao Wang, Shengli Lin, Zeju Li, Yuanyuan Wang, Yi Guo, Shuo Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.26232v1.pdf)  
  Keywords: dynamics, world model, denoising, benchmark, video generation, medical, evaluation, controllable, efficient, physical  
- **[Benchmarking and Improving GUI Agents in High-Dynamic Environments](https://arxiv.org/abs/2604.25380v1)**  
  Authors: Enqi Liu, Liyuan Pan, Zhi Gao, Yan Yang, Chenrui Shi, Yang Liu, Jingrong Wu, Qing Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.25380v1.pdf)  
  Keywords: dit, benchmark, action-conditioned  

### Text-to-Video Generation

*Showing the latest 50 out of 56 papers*

- **[HuM-Eval: A Coarse-to-Fine Framework for Human-Centric Video Evaluation](https://arxiv.org/abs/2604.25361v1)**  
  Authors: Bingzi Zhang, Kaisi Guan, Ruihua Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.25361v1.pdf)  
  Keywords: text-to-video, benchmark, video generation, evaluation, human motion  
- **[World-R1: Reinforcing 3D Constraints for Text-to-Video Generation](https://arxiv.org/abs/2604.24764v1)**  
  Authors: Weijie Wang, Xiaoxuan He, Youping Gu, Yifan Yang, Zeyu Zhang, Yefei He, Yanbo Ding, Xirui Hu, Donny Y. Chen, Zhiyuan He, Yuqing Yang, Bohan Zhuang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.24764v1.pdf)  
  Keywords: video generation, simulation, architecture, dit, evaluation, text-to-video  
- **[KD-CVG: A Knowledge-Driven Approach for Creative Video Generation](https://arxiv.org/abs/2604.21362v1)**  
  Authors: Linkai Liu, Wei Feng, Xi Zhao, Shen Zhang, Xingye Chen, Zheng Zhang, Jingjing Lv, Junjie Shen, Ching Law, Yuchen Zhou, Zipeng Guo, Chao Gou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21362v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://kdcvg.github.io/KDCVG)  
  Keywords: video generation, advertising, creative, t2v, text-to-video  
- **[Sparse Forcing: Native Trainable Sparse Attention for Real-time Autoregressive Diffusion Video Generation](https://arxiv.org/abs/2604.21221v1)**  
  Authors: Boxun Xu, Yuming Du, Zichang Liu, Siyu Yang, Ziyang Jiang, Siqi Yan, Rajasi Saha, Albert Pumarola, Wenchen Wang, Peng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21221v1.pdf)  
  Keywords: efficient, video generation, autoregressive, video diffusion, diffusion model, text-to-video  
- **[CityRAG: Stepping Into a City via Spatially-Grounded Video Generation](https://arxiv.org/abs/2604.19741v1)**  
  Authors: Gene Chou, Charles Herrmann, Kyle Genova, Boyang Deng, Songyou Peng, Bharath Hariharan, Jason Y. Zhang, Noah Snavely, Philipp Henzler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19741v1.pdf)  
  Keywords: robotics, video generation, simulation, i2v, dit, t2v, autonomous driving, physical  
- **[TS-Attn: Temporal-wise Separable Attention for Multi-Event Video Generation](https://arxiv.org/abs/2604.19473v1)**  
  Authors: Hongyu Zhang, Yufan Deng, Zilin Pan, Peng-Tao Jiang, Bo Li, Qibin Hou, Zhiyang Dou, Zhen Dong, Daquan Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19473v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Hong-yu-Zhang/TS-Attn?style=social)](https://github.com/Hong-yu-Zhang/TS-Attn)  
  Keywords: temporal consistency, video generation, dit, t2v, text-to-video, image-to-video  
- **[FlowC2S: Flowing from Current to Succeeding Frames for Fast and Memory-Efficient Video Continuation](https://arxiv.org/abs/2604.17625v1)**  
  Authors: Hovhannes Margaryan, Quentin Bammey, Christian Sandor  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.17625v1.pdf)  
  Keywords: efficient, text-to-video, evaluation  
- **[Generative Refinement Networks for Visual Synthesis](https://arxiv.org/abs/2604.13030v1)**  
  Authors: Jian Han, Jinlai Liu, Jiahuan Wang, Bingyue Peng, Zehuan Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.13030v1.pdf)  
  Keywords: efficient, benchmark, video generation, autoregressive, dit, diffusion model, text-to-video  
- **[VideoFlexTok: Flexible-Length Coarse-to-Fine Video Tokenization](https://arxiv.org/abs/2604.12887v1)**  
  Authors: Andrei Atanov, Jesse Allardice, Roman Bachmann, Oğuzhan Fatih Kar, R Devon Hjelm, David Griffiths, Peter Fu, Afshin Dehghan, Amir Zamir  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.12887v1.pdf)  
  Keywords: video generation, long video, efficient, text-to-video  
- **[Motif-Video 2B: Technical Report](https://arxiv.org/abs/2604.16503v1)**  
  Authors: Junghwan Lim, Wai Ting Cheung, Minsu Ha, Beomgyu Kim, Taewhan Kim, Haesol Lee, Dongpin Oh, Jeesoo Lee, Taehyun Kim, Minjae Kim, Sungmin Lee, Hyeyeon Cho, Dahye Choi, Jaeheui Her, Jaeyeon Huh, Hanbin Jung, Changjin Kang, Dongseok Kim, Jangwoong Kim, Youngrok Kim, Hyukjin Kweon, Hongjoo Lee, Jeongdoo Lee, Junhyeok Lee, Eunhwan Park, Yeongjae Park, Bokki Ryu, Dongjoo Weon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.16503v1.pdf)  
  Keywords: video generation, efficient, text-to-video, temporal consistency  

### Video Editing

- **[Latent Inter-Frame Pruning: A Training-Free Method Bridging Traditional Video Compression and Modern Diffusion Transformers for Efficient Generation](https://arxiv.org/abs/2604.23858v1)**  
  Authors: Dennis Menn, Chih-Hsien Chou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.23858v1.pdf)  
  Keywords: video generation, diffusion transformer, video editing, dit, diffusion model, efficient  
- **[LIVE: Leveraging Image Manipulation Priors for Instruction-based Video Editing](https://arxiv.org/abs/2604.17021v1)**  
  Authors: Weicheng Wang, Zhicheng Zhang, Zhongqi Zhang, Juncheng Zhou, Yongjie Zhu, Wenyu Qin, Meng Wang, Pengfei Wan, Jufeng Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.17021v1.pdf)  
  Keywords: benchmark, video generation, video editing, dit, evaluation  
- **[UniEditBench: A Unified and Cost-Effective Benchmark for Image and Video Editing via Distilled MLLMs](https://arxiv.org/abs/2604.15871v1)**  
  Authors: Lifan Jiang, Tianrun Wu, Yuhang Pei, Chenyang Wang, Boxi Wu, Deng Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.15871v1.pdf) | [![GitHub](https://img.shields.io/github/stars/wesar1/UniEditBench?style=social)](https://github.com/wesar1/UniEditBench)  
  Keywords: video editing, dit, evaluation, benchmark  
- **[Empowering Video Translation using Multimodal Large Language Models](https://arxiv.org/abs/2604.11283v1)**  
  Authors: Bingzheng QU, Kehai Chen, Xuefeng Bai, Min Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.11283v1.pdf)  
  Keywords: dit, video translation, survey, controllable, identity  
- **[Rein3D: Reinforced 3D Indoor Scene Generation with Panoramic Video Diffusion Models](https://arxiv.org/abs/2604.10578v2)**  
  Authors: Dehui Wang, Congsheng Xu, Rong Wei, Yue Shi, Shoufa Chen, Dingxiang Luo, Tianshuo Yang, Xiaokang Yang, Wei Sui, Yusen Qin, Rui Tang, Yao Mu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.10578v2.pdf)  
  Keywords: video-to-video, super-resolution, video diffusion, diffusion model  
- **[InsEdit: Towards Instruction-based Visual Editing via Data-Efficient Video Diffusion Models Adaptation](https://arxiv.org/abs/2604.08646v1)**  
  Authors: Zhefan Rao, Bin Zou, Haoxuan Che, Xuanhua He, Chong Hou Choi, Yanheng Li, Rui Liu, Qifeng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08646v1.pdf)  
  Keywords: benchmark, video generation, architecture, video editing, dit, video diffusion, diffusion model, efficient  
- **[Lighting-grounded Video Generation with Renderer-based Agent Reasoning](https://arxiv.org/abs/2604.07966v1)**  
  Authors: Ziqi Cai, Taoyu Yang, Zheng Chang, Si Li, Han Jiang, Shuchen Weng, Boxin Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07966v1.pdf)  
  Keywords: temporal consistency, video generation, video synthesis, dit, controllable, layout, video diffusion, diffusion model, video-to-video, film, image-to-video, trajectory  
- **[ImVideoEdit: Image-learning Video Editing via 2D Spatial Difference Attention Blocks](https://arxiv.org/abs/2604.07958v2)**  
  Authors: Jiayang Xu, Fan Zhuo, Majun Zhang, Changhao Pan, Zehan Wang, Siyu Chen, Xiaoda Yang, Tao Jin, Zhou Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07958v2.pdf)  
  Keywords: dynamics, temporal consistency, video editing, dit, efficient  
- **[Evolution of Video Generative Foundations](https://arxiv.org/abs/2604.06339v1)**  
  Authors: Teng Hu, Jiangning Zhang, Hongrui Huang, Ran Yi, Zihan Su, Jieyu Weng, Zhucun Xue, Lizhuang Ma, Ming-Hsuan Yang, Dacheng Tao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06339v1.pdf) | [![GitHub](https://img.shields.io/github/stars/sjtuplayer/Awesome-Video-Foundations?style=social)](https://github.com/sjtuplayer/Awesome-Video-Foundations)  
  Keywords: dynamics, world model, education, video generation, simulation, video editing, dit, survey, diffusion model, autonomous driving  
- **[UENR-600K: A Large-Scale Physically Grounded Dataset for Nighttime Video Deraining](https://arxiv.org/abs/2604.04402v1)**  
  Authors: Pei Yang, Hai Ci, Beibei Lin, Yiren Song, Mike Zheng Shou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04402v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://showlab.github.io/UENR-600K)  
  Keywords: video generation, video-to-video, physical, benchmark  

### Video Inpainting & Completion

- **[LMGenDrive: Bridging Multimodal Understanding and Generative World Modeling for End-to-End Driving](https://arxiv.org/abs/2604.08719v1)**  
  Authors: Hao Shao, Letian Wang, Yang Zhou, Yuxuan Hu, Zhuofan Zong, Steven L. Waslander, Wei Zhan, Hongsheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08719v1.pdf)  
  Keywords: world model, benchmark, video generation, autoregressive, autonomous driving, video prediction  
- **[Novel View Synthesis as Video Completion](https://arxiv.org/abs/2604.08500v1)**  
  Authors: Qi Wu, Khiem Vuong, Minsik Jeon, Srinivasa Narasimhan, Deva Ramanan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08500v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://frame-crafter.github.io)  
  Keywords: diffusion model, benchmark, video diffusion, video completion, novel view  
- **[SEM-ROVER: Semantic Voxel-Guided Diffusion for Large-Scale Driving Scene Generation](https://arxiv.org/abs/2604.06113v1)**  
  Authors: Hiba Dahmani, Nathan Piasco, Moussab Bennehar, Luis Roldão, Dzmitry Tsishkou, Laurent Caraffa, Jean-Philippe Tarel, Roland Brémond  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06113v1.pdf)  
  Keywords: dit, outpainting, diffusion model  
- **[ChopGrad: Pixel-Wise Losses for Latent Video Diffusion via Truncated Backpropagation](https://arxiv.org/abs/2603.17812v2)**  
  Authors: Dmitriy Rivkin, Parker Ewen, Lili Gao, Julian Ost, Stefanie Walz, Rasika Kangutkar, Mario Bijelic, Felix Heide  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17812v2.pdf)  
  Keywords: video generation, video enhancement, latent video, super-resolution, dit, video diffusion, diffusion model, video inpainting, efficient  
- **[ConfCtrl: Enabling Precise Camera Control in Video Diffusion via Confidence-Aware Interpolation](https://arxiv.org/abs/2603.09819v1)**  
  Authors: Liudi Yang, George Eskandar, Fengyi Shen, Mohammad Altillawi, Yang Bai, Chi Zhang, Ziyuan Liu, Abhinav Valada  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09819v1.pdf)  
  Keywords: camera control, dit, video diffusion, diffusion model, video interpolation, novel view  
- **[Pinterest Canvas: Large-Scale Image Generation at Pinterest](https://arxiv.org/abs/2603.06453v1)**  
  Authors: Yu Wang, Eric Tzeng, Raymond Shiau, Jie Yang, Dmitry Kislyuk, Charles Rosenberg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06453v1.pdf)  
  Keywords: diffusion model, video generation, dit, outpainting, image-to-video  

### Video Super-Resolution & Enhancement

*Showing the latest 50 out of 64 papers*

- **[ABC: Any-Subset Autoregression via Non-Markovian Diffusion Bridges in Continuous Time and Space](https://arxiv.org/abs/2604.27443v1)**  
  Authors: Gabe Guo, Thanawat Sornwanee, Lutong Hao, Elon Litman, Stefano Ermon, Jose Blanchet  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.27443v1.pdf)  
  Keywords: dynamics, denoising, video generation, autoregressive, dit, diffusion model, physical  
- **[Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising](https://arxiv.org/abs/2604.26694v1)**  
  Authors: Jun Guo, Qiwei Li, Peiyan Li, Zilong Chen, Nan Sun, Yifei Su, Heyun Wang, Yuan Zhang, Xinghang Li, Huaping Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.26694v1.pdf)  
  Keywords: world model, denoising, benchmark, diffusion transformer, video diffusion, diffusion model, efficient  
- **[MetaSR: Content-Adaptive Metadata Orchestration for Generative Super-Resolution](https://arxiv.org/abs/2604.26244v1)**  
  Authors: Jiaqi Guo, Mingzhen Li, Haohong Wang, Aggelos K. Katsaggelos  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.26244v1.pdf)  
  Keywords: super-resolution, diffusion transformer, dit, distillation, efficient  
- **[DepthPilot: From Controllability to Interpretability in Colonoscopy Video Generation](https://arxiv.org/abs/2604.26232v1)**  
  Authors: Junhu Fu, Ke Chen, Weidong Guo, Shuyu Liang, Jie Xu, Chen Ma, Kehao Wang, Shengli Lin, Zeju Li, Yuanyuan Wang, Yi Guo, Shuo Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.26232v1.pdf)  
  Keywords: dynamics, world model, denoising, benchmark, video generation, medical, evaluation, controllable, efficient, physical  
- **[Talker-T2AV: Joint Talking Audio-Video Generation with Autoregressive Diffusion Modeling](https://arxiv.org/abs/2604.23586v1)**  
  Authors: Zhen Ye, Xu Tan, Aoxiong Yin, Hongzhan Lin, Guangyan Zhang, Peiwen Sun, Yiming Li, Chi-Min Chan, Wei Ye, Shikun Zhang, Wei Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.23586v1.pdf)  
  Keywords: denoising, benchmark, video generation, diffusion transformer, autoregressive, talking head, diffusion model  
- **[BurstGP: Enhancing Raw Burst Image Super Resolution with Generative Priors](https://arxiv.org/abs/2604.23508v1)**  
  Authors: Dong Huo, Tristan Aumentado-Armstrong, Samrudhdhi B. Rangrej, Maitreya Suin, Angela Ning Ye, Zhiming Hu, Amanpreet Walia, Amirhossein Kazerouni, Konstantinos G. Derpanis, Iqbal Mohomed, Alex Levinshtein  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.23508v1.pdf)  
  Keywords: dit, super-resolution, diffusion model  
- **[HFS-TriNet: A Three-Branch Collaborative Feature Learning Network for Prostate Cancer Classification from TRUS Videos](https://arxiv.org/abs/2604.22388v1)**  
  Authors: Xu Lu, Qianhong Peng, Qihao Zhou, Shaopeng Liu, Xiuqin Ye, Chuan Yang, Yuan Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.22388v1.pdf)  
  Keywords: denoising, medical, temporal consistency, sound  
- **[Seeing Fast and Slow: Learning the Flow of Time in Videos](https://arxiv.org/abs/2604.21931v1)**  
  Authors: Yen-Siang Wu, Rundong Luo, Jingsen Zhu, Tao Tu, Ali Farhadi, Matthew Wallingford, Yu-Chiang Frank Wang, Steve Marschner, Wei-Chiu Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.21931v1.pdf)  
  Keywords: concept, video generation, super-resolution, dit, controllable, film  
- **[X-Cache: Cross-Chunk Block Caching for Few-Step Autoregressive World Models Inference](https://arxiv.org/abs/2604.20289v1)**  
  Authors: Yixiao Zeng, Jianlei Zheng, Chaoda Zheng, Shijia Chen, Mingdian Liu, Tongping Liu, Tengwei Luo, Yu Zhang, Boyang Wang, Linkun Xu, Siyuan Lu, Bo Tian, Xianming Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.20289v1.pdf)  
  Keywords: world model, denoising, interactive, action-conditioned, video generation, simulation, acceleration, autoregressive, dit, evaluation, video diffusion, controllable, autonomous driving  
- **[Learning to Credit the Right Steps: Objective-aware Process Optimization for Visual Generation](https://arxiv.org/abs/2604.19234v2)**  
  Authors: Rui Li, Ke Hao, Yuanzhi Liang, Haibin Huang, Chi Zhang, Yun Gu, XueLong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19234v2.pdf)  
  Keywords: denoising, video generation, dit, evaluation, trajectory  

### World Models & Simulation

*Showing the latest 50 out of 100 papers*

- **[Physically Native World Models: A Hamiltonian Perspective on Generative World Modeling](https://arxiv.org/abs/2605.00412v1)**  
  Authors: Sen Cui, Jingheng Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.00412v1.pdf)  
  Keywords: dynamics, world model, robotics, controllable, autonomous driving, physical, trajectory  
- **[Lucid-XR: An Extended-Reality Data Engine for Robotic Manipulation](https://arxiv.org/abs/2605.00244v1)**  
  Authors: Yajvan Ravan, Adam Rashid, Alan Yu, Kai McClennen, Gio Huh, Kevin Yang, Zhutian Yang, Qinxi Yu, Xiaolong Wang, Phillip Isola, Ge Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.00244v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lucidxr.github.io)  
  Keywords: video generation, simulation, multi-modal, evaluation, physics  
- **[PhyCo: Learning Controllable Physical Priors for Generative Motion](https://arxiv.org/abs/2604.28169v1)**  
  Authors: Sriram Narayanan, Ziyu Jiang, Srinivasa Narasimhan, Manmohan Chandraker  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.28169v1.pdf)  
  Keywords: benchmark, video generation, simulation, dit, video diffusion, diffusion model, controllable, physics, physical  
- **[World Model for Robot Learning: A Comprehensive Survey](https://arxiv.org/abs/2605.00080v1)**  
  Authors: Bohan Hou, Gen Li, Jindou Jia, Tuo An, Xinying Guo, Sicong Leng, Haoran Geng, Yanjie Ze, Tatsuya Harada, Philip Torr, Oier Mees, Marc Pollefeys, Zhuang Liu, Jiajun Wu, Pieter Abbeel, Jitendra Malik, Yilun Du, Jianfei Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2605.00080v1.pdf)  
  Keywords: world model, benchmark, video generation, simulation, architecture, evaluation, survey, controllable, autonomous driving  
- **[Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising](https://arxiv.org/abs/2604.26694v1)**  
  Authors: Jun Guo, Qiwei Li, Peiyan Li, Zilong Chen, Nan Sun, Yifei Su, Heyun Wang, Yuan Zhang, Xinghang Li, Huaping Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.26694v1.pdf)  
  Keywords: world model, denoising, benchmark, diffusion transformer, video diffusion, diffusion model, efficient  
- **[DepthPilot: From Controllability to Interpretability in Colonoscopy Video Generation](https://arxiv.org/abs/2604.26232v1)**  
  Authors: Junhu Fu, Ke Chen, Weidong Guo, Shuyu Liang, Jie Xu, Chen Ma, Kehao Wang, Shengli Lin, Zeju Li, Yuanyuan Wang, Yi Guo, Shuo Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.26232v1.pdf)  
  Keywords: dynamics, world model, denoising, benchmark, video generation, medical, evaluation, controllable, efficient, physical  
- **[Benchmarking and Improving GUI Agents in High-Dynamic Environments](https://arxiv.org/abs/2604.25380v1)**  
  Authors: Enqi Liu, Liyuan Pan, Zhi Gao, Yan Yang, Chenrui Shi, Yang Liu, Jingrong Wu, Qing Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.25380v1.pdf)  
  Keywords: dit, benchmark, action-conditioned  
- **[World-R1: Reinforcing 3D Constraints for Text-to-Video Generation](https://arxiv.org/abs/2604.24764v1)**  
  Authors: Weijie Wang, Xiaoxuan He, Youping Gu, Yifan Yang, Zeyu Zhang, Yefei He, Yanbo Ding, Xirui Hu, Donny Y. Chen, Zhiyuan He, Yuqing Yang, Bohan Zhuang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.24764v1.pdf)  
  Keywords: video generation, simulation, architecture, dit, evaluation, text-to-video  
- **[PhysLayer: Language-Guided Layered Animation with Depth-Aware Physics](https://arxiv.org/abs/2604.23574v1)**  
  Authors: Tianyidan Xie, Zhentao Huang, Mingjie Wang, Xin Huang, Jun Zhou, Minglun Gong, Zili Yi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.23574v1.pdf)  
  Keywords: dynamics, video generation, simulation, video synthesis, image animation, evaluation, controllable, physics, image-to-video, physical  
- **[Agentic World Modeling: Foundations, Capabilities, Laws, and Beyond](https://arxiv.org/abs/2604.22748v1)**  
  Authors: Meng Chu, Xuan Billy Zhang, Kevin Qinghong Lin, Lingdong Kong, Jize Zhang, Teng Tu, Weijian Ma, Ziqi Huang, Senqiao Yang, Wei Huang, Yeying Jin, Zhefan Rao, Jinhui Ye, Xinyu Lin, Xichen Zhang, Qisheng Hu, Shuai Yang, Leyang Shen, Wei Chow, Yifei Dong, Fengyi Wu, Quanyu Long, Bin Xia, Shaozuo Yu, Mingkang Zhu, Wenhu Zhang, Jiehui Huang, Haokun Gui, Haoxuan Che, Long Chen, Qifeng Chen, Wenxuan Zhang, Wenya Wang, Xiaojuan Qi, Yang Deng, Yanwei Li, Mike Zheng Shou, Zhi-Qi Cheng, See-Kiong Ng, Ziwei Liu, Philip Torr, Jiaya Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.22748v1.pdf)  
  Keywords: dynamics, world model, action-conditioned, video generation, simulation, dit, evaluation, physical  



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
