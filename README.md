# Awesome Video Diffusions [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Video Diffusion Models and Video Generation. Content is automatically updated daily.

🗺️ **[Explore the Paper Atlas](https://longxiang-ai.github.io/awesome-video-diffusions/)**: an interactive paper map, monthly trends, topic network, co-author network and author rankings of every tracked paper.

> Last Update: 2026-10-12 04:37:18

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

- [3D-aware Video Generation](#3d-aware-video-generation) (47 papers) - Video generation with 3D awareness, multi-view consistency, and 4D content creation
- [Applications](#applications) (199 papers) - Domain-specific applications of video diffusion models
- [Architecture & Efficiency](#architecture-&-efficiency) (386 papers) - Architectural innovations (DiT, UNet), flow matching, and training/inference efficiency
- [Audio & Multi-modal](#audio-&-multi-modal) (66 papers) - Audio-driven and multi-modal conditioned video generation
- [Controllable Generation](#controllable-generation) (323 papers) - Controllable video generation with motion, camera, pose, or layout guidance
- [Human & Character Animation](#human-&-character-animation) (55 papers) - Human-centric video generation including talking heads, dance, and character animation
- [Image-to-Video Generation](#image-to-video-generation) (94 papers) - Methods for animating still images into videos
- [Long Video Generation](#long-video-generation) (239 papers) - Generating temporally consistent long-form videos beyond short clips
- [Personalization & Customization](#personalization-&-customization) (157 papers) - Personalized video generation with custom subjects, identities, or styles
- [Physical Understanding](#physical-understanding) (306 papers) - Physics-aware video generation and dynamics modeling
- [Surveys & Benchmarks](#surveys-&-benchmarks) (319 papers) - Survey papers, benchmarks, and evaluation metrics for video generation
- [Text-to-Video Generation](#text-to-video-generation) (140 papers) - Foundation models and methods for generating videos from text prompts
- [Video Editing](#video-editing) (96 papers) - Diffusion-based video editing, style transfer, and manipulation
- [Video Inpainting & Completion](#video-inpainting-&-completion) (21 papers) - Video inpainting, completion, outpainting, and temporal prediction
- [Video Super-Resolution & Enhancement](#video-super-resolution-&-enhancement) (174 papers) - Video quality improvement, upscaling, restoration, and frame interpolation
- [World Models & Simulation](#world-models-&-simulation) (241 papers) - Video generation as world simulators and interactive environment generation



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3D-aware Video Generation

- **[LEGO: A Lifting-Free Approach for Exocentric-to-Egocentric Video Generation](https://arxiv.org/abs/2610.12442v1)**  
  Authors: Suhwan Cho, Yonwoo Choi, Soongjin Kim, Jicheol Park, Taegyu Lim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.12442v1.pdf)  
  Keywords: denoising, diffusion model, layout, novel view, style, video diffusion, video generation  
- **[SymRegFlow: Symmetry-Regularized Flow Matching for Video World Models](https://arxiv.org/abs/2610.02726v1)**  
  Authors: Xi Ye, Yuzhu Wang, Xiaoyang Liu, Jiayi Wang, Yangyang Xu, Ruyu Wang, Wenlin Chen, Duo Su, Jun Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.02726v1.pdf)  
  Keywords: autonomous driving, denoising, driving, flow matching, novel view, video generation, view-consistent  
- **[4Director: Controlling Video World Models with Rigid 3D Geometry](https://arxiv.org/abs/2610.02160v1)**  
  Authors: Wei Cao, Hao Zhang, Vikram Voleti, Yuqun Wu, Mallikarjun B R, Shimon Vainer, Mark Boss, Yaoyao Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.02160v1.pdf)  
  Keywords: dynamics, identity, video world model, view-consistent, world model  
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

### Applications

*Showing the latest 50 out of 199 papers*

- **[Golden Anchor for Video Generation](https://arxiv.org/abs/2610.13217v1)**  
  Authors: Jinyuan Xu, Shitong Shao, Lichen Bai, Zikai Zhou, Guoxi Huang, Nantheera Anantrasirichai, Zeke Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13217v1.pdf)  
  Keywords: game, i2v, identity, image to video, image-to-video, interactive, style, video generation  
- **[Grounded-Dreamer: Robot Learning from World Model Synthetic Data with Physical Grounding](https://arxiv.org/abs/2610.13164v1)**  
  Authors: Feng Jiang, Shu Chen, Yuanfei Wang, Yuan Li, Zhenhao Shen, Jiaqi Liang, Yang Chen, Lei Wei, Chen Xie, Ruihai Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13164v1.pdf)  
  Keywords: dynamics, physical, physics, robot learning, simulation, video world model, world model  
- **[StereoEngine: Scaling Stereo Bimanual Robot Data without Stereo Cameras](https://arxiv.org/abs/2610.12734v1)**  
  Authors: Jason Chen, I-Chun Arthur Liu, Gaurav Sukhatme, Daniel Seita  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.12734v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://stereoengine.github.io)  
  Keywords: autonomous driving, diffusion model, driving, simulation, video diffusion  
- **[Hybrid Cinematography: Previsualizing and Managing Hallucination Risk in Generative Video Reshooting](https://arxiv.org/abs/2610.12455v1)**  
  Authors: Nhan, Tran, Neal Wadhwa, Abe Davis, Stefan Stojanov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.12455v1.pdf)  
  Keywords: creative, film, physical  
- **[WOVEN: Weaving Visual World Modeling into Multimodal LLMs](https://arxiv.org/abs/2610.12417v1)**  
  Authors: Zheyu Fan, Yue Zhang, Mingkai Deng, Kangrui Wang, Qineng Wang, Canyu Chen, Jie Hao, Xing Fan, Chenlei Guo, Eric P. Xing, Mohit Bansal, Manling Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.12417v1.pdf)  
  Keywords: benchmark, embodied, physical, visual world model, world model  
- **[Towards Unified Evaluation of Prompt Enhancers for Video Generation](https://arxiv.org/abs/2610.11736v1)**  
  Authors: Yawen Shao, Yubo Zhu, Ziyun Dai, Zixun Fang, Kai Zhu, Zeyinzi Jiang, Yufeng Ai, Siyang Sun, Haolan Xue, Yu Shang, Yuxiang Bao, Zoubin Bi, Jingming Luo, Jie Xiao, Chaojie Mao, Zhehan Kan, Hongchen Luo, Yu Liu, Sheng Zhong, Wei Tong, Xueyang Fu, Yang Cao, Wei Zhai, Zheng-Jun Zha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11736v1.pdf)  
  Keywords: benchmark, cinematic, evaluation, image to video, image-to-video, text to video, text-to-video, video generation  
- **[AdSpark: A Large-Scale Dataset and Benchmark for Product-Centric Advertisement Video Generation](https://arxiv.org/abs/2610.10047v1)**  
  Authors: Zhifei Yang, Zhao Jiang, Keyang Lu, Honghe Zhu, Zheng Zhang, Jingjing Lv, Changping Peng, Ching Law, Zhen Xiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.10047v1.pdf)  
  Keywords: benchmark, creative, evaluation, identity, video generation  
- **[Beyond Masks and Trajectories: Flow-Guided Latent Action Injection for Stable Surgical Video Generation](https://arxiv.org/abs/2610.09800v1)**  
  Authors: Tsz-Yui Qin, Siyu Zhou, Chi-Keung Tang, Yuxiang Nie, Shu Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.09800v1.pdf)  
  Keywords: architecture, education, evaluation, simulation, video generation  
- **[RLHND: Video Foundation Models as Physically Grounded Hand Trackers for Robot Learning](https://arxiv.org/abs/2610.09455v1)**  
  Authors: Seungjun Moon, Subin Jeon, Sangwoo Kim, Hanbyul Joo, Jinwoo Shin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.09455v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://seungjun-moon.github.io/rlhnd)  
  Keywords: benchmark, physical, robot learning, video diffusion, video foundation model  
- **[RobotAPO: Adversarial Physics Preference Optimization for Robotic Manipulation Video Generation](https://arxiv.org/abs/2610.09454v1)**  
  Authors: Kerui Li, Zhe Jing, Chenyi Huang, Xiaofeng Wang, Zheng Zhu, Haoming Cui, Huaibo Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.09454v1.pdf)  
  Keywords: denoising, embodied, flow matching, physical, physical consistency, physics, video generation  

### Architecture & Efficiency

*Showing the latest 50 out of 386 papers*

- **[SmolWAM: A Latent World-Action Model for Robotic Manipulation on Edge Devices](https://arxiv.org/abs/2610.13740v1)**  
  Authors: Timi Owolabi, Hikmah Olawore, Frances Adelakun, Ayotomiwa Oyewumi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13740v1.pdf)  
  Keywords: rectified flow, video diffusion  
- **[LETHE: Defending against Unauthorized Image-to-Video Generation via Value Diversity Collapse](https://arxiv.org/abs/2610.13333v1)**  
  Authors: Boheng Li, Yueming Xing, Yiming Li, Jie Zhang, Tianwei Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13333v1.pdf)  
  Keywords: efficient, i2v, image to video, image-to-video, video generation  
- **[PAGE: Parts-Aware Guidance for Co-Speech Gesture Portrait Video Generation](https://arxiv.org/abs/2610.13301v1)**  
  Authors: Yabiao Wang, Jiafu Wu, Yicheng Xu, Teng Hu, Shengzhe Zhou, Yanxiao Sun, Jiangning Zhang, Ying Tai, Yong Liu, Ming-Hsuan Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13301v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://aigc-explorer.github.io/PAGE)  
  Keywords: audio-driven, benchmark, body motion, denoising, efficient, evaluation, gesture, trajectory, video generation  
- **[Destination-Conditioned Adaptation with Semantic-Geometric Alignment for Generative Inbetweening](https://arxiv.org/abs/2610.13187v1)**  
  Authors: Zhiyu Xu, Wei Shang, Yushen Xu, Wenwen Li, Zhiyan Xu, Pengfei Zhu, Dongwei Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13187v1.pdf)  
  Keywords: dynamics, flow matching, image to video, image-to-video, latent video, latent video diffusion, trajectory, video diffusion  
- **[PreCoG: Preview-Edit for Efficient Video Correction in Generation-Time](https://arxiv.org/abs/2610.13174v1)**  
  Authors: Yilai Liu, Wenqi Pei, Zhifeng Lu, Shiyuan Zhang, Zongxi Liu, Hongyang Du  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13174v1.pdf)  
  Keywords: efficient, t2v, text to video, text-to-video, trajectory, video generation  
- **[Unified Generative Video Compression with Autoregressive and Bidirectional Video Diffusion](https://arxiv.org/abs/2610.13023v1)**  
  Authors: Tianyu Zhang, Shuai Huo, Dengchao Jin, Hewei Liu, Meng Lei, Tianwen Wu, Jiawen Gu, Chao Zhou, Li Li, Dong Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13023v1.pdf)  
  Keywords: autoregressive, distillation, dit, streaming, video diffusion  
- **[DiffusionART: Efficient, Stable and Scalable Reinforcement of Diffusion Models](https://arxiv.org/abs/2610.12572v1)**  
  Authors: Zhenglin Wan, Jiayu Chen, Zhengfeiyang Zhang, Pengfei Zhou, Wangbo Zhao, Fangyuan Kong, Pengfei Wan, Kun Gai, Yang You  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.12572v1.pdf)  
  Keywords: efficient, style, video generation  
- **[Connected Self Forcing: Beyond Local Learning in Video Autoregression](https://arxiv.org/abs/2610.12156v1)**  
  Authors: Dongbin Zhang, Chaoda Zheng, Kangjie Chen, Xiangyu Li, Shijia Chen, Jinhao Deng, Yuqi Zhang, Guangfeng Jiang, Hongbin Lin, Choo Sin Wai, Minqi Wang, Puyi Wang, Jingye Zhang, Yu Zhang, Xianming Liu, Boyang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.12156v1.pdf)  
  Keywords: autoregressive, autoregressive video, distillation, efficient, temporal consistency, video generation  
- **[Phase-aware video generation for physics-grounded dynamics and interactions](https://arxiv.org/abs/2610.11791v1)**  
  Authors: Jingfeng Ou, Kun Wang, Rui Zhao, Jingwei Guan, Limin Wang, Chao Dong, Xingyu Zeng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11791v1.pdf)  
  Keywords: architecture, dynamics, physical, physical plausibility, physics, simulation, video generation  
- **[Parametric Trajectory Distillation for Few-Step Video Generation](https://arxiv.org/abs/2610.11498v1)**  
  Authors: Lan Feng, Peter Karkus, Maximilian Igl, Julius Berner, Yuxiao Chen, Shuhan Tan, Alexandre Alahi, Boris Ivanovic, Marco Pavone  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11498v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://alan-lanfeng.github.io/PTD)  
  Keywords: architecture, distillation, trajectory, video diffusion, video generation  

### Audio & Multi-modal

*Showing the latest 50 out of 66 papers*

- **[PAGE: Parts-Aware Guidance for Co-Speech Gesture Portrait Video Generation](https://arxiv.org/abs/2610.13301v1)**  
  Authors: Yabiao Wang, Jiafu Wu, Yicheng Xu, Teng Hu, Shengzhe Zhou, Yanxiao Sun, Jiangning Zhang, Ying Tai, Yong Liu, Ming-Hsuan Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13301v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://aigc-explorer.github.io/PAGE)  
  Keywords: audio-driven, benchmark, body motion, denoising, efficient, evaluation, gesture, trajectory, video generation  
- **[AV-FlowEdit: Training-Free Prompt-Driven Audio-Visual Editing with Event-Aware Spectral Trajectory Preservation](https://arxiv.org/abs/2610.13072v1)**  
  Authors: Shaohua Pan, Xiao Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13072v1.pdf)  
  Keywords: joint audio-video, temporal consistency, trajectory, video diffusion, video editing  
- **[Real-Time Joint Audio-Video Generation by Parallel Adapter Composition](https://arxiv.org/abs/2610.10343v2)**  
  Authors: Jingyu Li, Xiaoxiao Xiang, Yiwen Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.10343v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://pac-demo-2027.github.io/demo/) | [![Demo](https://img.shields.io/badge/-Demo-brightgreen)](https://pac-demo-2027.github.io/demo)  
  Keywords: audio-video generation, autoregressive, diffusion transformer, interactive, joint audio-video, streaming, video diffusion, video diffusion transformer, video generation  
- **[Kandinsky 6.0 Video: Foundation Models for Synchronized Video and Audio Generation](https://arxiv.org/abs/2610.05608v1)**  
  Authors: Team Kandinsky, Julia Agafonova, Bulat Akhmatov, Mikhail Aksyutin, Grigorii Alekseenko, Anastasia Aliaskina, Olga Androsova, Vladimir Arkhipkin, Anna Averchenkova, Alexander Belykh, Serafima Bocharova, Sofiya Bogakovskaya, Anton Bukashkin, Mark Bulygin, Kirill Buzygin, Irina Cheremnykh, Kirill Chernyshev, Mikhail Chernyshov, Vladimir Chernyy, David Chikovani, Georgy Daniltsev, Denis Dimitrov, Anna Dmitrienko, Vladimir Dokholyan, Sergey Emelyanov, Dmitry Ermilov, Georgii Fedorov, Polina Gavrilova, Nikolai Gerasimenko, Aleksandr Gordeev, Andrey Inozemtsev, Andrei Ivaniuta, Alexander Ivanov, Mikhail Karaev, Anastasiia Kargapoltseva, Ivan Kirillov, Nikita Kiselev, Valeria Kobenko, Yury Kolabushin, Denis Koposov, Anatoly Korobov, Vladimir Korviakov, Kirill Kozlov, Denis Krzhivokolskiy, Konstantin Kuklev, Alexander Kunitsyn, Sergey Kuzin, Vladislav Lakhtionov, Alexey Letunovskiy, Maxim Litvinov, Alexander Lyulkov, Georgy Makarov, Kirill Malakhov, Egor Malykh, Mikhail Mamaev, Dmitrii Mikhailov, Polina Mikhailova, Ivan Mikheev, Elizaveta Muromtseva, Nikolai Nazarkin, Tatiana Nikulina, Lev Novitskiy, Stanislav Onuchin, Nikita Osterov, Denis Parkhomenko, Anatoliy Parpara, Vladimir Polovnikov, Konstantin Reznikov, Azat Saginbaev, Nikita Samsonov, Alexander Sentsov, Nikita Shaimov, Artem Sherstyuk, Andrey Shutkin, Egor Silvestrov, Bulat Suleimanov, Matvey Suprunov, Sergey Taranov, Irina Tolstykh, Tatiana Trofimuk, Ilya Trushkin, Aleksandra Tsybina, Olga Varlashina, Viacheslav Vasilev, Ilya Vasiliev, Eugeny Vilisov, Sergey Yakubson, Konstantin Zakharov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.05608v1.pdf)  
  Keywords: architecture, audio-video generation, distillation, evaluation, human evaluation, super-resolution, video generation  
- **[DMAD: Distribution Matching as Adversarial Distillation for Fast Visual Generation](https://arxiv.org/abs/2610.02188v1)**  
  Authors: Zhengming Yu, Junkun Yuan, Haotian Yang, Gordon Guocheng Qian, Yizhi Wang, Angtian Wang, Yiding Yang, Bo Liu, Xin Li, Wenping Wang, Chongyang Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.02188v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yzmblog.github.io/projects/DMAD)  
  Keywords: audio-video generation, diffusion model, distillation, identity, joint audio-video, t2v, video generation  
- **[Soundwich: Video Generation with Layered and Controllable Audio](https://arxiv.org/abs/2610.00691v2)**  
  Authors: Zhuo Ning, AmirHossein Naghi Razlighi, Sagi Polaczek, Daniel Cohen-Or, Ali Mahdavi-Amiri  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.00691v2.pdf) | [![GitHub](https://img.shields.io/github/stars/CodyNing/Soundwich?style=social)](https://github.com/CodyNing/Soundwich)  
  Keywords: controllable, flow matching, joint audio-video, sound, video flow matching, video generation  
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

### Controllable Generation

*Showing the latest 50 out of 323 papers*

- **[PhysForge: Material-Controllable 3D Reconstruction with Separable Components](https://arxiv.org/abs/2610.13681v1)**  
  Authors: Yuchen Wang, Yanqi Bao, Zheng Gu, Zhengqing Chen, Jieqi Shi, Jing Huo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13681v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://masterwanna.github.io/PhysForge.html)  
  Keywords: controllable, diffusion model, dynamics, physical, simulation, video diffusion  
- **[Beyond Successful Robot Demonstrations: Learning from Human Interactions and Modeling Failure Dynamics](https://arxiv.org/abs/2610.13522v1)**  
  Authors: Peiyan Tu, Cong Wang, Hanxin Zhu, Xin Jin, Zhibo Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13522v1.pdf)  
  Keywords: action-conditioned, camera motion, dynamics, evaluation, physical, physical plausibility, video generation, world model  
- **[TextVBench: Evaluating Text Rendering and Preservation in Video Generation](https://arxiv.org/abs/2610.13412v1)**  
  Authors: Ruiqiang Zhang, Hengyi Wang, Chang Liu, Guanjie Wang, Zehua Ma, Weiming Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13412v1.pdf)  
  Keywords: benchmark, evaluation, layout, t2v, video generation  
- **[PAGE: Parts-Aware Guidance for Co-Speech Gesture Portrait Video Generation](https://arxiv.org/abs/2610.13301v1)**  
  Authors: Yabiao Wang, Jiafu Wu, Yicheng Xu, Teng Hu, Shengzhe Zhou, Yanxiao Sun, Jiangning Zhang, Ying Tai, Yong Liu, Ming-Hsuan Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13301v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://aigc-explorer.github.io/PAGE)  
  Keywords: audio-driven, benchmark, body motion, denoising, efficient, evaluation, gesture, trajectory, video generation  
- **[Destination-Conditioned Adaptation with Semantic-Geometric Alignment for Generative Inbetweening](https://arxiv.org/abs/2610.13187v1)**  
  Authors: Zhiyu Xu, Wei Shang, Yushen Xu, Wenwen Li, Zhiyan Xu, Pengfei Zhu, Dongwei Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13187v1.pdf)  
  Keywords: dynamics, flow matching, image to video, image-to-video, latent video, latent video diffusion, trajectory, video diffusion  
- **[PreCoG: Preview-Edit for Efficient Video Correction in Generation-Time](https://arxiv.org/abs/2610.13174v1)**  
  Authors: Yilai Liu, Wenqi Pei, Zhifeng Lu, Shiyuan Zhang, Zongxi Liu, Hongyang Du  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13174v1.pdf)  
  Keywords: efficient, t2v, text to video, text-to-video, trajectory, video generation  
- **[AV-FlowEdit: Training-Free Prompt-Driven Audio-Visual Editing with Event-Aware Spectral Trajectory Preservation](https://arxiv.org/abs/2610.13072v1)**  
  Authors: Shaohua Pan, Xiao Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13072v1.pdf)  
  Keywords: joint audio-video, temporal consistency, trajectory, video diffusion, video editing  
- **[CASTER: Formalizing Zero-Shot Manipulation from Synthetic Videos as Constrained Optimization](https://arxiv.org/abs/2610.12567v1)**  
  Authors: Yinlong Dai, Homanga Bharadhwaj, Dylan P. Losey  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.12567v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://collab.me.vt.edu/CASTER)  
  Keywords: physical, physical consistency, trajectory, video generation  
- **[LEGO: A Lifting-Free Approach for Exocentric-to-Egocentric Video Generation](https://arxiv.org/abs/2610.12442v1)**  
  Authors: Suhwan Cho, Yonwoo Choi, Soongjin Kim, Jicheol Park, Taegyu Lim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.12442v1.pdf)  
  Keywords: denoising, diffusion model, layout, novel view, style, video diffusion, video generation  
- **[WorldAlign: Decoupled 4D Reward for World-Consistent Video Generation](https://arxiv.org/abs/2610.12382v1)**  
  Authors: Jing He, Kaixin Ding, Xingye Tian, Guibao Shen, Wenhang Ge, Xin Tao, Pengfei Wan, Ying-Cong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.12382v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://worldalign.github.io)  
  Keywords: camera motion, evaluation, image to video, image-to-video, physical, physical plausibility, simulation, video generation, world simulation  

### Human & Character Animation

*Showing the latest 50 out of 55 papers*

- **[PAGE: Parts-Aware Guidance for Co-Speech Gesture Portrait Video Generation](https://arxiv.org/abs/2610.13301v1)**  
  Authors: Yabiao Wang, Jiafu Wu, Yicheng Xu, Teng Hu, Shengzhe Zhou, Yanxiao Sun, Jiangning Zhang, Ying Tai, Yong Liu, Ming-Hsuan Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13301v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://aigc-explorer.github.io/PAGE)  
  Keywords: audio-driven, benchmark, body motion, denoising, efficient, evaluation, gesture, trajectory, video generation  
- **[PVSync: A Unified Lip-Sync Expert for Timing and Articulation](https://arxiv.org/abs/2610.09223v1)**  
  Authors: Kevin Stephen, Varun Menon, Timo Mertens, Nikita Drobyshev  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.09223v1.pdf)  
  Keywords: benchmark, talking head, video generation  
- **[PixReenact: Pixel-Conditioned Causal Video Diffusion for Streaming Head-Avatar Reenactment](https://arxiv.org/abs/2610.05233v1)**  
  Authors: Gavriel Habib, Dvir Samuel, Or Shimshi, Rami Ben-Ari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.05233v1.pdf)  
  Keywords: autoregressive, avatar, benchmark, denoising, distillation, driving, identity, motion transfer, streaming, video diffusion  
- **[Parasitic Co-Denoising: Unlocking 3D Human Motion Generation in a Frozen Video Diffusion Model](https://arxiv.org/abs/2610.03047v1)**  
  Authors: Yunjiao Zhou, Junlang Qian, Lihua Xie, Jianfei Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.03047v1.pdf)  
  Keywords: denoising, diffusion model, efficient, flow matching, human motion, text to video, text-to-video, video diffusion  
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
- **[WB-WAM: Heterogeneous Body-Hand Pre-training for Humanoid Loco-Manipulation](https://arxiv.org/abs/2609.34199v3)**  
  Authors: Chuan Qin, Shaoting Zhu, Siyuan Luo, Siqiao Huang, Hongyu Zhao, Shanaka Baduge, Hang Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.34199v3.pdf)  
  Keywords: body motion, efficient, human motion, motion transfer, physical, simulation  

### Image-to-Video Generation

*Showing the latest 50 out of 94 papers*

- **[Images Talk Back: Guiding MMDiTs by Suppressing Image-to-Text Feedback](https://arxiv.org/abs/2610.13941v1)**  
  Authors: Yucheng Yang, Xiaoxiao Sun, Shusheng Yang, Jiakang Chen, Serena Yeung-Levy  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13941v1.pdf) | [![GitHub](https://img.shields.io/github/stars/yyc1215lll-creator/SFG?style=social)](https://github.com/yyc1215lll-creator/SFG)  
  Keywords: image to video, image-to-video, text to video, text-to-video, video generation  
- **[LETHE: Defending against Unauthorized Image-to-Video Generation via Value Diversity Collapse](https://arxiv.org/abs/2610.13333v1)**  
  Authors: Boheng Li, Yueming Xing, Yiming Li, Jie Zhang, Tianwei Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13333v1.pdf)  
  Keywords: efficient, i2v, image to video, image-to-video, video generation  
- **[Golden Anchor for Video Generation](https://arxiv.org/abs/2610.13217v1)**  
  Authors: Jinyuan Xu, Shitong Shao, Lichen Bai, Zikai Zhou, Guoxi Huang, Nantheera Anantrasirichai, Zeke Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13217v1.pdf)  
  Keywords: game, i2v, identity, image to video, image-to-video, interactive, style, video generation  
- **[Destination-Conditioned Adaptation with Semantic-Geometric Alignment for Generative Inbetweening](https://arxiv.org/abs/2610.13187v1)**  
  Authors: Zhiyu Xu, Wei Shang, Yushen Xu, Wenwen Li, Zhiyan Xu, Pengfei Zhu, Dongwei Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13187v1.pdf)  
  Keywords: dynamics, flow matching, image to video, image-to-video, latent video, latent video diffusion, trajectory, video diffusion  
- **[WorldAlign: Decoupled 4D Reward for World-Consistent Video Generation](https://arxiv.org/abs/2610.12382v1)**  
  Authors: Jing He, Kaixin Ding, Xingye Tian, Guibao Shen, Wenhang Ge, Xin Tao, Pengfei Wan, Ying-Cong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.12382v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://worldalign.github.io)  
  Keywords: camera motion, evaluation, image to video, image-to-video, physical, physical plausibility, simulation, video generation, world simulation  
- **[Towards Unified Evaluation of Prompt Enhancers for Video Generation](https://arxiv.org/abs/2610.11736v1)**  
  Authors: Yawen Shao, Yubo Zhu, Ziyun Dai, Zixun Fang, Kai Zhu, Zeyinzi Jiang, Yufeng Ai, Siyang Sun, Haolan Xue, Yu Shang, Yuxiang Bao, Zoubin Bi, Jingming Luo, Jie Xiao, Chaojie Mao, Zhehan Kan, Hongchen Luo, Yu Liu, Sheng Zhong, Wei Tong, Xueyang Fu, Yang Cao, Wei Zhai, Zheng-Jun Zha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11736v1.pdf)  
  Keywords: benchmark, cinematic, evaluation, image to video, image-to-video, text to video, text-to-video, video generation  
- **[Transforming Image Editors into Video Editors](https://arxiv.org/abs/2610.11037v1)**  
  Authors: Feng Wang, Zijie Li, Ceyuan Yang, Alan Yuille, Peng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11037v1.pdf) | [![GitHub](https://img.shields.io/github/stars/wangf3014/AVE?style=social)](https://github.com/wangf3014/AVE)  
  Keywords: diffusion model, image to video, image-to-video, temporal consistency, video diffusion, video editing  
- **[GRACE: Generation-aware latent compression for efficient video generation](https://arxiv.org/abs/2610.10524v1)**  
  Authors: Jiyoung Kim, Paul Hyunbin Cho, Jisu Nam, Donghoon Lee, Hyunsung Go, Yeonkyeong Lee, Hansaem Kim, Seungryong Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.10524v1.pdf)  
  Keywords: denoising, diffusion transformer, dit, efficient, i2v, video autoencoder, video diffusion, video generation  
- **[TasteRoute: Personalized Routing for Video Generation](https://arxiv.org/abs/2610.05896v1)**  
  Authors: Zhi Rui Tam, Chao-Chung Wu, Sin-Han Yang, Peyton Ku, Brendan Kuang, Tzu-Ting Hsieh, Min-Fang Hsu, Fang-Ling Tsai, Yun-Nung Chen, Wei-Chiu Ma, Chieh-Yen Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.05896v1.pdf)  
  Keywords: image to video, image-to-video, text to video, text-to-video, video generation  
- **[Generating the Wild: Individual-Consistent Image-to-Video Generation for Wildlife](https://arxiv.org/abs/2610.05587v1)**  
  Authors: Yuzhuo Li, Di Zhao, Xinyu Zhang, Daniel Wilson, Yun Sing Koh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.05587v1.pdf)  
  Keywords: evaluation, i2v, identity, image to video, image-to-video, layout, video generation  

### Long Video Generation

*Showing the latest 50 out of 239 papers*

- **[High-Throughput Generative Video Super-Resolution on a Single Consumer GPU](https://arxiv.org/abs/2610.13179v1)**  
  Authors: Georgios Panaretou, Sotirios Chatzis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13179v1.pdf)  
  Keywords: super-resolution, temporal consistency, upscaling  
- **[AV-FlowEdit: Training-Free Prompt-Driven Audio-Visual Editing with Event-Aware Spectral Trajectory Preservation](https://arxiv.org/abs/2610.13072v1)**  
  Authors: Shaohua Pan, Xiao Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13072v1.pdf)  
  Keywords: joint audio-video, temporal consistency, trajectory, video diffusion, video editing  
- **[Unified Generative Video Compression with Autoregressive and Bidirectional Video Diffusion](https://arxiv.org/abs/2610.13023v1)**  
  Authors: Tianyu Zhang, Shuai Huo, Dengchao Jin, Hewei Liu, Meng Lei, Tianwen Wu, Jiawen Gu, Chao Zhou, Li Li, Dong Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13023v1.pdf)  
  Keywords: autoregressive, distillation, dit, streaming, video diffusion  
- **[ForcingBooster: Adaptive Patch-wise Denoising for Fast Autoregressive Video Diffusion](https://arxiv.org/abs/2610.12625v1)**  
  Authors: Zekai Gu, Peng Wang, Jiahao Lu, Yongsen Mao, Cheng Lin, Yuan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.12625v1.pdf)  
  Keywords: autoregressive, autoregressive video, denoising, interactive, video diffusion, video generation  
- **[Connected Self Forcing: Beyond Local Learning in Video Autoregression](https://arxiv.org/abs/2610.12156v1)**  
  Authors: Dongbin Zhang, Chaoda Zheng, Kangjie Chen, Xiangyu Li, Shijia Chen, Jinhao Deng, Yuqi Zhang, Guangfeng Jiang, Hongbin Lin, Choo Sin Wai, Minqi Wang, Puyi Wang, Jingye Zhang, Yu Zhang, Xianming Liu, Boyang Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.12156v1.pdf)  
  Keywords: autoregressive, autoregressive video, distillation, efficient, temporal consistency, video generation  
- **[Memory Forcing: Attendable Mid-Horizon History for Streaming Video Generation](https://arxiv.org/abs/2610.11756v1)**  
  Authors: Jiaming Zhang, Xinyu Wang, Huafeng Shi, Gangshan Wu, Limin Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11756v1.pdf)  
  Keywords: autoregressive, autoregressive video, streaming, streaming video generation, video diffusion, video generation  
- **[Conditional Residual Prediction: Improving Autoregressive Video Diffusion without a Bidirectional Teacher](https://arxiv.org/abs/2610.11479v1)**  
  Authors: Bowen Zheng, Zhiguang Liu, Jiarong Ou, Rui Chen, Tianyang Hu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11479v1.pdf)  
  Keywords: autoregressive, autoregressive video, distillation, interactive, long video, streaming, video diffusion, video generation  
- **[Transforming Image Editors into Video Editors](https://arxiv.org/abs/2610.11037v1)**  
  Authors: Feng Wang, Zijie Li, Ceyuan Yang, Alan Yuille, Peng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11037v1.pdf) | [![GitHub](https://img.shields.io/github/stars/wangf3014/AVE?style=social)](https://github.com/wangf3014/AVE)  
  Keywords: diffusion model, image to video, image-to-video, temporal consistency, video diffusion, video editing  
- **[CORAL-KV: Compact Cross-Layer Prediction and Residual Coding for Autoregressive Video KV Caches](https://arxiv.org/abs/2610.12514v1)**  
  Authors: Albert Ge, Akash Haridas, Utkarsh Saxena, Ruijing Yang, Ian Colbert, Frederic Sala, Vikram Appia, Emad Barsoum  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.12514v1.pdf)  
  Keywords: autoregressive, autoregressive video, long video, video diffusion, video generation  
- **[SGF+: Decoupling Gradient Flows for Autoregressive Video Generation](https://arxiv.org/abs/2610.10429v2)**  
  Authors: Zihan Su, Junhao Zhuang, Yaowei Li, Siwen Lu, Haoran Li, Lingen Li, Haoyu Wu, Weiyang Jin, Songchun Zhang, Haoyang Huang, Chun Yuan, Zeyue Xue, Nan Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.10429v2.pdf)  
  Keywords: autoregressive, autoregressive video, denoising, long video, temporal consistency, video generation  

### Personalization & Customization

*Showing the latest 50 out of 157 papers*

- **[KVeil: First-Place Solution to ECCV 2026 LifeGenIP Challenge on Unlearnable Videos](https://arxiv.org/abs/2610.13733v1)**  
  Authors: Boheng Li, Yueming Xing, Yiming Li, Jie Zhang, Han Qiu, Tianwei Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13733v1.pdf) | [![GitHub](https://img.shields.io/github/stars/AntigoneRandy/KVeil?style=social)](https://github.com/AntigoneRandy/KVeil)  
  Keywords: customization, identity, video generation  
- **[Golden Anchor for Video Generation](https://arxiv.org/abs/2610.13217v1)**  
  Authors: Jinyuan Xu, Shitong Shao, Lichen Bai, Zikai Zhou, Guoxi Huang, Nantheera Anantrasirichai, Zeke Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13217v1.pdf)  
  Keywords: game, i2v, identity, image to video, image-to-video, interactive, style, video generation  
- **[DiffusionART: Efficient, Stable and Scalable Reinforcement of Diffusion Models](https://arxiv.org/abs/2610.12572v1)**  
  Authors: Zhenglin Wan, Jiayu Chen, Zhengfeiyang Zhang, Pengfei Zhou, Wangbo Zhao, Fangyuan Kong, Pengfei Wan, Kun Gai, Yang You  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.12572v1.pdf)  
  Keywords: efficient, style, video generation  
- **[LEGO: A Lifting-Free Approach for Exocentric-to-Egocentric Video Generation](https://arxiv.org/abs/2610.12442v1)**  
  Authors: Suhwan Cho, Yonwoo Choi, Soongjin Kim, Jicheol Park, Taegyu Lim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.12442v1.pdf)  
  Keywords: denoising, diffusion model, layout, novel view, style, video diffusion, video generation  
- **[Expression-Diverse References for Identity-Preserving Video Generation](https://arxiv.org/abs/2610.11023v1)**  
  Authors: Tianwen Fu, Wenbin Teng, Gonglin Chen, Junyi Ouyang, Haolin Xiong, Yajie Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11023v1.pdf)  
  Keywords: benchmark, evaluation, identity, identity-preserving, video generation  
- **[AdSpark: A Large-Scale Dataset and Benchmark for Product-Centric Advertisement Video Generation](https://arxiv.org/abs/2610.10047v1)**  
  Authors: Zhifei Yang, Zhao Jiang, Keyang Lu, Honghe Zhu, Zheng Zhang, Jingjing Lv, Changping Peng, Ching Law, Zhen Xiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.10047v1.pdf)  
  Keywords: benchmark, creative, evaluation, identity, video generation  
- **[Diverse Motion Customization via Control-based Dynamic Optimization](https://arxiv.org/abs/2610.07911v2)**  
  Authors: Youngyoon Choi, Kihyun Kim, Jeongwoo Shin, Joonseok Lee  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.07911v2.pdf)  
  Keywords: customization, dynamics, video generation  
- **[Generating the Wild: Individual-Consistent Image-to-Video Generation for Wildlife](https://arxiv.org/abs/2610.05587v1)**  
  Authors: Yuzhuo Li, Di Zhao, Xinyu Zhang, Daniel Wilson, Yun Sing Koh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.05587v1.pdf)  
  Keywords: evaluation, i2v, identity, image to video, image-to-video, layout, video generation  
- **[PixReenact: Pixel-Conditioned Causal Video Diffusion for Streaming Head-Avatar Reenactment](https://arxiv.org/abs/2610.05233v1)**  
  Authors: Gavriel Habib, Dvir Samuel, Or Shimshi, Rami Ben-Ari  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.05233v1.pdf)  
  Keywords: autoregressive, avatar, benchmark, denoising, distillation, driving, identity, motion transfer, streaming, video diffusion  
- **[SemCam: Semantic Camera Motion Control for Video Generation](https://arxiv.org/abs/2610.05141v1)**  
  Authors: Janna Bruner, Omer Talmi, Ianir Ideses, Lior Fritz, Lior Wolf, Sagie Benaim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.05141v1.pdf)  
  Keywords: benchmark, camera motion, identity, motion control, trajectory, video generation, video to video, video-to-video  

### Physical Understanding

*Showing the latest 50 out of 306 papers*

- **[PhysForge: Material-Controllable 3D Reconstruction with Separable Components](https://arxiv.org/abs/2610.13681v1)**  
  Authors: Yuchen Wang, Yanqi Bao, Zheng Gu, Zhengqing Chen, Jieqi Shi, Jing Huo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13681v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://masterwanna.github.io/PhysForge.html)  
  Keywords: controllable, diffusion model, dynamics, physical, simulation, video diffusion  
- **[Beyond Successful Robot Demonstrations: Learning from Human Interactions and Modeling Failure Dynamics](https://arxiv.org/abs/2610.13522v1)**  
  Authors: Peiyan Tu, Cong Wang, Hanxin Zhu, Xin Jin, Zhibo Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13522v1.pdf)  
  Keywords: action-conditioned, camera motion, dynamics, evaluation, physical, physical plausibility, video generation, world model  
- **[Destination-Conditioned Adaptation with Semantic-Geometric Alignment for Generative Inbetweening](https://arxiv.org/abs/2610.13187v1)**  
  Authors: Zhiyu Xu, Wei Shang, Yushen Xu, Wenwen Li, Zhiyan Xu, Pengfei Zhu, Dongwei Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13187v1.pdf)  
  Keywords: dynamics, flow matching, image to video, image-to-video, latent video, latent video diffusion, trajectory, video diffusion  
- **[Grounded-Dreamer: Robot Learning from World Model Synthetic Data with Physical Grounding](https://arxiv.org/abs/2610.13164v1)**  
  Authors: Feng Jiang, Shu Chen, Yuanfei Wang, Yuan Li, Zhenhao Shen, Jiaqi Liang, Yang Chen, Lei Wei, Chen Xie, Ruihai Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13164v1.pdf)  
  Keywords: dynamics, physical, physics, robot learning, simulation, video world model, world model  
- **[CASTER: Formalizing Zero-Shot Manipulation from Synthetic Videos as Constrained Optimization](https://arxiv.org/abs/2610.12567v1)**  
  Authors: Yinlong Dai, Homanga Bharadhwaj, Dylan P. Losey  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.12567v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://collab.me.vt.edu/CASTER)  
  Keywords: physical, physical consistency, trajectory, video generation  
- **[Hybrid Cinematography: Previsualizing and Managing Hallucination Risk in Generative Video Reshooting](https://arxiv.org/abs/2610.12455v1)**  
  Authors: Nhan, Tran, Neal Wadhwa, Abe Davis, Stefan Stojanov  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.12455v1.pdf)  
  Keywords: creative, film, physical  
- **[WOVEN: Weaving Visual World Modeling into Multimodal LLMs](https://arxiv.org/abs/2610.12417v1)**  
  Authors: Zheyu Fan, Yue Zhang, Mingkai Deng, Kangrui Wang, Qineng Wang, Canyu Chen, Jie Hao, Xing Fan, Chenlei Guo, Eric P. Xing, Mohit Bansal, Manling Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.12417v1.pdf)  
  Keywords: benchmark, embodied, physical, visual world model, world model  
- **[WorldAlign: Decoupled 4D Reward for World-Consistent Video Generation](https://arxiv.org/abs/2610.12382v1)**  
  Authors: Jing He, Kaixin Ding, Xingye Tian, Guibao Shen, Wenhang Ge, Xin Tao, Pengfei Wan, Ying-Cong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.12382v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://worldalign.github.io)  
  Keywords: camera motion, evaluation, image to video, image-to-video, physical, physical plausibility, simulation, video generation, world simulation  
- **[Phase-aware video generation for physics-grounded dynamics and interactions](https://arxiv.org/abs/2610.11791v1)**  
  Authors: Jingfeng Ou, Kun Wang, Rui Zhao, Jingwei Guan, Limin Wang, Chao Dong, Xingyu Zeng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11791v1.pdf)  
  Keywords: architecture, dynamics, physical, physical plausibility, physics, simulation, video generation  
- **[4-Tensor Attention Model for Semantic Physical Reality](https://arxiv.org/abs/2610.11716v1)**  
  Authors: Jongwook Kim, Sangheon Yun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11716v1.pdf)  
  Keywords: physical, video generation  

### Surveys & Benchmarks

*Showing the latest 50 out of 319 papers*

- **[HorizonNav: Geometry-Guided Video Diffusion for Anticipatory 3D Robot Navigation](https://arxiv.org/abs/2610.13849v1)**  
  Authors: Hajira Amjad, Valerii Serpiva, Viacheslav Liubimov, Didar Seyidov, Dzmitry Tsetserukou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13849v1.pdf)  
  Keywords: diffusion model, evaluation, video diffusion  
- **[Beyond Successful Robot Demonstrations: Learning from Human Interactions and Modeling Failure Dynamics](https://arxiv.org/abs/2610.13522v1)**  
  Authors: Peiyan Tu, Cong Wang, Hanxin Zhu, Xin Jin, Zhibo Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13522v1.pdf)  
  Keywords: action-conditioned, camera motion, dynamics, evaluation, physical, physical plausibility, video generation, world model  
- **[TextVBench: Evaluating Text Rendering and Preservation in Video Generation](https://arxiv.org/abs/2610.13412v1)**  
  Authors: Ruiqiang Zhang, Hengyi Wang, Chang Liu, Guanjie Wang, Zehua Ma, Weiming Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13412v1.pdf)  
  Keywords: benchmark, evaluation, layout, t2v, video generation  
- **[PAGE: Parts-Aware Guidance for Co-Speech Gesture Portrait Video Generation](https://arxiv.org/abs/2610.13301v1)**  
  Authors: Yabiao Wang, Jiafu Wu, Yicheng Xu, Teng Hu, Shengzhe Zhou, Yanxiao Sun, Jiangning Zhang, Ying Tai, Yong Liu, Ming-Hsuan Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13301v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://aigc-explorer.github.io/PAGE)  
  Keywords: audio-driven, benchmark, body motion, denoising, efficient, evaluation, gesture, trajectory, video generation  
- **[MotionCoach: Constructing Multimodal Guidance for Video Professional Motion Editing](https://arxiv.org/abs/2610.12963v1)**  
  Authors: Siyi Qian, Hanqing Yang, Weihuang Lin, Zihao Yang, Yichen Lu, Yuanhong Zheng, Sheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.12963v1.pdf)  
  Keywords: evaluation, motion editing, video editing  
- **[WOVEN: Weaving Visual World Modeling into Multimodal LLMs](https://arxiv.org/abs/2610.12417v1)**  
  Authors: Zheyu Fan, Yue Zhang, Mingkai Deng, Kangrui Wang, Qineng Wang, Canyu Chen, Jie Hao, Xing Fan, Chenlei Guo, Eric P. Xing, Mohit Bansal, Manling Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.12417v1.pdf)  
  Keywords: benchmark, embodied, physical, visual world model, world model  
- **[WorldAlign: Decoupled 4D Reward for World-Consistent Video Generation](https://arxiv.org/abs/2610.12382v1)**  
  Authors: Jing He, Kaixin Ding, Xingye Tian, Guibao Shen, Wenhang Ge, Xin Tao, Pengfei Wan, Ying-Cong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.12382v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://worldalign.github.io)  
  Keywords: camera motion, evaluation, image to video, image-to-video, physical, physical plausibility, simulation, video generation, world simulation  
- **[From Video Clips to Creation Trajectory: Sora100K for AI-Native Video Creation](https://arxiv.org/abs/2610.11770v1)**  
  Authors: Sicong Yang, Ruihuan Yang, Jian Lu, Jianfei Yuan, Xiaodong Cun, Xiuli Bi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11770v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://huggingface.co/datasets/ysicong/Sora100K.) | [![Dataset](https://img.shields.io/badge/-Dataset-orange)](https://huggingface.co/datasets/ysicong/Sora100K)  
  Keywords: evaluation, text to video, text-to-video, trajectory, video editing, video generation  
- **[Towards Unified Evaluation of Prompt Enhancers for Video Generation](https://arxiv.org/abs/2610.11736v1)**  
  Authors: Yawen Shao, Yubo Zhu, Ziyun Dai, Zixun Fang, Kai Zhu, Zeyinzi Jiang, Yufeng Ai, Siyang Sun, Haolan Xue, Yu Shang, Yuxiang Bao, Zoubin Bi, Jingming Luo, Jie Xiao, Chaojie Mao, Zhehan Kan, Hongchen Luo, Yu Liu, Sheng Zhong, Wei Tong, Xueyang Fu, Yang Cao, Wei Zhai, Zheng-Jun Zha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11736v1.pdf)  
  Keywords: benchmark, cinematic, evaluation, image to video, image-to-video, text to video, text-to-video, video generation  
- **[Generative Adversarial Loops](https://arxiv.org/abs/2610.11458v1)**  
  Authors: Kislay Aditya Oj, Nidhi Jain, Sri Surya Varma Datla, Priyanka Jayaswal, Kumar Krishna Agrawal, Aditya Desai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11458v1.pdf)  
  Keywords: benchmark, efficient, sparse attention, video generation  

### Text-to-Video Generation

*Showing the latest 50 out of 140 papers*

- **[Images Talk Back: Guiding MMDiTs by Suppressing Image-to-Text Feedback](https://arxiv.org/abs/2610.13941v1)**  
  Authors: Yucheng Yang, Xiaoxiao Sun, Shusheng Yang, Jiakang Chen, Serena Yeung-Levy  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13941v1.pdf) | [![GitHub](https://img.shields.io/github/stars/yyc1215lll-creator/SFG?style=social)](https://github.com/yyc1215lll-creator/SFG)  
  Keywords: image to video, image-to-video, text to video, text-to-video, video generation  
- **[TextVBench: Evaluating Text Rendering and Preservation in Video Generation](https://arxiv.org/abs/2610.13412v1)**  
  Authors: Ruiqiang Zhang, Hengyi Wang, Chang Liu, Guanjie Wang, Zehua Ma, Weiming Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13412v1.pdf)  
  Keywords: benchmark, evaluation, layout, t2v, video generation  
- **[PreCoG: Preview-Edit for Efficient Video Correction in Generation-Time](https://arxiv.org/abs/2610.13174v1)**  
  Authors: Yilai Liu, Wenqi Pei, Zhifeng Lu, Shiyuan Zhang, Zongxi Liu, Hongyang Du  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13174v1.pdf)  
  Keywords: efficient, t2v, text to video, text-to-video, trajectory, video generation  
- **[From Video Clips to Creation Trajectory: Sora100K for AI-Native Video Creation](https://arxiv.org/abs/2610.11770v1)**  
  Authors: Sicong Yang, Ruihuan Yang, Jian Lu, Jianfei Yuan, Xiaodong Cun, Xiuli Bi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11770v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://huggingface.co/datasets/ysicong/Sora100K.) | [![Dataset](https://img.shields.io/badge/-Dataset-orange)](https://huggingface.co/datasets/ysicong/Sora100K)  
  Keywords: evaluation, text to video, text-to-video, trajectory, video editing, video generation  
- **[Towards Unified Evaluation of Prompt Enhancers for Video Generation](https://arxiv.org/abs/2610.11736v1)**  
  Authors: Yawen Shao, Yubo Zhu, Ziyun Dai, Zixun Fang, Kai Zhu, Zeyinzi Jiang, Yufeng Ai, Siyang Sun, Haolan Xue, Yu Shang, Yuxiang Bao, Zoubin Bi, Jingming Luo, Jie Xiao, Chaojie Mao, Zhehan Kan, Hongchen Luo, Yu Liu, Sheng Zhong, Wei Tong, Xueyang Fu, Yang Cao, Wei Zhai, Zheng-Jun Zha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11736v1.pdf)  
  Keywords: benchmark, cinematic, evaluation, image to video, image-to-video, text to video, text-to-video, video generation  
- **[iCATS: Fast Video Generation via Interaction-Aware Sparse Attention and Timestep-Adaptive Sparsity](https://arxiv.org/abs/2610.11302v1)**  
  Authors: Chengfeng Han, Baole Ai, Xianlu Bian, Jie Yao, Zilong Huang, Ang Wang, Dandan Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11302v1.pdf)  
  Keywords: acceleration, denoising, efficient, sparse attention, t2v, video generation  
- **[TasteRoute: Personalized Routing for Video Generation](https://arxiv.org/abs/2610.05896v1)**  
  Authors: Zhi Rui Tam, Chao-Chung Wu, Sin-Han Yang, Peyton Ku, Brendan Kuang, Tzu-Ting Hsieh, Min-Fang Hsu, Fang-Ling Tsai, Yun-Nung Chen, Wei-Chiu Ma, Chieh-Yen Lin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.05896v1.pdf)  
  Keywords: image to video, image-to-video, text to video, text-to-video, video generation  
- **[Your Unlearning Gives You Away: Identifying Erased Concepts in Diffusion Models](https://arxiv.org/abs/2610.05601v1)**  
  Authors: Kaiyuan Deng, Yuchen Li, Yang Xiao, Bo Hui, Geng Yuan, Xiaolong Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.05601v1.pdf)  
  Keywords: efficient, text to video, text-to-video  
- **[FADE: Frame-Aware Diffusion-Transformer-based Multi-Concept Erasure for Video Unlearning](https://arxiv.org/abs/2610.03980v1)**  
  Authors: Yuchen Li, Kaiyuan Deng, Chaoran Feng, Zhenyu Tang, Li Yuan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.03980v1.pdf)  
  Keywords: benchmark, concept, denoising, diffusion transformer, t2v, text to video, text-to-video  
- **[VDOT++: Unified Few-Step Video Generation via Unbalanced Optimal Transport Distillation](https://arxiv.org/abs/2610.03221v1)**  
  Authors: Yutong Wang, Xingtong Ge, Enhuai Liu, Yunke Wang, Tianfan Xue, Yu Qiao, Yaohui Wang, Xinyuan Chen, Chang Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.03221v1.pdf)  
  Keywords: benchmark, distillation, i2v, image to video, image-to-video, t2v, text to video, text-to-video, video diffusion, video generation  

### Video Editing

*Showing the latest 50 out of 96 papers*

- **[AV-FlowEdit: Training-Free Prompt-Driven Audio-Visual Editing with Event-Aware Spectral Trajectory Preservation](https://arxiv.org/abs/2610.13072v1)**  
  Authors: Shaohua Pan, Xiao Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13072v1.pdf)  
  Keywords: joint audio-video, temporal consistency, trajectory, video diffusion, video editing  
- **[MotionCoach: Constructing Multimodal Guidance for Video Professional Motion Editing](https://arxiv.org/abs/2610.12963v1)**  
  Authors: Siyi Qian, Hanqing Yang, Weihuang Lin, Zihao Yang, Yichen Lu, Yuanhong Zheng, Sheng Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.12963v1.pdf)  
  Keywords: evaluation, motion editing, video editing  
- **[VINCIE-NExT: Unlocking Video Editing from Images via In-Context Modeling](https://arxiv.org/abs/2610.12104v1)**  
  Authors: Leigang Qu, Feng Cheng, Ziyan Yang, Bangbang Yang, Zhaoyang Huang, Wei Chow, Yicong Li, Wenjie Wang, Tat-Seng Chua, Yan Zeng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.12104v1.pdf)  
  Keywords: video editing  
- **[From Video Clips to Creation Trajectory: Sora100K for AI-Native Video Creation](https://arxiv.org/abs/2610.11770v1)**  
  Authors: Sicong Yang, Ruihuan Yang, Jian Lu, Jianfei Yuan, Xiaodong Cun, Xiuli Bi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11770v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://huggingface.co/datasets/ysicong/Sora100K.) | [![Dataset](https://img.shields.io/badge/-Dataset-orange)](https://huggingface.co/datasets/ysicong/Sora100K)  
  Keywords: evaluation, text to video, text-to-video, trajectory, video editing, video generation  
- **[Transforming Image Editors into Video Editors](https://arxiv.org/abs/2610.11037v1)**  
  Authors: Feng Wang, Zijie Li, Ceyuan Yang, Alan Yuille, Peng Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11037v1.pdf) | [![GitHub](https://img.shields.io/github/stars/wangf3014/AVE?style=social)](https://github.com/wangf3014/AVE)  
  Keywords: diffusion model, image to video, image-to-video, temporal consistency, video diffusion, video editing  
- **[SoccerNet-FoulRet: Retrieving Semantically Similar Soccer Foul Videos](https://arxiv.org/abs/2610.09742v1)**  
  Authors: Jacobus Arthur, Ahmad Sait, Batool Hani, Merey Ramazanova, Jan Held, Marc Van Droogenbroeck, Bernard Ghanem, Anthony Cioppa, Silvio Giancola  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.09742v1.pdf) | [![GitHub](https://img.shields.io/github/stars/SoccerNet/sn-foulret?style=social)](https://github.com/SoccerNet/sn-foulret)  
  Keywords: benchmark, video to video, video-to-video  
- **[ALIVE: Interaction-Aligned Object Insertion for First-Frame-Guided Video Editing](https://arxiv.org/abs/2610.08779v1)**  
  Authors: Zhenghong Zhou, Zhe Lin, Jiebo Luo, Yuqian Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.08779v1.pdf)  
  Keywords: benchmark, video editing  
- **[Robotizing Human Videos with Physically Consistent Interactions](https://arxiv.org/abs/2610.06137v1)**  
  Authors: Ching-Lam Cheng, Shengfeng He, Bin Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.06137v1.pdf)  
  Keywords: physical, video editing  
- **[SemCam: Semantic Camera Motion Control for Video Generation](https://arxiv.org/abs/2610.05141v1)**  
  Authors: Janna Bruner, Omer Talmi, Ianir Ideses, Lior Fritz, Lior Wolf, Sagie Benaim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.05141v1.pdf)  
  Keywords: benchmark, camera motion, identity, motion control, trajectory, video generation, video to video, video-to-video  
- **[Unsupervised Domain Adaptation for Enhanced Radiometer Image Precipitation Estimation using Conditional Flow Matching](https://arxiv.org/abs/2610.01890v1)**  
  Authors: Victor Enescu, Assaad Zeghina, Matthieu Meignin, Nicolas Viltard, Cécile Mallet  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.01890v1.pdf)  
  Keywords: flow matching, video editing  

### Video Inpainting & Completion

- **[ProAR: Learning Prospective Reasoning with Autoregressive Video Models](https://arxiv.org/abs/2610.03664v1)**  
  Authors: Linghui Shen, Tinghui Zhu, Sheng Zhang, Muhao Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.03664v1.pdf)  
  Keywords: autoregressive, autoregressive video, dynamics, efficient, embodied, frame prediction, video generation  
- **[Dexterous Tactile World Model](https://arxiv.org/abs/2609.34286v1)**  
  Authors: Ziyao Zeng, Xiatao Sun, Hao Wang, Yueyang Pan, Zhengxiang Yu, Fengyu Yang, Tianyu Liu, Zhiwen Fan, Daniel Rakita  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.34286v1.pdf)  
  Keywords: architecture, diffusion transformer, frame prediction, future frame prediction, video diffusion, video diffusion transformer, video world model, world model  
- **[WorldWeave: Growing Persistent Geometric Worlds for Video Generation](https://arxiv.org/abs/2609.34221v2)**  
  Authors: Yifan Huang, Lifan Jiang, Qingyue Hao, Cheng Chen, Boxi Wu, Xiaoxue Ren, Xiaofei He, Dehai Zhao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.34221v2.pdf)  
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

### Video Super-Resolution & Enhancement

*Showing the latest 50 out of 174 papers*

- **[PAGE: Parts-Aware Guidance for Co-Speech Gesture Portrait Video Generation](https://arxiv.org/abs/2610.13301v1)**  
  Authors: Yabiao Wang, Jiafu Wu, Yicheng Xu, Teng Hu, Shengzhe Zhou, Yanxiao Sun, Jiangning Zhang, Ying Tai, Yong Liu, Ming-Hsuan Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13301v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://aigc-explorer.github.io/PAGE)  
  Keywords: audio-driven, benchmark, body motion, denoising, efficient, evaluation, gesture, trajectory, video generation  
- **[High-Throughput Generative Video Super-Resolution on a Single Consumer GPU](https://arxiv.org/abs/2610.13179v1)**  
  Authors: Georgios Panaretou, Sotirios Chatzis  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13179v1.pdf)  
  Keywords: super-resolution, temporal consistency, upscaling  
- **[ForcingBooster: Adaptive Patch-wise Denoising for Fast Autoregressive Video Diffusion](https://arxiv.org/abs/2610.12625v1)**  
  Authors: Zekai Gu, Peng Wang, Jiahao Lu, Yongsen Mao, Cheng Lin, Yuan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.12625v1.pdf)  
  Keywords: autoregressive, autoregressive video, denoising, interactive, video diffusion, video generation  
- **[LEGO: A Lifting-Free Approach for Exocentric-to-Egocentric Video Generation](https://arxiv.org/abs/2610.12442v1)**  
  Authors: Suhwan Cho, Yonwoo Choi, Soongjin Kim, Jicheol Park, Taegyu Lim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.12442v1.pdf)  
  Keywords: denoising, diffusion model, layout, novel view, style, video diffusion, video generation  
- **[iCATS: Fast Video Generation via Interaction-Aware Sparse Attention and Timestep-Adaptive Sparsity](https://arxiv.org/abs/2610.11302v1)**  
  Authors: Chengfeng Han, Baole Ai, Xianlu Bian, Jie Yao, Zilong Huang, Ang Wang, Dandan Ding  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.11302v1.pdf)  
  Keywords: acceleration, denoising, efficient, sparse attention, t2v, video generation  
- **[Fluid-Gen-Zero: Grounding Pretrained Video Generators in Physics without Training](https://arxiv.org/abs/2610.10984v1)**  
  Authors: Hong Huang, Yuqiu Liu, Chenyu You, Daniel Martin, Chuhang Zou, Wuyang Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.10984v1.pdf)  
  Keywords: benchmark, denoising, dynamics, physical, physics, physics-aware, simulation, trajectory, video generation  
- **[GRACE: Generation-aware latent compression for efficient video generation](https://arxiv.org/abs/2610.10524v1)**  
  Authors: Jiyoung Kim, Paul Hyunbin Cho, Jisu Nam, Donghoon Lee, Hyunsung Go, Yeonkyeong Lee, Hansaem Kim, Seungryong Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.10524v1.pdf)  
  Keywords: denoising, diffusion transformer, dit, efficient, i2v, video autoencoder, video diffusion, video generation  
- **[MORCA: Offline-to-Online Reinforcement Learning for Adaptive Cache Reuse in Video Diffusion Acceleration](https://arxiv.org/abs/2610.10457v1)**  
  Authors: Yuxiang Xiong, Ruiyan Wang, Wenqiang Wang, Teng Hu, Songhang Shen, Bohao Feng, Hongqian Deng, Ran Yi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.10457v1.pdf) | [![GitHub](https://img.shields.io/github/stars/x10ngyx/MORCA?style=social)](https://github.com/x10ngyx/MORCA)  
  Keywords: acceleration, denoising, video diffusion, video generation, video synthesis  
- **[SGF+: Decoupling Gradient Flows for Autoregressive Video Generation](https://arxiv.org/abs/2610.10429v2)**  
  Authors: Zihan Su, Junhao Zhuang, Yaowei Li, Siwen Lu, Haoran Li, Lingen Li, Haoyu Wu, Weiyang Jin, Songchun Zhang, Haoyang Huang, Chun Yuan, Zeyue Xue, Nan Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.10429v2.pdf)  
  Keywords: autoregressive, autoregressive video, denoising, long video, temporal consistency, video generation  
- **[RobotAPO: Adversarial Physics Preference Optimization for Robotic Manipulation Video Generation](https://arxiv.org/abs/2610.09454v1)**  
  Authors: Kerui Li, Zhe Jing, Chenyi Huang, Xiaofeng Wang, Zheng Zhu, Haoming Cui, Huaibo Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.09454v1.pdf)  
  Keywords: denoising, embodied, flow matching, physical, physical consistency, physics, video generation  

### World Models & Simulation

*Showing the latest 50 out of 241 papers*

- **[GLIMPSE: Global-Local Indexing with Multi-Precision Spectral Encoding for Explorable Video World Models](https://arxiv.org/abs/2610.13706v1)**  
  Authors: Zhufeng Xu, Henglei Lv, Bailin Deng, Yikang Ding, Xiaoqiang Liu, Guoxin Zhang, Hongbo Fu, Lin Gao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13706v1.pdf)  
  Keywords: video world model, world model  
- **[PhysForge: Material-Controllable 3D Reconstruction with Separable Components](https://arxiv.org/abs/2610.13681v1)**  
  Authors: Yuchen Wang, Yanqi Bao, Zheng Gu, Zhengqing Chen, Jieqi Shi, Jing Huo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13681v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://masterwanna.github.io/PhysForge.html)  
  Keywords: controllable, diffusion model, dynamics, physical, simulation, video diffusion  
- **[Beyond Successful Robot Demonstrations: Learning from Human Interactions and Modeling Failure Dynamics](https://arxiv.org/abs/2610.13522v1)**  
  Authors: Peiyan Tu, Cong Wang, Hanxin Zhu, Xin Jin, Zhibo Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13522v1.pdf)  
  Keywords: action-conditioned, camera motion, dynamics, evaluation, physical, physical plausibility, video generation, world model  
- **[Golden Anchor for Video Generation](https://arxiv.org/abs/2610.13217v1)**  
  Authors: Jinyuan Xu, Shitong Shao, Lichen Bai, Zikai Zhou, Guoxi Huang, Nantheera Anantrasirichai, Zeke Xie  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13217v1.pdf)  
  Keywords: game, i2v, identity, image to video, image-to-video, interactive, style, video generation  
- **[Grounded-Dreamer: Robot Learning from World Model Synthetic Data with Physical Grounding](https://arxiv.org/abs/2610.13164v1)**  
  Authors: Feng Jiang, Shu Chen, Yuanfei Wang, Yuan Li, Zhenhao Shen, Jiaqi Liang, Yang Chen, Lei Wei, Chen Xie, Ruihai Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.13164v1.pdf)  
  Keywords: dynamics, physical, physics, robot learning, simulation, video world model, world model  
- **[StereoEngine: Scaling Stereo Bimanual Robot Data without Stereo Cameras](https://arxiv.org/abs/2610.12734v1)**  
  Authors: Jason Chen, I-Chun Arthur Liu, Gaurav Sukhatme, Daniel Seita  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.12734v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://stereoengine.github.io)  
  Keywords: autonomous driving, diffusion model, driving, simulation, video diffusion  
- **[ForcingBooster: Adaptive Patch-wise Denoising for Fast Autoregressive Video Diffusion](https://arxiv.org/abs/2610.12625v1)**  
  Authors: Zekai Gu, Peng Wang, Jiahao Lu, Yongsen Mao, Cheng Lin, Yuan Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.12625v1.pdf)  
  Keywords: autoregressive, autoregressive video, denoising, interactive, video diffusion, video generation  
- **[WorldGuide: Goal-Directed Video World Model for Procedural Task Execution](https://arxiv.org/abs/2610.12459v1)**  
  Authors: Ankan Deria, Komal Kumar, Hisham Cholakkal, Fahad Shahbaz Khan, Salman Khan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.12459v1.pdf)  
  Keywords: video generation, video world model, world model  
- **[WOVEN: Weaving Visual World Modeling into Multimodal LLMs](https://arxiv.org/abs/2610.12417v1)**  
  Authors: Zheyu Fan, Yue Zhang, Mingkai Deng, Kangrui Wang, Qineng Wang, Canyu Chen, Jie Hao, Xing Fan, Chenlei Guo, Eric P. Xing, Mohit Bansal, Manling Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.12417v1.pdf)  
  Keywords: benchmark, embodied, physical, visual world model, world model  
- **[WorldAlign: Decoupled 4D Reward for World-Consistent Video Generation](https://arxiv.org/abs/2610.12382v1)**  
  Authors: Jing He, Kaixin Ding, Xingye Tian, Guibao Shen, Wenhang Ge, Xin Tao, Pengfei Wan, Ying-Cong Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.12382v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://worldalign.github.io)  
  Keywords: camera motion, evaluation, image to video, image-to-video, physical, physical plausibility, simulation, video generation, world simulation  



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
