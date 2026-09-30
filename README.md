# Awesome Video Diffusions [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Video Diffusion Models and Video Generation. Content is automatically updated daily.

> Last Update: 2026-09-30 04:16:23

## 📰 Latest Updates

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
- [Applications](#applications) (200 papers) - Domain-specific applications of video diffusion models
- [Architecture & Efficiency](#architecture-&-efficiency) (389 papers) - Architectural innovations (DiT, UNet), flow matching, and training/inference efficiency
- [Audio & Multi-modal](#audio-&-multi-modal) (72 papers) - Audio-driven and multi-modal conditioned video generation
- [Controllable Generation](#controllable-generation) (331 papers) - Controllable video generation with motion, camera, pose, or layout guidance
- [Human & Character Animation](#human-&-character-animation) (61 papers) - Human-centric video generation including talking heads, dance, and character animation
- [Image-to-Video Generation](#image-to-video-generation) (93 papers) - Methods for animating still images into videos
- [Long Video Generation](#long-video-generation) (256 papers) - Generating temporally consistent long-form videos beyond short clips
- [Personalization & Customization](#personalization-&-customization) (168 papers) - Personalized video generation with custom subjects, identities, or styles
- [Physical Understanding](#physical-understanding) (308 papers) - Physics-aware video generation and dynamics modeling
- [Surveys & Benchmarks](#surveys-&-benchmarks) (313 papers) - Survey papers, benchmarks, and evaluation metrics for video generation
- [Text-to-Video Generation](#text-to-video-generation) (152 papers) - Foundation models and methods for generating videos from text prompts
- [Video Editing](#video-editing) (99 papers) - Diffusion-based video editing, style transfer, and manipulation
- [Video Inpainting & Completion](#video-inpainting-&-completion) (25 papers) - Video inpainting, completion, outpainting, and temporal prediction
- [Video Super-Resolution & Enhancement](#video-super-resolution-&-enhancement) (166 papers) - Video quality improvement, upscaling, restoration, and frame interpolation
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
- **[Stabilizing Camera-Controlled Novel View Synthesis at Inference Time](https://arxiv.org/abs/2609.03639v1)**  
  Authors: Prajwal Singh, Arjun Badola, Seema Kumari, Hajime Nagahara, Shanmuganathan Raman  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.03639v1.pdf)  
  Keywords: autoregressive, camera motion, efficient, novel view, video diffusion  

### Applications

*Showing the latest 50 out of 200 papers*

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
- **[Waypoint-1.5: A Real-Time Video World Model for Consumer Hardware](https://arxiv.org/abs/2609.37107v1)**  
  Authors: Rajit Rajpal, Shahbuland Matiana, Liew Wei Pyn, Anmol Agarwal, Ryan Craig, Andrew Lapp, Mithun Hunsur, Sami BuGhanem, Scottie Fox, Aaron Sanders Carson Poole, Irene Park, Dave Rossi, Spencer Frazier, Louis Castricato  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.37107v1.pdf)  
  Keywords: architecture, game, interactive, video diffusion, video generation, video world model, world model  
- **[WeLike2Party! In-Context Motion Transfer for Multi-Human Image Animation](https://arxiv.org/abs/2609.36937v1)**  
  Authors: Sangeyl Lee, Seunghyun Shin, Seungho Park, Wooseok Jeon, Hae-Gon Jeon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.36937v1.pdf)  
  Keywords: benchmark, driving, human animation, human image animation, identity, image animation, motion transfer, trajectory, video generation  
- **[Timeline-Bench: Evaluating Agents on Realistic Video-Editing Tasks, from Raw Footage to Final Cut](https://arxiv.org/abs/2609.35143v1)**  
  Authors: Gunin Gupta, Nirmit Arora, Pavan Kalyan Tankala  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.35143v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://timelinebench.tensortest.com)  
  Keywords: benchmark, creative, video editing  
- **[OPIS: An Input-Grounded Benchmark for Multi-Object Memory in Video World Models](https://arxiv.org/abs/2609.35052v1)**  
  Authors: Hao Wang, Tao Yu, Liuzhou Zhang, HeXin Wang, Haopeng Jin, Yuxuan Zhou, Xinming Wang, Hongzhu Yi, Xinye Li, Yuanlei Wang, Ping Nie, Yan Huang, Yuxuan Zhang, Pengfei Zhou, Yanyan Zou, Wei Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.35052v1.pdf)  
  Keywords: benchmark, camera-conditioned, embodied, evaluation, game, identity, image to video, image-to-video  
- **[CoDrive: Cross-Vehicle World-Consistent Video Generation with Precise Trajectory Control for Cooperative Driving](https://arxiv.org/abs/2609.34749v1)**  
  Authors: Yu Meng, Baining Zhao, Junta Wu, Tengfei Wang, Rongze Tang, Haiyu Zhang, Wenqiang Sun, Chen Gao, Zhibo Chen, Xinlei Chen, Yong Li, Xiao-Ping Zhang, Chunchao Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.34749v1.pdf)  
  Keywords: benchmark, camera trajectory, driving, evaluation, simulation, trajectory, video generation  
- **[SkillPE: Creativity-Oriented Cinematic Skill Evolution for Text-to-Video Prompt Engineering](https://arxiv.org/abs/2609.34335v1)**  
  Authors: Yanwei Huang, Mingxuan Zhu, Shujie Li, Shiyuan Liu, Yuanxing Zhang, Arpit Narechania  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.34335v1.pdf) | [![GitHub](https://img.shields.io/github/stars/Ais0n/SkillPE?style=social)](https://github.com/Ais0n/SkillPE)  
  Keywords: benchmark, cinematic, creative, evaluation, sound, text to video, text-to-video, video generation  
- **[FINE: Future-Informed Navigation Encoding for Data-Efficient Vision-Language Navigation](https://arxiv.org/abs/2609.32855v1)**  
  Authors: Khang H. Nguyen, Hoang Pham Quang Nguyen, Ha Phuong Nguyen, Khanh Dinh Binh, Xuan Ha Nguyen, Vien Ngo, Duy Ho Nguyen Minh, Huan Nguyen, An T. Le  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.32855v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://finevln.github.io)  
  Keywords: efficient, embodied, trajectory, video world model, world model  

### Architecture & Efficiency

*Showing the latest 50 out of 389 papers*

- **[LongLive-Plug: Once-for-All Distillation for Video Generation](https://arxiv.org/abs/2609.38154v1)**  
  Authors: Shuai Yang, Luozhou Wang, Wei Huang, ZhiFei Chen, Bohan Zhang, Xiao Fu, Qianli Ma, Chen-Hsuan Lin, Weian Mao, Bryan Chu, Song Han, Yukang Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38154v1.pdf)  
  Keywords: autoregressive, distillation, long video, robotics, video diffusion, video generation  
- **[LIFT: Layout-In-Future Video Generation under Large Viewpoint Change via On-Policy Self-Distillation](https://arxiv.org/abs/2609.38146v1)**  
  Authors: Shengxiang Ji, Boyang Wang, Haiyang Xu, Bingnan Li, Yucheng Mao, Zeyuan Chen, Xiaojun Shan, Xiang Zhang, Gang Hua, Jianwen Xie, Zezhou Cheng, Zhuowen Tu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38146v1.pdf)  
  Keywords: camera control, controllable, distillation, image to video, image-to-video, layout, video generation  
- **[Breaking the Uniformity Trap: Scaling Video Diffusion Model via SplitMoE](https://arxiv.org/abs/2609.38140v1)**  
  Authors: Yu Xu, Yuxin Zhang, Xiao Yang, Haotian Yang, Yizhi Wang, Xinwei Huang, Minxuan Lin, Angtian Wang, Chongyang Ma, Fan Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38140v1.pdf)  
  Keywords: architecture, denoising, diffusion model, video diffusion, video generation  
- **[HelixWorld: A Real-time Interactive Audio-Visual World Model](https://arxiv.org/abs/2609.38123v1)**  
  Authors: Lei Ke, Jiahao Pan, Zeyue Tian, Jiaming Wang, Haoyuan Huang, Kam Man Wu, Pengjun Fang, Hongyu Liu, Chenyang Qi, Lin Wang, Ruibin Yuan, Weijia Chen, Fangneng Zhan, Qifeng Chen, Wei Xue, Yike Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38123v1.pdf)  
  Keywords: distillation, dynamics, interactive, simulation, sound, streaming, trajectory, visual world model, world model, world simulation  
- **[WorldLine: Action-Driven Visual Simulation for Robotic Manipulation](https://arxiv.org/abs/2609.38059v1)**  
  Authors: Shenghe Zheng, Wenbo Li, Jiyao Zhang, Bin Xia, Haoyang Huang, Nan Duan, Jiaya Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38059v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zhengsh123.github.io/WorldLine)  
  Keywords: action-conditioned, distillation, dynamics, efficient, embodied, evaluation, physical, robot learning, simulation, trajectory, video generation  
- **[SoL-Refiner: Speed-of-Light One-Step Refinement for High-Resolution Video](https://arxiv.org/abs/2609.37969v1)**  
  Authors: Haozhe Liu, Tian Ye, Shuchen Xue, Yitong Li, Junsong Chen, Haopeng Li, Jincheng Yu, Duomin Wang, Ruihua Zhang, Lei Zhu, Song Han, Enze Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.37969v1.pdf)  
  Keywords: acceleration, benchmark, denoising, distillation, video generation  
- **[Rollout-Marginal Distillation for Long-Horizon Autoregressive Video Generation](https://arxiv.org/abs/2609.37925v1)**  
  Authors: Chenjian Gao, Zhihao Hu, Jianqi Ma, Jun Zhang, Weidong Zhang, Tianfan Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.37925v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://cjeen.github.io/RMD)  
  Keywords: autoregressive, autoregressive video, distillation, temporal consistency, video diffusion, video generation  
- **[Texture Space Material Diffusion](https://arxiv.org/abs/2609.37654v1)**  
  Authors: Jacob Munkberg, Peter Kocsis, Jon Hasselgren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.37654v1.pdf)  
  Keywords: diffusion transformer, upscaling, video diffusion, video diffusion transformer  
- **[Adaptive Reward Routing: Dynamic Multi-Reward Optimization for Joint Audio-Video Diffusion via Forward-Process RL](https://arxiv.org/abs/2609.37200v1)**  
  Authors: Songlin Yang, Xiaotong Zhao, Jiacheng Zhang, Zhe Wang, Toyota Li, Eric Liu, Alan Zhao, Anyi Rao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.37200v1.pdf)  
  Keywords: efficient, joint audio-video, video diffusion  
- **[Waypoint-1.5: A Real-Time Video World Model for Consumer Hardware](https://arxiv.org/abs/2609.37107v1)**  
  Authors: Rajit Rajpal, Shahbuland Matiana, Liew Wei Pyn, Anmol Agarwal, Ryan Craig, Andrew Lapp, Mithun Hunsur, Sami BuGhanem, Scottie Fox, Aaron Sanders Carson Poole, Irene Park, Dave Rossi, Spencer Frazier, Louis Castricato  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.37107v1.pdf)  
  Keywords: architecture, game, interactive, video diffusion, video generation, video world model, world model  

### Audio & Multi-modal

*Showing the latest 50 out of 72 papers*

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
- **[Qwen3.8-Omni: Towards Native Omni-Modal Agents](https://arxiv.org/abs/2609.25611v1)**  
  Authors: Qwen Team  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.25611v1.pdf)  
  Keywords: architecture, long-form, music video, video editing, video translation  

### Controllable Generation

*Showing the latest 50 out of 331 papers*

- **[FracGen: Learning How Objects Stretch and Tear with Physics-Informed Video Generation](https://arxiv.org/abs/2609.38152v1)**  
  Authors: Trong-Tung Nguyen, Jiahan Zhang, Anand Bhattad  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38152v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://fracgen.github.io)  
  Keywords: benchmark, controllable, dynamics, physical, physical plausibility, physics, physics-informed, simulation, video generation  
- **[LIFT: Layout-In-Future Video Generation under Large Viewpoint Change via On-Policy Self-Distillation](https://arxiv.org/abs/2609.38146v1)**  
  Authors: Shengxiang Ji, Boyang Wang, Haiyang Xu, Bingnan Li, Yucheng Mao, Zeyuan Chen, Xiaojun Shan, Xiang Zhang, Gang Hua, Jianwen Xie, Zezhou Cheng, Zhuowen Tu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38146v1.pdf)  
  Keywords: camera control, controllable, distillation, image to video, image-to-video, layout, video generation  
- **[HelixWorld: A Real-time Interactive Audio-Visual World Model](https://arxiv.org/abs/2609.38123v1)**  
  Authors: Lei Ke, Jiahao Pan, Zeyue Tian, Jiaming Wang, Haoyuan Huang, Kam Man Wu, Pengjun Fang, Hongyu Liu, Chenyang Qi, Lin Wang, Ruibin Yuan, Weijia Chen, Fangneng Zhan, Qifeng Chen, Wei Xue, Yike Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38123v1.pdf)  
  Keywords: distillation, dynamics, interactive, simulation, sound, streaming, trajectory, visual world model, world model, world simulation  
- **[MUGEN: Interactive Panoramic World Exploration via Camera Control](https://arxiv.org/abs/2609.38077v1)**  
  Authors: Jiaming Tan, Zhen Li, Shuwei Shi, Minggui Teng, Siqi Yang, Yuwei Wu, Bo Zheng, Chuanhao Li, Kaipeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38077v1.pdf)  
  Keywords: camera control, camera motion, controllable, interactive, video generation  
- **[WorldLine: Action-Driven Visual Simulation for Robotic Manipulation](https://arxiv.org/abs/2609.38059v1)**  
  Authors: Shenghe Zheng, Wenbo Li, Jiyao Zhang, Bin Xia, Haoyang Huang, Nan Duan, Jiaya Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38059v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zhengsh123.github.io/WorldLine)  
  Keywords: action-conditioned, distillation, dynamics, efficient, embodied, evaluation, physical, robot learning, simulation, trajectory, video generation  
- **[Complementary Retrieval-Augmented Prompting for Consistent Long-Form Video Generation](https://arxiv.org/abs/2609.37407v1)**  
  Authors: Xianghan Wei, Xiaoda Yang, Zhi Wang, An Pan, Daoan Zhang, Huayi Zhang, Yan Zhang, Wei Xu, Zishun Liao, Jianwen Lou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.37407v1.pdf)  
  Keywords: keyframe, long-form, long-form video, story generation, video generation  
- **[WeLike2Party! In-Context Motion Transfer for Multi-Human Image Animation](https://arxiv.org/abs/2609.36937v1)**  
  Authors: Sangeyl Lee, Seunghyun Shin, Seungho Park, Wooseok Jeon, Hae-Gon Jeon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.36937v1.pdf)  
  Keywords: benchmark, driving, human animation, human image animation, identity, image animation, motion transfer, trajectory, video generation  
- **[Learning via Self-Consistency for Diffusion-based Video Reasoning](https://arxiv.org/abs/2609.36826v1)**  
  Authors: Zhenghao Ni, Weimin Qiu, Meng Tang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.36826v1.pdf)  
  Keywords: denoising, distillation, trajectory, video generation  
- **[MeteoVerse: Unified Weather-Controllable Video World Model](https://arxiv.org/abs/2609.36810v1)**  
  Authors: Renlong Wu, Guanqiao Wang, Xuan Shang, Yin Hanming, Xiaoxiao Sheng, Tianyu Huang, Hui Li, Wangmeng Zuo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.36810v1.pdf)  
  Keywords: camera control, camera motion, camera trajectory, controllable, dynamics, trajectory, video world model, world model  
- **[Foresight at the Event Boundary: Evaluating Physical Prediction in Video World Models](https://arxiv.org/abs/2609.36531v1)**  
  Authors: Estela Monserrat Arriaga Santana, Julian Rosas Scull, Ehécatl Sacamch'en Núñez Rico, Hugo Jair Escalante  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.36531v1.pdf)  
  Keywords: evaluation, physical, trajectory, video generation, world model  

### Human & Character Animation

*Showing the latest 50 out of 61 papers*

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
- **[WB-WAM: Heterogeneous Body-Hand Pre-training for Humanoid Loco-Manipulation](https://arxiv.org/abs/2609.34199v1)**  
  Authors: Chuan Qin, Shaoting Zhu, Siyuan Luo, Siqiao Huang, Hongyu Zhao, Hang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.34199v1.pdf)  
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
- **[PAI-Actor: Cinematic Multi-Character Replacement in Dynamic Scenes](https://arxiv.org/abs/2609.05918v1)**  
  Authors: Bangxun Tang, Heyuan Gao, Yiren Song, Guian Fang, Zijian He, Jie Yang, Mike Zheng Shou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.05918v1.pdf)  
  Keywords: autoregressive, autoregressive video, camera motion, character animation, cinematic, diffusion transformer, distillation, dynamics, efficient, film, long-form, video generation, video to video, video-to-video  
- **[BooM-VVT: Boosting Mask-Free Video Virtual Try-On with Image-Level Pseudo Data](https://arxiv.org/abs/2609.04120v1)**  
  Authors: Wei Zhang, Xin Li, Peishu Shi, Jialin Gao, Xuekang Peng, Zhichao Lian, Yeying Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.04120v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://boomvvt.github.io/boomvvt)  
  Keywords: keyframe, temporal consistency, video generation, virtual try-on  

### Image-to-Video Generation

*Showing the latest 50 out of 93 papers*

- **[LIFT: Layout-In-Future Video Generation under Large Viewpoint Change via On-Policy Self-Distillation](https://arxiv.org/abs/2609.38146v1)**  
  Authors: Shengxiang Ji, Boyang Wang, Haiyang Xu, Bingnan Li, Yucheng Mao, Zeyuan Chen, Xiaojun Shan, Xiang Zhang, Gang Hua, Jianwen Xie, Zezhou Cheng, Zhuowen Tu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38146v1.pdf)  
  Keywords: camera control, controllable, distillation, image to video, image-to-video, layout, video generation  
- **[WeLike2Party! In-Context Motion Transfer for Multi-Human Image Animation](https://arxiv.org/abs/2609.36937v1)**  
  Authors: Sangeyl Lee, Seunghyun Shin, Seungho Park, Wooseok Jeon, Hae-Gon Jeon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.36937v1.pdf)  
  Keywords: benchmark, driving, human animation, human image animation, identity, image animation, motion transfer, trajectory, video generation  
- **[Beyond Legibility: Benchmarking Visual Text Rendering and In-Place Editing in Unified Video Generation](https://arxiv.org/abs/2609.36598v1)**  
  Authors: Ziying Zhang, Litao Li, Junchao Liao, Tianyi Zeng, Siyu Zhu, Long Qin, Zhenghao Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.36598v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://huggingface.co/datasets/Vicky0720/VidScribe.) | [![Dataset](https://img.shields.io/badge/-Dataset-orange)](https://huggingface.co/datasets/Vicky0720/VidScribe)  
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
- **[StrucPhysVideo: Learning Physical Dynamics from Structured Captions and Robot Actions](https://arxiv.org/abs/2609.18430v1)**  
  Authors: Awomo-WM Team, :, Enhui Ma, Kaiwen Guo, Tingrui Zhang, Wei Song, Yingshui Tan, Jianhua Xu, Tong Zhang, Kaicheng Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.18430v1.pdf)  
  Keywords: action-conditioned, autoregressive, camera motion, denoising, distillation, dynamics, embodied, image to video, image-to-video, interactive, physical, physics, video prediction, video world model, world model  

### Long Video Generation

*Showing the latest 50 out of 256 papers*

- **[LongLive-Plug: Once-for-All Distillation for Video Generation](https://arxiv.org/abs/2609.38154v1)**  
  Authors: Shuai Yang, Luozhou Wang, Wei Huang, ZhiFei Chen, Bohan Zhang, Xiao Fu, Qianli Ma, Chen-Hsuan Lin, Weian Mao, Bryan Chu, Song Han, Yukang Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38154v1.pdf)  
  Keywords: autoregressive, distillation, long video, robotics, video diffusion, video generation  
- **[HelixWorld: A Real-time Interactive Audio-Visual World Model](https://arxiv.org/abs/2609.38123v1)**  
  Authors: Lei Ke, Jiahao Pan, Zeyue Tian, Jiaming Wang, Haoyuan Huang, Kam Man Wu, Pengjun Fang, Hongyu Liu, Chenyang Qi, Lin Wang, Ruibin Yuan, Weijia Chen, Fangneng Zhan, Qifeng Chen, Wei Xue, Yike Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38123v1.pdf)  
  Keywords: distillation, dynamics, interactive, simulation, sound, streaming, trajectory, visual world model, world model, world simulation  
- **[Self-Aligned Forcing: Streaming Video Diffusion with Differentiable Noisy History](https://arxiv.org/abs/2609.38114v1)**  
  Authors: Weiqiang Wang, Zhuokun Chen, Yusheng Dai, Boying Li, Yi Zhang, Hossein Rahmani, Qiuhong Ke, Jianfei Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38114v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://anonymous.4open.science/w/self-aligned-forcing)  
  Keywords: autoregressive, autoregressive video, denoising, interactive, streaming, video diffusion  
- **[Rollout-Marginal Distillation for Long-Horizon Autoregressive Video Generation](https://arxiv.org/abs/2609.37925v1)**  
  Authors: Chenjian Gao, Zhihao Hu, Jianqi Ma, Jun Zhang, Weidong Zhang, Tianfan Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.37925v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://cjeen.github.io/RMD)  
  Keywords: autoregressive, autoregressive video, distillation, temporal consistency, video diffusion, video generation  
- **[Complementary Retrieval-Augmented Prompting for Consistent Long-Form Video Generation](https://arxiv.org/abs/2609.37407v1)**  
  Authors: Xianghan Wei, Xiaoda Yang, Zhi Wang, An Pan, Daoan Zhang, Huayi Zhang, Yan Zhang, Wei Xu, Zishun Liao, Jianwen Lou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.37407v1.pdf)  
  Keywords: keyframe, long-form, long-form video, story generation, video generation  
- **[Salt++: Context-Aligned Post-Training for Few-Step Streaming Multimodal Generation](https://arxiv.org/abs/2609.36995v1)**  
  Authors: Xingtong Ge, Yutong Wang, Lunjie Zhu, Haitao Lin, Fangyu Lin, Yushi Huang, Xin Zhang, Yi Zhang, Yu Liu, Jun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.36995v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xingtongge.github.io/Saltpp)  
  Keywords: audio-video generation, autoregressive, consistency distillation, distillation, evaluation, streaming, video generation  
- **[Scaling Video Generation for Reasoning: At What Cost?](https://arxiv.org/abs/2609.36599v1)**  
  Authors: Weihang Guo, Xiaoyu Wu, Yifei Wang, Niloofar Mireshghallah, Lydia E. Kavraki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.36599v1.pdf)  
  Keywords: autoregressive, benchmark, evaluation, video generation  
- **[Compress to Remember: Learning Compact Memory via On-Policy Distillation for Long Video Generation](https://arxiv.org/abs/2609.36364v1)**  
  Authors: Xiaoyu Wu, Weihang Guo, Yifei Wang, Xinze Feng, Lydia E. Kavraki, Zhiwei Steven Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.36364v1.pdf)  
  Keywords: denoising, distillation, evaluation, long video, minute-long, video generation  
- **[FlowAct-R2: Beyond Talking Avatar via Streaming Multimodal References and Proactive Agent Planning](https://arxiv.org/abs/2609.35728v1)**  
  Authors: Ziyao Huang, Zhengkun Rong, Shiyang Qin, Shuang Liang, Wentao Hu, Yuxuan Luo, Yuan Zhang, Mingyuan Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.35728v1.pdf)  
  Keywords: avatar, diffusion transformer, interactive, streaming, talking avatar, video generation  
- **[From Scores to Samples: Elastic Forcing for Autoregressive Video Generation](https://arxiv.org/abs/2609.35491v2)**  
  Authors: Chi Zhang, Yueyi Liu, Haoyang Shi, Ruichuan An, Haoyu Li, Yuhang Wu, Sen Cui, Miao Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.35491v2.pdf)  
  Keywords: architecture, autoregressive, autoregressive video, distillation, efficient, video generation  

### Personalization & Customization

*Showing the latest 50 out of 168 papers*

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
- **[Beyond Legibility: Benchmarking Visual Text Rendering and In-Place Editing in Unified Video Generation](https://arxiv.org/abs/2609.36598v1)**  
  Authors: Ziying Zhang, Litao Li, Junchao Liao, Tianyi Zeng, Siyu Zhu, Long Qin, Zhenghao Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.36598v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://huggingface.co/datasets/Vicky0720/VidScribe.) | [![Dataset](https://img.shields.io/badge/-Dataset-orange)](https://huggingface.co/datasets/Vicky0720/VidScribe)  
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
- **[VideoGen-Agent: Reinforcing Video Generation Agents](https://arxiv.org/abs/2609.24997v2)**  
  Authors: Binxu Li, Haoyi Duan, Yuhui Zhang, Yaohui Zhang, Zihao Lin, Kaituo Feng, Suozhi Huang, Xiangyi Li, Yu Li, Chunyuan Li, Shilong Liu, Mengdi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.24997v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://andyca111.github.io/VideoGen_Agent)  
  Keywords: benchmark, identity, physical, physical consistency, text to video, text-to-video, video generation  
- **[OmniVBench: A Benchmark and Large-Scale Dataset for Omni Reference-to-Video Generation](https://arxiv.org/abs/2609.22069v1)**  
  Authors: Wenxue Li, Peiyan Guan, Haoyang Jiang, Junxian Cai, Hualuo Liu, Chunjie Zhang, Chong Guan, Kai Huang, Songlian Li, Taiyi Wu, Yongjian Yu, Xiaotong Zhao, Alan Zhao, Eric Liu, Xi Chen, Yu Liu, Lei Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.22069v1.pdf)  
  Keywords: benchmark, evaluation, style, video generation  

### Physical Understanding

*Showing the latest 50 out of 308 papers*

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
- **[WorldLine: Action-Driven Visual Simulation for Robotic Manipulation](https://arxiv.org/abs/2609.38059v1)**  
  Authors: Shenghe Zheng, Wenbo Li, Jiyao Zhang, Bin Xia, Haoyang Huang, Nan Duan, Jiaya Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38059v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zhengsh123.github.io/WorldLine)  
  Keywords: action-conditioned, distillation, dynamics, efficient, embodied, evaluation, physical, robot learning, simulation, trajectory, video generation  
- **[Geometry-Preserving Human-to-Robot Upper-Body Motion Retargeting from Monocular Video](https://arxiv.org/abs/2609.37776v1)**  
  Authors: Xiaoyu Yang, Sen Han, Da Li, Nan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.37776v1.pdf)  
  Keywords: body motion, physical, simulation, video generation  
- **[MotionInsight: Diagnosing Object Motion Deficiencies in Generated Videos](https://arxiv.org/abs/2609.37030v1)**  
  Authors: Jiahao Zhan, Yongrui Ma, Qunliang Xing, Xuanyu Zhang, Jingqi Tong, Junlin Li, Li zhang, Shijie Zhao, Tianfan Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.37030v1.pdf)  
  Keywords: physical, physical plausibility, video generation  
- **[Motion Concept Unlearning in Video Diffusion Models](https://arxiv.org/abs/2609.36832v1)**  
  Authors: Ping Liu, Chi Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.36832v1.pdf)  
  Keywords: concept, denoising, dit, dynamics, t2v, text to video, text-to-video, video diffusion, video dit, video generation  
- **[MeteoVerse: Unified Weather-Controllable Video World Model](https://arxiv.org/abs/2609.36810v1)**  
  Authors: Renlong Wu, Guanqiao Wang, Xuan Shang, Yin Hanming, Xiaoxiao Sheng, Tianyu Huang, Hui Li, Wangmeng Zuo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.36810v1.pdf)  
  Keywords: camera control, camera motion, camera trajectory, controllable, dynamics, trajectory, video world model, world model  
- **[Beyond Legibility: Benchmarking Visual Text Rendering and In-Place Editing in Unified Video Generation](https://arxiv.org/abs/2609.36598v1)**  
  Authors: Ziying Zhang, Litao Li, Junchao Liao, Tianyi Zeng, Siyu Zhu, Long Qin, Zhenghao Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.36598v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://huggingface.co/datasets/Vicky0720/VidScribe.) | [![Dataset](https://img.shields.io/badge/-Dataset-orange)](https://huggingface.co/datasets/Vicky0720/VidScribe)  
  Keywords: benchmark, dynamics, evaluation, i2v, identity, physical, t2v, v2v, video generation  
- **[Foresight at the Event Boundary: Evaluating Physical Prediction in Video World Models](https://arxiv.org/abs/2609.36531v1)**  
  Authors: Estela Monserrat Arriaga Santana, Julian Rosas Scull, Ehécatl Sacamch'en Núñez Rico, Hugo Jair Escalante  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.36531v1.pdf)  
  Keywords: evaluation, physical, trajectory, video generation, world model  

### Surveys & Benchmarks

*Showing the latest 50 out of 313 papers*

- **[FracGen: Learning How Objects Stretch and Tear with Physics-Informed Video Generation](https://arxiv.org/abs/2609.38152v1)**  
  Authors: Trong-Tung Nguyen, Jiahan Zhang, Anand Bhattad  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38152v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://fracgen.github.io)  
  Keywords: benchmark, controllable, dynamics, physical, physical plausibility, physics, physics-informed, simulation, video generation  
- **[WorldLine: Action-Driven Visual Simulation for Robotic Manipulation](https://arxiv.org/abs/2609.38059v1)**  
  Authors: Shenghe Zheng, Wenbo Li, Jiyao Zhang, Bin Xia, Haoyang Huang, Nan Duan, Jiaya Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38059v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zhengsh123.github.io/WorldLine)  
  Keywords: action-conditioned, distillation, dynamics, efficient, embodied, evaluation, physical, robot learning, simulation, trajectory, video generation  
- **[SoL-Refiner: Speed-of-Light One-Step Refinement for High-Resolution Video](https://arxiv.org/abs/2609.37969v1)**  
  Authors: Haozhe Liu, Tian Ye, Shuchen Xue, Yitong Li, Junsong Chen, Haopeng Li, Jincheng Yu, Duomin Wang, Ruihua Zhang, Lei Zhu, Song Han, Enze Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.37969v1.pdf)  
  Keywords: acceleration, benchmark, denoising, distillation, video generation  
- **[Salt++: Context-Aligned Post-Training for Few-Step Streaming Multimodal Generation](https://arxiv.org/abs/2609.36995v1)**  
  Authors: Xingtong Ge, Yutong Wang, Lunjie Zhu, Haitao Lin, Fangyu Lin, Yushi Huang, Xin Zhang, Yi Zhang, Yu Liu, Jun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.36995v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://xingtongge.github.io/Saltpp)  
  Keywords: audio-video generation, autoregressive, consistency distillation, distillation, evaluation, streaming, video generation  
- **[WeLike2Party! In-Context Motion Transfer for Multi-Human Image Animation](https://arxiv.org/abs/2609.36937v1)**  
  Authors: Sangeyl Lee, Seunghyun Shin, Seungho Park, Wooseok Jeon, Hae-Gon Jeon  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.36937v1.pdf)  
  Keywords: benchmark, driving, human animation, human image animation, identity, image animation, motion transfer, trajectory, video generation  
- **[Scaling Video Generation for Reasoning: At What Cost?](https://arxiv.org/abs/2609.36599v1)**  
  Authors: Weihang Guo, Xiaoyu Wu, Yifei Wang, Niloofar Mireshghallah, Lydia E. Kavraki  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.36599v1.pdf)  
  Keywords: autoregressive, benchmark, evaluation, video generation  
- **[Beyond Legibility: Benchmarking Visual Text Rendering and In-Place Editing in Unified Video Generation](https://arxiv.org/abs/2609.36598v1)**  
  Authors: Ziying Zhang, Litao Li, Junchao Liao, Tianyi Zeng, Siyu Zhu, Long Qin, Zhenghao Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.36598v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://huggingface.co/datasets/Vicky0720/VidScribe.) | [![Dataset](https://img.shields.io/badge/-Dataset-orange)](https://huggingface.co/datasets/Vicky0720/VidScribe)  
  Keywords: benchmark, dynamics, evaluation, i2v, identity, physical, t2v, v2v, video generation  
- **[Foresight at the Event Boundary: Evaluating Physical Prediction in Video World Models](https://arxiv.org/abs/2609.36531v1)**  
  Authors: Estela Monserrat Arriaga Santana, Julian Rosas Scull, Ehécatl Sacamch'en Núñez Rico, Hugo Jair Escalante  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.36531v1.pdf)  
  Keywords: evaluation, physical, trajectory, video generation, world model  
- **[Compress to Remember: Learning Compact Memory via On-Policy Distillation for Long Video Generation](https://arxiv.org/abs/2609.36364v1)**  
  Authors: Xiaoyu Wu, Weihang Guo, Yifei Wang, Xinze Feng, Lydia E. Kavraki, Zhiwei Steven Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.36364v1.pdf)  
  Keywords: denoising, distillation, evaluation, long video, minute-long, video generation  
- **[G$^3$-LoRA: Organizing Reward-Weighted Video Data with Gradient-Guided Grouped LoRA](https://arxiv.org/abs/2609.35189v1)**  
  Authors: Jia Song, Wenhow Li, Lichen Bai, Bada Ye, Zeke Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.35189v1.pdf)  
  Keywords: camera motion, denoising, distillation, evaluation, flow matching, t2v, text to video, text-to-video  

### Text-to-Video Generation

*Showing the latest 50 out of 152 papers*

- **[Motion Concept Unlearning in Video Diffusion Models](https://arxiv.org/abs/2609.36832v1)**  
  Authors: Ping Liu, Chi Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.36832v1.pdf)  
  Keywords: concept, denoising, dit, dynamics, t2v, text to video, text-to-video, video diffusion, video dit, video generation  
- **[Beyond Legibility: Benchmarking Visual Text Rendering and In-Place Editing in Unified Video Generation](https://arxiv.org/abs/2609.36598v1)**  
  Authors: Ziying Zhang, Litao Li, Junchao Liao, Tianyi Zeng, Siyu Zhu, Long Qin, Zhenghao Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.36598v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://huggingface.co/datasets/Vicky0720/VidScribe.) | [![Dataset](https://img.shields.io/badge/-Dataset-orange)](https://huggingface.co/datasets/Vicky0720/VidScribe)  
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

*Showing the latest 50 out of 99 papers*

- **[Counterfactual Video Generation Enables Scalable Humanoid Loco-Manipulation](https://arxiv.org/abs/2609.38172v1)**  
  Authors: Zihan Wang, Zhen Wu, Pieter Abbeel, Rocky Duan, Jitendra Malik, Carmelo Sferrazza, C. Karen Liu, Guanya Shi, Angjoo Kanazawa  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38172v1.pdf)  
  Keywords: v2v, video generation, video to video, video-to-video  
- **[Beyond Legibility: Benchmarking Visual Text Rendering and In-Place Editing in Unified Video Generation](https://arxiv.org/abs/2609.36598v1)**  
  Authors: Ziying Zhang, Litao Li, Junchao Liao, Tianyi Zeng, Siyu Zhu, Long Qin, Zhenghao Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.36598v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://huggingface.co/datasets/Vicky0720/VidScribe.) | [![Dataset](https://img.shields.io/badge/-Dataset-orange)](https://huggingface.co/datasets/Vicky0720/VidScribe)  
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
- **[VideoX-Qwen: Data-Centric Instruction-Based Video Editing](https://arxiv.org/abs/2609.26015v1)**  
  Authors: JJiahang Li, Dingbao Shao, Xinyu Chen, Song Wu, Jiang Lin, Duo Li, Yuhang Liu, Jiaxin Hu, Shengrong Gu, Ying Tai, Zili Yi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.26015v1.pdf)  
  Keywords: instruction-based video editing, video editing, video generation  
- **[Qwen3.8-Omni: Towards Native Omni-Modal Agents](https://arxiv.org/abs/2609.25611v1)**  
  Authors: Qwen Team  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.25611v1.pdf)  
  Keywords: architecture, long-form, music video, video editing, video translation  

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

*Showing the latest 50 out of 166 papers*

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
- **[Compress to Remember: Learning Compact Memory via On-Policy Distillation for Long Video Generation](https://arxiv.org/abs/2609.36364v1)**  
  Authors: Xiaoyu Wu, Weihang Guo, Yifei Wang, Xinze Feng, Lydia E. Kavraki, Zhiwei Steven Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.36364v1.pdf)  
  Keywords: denoising, distillation, evaluation, long video, minute-long, video generation  
- **[PreviewDiff: Multimodal Critic-Guided Search over Diffusion Latents](https://arxiv.org/abs/2609.36199v1)**  
  Authors: Vighnesh Subramaniam, Boris Katz, Brian Cheung, Chun-Liang Li, Tomas Pfister, Yale Song  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.36199v1.pdf)  
  Keywords: denoising, trajectory, video generation  
- **[PDMD: Projected Distribution Matching Distillation for Video Diffusion Models](https://arxiv.org/abs/2609.35768v1)**  
  Authors: Zimo Wang, Junkun Yuan, Angtian Wang, Haotian Yang, Canyu Zhang, Siyuan Yuan, Xingchang Huang, Bo Liu, Yizhi Wang, Yiding Yang, Chongyang Ma, Gordon Guocheng Qian  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.35768v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pdmd2026.github.io)  
  Keywords: denoising, distillation, video diffusion  
- **[G$^3$-LoRA: Organizing Reward-Weighted Video Data with Gradient-Guided Grouped LoRA](https://arxiv.org/abs/2609.35189v1)**  
  Authors: Jia Song, Wenhow Li, Lichen Bai, Bada Ye, Zeke Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.35189v1.pdf)  
  Keywords: camera motion, denoising, distillation, evaluation, flow matching, t2v, text to video, text-to-video  

### World Models & Simulation

*Showing the latest 50 out of 243 papers*

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
- **[MUGEN: Interactive Panoramic World Exploration via Camera Control](https://arxiv.org/abs/2609.38077v1)**  
  Authors: Jiaming Tan, Zhen Li, Shuwei Shi, Minggui Teng, Siqi Yang, Yuwei Wu, Bo Zheng, Chuanhao Li, Kaipeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38077v1.pdf)  
  Keywords: camera control, camera motion, controllable, interactive, video generation  
- **[WorldLine: Action-Driven Visual Simulation for Robotic Manipulation](https://arxiv.org/abs/2609.38059v1)**  
  Authors: Shenghe Zheng, Wenbo Li, Jiyao Zhang, Bin Xia, Haoyang Huang, Nan Duan, Jiaya Jia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.38059v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://zhengsh123.github.io/WorldLine)  
  Keywords: action-conditioned, distillation, dynamics, efficient, embodied, evaluation, physical, robot learning, simulation, trajectory, video generation  
- **[Geometry-Preserving Human-to-Robot Upper-Body Motion Retargeting from Monocular Video](https://arxiv.org/abs/2609.37776v1)**  
  Authors: Xiaoyu Yang, Sen Han, Da Li, Nan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.37776v1.pdf)  
  Keywords: body motion, physical, simulation, video generation  
- **[Honeycomb: Constant-Size Scene Memory Representation for Video World Models](https://arxiv.org/abs/2609.37690v1)**  
  Authors: Jack Wei Lun Shi, Kaichen Zhou, Haoyu Chen, Yufeng Weng, Keane Ong, Ruojin Cai, Hang Hua, Justin K. W. Yeoh, Mengyu Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.37690v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jackswl.github.io/honeycomb)  
  Keywords: video generation, video world model, world model  
- **[Waypoint-1.5: A Real-Time Video World Model for Consumer Hardware](https://arxiv.org/abs/2609.37107v1)**  
  Authors: Rajit Rajpal, Shahbuland Matiana, Liew Wei Pyn, Anmol Agarwal, Ryan Craig, Andrew Lapp, Mithun Hunsur, Sami BuGhanem, Scottie Fox, Aaron Sanders Carson Poole, Irene Park, Dave Rossi, Spencer Frazier, Louis Castricato  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.37107v1.pdf)  
  Keywords: architecture, game, interactive, video diffusion, video generation, video world model, world model  
- **[RolloutFaith: Auditing Persistent Internal Interventions in Visual World Model](https://arxiv.org/abs/2609.36843v1)**  
  Authors: Junchi Yao, Ziyi Wang, Youling Huang, Lijie Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.36843v1.pdf)  
  Keywords: visual world model, world model  



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
