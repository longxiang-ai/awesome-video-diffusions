# Awesome Video Diffusions [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Video Diffusion Models and Video Generation. Content is automatically updated daily.

> Last Update: 2026-04-22 02:36:39

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
- [Applications](#applications) (39 papers) - Domain-specific applications of video diffusion models
- [Architecture & Efficiency](#architecture-&-efficiency) (354 papers) - Architectural innovations (DiT, UNet), flow matching, and training/inference efficiency
- [Audio & Multi-modal](#audio-&-multi-modal) (31 papers) - Audio-driven and multi-modal conditioned video generation
- [Controllable Generation](#controllable-generation) (136 papers) - Controllable video generation with motion, camera, pose, or layout guidance
- [Human & Character Animation](#human-&-character-animation) (23 papers) - Human-centric video generation including talking heads, dance, and character animation
- [Image-to-Video Generation](#image-to-video-generation) (42 papers) - Methods for animating still images into videos
- [Long Video Generation](#long-video-generation) (112 papers) - Generating temporally consistent long-form videos beyond short clips
- [Personalization & Customization](#personalization-&-customization) (83 papers) - Personalized video generation with custom subjects, identities, or styles
- [Physical Understanding](#physical-understanding) (144 papers) - Physics-aware video generation and dynamics modeling
- [Surveys & Benchmarks](#surveys-&-benchmarks) (201 papers) - Survey papers, benchmarks, and evaluation metrics for video generation
- [Text-to-Video Generation](#text-to-video-generation) (59 papers) - Foundation models and methods for generating videos from text prompts
- [Video Editing](#video-editing) (30 papers) - Diffusion-based video editing, style transfer, and manipulation
- [Video Inpainting & Completion](#video-inpainting-&-completion) (6 papers) - Video inpainting, completion, outpainting, and temporal prediction
- [Video Super-Resolution & Enhancement](#video-super-resolution-&-enhancement) (61 papers) - Video quality improvement, upscaling, restoration, and frame interpolation
- [World Models & Simulation](#world-models-&-simulation) (95 papers) - Video generation as world simulators and interactive environment generation



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
  Keywords: novel view, diffusion model, video diffusion, dit, distillation  
- **[MultiWorld: Scalable Multi-Agent Multi-View Video World Models](https://arxiv.org/abs/2604.18564v2)**  
  Authors: Haoyu Wu, Jiwen Yu, Yingtian Zou, Xihui Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.18564v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://multi-world.github.io)  
  Keywords: multi-view video, video generation, world model, action-conditioned, dynamics, dit  
- **[ArtifactWorld: Scaling 3D Gaussian Splatting Artifact Restoration via Video Generation Models](https://arxiv.org/abs/2604.12251v1)**  
  Authors: Xinliang Wang, Yifeng Shi, Zhenyu Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.12251v1.pdf)  
  Keywords: novel view, video diffusion, video generation  
- **[Rays as Pixels: Learning A Joint Distribution of Videos and Camera Trajectories](https://arxiv.org/abs/2604.09429v2)**  
  Authors: Wonbong Jang, Shikun Liu, Soubhik Sanyal, Juan Camilo Perez, Kam Woh Ng, Sanskar Agrawal, Juan-Manuel Perez-Rua, Yiannis Douratsos, Tao Xiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.09429v2.pdf)  
  Keywords: novel view, diffusion model, trajectory, video diffusion, video generation, dit  
- **[Novel View Synthesis as Video Completion](https://arxiv.org/abs/2604.08500v1)**  
  Authors: Qi Wu, Khiem Vuong, Minsik Jeon, Srinivasa Narasimhan, Deva Ramanan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08500v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://frame-crafter.github.io)  
  Keywords: novel view, video completion, diffusion model, video diffusion, benchmark  
- **[Multi-View Video Diffusion Policy: A 3D Spatio-Temporal-Aware Video Action Model](https://arxiv.org/abs/2604.03181v1)**  
  Authors: Peiyan Li, Yixiang Chen, Yuan Xu, Jiabing Yang, Xiangnan Wu, Jun Guo, Nan Sun, Long Qian, Xinghang Li, Xin Xiao, Jing Liu, Nianfeng Liu, Tao Kong, Yan Huang, Liang Wang, Tieniu Tan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.03181v1.pdf)  
  Keywords: multi-view video, video diffusion, efficient, dynamics, dit  
- **[Control-DINO: Feature Space Conditioning for Controllable Image-to-Video Diffusion](https://arxiv.org/abs/2604.01761v1)**  
  Authors: Edoardo A. Dominici, Thomas Deixelberger, Konstantinos Vardis, Markus Steinberger  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01761v1.pdf)  
  Keywords: novel view, controllable, diffusion model, architecture, simulation, video diffusion, image-to-video, style, dit  
- **[HVG-3D: Bridging Real and Simulation Domains for 3D-Conditional Hand-Object Interaction Video Synthesis](https://arxiv.org/abs/2604.03305v1)**  
  Authors: Mingjin Chen, Junhao Chen, Zhaoxin Fan, Yujian Lee, Zichen Dang, Lili Wang, Yawen Cui, Lap-Pui Chau, Yi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.03305v1.pdf)  
  Keywords: 3d-aware, architecture, simulation, video generation, video synthesis, dit  
- **[I3DM: Implicit 3D-aware Memory Retrieval and Injection for Consistent Video Scene Generation](https://arxiv.org/abs/2603.23413v1)**  
  Authors: Jia Li, Han Yan, Yihang Chen, Siqi Li, Xibin Song, Yifu Wang, Jianfei Cai, Tien-Tsin Wong, Pan Ji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23413v1.pdf)  
  Keywords: novel view, 3d-aware, camera control, video generation, dit  
- **[GO-Renderer: Generative Object Rendering with 3D-aware Controllable Video Diffusion Models](https://arxiv.org/abs/2603.23246v1)**  
  Authors: Zekai Gu, Shuoxuan Feng, Yansong Wang, Hanzhuo Huang, Zhongshuo Du, Chengfeng Zhao, Chengwei Ren, Peng Wang, Yuan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.23246v1.pdf)  
  Keywords: 3d-aware, controllable, diffusion model, video diffusion, efficient, dit  

### Applications

- **[CityRAG: Stepping Into a City via Spatially-Grounded Video Generation](https://arxiv.org/abs/2604.19741v1)**  
  Authors: Gene Chou, Charles Herrmann, Kyle Genova, Boyang Deng, Songyou Peng, Bharath Hariharan, Jason Y. Zhang, Noah Snavely, Philipp Henzler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19741v1.pdf)  
  Keywords: dit, i2v, simulation, physical, video generation, robotics, t2v, autonomous driving  
- **[CoInteract: Physically-Consistent Human-Object Interaction Video Synthesis via Spatially-Structured Co-Generation](https://arxiv.org/abs/2604.19636v1)**  
  Authors: Xiangyang Luo, Xiaozhe Xin, Tao Feng, Xu Guo, Meiguang Jin, Junfeng Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19636v1.pdf)  
  Keywords: diffusion model, physical, diffusion transformer, advertising, video synthesis, dit  
- **[AutoAWG: Adverse Weather Generation with Adaptive Multi-Controls for Automotive Videos](https://arxiv.org/abs/2604.18993v1)**  
  Authors: Jiagao Hu, Daiguo Zhou, Danzhen Fu, Fuhao Li, Zepeng Wang, Fei Wang, Wenhua Liao, Jiayi Xie, Haiyang Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.18993v1.pdf) | [![GitHub](https://img.shields.io/github/stars/higherhu/AutoAWG?style=social)](https://github.com/higherhu/AutoAWG)  
  Keywords: temporal consistency, controllable, video generation, style, dit, autonomous driving  
- **[Implicit Neural Representations: A Signal Processing Perspective](https://arxiv.org/abs/2604.15047v1)**  
  Authors: Dhananjaya Jayasundara, Vishal M. Patel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.15047v1.pdf)  
  Keywords: concept, medical  
- **[Flow of Truth: Proactive Temporal Forensics for Image-to-Video Generation](https://arxiv.org/abs/2604.15003v1)**  
  Authors: Yuzhuo Chen, Zehua Ma, Han Fang, Hengyi Wang, Guanjie Wang, Weiming Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.15003v1.pdf)  
  Keywords: i2v, video generation, creative, image-to-video, dit  
- **[Seedance 2.0: Advancing Video Generation for World Complexity](https://arxiv.org/abs/2604.14148v1)**  
  Authors: Team Seedance, De Chen, Liyang Chen, Xin Chen, Ying Chen, Zhuo Chen, Zhuowei Chen, Feng Cheng, Tianheng Cheng, Yufeng Cheng, Mojie Chi, Xuyan Chi, Jian Cong, Qinpeng Cui, Fei Ding, Qide Dong, Yujiao Du, Haojie Duanmu, Junliang Fan, Jiarui Fang, Jing Fang, Zetao Fang, Chengjian Feng, Yu Gao, Diandian Gu, Dong Guo, Hanzhong Guo, Qiushan Guo, Boyang Hao, Hongxiang Hao, Haoxun He, Jiaao He, Qian He, Tuyen Hoang, Heng Hu, Ruoqing Hu, Yuxiang Hu, Jiancheng Huang, Weilin Huang, Zhaoyang Huang, Zhongyi Huang, Jishuo Jin, Ming Jing, Ashley Kim, Shanshan Lao, Yichong Leng, Bingchuan Li, Gen Li, Haifeng Li, Huixia Li, Jiashi Li, Ming Li, Xiaojie Li, Xingxing Li, Yameng Li, Yiying Li, Yu Li, Yueyan Li, Chao Liang, Han Liang, Jianzhong Liang, Ying Liang, Wang Liao, J. H. Lien, Shanchuan Lin, Xi Lin, Feng Ling, Yue Ling, Fangfang Liu, Jiawei Liu, Jihao Liu, Jingtuo Liu, Shu Liu, Sichao Liu, Wei Liu, Xue Liu, Zuxi Liu, Ruijie Lu, Lecheng Lyu, Jingting Ma, Tianxiang Ma, Xiaonan Nie, Jingzhe Ning, Junjie Pan, Xitong Pan, Ronggui Peng, Xueqiong Qu, Yuxi Ren, Yuchen Shen, Guang Shi, Lei Shi, Yinglong Song, Fan Sun, Li Sun, Renfei Sun, Wenjing Tang, Boyang Tao, Zirui Tao, Dongliang Wang, Feng Wang, Hulin Wang, Ke Wang, Qingyi Wang, Rui Wang, Shuai Wang, Shulei Wang, Weichen Wang, Xuanda Wang, Yanhui Wang, Yue Wang, Yuping Wang, Yuxuan Wang, Zijie Wang, Ziyu Wang, Guoqiang Wei, Meng Wei, Di Wu, Guohong Wu, Hanjie Wu, Huachao Wu, Jian Wu, Jie Wu, Ruolan Wu, Shaojin Wu, Xiaohu Wu, Xinglong Wu, Yonghui Wu, Ruiqi Xia, Xin Xia, Xuefeng Xiao, Shuang Xu, Bangbang Yang, Jiaqi Yang, Runkai Yang, Tao Yang, Yihang Yang, Zhixian Yang, Ziyan Yang, Fulong Ye, Bingqian Yi, Xing Yin, Yongbin You, Linxiao Yuan, Weihong Zeng, Xuejiao Zeng, Yan Zeng, Siyu Zhai, Zhonghua Zhai, Bowen Zhang, Chenlin Zhang, Heng Zhang, Jun Zhang, Manlin Zhang, Peiyuan Zhang, Shuo Zhang, Xiaohe Zhang, Xiaoying Zhang, Xinyan Zhang, Xinyi Zhang, Yichi Zhang, Zixiang Zhang, Haiyu Zhao, Huating Zhao, Liming Zhao, Yian Zhao, Guangcong Zheng, Jianbin Zheng, Xiaozheng Zheng, Zerong Zheng, Kuan Zhu, Feilong Zuo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.14148v1.pdf)  
  Keywords: evaluation, architecture, video generation, creative, efficient, multi-modal, dit  
- **[Lyra 2.0: Explorable Generative 3D Worlds](https://arxiv.org/abs/2604.13036v1)**  
  Authors: Tianchang Shen, Sherwin Bahmani, Kai He, Sangeetha Grama Srinivasan, Tianshi Cao, Jiawei Ren, Ruilong Li, Zian Wang, Nicholas Sharp, Zan Gojcic, Sanja Fidler, Jiahui Huang, Huan Ling, Jun Gao, Xuanchi Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.13036v1.pdf)  
  Keywords: autoregressive, simulation, creative, video generation  
- **[Camera Artist: A Multi-Agent Framework for Cinematic Language Storytelling Video Generation](https://arxiv.org/abs/2604.09195v1)**  
  Authors: Haobo Hu, Qi Mao, Yuanhang Li, Libiao Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.09195v1.pdf)  
  Keywords: film, video generation  
- **[LMGenDrive: Bridging Multimodal Understanding and Generative World Modeling for End-to-End Driving](https://arxiv.org/abs/2604.08719v1)**  
  Authors: Hao Shao, Letian Wang, Yang Zhou, Yuxuan Hu, Zhuofan Zong, Steven L. Waslander, Wei Zhan, Hongsheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08719v1.pdf)  
  Keywords: video prediction, autoregressive, benchmark, video generation, world model, autonomous driving  
- **[Lighting-grounded Video Generation with Renderer-based Agent Reasoning](https://arxiv.org/abs/2604.07966v1)**  
  Authors: Ziqi Cai, Taoyu Yang, Zheng Chang, Si Li, Han Jiang, Shuchen Weng, Boxin Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07966v1.pdf)  
  Keywords: controllable, diffusion model, temporal consistency, trajectory, video diffusion, video generation, layout, video synthesis, image-to-video, film, dit, video-to-video  

### Architecture & Efficiency

*Showing the latest 50 out of 354 papers*

- **[AnyRecon: Arbitrary-View 3D Reconstruction with Video Diffusion Model](https://arxiv.org/abs/2604.19747v1)**  
  Authors: Yutian Chen, Shi Guo, Renbiao Jin, Tianshuo Yang, Xin Cai, Yawen Luo, Mingxin Yang, Mulin Yu, Linning Xu, Tianfan Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19747v1.pdf)  
  Keywords: novel view, diffusion model, video diffusion, dit, distillation  
- **[CityRAG: Stepping Into a City via Spatially-Grounded Video Generation](https://arxiv.org/abs/2604.19741v1)**  
  Authors: Gene Chou, Charles Herrmann, Kyle Genova, Boyang Deng, Songyou Peng, Bharath Hariharan, Jason Y. Zhang, Noah Snavely, Philipp Henzler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19741v1.pdf)  
  Keywords: dit, i2v, simulation, physical, video generation, robotics, t2v, autonomous driving  
- **[UniT: Toward a Unified Physical Language for Human-to-Humanoid Policy Learning and World Modeling](https://arxiv.org/abs/2604.19734v1)**  
  Authors: Boyu Chen, Yi Chen, Lu Qiu, Jerry Bai, Yuying Ge, Yixiao Ge  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19734v1.pdf)  
  Keywords: simulation, physical, benchmark, video generation, world model, dynamics, dit  
- **[Face Anything: 4D Face Reconstruction from Any Image Sequence](https://arxiv.org/abs/2604.19702v1)**  
  Authors: Umut Kocasari, Simon Giebenhain, Richard Shaw, Matthias Nießner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19702v1.pdf)  
  Keywords: architecture, benchmark  
- **[MMControl: Unified Multi-Modal Control for Joint Audio-Video Generation](https://arxiv.org/abs/2604.19679v1)**  
  Authors: Liyang Li, Wen Wang, Canyu Zhao, Tianjian Feng, Zhiyue Zhao, Hao Chen, Chunhua Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19679v1.pdf)  
  Keywords: controllable, identity, diffusion transformer, video diffusion, video generation, layout, multi-modal, dit  
- **[CoInteract: Physically-Consistent Human-Object Interaction Video Synthesis via Spatially-Structured Co-Generation](https://arxiv.org/abs/2604.19636v1)**  
  Authors: Xiangyang Luo, Xiaozhe Xin, Tao Feng, Xu Guo, Meiguang Jin, Junfeng Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19636v1.pdf)  
  Keywords: diffusion model, physical, diffusion transformer, advertising, video synthesis, dit  
- **[TS-Attn: Temporal-wise Separable Attention for Multi-Event Video Generation](https://arxiv.org/abs/2604.19473v1)**  
  Authors: Hongyu Zhang, Yufan Deng, Zilin Pan, Peng-Tao Jiang, Bo Li, Qibin Hou, Zhiyang Dou, Zhen Dong, Daquan Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19473v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Hong-yu-Zhang/TS-Attn?style=social)](https://github.com/Hong-yu-Zhang/TS-Attn)  
  Keywords: dit, temporal consistency, video generation, image-to-video, text-to-video, t2v  
- **[Learning to Credit the Right Steps: Objective-aware Process Optimization for Visual Generation](https://arxiv.org/abs/2604.19234v1)**  
  Authors: Rui Li, Ke Hao, Yuanzhi Liang, Haibin Huang, Chi Zhang, YunGu, XueLong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19234v1.pdf)  
  Keywords: evaluation, trajectory, video generation, denoising, dit  
- **[Attention-based Multi-modal Deep Learning Model of Spatio-temporal Crop Yield Prediction with Satellite, Soil and Climate Data](https://arxiv.org/abs/2604.19217v1)**  
  Authors: Gopal Krishna Shyam, Ila Chandrakar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19217v1.pdf)  
  Keywords: multi-modal, dit, architecture  
- **[AutoAWG: Adverse Weather Generation with Adaptive Multi-Controls for Automotive Videos](https://arxiv.org/abs/2604.18993v1)**  
  Authors: Jiagao Hu, Daiguo Zhou, Danzhen Fu, Fuhao Li, Zepeng Wang, Fei Wang, Wenhua Liao, Jiayi Xie, Haiyang Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.18993v1.pdf) | [![GitHub](https://img.shields.io/github/stars/higherhu/AutoAWG?style=social)](https://github.com/higherhu/AutoAWG)  
  Keywords: temporal consistency, controllable, video generation, style, dit, autonomous driving  

### Audio & Multi-modal

- **[MMControl: Unified Multi-Modal Control for Joint Audio-Video Generation](https://arxiv.org/abs/2604.19679v1)**  
  Authors: Liyang Li, Wen Wang, Canyu Zhao, Tianjian Feng, Zhiyue Zhao, Hao Chen, Chunhua Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19679v1.pdf)  
  Keywords: controllable, identity, diffusion transformer, video diffusion, video generation, layout, multi-modal, dit  
- **[Attention-based Multi-modal Deep Learning Model of Spatio-temporal Crop Yield Prediction with Satellite, Soil and Climate Data](https://arxiv.org/abs/2604.19217v1)**  
  Authors: Gopal Krishna Shyam, Ila Chandrakar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19217v1.pdf)  
  Keywords: multi-modal, dit, architecture  
- **[OmniHuman: A Large-scale Dataset and Benchmark for Human-Centric Video Generation](https://arxiv.org/abs/2604.18326v1)**  
  Authors: Lei Zhu, Xing Cai, Yingjie Chen, Yiheng Li, Binxin Yang, Hao Liu, Jie Chen, Chen Li, Jing LYu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.18326v1.pdf)  
  Keywords: evaluation, physical, benchmark, video generation, video synthesis, multi-modal  
- **[TurboTalk: Progressive Distillation for One-Step Audio-Driven Talking Avatar Generation](https://arxiv.org/abs/2604.14580v1)**  
  Authors: Xiangyu Liu, Feng Gao, Xiaomei Zhang, Yong Zhang, Xiaoming Wei, Zhen Lei, Xiangyu Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.14580v1.pdf)  
  Keywords: diffusion model, video diffusion, avatar, audio-driven, denoising, distillation  
- **[Seedance 2.0: Advancing Video Generation for World Complexity](https://arxiv.org/abs/2604.14148v1)**  
  Authors: Team Seedance, De Chen, Liyang Chen, Xin Chen, Ying Chen, Zhuo Chen, Zhuowei Chen, Feng Cheng, Tianheng Cheng, Yufeng Cheng, Mojie Chi, Xuyan Chi, Jian Cong, Qinpeng Cui, Fei Ding, Qide Dong, Yujiao Du, Haojie Duanmu, Junliang Fan, Jiarui Fang, Jing Fang, Zetao Fang, Chengjian Feng, Yu Gao, Diandian Gu, Dong Guo, Hanzhong Guo, Qiushan Guo, Boyang Hao, Hongxiang Hao, Haoxun He, Jiaao He, Qian He, Tuyen Hoang, Heng Hu, Ruoqing Hu, Yuxiang Hu, Jiancheng Huang, Weilin Huang, Zhaoyang Huang, Zhongyi Huang, Jishuo Jin, Ming Jing, Ashley Kim, Shanshan Lao, Yichong Leng, Bingchuan Li, Gen Li, Haifeng Li, Huixia Li, Jiashi Li, Ming Li, Xiaojie Li, Xingxing Li, Yameng Li, Yiying Li, Yu Li, Yueyan Li, Chao Liang, Han Liang, Jianzhong Liang, Ying Liang, Wang Liao, J. H. Lien, Shanchuan Lin, Xi Lin, Feng Ling, Yue Ling, Fangfang Liu, Jiawei Liu, Jihao Liu, Jingtuo Liu, Shu Liu, Sichao Liu, Wei Liu, Xue Liu, Zuxi Liu, Ruijie Lu, Lecheng Lyu, Jingting Ma, Tianxiang Ma, Xiaonan Nie, Jingzhe Ning, Junjie Pan, Xitong Pan, Ronggui Peng, Xueqiong Qu, Yuxi Ren, Yuchen Shen, Guang Shi, Lei Shi, Yinglong Song, Fan Sun, Li Sun, Renfei Sun, Wenjing Tang, Boyang Tao, Zirui Tao, Dongliang Wang, Feng Wang, Hulin Wang, Ke Wang, Qingyi Wang, Rui Wang, Shuai Wang, Shulei Wang, Weichen Wang, Xuanda Wang, Yanhui Wang, Yue Wang, Yuping Wang, Yuxuan Wang, Zijie Wang, Ziyu Wang, Guoqiang Wei, Meng Wei, Di Wu, Guohong Wu, Hanjie Wu, Huachao Wu, Jian Wu, Jie Wu, Ruolan Wu, Shaojin Wu, Xiaohu Wu, Xinglong Wu, Yonghui Wu, Ruiqi Xia, Xin Xia, Xuefeng Xiao, Shuang Xu, Bangbang Yang, Jiaqi Yang, Runkai Yang, Tao Yang, Yihang Yang, Zhixian Yang, Ziyan Yang, Fulong Ye, Bingqian Yi, Xing Yin, Yongbin You, Linxiao Yuan, Weihong Zeng, Xuejiao Zeng, Yan Zeng, Siyu Zhai, Zhonghua Zhai, Bowen Zhang, Chenlin Zhang, Heng Zhang, Jun Zhang, Manlin Zhang, Peiyuan Zhang, Shuo Zhang, Xiaohe Zhang, Xiaoying Zhang, Xinyan Zhang, Xinyi Zhang, Yichi Zhang, Zixiang Zhang, Haiyu Zhao, Huating Zhao, Liming Zhao, Yian Zhao, Guangcong Zheng, Jianbin Zheng, Xiaozheng Zheng, Zerong Zheng, Kuan Zhu, Feilong Zuo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.14148v1.pdf)  
  Keywords: evaluation, architecture, video generation, creative, efficient, multi-modal, dit  
- **[HY-World 2.0: A Multi-Modal World Model for Reconstructing, Generating, and Simulating 3D Worlds](https://arxiv.org/abs/2604.14268v1)**  
  Authors: Team HY-World, Chenjie Cao, Xuhui Zuo, Zhenwei Wang, Yisu Zhang, Junta Wu, Zhenyang Liu, Yuning Gong, Yang Liu, Bo Yuan, Chao Zhang, Coopers Li, Dongyuan Guo, Fan Yang, Haiyu Zhang, Hang Cao, Jianchen Zhu, Jiaxin Lin, Jie Xiao, Jihong Zhang, Junlin Yu, Lei Wang, Lifu Wang, Lilin Wang, Linus, Minghui Chen, Peng He, Penghao Zhao, Qi Chen, Rui Chen, Rui Shao, Sicong Liu, Wangchen Qin, Xiaochuan Niu, Xiang Yuan, Yi Sun, Yifei Tang, Yifu Sun, Yihang Lian, Yonghao Tan, Yuhong Liu, Yuyang Yin, Zhiyuan Min, Tengfei Wang, Chunchao Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.14268v1.pdf)  
  Keywords: interactive, architecture, trajectory, benchmark, world model, efficient, multi-modal  
- **[Deepfakes at Face Value: Image and Authority](https://arxiv.org/abs/2604.12490v1)**  
  Authors: James Ravi Kirkpatrick  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.12490v1.pdf)  
  Keywords: identity, simulation, sound  
- **[Beyond Monologue: Interactive Talking-Listening Avatar Generation with Conversational Audio Context-Aware Kernels](https://arxiv.org/abs/2604.10367v1)**  
  Authors: Yuzhe Weng, Haotian Wang, Xinyi Yu, Xiaoyan Wu, Haoran Xu, Shan He, Jun Du  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.10367v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://warmcongee.github.io/beyond-monologue)  
  Keywords: interactive, physical, video generation, avatar, audio-driven, dynamics  
- **[Tora3: Trajectory-Guided Audio-Video Generation with Physical Coherence](https://arxiv.org/abs/2604.09057v2)**  
  Authors: Junchao Liao, Zhenghao Zhang, Xiangyu Meng, Litao Li, Ziying Zhang, Siyu Zhu, Long Qin, Weizhi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.09057v2.pdf)  
  Keywords: trajectory, physical, video generation, flow matching, dit, sound  
- **[SceneScribe-1M: A Large-Scale Video Dataset with Comprehensive Geometric and Semantic Annotations](https://arxiv.org/abs/2604.07990v1)**  
  Authors: Yunnan Wang, Kecheng Zheng, Jianyuan Wang, Minghao Chen, David Novotny, Christian Rupprecht, Yinghao Xu, Xing Zhu, Wenjun Zeng, Xin Jin, Yujun Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07990v1.pdf)  
  Keywords: controllable, camera control, benchmark, video generation, video synthesis, text-to-video, multi-modal  

### Controllable Generation

*Showing the latest 50 out of 136 papers*

- **[ReImagine: Rethinking Controllable High-Quality Human Video Generation via Image-First Synthesis](https://arxiv.org/abs/2604.19720v1)**  
  Authors: Zhengwentai Sun, Keru Zheng, Chenghong Li, Hongjie Liao, Xihe Yang, Heyuan Li, Yihao Zhi, Shuliang Ning, Shuguang Cui, Xiaoguang Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19720v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Taited/ReImagine?style=social)](https://github.com/Taited/ReImagine)  
  Keywords: controllable, diffusion model, temporal consistency, video diffusion, video generation, video synthesis  
- **[MMControl: Unified Multi-Modal Control for Joint Audio-Video Generation](https://arxiv.org/abs/2604.19679v1)**  
  Authors: Liyang Li, Wen Wang, Canyu Zhao, Tianjian Feng, Zhiyue Zhao, Hao Chen, Chunhua Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19679v1.pdf)  
  Keywords: controllable, identity, diffusion transformer, video diffusion, video generation, layout, multi-modal, dit  
- **[Learning to Credit the Right Steps: Objective-aware Process Optimization for Visual Generation](https://arxiv.org/abs/2604.19234v1)**  
  Authors: Rui Li, Ke Hao, Yuanzhi Liang, Haibin Huang, Chi Zhang, YunGu, XueLong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19234v1.pdf)  
  Keywords: evaluation, trajectory, video generation, denoising, dit  
- **[AutoAWG: Adverse Weather Generation with Adaptive Multi-Controls for Automotive Videos](https://arxiv.org/abs/2604.18993v1)**  
  Authors: Jiagao Hu, Daiguo Zhou, Danzhen Fu, Fuhao Li, Zepeng Wang, Fei Wang, Wenhua Liao, Jiayi Xie, Haiyang Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.18993v1.pdf) | [![GitHub](https://img.shields.io/github/stars/higherhu/AutoAWG?style=social)](https://github.com/higherhu/AutoAWG)  
  Keywords: temporal consistency, controllable, video generation, style, dit, autonomous driving  
- **[ViPS: Video-informed Pose Spaces for Auto-Rigged Meshes](https://arxiv.org/abs/2604.17623v1)**  
  Authors: Honglin Chen, Karran Pandey, Rundi Wu, Matheus Gadelha, Yannick Hold-Geoffroy, Ayush Tewari, Niloy J. Mitra, Changxi Zheng, Paul Guerrero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.17623v1.pdf)  
  Keywords: evaluation, controllable, diffusion model, video diffusion, physical, dit  
- **[DreamShot: Personalized Storyboard Synthesis with Video Diffusion Prior](https://arxiv.org/abs/2604.17195v1)**  
  Authors: Junjia Huang, Binbin Yang, Pengxiang Yan, Jiyang Liu, Bin Xia, Zhao Wang, Yitong Wang, Liang Lin, Guanbin Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.17195v1.pdf)  
  Keywords: temporal consistency, controllable, diffusion model, identity, video diffusion, dit  
- **[Efficient Video Diffusion Models: Advancements and Challenges](https://arxiv.org/abs/2604.15911v1)**  
  Authors: Shitong Shao, Lichen Bai, Pengfei Wan, James Kwok, Zeke Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.15911v1.pdf)  
  Keywords: evaluation, survey, diffusion model, trajectory, video diffusion, acceleration, video synthesis, denoising, efficient, distillation  
- **[Controllable Video Object Insertion via Multiview Priors](https://arxiv.org/abs/2604.14556v1)**  
  Authors: Xia Qi, Peishan Cong, Yichen Yao, Ziyi Wang, Yaoqin Ye, Yuexin Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.14556v1.pdf)  
  Keywords: dit, identity, controllable, video generation  
- **[HY-World 2.0: A Multi-Modal World Model for Reconstructing, Generating, and Simulating 3D Worlds](https://arxiv.org/abs/2604.14268v1)**  
  Authors: Team HY-World, Chenjie Cao, Xuhui Zuo, Zhenwei Wang, Yisu Zhang, Junta Wu, Zhenyang Liu, Yuning Gong, Yang Liu, Bo Yuan, Chao Zhang, Coopers Li, Dongyuan Guo, Fan Yang, Haiyu Zhang, Hang Cao, Jianchen Zhu, Jiaxin Lin, Jie Xiao, Jihong Zhang, Junlin Yu, Lei Wang, Lifu Wang, Lilin Wang, Linus, Minghui Chen, Peng He, Penghao Zhao, Qi Chen, Rui Chen, Rui Shao, Sicong Liu, Wangchen Qin, Xiaochuan Niu, Xiang Yuan, Yi Sun, Yifei Tang, Yifu Sun, Yihang Lian, Yonghao Tan, Yuhong Liu, Yuyang Yin, Zhiyuan Min, Tengfei Wang, Chunchao Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.14268v1.pdf)  
  Keywords: interactive, architecture, trajectory, benchmark, world model, efficient, multi-modal  
- **[Ride the Wave: Precision-Allocated Sparse Attention for Smooth Video Generation](https://arxiv.org/abs/2604.12219v1)**  
  Authors: Wentai Zhang, Ronghui Xi, Shiyao Peng, Jiayu Huang, Haoran Luo, Zichen Tang, Haihong E  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.12219v1.pdf)  
  Keywords: evaluation, diffusion model, trajectory, diffusion transformer, video diffusion, video generation, acceleration, efficient  

### Human & Character Animation

- **[Prompt-to-Gesture: Measuring the Capabilities of Image-to-Video Deictic Gesture Generation](https://arxiv.org/abs/2604.14953v1)**  
  Authors: Hassan Ali, Doreen Jirak, Luca Müller, Stefan Wermter  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.14953v1.pdf)  
  Keywords: dit, image-to-video, gesture, video generation  
- **[TurboTalk: Progressive Distillation for One-Step Audio-Driven Talking Avatar Generation](https://arxiv.org/abs/2604.14580v1)**  
  Authors: Xiangyu Liu, Feng Gao, Xiaomei Zhang, Yong Zhang, Xiaoming Wei, Zhen Lei, Xiangyu Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.14580v1.pdf)  
  Keywords: diffusion model, video diffusion, avatar, audio-driven, denoising, distillation  
- **[Beyond Monologue: Interactive Talking-Listening Avatar Generation with Conversational Audio Context-Aware Kernels](https://arxiv.org/abs/2604.10367v1)**  
  Authors: Yuzhe Weng, Haotian Wang, Xinyi Yu, Xiaoyan Wu, Haoran Xu, Shan He, Jun Du  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.10367v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://warmcongee.github.io/beyond-monologue)  
  Keywords: interactive, physical, video generation, avatar, audio-driven, dynamics  
- **[HumANDiff: Articulated Noise Diffusion for Motion-Consistent Human Video Generation](https://arxiv.org/abs/2604.05961v1)**  
  Authors: Tao Hu, Varun Jampani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.05961v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://taohuumd.github.io/projects/HumANDiff)  
  Keywords: human motion, controllable, diffusion model, architecture, video diffusion, physical, video generation, motion control, dynamics, video synthesis, image-to-video, style, dit, physics  
- **[Vanast: Virtual Try-On with Human Image Animation via Synthetic Triplet Supervision](https://arxiv.org/abs/2604.04934v1)**  
  Authors: Hyunsoo Cha, Wonjung Woo, Byungjun Kim, Hanbyul Joo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04934v1.pdf)  
  Keywords: architecture, identity, image animation, diffusion transformer, video diffusion, virtual try-on, human animation  
- **[DynaVid: Learning to Generate Highly Dynamic Videos using Synthetic Motion Data](https://arxiv.org/abs/2604.01666v1)**  
  Authors: Wonjoon Jin, Jiyun Won, Janghyeok Han, Qi Dai, Chong Luo, Seung-Hwan Baek, Sunghyun Cho  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.01666v1.pdf)  
  Keywords: human motion, diffusion model, video diffusion, motion control, video synthesis, dit  
- **[FlashSign: Pose-Free Guidance for Efficient Sign Language Video Generation](https://arxiv.org/abs/2603.27915v1)**  
  Authors: Liuzhou Zhang, Zeyu Zhang, Biao Wu, Luyao Tang, Zirui Song, Hongyang He, Renda Han, Guangzhen Yao, Huacan Wang, Ronghao Chen, Xiuying Chen, Guan Huang, Zheng Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27915v1.pdf) | [![GitHub](https://img.shields.io/github/stars/AIGeeksGroup/FlashSign?style=social)](https://github.com/AIGeeksGroup/FlashSign)  
  Keywords: gesture, efficient, video generation  
- **[LOME: Learning Human-Object Manipulation with Action-Conditioned Egocentric World Model](https://arxiv.org/abs/2603.27449v1)**  
  Authors: Quankai Gao, Jiawei Yang, Qiangeng Xu, Le Chen, Yue Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.27449v1.pdf)  
  Keywords: dit, temporal consistency, gesture, physical, motion control, world model, text-to-video, action-conditioned, t2v, physics  
- **[RefAlign: Representation Alignment for Reference-to-Video Generation](https://arxiv.org/abs/2603.25743v1)**  
  Authors: Lei Wang, YuXin Song, Ge Wu, Haocheng Feng, Hang Zhou, Jingdong Wang, Yaxing Wang, jian Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.25743v1.pdf)  
  Keywords: controllable, identity, diffusion transformer, benchmark, video generation, advertising, video synthesis, virtual try-on, dit  
- **[Anti-I2V: Safeguarding your photos from malicious image-to-video generation](https://arxiv.org/abs/2603.24570v1)**  
  Authors: Duc Vu, Anh Nguyen, Chi Tran, Anh Tran  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.24570v1.pdf)  
  Keywords: i2v, diffusion model, temporal consistency, architecture, diffusion transformer, video diffusion, video generation, image-to-video, denoising, dit, human animation  

### Image-to-Video Generation

- **[CityRAG: Stepping Into a City via Spatially-Grounded Video Generation](https://arxiv.org/abs/2604.19741v1)**  
  Authors: Gene Chou, Charles Herrmann, Kyle Genova, Boyang Deng, Songyou Peng, Bharath Hariharan, Jason Y. Zhang, Noah Snavely, Philipp Henzler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19741v1.pdf)  
  Keywords: dit, i2v, simulation, physical, video generation, robotics, t2v, autonomous driving  
- **[TS-Attn: Temporal-wise Separable Attention for Multi-Event Video Generation](https://arxiv.org/abs/2604.19473v1)**  
  Authors: Hongyu Zhang, Yufan Deng, Zilin Pan, Peng-Tao Jiang, Bo Li, Qibin Hou, Zhiyang Dou, Zhen Dong, Daquan Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19473v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Hong-yu-Zhang/TS-Attn?style=social)](https://github.com/Hong-yu-Zhang/TS-Attn)  
  Keywords: dit, temporal consistency, video generation, image-to-video, text-to-video, t2v  
- **[AnimationBench: Are Video Models Good at Character-Centric Animation?](https://arxiv.org/abs/2604.15299v1)**  
  Authors: Leyi Wu, Pengjun Fang, Kai Sun, Yazhou Xing, Yinwei Wu, Songsong Wang, Ziqi Huang, Dan Zhou, Yingqing He, Ying-Cong Chen, Qifeng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.15299v1.pdf)  
  Keywords: evaluation, i2v, benchmark, video generation, image-to-video, style  
- **[Flow of Truth: Proactive Temporal Forensics for Image-to-Video Generation](https://arxiv.org/abs/2604.15003v1)**  
  Authors: Yuzhuo Chen, Zehua Ma, Han Fang, Hengyi Wang, Guanjie Wang, Weiming Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.15003v1.pdf)  
  Keywords: i2v, video generation, creative, image-to-video, dit  
- **[Prompt-to-Gesture: Measuring the Capabilities of Image-to-Video Deictic Gesture Generation](https://arxiv.org/abs/2604.14953v1)**  
  Authors: Hassan Ali, Doreen Jirak, Luca Müller, Stefan Wermter  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.14953v1.pdf)  
  Keywords: dit, image-to-video, gesture, video generation  
- **[ARGen: Affect-Reinforced Generative Augmentation towards Vision-based Dynamic Emotion Perception](https://arxiv.org/abs/2604.12255v1)**  
  Authors: Huanzhen Wang, Ziheng Zhou, Jiaqi Song, Li He, Yunshi Lan, Yan Wang, Wenqiang Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.12255v1.pdf)  
  Keywords: dit, image-to-video, video diffusion, dynamics  
- **[Immune2V: Image Immunization Against Dual-Stream Image-to-Video Generation](https://arxiv.org/abs/2604.10837v1)**  
  Authors: Zeqian Long, Ozgur Kara, Haotian Xue, Yongxin Chen, James M. Rehg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.10837v1.pdf)  
  Keywords: i2v, trajectory, video generation, image-to-video, dit  
- **[Lighting-grounded Video Generation with Renderer-based Agent Reasoning](https://arxiv.org/abs/2604.07966v1)**  
  Authors: Ziqi Cai, Taoyu Yang, Zheng Chang, Si Li, Han Jiang, Shuchen Weng, Boxin Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07966v1.pdf)  
  Keywords: controllable, diffusion model, temporal consistency, trajectory, video diffusion, video generation, layout, video synthesis, image-to-video, film, dit, video-to-video  
- **[HumANDiff: Articulated Noise Diffusion for Motion-Consistent Human Video Generation](https://arxiv.org/abs/2604.05961v1)**  
  Authors: Tao Hu, Varun Jampani  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.05961v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://taohuumd.github.io/projects/HumANDiff)  
  Keywords: human motion, controllable, diffusion model, architecture, video diffusion, physical, video generation, motion control, dynamics, video synthesis, image-to-video, style, dit, physics  
- **[Vanast: Virtual Try-On with Human Image Animation via Synthetic Triplet Supervision](https://arxiv.org/abs/2604.04934v1)**  
  Authors: Hyunsoo Cha, Wonjung Woo, Byungjun Kim, Hanbyul Joo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04934v1.pdf)  
  Keywords: architecture, identity, image animation, diffusion transformer, video diffusion, virtual try-on, human animation  

### Long Video Generation

*Showing the latest 50 out of 112 papers*

- **[ReImagine: Rethinking Controllable High-Quality Human Video Generation via Image-First Synthesis](https://arxiv.org/abs/2604.19720v1)**  
  Authors: Zhengwentai Sun, Keru Zheng, Chenghong Li, Hongjie Liao, Xihe Yang, Heyuan Li, Yihao Zhi, Shuliang Ning, Shuguang Cui, Xiaoguang Han  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19720v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Taited/ReImagine?style=social)](https://github.com/Taited/ReImagine)  
  Keywords: controllable, diffusion model, temporal consistency, video diffusion, video generation, video synthesis  
- **[TS-Attn: Temporal-wise Separable Attention for Multi-Event Video Generation](https://arxiv.org/abs/2604.19473v1)**  
  Authors: Hongyu Zhang, Yufan Deng, Zilin Pan, Peng-Tao Jiang, Bo Li, Qibin Hou, Zhiyang Dou, Zhen Dong, Daquan Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19473v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Hong-yu-Zhang/TS-Attn?style=social)](https://github.com/Hong-yu-Zhang/TS-Attn)  
  Keywords: dit, temporal consistency, video generation, image-to-video, text-to-video, t2v  
- **[AutoAWG: Adverse Weather Generation with Adaptive Multi-Controls for Automotive Videos](https://arxiv.org/abs/2604.18993v1)**  
  Authors: Jiagao Hu, Daiguo Zhou, Danzhen Fu, Fuhao Li, Zepeng Wang, Fei Wang, Wenhua Liao, Jiayi Xie, Haiyang Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.18993v1.pdf) | [![GitHub](https://img.shields.io/github/stars/higherhu/AutoAWG?style=social)](https://github.com/higherhu/AutoAWG)  
  Keywords: temporal consistency, controllable, video generation, style, dit, autonomous driving  
- **[Video-Robin: Autoregressive Diffusion Planning for Intent-Grounded Video-to-Music Generation](https://arxiv.org/abs/2604.17656v1)**  
  Authors: Vaibhavi Lokegaonkar, Aryan Vijay Bhosale, Vishnu Raj, Gouthaman KV, Ramani Duraiswami, Lie Lu, Sreyan Ghosh, Dinesh Manocha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.17656v1.pdf)  
  Keywords: dit, autoregressive, diffusion transformer, benchmark  
- **[Speculative Decoding for Autoregressive Video Generation](https://arxiv.org/abs/2604.17397v1)**  
  Authors: Yuezhou Hu, Jintao Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.17397v1.pdf)  
  Keywords: autoregressive, video diffusion, video generation, streaming, acceleration, video synthesis, denoising, dit, distillation  
- **[DreamShot: Personalized Storyboard Synthesis with Video Diffusion Prior](https://arxiv.org/abs/2604.17195v1)**  
  Authors: Junjia Huang, Binbin Yang, Pengxiang Yan, Jiyang Liu, Bin Xia, Zhao Wang, Yitong Wang, Liang Lin, Guanbin Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.17195v1.pdf)  
  Keywords: temporal consistency, controllable, diffusion model, identity, video diffusion, dit  
- **[DiT as Real-Time Rerenderer: Streaming Video Stylization with Autoregressive Diffusion Transformer](https://arxiv.org/abs/2604.13509v1)**  
  Authors: Hengye Lyu, Zisu Li, Yue Hong, Yueting Weng, Jiaxin Shi, Hanwang Zhang, Chen Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.13509v1.pdf)  
  Keywords: interactive, autoregressive, diffusion transformer, video generation, streaming, denoising, style, distillation, dit, long video  
- **[Lyra 2.0: Explorable Generative 3D Worlds](https://arxiv.org/abs/2604.13036v1)**  
  Authors: Tianchang Shen, Sherwin Bahmani, Kai He, Sangeetha Grama Srinivasan, Tianshi Cao, Jiawei Ren, Ruilong Li, Zian Wang, Nicholas Sharp, Zan Gojcic, Sanja Fidler, Jiahui Huang, Huan Ling, Jun Gao, Xuanchi Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.13036v1.pdf)  
  Keywords: autoregressive, simulation, creative, video generation  
- **[Generative Refinement Networks for Visual Synthesis](https://arxiv.org/abs/2604.13030v1)**  
  Authors: Jian Han, Jinlai Liu, Jiahuan Wang, Bingyue Peng, Zehuan Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.13030v1.pdf)  
  Keywords: diffusion model, autoregressive, benchmark, video generation, text-to-video, efficient, dit  
- **[VideoFlexTok: Flexible-Length Coarse-to-Fine Video Tokenization](https://arxiv.org/abs/2604.12887v1)**  
  Authors: Andrei Atanov, Jesse Allardice, Roman Bachmann, Oğuzhan Fatih Kar, R Devon Hjelm, David Griffiths, Peter Fu, Afshin Dehghan, Amir Zamir  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.12887v1.pdf)  
  Keywords: long video, efficient, text-to-video, video generation  

### Personalization & Customization

*Showing the latest 50 out of 83 papers*

- **[MMControl: Unified Multi-Modal Control for Joint Audio-Video Generation](https://arxiv.org/abs/2604.19679v1)**  
  Authors: Liyang Li, Wen Wang, Canyu Zhao, Tianjian Feng, Zhiyue Zhao, Hao Chen, Chunhua Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19679v1.pdf)  
  Keywords: controllable, identity, diffusion transformer, video diffusion, video generation, layout, multi-modal, dit  
- **[AutoAWG: Adverse Weather Generation with Adaptive Multi-Controls for Automotive Videos](https://arxiv.org/abs/2604.18993v1)**  
  Authors: Jiagao Hu, Daiguo Zhou, Danzhen Fu, Fuhao Li, Zepeng Wang, Fei Wang, Wenhua Liao, Jiayi Xie, Haiyang Sun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.18993v1.pdf) | [![GitHub](https://img.shields.io/github/stars/higherhu/AutoAWG?style=social)](https://github.com/higherhu/AutoAWG)  
  Keywords: temporal consistency, controllable, video generation, style, dit, autonomous driving  
- **[DreamShot: Personalized Storyboard Synthesis with Video Diffusion Prior](https://arxiv.org/abs/2604.17195v1)**  
  Authors: Junjia Huang, Binbin Yang, Pengxiang Yan, Jiyang Liu, Bin Xia, Zhao Wang, Yitong Wang, Liang Lin, Guanbin Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.17195v1.pdf)  
  Keywords: temporal consistency, controllable, diffusion model, identity, video diffusion, dit  
- **[AnimationBench: Are Video Models Good at Character-Centric Animation?](https://arxiv.org/abs/2604.15299v1)**  
  Authors: Leyi Wu, Pengjun Fang, Kai Sun, Yazhou Xing, Yinwei Wu, Songsong Wang, Ziqi Huang, Dan Zhou, Yingqing He, Ying-Cong Chen, Qifeng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.15299v1.pdf)  
  Keywords: evaluation, i2v, benchmark, video generation, image-to-video, style  
- **[Implicit Neural Representations: A Signal Processing Perspective](https://arxiv.org/abs/2604.15047v1)**  
  Authors: Dhananjaya Jayasundara, Vishal M. Patel  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.15047v1.pdf)  
  Keywords: concept, medical  
- **[Controllable Video Object Insertion via Multiview Priors](https://arxiv.org/abs/2604.14556v1)**  
  Authors: Xia Qi, Peishan Cong, Yichen Yao, Ziyi Wang, Yaoqin Ye, Yuexin Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.14556v1.pdf)  
  Keywords: dit, identity, controllable, video generation  
- **[DiT as Real-Time Rerenderer: Streaming Video Stylization with Autoregressive Diffusion Transformer](https://arxiv.org/abs/2604.13509v1)**  
  Authors: Hengye Lyu, Zisu Li, Yue Hong, Yueting Weng, Jiaxin Shi, Hanwang Zhang, Chen Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.13509v1.pdf)  
  Keywords: interactive, autoregressive, diffusion transformer, video generation, streaming, denoising, style, distillation, dit, long video  
- **[Deepfakes at Face Value: Image and Authority](https://arxiv.org/abs/2604.12490v1)**  
  Authors: James Ravi Kirkpatrick  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.12490v1.pdf)  
  Keywords: identity, simulation, sound  
- **[LottieGPT: Tokenizing Vector Animation for Autoregressive Generation](https://arxiv.org/abs/2604.11792v1)**  
  Authors: Junhao Chen, Kejun Gao, Yuehan Cui, Mingze Sun, Mingjin Chen, Shaohui Wang, Xiaoxiao Long, Fei Ma, Qi Tian, Ruqi Huang, Hao Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.11792v1.pdf)  
  Keywords: autoregressive, video generation, layout, style, dit  
- **[Empowering Video Translation using Multimodal Large Language Models](https://arxiv.org/abs/2604.11283v1)**  
  Authors: Bingzheng QU, Kehai Chen, Xuefeng Bai, Min Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.11283v1.pdf)  
  Keywords: survey, controllable, identity, dit, video translation  

### Physical Understanding

*Showing the latest 50 out of 144 papers*

- **[CityRAG: Stepping Into a City via Spatially-Grounded Video Generation](https://arxiv.org/abs/2604.19741v1)**  
  Authors: Gene Chou, Charles Herrmann, Kyle Genova, Boyang Deng, Songyou Peng, Bharath Hariharan, Jason Y. Zhang, Noah Snavely, Philipp Henzler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19741v1.pdf)  
  Keywords: dit, i2v, simulation, physical, video generation, robotics, t2v, autonomous driving  
- **[UniT: Toward a Unified Physical Language for Human-to-Humanoid Policy Learning and World Modeling](https://arxiv.org/abs/2604.19734v1)**  
  Authors: Boyu Chen, Yi Chen, Lu Qiu, Jerry Bai, Yuying Ge, Yixiao Ge  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19734v1.pdf)  
  Keywords: simulation, physical, benchmark, video generation, world model, dynamics, dit  
- **[CoInteract: Physically-Consistent Human-Object Interaction Video Synthesis via Spatially-Structured Co-Generation](https://arxiv.org/abs/2604.19636v1)**  
  Authors: Xiangyang Luo, Xiaozhe Xin, Tao Feng, Xu Guo, Meiguang Jin, Junfeng Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19636v1.pdf)  
  Keywords: diffusion model, physical, diffusion transformer, advertising, video synthesis, dit  
- **[How Far Are Video Models from True Multimodal Reasoning?](https://arxiv.org/abs/2604.19193v1)**  
  Authors: Xiaotian Zhang, Jianhui Wei, Yuan Wang, Jie Tan, Yichen Li, Yan Zhang, Ziyi Chen, Daoan Zhang, Dezhi YU, Wei Xu, Songtao Jiang, Zuozhu Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19193v1.pdf)  
  Keywords: evaluation, interactive, simulation, physical, benchmark, video generation, physical simulation  
- **[RoboWM-Bench: A Benchmark for Evaluating World Models in Robotic Manipulation](https://arxiv.org/abs/2604.19092v1)**  
  Authors: Feng Jiang, Yang Chen, Kyle Xu, Yuchen Liu, Haifeng Wang, Zhenhao Shen, Jasper Lu, Shengze Huang, Yuanfei Wang, Chen Xie, Ruihai Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19092v1.pdf)  
  Keywords: evaluation, physical, benchmark, video generation, world model, dynamics  
- **[MultiWorld: Scalable Multi-Agent Multi-View Video World Models](https://arxiv.org/abs/2604.18564v2)**  
  Authors: Haoyu Wu, Jiwen Yu, Yingtian Zou, Xihui Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.18564v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://multi-world.github.io)  
  Keywords: multi-view video, video generation, world model, action-conditioned, dynamics, dit  
- **[OmniHuman: A Large-scale Dataset and Benchmark for Human-Centric Video Generation](https://arxiv.org/abs/2604.18326v1)**  
  Authors: Lei Zhu, Xing Cai, Yingjie Chen, Yiheng Li, Binxin Yang, Hao Liu, Jie Chen, Chen Li, Jing LYu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.18326v1.pdf)  
  Keywords: evaluation, physical, benchmark, video generation, video synthesis, multi-modal  
- **[ViPS: Video-informed Pose Spaces for Auto-Rigged Meshes](https://arxiv.org/abs/2604.17623v1)**  
  Authors: Honglin Chen, Karran Pandey, Rundi Wu, Matheus Gadelha, Yannick Hold-Geoffroy, Ayush Tewari, Niloy J. Mitra, Changxi Zheng, Paul Guerrero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.17623v1.pdf)  
  Keywords: evaluation, controllable, diffusion model, video diffusion, physical, dit  
- **[Long-CODE: Isolating Pure Long-Context as an Orthogonal Dimension in Video Evaluation](https://arxiv.org/abs/2604.17428v1)**  
  Authors: Zhijiang Tang, Jiaxin Qi, Bing Zhao, Jianqiang Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.17428v1.pdf)  
  Keywords: evaluation, benchmark, video generation, dynamics, dit  
- **[VibeFlow: Versatile Video Chroma-Lux Editing through Self-Supervised Learning](https://arxiv.org/abs/2604.13425v1)**  
  Authors: Yifan Li, Pei Cheng, Bin Fu, Shuai Yang, Jiaying Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.13425v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://lyf1212.github.io/VibeFlow-webpage)  
  Keywords: dit, physical, video generation  

### Surveys & Benchmarks

*Showing the latest 50 out of 201 papers*

- **[UniT: Toward a Unified Physical Language for Human-to-Humanoid Policy Learning and World Modeling](https://arxiv.org/abs/2604.19734v1)**  
  Authors: Boyu Chen, Yi Chen, Lu Qiu, Jerry Bai, Yuying Ge, Yixiao Ge  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19734v1.pdf)  
  Keywords: simulation, physical, benchmark, video generation, world model, dynamics, dit  
- **[Face Anything: 4D Face Reconstruction from Any Image Sequence](https://arxiv.org/abs/2604.19702v1)**  
  Authors: Umut Kocasari, Simon Giebenhain, Richard Shaw, Matthias Nießner  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19702v1.pdf)  
  Keywords: architecture, benchmark  
- **[Learning to Credit the Right Steps: Objective-aware Process Optimization for Visual Generation](https://arxiv.org/abs/2604.19234v1)**  
  Authors: Rui Li, Ke Hao, Yuanzhi Liang, Haibin Huang, Chi Zhang, YunGu, XueLong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19234v1.pdf)  
  Keywords: evaluation, trajectory, video generation, denoising, dit  
- **[How Far Are Video Models from True Multimodal Reasoning?](https://arxiv.org/abs/2604.19193v1)**  
  Authors: Xiaotian Zhang, Jianhui Wei, Yuan Wang, Jie Tan, Yichen Li, Yan Zhang, Ziyi Chen, Daoan Zhang, Dezhi YU, Wei Xu, Songtao Jiang, Zuozhu Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19193v1.pdf)  
  Keywords: evaluation, interactive, simulation, physical, benchmark, video generation, physical simulation  
- **[RoboWM-Bench: A Benchmark for Evaluating World Models in Robotic Manipulation](https://arxiv.org/abs/2604.19092v1)**  
  Authors: Feng Jiang, Yang Chen, Kyle Xu, Yuchen Liu, Haifeng Wang, Zhenhao Shen, Jasper Lu, Shengze Huang, Yuanfei Wang, Chen Xie, Ruihai Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19092v1.pdf)  
  Keywords: evaluation, physical, benchmark, video generation, world model, dynamics  
- **[OmniHuman: A Large-scale Dataset and Benchmark for Human-Centric Video Generation](https://arxiv.org/abs/2604.18326v1)**  
  Authors: Lei Zhu, Xing Cai, Yingjie Chen, Yiheng Li, Binxin Yang, Hao Liu, Jie Chen, Chen Li, Jing LYu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.18326v1.pdf)  
  Keywords: evaluation, physical, benchmark, video generation, video synthesis, multi-modal  
- **[WebCompass: Towards Multimodal Web Coding Evaluation for Code Language Models](https://arxiv.org/abs/2604.18224v1)**  
  Authors: Xinping Lei, Xinyu Che, Junqi Xiong, Chenchen Zhang, Yukai Huang, Chenyu Zhou, Haoyang Huang, Minghao Liu, Letian Zhu, Hongyi Ye, Jinhua Hao, Ken Deng, Zizheng Zhan, Han Li, Dailin Li, Yifan Yao, Ming Sun, Zhaoxiang Zhang, Jiaheng Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.18224v1.pdf)  
  Keywords: dit, evaluation, interactive, benchmark  
- **[Video-Robin: Autoregressive Diffusion Planning for Intent-Grounded Video-to-Music Generation](https://arxiv.org/abs/2604.17656v1)**  
  Authors: Vaibhavi Lokegaonkar, Aryan Vijay Bhosale, Vishnu Raj, Gouthaman KV, Ramani Duraiswami, Lie Lu, Sreyan Ghosh, Dinesh Manocha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.17656v1.pdf)  
  Keywords: dit, autoregressive, diffusion transformer, benchmark  
- **[FlowC2S: Flowing from Current to Succeeding Frames for Fast and Memory-Efficient Video Continuation](https://arxiv.org/abs/2604.17625v1)**  
  Authors: Hovhannes Margaryan, Quentin Bammey, Christian Sandor  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.17625v1.pdf)  
  Keywords: efficient, evaluation, text-to-video  
- **[ViPS: Video-informed Pose Spaces for Auto-Rigged Meshes](https://arxiv.org/abs/2604.17623v1)**  
  Authors: Honglin Chen, Karran Pandey, Rundi Wu, Matheus Gadelha, Yannick Hold-Geoffroy, Ayush Tewari, Niloy J. Mitra, Changxi Zheng, Paul Guerrero  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.17623v1.pdf)  
  Keywords: evaluation, controllable, diffusion model, video diffusion, physical, dit  

### Text-to-Video Generation

*Showing the latest 50 out of 59 papers*

- **[CityRAG: Stepping Into a City via Spatially-Grounded Video Generation](https://arxiv.org/abs/2604.19741v1)**  
  Authors: Gene Chou, Charles Herrmann, Kyle Genova, Boyang Deng, Songyou Peng, Bharath Hariharan, Jason Y. Zhang, Noah Snavely, Philipp Henzler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19741v1.pdf)  
  Keywords: dit, i2v, simulation, physical, video generation, robotics, t2v, autonomous driving  
- **[TS-Attn: Temporal-wise Separable Attention for Multi-Event Video Generation](https://arxiv.org/abs/2604.19473v1)**  
  Authors: Hongyu Zhang, Yufan Deng, Zilin Pan, Peng-Tao Jiang, Bo Li, Qibin Hou, Zhiyang Dou, Zhen Dong, Daquan Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19473v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Hong-yu-Zhang/TS-Attn?style=social)](https://github.com/Hong-yu-Zhang/TS-Attn)  
  Keywords: dit, temporal consistency, video generation, image-to-video, text-to-video, t2v  
- **[FlowC2S: Flowing from Current to Succeeding Frames for Fast and Memory-Efficient Video Continuation](https://arxiv.org/abs/2604.17625v1)**  
  Authors: Hovhannes Margaryan, Quentin Bammey, Christian Sandor  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.17625v1.pdf)  
  Keywords: efficient, evaluation, text-to-video  
- **[Generative Refinement Networks for Visual Synthesis](https://arxiv.org/abs/2604.13030v1)**  
  Authors: Jian Han, Jinlai Liu, Jiahuan Wang, Bingyue Peng, Zehuan Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.13030v1.pdf)  
  Keywords: diffusion model, autoregressive, benchmark, video generation, text-to-video, efficient, dit  
- **[VideoFlexTok: Flexible-Length Coarse-to-Fine Video Tokenization](https://arxiv.org/abs/2604.12887v1)**  
  Authors: Andrei Atanov, Jesse Allardice, Roman Bachmann, Oğuzhan Fatih Kar, R Devon Hjelm, David Griffiths, Peter Fu, Afshin Dehghan, Amir Zamir  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.12887v1.pdf)  
  Keywords: long video, efficient, text-to-video, video generation  
- **[Motif-Video 2B: Technical Report](https://arxiv.org/abs/2604.16503v1)**  
  Authors: Junghwan Lim, Wai Ting Cheung, Minsu Ha, Beomgyu Kim, Taewhan Kim, Haesol Lee, Dongpin Oh, Jeesoo Lee, Taehyun Kim, Minjae Kim, Sungmin Lee, Hyeyeon Cho, Dahye Choi, Jaeheui Her, Jaeyeon Huh, Hanbin Jung, Changjin Kang, Dongseok Kim, Jangwoong Kim, Youngrok Kim, Hyukjin Kweon, Hongjoo Lee, Jeongdoo Lee, Junhyeok Lee, Eunhwan Park, Yeongjae Park, Bokki Ryu, Dongjoo Weon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.16503v1.pdf)  
  Keywords: efficient, temporal consistency, text-to-video, video generation  
- **[When Numbers Speak: Aligning Textual Numerals and Visual Instances in Text-to-Video Diffusion Models](https://arxiv.org/abs/2604.08546v1)**  
  Authors: Zhengyang Sun, Yu Chen, Xin Zhou, Xiaofan Li, Xiwu Chen, Dingkang Liang, Xiang Bai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08546v1.pdf) | [![GitHub](https://img.shields.io/github/stars/H-EmbodVis/NUMINA?style=social)](https://github.com/H-EmbodVis/NUMINA)  
  Keywords: temporal consistency, diffusion model, video diffusion, layout, video synthesis, text-to-video  
- **[SceneScribe-1M: A Large-Scale Video Dataset with Comprehensive Geometric and Semantic Annotations](https://arxiv.org/abs/2604.07990v1)**  
  Authors: Yunnan Wang, Kecheng Zheng, Jianyuan Wang, Minghao Chen, David Novotny, Christian Rupprecht, Yinghao Xu, Xing Zhu, Wenjun Zeng, Xin Jin, Yujun Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07990v1.pdf)  
  Keywords: controllable, camera control, benchmark, video generation, video synthesis, text-to-video, multi-modal  
- **[Not all tokens contribute equally to diffusion learning](https://arxiv.org/abs/2604.07026v1)**  
  Authors: Guoqing Zhang, Lu Shi, Wanru Xu, Linna Zhang, Sen Wang, Fangfang Wang, Yigang Cen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07026v1.pdf)  
  Keywords: diffusion model, benchmark, video generation, text-to-video, dit  
- **[Accelerating Training of Autoregressive Video Generation Models via Local Optimization with Representation Continuity](https://arxiv.org/abs/2604.07402v1)**  
  Authors: Yucheng Zhou, Jianbing Shen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07402v1.pdf)  
  Keywords: autoregressive, text-to-video, video generation  

### Video Editing

- **[LIVE: Leveraging Image Manipulation Priors for Instruction-based Video Editing](https://arxiv.org/abs/2604.17021v1)**  
  Authors: Weicheng Wang, Zhicheng Zhang, Zhongqi Zhang, Juncheng Zhou, Yongjie Zhu, Wenyu Qin, Meng Wang, Pengfei Wan, Jufeng Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.17021v1.pdf)  
  Keywords: evaluation, benchmark, video generation, dit, video editing  
- **[UniEditBench: A Unified and Cost-Effective Benchmark for Image and Video Editing via Distilled MLLMs](https://arxiv.org/abs/2604.15871v1)**  
  Authors: Lifan Jiang, Tianrun Wu, Yuhang Pei, Chenyang Wang, Boxi Wu, Deng Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.15871v1.pdf) | [![GitHub](https://img.shields.io/github/stars/wesar1/UniEditBench?style=social)](https://github.com/wesar1/UniEditBench)  
  Keywords: dit, video editing, evaluation, benchmark  
- **[Empowering Video Translation using Multimodal Large Language Models](https://arxiv.org/abs/2604.11283v1)**  
  Authors: Bingzheng QU, Kehai Chen, Xuefeng Bai, Min Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.11283v1.pdf)  
  Keywords: survey, controllable, identity, dit, video translation  
- **[Rein3D: Reinforced 3D Indoor Scene Generation with Panoramic Video Diffusion Models](https://arxiv.org/abs/2604.10578v2)**  
  Authors: Dehui Wang, Congsheng Xu, Rong Wei, Yue Shi, Shoufa Chen, Dingxiang Luo, Tianshuo Yang, Xiaokang Yang, Wei Sui, Yusen Qin, Rui Tang, Yao Mu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.10578v2.pdf)  
  Keywords: super-resolution, video-to-video, video diffusion, diffusion model  
- **[InsEdit: Towards Instruction-based Visual Editing via Data-Efficient Video Diffusion Models Adaptation](https://arxiv.org/abs/2604.08646v1)**  
  Authors: Zhefan Rao, Bin Zou, Haoxuan Che, Xuanhua He, Chong Hou Choi, Yanheng Li, Rui Liu, Qifeng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08646v1.pdf)  
  Keywords: architecture, diffusion model, video diffusion, benchmark, video generation, efficient, dit, video editing  
- **[Lighting-grounded Video Generation with Renderer-based Agent Reasoning](https://arxiv.org/abs/2604.07966v1)**  
  Authors: Ziqi Cai, Taoyu Yang, Zheng Chang, Si Li, Han Jiang, Shuchen Weng, Boxin Shi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07966v1.pdf)  
  Keywords: controllable, diffusion model, temporal consistency, trajectory, video diffusion, video generation, layout, video synthesis, image-to-video, film, dit, video-to-video  
- **[ImVideoEdit: Image-learning Video Editing via 2D Spatial Difference Attention Blocks](https://arxiv.org/abs/2604.07958v1)**  
  Authors: Jiayang Xu, Fan Zhuo, Majun Zhang, Changhao Pan, Zehan Wang, Siyu Chen, Xiaoda Yang, Tao Jin, Zhou Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.07958v1.pdf)  
  Keywords: temporal consistency, efficient, dynamics, dit, video editing  
- **[Evolution of Video Generative Foundations](https://arxiv.org/abs/2604.06339v1)**  
  Authors: Teng Hu, Jiangning Zhang, Hongrui Huang, Ran Yi, Zihan Su, Jieyu Weng, Zhucun Xue, Lizhuang Ma, Ming-Hsuan Yang, Dacheng Tao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06339v1.pdf) | [![GitHub](https://img.shields.io/github/stars/sjtuplayer/Awesome-Video-Foundations?style=social)](https://github.com/sjtuplayer/Awesome-Video-Foundations)  
  Keywords: survey, diffusion model, education, simulation, video generation, world model, dynamics, dit, autonomous driving, video editing  
- **[UENR-600K: A Large-Scale Physically Grounded Dataset for Nighttime Video Deraining](https://arxiv.org/abs/2604.04402v1)**  
  Authors: Pei Yang, Hai Ci, Beibei Lin, Yiren Song, Mike Zheng Shou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04402v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://showlab.github.io/UENR-600K)  
  Keywords: physical, benchmark, video-to-video, video generation  
- **[VOID: Video Object and Interaction Deletion](https://arxiv.org/abs/2604.02296v1)**  
  Authors: Saman Motamed, William Harvey, Benjamin Klein, Luc Van Gool, Zhuoning Yuan, Ta-Ying Cheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.02296v1.pdf)  
  Keywords: diffusion model, physical, video diffusion, dynamics, dit, video editing  

### Video Inpainting & Completion

- **[LMGenDrive: Bridging Multimodal Understanding and Generative World Modeling for End-to-End Driving](https://arxiv.org/abs/2604.08719v1)**  
  Authors: Hao Shao, Letian Wang, Yang Zhou, Yuxuan Hu, Zhuofan Zong, Steven L. Waslander, Wei Zhan, Hongsheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08719v1.pdf)  
  Keywords: video prediction, autoregressive, benchmark, video generation, world model, autonomous driving  
- **[Novel View Synthesis as Video Completion](https://arxiv.org/abs/2604.08500v1)**  
  Authors: Qi Wu, Khiem Vuong, Minsik Jeon, Srinivasa Narasimhan, Deva Ramanan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.08500v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://frame-crafter.github.io)  
  Keywords: novel view, video completion, diffusion model, video diffusion, benchmark  
- **[SEM-ROVER: Semantic Voxel-Guided Diffusion for Large-Scale Driving Scene Generation](https://arxiv.org/abs/2604.06113v1)**  
  Authors: Hiba Dahmani, Nathan Piasco, Moussab Bennehar, Luis Roldão, Dzmitry Tsishkou, Laurent Caraffa, Jean-Philippe Tarel, Roland Brémond  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.06113v1.pdf)  
  Keywords: outpainting, dit, diffusion model  
- **[ChopGrad: Pixel-Wise Losses for Latent Video Diffusion via Truncated Backpropagation](https://arxiv.org/abs/2603.17812v2)**  
  Authors: Dmitriy Rivkin, Parker Ewen, Lili Gao, Julian Ost, Stefanie Walz, Rasika Kangutkar, Mario Bijelic, Felix Heide  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.17812v2.pdf)  
  Keywords: super-resolution, video enhancement, diffusion model, video diffusion, video generation, efficient, latent video, dit, video inpainting  
- **[ConfCtrl: Enabling Precise Camera Control in Video Diffusion via Confidence-Aware Interpolation](https://arxiv.org/abs/2603.09819v1)**  
  Authors: Liudi Yang, George Eskandar, Fengyi Shen, Mohammad Altillawi, Yang Bai, Chi Zhang, Ziyuan Liu, Abhinav Valada  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.09819v1.pdf)  
  Keywords: novel view, diffusion model, video interpolation, camera control, video diffusion, dit  
- **[Pinterest Canvas: Large-Scale Image Generation at Pinterest](https://arxiv.org/abs/2603.06453v1)**  
  Authors: Yu Wang, Eric Tzeng, Raymond Shiau, Jie Yang, Dmitry Kislyuk, Charles Rosenberg  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2603.06453v1.pdf)  
  Keywords: diffusion model, outpainting, video generation, image-to-video, dit  

### Video Super-Resolution & Enhancement

*Showing the latest 50 out of 61 papers*

- **[Learning to Credit the Right Steps: Objective-aware Process Optimization for Visual Generation](https://arxiv.org/abs/2604.19234v1)**  
  Authors: Rui Li, Ke Hao, Yuanzhi Liang, Haibin Huang, Chi Zhang, YunGu, XueLong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19234v1.pdf)  
  Keywords: evaluation, trajectory, video generation, denoising, dit  
- **[Trustworthy Endoscopic Super-Resolution](https://arxiv.org/abs/2604.18001v1)**  
  Authors: Julio Silva-Rodríguez, Ender Konukoglu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.18001v1.pdf)  
  Keywords: super-resolution, efficient  
- **[Speculative Decoding for Autoregressive Video Generation](https://arxiv.org/abs/2604.17397v1)**  
  Authors: Yuezhou Hu, Jintao Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.17397v1.pdf)  
  Keywords: autoregressive, video diffusion, video generation, streaming, acceleration, video synthesis, denoising, dit, distillation  
- **[Efficient Video Diffusion Models: Advancements and Challenges](https://arxiv.org/abs/2604.15911v1)**  
  Authors: Shitong Shao, Lichen Bai, Pengfei Wan, James Kwok, Zeke Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.15911v1.pdf)  
  Keywords: evaluation, survey, diffusion model, trajectory, video diffusion, acceleration, video synthesis, denoising, efficient, distillation  
- **[TurboTalk: Progressive Distillation for One-Step Audio-Driven Talking Avatar Generation](https://arxiv.org/abs/2604.14580v1)**  
  Authors: Xiangyu Liu, Feng Gao, Xiaomei Zhang, Yong Zhang, Xiaoming Wei, Zhen Lei, Xiangyu Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.14580v1.pdf)  
  Keywords: diffusion model, video diffusion, avatar, audio-driven, denoising, distillation  
- **[DiT as Real-Time Rerenderer: Streaming Video Stylization with Autoregressive Diffusion Transformer](https://arxiv.org/abs/2604.13509v1)**  
  Authors: Hengye Lyu, Zisu Li, Yue Hong, Yueting Weng, Jiaxin Shi, Hanwang Zhang, Chen Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.13509v1.pdf)  
  Keywords: interactive, autoregressive, diffusion transformer, video generation, streaming, denoising, style, distillation, dit, long video  
- **[Rein3D: Reinforced 3D Indoor Scene Generation with Panoramic Video Diffusion Models](https://arxiv.org/abs/2604.10578v2)**  
  Authors: Dehui Wang, Congsheng Xu, Rong Wei, Yue Shi, Shoufa Chen, Dingxiang Luo, Tianshuo Yang, Xiaokang Yang, Wei Sui, Yusen Qin, Rui Tang, Yao Mu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.10578v2.pdf)  
  Keywords: super-resolution, video-to-video, video diffusion, diffusion model  
- **[Beyond Few-Step Inference: Accelerating Video Diffusion Transformer Model Serving with Inter-Request Caching Reuse](https://arxiv.org/abs/2604.04451v1)**  
  Authors: Hao Liu, Ye Huang, Chenghuan Huang, Zhenyi Zheng, Jiangsu Du, Ziyang Ma, Jing Lyu, Yutong Lu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04451v1.pdf)  
  Keywords: diffusion model, diffusion transformer, video diffusion, video generation, denoising, dit  
- **[OP-GRPO: Efficient Off-Policy GRPO for Flow-Matching Models](https://arxiv.org/abs/2604.04142v1)**  
  Authors: Liyu Zhang, Kehan Li, Tingrui Han, Tao Zhao, Yuxuan Sheng, Shibo He, Chao Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.04142v1.pdf)  
  Keywords: benchmark, video generation, denoising, efficient, dit  
- **[Salt: Self-Consistent Distribution Matching with Cache-Aware Training for Fast Video Generation](https://arxiv.org/abs/2604.03118v1)**  
  Authors: Xingtong Ge, Yi Zhang, Yushi Huang, Dailan He, Xiahong Wang, Bingqi Ma, Guanglu Song, Yu Liu, Jun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.03118v1.pdf) | [![GitHub](https://img.shields.io/github/stars/XingtongGe/Salt?style=social)](https://github.com/XingtongGe/Salt)  
  Keywords: autoregressive, trajectory, dynamics, video generation, denoising, style, dit, distillation  

### World Models & Simulation

*Showing the latest 50 out of 95 papers*

- **[CityRAG: Stepping Into a City via Spatially-Grounded Video Generation](https://arxiv.org/abs/2604.19741v1)**  
  Authors: Gene Chou, Charles Herrmann, Kyle Genova, Boyang Deng, Songyou Peng, Bharath Hariharan, Jason Y. Zhang, Noah Snavely, Philipp Henzler  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19741v1.pdf)  
  Keywords: dit, i2v, simulation, physical, video generation, robotics, t2v, autonomous driving  
- **[UniT: Toward a Unified Physical Language for Human-to-Humanoid Policy Learning and World Modeling](https://arxiv.org/abs/2604.19734v1)**  
  Authors: Boyu Chen, Yi Chen, Lu Qiu, Jerry Bai, Yuying Ge, Yixiao Ge  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19734v1.pdf)  
  Keywords: simulation, physical, benchmark, video generation, world model, dynamics, dit  
- **[How Far Are Video Models from True Multimodal Reasoning?](https://arxiv.org/abs/2604.19193v1)**  
  Authors: Xiaotian Zhang, Jianhui Wei, Yuan Wang, Jie Tan, Yichen Li, Yan Zhang, Ziyi Chen, Daoan Zhang, Dezhi YU, Wei Xu, Songtao Jiang, Zuozhu Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19193v1.pdf)  
  Keywords: evaluation, interactive, simulation, physical, benchmark, video generation, physical simulation  
- **[RoboWM-Bench: A Benchmark for Evaluating World Models in Robotic Manipulation](https://arxiv.org/abs/2604.19092v1)**  
  Authors: Feng Jiang, Yang Chen, Kyle Xu, Yuchen Liu, Haifeng Wang, Zhenhao Shen, Jasper Lu, Shengze Huang, Yuanfei Wang, Chen Xie, Ruihai Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.19092v1.pdf)  
  Keywords: evaluation, physical, benchmark, video generation, world model, dynamics  
- **[MultiWorld: Scalable Multi-Agent Multi-View Video World Models](https://arxiv.org/abs/2604.18564v2)**  
  Authors: Haoyu Wu, Jiwen Yu, Yingtian Zou, Xihui Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.18564v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://multi-world.github.io)  
  Keywords: multi-view video, video generation, world model, action-conditioned, dynamics, dit  
- **[WebCompass: Towards Multimodal Web Coding Evaluation for Code Language Models](https://arxiv.org/abs/2604.18224v1)**  
  Authors: Xinping Lei, Xinyu Che, Junqi Xiong, Chenchen Zhang, Yukai Huang, Chenyu Zhou, Haoyang Huang, Minghao Liu, Letian Zhu, Hongyi Ye, Jinhua Hao, Ken Deng, Zizheng Zhan, Han Li, Dailin Li, Yifan Yao, Ming Sun, Zhaoxiang Zhang, Jiaheng Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.18224v1.pdf)  
  Keywords: dit, evaluation, interactive, benchmark  
- **[HY-World 2.0: A Multi-Modal World Model for Reconstructing, Generating, and Simulating 3D Worlds](https://arxiv.org/abs/2604.14268v1)**  
  Authors: Team HY-World, Chenjie Cao, Xuhui Zuo, Zhenwei Wang, Yisu Zhang, Junta Wu, Zhenyang Liu, Yuning Gong, Yang Liu, Bo Yuan, Chao Zhang, Coopers Li, Dongyuan Guo, Fan Yang, Haiyu Zhang, Hang Cao, Jianchen Zhu, Jiaxin Lin, Jie Xiao, Jihong Zhang, Junlin Yu, Lei Wang, Lifu Wang, Lilin Wang, Linus, Minghui Chen, Peng He, Penghao Zhao, Qi Chen, Rui Chen, Rui Shao, Sicong Liu, Wangchen Qin, Xiaochuan Niu, Xiang Yuan, Yi Sun, Yifei Tang, Yifu Sun, Yihang Lian, Yonghao Tan, Yuhong Liu, Yuyang Yin, Zhiyuan Min, Tengfei Wang, Chunchao Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.14268v1.pdf)  
  Keywords: interactive, architecture, trajectory, benchmark, world model, efficient, multi-modal  
- **[Depth-Aware Image and Video Orientation Estimation](https://arxiv.org/abs/2604.13995v1)**  
  Authors: Muhammad Z. Alam, Larry Stetsiuk, M. Umair Mukati, Zeeshan Kaleem  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.13995v1.pdf)  
  Keywords: evaluation, interactive  
- **[DiT as Real-Time Rerenderer: Streaming Video Stylization with Autoregressive Diffusion Transformer](https://arxiv.org/abs/2604.13509v1)**  
  Authors: Hengye Lyu, Zisu Li, Yue Hong, Yueting Weng, Jiaxin Shi, Hanwang Zhang, Chen Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.13509v1.pdf)  
  Keywords: interactive, autoregressive, diffusion transformer, video generation, streaming, denoising, style, distillation, dit, long video  
- **[Lyra 2.0: Explorable Generative 3D Worlds](https://arxiv.org/abs/2604.13036v1)**  
  Authors: Tianchang Shen, Sherwin Bahmani, Kai He, Sangeetha Grama Srinivasan, Tianshi Cao, Jiawei Ren, Ruilong Li, Zian Wang, Nicholas Sharp, Zan Gojcic, Sanja Fidler, Jiahui Huang, Huan Ling, Jun Gao, Xuanchi Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2604.13036v1.pdf)  
  Keywords: autoregressive, simulation, creative, video generation  



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
