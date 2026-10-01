# Awesome Video Diffusions [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Video Diffusion Models and Video Generation. Content is automatically updated daily.

🗺️ **[Explore the Paper Atlas](https://longxiang-ai.github.io/awesome-video-diffusions/)**: an interactive paper map, monthly trends, topic network, co-author network and author rankings of every tracked paper.

> Last Update: 2026-10-01 04:28:27

## 📰 Latest Updates

🗺️ **[2026-09-30] Paper Atlas on GitHub Pages**
- New [interactive site](https://longxiang-ai.github.io/awesome-video-diffusions/) built from all daily snapshots, rebuilt after every update

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

- [3D-aware Video Generation](#3d-aware-video-generation) (54 papers) - Video generation with 3D awareness, multi-view consistency, and 4D content creation
- [Applications](#applications) (202 papers) - Domain-specific applications of video diffusion models
- [Architecture & Efficiency](#architecture-&-efficiency) (388 papers) - Architectural innovations (DiT, UNet), flow matching, and training/inference efficiency
- [Audio & Multi-modal](#audio-&-multi-modal) (70 papers) - Audio-driven and multi-modal conditioned video generation
- [Controllable Generation](#controllable-generation) (331 papers) - Controllable video generation with motion, camera, pose, or layout guidance
- [Human & Character Animation](#human-&-character-animation) (63 papers) - Human-centric video generation including talking heads, dance, and character animation
- [Image-to-Video Generation](#image-to-video-generation) (91 papers) - Methods for animating still images into videos
- [Long Video Generation](#long-video-generation) (255 papers) - Generating temporally consistent long-form videos beyond short clips
- [Personalization & Customization](#personalization-&-customization) (165 papers) - Personalized video generation with custom subjects, identities, or styles
- [Physical Understanding](#physical-understanding) (309 papers) - Physics-aware video generation and dynamics modeling
- [Surveys & Benchmarks](#surveys-&-benchmarks) (312 papers) - Survey papers, benchmarks, and evaluation metrics for video generation
- [Text-to-Video Generation](#text-to-video-generation) (147 papers) - Foundation models and methods for generating videos from text prompts
- [Video Editing](#video-editing) (97 papers) - Diffusion-based video editing, style transfer, and manipulation
- [Video Inpainting & Completion](#video-inpainting-&-completion) (23 papers) - Video inpainting, completion, outpainting, and temporal prediction
- [Video Super-Resolution & Enhancement](#video-super-resolution-&-enhancement) (167 papers) - Video quality improvement, upscaling, restoration, and frame interpolation
- [World Models & Simulation](#world-models-&-simulation) (243 papers) - Video generation as world simulators and interactive environment generation



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3D-aware Video Generation

*Showing the latest 50 out of 54 papers*

- **[PartiCam: Camera Controlled Video Generation with Reward Guidance](https://arxiv.org/abs/2609.39504v1)**  
  Authors: Amine Ouasfi, Runjia Li, Junlin Han, Eric Marchand, Philip H. S. Torr, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.39504v1.pdf)  
  Keywords: camera control, camera motion, camera trajectory, camera-conditioned, trajectory, video diffusion, video generation  
- **[GeoVerse: World-Consistent Novel View Synthesis in Geometric Latent Space](https://arxiv.org/abs/2609.35734v2)**  
  Authors: Kerui Ren, Tao Lu, Linning Xu, Changjian Jiang, Mu Huang, Chunhua Shen, Mulin Yu, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.35734v2.pdf)  
  Keywords: diffusion model, novel view, style  
- **[OPIS: An Input-Grounded Benchmark for Multi-Object Memory in Video World Models](https://arxiv.org/abs/2609.35052v1)**  
  Authors: Hao Wang, Tao Yu, Liuzhou Zhang, HeXin Wang, Haopeng Jin, Yuxuan Zhou, Xinming Wang, Hongzhu Yi, Xinye Li, Yuanlei Wang, Ping Nie, Yan Huang, Yuxuan Zhang, Pengfei Zhou, Yanyan Zou, Wei Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.35052v1.pdf)  
  Keywords: benchmark, camera-conditioned, embodied, evaluation, game, identity, image to video, image-to-video  
- **[GenNVS: Geometry-enhanced Novel View Synthesis via Disentangled 3D Prior](https://arxiv.org/abs/2609.34579v2)**  
  Authors: Yajiao Xiong, Youyu Luan, Xiaoyu Zhou, Yongtao Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.34579v2.pdf)  
  Keywords: diffusion model, novel view, video diffusion  
- **[VGGT-Diff: Visual Geometry Meets Diffusion for Sparse-View Novel View Synthesis](https://arxiv.org/abs/2609.33253v1)**  
  Authors: Kangjie Chen, Xiangyu Li, Dongbin Zhang, Chaoda Zheng, Shijia Chen, Jinhao Deng, Hongbin Lin, Choo Sin Wai, Minqi Wang, Minghao Yang, Dake Zhong, Guorui Song, Yu Zhang, Xianming Liu, Boyang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.33253v1.pdf) | [![GitHub](https://img.shields.io/github/stars/chenkangjie1123/VGGT-Diff?style=social)](https://github.com/chenkangjie1123/VGGT-Diff)  
  Keywords: denoising, diffusion model, novel view, video diffusion  
- **[WorldCrafter: Consistent Video World Model with Implicit 3D-aware Memory](https://arxiv.org/abs/2609.24984v1)**  
  Authors: Wangbo Yu, Kunhao Liu, Wenbo Hu, Shenghai Yuan, Chaoran Feng, Haiyang Zhou, Yukun Huang, Yiran Wang, Wang Zhao, Yingmin Luo, Ying Shan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.24984v1.pdf)  
  Keywords: 3d-aware, camera control, denoising, distillation, interactive, streaming, video world model, world model  
- **[Printing the Underdetermined: Materializing Multi-solutionness in Figurative Paintings](https://arxiv.org/abs/2609.19782v2)**  
  Authors: Yutao Ming, Teng Xu, Youjia Wang, Yunyang Liu, Fengmin Yang, Fuqiang Zhao, Jingyi Yu, Hua Yang, Yanjun Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.19782v2.pdf)  
  Keywords: multi-view video, physical  
- **[AlayaVista: Streaming World Modeling from Panoramic States to Perspective Video](https://arxiv.org/abs/2609.14462v1)**  
  Authors: Jiaming Tan, Mingliang Zhai, Zhen Li, Yuwei Wu, Chuanhao Li, Kaipeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.14462v1.pdf)  
  Keywords: autoregressive, camera motion, camera-conditioned, controllable, efficient, interactive, streaming, super-resolution, video world model, world model  
- **[VideoTok4D: A 4D-Aware Video Tokenizer for Compact World Representation](https://arxiv.org/abs/2609.12874v1)**  
  Authors: Xinyi Chen, Hanxin Zhu, Xijun Wang, Xingrui Wang, Sen Liang, Xin Li, Zhibo Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.12874v1.pdf)  
  Keywords: dynamic 3d, efficient, trajectory, video tokenizer  
- **[Rethinking 3D Noise: Learning 3D-Aware Video Priors via Optimization-Free Morphological Perturbations](https://arxiv.org/abs/2609.03657v1)**  
  Authors: Onat Şahin, Mohammad Altillawi, George Eskandar, Carlos Carbone, Ziyuan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.03657v1.pdf)  
  Keywords: 3d-aware, robotics, video diffusion  

### Applications

*Showing the latest 50 out of 202 papers*

- **[Dream4ACT: A Shared Visual Action Interface for Multi-Embodiment Video-Action Modeling](https://arxiv.org/abs/2609.40153v1)**  
  Authors: Xiangyu Zhu, Jin Xu, Yue Guo, Xin Wu, Yifan Sun, Xiancong Ren, Jianxin Sun, Yong Dai, Xiaozhu Ju  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.40153v1.pdf)  
  Keywords: action-conditioned, diffusion transformer, dynamics, embodied, flow matching, video autoencoder, video generation, world model  
- **[DiffWAM: A Fast and Efficient Navigation World Action Model](https://arxiv.org/abs/2609.39763v1)**  
  Authors: Mo Zhu, Yuze Wu, Xijie Huang, Xiao Cui, Fei Gao, Xin Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.39763v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zzmmzzm.github.io/diffwam.github.io)  
  Keywords: benchmark, efficient, embodied, trajectory, video synthesis  
- **[GroundingPI: A Grounding Foundation Model towards Physical Intelligence with Visual Primitives](https://arxiv.org/abs/2609.39601v1)**  
  Authors: Qize Yu, Lianrui Fan, Boyu Chen, Jiaqi Liang, Xini Ding, Yue Chen, Zetian Song, Yuran Wang, Yi Zou, Kaixuan Wang, Tianxing Chen, Wenxuan Song, Bohan Zhou, Mingleyang Li, Siqiao Huang, Yuqi Ye, Caigao Jiang, Wei Wei, Ruihai Wu, Hang Zhang, Yixiao Ge, Shuchang Zhou, Shilong Liu, Xianming Liu, Ping Luo, Shiyu Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.39601v1.pdf)  
  Keywords: autonomous driving, driving, physical, video generation  
- **[Exo2EgoHOI: Hand-Object-Interaction Aware Exocentric-to-Egocentric Video Generation](https://arxiv.org/abs/2609.38615v1)**  
  Authors: Hongjia Zhai, Xiyu Zhang, Haoran Zhang, Zhichao Ye, Haomin Liu, Guofeng Zhang, Ian Reid, Xingxing Zuo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38615v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rcl-robotics.github.io/Exo2EgoHOI)  
  Keywords: embodied, robotics, video generation  
- **[LongTake: Learning to Sustain Dynamics in Long-Horizon Video Generation](https://arxiv.org/abs/2609.38562v1)**  
  Authors: Byoungwoo Park, Jaemoo Choi, Juho Lee, Yongxin Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38562v1.pdf)  
  Keywords: autoregressive, distillation, dynamics, game, video diffusion, video generation  
- **[Rethinking Representations for World-Action Modeling](https://arxiv.org/abs/2609.38163v1)**  
  Authors: Haoyi Jiang, Liu Liu, Xinjiang Wang, Zhihao Sun, Zequn Chen, Sen Wang, Xinjie Wang, Xia Chen, Jingfeng Yao, Weiheng Zhao, Shanglin Yuan, Zhizhong Su, Wei Sui, Wenyu Liu, Xinggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38163v1.pdf)  
  Keywords: dynamics, embodied, world model  
- **[LongLive-Plug: Once-for-All Distillation for Video Generation](https://arxiv.org/abs/2609.38154v1)**  
  Authors: Shuai Yang, Luozhou Wang, Wei Huang, ZhiFei Chen, Bohan Zhang, Xiao Fu, Qianli Ma, Chen-Hsuan Lin, Weian Mao, Bryan Chu, Song Han, Yukang Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38154v1.pdf)  
  Keywords: autoregressive, distillation, long video, robotics, video diffusion, video generation  
- **[WorldLine: Action-Driven Visual Simulation for Robotic Manipulation](https://arxiv.org/abs/2609.38059v1)**  
  Authors: Shenghe Zheng, Wenbo Li, Jiyao Zhang, Bin Xia, Haoyang Huang, Nan Duan, Jiaya Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38059v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zhengsh123.github.io/WorldLine)  
  Keywords: action-conditioned, distillation, dynamics, efficient, embodied, evaluation, physical, robot learning, simulation, trajectory, video generation  
- **[Waypoint-1.5: A Real-Time Video World Model for Consumer Hardware](https://arxiv.org/abs/2609.37107v2)**  
  Authors: Rajit Rajpal, Shahbuland Matiana, Liew Wei Pyn, Anmol Agarwal, Ryan Craig, Andrew Lapp, Mithun Hunsur, Sami BuGhanem, Scottie Fox, Aaron Sanders, Carson Poole, Irene Park, Dave Rossi, Spencer Frazier, Louis Castricato  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.37107v2.pdf)  
  Keywords: architecture, game, interactive, video diffusion, video generation, video world model, world model  
- **[WeLike2Party! In-Context Motion Transfer for Multi-Human Image Animation](https://arxiv.org/abs/2609.36937v1)**  
  Authors: Sangeyl Lee, Seunghyun Shin, Seungho Park, Wooseok Jeon, Hae-Gon Jeon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.36937v1.pdf)  
  Keywords: benchmark, driving, human animation, human image animation, identity, image animation, motion transfer, trajectory, video generation  

### Architecture & Efficiency

*Showing the latest 50 out of 388 papers*

- **[GLARE: Generating Listening Heads with Appropriate Reactions](https://arxiv.org/abs/2609.40317v1)**  
  Authors: Zikai Liao, Yumin Suh, Yi Ouyang, Yi-Lun Lee, Yi-Hsuan Tsai, Zhaozheng Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.40317v1.pdf)  
  Keywords: audio-driven, evaluation, flow matching, talking head, video generation  
- **[LOCI: Spatial Linear Memory for Streaming World Models](https://arxiv.org/abs/2609.40222v1)**  
  Authors: Ji Xia, Tingting Liao, Xuezhi Liang, Hao Li, Guangyi Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.40222v1.pdf)  
  Keywords: architecture, benchmark, streaming, video world model, world model  
- **[Dream4ACT: A Shared Visual Action Interface for Multi-Embodiment Video-Action Modeling](https://arxiv.org/abs/2609.40153v1)**  
  Authors: Xiangyu Zhu, Jin Xu, Yue Guo, Xin Wu, Yifan Sun, Xiancong Ren, Jianxin Sun, Yong Dai, Xiaozhu Ju  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.40153v1.pdf)  
  Keywords: action-conditioned, diffusion transformer, dynamics, embodied, flow matching, video autoencoder, video generation, world model  
- **[VR-JEPA: Learning Contrastive-State Latent Guidance for Generation-based Video Reasoning](https://arxiv.org/abs/2609.40129v1)**  
  Authors: Zehua Ma, Kun Xiang, Yunshuang Nie, Quanlin Chen, Haoyuan Li, Xiuwei Chen, Jiang Ji, Haijun Wu, Zhenyu Xie, Michael Kampffmeyer, Hanhui Li, Xiaodan Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.40129v1.pdf)  
  Keywords: architecture, dynamics, physical, video generation  
- **[Enhancing Autoregressive Video Generation via Representation Adversarial Distillation](https://arxiv.org/abs/2609.40037v1)**  
  Authors: Fangyu Lin, Xingtong Ge, Lunjie Zhu, Yi Zhang, Zhening Liu, Tianhang Wang, Mengfei Li, Yumeng Zhang, Guanglu Song, Yu Liu, Jun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.40037v1.pdf)  
  Keywords: architecture, autoregressive, autoregressive video, denoising, distillation, efficient, minute-long, streaming, video generation  
- **[DiffWAM: A Fast and Efficient Navigation World Action Model](https://arxiv.org/abs/2609.39763v1)**  
  Authors: Mo Zhu, Yuze Wu, Xijie Huang, Xiao Cui, Fei Gao, Xin Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.39763v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zzmmzzm.github.io/diffwam.github.io)  
  Keywords: benchmark, efficient, embodied, trajectory, video synthesis  
- **[TexTailor: Texture-Preserving Video Virtual Try-On via Adaptive Garment Conditioning](https://arxiv.org/abs/2609.39335v1)**  
  Authors: Zijing Qin, Jun Zhou, Ruicheng Zhang, Jiaqi Hou, Zunnan Xu, Ronghui Li, Zhenyu Xie, Xiu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.39335v1.pdf)  
  Keywords: denoising, diffusion transformer, temporal consistency, video diffusion, video diffusion transformer, virtual try-on  
- **[Uncertainty-Aware Consistency Distillation for Few-Step Video Generation](https://arxiv.org/abs/2609.39132v1)**  
  Authors: Lingyu Liu, Yaxiong Wang, Li Zhu, Zhedong Zheng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.39132v1.pdf)  
  Keywords: consistency distillation, distillation, efficient, video generation  
- **[DeCoPrune: Efficient KV-Cache Pruning for Autoregressive Video Diffusion via Denoising Consistency](https://arxiv.org/abs/2609.39096v1)**  
  Authors: Zeqi Xiao, Qingle Liu, Kaiwen Zhang, Yifan Zhou, Zihan Ding, Xingang Pan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.39096v1.pdf) | [![GitHub](https://img.shields.io/github/stars/DeCoPrune/CMBench?style=social)](https://github.com/DeCoPrune/CMBench) | [![Project](https://img.shields.io/badge/-Project-blue)](https://decoprune.github.io) | [![Dataset](https://img.shields.io/badge/-Dataset-orange)](https://huggingface.co/datasets/Aoraku/CMBench)  
  Keywords: autoregressive, autoregressive video, benchmark, denoising, efficient, interactive, streaming, video diffusion  
- **[Sparse-WAM: Accelerating World Action Models via Action-Guided Sparse Imagination](https://arxiv.org/abs/2609.38984v1)**  
  Authors: Xinling Xie, Haodong Wang, Jiazhi Mi, Zhiming Liu, Zicong Hong, Xiaoyi Pang, Qianli Liu, Yangjia Hu, Ying Chen, Zhengyang Yan, Song Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38984v1.pdf)  
  Keywords: denoising, efficient, video diffusion  

### Audio & Multi-modal

*Showing the latest 50 out of 70 papers*

- **[GLARE: Generating Listening Heads with Appropriate Reactions](https://arxiv.org/abs/2609.40317v1)**  
  Authors: Zikai Liao, Yumin Suh, Yi Ouyang, Yi-Lun Lee, Yi-Hsuan Tsai, Zhaozheng Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.40317v1.pdf)  
  Keywords: audio-driven, evaluation, flow matching, talking head, video generation  
- **[HelixWorld: A Real-time Interactive Audio-Visual World Model](https://arxiv.org/abs/2609.38123v1)**  
  Authors: Lei Ke, Jiahao Pan, Zeyue Tian, Jiaming Wang, Haoyuan Huang, Kam Man Wu, Pengjun Fang, Hongyu Liu, Chenyang Qi, Lin Wang, Ruibin Yuan, Weijia Chen, Fangneng Zhan, Qifeng Chen, Wei Xue, Yike Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38123v1.pdf)  
  Keywords: distillation, dynamics, interactive, simulation, sound, streaming, trajectory, visual world model, world model, world simulation  
- **[Adaptive Reward Routing: Dynamic Multi-Reward Optimization for Joint Audio-Video Diffusion via Forward-Process RL](https://arxiv.org/abs/2609.37200v1)**  
  Authors: Songlin Yang, Xiaotong Zhao, Jiacheng Zhang, Zhe Wang, Toyota Li, Eric Liu, Alan Zhao, Anyi Rao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.37200v1.pdf)  
  Keywords: efficient, joint audio-video, video diffusion  
- **[Salt++: Context-Aligned Post-Training for Few-Step Streaming Multimodal Generation](https://arxiv.org/abs/2609.36995v1)**  
  Authors: Xingtong Ge, Yutong Wang, Lunjie Zhu, Haitao Lin, Fangyu Lin, Yushi Huang, Xin Zhang, Yi Zhang, Yu Liu, Jun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.36995v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xingtongge.github.io/Saltpp)  
  Keywords: audio-video generation, autoregressive, consistency distillation, distillation, evaluation, streaming, video generation  
- **[Enabling Immersive Audio-Visual Experience from Any Video](https://arxiv.org/abs/2609.36295v1)**  
  Authors: Zitong Lan, Mutian Tong, Jiatao Gu, Mingmin Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.36295v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://huggingface.co/spaces/CuriousAlien000/spatial-audio-360-demo) | [![HuggingFace](https://img.shields.io/badge/-HuggingFace-yellow)](https://huggingface.co/spaces/CuriousAlien000/spatial-audio-360-demo)  
  Keywords: physics, simulation, sound, video generation  
- **[ORAV: Benchmarking Audio-Video Generation from Multimodal Contexts](https://arxiv.org/abs/2609.34843v1)**  
  Authors: Jiacheng Hua, Xiaokun Feng, Jiaqi Hua, Chang Liu, Biao Wang, Miao Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.34843v1.pdf)  
  Keywords: audio-video generation, benchmark, controllable, dynamics, video generation  
- **[SkillPE: Creativity-Oriented Cinematic Skill Evolution for Text-to-Video Prompt Engineering](https://arxiv.org/abs/2609.34335v1)**  
  Authors: Yanwei Huang, Mingxuan Zhu, Shujie Li, Shiyuan Liu, Yuanxing Zhang, Arpit Narechania  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.34335v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Ais0n/SkillPE?style=social)](https://github.com/Ais0n/SkillPE)  
  Keywords: benchmark, cinematic, creative, evaluation, sound, text to video, text-to-video, video generation  
- **[Where and When to Force: Routed Forcing for Streaming Avatars](https://arxiv.org/abs/2609.30963v1)**  
  Authors: Zihan Su, Siwen Lu, Junhao Zhuang, Zeyue Xue, Haoyang Huang, Guanghao Li, Xiaofeng Tan, Chun Yuan, Nan Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.30963v1.pdf)  
  Keywords: audio-driven, avatar, distillation, dynamics, gesture, streaming, video diffusion  
- **[WanPE: Towards Cinematic Prompt Enhancement for Modern Text-to-Video Generation](https://arxiv.org/abs/2609.30221v1)**  
  Authors: Yubo Zhu, Yawen Shao, Ziyun Dai, Zixun Fang, Kai Zhu, Siyang Sun, Haolan Xue, Chuxin Wang, Tingyu Weng, Jingming Luo, Chen Shi, Lianghua Huang, Yufeng Ai, Yuzheng Wang, Wenyuan Zhang, Yu Shang, Yuxiang Bao, Zoubin Bi, Jie Xiao, Jinbo Xing, Jiaxing Zhao, Chongyang Zhong, Hengjian Chen, Chenwei Xie, Akide Liu, Zhehan Kan, Yu Liu, Wei Zhai, Sheng Zhong, Wei Tong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.30221v1.pdf)  
  Keywords: benchmark, cinematic, sound, text to video, text-to-video, video generation  
- **[AV-GRPO: Modality-Anchored Decoupling Diffusion Reinforcement Learning for Joint Audio-Video Generation](https://arxiv.org/abs/2609.29816v3)**  
  Authors: Zhiyu Xu, Weilong Yan, Yufei Shi, Shiyang Li, Yihao Liu, Kin-Man Lam, Yuewen Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.29816v3.pdf) | [![GitHub](https://img.shields.io/github/stars/zhiyuxu03/AV-GRPO?style=social)](https://github.com/zhiyuxu03/AV-GRPO)  
  Keywords: audio-video generation, controllable, dynamics, evaluation, joint audio-video, trajectory, video generation  

### Controllable Generation

*Showing the latest 50 out of 331 papers*

- **[ViTeX-Bench: Benchmarking High-Fidelity Video Scene Text Editing](https://arxiv.org/abs/2609.40356v1)**  
  Authors: Xinghao Chen, Xiangbo Gao, Jiongze Yu, Yuheng Wu, Zhengzhong Tu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.40356v1.pdf)  
  Keywords: benchmark, controllable, dynamics, evaluation, human evaluation, temporal consistency, video editing, video generation  
- **[Dream4ACT: A Shared Visual Action Interface for Multi-Embodiment Video-Action Modeling](https://arxiv.org/abs/2609.40153v1)**  
  Authors: Xiangyu Zhu, Jin Xu, Yue Guo, Xin Wu, Yifan Sun, Xiancong Ren, Jianxin Sun, Yong Dai, Xiaozhu Ju  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.40153v1.pdf)  
  Keywords: action-conditioned, diffusion transformer, dynamics, embodied, flow matching, video autoencoder, video generation, world model  
- **[Grounding with Confidence: Controllable Generative Video Temporal Grounding](https://arxiv.org/abs/2609.39883v1)**  
  Authors: Jinhao Chen, Benlei Cui, Ruijian Jia, Ziheng Wang, Tianyu Wo, Pengfei Sun, Longtao Huang, Hui Xue, Yitong Yang, Haiwen Hong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.39883v1.pdf)  
  Keywords: controllable  
- **[DiffWAM: A Fast and Efficient Navigation World Action Model](https://arxiv.org/abs/2609.39763v1)**  
  Authors: Mo Zhu, Yuze Wu, Xijie Huang, Xiao Cui, Fei Gao, Xin Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.39763v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zzmmzzm.github.io/diffwam.github.io)  
  Keywords: benchmark, efficient, embodied, trajectory, video synthesis  
- **[PartiCam: Camera Controlled Video Generation with Reward Guidance](https://arxiv.org/abs/2609.39504v1)**  
  Authors: Amine Ouasfi, Runjia Li, Junlin Han, Eric Marchand, Philip H. S. Torr, Adnane Boukhayma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.39504v1.pdf)  
  Keywords: camera control, camera motion, camera trajectory, camera-conditioned, trajectory, video diffusion, video generation  
- **[BadAction: Backdoor Attacks on Interactive Video Generation via Action-Guided Triggers](https://arxiv.org/abs/2609.39047v1)**  
  Authors: Zhihang Wu, Zhongqi Wang, Jie Zhang, Fengming Gu, Shiguang Shan, Xilin Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.39047v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wsad55.github.io/badaction01)  
  Keywords: controllable, interactive, video generation  
- **[Visualizing Distribution Coverage in Generative Diffusion Models](https://arxiv.org/abs/2609.38853v1)**  
  Authors: Yifei Wang, Xiaoyu Wu, Tsu-Jui Fu, Chen Chen, Liang-Chieh Chen, Zhe Gan, Chen Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38853v1.pdf)  
  Keywords: diffusion distillation, distillation, evaluation, trajectory, video generation  
- **[FrameMorrow: Future-guided Frame Selection with Prospective Tokens for Long-Horizon Video Generation](https://arxiv.org/abs/2609.38839v1)**  
  Authors: Bo Yin, Xiaobin Hu, Jiaqi Zhao, Shuicheng Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38839v1.pdf)  
  Keywords: action-conditioned, interactive, long video, video generation  
- **[ThinkV2V: Unleashing the Reasoning Capability of MLLMs for Instruction-Guided Video Editing](https://arxiv.org/abs/2609.38541v1)**  
  Authors: Donghao Zhou, Haoyang He, Fan Zhang, Hao Yang, Guisheng Liu, Xin Gao, Zhongwei Wan, Xingyuan Bu, Jie Wang, Qiangpeng Yang, Shilei Wen, Chi-Wing Fu, Pheng-Ann Heng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38541v1.pdf)  
  Keywords: architecture, dit, evaluation, instruction-guided, video editing  
- **[FracGen: Learning How Objects Stretch and Tear with Physics-Informed Video Generation](https://arxiv.org/abs/2609.38152v1)**  
  Authors: Trong-Tung Nguyen, Jiahan Zhang, Anand Bhattad  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38152v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://fracgen.github.io)  
  Keywords: benchmark, controllable, dynamics, physical, physical plausibility, physics, physics-informed, simulation, video generation  

### Human & Character Animation

*Showing the latest 50 out of 63 papers*

- **[GLARE: Generating Listening Heads with Appropriate Reactions](https://arxiv.org/abs/2609.40317v1)**  
  Authors: Zikai Liao, Yumin Suh, Yi Ouyang, Yi-Lun Lee, Yi-Hsuan Tsai, Zhaozheng Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.40317v1.pdf)  
  Keywords: audio-driven, evaluation, flow matching, talking head, video generation  
- **[TexTailor: Texture-Preserving Video Virtual Try-On via Adaptive Garment Conditioning](https://arxiv.org/abs/2609.39335v1)**  
  Authors: Zijing Qin, Jun Zhou, Ruicheng Zhang, Jiaqi Hou, Zunnan Xu, Ronghui Li, Zhenyu Xie, Xiu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.39335v1.pdf)  
  Keywords: denoising, diffusion transformer, temporal consistency, video diffusion, video diffusion transformer, virtual try-on  
- **[Geometry-Preserving Human-to-Robot Upper-Body Motion Retargeting from Monocular Video](https://arxiv.org/abs/2609.37776v1)**  
  Authors: Xiaoyu Yang, Sen Han, Da Li, Nan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.37776v1.pdf)  
  Keywords: body motion, physical, simulation, video generation  
- **[WeLike2Party! In-Context Motion Transfer for Multi-Human Image Animation](https://arxiv.org/abs/2609.36937v1)**  
  Authors: Sangeyl Lee, Seunghyun Shin, Seungho Park, Wooseok Jeon, Hae-Gon Jeon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.36937v1.pdf)  
  Keywords: benchmark, driving, human animation, human image animation, identity, image animation, motion transfer, trajectory, video generation  
- **[FlowAct-R2: Beyond Talking Avatar via Streaming Multimodal References and Proactive Agent Planning](https://arxiv.org/abs/2609.35728v1)**  
  Authors: Ziyao Huang, Zhengkun Rong, Shiyang Qin, Shuang Liang, Wentao Hu, Yuxuan Luo, Yuan Zhang, Mingyuan Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.35728v1.pdf)  
  Keywords: avatar, diffusion transformer, interactive, streaming, talking avatar, video generation  
- **[WB-WAM: Heterogeneous Body-Hand Pre-training for Humanoid Loco-Manipulation](https://arxiv.org/abs/2609.34199v2)**  
  Authors: Chuan Qin, Shaoting Zhu, Siyuan Luo, Siqiao Huang, Hongyu Zhao, Shanaka Baduge, Hang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.34199v2.pdf)  
  Keywords: body motion, efficient, human motion, motion transfer, physical, simulation  
- **[Where and When to Force: Routed Forcing for Streaming Avatars](https://arxiv.org/abs/2609.30963v1)**  
  Authors: Zihan Su, Siwen Lu, Junhao Zhuang, Zeyue Xue, Haoyang Huang, Guanghao Li, Xiaofeng Tan, Chun Yuan, Nan Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.30963v1.pdf)  
  Keywords: audio-driven, avatar, distillation, dynamics, gesture, streaming, video diffusion  
- **[All modalities are equal, but video is more equal: Closing the Cross-Attention Gap in Joint Video Generation](https://arxiv.org/abs/2609.27901v1)**  
  Authors: Ohad Rahamim, Dvir Samuel, Idan Schwartz, Gal Chechik  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.27901v1.pdf)  
  Keywords: body motion, physical, video generation  
- **[Vidu S2: Real-Time Interactive, Editable, and Spatial Video Generation](https://arxiv.org/abs/2609.11638v1)**  
  Authors: Jintao Zhang, Kai Jiang, Jintao Chen, Xu Wang, Deyuan Liu, Jungang Li, Dechuang Chen, Ming Lin, Jingjiang Zhou, Haopeng Jin, Qi Jia, Xiaohang Wang, Yaole Wang, Zhanqiang Zhang, Ran Li, Zhengkun Huang, Shuyue Xiong, Yuji Wang, Zikun Dai, Hui He, Yang Luo, Mang Ning, Weiqi Feng, Chengyang Ye, Xinyue Lin, Min Zhao, Hongzhou Zhu, Hengkai Tan, Zeyuan Wang, Chendong Xiang, Kaiwen Zheng, Zhijie Deng, Fan Bao, Jianfei Chen, Jun Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.11638v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vidu.com/vidu-stream)  
  Keywords: avatar, interactive, style, video editing, video generation  
- **[Decoupled Self-Forcing Distillation for Streaming Talking Head Generation](https://arxiv.org/abs/2609.10317v1)**  
  Authors: Yanru An, Ruiyan Wang, Wenwu Wei, Rui Bu, Qi Wang, Hongwei Hu, Zhengxue Cheng, Rong Xie, Li Song, Wenjun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.10317v1.pdf)  
  Keywords: autoregressive, diffusion model, distillation, driving, identity, streaming, talking head, video diffusion  

### Image-to-Video Generation

*Showing the latest 50 out of 91 papers*

- **[MindWorldBench: Evaluating Mental-State-to-Behavior Reasoning in Image-to-Video Generation](https://arxiv.org/abs/2609.39147v1)**  
  Authors: Ruiqi Li, Xuanyi Liu, Sijia Li, Haofeng Wang, Yuxin Liu, Feng Xie, Songchao Tan, Shiqi Wang, Hanwei Zhu, Yizong Wang, Chuanmin Jia, Siwei Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.39147v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://richard2049-lee.github.io/MindWorldBench)  
  Keywords: image to video, image-to-video, physical, physical plausibility, video generation  
- **[LIFT: Layout-In-Future Video Generation under Large Viewpoint Change via On-Policy Self-Distillation](https://arxiv.org/abs/2609.38146v1)**  
  Authors: Shengxiang Ji, Boyang Wang, Haiyang Xu, Bingnan Li, Yucheng Mao, Zeyuan Chen, Xiaojun Shan, Xiang Zhang, Gang Hua, Jianwen Xie, Zezhou Cheng, Zhuowen Tu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38146v1.pdf)  
  Keywords: camera control, controllable, distillation, image to video, image-to-video, layout, video generation  
- **[WeLike2Party! In-Context Motion Transfer for Multi-Human Image Animation](https://arxiv.org/abs/2609.36937v1)**  
  Authors: Sangeyl Lee, Seunghyun Shin, Seungho Park, Wooseok Jeon, Hae-Gon Jeon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.36937v1.pdf)  
  Keywords: benchmark, driving, human animation, human image animation, identity, image animation, motion transfer, trajectory, video generation  
- **[Beyond Legibility: Benchmarking Visual Text Rendering and In-Place Editing in Unified Video Generation](https://arxiv.org/abs/2609.36598v2)**  
  Authors: Ziying Zhang, Litao Li, Junchao Liao, Tianyi Zeng, Siyu Zhu, Long Qin, Zhenghao Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.36598v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://huggingface.co/datasets/Vicky0720/VidScribe.) | [![Dataset](https://img.shields.io/badge/-Dataset-orange)](https://huggingface.co/datasets/Vicky0720/VidScribe)  
  Keywords: benchmark, dynamics, evaluation, i2v, identity, physical, t2v, v2v, video generation  
- **[OPIS: An Input-Grounded Benchmark for Multi-Object Memory in Video World Models](https://arxiv.org/abs/2609.35052v1)**  
  Authors: Hao Wang, Tao Yu, Liuzhou Zhang, HeXin Wang, Haopeng Jin, Yuxuan Zhou, Xinming Wang, Hongzhu Yi, Xinye Li, Yuanlei Wang, Ping Nie, Yan Huang, Yuxuan Zhang, Pengfei Zhou, Yanyan Zou, Wei Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.35052v1.pdf)  
  Keywords: benchmark, camera-conditioned, embodied, evaluation, game, identity, image to video, image-to-video  
- **[From Static to Dynamic: On-Policy Distillation from Image to Video Diffusion Models](https://arxiv.org/abs/2609.34371v1)**  
  Authors: Bingqing Jiang, Li Luo, Zichao Yu, Yujin Han, Zhaolong Su, Difan Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.34371v1.pdf)  
  Keywords: distillation, dynamics, image to video, image-to-video, temporal consistency, trajectory, video diffusion, video generation  
- **[Cache-Aware Conv3D Lowering Across Embedded World-Model Decoders](https://arxiv.org/abs/2609.31938v1)**  
  Authors: Jiaming Zhang, Wu Yang, Shuai Tao, Wulong Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.31938v1.pdf)  
  Keywords: acceleration, embodied, image to video, image-to-video, layout, world model  
- **[SparkDiffusion: Mitigating the High-Sparsity Trap --- A Unified Framework for up to $265\times$ Single-GPU Acceleration of Visual Generation](https://arxiv.org/abs/2609.23153v1)**  
  Authors: Yuxi Liu, Haoyu Li, Zekun Zhang, Tengxu Sun, Yixiang Cai, Jiayong Li, Yifei Xia, Tianle Liu, Baole Ai, Ang Wang, Jiamang Wang, Lin Qu, Kai Zhang, Kun Yuan, Bin Cui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.23153v1.pdf)  
  Keywords: acceleration, architecture, distillation, i2v, t2v, trajectory, video diffusion  
- **[DART: Distillation-Aware Reparameterization for Training-Free LoRA Reuse in Few-Step Video Diffusion Models](https://arxiv.org/abs/2609.20051v2)**  
  Authors: Shihong Li, Juntao Xu, JinCao, Maowen Tang, Jun Huang, Jintao Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.20051v2.pdf)  
  Keywords: denoising, distillation, i2v, image to video, image-to-video, video diffusion, video generation  
- **[Astronex-World 1.0: Real-Time Interactive World Model Foundation](https://arxiv.org/abs/2609.20034v1)**  
  Authors: Xin Zhou, Cong Miao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.20034v1.pdf)  
  Keywords: autonomous driving, controllable, driving, dynamics, embodied, image to video, image-to-video, interactive, text to video, text-to-video, video world model, world model  

### Long Video Generation

*Showing the latest 50 out of 255 papers*

- **[ViTeX-Bench: Benchmarking High-Fidelity Video Scene Text Editing](https://arxiv.org/abs/2609.40356v1)**  
  Authors: Xinghao Chen, Xiangbo Gao, Jiongze Yu, Yuheng Wu, Zhengzhong Tu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.40356v1.pdf)  
  Keywords: benchmark, controllable, dynamics, evaluation, human evaluation, temporal consistency, video editing, video generation  
- **[LOCI: Spatial Linear Memory for Streaming World Models](https://arxiv.org/abs/2609.40222v1)**  
  Authors: Ji Xia, Tingting Liao, Xuezhi Liang, Hao Li, Guangyi Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.40222v1.pdf)  
  Keywords: architecture, benchmark, streaming, video world model, world model  
- **[Enhancing Autoregressive Video Generation via Representation Adversarial Distillation](https://arxiv.org/abs/2609.40037v1)**  
  Authors: Fangyu Lin, Xingtong Ge, Lunjie Zhu, Yi Zhang, Zhening Liu, Tianhang Wang, Mengfei Li, Yumeng Zhang, Guanglu Song, Yu Liu, Jun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.40037v1.pdf)  
  Keywords: architecture, autoregressive, autoregressive video, denoising, distillation, efficient, minute-long, streaming, video generation  
- **[TexTailor: Texture-Preserving Video Virtual Try-On via Adaptive Garment Conditioning](https://arxiv.org/abs/2609.39335v1)**  
  Authors: Zijing Qin, Jun Zhou, Ruicheng Zhang, Jiaqi Hou, Zunnan Xu, Ronghui Li, Zhenyu Xie, Xiu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.39335v1.pdf)  
  Keywords: denoising, diffusion transformer, temporal consistency, video diffusion, video diffusion transformer, virtual try-on  
- **[DeCoPrune: Efficient KV-Cache Pruning for Autoregressive Video Diffusion via Denoising Consistency](https://arxiv.org/abs/2609.39096v1)**  
  Authors: Zeqi Xiao, Qingle Liu, Kaiwen Zhang, Yifan Zhou, Zihan Ding, Xingang Pan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.39096v1.pdf) | [![GitHub](https://img.shields.io/github/stars/DeCoPrune/CMBench?style=social)](https://github.com/DeCoPrune/CMBench) | [![Project](https://img.shields.io/badge/-Project-blue)](https://decoprune.github.io) | [![Dataset](https://img.shields.io/badge/-Dataset-orange)](https://huggingface.co/datasets/Aoraku/CMBench)  
  Keywords: autoregressive, autoregressive video, benchmark, denoising, efficient, interactive, streaming, video diffusion  
- **[FrameMorrow: Future-guided Frame Selection with Prospective Tokens for Long-Horizon Video Generation](https://arxiv.org/abs/2609.38839v1)**  
  Authors: Bo Yin, Xiaobin Hu, Jiaqi Zhao, Shuicheng Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38839v1.pdf)  
  Keywords: action-conditioned, interactive, long video, video generation  
- **[Future Video Generation Better Aligns with the Human Visual Cortex than Observed Video](https://arxiv.org/abs/2609.38819v1)**  
  Authors: Chang-Bae Bang, Hyungjin Chung, Byung-Hoon Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38819v1.pdf)  
  Keywords: autoregressive, diffusion model, video diffusion, video generation  
- **[No Corners Cut: State-Grounded Transitions for Mid-Stream Prompt Switches in Video Generation](https://arxiv.org/abs/2609.38691v1)**  
  Authors: Zejing Rao, Ketong Ren, Xiaoqiang Liu, Yiping Meng, Guoxin Zhang, Fan Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38691v1.pdf)  
  Keywords: autoregressive, benchmark, streaming, video generation, video synthesis  
- **[PixelUMM: Encoder-Free Unified Image and Video Understanding and Generation](https://arxiv.org/abs/2609.38597v1)**  
  Authors: Cong Wei, Xuanchi Ren, Bryan Chu, Weiming Ren, Huan Ling, Jiahui Huang, Laura Leal-Taixé, Sanja Fidler, Wenhu Chen, Zian Wang, Jay Zhangjie Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38597v1.pdf)  
  Keywords: architecture, autoregressive, flow matching, video generation  
- **[LongTake: Learning to Sustain Dynamics in Long-Horizon Video Generation](https://arxiv.org/abs/2609.38562v1)**  
  Authors: Byoungwoo Park, Jaemoo Choi, Juho Lee, Yongxin Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38562v1.pdf)  
  Keywords: autoregressive, distillation, dynamics, game, video diffusion, video generation  

### Personalization & Customization

*Showing the latest 50 out of 165 papers*

- **[FOMO: Forget the Concept, Don't Miss Out on the Scene in Selective Video Unlearning](https://arxiv.org/abs/2609.39605v1)**  
  Authors: Łukasz Rudnik, Agnieszka Polowczyk, Alicja Polowczyk, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.39605v1.pdf) | [![GitHub](https://img.shields.io/github/stars/gmum/FOMO?style=social)](https://github.com/gmum/FOMO) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gmum.github.io/FOMO)  
  Keywords: concept, dynamics  
- **[Strike a Chord! Modal Kinetic Typography](https://arxiv.org/abs/2609.38325v1)**  
  Authors: Maham Tanveer, Jiyeon Han, Nanxuan Zhao, Hao Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38325v1.pdf)  
  Keywords: concept, diffusion model, distillation, video diffusion  
- **[DIET: Deletion-response Expert Trimming for Video Diffusion Transformers](https://arxiv.org/abs/2609.37829v1)**  
  Authors: Jiachang Zhang, Teng Hu, Bohao Feng, Songhang Shen, Wenqiang Wang, Hongqian Deng, Ran Yi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.37829v1.pdf)  
  Keywords: one-shot, video diffusion  
- **[WeLike2Party! In-Context Motion Transfer for Multi-Human Image Animation](https://arxiv.org/abs/2609.36937v1)**  
  Authors: Sangeyl Lee, Seunghyun Shin, Seungho Park, Wooseok Jeon, Hae-Gon Jeon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.36937v1.pdf)  
  Keywords: benchmark, driving, human animation, human image animation, identity, image animation, motion transfer, trajectory, video generation  
- **[Motion Concept Unlearning in Video Diffusion Models](https://arxiv.org/abs/2609.36832v1)**  
  Authors: Ping Liu, Chi Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.36832v1.pdf)  
  Keywords: concept, denoising, dit, dynamics, t2v, text to video, text-to-video, video diffusion, video dit, video generation  
- **[Beyond Legibility: Benchmarking Visual Text Rendering and In-Place Editing in Unified Video Generation](https://arxiv.org/abs/2609.36598v2)**  
  Authors: Ziying Zhang, Litao Li, Junchao Liao, Tianyi Zeng, Siyu Zhu, Long Qin, Zhenghao Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.36598v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://huggingface.co/datasets/Vicky0720/VidScribe.) | [![Dataset](https://img.shields.io/badge/-Dataset-orange)](https://huggingface.co/datasets/Vicky0720/VidScribe)  
  Keywords: benchmark, dynamics, evaluation, i2v, identity, physical, t2v, v2v, video generation  
- **[GeoVerse: World-Consistent Novel View Synthesis in Geometric Latent Space](https://arxiv.org/abs/2609.35734v2)**  
  Authors: Kerui Ren, Tao Lu, Linning Xu, Changjian Jiang, Mu Huang, Chunhua Shen, Mulin Yu, Bo Dai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.35734v2.pdf)  
  Keywords: diffusion model, novel view, style  
- **[OPIS: An Input-Grounded Benchmark for Multi-Object Memory in Video World Models](https://arxiv.org/abs/2609.35052v1)**  
  Authors: Hao Wang, Tao Yu, Liuzhou Zhang, HeXin Wang, Haopeng Jin, Yuxuan Zhou, Xinming Wang, Hongzhu Yi, Xinye Li, Yuanlei Wang, Ping Nie, Yan Huang, Yuxuan Zhang, Pengfei Zhou, Yanyan Zou, Wei Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.35052v1.pdf)  
  Keywords: benchmark, camera-conditioned, embodied, evaluation, game, identity, image to video, image-to-video  
- **[TemplateCraft: Agentic Visual Template Generation](https://arxiv.org/abs/2609.31451v1)**  
  Authors: Hongjie Yu, Zhiyuan Fan, Yuzhe Zhang, Jiangcun Du, Zhicheng Gao, Yuhong Zhang, Xiaokai Zhan, Zongshi Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.31451v1.pdf)  
  Keywords: evaluation, style, video generation  
- **[NavGen: Visual Generative Models as a Scalable Data Engine for Embodied 3D Navigation](https://arxiv.org/abs/2609.30770v1)**  
  Authors: Xijie Huang, Yongyang Wan, Chengbin Dong, Zimo Ding, Mo Zhu, Yijin Wang, Zhiyang Liu, Fei Gao, Yuze Wu, Xin Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.30770v1.pdf)  
  Keywords: embodied, style, text to video, text-to-video  

### Physical Understanding

*Showing the latest 50 out of 309 papers*

- **[Physis-Lang: Self-Evolving Language as a Physical Representation for Video World Model](https://arxiv.org/abs/2609.40358v1)**  
  Authors: Liming Lu, Xianzheng Ma, Wenkun He, Guanqi Zhan, Yilin Zhao, Junyu Chen, Mengyao Xu, Jiaojiao Fan, Wenhang Ge, Yuchao Gu, Yunze Liu, Boyi Li, Zhen Dong, Victor Prisacariu, Ming-Yu Liu, Song Han, Han Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.40358v1.pdf)  
  Keywords: physical, physical plausibility, video generation, video world model, world model  
- **[ViTeX-Bench: Benchmarking High-Fidelity Video Scene Text Editing](https://arxiv.org/abs/2609.40356v1)**  
  Authors: Xinghao Chen, Xiangbo Gao, Jiongze Yu, Yuheng Wu, Zhengzhong Tu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.40356v1.pdf)  
  Keywords: benchmark, controllable, dynamics, evaluation, human evaluation, temporal consistency, video editing, video generation  
- **[Dream4ACT: A Shared Visual Action Interface for Multi-Embodiment Video-Action Modeling](https://arxiv.org/abs/2609.40153v1)**  
  Authors: Xiangyu Zhu, Jin Xu, Yue Guo, Xin Wu, Yifan Sun, Xiancong Ren, Jianxin Sun, Yong Dai, Xiaozhu Ju  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.40153v1.pdf)  
  Keywords: action-conditioned, diffusion transformer, dynamics, embodied, flow matching, video autoencoder, video generation, world model  
- **[VR-JEPA: Learning Contrastive-State Latent Guidance for Generation-based Video Reasoning](https://arxiv.org/abs/2609.40129v1)**  
  Authors: Zehua Ma, Kun Xiang, Yunshuang Nie, Quanlin Chen, Haoyuan Li, Xiuwei Chen, Jiang Ji, Haijun Wu, Zhenyu Xie, Michael Kampffmeyer, Hanhui Li, Xiaodan Liang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.40129v1.pdf)  
  Keywords: architecture, dynamics, physical, video generation  
- **[FOMO: Forget the Concept, Don't Miss Out on the Scene in Selective Video Unlearning](https://arxiv.org/abs/2609.39605v1)**  
  Authors: Łukasz Rudnik, Agnieszka Polowczyk, Alicja Polowczyk, Przemysław Spurek  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.39605v1.pdf) | [![GitHub](https://img.shields.io/github/stars/gmum/FOMO?style=social)](https://github.com/gmum/FOMO) | [![Project](https://img.shields.io/badge/-Project-blue)](https://gmum.github.io/FOMO)  
  Keywords: concept, dynamics  
- **[GroundingPI: A Grounding Foundation Model towards Physical Intelligence with Visual Primitives](https://arxiv.org/abs/2609.39601v1)**  
  Authors: Qize Yu, Lianrui Fan, Boyu Chen, Jiaqi Liang, Xini Ding, Yue Chen, Zetian Song, Yuran Wang, Yi Zou, Kaixuan Wang, Tianxing Chen, Wenxuan Song, Bohan Zhou, Mingleyang Li, Siqiao Huang, Yuqi Ye, Caigao Jiang, Wei Wei, Ruihai Wu, Hang Zhang, Yixiao Ge, Shuchang Zhou, Shilong Liu, Xianming Liu, Ping Luo, Shiyu Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.39601v1.pdf)  
  Keywords: autonomous driving, driving, physical, video generation  
- **[MindWorldBench: Evaluating Mental-State-to-Behavior Reasoning in Image-to-Video Generation](https://arxiv.org/abs/2609.39147v1)**  
  Authors: Ruiqi Li, Xuanyi Liu, Sijia Li, Haofeng Wang, Yuxin Liu, Feng Xie, Songchao Tan, Shiqi Wang, Hanwei Zhu, Yizong Wang, Chuanmin Jia, Siwei Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.39147v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://richard2049-lee.github.io/MindWorldBench)  
  Keywords: image to video, image-to-video, physical, physical plausibility, video generation  
- **[LongTake: Learning to Sustain Dynamics in Long-Horizon Video Generation](https://arxiv.org/abs/2609.38562v1)**  
  Authors: Byoungwoo Park, Jaemoo Choi, Juho Lee, Yongxin Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38562v1.pdf)  
  Keywords: autoregressive, distillation, dynamics, game, video diffusion, video generation  
- **[Rethinking Representations for World-Action Modeling](https://arxiv.org/abs/2609.38163v1)**  
  Authors: Haoyi Jiang, Liu Liu, Xinjiang Wang, Zhihao Sun, Zequn Chen, Sen Wang, Xinjie Wang, Xia Chen, Jingfeng Yao, Weiheng Zhao, Shanglin Yuan, Zhizhong Su, Wei Sui, Wenyu Liu, Xinggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38163v1.pdf)  
  Keywords: dynamics, embodied, world model  
- **[FracGen: Learning How Objects Stretch and Tear with Physics-Informed Video Generation](https://arxiv.org/abs/2609.38152v1)**  
  Authors: Trong-Tung Nguyen, Jiahan Zhang, Anand Bhattad  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38152v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://fracgen.github.io)  
  Keywords: benchmark, controllable, dynamics, physical, physical plausibility, physics, physics-informed, simulation, video generation  

### Surveys & Benchmarks

*Showing the latest 50 out of 312 papers*

- **[ViTeX-Bench: Benchmarking High-Fidelity Video Scene Text Editing](https://arxiv.org/abs/2609.40356v1)**  
  Authors: Xinghao Chen, Xiangbo Gao, Jiongze Yu, Yuheng Wu, Zhengzhong Tu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.40356v1.pdf)  
  Keywords: benchmark, controllable, dynamics, evaluation, human evaluation, temporal consistency, video editing, video generation  
- **[GLARE: Generating Listening Heads with Appropriate Reactions](https://arxiv.org/abs/2609.40317v1)**  
  Authors: Zikai Liao, Yumin Suh, Yi Ouyang, Yi-Lun Lee, Yi-Hsuan Tsai, Zhaozheng Yin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.40317v1.pdf)  
  Keywords: audio-driven, evaluation, flow matching, talking head, video generation  
- **[LOCI: Spatial Linear Memory for Streaming World Models](https://arxiv.org/abs/2609.40222v1)**  
  Authors: Ji Xia, Tingting Liao, Xuezhi Liang, Hao Li, Guangyi Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.40222v1.pdf)  
  Keywords: architecture, benchmark, streaming, video world model, world model  
- **[DiffWAM: A Fast and Efficient Navigation World Action Model](https://arxiv.org/abs/2609.39763v1)**  
  Authors: Mo Zhu, Yuze Wu, Xijie Huang, Xiao Cui, Fei Gao, Xin Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.39763v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zzmmzzm.github.io/diffwam.github.io)  
  Keywords: benchmark, efficient, embodied, trajectory, video synthesis  
- **[DeCoPrune: Efficient KV-Cache Pruning for Autoregressive Video Diffusion via Denoising Consistency](https://arxiv.org/abs/2609.39096v1)**  
  Authors: Zeqi Xiao, Qingle Liu, Kaiwen Zhang, Yifan Zhou, Zihan Ding, Xingang Pan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.39096v1.pdf) | [![GitHub](https://img.shields.io/github/stars/DeCoPrune/CMBench?style=social)](https://github.com/DeCoPrune/CMBench) | [![Project](https://img.shields.io/badge/-Project-blue)](https://decoprune.github.io) | [![Dataset](https://img.shields.io/badge/-Dataset-orange)](https://huggingface.co/datasets/Aoraku/CMBench)  
  Keywords: autoregressive, autoregressive video, benchmark, denoising, efficient, interactive, streaming, video diffusion  
- **[Visualizing Distribution Coverage in Generative Diffusion Models](https://arxiv.org/abs/2609.38853v1)**  
  Authors: Yifei Wang, Xiaoyu Wu, Tsu-Jui Fu, Chen Chen, Liang-Chieh Chen, Zhe Gan, Chen Wei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38853v1.pdf)  
  Keywords: diffusion distillation, distillation, evaluation, trajectory, video generation  
- **[No Corners Cut: State-Grounded Transitions for Mid-Stream Prompt Switches in Video Generation](https://arxiv.org/abs/2609.38691v1)**  
  Authors: Zejing Rao, Ketong Ren, Xiaoqiang Liu, Yiping Meng, Guoxin Zhang, Fan Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38691v1.pdf)  
  Keywords: autoregressive, benchmark, streaming, video generation, video synthesis  
- **[ThinkV2V: Unleashing the Reasoning Capability of MLLMs for Instruction-Guided Video Editing](https://arxiv.org/abs/2609.38541v1)**  
  Authors: Donghao Zhou, Haoyang He, Fan Zhang, Hao Yang, Guisheng Liu, Xin Gao, Zhongwei Wan, Xingyuan Bu, Jie Wang, Qiangpeng Yang, Shilei Wen, Chi-Wing Fu, Pheng-Ann Heng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38541v1.pdf)  
  Keywords: architecture, dit, evaluation, instruction-guided, video editing  
- **[FracGen: Learning How Objects Stretch and Tear with Physics-Informed Video Generation](https://arxiv.org/abs/2609.38152v1)**  
  Authors: Trong-Tung Nguyen, Jiahan Zhang, Anand Bhattad  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38152v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://fracgen.github.io)  
  Keywords: benchmark, controllable, dynamics, physical, physical plausibility, physics, physics-informed, simulation, video generation  
- **[WorldLine: Action-Driven Visual Simulation for Robotic Manipulation](https://arxiv.org/abs/2609.38059v1)**  
  Authors: Shenghe Zheng, Wenbo Li, Jiyao Zhang, Bin Xia, Haoyang Huang, Nan Duan, Jiaya Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38059v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zhengsh123.github.io/WorldLine)  
  Keywords: action-conditioned, distillation, dynamics, efficient, embodied, evaluation, physical, robot learning, simulation, trajectory, video generation  

### Text-to-Video Generation

*Showing the latest 50 out of 147 papers*

- **[Motion Concept Unlearning in Video Diffusion Models](https://arxiv.org/abs/2609.36832v1)**  
  Authors: Ping Liu, Chi Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.36832v1.pdf)  
  Keywords: concept, denoising, dit, dynamics, t2v, text to video, text-to-video, video diffusion, video dit, video generation  
- **[Beyond Legibility: Benchmarking Visual Text Rendering and In-Place Editing in Unified Video Generation](https://arxiv.org/abs/2609.36598v2)**  
  Authors: Ziying Zhang, Litao Li, Junchao Liao, Tianyi Zeng, Siyu Zhu, Long Qin, Zhenghao Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.36598v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://huggingface.co/datasets/Vicky0720/VidScribe.) | [![Dataset](https://img.shields.io/badge/-Dataset-orange)](https://huggingface.co/datasets/Vicky0720/VidScribe)  
  Keywords: benchmark, dynamics, evaluation, i2v, identity, physical, t2v, v2v, video generation  
- **[CoRe: Co-Evolving Reward Models for Mitigating Latent Reward Hacking in Video Diffusion Models](https://arxiv.org/abs/2609.36245v1)**  
  Authors: Zhaolong Su, Yujin Han, Feng Wang, Jameson Dong, Hins Hu, Difan Zou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.36245v1.pdf)  
  Keywords: efficient, t2v, video diffusion  
- **[Generative Uncertainty as a Self-supervised Signal for Semantic Similarity Learning](https://arxiv.org/abs/2609.35341v1)**  
  Authors: Enrico Pallotta, Sina Raoufi, Lars Doorenbos, Gianni Franchi, Juergen Gall  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.35341v1.pdf)  
  Keywords: t2v, text to video, text-to-video  
- **[G$^3$-LoRA: Organizing Reward-Weighted Video Data with Gradient-Guided Grouped LoRA](https://arxiv.org/abs/2609.35189v1)**  
  Authors: Jia Song, Wenhow Li, Lichen Bai, Bada Ye, Zeke Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.35189v1.pdf)  
  Keywords: camera motion, denoising, distillation, evaluation, flow matching, t2v, text to video, text-to-video  
- **[Advancing Video-Text Pretraining with Multi-View Captions](https://arxiv.org/abs/2609.35090v1)**  
  Authors: Fida M. Thoker, Renaud Vandeghen, Karen Sanchez, Marc Van Droogenbroeck, Bernard Ghanem  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.35090v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://rvandeghen.github.io/mvc)  
  Keywords: text to video, text-to-video  
- **[SkillPE: Creativity-Oriented Cinematic Skill Evolution for Text-to-Video Prompt Engineering](https://arxiv.org/abs/2609.34335v1)**  
  Authors: Yanwei Huang, Mingxuan Zhu, Shujie Li, Shiyuan Liu, Yuanxing Zhang, Arpit Narechania  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.34335v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Ais0n/SkillPE?style=social)](https://github.com/Ais0n/SkillPE)  
  Keywords: benchmark, cinematic, creative, evaluation, sound, text to video, text-to-video, video generation  
- **[Carnator: Fast Text-to-Video Generation with Generation-Native Compatibility-Guided Cross-Request Reuse](https://arxiv.org/abs/2609.32420v1)**  
  Authors: Xingkun Yin, Xuebin Tang, Mingkun Xu, Hongyang Du  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.32420v1.pdf)  
  Keywords: acceleration, denoising, interactive, sparse attention, text to video, text-to-video, trajectory, video diffusion, video generation  
- **[TempQ-Jail: Query-Constrained Candidate Ranking for Text-to-Video Jailbreak Attacks](https://arxiv.org/abs/2609.31032v1)**  
  Authors: Tianmeng Fang, Jiancheng Wang, Chen Wang, Liming Wang, Wei Wang, Jiayang Liu, Xiaochun Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.31032v1.pdf)  
  Keywords: evaluation, t2v, text to video, text-to-video, trajectory, video generation  
- **[NavGen: Visual Generative Models as a Scalable Data Engine for Embodied 3D Navigation](https://arxiv.org/abs/2609.30770v1)**  
  Authors: Xijie Huang, Yongyang Wan, Chengbin Dong, Zimo Ding, Mo Zhu, Yijin Wang, Zhiyang Liu, Fei Gao, Yuze Wu, Xin Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.30770v1.pdf)  
  Keywords: embodied, style, text to video, text-to-video  

### Video Editing

*Showing the latest 50 out of 97 papers*

- **[ViTeX-Bench: Benchmarking High-Fidelity Video Scene Text Editing](https://arxiv.org/abs/2609.40356v1)**  
  Authors: Xinghao Chen, Xiangbo Gao, Jiongze Yu, Yuheng Wu, Zhengzhong Tu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.40356v1.pdf)  
  Keywords: benchmark, controllable, dynamics, evaluation, human evaluation, temporal consistency, video editing, video generation  
- **[ThinkV2V: Unleashing the Reasoning Capability of MLLMs for Instruction-Guided Video Editing](https://arxiv.org/abs/2609.38541v1)**  
  Authors: Donghao Zhou, Haoyang He, Fan Zhang, Hao Yang, Guisheng Liu, Xin Gao, Zhongwei Wan, Xingyuan Bu, Jie Wang, Qiangpeng Yang, Shilei Wen, Chi-Wing Fu, Pheng-Ann Heng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38541v1.pdf)  
  Keywords: architecture, dit, evaluation, instruction-guided, video editing  
- **[Counterfactual Video Generation Enables Scalable Humanoid Loco-Manipulation](https://arxiv.org/abs/2609.38172v1)**  
  Authors: Zihan Wang, Zhen Wu, Pieter Abbeel, Rocky Duan, Jitendra Malik, Carmelo Sferrazza, C. Karen Liu, Guanya Shi, Angjoo Kanazawa  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38172v1.pdf)  
  Keywords: v2v, video generation, video to video, video-to-video  
- **[Beyond Legibility: Benchmarking Visual Text Rendering and In-Place Editing in Unified Video Generation](https://arxiv.org/abs/2609.36598v2)**  
  Authors: Ziying Zhang, Litao Li, Junchao Liao, Tianyi Zeng, Siyu Zhu, Long Qin, Zhenghao Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.36598v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://huggingface.co/datasets/Vicky0720/VidScribe.) | [![Dataset](https://img.shields.io/badge/-Dataset-orange)](https://huggingface.co/datasets/Vicky0720/VidScribe)  
  Keywords: benchmark, dynamics, evaluation, i2v, identity, physical, t2v, v2v, video generation  
- **[Reimagine Video Dynamics](https://arxiv.org/abs/2609.36496v1)**  
  Authors: Yu Yuan, Yawen Lu, Guoxian Song, Kevin Duarte, Ratheesh Kalarot, Di Chang, Xijun Wang, Stanley H. Chan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.36496v1.pdf)  
  Keywords: dynamics, video editing  
- **[Timeline-Bench: Evaluating Agents on Realistic Video-Editing Tasks, from Raw Footage to Final Cut](https://arxiv.org/abs/2609.35143v1)**  
  Authors: Gunin Gupta, Nirmit Arora, Pavan Kalyan Tankala  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.35143v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://timelinebench.tensortest.com)  
  Keywords: benchmark, creative, video editing  
- **[VideoPhysEdit: Physical Counterfactual Video Editing via Rigid-Body Physical Scene Reconstruction](https://arxiv.org/abs/2609.35134v1)**  
  Authors: Conghan Yue, Yuanjie Chen, Yue Han, Ya Gao, Yunyan Xiao, WeiYao Zhang, Zhineng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.35134v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Hammour-steak/VideoPhysEdit?style=social)](https://github.com/Hammour-steak/VideoPhysEdit)  
  Keywords: benchmark, evaluation, physical, physics, simulation, video editing, video generation  
- **[Enhanced Video Text Editing with Trajectory-Aligned Glyph Rendering](https://arxiv.org/abs/2609.34178v1)**  
  Authors: Shulian Zhang, Xiangyu Shu, Wenbo Li, Jian Chen, Yong Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.34178v1.pdf)  
  Keywords: benchmark, trajectory, video diffusion, video editing  
- **[DataMagic: Authoring Data Videos through Declarative Multi-Agent Orchestration](https://arxiv.org/abs/2609.33403v1)**  
  Authors: Yupeng Xie, Zhenyang Wang, Liangwei Wang, Jiayi Zhu, Zhouan Shen, Yuyu Luo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.33403v1.pdf) | [![GitHub](https://img.shields.io/github/stars/HKUSTDial/DataMagic?style=social)](https://github.com/HKUSTDial/DataMagic)  
  Keywords: video editing  
- **[CraftTrace: Unflattening Videos into Malleable, Creation-Inspired Structures for Generative Editing](https://arxiv.org/abs/2609.30623v1)**  
  Authors: Boyu Li, Yuqian Zhou, Duotun Wang, Ding Li, Zhe Lin, Nanxuan Zhao, Zeyu Wang, Lin-Ping Yuan, Hongbo Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.30623v1.pdf)  
  Keywords: interactive, video editing  

### Video Inpainting & Completion

- **[Dexterous Tactile World Model](https://arxiv.org/abs/2609.34286v1)**  
  Authors: Ziyao Zeng, Xiatao Sun, Hao Wang, Yueyang Pan, Zhengxiang Yu, Fengyu Yang, Tianyu Liu, Zhiwen Fan, Daniel Rakita  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.34286v1.pdf)  
  Keywords: architecture, diffusion transformer, frame prediction, future frame prediction, video diffusion, video diffusion transformer, video world model, world model  
- **[WorldWeave: Growing Persistent Geometric Worlds for Video Generation](https://arxiv.org/abs/2609.34221v1)**  
  Authors: Yifan Huang, Lifan Jiang, Qingyue Hao, Cheng Chen, Boxi Wu, Xiaoxue Ren, Xiaofei He, Dehai Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.34221v1.pdf)  
  Keywords: outpainting, video generation, video synthesis  
- **[MT-WAM: Reorienting the One-Pass Predictive Representation Toward Action Generation](https://arxiv.org/abs/2609.21474v1)**  
  Authors: Yiguang Yang, Jiankun Peng, Xiaoming Wang, Yiran Zhang, Zhibo Fang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.21474v1.pdf)  
  Keywords: diffusion transformer, dynamics, embodied, video diffusion, video diffusion transformer, video prediction  
- **[StrucPhysVideo: Learning Physical Dynamics from Structured Captions and Robot Actions](https://arxiv.org/abs/2609.18430v1)**  
  Authors: Awomo-WM Team, :, Enhui Ma, Kaiwen Guo, Tingrui Zhang, Wei Song, Yingshui Tan, Jianhua Xu, Tong Zhang, Kaicheng Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.18430v1.pdf)  
  Keywords: action-conditioned, autoregressive, camera motion, denoising, distillation, dynamics, embodied, image to video, image-to-video, interactive, physical, physics, video prediction, video world model, world model  
- **[GeoLAM: Learning Geometry-Grounded Latent Actions from Unlabeled Human Videos](https://arxiv.org/abs/2609.17099v1)**  
  Authors: Yifan Xie, Hekun Tian, Jinkun Liu, YuAn Wang, Qiao Sun, Wenbo Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.17099v1.pdf)  
  Keywords: benchmark, trajectory, video generation, video prediction  
- **[Stream4D: 4D-Consistency for Streaming Autoregressive Diffusion Video Models](https://arxiv.org/abs/2608.19556v1)**  
  Authors: Yuanhao Ban, Jiaqi Feng, Hengguang Zhou, Xiaohuan Pei, Justin Cui, Cho-Jui Hsieh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.19556v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://banyuanhao.github.io/Stream4D)  
  Keywords: autoregressive, autoregressive video, dynamics, frame prediction, streaming, video generation  
- **[V-RAE: Rethinking Video Latent Spaces for Generation](https://arxiv.org/abs/2608.13556v1)**  
  Authors: Minghui Guo, Shengqiong Wu, Hao Fei  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.13556v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://v-rae.github.io)  
  Keywords: latent video, video autoencoder, video generation, video prediction, video tokenizer  
- **[GeoRoute: Geometry-Aware Hybrid Inference for Traffic Future-Frame Prediction](https://arxiv.org/abs/2608.09493v1)**  
  Authors: Khang Minh Le, Hieu Dinh Trung Pham, Luu Thanh Danh, Nam-Tien Le, Hieu Anh Ngo, Phuong Huu Vu Tran, Son Nguyen Minh Le, Nguyen Trong Nghia, Tu Tran Thi Cam, Huy Minh Nhat Nguyen, Cuong Tuan Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.09493v1.pdf)  
  Keywords: architecture, autonomous driving, benchmark, driving, frame prediction, future frame prediction, latent video, latent video diffusion, video diffusion  
- **[SimWAM: A Simple World Action Model for End-to-End Autonomous Driving](https://arxiv.org/abs/2608.07468v5)**  
  Authors: Zongchuang Zhao, Xin Zhou, Tianyang Xu, Zhengyang Sun, Kaixuan Zhou, Yu Wu, Honglin Li, Dingkang Liang, Xiang Bai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.07468v5.pdf) | [![GitHub](https://img.shields.io/github/stars/H-EmbodVis/SimWAM?style=social)](https://github.com/H-EmbodVis/SimWAM)  
  Keywords: autonomous driving, driving, dynamics, efficient, flow matching, trajectory, video generation, video prediction, world model  
- **[MirrorWorld: Taming Video Diffusion Models for Mirror Reflection Generation](https://arxiv.org/abs/2608.07463v1)**  
  Authors: Youjun Zhao, Alex Warren, Gary K. L. Tam, Rynson W. H. Lau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.07463v1.pdf)  
  Keywords: benchmark, distillation, video diffusion, video inpainting, video synthesis  

### Video Super-Resolution & Enhancement

*Showing the latest 50 out of 167 papers*

- **[Enhancing Autoregressive Video Generation via Representation Adversarial Distillation](https://arxiv.org/abs/2609.40037v1)**  
  Authors: Fangyu Lin, Xingtong Ge, Lunjie Zhu, Yi Zhang, Zhening Liu, Tianhang Wang, Mengfei Li, Yumeng Zhang, Guanglu Song, Yu Liu, Jun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.40037v1.pdf)  
  Keywords: architecture, autoregressive, autoregressive video, denoising, distillation, efficient, minute-long, streaming, video generation  
- **[TexTailor: Texture-Preserving Video Virtual Try-On via Adaptive Garment Conditioning](https://arxiv.org/abs/2609.39335v1)**  
  Authors: Zijing Qin, Jun Zhou, Ruicheng Zhang, Jiaqi Hou, Zunnan Xu, Ronghui Li, Zhenyu Xie, Xiu Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.39335v1.pdf)  
  Keywords: denoising, diffusion transformer, temporal consistency, video diffusion, video diffusion transformer, virtual try-on  
- **[DeCoPrune: Efficient KV-Cache Pruning for Autoregressive Video Diffusion via Denoising Consistency](https://arxiv.org/abs/2609.39096v1)**  
  Authors: Zeqi Xiao, Qingle Liu, Kaiwen Zhang, Yifan Zhou, Zihan Ding, Xingang Pan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.39096v1.pdf) | [![GitHub](https://img.shields.io/github/stars/DeCoPrune/CMBench?style=social)](https://github.com/DeCoPrune/CMBench) | [![Project](https://img.shields.io/badge/-Project-blue)](https://decoprune.github.io) | [![Dataset](https://img.shields.io/badge/-Dataset-orange)](https://huggingface.co/datasets/Aoraku/CMBench)  
  Keywords: autoregressive, autoregressive video, benchmark, denoising, efficient, interactive, streaming, video diffusion  
- **[Sparse-WAM: Accelerating World Action Models via Action-Guided Sparse Imagination](https://arxiv.org/abs/2609.38984v1)**  
  Authors: Xinling Xie, Haodong Wang, Jiazhi Mi, Zhiming Liu, Zicong Hong, Xiaoyi Pang, Qianli Liu, Yangjia Hu, Ying Chen, Zhengyang Yan, Song Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38984v1.pdf)  
  Keywords: denoising, efficient, video diffusion  
- **[Breaking the Uniformity Trap: Scaling Video Diffusion Model via SplitMoE](https://arxiv.org/abs/2609.38140v1)**  
  Authors: Yu Xu, Yuxin Zhang, Xiao Yang, Haotian Yang, Yizhi Wang, Xinwei Huang, Minxuan Lin, Angtian Wang, Chongyang Ma, Fan Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38140v1.pdf)  
  Keywords: architecture, denoising, diffusion model, video diffusion, video generation  
- **[Self-Aligned Forcing: Streaming Video Diffusion with Differentiable Noisy History](https://arxiv.org/abs/2609.38114v1)**  
  Authors: Weiqiang Wang, Zhuokun Chen, Yusheng Dai, Boying Li, Yi Zhang, Hossein Rahmani, Qiuhong Ke, Jianfei Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38114v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://anonymous.4open.science/w/self-aligned-forcing)  
  Keywords: autoregressive, autoregressive video, denoising, interactive, streaming, video diffusion  
- **[SoL-Refiner: Speed-of-Light One-Step Refinement for High-Resolution Video](https://arxiv.org/abs/2609.37969v1)**  
  Authors: Haozhe Liu, Tian Ye, Shuchen Xue, Yitong Li, Junsong Chen, Haopeng Li, Jincheng Yu, Duomin Wang, Ruihua Zhang, Lei Zhu, Song Han, Enze Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.37969v1.pdf)  
  Keywords: acceleration, benchmark, denoising, distillation, video generation  
- **[Texture Space Material Diffusion](https://arxiv.org/abs/2609.37654v1)**  
  Authors: Jacob Munkberg, Peter Kocsis, Jon Hasselgren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.37654v1.pdf)  
  Keywords: diffusion transformer, upscaling, video diffusion, video diffusion transformer  
- **[Motion Concept Unlearning in Video Diffusion Models](https://arxiv.org/abs/2609.36832v1)**  
  Authors: Ping Liu, Chi Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.36832v1.pdf)  
  Keywords: concept, denoising, dit, dynamics, t2v, text to video, text-to-video, video diffusion, video dit, video generation  
- **[Learning via Self-Consistency for Diffusion-based Video Reasoning](https://arxiv.org/abs/2609.36826v1)**  
  Authors: Zhenghao Ni, Weimin Qiu, Meng Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.36826v1.pdf)  
  Keywords: denoising, distillation, trajectory, video generation  

### World Models & Simulation

*Showing the latest 50 out of 243 papers*

- **[Physis-Lang: Self-Evolving Language as a Physical Representation for Video World Model](https://arxiv.org/abs/2609.40358v1)**  
  Authors: Liming Lu, Xianzheng Ma, Wenkun He, Guanqi Zhan, Yilin Zhao, Junyu Chen, Mengyao Xu, Jiaojiao Fan, Wenhang Ge, Yuchao Gu, Yunze Liu, Boyi Li, Zhen Dong, Victor Prisacariu, Ming-Yu Liu, Song Han, Han Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.40358v1.pdf)  
  Keywords: physical, physical plausibility, video generation, video world model, world model  
- **[LOCI: Spatial Linear Memory for Streaming World Models](https://arxiv.org/abs/2609.40222v1)**  
  Authors: Ji Xia, Tingting Liao, Xuezhi Liang, Hao Li, Guangyi Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.40222v1.pdf)  
  Keywords: architecture, benchmark, streaming, video world model, world model  
- **[Dream4ACT: A Shared Visual Action Interface for Multi-Embodiment Video-Action Modeling](https://arxiv.org/abs/2609.40153v1)**  
  Authors: Xiangyu Zhu, Jin Xu, Yue Guo, Xin Wu, Yifan Sun, Xiancong Ren, Jianxin Sun, Yong Dai, Xiaozhu Ju  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.40153v1.pdf)  
  Keywords: action-conditioned, diffusion transformer, dynamics, embodied, flow matching, video autoencoder, video generation, world model  
- **[DeCoPrune: Efficient KV-Cache Pruning for Autoregressive Video Diffusion via Denoising Consistency](https://arxiv.org/abs/2609.39096v1)**  
  Authors: Zeqi Xiao, Qingle Liu, Kaiwen Zhang, Yifan Zhou, Zihan Ding, Xingang Pan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.39096v1.pdf) | [![GitHub](https://img.shields.io/github/stars/DeCoPrune/CMBench?style=social)](https://github.com/DeCoPrune/CMBench) | [![Project](https://img.shields.io/badge/-Project-blue)](https://decoprune.github.io) | [![Dataset](https://img.shields.io/badge/-Dataset-orange)](https://huggingface.co/datasets/Aoraku/CMBench)  
  Keywords: autoregressive, autoregressive video, benchmark, denoising, efficient, interactive, streaming, video diffusion  
- **[BadAction: Backdoor Attacks on Interactive Video Generation via Action-Guided Triggers](https://arxiv.org/abs/2609.39047v1)**  
  Authors: Zhihang Wu, Zhongqi Wang, Jie Zhang, Fengming Gu, Shiguang Shan, Xilin Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.39047v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://wsad55.github.io/badaction01)  
  Keywords: controllable, interactive, video generation  
- **[FrameMorrow: Future-guided Frame Selection with Prospective Tokens for Long-Horizon Video Generation](https://arxiv.org/abs/2609.38839v1)**  
  Authors: Bo Yin, Xiaobin Hu, Jiaqi Zhao, Shuicheng Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38839v1.pdf)  
  Keywords: action-conditioned, interactive, long video, video generation  
- **[Rethinking Representations for World-Action Modeling](https://arxiv.org/abs/2609.38163v1)**  
  Authors: Haoyi Jiang, Liu Liu, Xinjiang Wang, Zhihao Sun, Zequn Chen, Sen Wang, Xinjie Wang, Xia Chen, Jingfeng Yao, Weiheng Zhao, Shanglin Yuan, Zhizhong Su, Wei Sui, Wenyu Liu, Xinggang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38163v1.pdf)  
  Keywords: dynamics, embodied, world model  
- **[FracGen: Learning How Objects Stretch and Tear with Physics-Informed Video Generation](https://arxiv.org/abs/2609.38152v1)**  
  Authors: Trong-Tung Nguyen, Jiahan Zhang, Anand Bhattad  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38152v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://fracgen.github.io)  
  Keywords: benchmark, controllable, dynamics, physical, physical plausibility, physics, physics-informed, simulation, video generation  
- **[HelixWorld: A Real-time Interactive Audio-Visual World Model](https://arxiv.org/abs/2609.38123v1)**  
  Authors: Lei Ke, Jiahao Pan, Zeyue Tian, Jiaming Wang, Haoyuan Huang, Kam Man Wu, Pengjun Fang, Hongyu Liu, Chenyang Qi, Lin Wang, Ruibin Yuan, Weijia Chen, Fangneng Zhan, Qifeng Chen, Wei Xue, Yike Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38123v1.pdf)  
  Keywords: distillation, dynamics, interactive, simulation, sound, streaming, trajectory, visual world model, world model, world simulation  
- **[Self-Aligned Forcing: Streaming Video Diffusion with Differentiable Noisy History](https://arxiv.org/abs/2609.38114v1)**  
  Authors: Weiqiang Wang, Zhuokun Chen, Yusheng Dai, Boying Li, Yi Zhang, Hossein Rahmani, Qiuhong Ke, Jianfei Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38114v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://anonymous.4open.science/w/self-aligned-forcing)  
  Keywords: autoregressive, autoregressive video, denoising, interactive, streaming, video diffusion  



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
