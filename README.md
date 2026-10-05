# Awesome Video Diffusions [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Video Diffusion Models and Video Generation. Content is automatically updated daily.

🗺️ **[Explore the Paper Atlas](https://longxiang-ai.github.io/awesome-video-diffusions/)**: an interactive paper map, monthly trends, topic network, co-author network and author rankings of every tracked paper.

> Last Update: 2026-10-05 04:22:28

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

- [3D-aware Video Generation](#3d-aware-video-generation) (52 papers) - Video generation with 3D awareness, multi-view consistency, and 4D content creation
- [Applications](#applications) (204 papers) - Domain-specific applications of video diffusion models
- [Architecture & Efficiency](#architecture-&-efficiency) (392 papers) - Architectural innovations (DiT, UNet), flow matching, and training/inference efficiency
- [Audio & Multi-modal](#audio-&-multi-modal) (68 papers) - Audio-driven and multi-modal conditioned video generation
- [Controllable Generation](#controllable-generation) (328 papers) - Controllable video generation with motion, camera, pose, or layout guidance
- [Human & Character Animation](#human-&-character-animation) (60 papers) - Human-centric video generation including talking heads, dance, and character animation
- [Image-to-Video Generation](#image-to-video-generation) (93 papers) - Methods for animating still images into videos
- [Long Video Generation](#long-video-generation) (255 papers) - Generating temporally consistent long-form videos beyond short clips
- [Personalization & Customization](#personalization-&-customization) (164 papers) - Personalized video generation with custom subjects, identities, or styles
- [Physical Understanding](#physical-understanding) (310 papers) - Physics-aware video generation and dynamics modeling
- [Surveys & Benchmarks](#surveys-&-benchmarks) (313 papers) - Survey papers, benchmarks, and evaluation metrics for video generation
- [Text-to-Video Generation](#text-to-video-generation) (149 papers) - Foundation models and methods for generating videos from text prompts
- [Video Editing](#video-editing) (93 papers) - Diffusion-based video editing, style transfer, and manipulation
- [Video Inpainting & Completion](#video-inpainting-&-completion) (24 papers) - Video inpainting, completion, outpainting, and temporal prediction
- [Video Super-Resolution & Enhancement](#video-super-resolution-&-enhancement) (171 papers) - Video quality improvement, upscaling, restoration, and frame interpolation
- [World Models & Simulation](#world-models-&-simulation) (241 papers) - Video generation as world simulators and interactive environment generation



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3D-aware Video Generation

*Showing the latest 50 out of 52 papers*

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
- **[AlayaVista: Streaming World Modeling from Panoramic States to Perspective Video](https://arxiv.org/abs/2609.14462v1)**  
  Authors: Jiaming Tan, Mingliang Zhai, Zhen Li, Yuwei Wu, Chuanhao Li, Kaipeng Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.14462v1.pdf)  
  Keywords: autoregressive, camera motion, camera-conditioned, controllable, efficient, interactive, streaming, super-resolution, video world model, world model  

### Applications

*Showing the latest 50 out of 204 papers*

- **[ProAR: Learning Prospective Reasoning with Autoregressive Video Models](https://arxiv.org/abs/2610.03664v1)**  
  Authors: Linghui Shen, Tinghui Zhu, Sheng Zhang, Muhao Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.03664v1.pdf)  
  Keywords: autoregressive, autoregressive video, dynamics, efficient, embodied, frame prediction, video generation  
- **[SymRegFlow: Symmetry-Regularized Flow Matching for Video World Models](https://arxiv.org/abs/2610.02726v1)**  
  Authors: Xi Ye, Yuzhu Wang, Xiaoyang Liu, Jiayi Wang, Yangyang Xu, Ruyu Wang, Wenlin Chen, Duo Su, Jun Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.02726v1.pdf)  
  Keywords: autonomous driving, denoising, driving, flow matching, novel view, video generation, view-consistent  
- **[Spatial Memory Intelligence: Endowing World Models with Understanding-Driven Long-Term Memory](https://arxiv.org/abs/2610.02521v1)**  
  Authors: Ying Yang, Guiyu Zhang, Lianghua Huang, Chang Nie, Chenyang Si, Haofan Wang, Shaoshuai Shi, Li Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.02521v1.pdf)  
  Keywords: embodied, interactive, long video, simulation, video generation, world model  
- **[UniWAM: Unified World-Action Model](https://arxiv.org/abs/2610.02054v1)**  
  Authors: Jiayi Chen, Wenxuan Song, Jingbo Wang, Shuai Zhou, Xicheng Gong, Zehua Fan, Ziyang Zhou, Junwu E, Haodong Yan, Fuhao Li, Qize Yu, Xu Huang, Pengwei Wang, Wen Chen, Shunbo Zhou, Haoang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.02054v1.pdf)  
  Keywords: architecture, denoising, dynamics, embodied, flow matching, physical, video generation  
- **[DiVid: Diagnosing Dimension-Specific Diversity Collapse in Video Generation Models](https://arxiv.org/abs/2610.01661v1)**  
  Authors: Huanran Hu, Zihui Ren, Dingyi Yang, Zhinan Song, Guozheng Wu, Tiezheng Ge, Qin Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.01661v1.pdf)  
  Keywords: controllable, creative, evaluation, style, video generation  
- **[VTR-Bench: A Systematic Benchmark for Evaluating Visual Text Rendering in Video Generation](https://arxiv.org/abs/2610.01499v1)**  
  Authors: Yu Huang, Jungang Li, Zhiyuan Wang, Yonghua Hei, Song Dai, Jiayu Yang, Deyuan Liu, Xiang Zheng, Xiaoshuang Shi, Hao Cheng, Kaidi Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.01499v1.pdf) | [![GitHub](https://img.shields.io/github/stars/hardenyu21/VTR-Bench?style=social)](https://github.com/hardenyu21/VTR-Bench)  
  Keywords: benchmark, cinematic, evaluation, keyframe, physical, physical plausibility, video generation  
- **[PhysicsLENS: Diagnosing Physical Property Blindness in Video Generation Models](https://arxiv.org/abs/2610.01162v1)**  
  Authors: Isaiah Milkey, Som Sagar, Aditya Taparia, Xinyuan Liu, Jiqing Wen, Ransalu Senanayake  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.01162v1.pdf)  
  Keywords: benchmark, evaluation, physical, physics, robot learning, robotics, video generation  
- **[Ego2Act: Evaluating Goal-Directed Manipulation in Egocentric Video Generation](https://arxiv.org/abs/2610.01092v1)**  
  Authors: Patrick Amadeus Irawan, Iskandar Muda Rizky Parlambang, Rava Maulana, Qinrong Cui, Erland Hilman Fuadi, Zayd M. K. Zuhri, Nanda Ryaas Absar, Ahmed Elshabrawy, Wilfried Ariel Mulyawan, Shoubin Yu, Yue Zhang, Mohit Bansal, Alham Fikri Aji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.01092v1.pdf)  
  Keywords: benchmark, dynamics, embodied, evaluation, physical, physics, simulation, video generation  
- **[Towards Subject Consistency over Dynamic Subject Sets in Video Generation](https://arxiv.org/abs/2610.01052v1)**  
  Authors: Tongcheng Zhang, Jun Zhu, Jianfei Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.01052v1.pdf)  
  Keywords: autonomous driving, driving, evaluation, i2v, identity, video generation  
- **[Dream4ACT: A Shared Visual Action Interface for Multi-Embodiment Video-Action Modeling](https://arxiv.org/abs/2609.40153v1)**  
  Authors: Xiangyu Zhu, Jin Xu, Yue Guo, Xin Wu, Yifan Sun, Xiancong Ren, Jianxin Sun, Yong Dai, Xiaozhu Ju  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.40153v1.pdf)  
  Keywords: action-conditioned, diffusion transformer, dynamics, embodied, flow matching, video autoencoder, video generation, world model  

### Architecture & Efficiency

*Showing the latest 50 out of 392 papers*

- **[ProAR: Learning Prospective Reasoning with Autoregressive Video Models](https://arxiv.org/abs/2610.03664v1)**  
  Authors: Linghui Shen, Tinghui Zhu, Sheng Zhang, Muhao Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.03664v1.pdf)  
  Keywords: autoregressive, autoregressive video, dynamics, efficient, embodied, frame prediction, video generation  
- **[DuoMatching: Joint-Marginal Distribution Matching for Few-Step Video Generation](https://arxiv.org/abs/2610.03543v1)**  
  Authors: Jiahao Zhan, Yan Wang, Yongrui Ma, Qunliang Xing, Ruchang Yao, Runtao Liu, Shijie Zhao, Tianfan Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.03543v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://johnzhan2023.github.io/DuoMatching)  
  Keywords: autoregressive, distillation, dynamics, streaming, streaming video generation, video generation  
- **[XGenAct: Geometry-Enhanced World Action Models through Cross-Task Generation](https://arxiv.org/abs/2610.03516v1)**  
  Authors: Tingting Du, Ziyao Wang, Guoheng Sun, Ang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.03516v1.pdf)  
  Keywords: architecture, diffusion transformer, video diffusion, video diffusion transformer  
- **[Native Action-Prior Learning from Videos for World Action Models](https://arxiv.org/abs/2610.03391v1)**  
  Authors: Zhaochong An, Fei Zhang, Menglin Jia, Duncan Frost, Zijian Zhou, Yikai Wang, Xudong Wang, Aditya Patel, Belinda Zeng, Tao Xiang, Serge Belongie, Amir Bar, Sen He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.03391v1.pdf)  
  Keywords: denoising, dit, dynamics, efficient, flow matching, video flow matching  
- **[VDOT++: Unified Few-Step Video Generation via Unbalanced Optimal Transport Distillation](https://arxiv.org/abs/2610.03221v1)**  
  Authors: Yutong Wang, Xingtong Ge, Enhuai Liu, Yunke Wang, Tianfan Xue, Yu Qiao, Yaohui Wang, Xinyuan Chen, Chang Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.03221v1.pdf)  
  Keywords: benchmark, distillation, i2v, image to video, image-to-video, t2v, text to video, text-to-video, video diffusion, video generation  
- **[Contextual Flow Matching: Adaptive Step Selection in Flow Models for Efficient Visual Generation](https://arxiv.org/abs/2610.03202v1)**  
  Authors: Divya Jyoti Bajpai, Arun Verma, Manjesh Kumar Hanawal  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.03202v1.pdf)  
  Keywords: acceleration, dynamics, efficient, flow matching, video generation  
- **[Parasitic Co-Denoising: Unlocking 3D Human Motion Generation in a Frozen Video Diffusion Model](https://arxiv.org/abs/2610.03047v1)**  
  Authors: Yunjiao Zhou, Junlang Qian, Lihua Xie, Jianfei Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.03047v1.pdf)  
  Keywords: denoising, diffusion model, efficient, flow matching, human motion, text to video, text-to-video, video diffusion  
- **[TRAC: Trajectory-aware Reuse and Adaptive Correction for Efficient Autoregressive Video Generation](https://arxiv.org/abs/2610.02779v1)**  
  Authors: Jiaxing Song, Weiqi Yan, You Huang, Mingte Qiu, Huazhong Liu, Xiaofeng Zhu, Yunshan Zhong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.02779v1.pdf)  
  Keywords: acceleration, autoregressive, autoregressive video, denoising, efficient, trajectory, video generation  
- **[SymRegFlow: Symmetry-Regularized Flow Matching for Video World Models](https://arxiv.org/abs/2610.02726v1)**  
  Authors: Xi Ye, Yuzhu Wang, Xiaoyang Liu, Jiayi Wang, Yangyang Xu, Ruyu Wang, Wenlin Chen, Duo Su, Jun Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.02726v1.pdf)  
  Keywords: autonomous driving, denoising, driving, flow matching, novel view, video generation, view-consistent  
- **[Imagine the Future, Internalize the Gist: Efficient VLA Reasoning via Internalized Spatiotemporal Imagination](https://arxiv.org/abs/2610.02626v1)**  
  Authors: Shenglan Li, Zhendong Mi, Hengyi Zhu, Jingwu Luo, Chun Kit Chan, Geng Yuan, Yanzhi Wang, Pu Zhao, Shaoyi Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.02626v1.pdf)  
  Keywords: efficient, video generation  

### Audio & Multi-modal

*Showing the latest 50 out of 68 papers*

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

### Controllable Generation

*Showing the latest 50 out of 328 papers*

- **[LoGo: Local-Global Rewards for Consistent Long-Horizon Video Generation](https://arxiv.org/abs/2610.03636v1)**  
  Authors: Ziqi Ma, Shreya Sharma, Mohamed El Banani, Katja Schwarz, Chongjie Ye, Chao-Yuan Wu, Li Fei-Fei, Ben Mildenhall, Georgia Gkioxari, Justin Johnson, Gowthami Somepalli  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.03636v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ziqi-ma.github.io/logo-website)  
  Keywords: benchmark, camera control, video generation  
- **[TRAC: Trajectory-aware Reuse and Adaptive Correction for Efficient Autoregressive Video Generation](https://arxiv.org/abs/2610.02779v1)**  
  Authors: Jiaxing Song, Weiqi Yan, You Huang, Mingte Qiu, Huazhong Liu, Xiaofeng Zhu, Yunshan Zhong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.02779v1.pdf)  
  Keywords: acceleration, autoregressive, autoregressive video, denoising, efficient, trajectory, video generation  
- **[A Simulation-Grounded Agentic VLM Framework for Wildfire Monitoring and Reporting](https://arxiv.org/abs/2610.02451v1)**  
  Authors: Duowen Chen, Yuchen Sun, Zhiqi Li, Yuxuan Liao, Sinan Wang, Bart van Bloemen Waanders, Bo Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.02451v1.pdf)  
  Keywords: controllable, dynamics, layout, physical, simulation, video generation  
- **[Generative Cinematographer: Composing Camera and Object Motion in 3D](https://arxiv.org/abs/2610.02180v1)**  
  Authors: Jiahan Zhang, Chaohao Yang, Namitha Guruprasad, Vivekjyoti Banerjee, Trong-Tung Nguyen, Alan Yuille, Anand Bhattad  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.02180v1.pdf)  
  Keywords: controllable, physics, trajectory, video generation  
- **[DiVid: Diagnosing Dimension-Specific Diversity Collapse in Video Generation Models](https://arxiv.org/abs/2610.01661v1)**  
  Authors: Huanran Hu, Zihui Ren, Dingyi Yang, Zhinan Song, Guozheng Wu, Tiezheng Ge, Qin Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.01661v1.pdf)  
  Keywords: controllable, creative, evaluation, style, video generation  
- **[Oneira: From Open-Ended Generation to Open-World Interaction in Video World Models](https://arxiv.org/abs/2610.01614v1)**  
  Authors: Xindi Yang, Baolu Li, Liam Lee, Zhenfei Yin, Songxin Zhang, Zhuoyang Song, Xu Jia, Jianfei Cai, Tien-Tsin Wong, Bingyi Jing, Mengyue Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.01614v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://madaoer.github.io/projects/oneira)  
  Keywords: interactive, trajectory, video world model, world model  
- **[VTR-Bench: A Systematic Benchmark for Evaluating Visual Text Rendering in Video Generation](https://arxiv.org/abs/2610.01499v1)**  
  Authors: Yu Huang, Jungang Li, Zhiyuan Wang, Yonghua Hei, Song Dai, Jiayu Yang, Deyuan Liu, Xiang Zheng, Xiaoshuang Shi, Hao Cheng, Kaidi Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.01499v1.pdf) | [![GitHub](https://img.shields.io/github/stars/hardenyu21/VTR-Bench?style=social)](https://github.com/hardenyu21/VTR-Bench)  
  Keywords: benchmark, cinematic, evaluation, keyframe, physical, physical plausibility, video generation  
- **[Video Generation Models: A Survey of Post-Training and Alignment](https://arxiv.org/abs/2610.00812v1)**  
  Authors: Chaoyu Li, Xiaoyi Gu, Yogesh Kulkarni, Eun Woo Im, Mohammadmahdi Honarmand, Zeyu Wang, Juntong Song, Fei Du, Xilin Jiang, Kexin Zheng, Tianzhi Li, Fei Tao, Pooyan Fazli  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.00812v1.pdf)  
  Keywords: controllable, distillation, dynamics, evaluation, physical, survey, temporal consistency, video generation  
- **[Soundwich: Video Generation with Layered and Controllable Audio](https://arxiv.org/abs/2610.00691v2)**  
  Authors: Zhuo Ning, AmirHossein Naghi Razlighi, Sagi Polaczek, Daniel Cohen-Or, Ali Mahdavi-Amiri  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.00691v2.pdf) | [![GitHub](https://img.shields.io/github/stars/CodyNing/Soundwich?style=social)](https://github.com/CodyNing/Soundwich)  
  Keywords: controllable, flow matching, joint audio-video, sound, video flow matching, video generation  
- **[ViTeX-Bench: Benchmarking High-Fidelity Video Scene Text Editing](https://arxiv.org/abs/2609.40356v1)**  
  Authors: Xinghao Chen, Xiangbo Gao, Jiongze Yu, Yuheng Wu, Zhengzhong Tu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.40356v1.pdf)  
  Keywords: benchmark, controllable, dynamics, evaluation, human evaluation, temporal consistency, video editing, video generation  

### Human & Character Animation

*Showing the latest 50 out of 60 papers*

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

### Image-to-Video Generation

*Showing the latest 50 out of 93 papers*

- **[VDOT++: Unified Few-Step Video Generation via Unbalanced Optimal Transport Distillation](https://arxiv.org/abs/2610.03221v1)**  
  Authors: Yutong Wang, Xingtong Ge, Enhuai Liu, Yunke Wang, Tianfan Xue, Yu Qiao, Yaohui Wang, Xinyuan Chen, Chang Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.03221v1.pdf)  
  Keywords: benchmark, distillation, i2v, image to video, image-to-video, t2v, text to video, text-to-video, video diffusion, video generation  
- **[Custom Forcing: Training-Free Subject Customization for Autoregressive Video Generation](https://arxiv.org/abs/2610.02914v1)**  
  Authors: Yunseung Ok, Hyunsoo Kim, Minseo Kim, Suhyun Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.02914v1.pdf)  
  Keywords: autoregressive, autoregressive video, customization, identity, image to video, image-to-video, long video, minute-long, streaming, subject customization, video generation  
- **[MosaiChunk: Compositing Spatio-Temporal Memory for Autoregressive Video Generation](https://arxiv.org/abs/2610.02153v1)**  
  Authors: Yiwen Zhang, Haocheng Xi, Michael Tian-Yue Liu, Alexei A. Efros, Hadar Averbuch-Elor, Qianqian Wang, Haiwen Feng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.02153v1.pdf)  
  Keywords: autoregressive, autoregressive video, benchmark, i2v, image to video, image-to-video, t2v, text to video, text-to-video, video generation  
- **[PickMoment: Continuous-Time Single-Image-to-Video via Learning Deblurring and Blur-to-Video](https://arxiv.org/abs/2610.01279v1)**  
  Authors: Junseong Shin, Hyeonsu Jo, Daehyun Kim, Tae Hyun Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.01279v1.pdf)  
  Keywords: image to video, image-to-video, physical, video generation  
- **[Towards Subject Consistency over Dynamic Subject Sets in Video Generation](https://arxiv.org/abs/2610.01052v1)**  
  Authors: Tongcheng Zhang, Jun Zhu, Jianfei Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.01052v1.pdf)  
  Keywords: autonomous driving, driving, evaluation, i2v, identity, video generation  
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

### Long Video Generation

*Showing the latest 50 out of 255 papers*

- **[ProAR: Learning Prospective Reasoning with Autoregressive Video Models](https://arxiv.org/abs/2610.03664v1)**  
  Authors: Linghui Shen, Tinghui Zhu, Sheng Zhang, Muhao Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.03664v1.pdf)  
  Keywords: autoregressive, autoregressive video, dynamics, efficient, embodied, frame prediction, video generation  
- **[DuoMatching: Joint-Marginal Distribution Matching for Few-Step Video Generation](https://arxiv.org/abs/2610.03543v1)**  
  Authors: Jiahao Zhan, Yan Wang, Yongrui Ma, Qunliang Xing, Ruchang Yao, Runtao Liu, Shijie Zhao, Tianfan Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.03543v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://johnzhan2023.github.io/DuoMatching)  
  Keywords: autoregressive, distillation, dynamics, streaming, streaming video generation, video generation  
- **[Weave Forcing: Compositional Memory Routing for Interactive Long Video Generation](https://arxiv.org/abs/2610.03510v1)**  
  Authors: Ziyi Wang, Junchi Yao, Heqian Qiu, Wenbo Shi, Chengjiu Wang, Jinyang He, Binkai Hong, Hongliang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.03510v1.pdf)  
  Keywords: autoregressive, autoregressive video, interactive, long video, temporal consistency, video generation  
- **[In-Distribution Forcing for Long Video Generation at Test Time](https://arxiv.org/abs/2610.03120v1)**  
  Authors: Jeongwoo Shin, Youngyoon Choi, Sangwoo Jo, Hyunmog Kim, Sungjoon Choi, Joonseok Lee, Jaewoong Choi, Jaemoo Choi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.03120v1.pdf)  
  Keywords: autoregressive, benchmark, dynamics, long video, video diffusion, video generation  
- **[Custom Forcing: Training-Free Subject Customization for Autoregressive Video Generation](https://arxiv.org/abs/2610.02914v1)**  
  Authors: Yunseung Ok, Hyunsoo Kim, Minseo Kim, Suhyun Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.02914v1.pdf)  
  Keywords: autoregressive, autoregressive video, customization, identity, image to video, image-to-video, long video, minute-long, streaming, subject customization, video generation  
- **[TRAC: Trajectory-aware Reuse and Adaptive Correction for Efficient Autoregressive Video Generation](https://arxiv.org/abs/2610.02779v1)**  
  Authors: Jiaxing Song, Weiqi Yan, You Huang, Mingte Qiu, Huazhong Liu, Xiaofeng Zhu, Yunshan Zhong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.02779v1.pdf)  
  Keywords: acceleration, autoregressive, autoregressive video, denoising, efficient, trajectory, video generation  
- **[Spatial Memory Intelligence: Endowing World Models with Understanding-Driven Long-Term Memory](https://arxiv.org/abs/2610.02521v1)**  
  Authors: Ying Yang, Guiyu Zhang, Lianghua Huang, Chang Nie, Chenyang Si, Haofan Wang, Shaoshuai Shi, Li Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.02521v1.pdf)  
  Keywords: embodied, interactive, long video, simulation, video generation, world model  
- **[MosaiChunk: Compositing Spatio-Temporal Memory for Autoregressive Video Generation](https://arxiv.org/abs/2610.02153v1)**  
  Authors: Yiwen Zhang, Haocheng Xi, Michael Tian-Yue Liu, Alexei A. Efros, Hadar Averbuch-Elor, Qianqian Wang, Haiwen Feng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.02153v1.pdf)  
  Keywords: autoregressive, autoregressive video, benchmark, i2v, image to video, image-to-video, t2v, text to video, text-to-video, video generation  
- **[Video Generation Models: A Survey of Post-Training and Alignment](https://arxiv.org/abs/2610.00812v1)**  
  Authors: Chaoyu Li, Xiaoyi Gu, Yogesh Kulkarni, Eun Woo Im, Mohammadmahdi Honarmand, Zeyu Wang, Juntong Song, Fei Du, Xilin Jiang, Kexin Zheng, Tianzhi Li, Fei Tao, Pooyan Fazli  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.00812v1.pdf)  
  Keywords: controllable, distillation, dynamics, evaluation, physical, survey, temporal consistency, video generation  
- **[SemanTok: Predictable Semantic Tokens for Efficient Autoregressive Video Generation](https://arxiv.org/abs/2610.00686v1)**  
  Authors: Mikhail Dereviannykh, Vikram Voleti, Simon Donne, Mallikarjun Byrasandra Ramalinga Reddy, Shimon Vainer, Mark Boss  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.00686v1.pdf)  
  Keywords: autoregressive, autoregressive video, efficient, video generation, video tokenizer  

### Personalization & Customization

*Showing the latest 50 out of 164 papers*

- **[Custom Forcing: Training-Free Subject Customization for Autoregressive Video Generation](https://arxiv.org/abs/2610.02914v1)**  
  Authors: Yunseung Ok, Hyunsoo Kim, Minseo Kim, Suhyun Kim  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.02914v1.pdf)  
  Keywords: autoregressive, autoregressive video, customization, identity, image to video, image-to-video, long video, minute-long, streaming, subject customization, video generation  
- **[DMAD: Distribution Matching as Adversarial Distillation for Fast Visual Generation](https://arxiv.org/abs/2610.02188v1)**  
  Authors: Zhengming Yu, Junkun Yuan, Haotian Yang, Gordon Guocheng Qian, Yizhi Wang, Angtian Wang, Yiding Yang, Bo Liu, Xin Li, Wenping Wang, Chongyang Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.02188v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yzmblog.github.io/projects/DMAD)  
  Keywords: audio-video generation, diffusion model, distillation, identity, joint audio-video, t2v, video generation  
- **[4Director: Controlling Video World Models with Rigid 3D Geometry](https://arxiv.org/abs/2610.02160v1)**  
  Authors: Wei Cao, Hao Zhang, Vikram Voleti, Yuqun Wu, Mallikarjun B R, Shimon Vainer, Mark Boss, Yaoyao Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.02160v1.pdf)  
  Keywords: dynamics, identity, video world model, view-consistent, world model  
- **[Memory-Guided B-Roll Generation from User Video Collections](https://arxiv.org/abs/2610.01884v1)**  
  Authors: Cusuh Ham, Fabian Caba Heilbron, Josef Sivic, Bryan Russell  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.01884v1.pdf)  
  Keywords: identity, style, text to video, text-to-video  
- **[DiVid: Diagnosing Dimension-Specific Diversity Collapse in Video Generation Models](https://arxiv.org/abs/2610.01661v1)**  
  Authors: Huanran Hu, Zihui Ren, Dingyi Yang, Zhinan Song, Guozheng Wu, Tiezheng Ge, Qin Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.01661v1.pdf)  
  Keywords: controllable, creative, evaluation, style, video generation  
- **[Towards Subject Consistency over Dynamic Subject Sets in Video Generation](https://arxiv.org/abs/2610.01052v1)**  
  Authors: Tongcheng Zhang, Jun Zhu, Jianfei Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.01052v1.pdf)  
  Keywords: autonomous driving, driving, evaluation, i2v, identity, video generation  
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

### Physical Understanding

*Showing the latest 50 out of 310 papers*

- **[ProAR: Learning Prospective Reasoning with Autoregressive Video Models](https://arxiv.org/abs/2610.03664v1)**  
  Authors: Linghui Shen, Tinghui Zhu, Sheng Zhang, Muhao Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.03664v1.pdf)  
  Keywords: autoregressive, autoregressive video, dynamics, efficient, embodied, frame prediction, video generation  
- **[World Embedding Benchmark](https://arxiv.org/abs/2610.03632v1)**  
  Authors: Yiqi Liu, Ruifeng Yuan, Yang Wang, Long Li, Fengyu Cai, Hou Pong Chan, Jialin Yu, Hao Zhang, Chenghua Lin, Chenghao Xiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.03632v1.pdf)  
  Keywords: benchmark, dynamics, physical, physics, simulation, video generation  
- **[DuoMatching: Joint-Marginal Distribution Matching for Few-Step Video Generation](https://arxiv.org/abs/2610.03543v1)**  
  Authors: Jiahao Zhan, Yan Wang, Yongrui Ma, Qunliang Xing, Ruchang Yao, Runtao Liu, Shijie Zhao, Tianfan Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.03543v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://johnzhan2023.github.io/DuoMatching)  
  Keywords: autoregressive, distillation, dynamics, streaming, streaming video generation, video generation  
- **[Native Action-Prior Learning from Videos for World Action Models](https://arxiv.org/abs/2610.03391v1)**  
  Authors: Zhaochong An, Fei Zhang, Menglin Jia, Duncan Frost, Zijian Zhou, Yikai Wang, Xudong Wang, Aditya Patel, Belinda Zeng, Tao Xiang, Serge Belongie, Amir Bar, Sen He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.03391v1.pdf)  
  Keywords: denoising, dit, dynamics, efficient, flow matching, video flow matching  
- **[Contextual Flow Matching: Adaptive Step Selection in Flow Models for Efficient Visual Generation](https://arxiv.org/abs/2610.03202v1)**  
  Authors: Divya Jyoti Bajpai, Arun Verma, Manjesh Kumar Hanawal  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.03202v1.pdf)  
  Keywords: acceleration, dynamics, efficient, flow matching, video generation  
- **[Does Physics Live in the Activations? Localizing Physical Quantities in Video Diffusion Models](https://arxiv.org/abs/2610.03154v1)**  
  Authors: Jonas Kneifl, Jakub Skalski, Bartłomiej Twardowski, Kamil Deja  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.03154v1.pdf)  
  Keywords: denoising, dynamics, physical, physics, video diffusion, video generation  
- **[In-Distribution Forcing for Long Video Generation at Test Time](https://arxiv.org/abs/2610.03120v1)**  
  Authors: Jeongwoo Shin, Youngyoon Choi, Sangwoo Jo, Hyunmog Kim, Sungjoon Choi, Joonseok Lee, Jaewoong Choi, Jaemoo Choi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.03120v1.pdf)  
  Keywords: autoregressive, benchmark, dynamics, long video, video diffusion, video generation  
- **[World Action Modeling with Progressive Visual Planning](https://arxiv.org/abs/2610.02508v1)**  
  Authors: Fei Zhang, Zhaochong An, Duncan Frost, Yikai Wang, Pengfei Liu, Ya Zhang, Michal Drozdzal, Amir Bar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.02508v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://sii-ferenas.github.io/ProWAM-page)  
  Keywords: denoising, dynamics, efficient, simulation, video generation  
- **[A Simulation-Grounded Agentic VLM Framework for Wildfire Monitoring and Reporting](https://arxiv.org/abs/2610.02451v1)**  
  Authors: Duowen Chen, Yuchen Sun, Zhiqi Li, Yuxuan Liao, Sinan Wang, Bart van Bloemen Waanders, Bo Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.02451v1.pdf)  
  Keywords: controllable, dynamics, layout, physical, simulation, video generation  
- **[HiPhy: Hierarchical Alignment for Physically-Plausible Multi-Principle Video Generation](https://arxiv.org/abs/2610.02197v1)**  
  Authors: Tahira Kazimi, Shubhankar Borse, Munawar Hayat, Fatih Porikli, Pinar Yanardag  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.02197v1.pdf)  
  Keywords: benchmark, dynamics, physical, physics, video generation  

### Surveys & Benchmarks

*Showing the latest 50 out of 313 papers*

- **[LoGo: Local-Global Rewards for Consistent Long-Horizon Video Generation](https://arxiv.org/abs/2610.03636v1)**  
  Authors: Ziqi Ma, Shreya Sharma, Mohamed El Banani, Katja Schwarz, Chongjie Ye, Chao-Yuan Wu, Li Fei-Fei, Ben Mildenhall, Georgia Gkioxari, Justin Johnson, Gowthami Somepalli  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.03636v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://ziqi-ma.github.io/logo-website)  
  Keywords: benchmark, camera control, video generation  
- **[World Embedding Benchmark](https://arxiv.org/abs/2610.03632v1)**  
  Authors: Yiqi Liu, Ruifeng Yuan, Yang Wang, Long Li, Fengyu Cai, Hou Pong Chan, Jialin Yu, Hao Zhang, Chenghua Lin, Chenghao Xiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.03632v1.pdf)  
  Keywords: benchmark, dynamics, physical, physics, simulation, video generation  
- **[VDOT++: Unified Few-Step Video Generation via Unbalanced Optimal Transport Distillation](https://arxiv.org/abs/2610.03221v1)**  
  Authors: Yutong Wang, Xingtong Ge, Enhuai Liu, Yunke Wang, Tianfan Xue, Yu Qiao, Yaohui Wang, Xinyuan Chen, Chang Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.03221v1.pdf)  
  Keywords: benchmark, distillation, i2v, image to video, image-to-video, t2v, text to video, text-to-video, video diffusion, video generation  
- **[In-Distribution Forcing for Long Video Generation at Test Time](https://arxiv.org/abs/2610.03120v1)**  
  Authors: Jeongwoo Shin, Youngyoon Choi, Sangwoo Jo, Hyunmog Kim, Sungjoon Choi, Joonseok Lee, Jaewoong Choi, Jaemoo Choi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.03120v1.pdf)  
  Keywords: autoregressive, benchmark, dynamics, long video, video diffusion, video generation  
- **[HiPhy: Hierarchical Alignment for Physically-Plausible Multi-Principle Video Generation](https://arxiv.org/abs/2610.02197v1)**  
  Authors: Tahira Kazimi, Shubhankar Borse, Munawar Hayat, Fatih Porikli, Pinar Yanardag  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.02197v1.pdf)  
  Keywords: benchmark, dynamics, physical, physics, video generation  
- **[MosaiChunk: Compositing Spatio-Temporal Memory for Autoregressive Video Generation](https://arxiv.org/abs/2610.02153v1)**  
  Authors: Yiwen Zhang, Haocheng Xi, Michael Tian-Yue Liu, Alexei A. Efros, Hadar Averbuch-Elor, Qianqian Wang, Haiwen Feng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.02153v1.pdf)  
  Keywords: autoregressive, autoregressive video, benchmark, i2v, image to video, image-to-video, t2v, text to video, text-to-video, video generation  
- **[DiVid: Diagnosing Dimension-Specific Diversity Collapse in Video Generation Models](https://arxiv.org/abs/2610.01661v1)**  
  Authors: Huanran Hu, Zihui Ren, Dingyi Yang, Zhinan Song, Guozheng Wu, Tiezheng Ge, Qin Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.01661v1.pdf)  
  Keywords: controllable, creative, evaluation, style, video generation  
- **[VTR-Bench: A Systematic Benchmark for Evaluating Visual Text Rendering in Video Generation](https://arxiv.org/abs/2610.01499v1)**  
  Authors: Yu Huang, Jungang Li, Zhiyuan Wang, Yonghua Hei, Song Dai, Jiayu Yang, Deyuan Liu, Xiang Zheng, Xiaoshuang Shi, Hao Cheng, Kaidi Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.01499v1.pdf) | [![GitHub](https://img.shields.io/github/stars/hardenyu21/VTR-Bench?style=social)](https://github.com/hardenyu21/VTR-Bench)  
  Keywords: benchmark, cinematic, evaluation, keyframe, physical, physical plausibility, video generation  
- **[PhysicsLENS: Diagnosing Physical Property Blindness in Video Generation Models](https://arxiv.org/abs/2610.01162v1)**  
  Authors: Isaiah Milkey, Som Sagar, Aditya Taparia, Xinyuan Liu, Jiqing Wen, Ransalu Senanayake  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.01162v1.pdf)  
  Keywords: benchmark, evaluation, physical, physics, robot learning, robotics, video generation  
- **[Ego2Act: Evaluating Goal-Directed Manipulation in Egocentric Video Generation](https://arxiv.org/abs/2610.01092v1)**  
  Authors: Patrick Amadeus Irawan, Iskandar Muda Rizky Parlambang, Rava Maulana, Qinrong Cui, Erland Hilman Fuadi, Zayd M. K. Zuhri, Nanda Ryaas Absar, Ahmed Elshabrawy, Wilfried Ariel Mulyawan, Shoubin Yu, Yue Zhang, Mohit Bansal, Alham Fikri Aji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.01092v1.pdf)  
  Keywords: benchmark, dynamics, embodied, evaluation, physical, physics, simulation, video generation  

### Text-to-Video Generation

*Showing the latest 50 out of 149 papers*

- **[VDOT++: Unified Few-Step Video Generation via Unbalanced Optimal Transport Distillation](https://arxiv.org/abs/2610.03221v1)**  
  Authors: Yutong Wang, Xingtong Ge, Enhuai Liu, Yunke Wang, Tianfan Xue, Yu Qiao, Yaohui Wang, Xinyuan Chen, Chang Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.03221v1.pdf)  
  Keywords: benchmark, distillation, i2v, image to video, image-to-video, t2v, text to video, text-to-video, video diffusion, video generation  
- **[Parasitic Co-Denoising: Unlocking 3D Human Motion Generation in a Frozen Video Diffusion Model](https://arxiv.org/abs/2610.03047v1)**  
  Authors: Yunjiao Zhou, Junlang Qian, Lihua Xie, Jianfei Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.03047v1.pdf)  
  Keywords: denoising, diffusion model, efficient, flow matching, human motion, text to video, text-to-video, video diffusion  
- **[DMAD: Distribution Matching as Adversarial Distillation for Fast Visual Generation](https://arxiv.org/abs/2610.02188v1)**  
  Authors: Zhengming Yu, Junkun Yuan, Haotian Yang, Gordon Guocheng Qian, Yizhi Wang, Angtian Wang, Yiding Yang, Bo Liu, Xin Li, Wenping Wang, Chongyang Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.02188v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://yzmblog.github.io/projects/DMAD)  
  Keywords: audio-video generation, diffusion model, distillation, identity, joint audio-video, t2v, video generation  
- **[MosaiChunk: Compositing Spatio-Temporal Memory for Autoregressive Video Generation](https://arxiv.org/abs/2610.02153v1)**  
  Authors: Yiwen Zhang, Haocheng Xi, Michael Tian-Yue Liu, Alexei A. Efros, Hadar Averbuch-Elor, Qianqian Wang, Haiwen Feng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.02153v1.pdf)  
  Keywords: autoregressive, autoregressive video, benchmark, i2v, image to video, image-to-video, t2v, text to video, text-to-video, video generation  
- **[Memory-Guided B-Roll Generation from User Video Collections](https://arxiv.org/abs/2610.01884v1)**  
  Authors: Cusuh Ham, Fabian Caba Heilbron, Josef Sivic, Bryan Russell  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.01884v1.pdf)  
  Keywords: identity, style, text to video, text-to-video  
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

### Video Editing

*Showing the latest 50 out of 93 papers*

- **[Unsupervised Domain Adaptation for Enhanced Radiometer Image Precipitation Estimation using Conditional Flow Matching](https://arxiv.org/abs/2610.01890v1)**  
  Authors: Victor Enescu, Assaad Zeghina, Matthieu Meignin, Nicolas Viltard, Cécile Mallet  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.01890v1.pdf)  
  Keywords: flow matching, video editing  
- **[ViTeX-Bench: Benchmarking High-Fidelity Video Scene Text Editing](https://arxiv.org/abs/2609.40356v1)**  
  Authors: Xinghao Chen, Xiangbo Gao, Jiongze Yu, Yuheng Wu, Zhengzhong Tu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.40356v1.pdf)  
  Keywords: benchmark, controllable, dynamics, evaluation, human evaluation, temporal consistency, video editing, video generation  
- **[Diffusion Editing with Soft Mask: Pixel Level Redo of Image and Video with Adjustable Strength](https://arxiv.org/abs/2610.00359v1)**  
  Authors: Candi Zheng, Yuan Lan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.00359v1.pdf)  
  Keywords: efficient, video diffusion, video editing  
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

### Video Inpainting & Completion

- **[ProAR: Learning Prospective Reasoning with Autoregressive Video Models](https://arxiv.org/abs/2610.03664v1)**  
  Authors: Linghui Shen, Tinghui Zhu, Sheng Zhang, Muhao Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.03664v1.pdf)  
  Keywords: autoregressive, autoregressive video, dynamics, efficient, embodied, frame prediction, video generation  
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

### Video Super-Resolution & Enhancement

*Showing the latest 50 out of 171 papers*

- **[Native Action-Prior Learning from Videos for World Action Models](https://arxiv.org/abs/2610.03391v1)**  
  Authors: Zhaochong An, Fei Zhang, Menglin Jia, Duncan Frost, Zijian Zhou, Yikai Wang, Xudong Wang, Aditya Patel, Belinda Zeng, Tao Xiang, Serge Belongie, Amir Bar, Sen He  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.03391v1.pdf)  
  Keywords: denoising, dit, dynamics, efficient, flow matching, video flow matching  
- **[Does Physics Live in the Activations? Localizing Physical Quantities in Video Diffusion Models](https://arxiv.org/abs/2610.03154v1)**  
  Authors: Jonas Kneifl, Jakub Skalski, Bartłomiej Twardowski, Kamil Deja  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.03154v1.pdf)  
  Keywords: denoising, dynamics, physical, physics, video diffusion, video generation  
- **[Parasitic Co-Denoising: Unlocking 3D Human Motion Generation in a Frozen Video Diffusion Model](https://arxiv.org/abs/2610.03047v1)**  
  Authors: Yunjiao Zhou, Junlang Qian, Lihua Xie, Jianfei Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.03047v1.pdf)  
  Keywords: denoising, diffusion model, efficient, flow matching, human motion, text to video, text-to-video, video diffusion  
- **[TRAC: Trajectory-aware Reuse and Adaptive Correction for Efficient Autoregressive Video Generation](https://arxiv.org/abs/2610.02779v1)**  
  Authors: Jiaxing Song, Weiqi Yan, You Huang, Mingte Qiu, Huazhong Liu, Xiaofeng Zhu, Yunshan Zhong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.02779v1.pdf)  
  Keywords: acceleration, autoregressive, autoregressive video, denoising, efficient, trajectory, video generation  
- **[SymRegFlow: Symmetry-Regularized Flow Matching for Video World Models](https://arxiv.org/abs/2610.02726v1)**  
  Authors: Xi Ye, Yuzhu Wang, Xiaoyang Liu, Jiayi Wang, Yangyang Xu, Ruyu Wang, Wenlin Chen, Duo Su, Jun Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.02726v1.pdf)  
  Keywords: autonomous driving, denoising, driving, flow matching, novel view, video generation, view-consistent  
- **[World Action Modeling with Progressive Visual Planning](https://arxiv.org/abs/2610.02508v1)**  
  Authors: Fei Zhang, Zhaochong An, Duncan Frost, Yikai Wang, Pengfei Liu, Ya Zhang, Michal Drozdzal, Amir Bar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.02508v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://sii-ferenas.github.io/ProWAM-page)  
  Keywords: denoising, dynamics, efficient, simulation, video generation  
- **[UniWAM: Unified World-Action Model](https://arxiv.org/abs/2610.02054v1)**  
  Authors: Jiayi Chen, Wenxuan Song, Jingbo Wang, Shuai Zhou, Xicheng Gong, Zehua Fan, Ziyang Zhou, Junwu E, Haodong Yan, Fuhao Li, Qize Yu, Xu Huang, Pengwei Wang, Wen Chen, Shunbo Zhou, Haoang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.02054v1.pdf)  
  Keywords: architecture, denoising, dynamics, embodied, flow matching, physical, video generation  
- **[Token-Level Video Reinforcement Learning](https://arxiv.org/abs/2610.01973v1)**  
  Authors: Yifan Wang, Gordon Guocheng Qian, Yanyu Li, Anil Kag, Yun Fu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.01973v1.pdf)  
  Keywords: denoising, video generation  
- **[TacDyn-WAM: Learning Implicit Tactile Dynamics in a Heterogeneous Visuo-Tactile World Action Model](https://arxiv.org/abs/2610.00638v1)**  
  Authors: Enyi Wang, Mingxin Wang, Quan Shi, Hetian Guo, Hongyu Wang, Xi Wang, Bin Qian, Yupeng Zheng, Wenxuan Song, Houde Liu, Yong Xu, Cheng Chi, Wenchao Ding, Yilun Chen, Yan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.00638v1.pdf)  
  Keywords: denoising, distillation, dynamics, dynamics-aware, video generation  
- **[Enhancing Autoregressive Video Generation via Representation Adversarial Distillation](https://arxiv.org/abs/2609.40037v1)**  
  Authors: Fangyu Lin, Xingtong Ge, Lunjie Zhu, Yi Zhang, Zhening Liu, Tianhang Wang, Mengfei Li, Yumeng Zhang, Guanglu Song, Yu Liu, Jun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.40037v1.pdf)  
  Keywords: architecture, autoregressive, autoregressive video, denoising, distillation, efficient, minute-long, streaming, video generation  

### World Models & Simulation

*Showing the latest 50 out of 241 papers*

- **[World Embedding Benchmark](https://arxiv.org/abs/2610.03632v1)**  
  Authors: Yiqi Liu, Ruifeng Yuan, Yang Wang, Long Li, Fengyu Cai, Hou Pong Chan, Jialin Yu, Hao Zhang, Chenghua Lin, Chenghao Xiao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.03632v1.pdf)  
  Keywords: benchmark, dynamics, physical, physics, simulation, video generation  
- **[Weave Forcing: Compositional Memory Routing for Interactive Long Video Generation](https://arxiv.org/abs/2610.03510v1)**  
  Authors: Ziyi Wang, Junchi Yao, Heqian Qiu, Wenbo Shi, Chengjiu Wang, Jinyang He, Binkai Hong, Hongliang Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.03510v1.pdf)  
  Keywords: autoregressive, autoregressive video, interactive, long video, temporal consistency, video generation  
- **[Spatial Memory Intelligence: Endowing World Models with Understanding-Driven Long-Term Memory](https://arxiv.org/abs/2610.02521v1)**  
  Authors: Ying Yang, Guiyu Zhang, Lianghua Huang, Chang Nie, Chenyang Si, Haofan Wang, Shaoshuai Shi, Li Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.02521v1.pdf)  
  Keywords: embodied, interactive, long video, simulation, video generation, world model  
- **[World Action Modeling with Progressive Visual Planning](https://arxiv.org/abs/2610.02508v1)**  
  Authors: Fei Zhang, Zhaochong An, Duncan Frost, Yikai Wang, Pengfei Liu, Ya Zhang, Michal Drozdzal, Amir Bar  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.02508v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://sii-ferenas.github.io/ProWAM-page)  
  Keywords: denoising, dynamics, efficient, simulation, video generation  
- **[A Simulation-Grounded Agentic VLM Framework for Wildfire Monitoring and Reporting](https://arxiv.org/abs/2610.02451v1)**  
  Authors: Duowen Chen, Yuchen Sun, Zhiqi Li, Yuxuan Liao, Sinan Wang, Bart van Bloemen Waanders, Bo Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.02451v1.pdf)  
  Keywords: controllable, dynamics, layout, physical, simulation, video generation  
- **[4Director: Controlling Video World Models with Rigid 3D Geometry](https://arxiv.org/abs/2610.02160v1)**  
  Authors: Wei Cao, Hao Zhang, Vikram Voleti, Yuqun Wu, Mallikarjun B R, Shimon Vainer, Mark Boss, Yaoyao Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.02160v1.pdf)  
  Keywords: dynamics, identity, video world model, view-consistent, world model  
- **[Oneira: From Open-Ended Generation to Open-World Interaction in Video World Models](https://arxiv.org/abs/2610.01614v1)**  
  Authors: Xindi Yang, Baolu Li, Liam Lee, Zhenfei Yin, Songxin Zhang, Zhuoyang Song, Xu Jia, Jianfei Cai, Tien-Tsin Wong, Bingyi Jing, Mengyue Yang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.01614v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://madaoer.github.io/projects/oneira)  
  Keywords: interactive, trajectory, video world model, world model  
- **[Ego2Act: Evaluating Goal-Directed Manipulation in Egocentric Video Generation](https://arxiv.org/abs/2610.01092v1)**  
  Authors: Patrick Amadeus Irawan, Iskandar Muda Rizky Parlambang, Rava Maulana, Qinrong Cui, Erland Hilman Fuadi, Zayd M. K. Zuhri, Nanda Ryaas Absar, Ahmed Elshabrawy, Wilfried Ariel Mulyawan, Shoubin Yu, Yue Zhang, Mohit Bansal, Alham Fikri Aji  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2610.01092v1.pdf)  
  Keywords: benchmark, dynamics, embodied, evaluation, physical, physics, simulation, video generation  
- **[Physis-Lang: Self-Evolving Language as a Physical Representation for Video World Model](https://arxiv.org/abs/2609.40358v1)**  
  Authors: Liming Lu, Xianzheng Ma, Wenkun He, Guanqi Zhan, Yilin Zhao, Junyu Chen, Mengyao Xu, Jiaojiao Fan, Wenhang Ge, Yuchao Gu, Yunze Liu, Boyi Li, Zhen Dong, Victor Prisacariu, Ming-Yu Liu, Song Han, Han Cai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.40358v1.pdf)  
  Keywords: physical, physical plausibility, video generation, video world model, world model  
- **[LOCI: Spatial Linear Memory for Streaming World Models](https://arxiv.org/abs/2609.40222v1)**  
  Authors: Ji Xia, Tingting Liao, Xuezhi Liang, Hao Li, Guangyi Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.40222v1.pdf)  
  Keywords: architecture, benchmark, streaming, video world model, world model  



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
Suggestions are welcome through [Issues](https://github.com/longxiang-ai/awesome-video-diffusions/issues/new/choose) or Pull Requests. This list covers:
- **Research papers** on video diffusion and video generation (arXiv or peer-reviewed venues). Most papers are collected automatically every day, so please suggest ones the crawler missed.
- **Open-source projects** with public code, such as models, training frameworks and toolkits.
- **Tutorials and blog posts** that explain the research.

Commercial products, paid services and promotional links are out of scope, and issues suggesting them will be closed.

Please follow these formats:
- Paper entry format: `**[Paper Title](link)** - Brief description`
- Project entry format: `[Project Name](link) - Project description`

## License
[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/) 
