# Awesome Video Diffusions [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

A curated list of latest research papers, projects and resources related to Video Diffusion Models and Video Generation. Content is automatically updated daily.

> Last Update: 2026-09-27 03:58:57

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

- [3D-aware Video Generation](#3d-aware-video-generation) (53 papers) - Video generation with 3D awareness, multi-view consistency, and 4D content creation
- [Applications](#applications) (200 papers) - Domain-specific applications of video diffusion models
- [Architecture & Efficiency](#architecture-&-efficiency) (396 papers) - Architectural innovations (DiT, UNet), flow matching, and training/inference efficiency
- [Audio & Multi-modal](#audio-&-multi-modal) (71 papers) - Audio-driven and multi-modal conditioned video generation
- [Controllable Generation](#controllable-generation) (327 papers) - Controllable video generation with motion, camera, pose, or layout guidance
- [Human & Character Animation](#human-&-character-animation) (61 papers) - Human-centric video generation including talking heads, dance, and character animation
- [Image-to-Video Generation](#image-to-video-generation) (93 papers) - Methods for animating still images into videos
- [Long Video Generation](#long-video-generation) (267 papers) - Generating temporally consistent long-form videos beyond short clips
- [Personalization & Customization](#personalization-&-customization) (180 papers) - Personalized video generation with custom subjects, identities, or styles
- [Physical Understanding](#physical-understanding) (314 papers) - Physics-aware video generation and dynamics modeling
- [Surveys & Benchmarks](#surveys-&-benchmarks) (309 papers) - Survey papers, benchmarks, and evaluation metrics for video generation
- [Text-to-Video Generation](#text-to-video-generation) (148 papers) - Foundation models and methods for generating videos from text prompts
- [Video Editing](#video-editing) (102 papers) - Diffusion-based video editing, style transfer, and manipulation
- [Video Inpainting & Completion](#video-inpainting-&-completion) (24 papers) - Video inpainting, completion, outpainting, and temporal prediction
- [Video Super-Resolution & Enhancement](#video-super-resolution-&-enhancement) (165 papers) - Video quality improvement, upscaling, restoration, and frame interpolation
- [World Models & Simulation](#world-models-&-simulation) (243 papers) - Video generation as world simulators and interactive environment generation



## Table of Contents

- [Categorized Papers](#categorized-papers)
- [Classic Papers](#classic-papers)
- [Open Source Projects](#open-source-projects)
- [Applications](#applications)
- [Tutorials & Blogs](#tutorials--blogs)





## Categorized Papers

### 3D-aware Video Generation

*Showing the latest 50 out of 53 papers*

- **[WorldCrafter: Consistent Video World Model with Implicit 3D-aware Memory](https://arxiv.org/abs/2609.24984v1)**  
  Authors: Wangbo Yu, Kunhao Liu, Wenbo Hu, Shenghai Yuan, Chaoran Feng, Haiyang Zhou, Yukun Huang, Yiran Wang, Wang Zhao, Yingmin Luo, Ying Shan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.24984v1.pdf)  
  Keywords: 3d-aware, camera control, denoising, distillation, interactive, streaming, video world model, world model  
- **[Printing the Underdetermined: Materializing Multi-solutionness in Figurative Paintings](https://arxiv.org/abs/2609.19782v1)**  
  Authors: Yutao Ming, Teng Xu, Youjia Wang, Yunyang Liu, Fengmin Yang, Fuqiang Zhao, Jingyi Yu, Hua Yang, Yanjun Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.19782v1.pdf)  
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
- **[Building Pretraining Data for World Models: An Unreal Engine-Based Pipeline for Action-Conditioned Video Generation](https://arxiv.org/abs/2609.03557v1)**  
  Authors: Haoyu Wang, Songchun Zhang, Haoran Li, Haoyang Huang, Zeyue Xue, Nan Duan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.03557v1.pdf)  
  Keywords: action-conditioned, architecture, multi-view video, physics, trajectory, video generation, world model  
- **[RoGe: Novel View Synthesis via End-to-End Implicit Reconstruction and Generation](https://arxiv.org/abs/2609.02847v2)**  
  Authors: Xiaolei Lang, Ze Kang, Zehao Huang, Naiyan Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.02847v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://jerry-locker.github.io/roge)  
  Keywords: camera trajectory, diffusion model, novel view, temporal consistency, trajectory, video diffusion  
- **[Spatially Aware World Action Model via Geometric Latent Diffusion](https://arxiv.org/abs/2609.02531v1)**  
  Authors: Javier Alejandro Lopetegui Gonzalez, Paul Pacaud, Cordelia Schmid  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.02531v1.pdf)  
  Keywords: 3d-aware, evaluation, physical, video diffusion, world model  
- **[Streaming4D: Accelerate 4D World Models via Block-wise Video Generation and Incremental Reconstruction](https://arxiv.org/abs/2609.00610v2)**  
  Authors: Xiaoyan Liu, Jiaxin Liu, Kangrui Li, Sifan Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.00610v2.pdf)  
  Keywords: 4d generation, autoregressive, autoregressive video, interactive, style, video generation  

### Applications

*Showing the latest 50 out of 200 papers*

- **[WanPE: Towards Cinematic Prompt Enhancement for Modern Text-to-Video Generation](https://arxiv.org/abs/2609.30221v1)**  
  Authors: Yubo Zhu, Yawen Shao, Ziyun Dai, Zixun Fang, Kai Zhu, Siyang Sun, Haolan Xue, Chuxin Wang, Tingyu Weng, Jingming Luo, Chen Shi, Lianghua Huang, Yufeng Ai, Yuzheng Wang, Wenyuan Zhang, Yu Shang, Yuxiang Bao, Zoubin Bi, Jie Xiao, Jinbo Xing, Jiaxing Zhao, Chongyang Zhong, Hengjian Chen, Chenwei Xie, Akide Liu, Zhehan Kan, Yu Liu, Wei Zhai, Sheng Zhong, Wei Tong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.30221v1.pdf)  
  Keywords: benchmark, cinematic, sound, text to video, text-to-video, video generation  
- **[SALI: Shot-Aware Late Interaction for Cross-Shot Relation Matching in Text-to-Video Retrieval using Film-Grammar Knowledge](https://arxiv.org/abs/2609.29721v1)**  
  Authors: Toya Oyama, Rainer Lienhart, Shin'ichi Satoh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.29721v1.pdf)  
  Keywords: film, text to video, text-to-video  
- **[QuantWM: Temporally Consistent 2-Bit KV Cache Quantization for World Models and Video Generation](https://arxiv.org/abs/2609.26425v2)**  
  Authors: Jiaqi Zhao, Xiaobin Hu, Bo Yin, Junpeng Jiang, Miao Zhang, Shuicheng Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.26425v2.pdf)  
  Keywords: efficient, game, temporal consistency, video generation  
- **[GameDirector: Decoupling Gameplay Logic from Rendering for Player-Configurable Game World Models](https://arxiv.org/abs/2609.25652v1)**  
  Authors: Zijun Lin, Zhiyang Deng, Yuzhe Wu, Bihan Wen, Yeying Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.25652v1.pdf)  
  Keywords: controllable, dynamics, game, interactive, simulation, video world model, world model  
- **[Grounded Action Model: 3D Grounding as a Foundation for Robotics](https://arxiv.org/abs/2609.23863v1)**  
  Authors: Gehao Zhang, Weikai Huang, Shailesh Shailesh, Yiyan Peng, Jiafei Duan, Ranjay Krishna  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.23863v1.pdf)  
  Keywords: robotics, video generation  
- **[Why Do Video Diffusion Models Violate Physics? Unveiling the Flaws in Attention Mechanisms](https://arxiv.org/abs/2609.23658v1)**  
  Authors: Yueyan Li, Haibo Wang, Caixia Yuan, Xiaojie Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.23658v1.pdf)  
  Keywords: denoising, driving, physical, physics, text to video, text-to-video, trajectory, video diffusion  
- **[MT-WAM: Reorienting the One-Pass Predictive Representation Toward Action Generation](https://arxiv.org/abs/2609.21474v1)**  
  Authors: Yiguang Yang, Jiankun Peng, Xiaoming Wang, Yiran Zhang, Zhibo Fang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.21474v1.pdf)  
  Keywords: diffusion transformer, dynamics, embodied, video diffusion, video diffusion transformer, video prediction  
- **[Astronex-World 1.0: Real-Time Interactive World Model Foundation](https://arxiv.org/abs/2609.20034v1)**  
  Authors: Xin Zhou, Cong Miao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.20034v1.pdf)  
  Keywords: autonomous driving, controllable, driving, dynamics, embodied, image to video, image-to-video, interactive, text to video, text-to-video, video world model, world model  
- **[StrucPhysVideo: Learning Physical Dynamics from Structured Captions and Robot Actions](https://arxiv.org/abs/2609.18430v1)**  
  Authors: Awomo-WM Team, :, Enhui Ma, Kaiwen Guo, Tingrui Zhang, Wei Song, Yingshui Tan, Jianhua Xu, Tong Zhang, Kaicheng Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.18430v1.pdf)  
  Keywords: action-conditioned, autoregressive, camera motion, denoising, distillation, dynamics, embodied, image to video, image-to-video, interactive, physical, physics, video prediction, video world model, world model  
- **[LynnReal-Omni: Native multi-modal Video Generation for Agentic Visual Workflows](https://arxiv.org/abs/2609.15863v1)**  
  Authors: Xiaofeng Mao, Peijia Lin, Shaohao Rui, Yibo Zhang, Haibin Wan, Weijie Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.15863v1.pdf)  
  Keywords: acceleration, controllable, diffusion transformer, efficient, evaluation, game, long video, multi-modal, reference-guided, streaming, streaming video generation, text to video, text-to-video, video diffusion, video generation, video restoration  

### Architecture & Efficiency

*Showing the latest 50 out of 396 papers*

- **[Accelerating Video Diffusion via Training-Free Trajectory Routing](https://arxiv.org/abs/2609.30096v1)**  
  Authors: Mustafa Munir, Huy Vu, Shreyas Misra, Rohit Jena, Sajad Norouzi, Ali Taghibakhshi, Anis Ahmad, Anjul Patney, Pavlo Molchanov, Nima Tajbakhsh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.30096v1.pdf)  
  Keywords: acceleration, architecture, denoising, distillation, efficient, evaluation, trajectory, video diffusion  
- **[ViRDM: Taming Representation Distribution Matching for Few-Step Causal Video Generation](https://arxiv.org/abs/2609.28923v1)**  
  Authors: Zichong Meng, Chongjian Ge, Chun-Hao P. Huang, Yang Zhou, Huaizu Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.28923v1.pdf)  
  Keywords: autoregressive, distillation, dynamics, evaluation, streaming, video diffusion, video generation  
- **[Beyond Future Prediction: Denoising as Generative Adaptation for Robot Control](https://arxiv.org/abs/2609.28339v1)**  
  Authors: Zanyi Wang, Yuheng Lei, Dengyang Jiang, Ping Luo, Mengdi Wang, Zhixuan Liang, Shilong Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.28339v1.pdf)  
  Keywords: denoising, dit, trajectory, video generation  
- **[Information Capacity of Generative Video Compression: Quantifying the Rate-Compute Exchange at Identical Quality](https://arxiv.org/abs/2609.27493v1)**  
  Authors: Cheng Yuan, Jiawei Shao, Xuelong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.27493v1.pdf)  
  Keywords: architecture, denoising  
- **[Latent evolving World Action Model](https://arxiv.org/abs/2609.27455v2)**  
  Authors: Xueji Fang, Boqiang Duan, Hua Wu, Jingdong Wang, Guo-Jun Qi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.27455v2.pdf)  
  Keywords: architecture, dynamics, video diffusion, video generation  
- **[QuantWM: Temporally Consistent 2-Bit KV Cache Quantization for World Models and Video Generation](https://arxiv.org/abs/2609.26425v2)**  
  Authors: Jiaqi Zhao, Xiaobin Hu, Bo Yin, Junpeng Jiang, Miao Zhang, Shuicheng Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.26425v2.pdf)  
  Keywords: efficient, game, temporal consistency, video generation  
- **[Qwen3.8-Omni: Towards Native Omni-Modal Agents](https://arxiv.org/abs/2609.25611v1)**  
  Authors: Qwen Team  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.25611v1.pdf)  
  Keywords: architecture, long-form, music video, video editing, video translation  
- **[WorldCrafter: Consistent Video World Model with Implicit 3D-aware Memory](https://arxiv.org/abs/2609.24984v1)**  
  Authors: Wangbo Yu, Kunhao Liu, Wenbo Hu, Shenghai Yuan, Chaoran Feng, Haiyang Zhou, Yukun Huang, Yiran Wang, Wang Zhao, Yingmin Luo, Ying Shan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.24984v1.pdf)  
  Keywords: 3d-aware, camera control, denoising, distillation, interactive, streaming, video world model, world model  
- **[DexTacWAM: A Visuo-Tactile World-Action Model for Dexterous Manipulation](https://arxiv.org/abs/2609.24976v1)**  
  Authors: Haoran Yuan, Zekai Wang, Boning Shao, Haoran Lu, Trevor Darrell, Ismini Lourentzou, Wei Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.24976v1.pdf)  
  Keywords: dynamics, efficient, video diffusion, world model  
- **[Streaming Video Editing with Easy Adaptation](https://arxiv.org/abs/2609.24788v1)**  
  Authors: Yujia Hu, Jiajun Li, Zihao He, Songhua Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.24788v1.pdf) | [![GitHub](https://img.shields.io/github/stars/YujiaHu1109/SVEET?style=social)](https://github.com/YujiaHu1109/SVEET)  
  Keywords: acceleration, controllable, diffusion model, streaming, video diffusion, video editing, video generation, video to video, video-to-video  

### Audio & Multi-modal

*Showing the latest 50 out of 71 papers*

- **[WanPE: Towards Cinematic Prompt Enhancement for Modern Text-to-Video Generation](https://arxiv.org/abs/2609.30221v1)**  
  Authors: Yubo Zhu, Yawen Shao, Ziyun Dai, Zixun Fang, Kai Zhu, Siyang Sun, Haolan Xue, Chuxin Wang, Tingyu Weng, Jingming Luo, Chen Shi, Lianghua Huang, Yufeng Ai, Yuzheng Wang, Wenyuan Zhang, Yu Shang, Yuxiang Bao, Zoubin Bi, Jie Xiao, Jinbo Xing, Jiaxing Zhao, Chongyang Zhong, Hengjian Chen, Chenwei Xie, Akide Liu, Zhehan Kan, Yu Liu, Wei Zhai, Sheng Zhong, Wei Tong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.30221v1.pdf)  
  Keywords: benchmark, cinematic, sound, text to video, text-to-video, video generation  
- **[AV-GRPO: Modality-Anchored Decoupling Diffusion Reinforcement Learning for Joint Audio-Video Generation](https://arxiv.org/abs/2609.29816v1)**  
  Authors: Zhiyu Xu, Weilong Yan, Yufei Shi, Shiyang Li, Yihao Liu, Kin-Man Lam, Yuewen Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.29816v1.pdf) | [![GitHub](https://img.shields.io/github/stars/zhiyuxu03/AV-GRPO?style=social)](https://github.com/zhiyuxu03/AV-GRPO)  
  Keywords: audio-video generation, controllable, dynamics, evaluation, joint audio-video, trajectory, video generation  
- **[Qwen3.8-Omni: Towards Native Omni-Modal Agents](https://arxiv.org/abs/2609.25611v1)**  
  Authors: Qwen Team  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.25611v1.pdf)  
  Keywords: architecture, long-form, music video, video editing, video translation  
- **[Dreaming the Sound of Contact: Leveraging Video and Audio Generation for Zero-Shot Force-Aware Manipulation and Data Generation](https://arxiv.org/abs/2609.19137v2)**  
  Authors: Guanhua Ji, Tianyu Li, Dayoon Suh, Yuqian Zhang, Boyan Zhang, Nadia Figueroa  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.19137v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://dreamingcontactsound.github.io)  
  Keywords: sound, video generation  
- **[Can MiniMax-H3 Reason About the Physical World? An Evaluation of Omni-Modal Generative Model](https://arxiv.org/abs/2609.18323v1)**  
  Authors: Haoyu Zhao, Zihao Zhao, Tianyu Deng, Ziqin Xu, Zihao Zhang, Xudong Wang, Jinxiang Guo, Chen Gao, Ziyi Ye, Yeying Jin, Jiaxi Gu, Zuxuan Wu, Shuicheng Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.18323v1.pdf) | [![GitHub](https://img.shields.io/github/stars/gulucaptain/MiniMax-H3-Reason?style=social)](https://github.com/gulucaptain/MiniMax-H3-Reason)  
  Keywords: architecture, audio-visual generation, dynamics, evaluation, physical, video generation  
- **[LynnReal-Omni: Native multi-modal Video Generation for Agentic Visual Workflows](https://arxiv.org/abs/2609.15863v1)**  
  Authors: Xiaofeng Mao, Peijia Lin, Shaohao Rui, Yibo Zhang, Haibin Wan, Weijie Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.15863v1.pdf)  
  Keywords: acceleration, controllable, diffusion transformer, efficient, evaluation, game, long video, multi-modal, reference-guided, streaming, streaming video generation, text to video, text-to-video, video diffusion, video generation, video restoration  
- **[Dynamic Learning Solutions: A System for Personalized Educational Video Generation](https://arxiv.org/abs/2609.14408v1)**  
  Authors: Siddhanth Sridhar, Shreya Chaurasia, Baddela Sai Yaswantha Reddy, Deepak Parmar, Shylaja S S  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.14408v1.pdf)  
  Keywords: education, interactive, multi-modal, style, video generation  
- **[Beyond Coherence: Benchmarking Professional Editing-Technique Execution in Multi-Shot Audio-Video Generation](https://arxiv.org/abs/2609.08275v2)**  
  Authors: Tianyi Zeng, Junchao Liao, Yujie Wei, Ziying Zhang, Litao Li, Tianyi Wang, Zhichao Wei, Shuyao Xu, Wenwen Qiang, Siyu Zhu, Zhenghao Zhang, Long Qin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.08275v2.pdf) | [![GitHub](https://img.shields.io/github/stars/AlibabaResearch/cut-craft-bench?style=social)](https://github.com/AlibabaResearch/cut-craft-bench)  
  Keywords: audio-video generation, benchmark, cinematic, evaluation, physical, physical plausibility, video generation  
- **[AV-SafetyBench: A Safety Benchmark for Text-to-Audio-Video Generation](https://arxiv.org/abs/2609.06991v1)**  
  Authors: Suah Choi, Tae-Young Lee, Gyeong-Moon Park  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.06991v1.pdf)  
  Keywords: audio-video generation, benchmark, evaluation, sound, video generation  
- **[MVWeaver: A Hierarchical Music Video Generation Agent with a Learned Song-to-Visual Bridge](https://arxiv.org/abs/2609.06478v1)**  
  Authors: Sifei Li, Minyan Luo, Xu Li, Guodong Qi, Xincan Wang, Hanwen Wang, Chen Zhang, Pengfei Wan, Oliver Deussen, Weiming Dong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.06478v1.pdf)  
  Keywords: architecture, long-form, music video, video generation  

### Controllable Generation

*Showing the latest 50 out of 327 papers*

- **[Accelerating Video Diffusion via Training-Free Trajectory Routing](https://arxiv.org/abs/2609.30096v1)**  
  Authors: Mustafa Munir, Huy Vu, Shreyas Misra, Rohit Jena, Sajad Norouzi, Ali Taghibakhshi, Anis Ahmad, Anjul Patney, Pavlo Molchanov, Nima Tajbakhsh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.30096v1.pdf)  
  Keywords: acceleration, architecture, denoising, distillation, efficient, evaluation, trajectory, video diffusion  
- **[AV-GRPO: Modality-Anchored Decoupling Diffusion Reinforcement Learning for Joint Audio-Video Generation](https://arxiv.org/abs/2609.29816v1)**  
  Authors: Zhiyu Xu, Weilong Yan, Yufei Shi, Shiyang Li, Yihao Liu, Kin-Man Lam, Yuewen Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.29816v1.pdf) | [![GitHub](https://img.shields.io/github/stars/zhiyuxu03/AV-GRPO?style=social)](https://github.com/zhiyuxu03/AV-GRPO)  
  Keywords: audio-video generation, controllable, dynamics, evaluation, joint audio-video, trajectory, video generation  
- **[Beyond Future Prediction: Denoising as Generative Adaptation for Robot Control](https://arxiv.org/abs/2609.28339v1)**  
  Authors: Zanyi Wang, Yuheng Lei, Dengyang Jiang, Ping Luo, Mengdi Wang, Zhixuan Liang, Shilong Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.28339v1.pdf)  
  Keywords: denoising, dit, trajectory, video generation  
- **[MotionSpec: Spectral Trajectory Supervision for Motion-Consistent Video Generation](https://arxiv.org/abs/2609.28095v1)**  
  Authors: Ziqi Ni, Rui Li, Shiqi Jiang, Wei Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.28095v1.pdf)  
  Keywords: text to video, text-to-video, trajectory, video generation  
- **[GameDirector: Decoupling Gameplay Logic from Rendering for Player-Configurable Game World Models](https://arxiv.org/abs/2609.25652v1)**  
  Authors: Zijun Lin, Zhiyang Deng, Yuzhe Wu, Bihan Wen, Yeying Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.25652v1.pdf)  
  Keywords: controllable, dynamics, game, interactive, simulation, video world model, world model  
- **[WorldCrafter: Consistent Video World Model with Implicit 3D-aware Memory](https://arxiv.org/abs/2609.24984v1)**  
  Authors: Wangbo Yu, Kunhao Liu, Wenbo Hu, Shenghai Yuan, Chaoran Feng, Haiyang Zhou, Yukun Huang, Yiran Wang, Wang Zhao, Yingmin Luo, Ying Shan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.24984v1.pdf)  
  Keywords: 3d-aware, camera control, denoising, distillation, interactive, streaming, video world model, world model  
- **[Streaming Video Editing with Easy Adaptation](https://arxiv.org/abs/2609.24788v1)**  
  Authors: Yujia Hu, Jiajun Li, Zihao He, Songhua Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.24788v1.pdf) | [![GitHub](https://img.shields.io/github/stars/YujiaHu1109/SVEET?style=social)](https://github.com/YujiaHu1109/SVEET)  
  Keywords: acceleration, controllable, diffusion model, streaming, video diffusion, video editing, video generation, video to video, video-to-video  
- **[CoaG: Cylinders on a Grid for Coarse 3D Layout Control in Video Generation](https://arxiv.org/abs/2609.24208v2)**  
  Authors: Zhangsihao Yang, Mengyi Shan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.24208v2.pdf)  
  Keywords: layout, text to video, text-to-video, video generation  
- **[Why Do Video Diffusion Models Violate Physics? Unveiling the Flaws in Attention Mechanisms](https://arxiv.org/abs/2609.23658v1)**  
  Authors: Yueyan Li, Haibo Wang, Caixia Yuan, Xiaojie Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.23658v1.pdf)  
  Keywords: denoising, driving, physical, physics, text to video, text-to-video, trajectory, video diffusion  
- **[SparkDiffusion: Mitigating the High-Sparsity Trap --- A Unified Framework for up to $265\times$ Single-GPU Acceleration of Visual Generation](https://arxiv.org/abs/2609.23153v1)**  
  Authors: Yuxi Liu, Haoyu Li, Zekun Zhang, Tengxu Sun, Yixiang Cai, Jiayong Li, Yifei Xia, Tianle Liu, Baole Ai, Ang Wang, Jiamang Wang, Lin Qu, Kai Zhang, Kun Yuan, Bin Cui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.23153v1.pdf)  
  Keywords: acceleration, architecture, distillation, i2v, t2v, trajectory, video diffusion  

### Human & Character Animation

*Showing the latest 50 out of 61 papers*

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
- **[4DStreamCtrl: Interactive Video Generation with Online 4D Control](https://arxiv.org/abs/2608.25479v3)**  
  Authors: Shiqian Li, Chenguo Lin, Zhiguang Liu, Yu Tang, Jiarong Ou, Rui Chen, Yixin Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.25479v3.pdf)  
  Keywords: 3d consistent, camera motion, controllable, denoising, diffusion model, efficient, embodied, interactive, long video, motion control, motion transfer, streaming, trajectory, video diffusion, video generation  
- **[AvatarDynamizer: From Static to Dynamic Human Avatars via Generative Dynamic Textures](https://arxiv.org/abs/2608.19900v1)**  
  Authors: Guoxing Sun, Heming Zhu, Linjie Lyu, Pascal Fua, Christian Theobalt, Marc Habermann  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.19900v1.pdf)  
  Keywords: avatar, controllable, dynamics, video diffusion, view-consistent  
- **[SingDance: Compositional Zero-Shot Singing-and-Dancing Video Generation with Role-Aware Audio Conditioning](https://arxiv.org/abs/2608.16220v1)**  
  Authors: Tao Feng, Xu Li, Xiangyang Luo, Ming Wen, Huadai Liu, Chen Zhang, Wei Xue  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.16220v1.pdf)  
  Keywords: body motion, controllable, speech-driven, video diffusion, video generation  
- **[AnyTalk: Speech Animation for Arbitrary Characters Leveraging a Video Generation Model](https://arxiv.org/abs/2608.16143v1)**  
  Authors: Kwan Yun, Serin Yoon, Sunjin Jung, Jung Eun Yoo, Inyup Lee, Junyong Noh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.16143v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://serin-yoon.github.io/projects/anytalk)  
  Keywords: audio-driven, diffusion model, talking head, video diffusion, video generation  
- **[FlowDance: Music-Driven Dance Video Generation with Parallel Pose and RGB Streams](https://arxiv.org/abs/2608.15818v1)**  
  Authors: Genying Li, Boda Lin, Jiachen Li, Zijian Jia, Haojie Zheng, Yiming Wang, Shuchen Weng, Si Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.15818v1.pdf)  
  Keywords: body motion, denoising, human animation, identity, identity-preserving, long video, video generation, video synthesis  

### Image-to-Video Generation

*Showing the latest 50 out of 93 papers*

- **[SparkDiffusion: Mitigating the High-Sparsity Trap --- A Unified Framework for up to $265\times$ Single-GPU Acceleration of Visual Generation](https://arxiv.org/abs/2609.23153v1)**  
  Authors: Yuxi Liu, Haoyu Li, Zekun Zhang, Tengxu Sun, Yixiang Cai, Jiayong Li, Yifei Xia, Tianle Liu, Baole Ai, Ang Wang, Jiamang Wang, Lin Qu, Kai Zhang, Kun Yuan, Bin Cui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.23153v1.pdf)  
  Keywords: acceleration, architecture, distillation, i2v, t2v, trajectory, video diffusion  
- **[Astronex-World 1.0: Real-Time Interactive World Model Foundation](https://arxiv.org/abs/2609.20034v1)**  
  Authors: Xin Zhou, Cong Miao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.20034v1.pdf)  
  Keywords: autonomous driving, controllable, driving, dynamics, embodied, image to video, image-to-video, interactive, text to video, text-to-video, video world model, world model  
- **[StrucPhysVideo: Learning Physical Dynamics from Structured Captions and Robot Actions](https://arxiv.org/abs/2609.18430v1)**  
  Authors: Awomo-WM Team, :, Enhui Ma, Kaiwen Guo, Tingrui Zhang, Wei Song, Yingshui Tan, Jianhua Xu, Tong Zhang, Kaicheng Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.18430v1.pdf)  
  Keywords: action-conditioned, autoregressive, camera motion, denoising, distillation, dynamics, embodied, image to video, image-to-video, interactive, physical, physics, video prediction, video world model, world model  
- **[PhysStream: Streaming Physics-Grounded Video Generation with Structured Scene Memory and Fine-Grained Motion Control](https://arxiv.org/abs/2609.17521v2)**  
  Authors: Chuhao Chen, Peter Wonka, Chaoyang Wang, Chen Wang, Qiao Feng, Sergey Tulyakov, Lingjie Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.17521v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://czzzzh.github.io/PhysStream)  
  Keywords: autoregressive, controllable, dynamics, image to video, image-to-video, interactive, motion control, physical, physical consistency, physics, streaming, trajectory, video generation, video synthesis  
- **[CrossDistill: Balancing Quality and Diversity via Trajectory-Level Hybrid Few-Step Distillation](https://arxiv.org/abs/2609.14725v2)**  
  Authors: Yuxi Liu, Haoyu Li, Yixiang Cai, Tengxu Sun, Zekun Zhang, Baole Ai, Ang Wang, Jiamang Wang, Lin Qu, Kun Yuan, Kai Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.14725v2.pdf)  
  Keywords: distillation, image to video, image-to-video, text to video, text-to-video, trajectory, video diffusion  
- **[DF26: We Cannot Tell Fake From Real Anymore](https://arxiv.org/abs/2609.07369v1)**  
  Authors: Severyn Shykula, Andrii Yermakov, Ivan Samarskyi, Dmytro Mishkin, Jan Cech, Anastasiia Mishchuk  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.07369v1.pdf)  
  Keywords: benchmark, evaluation, image to video, image-to-video, text to video, text-to-video  
- **[PhysWeep: Does a Video Generator Realize the Physics You Ask For?](https://arxiv.org/abs/2609.06207v1)**  
  Authors: Rasul Khanbayov, Hasan Kurban  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.06207v1.pdf)  
  Keywords: benchmark, dynamics, image to video, image-to-video, physical, physics  
- **[EditaLive! Unified Character Video Editing for Live Streaming](https://arxiv.org/abs/2608.27123v1)**  
  Authors: Zhiyuan Li, Chi-Man Pun, Peng-Tao Jiang, Bo Li, Xiaodong Cun  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.27123v1.pdf)  
  Keywords: distillation, image animation, sparse attention, streaming, video editing  
- **[TempJail: Temporal Jailbreak Attacks against Image-to-Video Generation Models](https://arxiv.org/abs/2608.26971v2)**  
  Authors: Qi Lu, Zehui Guo, David Yuanda Gan, Zijing Li, Hengda Zhang, Weijun Xu, Qiankun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.26971v2.pdf) | [![GitHub](https://img.shields.io/github/stars/luqi-glory/TempJail?style=social)](https://github.com/luqi-glory/TempJail)  
  Keywords: evaluation, human evaluation, i2v, image to video, image-to-video, video generation, video synthesis  
- **[Direct, Parallel, or Sequential? A Comparative Study of Training-Free Multi-Subject Image-to-Video Generation](https://arxiv.org/abs/2608.22819v1)**  
  Authors: Yanliang Qi, Kexi Chen, Muchao Ye, Haomiao Ni  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.22819v1.pdf)  
  Keywords: controllable, i2v, image to video, image-to-video, temporal consistency, video generation  

### Long Video Generation

*Showing the latest 50 out of 267 papers*

- **[ViRDM: Taming Representation Distribution Matching for Few-Step Causal Video Generation](https://arxiv.org/abs/2609.28923v1)**  
  Authors: Zichong Meng, Chongjian Ge, Chun-Hao P. Huang, Yang Zhou, Huaizu Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.28923v1.pdf)  
  Keywords: autoregressive, distillation, dynamics, evaluation, streaming, video diffusion, video generation  
- **[The Past Frames the Future: Memory for Autoregressive Video Generation](https://arxiv.org/abs/2609.28466v1)**  
  Authors: Harold Haodong Chen, Rongjin Guo, Disen Lan, Wen-Jie Shu, Hongfei Zhang, Hanzhe Hu, Shengtao Yao, Zixin Zhang, Guibin Zhang, Zhefan Rao, Jinxiu Liu, Yexin Liu, Rui Peng, Yuhao Liu, Bin Ren, Shuai Yang, Yukang Chen, Salman Khan, Ying-Cong Chen, Ser-Nam Lim, Rynson W. H. Lau, Nicu Sebe, Yu Cheng, Ming-Hsuan Yang, Qifeng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.28466v1.pdf)  
  Keywords: autoregressive, autoregressive video, evaluation, interactive, physical, video generation  
- **[QuantWM: Temporally Consistent 2-Bit KV Cache Quantization for World Models and Video Generation](https://arxiv.org/abs/2609.26425v2)**  
  Authors: Jiaqi Zhao, Xiaobin Hu, Bo Yin, Junpeng Jiang, Miao Zhang, Shuicheng Yan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.26425v2.pdf)  
  Keywords: efficient, game, temporal consistency, video generation  
- **[Qwen3.8-Omni: Towards Native Omni-Modal Agents](https://arxiv.org/abs/2609.25611v1)**  
  Authors: Qwen Team  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.25611v1.pdf)  
  Keywords: architecture, long-form, music video, video editing, video translation  
- **[WorldCrafter: Consistent Video World Model with Implicit 3D-aware Memory](https://arxiv.org/abs/2609.24984v1)**  
  Authors: Wangbo Yu, Kunhao Liu, Wenbo Hu, Shenghai Yuan, Chaoran Feng, Haiyang Zhou, Yukun Huang, Yiran Wang, Wang Zhao, Yingmin Luo, Ying Shan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.24984v1.pdf)  
  Keywords: 3d-aware, camera control, denoising, distillation, interactive, streaming, video world model, world model  
- **[Streaming Video Editing with Easy Adaptation](https://arxiv.org/abs/2609.24788v1)**  
  Authors: Yujia Hu, Jiajun Li, Zihao He, Songhua Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.24788v1.pdf) | [![GitHub](https://img.shields.io/github/stars/YujiaHu1109/SVEET?style=social)](https://github.com/YujiaHu1109/SVEET)  
  Keywords: acceleration, controllable, diffusion model, streaming, video diffusion, video editing, video generation, video to video, video-to-video  
- **[Edit-VAR: Taming Visual Autoregressive Model for Precise Video Editing](https://arxiv.org/abs/2609.21268v1)**  
  Authors: Chongbo Zhao, Jiangming Wang, Xilai Wang, Xinyu Wang, Jingyi Tang, Chunjie Hao, Pengjie Song, Yue Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.21268v1.pdf)  
  Keywords: autoregressive, autoregressive video, text-guided video editing, trajectory, video editing  
- **[Recency Forcing: Bridging the Long-Horizon Gap in Autoregressive Video Generation](https://arxiv.org/abs/2609.19729v1)**  
  Authors: Tri Cao, Hung Nguyen, Phong Nguyen, Khoi Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.19729v1.pdf)  
  Keywords: autoregressive, autoregressive video, denoising, video generation  
- **[StrucPhysVideo: Learning Physical Dynamics from Structured Captions and Robot Actions](https://arxiv.org/abs/2609.18430v1)**  
  Authors: Awomo-WM Team, :, Enhui Ma, Kaiwen Guo, Tingrui Zhang, Wei Song, Yingshui Tan, Jianhua Xu, Tong Zhang, Kaicheng Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.18430v1.pdf)  
  Keywords: action-conditioned, autoregressive, camera motion, denoising, distillation, dynamics, embodied, image to video, image-to-video, interactive, physical, physics, video prediction, video world model, world model  
- **[PhysStream: Streaming Physics-Grounded Video Generation with Structured Scene Memory and Fine-Grained Motion Control](https://arxiv.org/abs/2609.17521v2)**  
  Authors: Chuhao Chen, Peter Wonka, Chaoyang Wang, Chen Wang, Qiao Feng, Sergey Tulyakov, Lingjie Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.17521v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://czzzzh.github.io/PhysStream)  
  Keywords: autoregressive, controllable, dynamics, image to video, image-to-video, interactive, motion control, physical, physical consistency, physics, streaming, trajectory, video generation, video synthesis  

### Personalization & Customization

*Showing the latest 50 out of 180 papers*

- **[VideoGen-Agent: Reinforcing Video Generation Agents](https://arxiv.org/abs/2609.24997v1)**  
  Authors: Binxu Li, Haoyi Duan, Yuhui Zhang, Yaohui Zhang, Zihao Lin, Kaituo Feng, Suozhi Huang, Xiangyi Li, Yu Li, Chunyuan Li, Shilong Liu, Mengdi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.24997v1.pdf)  
  Keywords: benchmark, identity, physical, physical consistency, text to video, text-to-video, video generation  
- **[OmniVBench: A Benchmark and Large-Scale Dataset for Omni Reference-to-Video Generation](https://arxiv.org/abs/2609.22069v1)**  
  Authors: Wenxue Li, Peiyan Guan, Haoyang Jiang, Junxian Cai, Hualuo Liu, Chunjie Zhang, Chong Guan, Kai Huang, Songlian Li, Taiyi Wu, Yongjian Yu, Xiaotong Zhao, Alan Zhao, Eric Liu, Xi Chen, Yu Liu, Lei Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.22069v1.pdf)  
  Keywords: benchmark, evaluation, style, video generation  
- **[OmniVChat: Synthesizing, Benchmarking, and Training for Native Audio-Visual Dialogue](https://arxiv.org/abs/2609.21465v1)**  
  Authors: Haolin He, Yunfei Chu, Qi Chen, Wen Huang, Yuan Feng, Muzhi Zhu, Zheqi Dai, Haoning Xu, Dongchao Yang, Chunyat Wu, Zining Liang, Zhengxi Liu, Xiquan Li, Xie Chen, Xize Cheng, Qize Yang, Jin Xu, Qiuqiang Kong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.21465v1.pdf)  
  Keywords: benchmark, evaluation, style, video generation  
- **[CompAdapt: Adaptable Composite Motion Modeling for Physics-Consistent Text-to-Video Generation](https://arxiv.org/abs/2609.21455v2)**  
  Authors: Haoran Qin, Renlong Wu, Tianyu Huang, Yukang Ding, Hui Li, Wangmeng Zuo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.21455v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://makapic.github.io/CompAdapt)  
  Keywords: dynamics, dynamics-aware, one-shot, physical, physical consistency, physical plausibility, physics, physics-aware, t2v, text to video, text-to-video, video generation  
- **[LynnReal-Omni: Native multi-modal Video Generation for Agentic Visual Workflows](https://arxiv.org/abs/2609.15863v1)**  
  Authors: Xiaofeng Mao, Peijia Lin, Shaohao Rui, Yibo Zhang, Haibin Wan, Weijie Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.15863v1.pdf)  
  Keywords: acceleration, controllable, diffusion transformer, efficient, evaluation, game, long video, multi-modal, reference-guided, streaming, streaming video generation, text to video, text-to-video, video diffusion, video generation, video restoration  
- **[Dynamic Learning Solutions: A System for Personalized Educational Video Generation](https://arxiv.org/abs/2609.14408v1)**  
  Authors: Siddhanth Sridhar, Shreya Chaurasia, Baddela Sai Yaswantha Reddy, Deepak Parmar, Shylaja S S  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.14408v1.pdf)  
  Keywords: education, interactive, multi-modal, style, video generation  
- **[SignMimic: Robust High-Quality Sign Language Motion Generation via Human-Shape-Oblivious Pose Transfer Guidance](https://arxiv.org/abs/2609.14122v2)**  
  Authors: Zhewen He, Junyi Yu, Haomian Huang, Zhenhua Li, Yi Fang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.14122v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://anonymous.4open.science/r/UniSignMimicTurbo-6088)  
  Keywords: driving, identity, style, temporal consistency, video diffusion  
- **[Vidu S2: Real-Time Interactive, Editable, and Spatial Video Generation](https://arxiv.org/abs/2609.11638v1)**  
  Authors: Jintao Zhang, Kai Jiang, Jintao Chen, Xu Wang, Deyuan Liu, Jungang Li, Dechuang Chen, Ming Lin, Jingjiang Zhou, Haopeng Jin, Qi Jia, Xiaohang Wang, Yaole Wang, Zhanqiang Zhang, Ran Li, Zhengkun Huang, Shuyue Xiong, Yuji Wang, Zikun Dai, Hui He, Yang Luo, Mang Ning, Weiqi Feng, Chengyang Ye, Xinyue Lin, Min Zhao, Hongzhou Zhu, Hengkai Tan, Zeyuan Wang, Chendong Xiang, Kaiwen Zheng, Zhijie Deng, Fan Bao, Jianfei Chen, Jun Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.11638v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vidu.com/vidu-stream)  
  Keywords: avatar, interactive, style, video editing, video generation  
- **[Harnessing Intrinsic Subject-Aware Attention for Controllable Multi-Subject Video Generation](https://arxiv.org/abs/2609.11507v1)**  
  Authors: Niange Yu, Ye Tian, Biaolong Chen, Miao Lu, Aixi Zhang, Hao Jiang, Yunhai Tong, Pipei Huang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.11507v1.pdf)  
  Keywords: benchmark, controllable, identity, video generation  
- **[Decoupled Self-Forcing Distillation for Streaming Talking Head Generation](https://arxiv.org/abs/2609.10317v1)**  
  Authors: Yanru An, Ruiyan Wang, Wenwu Wei, Rui Bu, Qi Wang, Hongwei Hu, Zhengxue Cheng, Rong Xie, Li Song, Wenjun Zhang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.10317v1.pdf)  
  Keywords: autoregressive, diffusion model, distillation, driving, identity, streaming, talking head, video diffusion  

### Physical Understanding

*Showing the latest 50 out of 314 papers*

- **[AV-GRPO: Modality-Anchored Decoupling Diffusion Reinforcement Learning for Joint Audio-Video Generation](https://arxiv.org/abs/2609.29816v1)**  
  Authors: Zhiyu Xu, Weilong Yan, Yufei Shi, Shiyang Li, Yihao Liu, Kin-Man Lam, Yuewen Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.29816v1.pdf) | [![GitHub](https://img.shields.io/github/stars/zhiyuxu03/AV-GRPO?style=social)](https://github.com/zhiyuxu03/AV-GRPO)  
  Keywords: audio-video generation, controllable, dynamics, evaluation, joint audio-video, trajectory, video generation  
- **[ViRDM: Taming Representation Distribution Matching for Few-Step Causal Video Generation](https://arxiv.org/abs/2609.28923v1)**  
  Authors: Zichong Meng, Chongjian Ge, Chun-Hao P. Huang, Yang Zhou, Huaizu Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.28923v1.pdf)  
  Keywords: autoregressive, distillation, dynamics, evaluation, streaming, video diffusion, video generation  
- **[Training Object Permanence in World Models](https://arxiv.org/abs/2609.28654v1)**  
  Authors: Haotian Zhang, Fengyuan Yu, Dezhi Luo, Haoran Sun, Zehong Zhao, Qingying Gao, Yihan Li, Siyuan An, Huayi Qin, Yilan Zhang, Zhengze Jiang, Pinyuan Feng, Renrui Zhang, Ziyu Guo, Letian Wang, Mengyue Yang, Kangfu Mei, Maijunxian Wang, Ran Ji, Vikash Kumar, Freda Shi, Chandra Sripada, Vincent C. Muller, Philip Torr, Alan Yuille, Nikolaus Kriegeskorte, Felix Juefei-Xu, Lvmin Zhang, Jieneng Chen, Yilun Du, Hokin Deng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.28654v1.pdf)  
  Keywords: physical, video generation, world model  
- **[The Past Frames the Future: Memory for Autoregressive Video Generation](https://arxiv.org/abs/2609.28466v1)**  
  Authors: Harold Haodong Chen, Rongjin Guo, Disen Lan, Wen-Jie Shu, Hongfei Zhang, Hanzhe Hu, Shengtao Yao, Zixin Zhang, Guibin Zhang, Zhefan Rao, Jinxiu Liu, Yexin Liu, Rui Peng, Yuhao Liu, Bin Ren, Shuai Yang, Yukang Chen, Salman Khan, Ying-Cong Chen, Ser-Nam Lim, Rynson W. H. Lau, Nicu Sebe, Yu Cheng, Ming-Hsuan Yang, Qifeng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.28466v1.pdf)  
  Keywords: autoregressive, autoregressive video, evaluation, interactive, physical, video generation  
- **[All modalities are equal, but video is more equal: Closing the Cross-Attention Gap in Joint Video Generation](https://arxiv.org/abs/2609.27901v1)**  
  Authors: Ohad Rahamim, Dvir Samuel, Idan Schwartz, Gal Chechik  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.27901v1.pdf)  
  Keywords: body motion, physical, video generation  
- **[Latent evolving World Action Model](https://arxiv.org/abs/2609.27455v2)**  
  Authors: Xueji Fang, Boqiang Duan, Hua Wu, Jingdong Wang, Guo-Jun Qi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.27455v2.pdf)  
  Keywords: architecture, dynamics, video diffusion, video generation  
- **[Code Plans, Diffusion Renders: Open-Ended Generative World Modeling](https://arxiv.org/abs/2609.26458v1)**  
  Authors: Zixun Fang, Yawen Shao, Kai Zhu, Jie Xiao, Shihan Chen, Yu Liu, Xueyang Fu, Yang Cao, Wei Zhai, Zheng-Jun Zha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.26458v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://becauseimbatman0.github.io/CoDeR)  
  Keywords: dynamics, evaluation, video generation  
- **[GameDirector: Decoupling Gameplay Logic from Rendering for Player-Configurable Game World Models](https://arxiv.org/abs/2609.25652v1)**  
  Authors: Zijun Lin, Zhiyang Deng, Yuzhe Wu, Bihan Wen, Yeying Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.25652v1.pdf)  
  Keywords: controllable, dynamics, game, interactive, simulation, video world model, world model  
- **[VideoGen-Agent: Reinforcing Video Generation Agents](https://arxiv.org/abs/2609.24997v1)**  
  Authors: Binxu Li, Haoyi Duan, Yuhui Zhang, Yaohui Zhang, Zihao Lin, Kaituo Feng, Suozhi Huang, Xiangyi Li, Yu Li, Chunyuan Li, Shilong Liu, Mengdi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.24997v1.pdf)  
  Keywords: benchmark, identity, physical, physical consistency, text to video, text-to-video, video generation  
- **[DexTacWAM: A Visuo-Tactile World-Action Model for Dexterous Manipulation](https://arxiv.org/abs/2609.24976v1)**  
  Authors: Haoran Yuan, Zekai Wang, Boning Shao, Haoran Lu, Trevor Darrell, Ismini Lourentzou, Wei Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.24976v1.pdf)  
  Keywords: dynamics, efficient, video diffusion, world model  

### Surveys & Benchmarks

*Showing the latest 50 out of 309 papers*

- **[WanPE: Towards Cinematic Prompt Enhancement for Modern Text-to-Video Generation](https://arxiv.org/abs/2609.30221v1)**  
  Authors: Yubo Zhu, Yawen Shao, Ziyun Dai, Zixun Fang, Kai Zhu, Siyang Sun, Haolan Xue, Chuxin Wang, Tingyu Weng, Jingming Luo, Chen Shi, Lianghua Huang, Yufeng Ai, Yuzheng Wang, Wenyuan Zhang, Yu Shang, Yuxiang Bao, Zoubin Bi, Jie Xiao, Jinbo Xing, Jiaxing Zhao, Chongyang Zhong, Hengjian Chen, Chenwei Xie, Akide Liu, Zhehan Kan, Yu Liu, Wei Zhai, Sheng Zhong, Wei Tong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.30221v1.pdf)  
  Keywords: benchmark, cinematic, sound, text to video, text-to-video, video generation  
- **[Accelerating Video Diffusion via Training-Free Trajectory Routing](https://arxiv.org/abs/2609.30096v1)**  
  Authors: Mustafa Munir, Huy Vu, Shreyas Misra, Rohit Jena, Sajad Norouzi, Ali Taghibakhshi, Anis Ahmad, Anjul Patney, Pavlo Molchanov, Nima Tajbakhsh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.30096v1.pdf)  
  Keywords: acceleration, architecture, denoising, distillation, efficient, evaluation, trajectory, video diffusion  
- **[AV-GRPO: Modality-Anchored Decoupling Diffusion Reinforcement Learning for Joint Audio-Video Generation](https://arxiv.org/abs/2609.29816v1)**  
  Authors: Zhiyu Xu, Weilong Yan, Yufei Shi, Shiyang Li, Yihao Liu, Kin-Man Lam, Yuewen Cao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.29816v1.pdf) | [![GitHub](https://img.shields.io/github/stars/zhiyuxu03/AV-GRPO?style=social)](https://github.com/zhiyuxu03/AV-GRPO)  
  Keywords: audio-video generation, controllable, dynamics, evaluation, joint audio-video, trajectory, video generation  
- **[ViRDM: Taming Representation Distribution Matching for Few-Step Causal Video Generation](https://arxiv.org/abs/2609.28923v1)**  
  Authors: Zichong Meng, Chongjian Ge, Chun-Hao P. Huang, Yang Zhou, Huaizu Jiang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.28923v1.pdf)  
  Keywords: autoregressive, distillation, dynamics, evaluation, streaming, video diffusion, video generation  
- **[The Past Frames the Future: Memory for Autoregressive Video Generation](https://arxiv.org/abs/2609.28466v1)**  
  Authors: Harold Haodong Chen, Rongjin Guo, Disen Lan, Wen-Jie Shu, Hongfei Zhang, Hanzhe Hu, Shengtao Yao, Zixin Zhang, Guibin Zhang, Zhefan Rao, Jinxiu Liu, Yexin Liu, Rui Peng, Yuhao Liu, Bin Ren, Shuai Yang, Yukang Chen, Salman Khan, Ying-Cong Chen, Ser-Nam Lim, Rynson W. H. Lau, Nicu Sebe, Yu Cheng, Ming-Hsuan Yang, Qifeng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.28466v1.pdf)  
  Keywords: autoregressive, autoregressive video, evaluation, interactive, physical, video generation  
- **[LAYERSCOPE: A Layerwise Characterization of Video and Multimodal Learned Representations](https://arxiv.org/abs/2609.28086v2)**  
  Authors: Sandra Arcos-Holzinger, Debashish Chakraborty, Rohita Mocharla, Will Walden, Andrew Yates, Reno Kriz, Sarah M. Erfani, James Bailey, Vishal M. Patel, Sanjeev Khudanpur  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.28086v2.pdf)  
  Keywords: evaluation, text to video, text-to-video  
- **[Don't Read the Log: Execution Traces Contaminate Verifiers in Video-Generation Agents](https://arxiv.org/abs/2609.28564v1)**  
  Authors: Jian Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.28564v1.pdf)  
  Keywords: benchmark, simulation, text to video, text-to-video, video generation  
- **[Code Plans, Diffusion Renders: Open-Ended Generative World Modeling](https://arxiv.org/abs/2609.26458v1)**  
  Authors: Zixun Fang, Yawen Shao, Kai Zhu, Jie Xiao, Shihan Chen, Yu Liu, Xueyang Fu, Yang Cao, Wei Zhai, Zheng-Jun Zha  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.26458v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://becauseimbatman0.github.io/CoDeR)  
  Keywords: dynamics, evaluation, video generation  
- **[VideoGen-Agent: Reinforcing Video Generation Agents](https://arxiv.org/abs/2609.24997v1)**  
  Authors: Binxu Li, Haoyi Duan, Yuhui Zhang, Yaohui Zhang, Zihao Lin, Kaituo Feng, Suozhi Huang, Xiangyi Li, Yu Li, Chunyuan Li, Shilong Liu, Mengdi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.24997v1.pdf)  
  Keywords: benchmark, identity, physical, physical consistency, text to video, text-to-video, video generation  
- **[Generative Tutorial: Towards Live Contextualized Visual Instructions for Physical Tasks](https://arxiv.org/abs/2609.24955v1)**  
  Authors: Muzhe Wu, Zuchen Li, Xu Wang, Anhong Guo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.24955v1.pdf)  
  Keywords: evaluation, physical, video generation  

### Text-to-Video Generation

*Showing the latest 50 out of 148 papers*

- **[WanPE: Towards Cinematic Prompt Enhancement for Modern Text-to-Video Generation](https://arxiv.org/abs/2609.30221v1)**  
  Authors: Yubo Zhu, Yawen Shao, Ziyun Dai, Zixun Fang, Kai Zhu, Siyang Sun, Haolan Xue, Chuxin Wang, Tingyu Weng, Jingming Luo, Chen Shi, Lianghua Huang, Yufeng Ai, Yuzheng Wang, Wenyuan Zhang, Yu Shang, Yuxiang Bao, Zoubin Bi, Jie Xiao, Jinbo Xing, Jiaxing Zhao, Chongyang Zhong, Hengjian Chen, Chenwei Xie, Akide Liu, Zhehan Kan, Yu Liu, Wei Zhai, Sheng Zhong, Wei Tong  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.30221v1.pdf)  
  Keywords: benchmark, cinematic, sound, text to video, text-to-video, video generation  
- **[SALI: Shot-Aware Late Interaction for Cross-Shot Relation Matching in Text-to-Video Retrieval using Film-Grammar Knowledge](https://arxiv.org/abs/2609.29721v1)**  
  Authors: Toya Oyama, Rainer Lienhart, Shin'ichi Satoh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.29721v1.pdf)  
  Keywords: film, text to video, text-to-video  
- **[MotionSpec: Spectral Trajectory Supervision for Motion-Consistent Video Generation](https://arxiv.org/abs/2609.28095v1)**  
  Authors: Ziqi Ni, Rui Li, Shiqi Jiang, Wei Zhou  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.28095v1.pdf)  
  Keywords: text to video, text-to-video, trajectory, video generation  
- **[LAYERSCOPE: A Layerwise Characterization of Video and Multimodal Learned Representations](https://arxiv.org/abs/2609.28086v2)**  
  Authors: Sandra Arcos-Holzinger, Debashish Chakraborty, Rohita Mocharla, Will Walden, Andrew Yates, Reno Kriz, Sarah M. Erfani, James Bailey, Vishal M. Patel, Sanjeev Khudanpur  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.28086v2.pdf)  
  Keywords: evaluation, text to video, text-to-video  
- **[Don't Read the Log: Execution Traces Contaminate Verifiers in Video-Generation Agents](https://arxiv.org/abs/2609.28564v1)**  
  Authors: Jian Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.28564v1.pdf)  
  Keywords: benchmark, simulation, text to video, text-to-video, video generation  
- **[VideoGen-Agent: Reinforcing Video Generation Agents](https://arxiv.org/abs/2609.24997v1)**  
  Authors: Binxu Li, Haoyi Duan, Yuhui Zhang, Yaohui Zhang, Zihao Lin, Kaituo Feng, Suozhi Huang, Xiangyi Li, Yu Li, Chunyuan Li, Shilong Liu, Mengdi Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.24997v1.pdf)  
  Keywords: benchmark, identity, physical, physical consistency, text to video, text-to-video, video generation  
- **[CoaG: Cylinders on a Grid for Coarse 3D Layout Control in Video Generation](https://arxiv.org/abs/2609.24208v2)**  
  Authors: Zhangsihao Yang, Mengyi Shan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.24208v2.pdf)  
  Keywords: layout, text to video, text-to-video, video generation  
- **[Why Do Video Diffusion Models Violate Physics? Unveiling the Flaws in Attention Mechanisms](https://arxiv.org/abs/2609.23658v1)**  
  Authors: Yueyan Li, Haibo Wang, Caixia Yuan, Xiaojie Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.23658v1.pdf)  
  Keywords: denoising, driving, physical, physics, text to video, text-to-video, trajectory, video diffusion  
- **[SparkDiffusion: Mitigating the High-Sparsity Trap --- A Unified Framework for up to $265\times$ Single-GPU Acceleration of Visual Generation](https://arxiv.org/abs/2609.23153v1)**  
  Authors: Yuxi Liu, Haoyu Li, Zekun Zhang, Tengxu Sun, Yixiang Cai, Jiayong Li, Yifei Xia, Tianle Liu, Baole Ai, Ang Wang, Jiamang Wang, Lin Qu, Kai Zhang, Kun Yuan, Bin Cui  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.23153v1.pdf)  
  Keywords: acceleration, architecture, distillation, i2v, t2v, trajectory, video diffusion  
- **[CompAdapt: Adaptable Composite Motion Modeling for Physics-Consistent Text-to-Video Generation](https://arxiv.org/abs/2609.21455v2)**  
  Authors: Haoran Qin, Renlong Wu, Tianyu Huang, Yukang Ding, Hui Li, Wangmeng Zuo  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.21455v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://makapic.github.io/CompAdapt)  
  Keywords: dynamics, dynamics-aware, one-shot, physical, physical consistency, physical plausibility, physics, physics-aware, t2v, text to video, text-to-video, video generation  

### Video Editing

*Showing the latest 50 out of 102 papers*

- **[VideoX-Qwen: Data-Centric Instruction-Based Video Editing](https://arxiv.org/abs/2609.26015v1)**  
  Authors: JJiahang Li, Dingbao Shao, Xinyu Chen, Song Wu, Jiang Lin, Duo Li, Yuhang Liu, Jiaxin Hu, Shengrong Gu, Ying Tai, Zili Yi  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.26015v1.pdf)  
  Keywords: instruction-based video editing, video editing, video generation  
- **[Qwen3.8-Omni: Towards Native Omni-Modal Agents](https://arxiv.org/abs/2609.25611v1)**  
  Authors: Qwen Team  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.25611v1.pdf)  
  Keywords: architecture, long-form, music video, video editing, video translation  
- **[Streaming Video Editing with Easy Adaptation](https://arxiv.org/abs/2609.24788v1)**  
  Authors: Yujia Hu, Jiajun Li, Zihao He, Songhua Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.24788v1.pdf) | [![GitHub](https://img.shields.io/github/stars/YujiaHu1109/SVEET?style=social)](https://github.com/YujiaHu1109/SVEET)  
  Keywords: acceleration, controllable, diffusion model, streaming, video diffusion, video editing, video generation, video to video, video-to-video  
- **[Edit-VAR: Taming Visual Autoregressive Model for Precise Video Editing](https://arxiv.org/abs/2609.21268v1)**  
  Authors: Chongbo Zhao, Jiangming Wang, Xilai Wang, Xinyu Wang, Jingyi Tang, Chunjie Hao, Pengjie Song, Yue Ma  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.21268v1.pdf)  
  Keywords: autoregressive, autoregressive video, text-guided video editing, trajectory, video editing  
- **[Video DeltaNet: A Video-Native Hybrid Attention for Livestream Video Generation](https://arxiv.org/abs/2609.20744v2)**  
  Authors: Haocheng Xi, Yiming Xie, Hexu Zhao, Yiwen Zhang, Michael Liu, Thomas Creavin, Kurt Keutzer, Xiuyu Li, Zhaoyang Lv, Chenfeng Xu, Haiwen Feng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.20744v2.pdf) | [![GitHub](https://img.shields.io/github/stars/OpenVDN/vdn-minimax-h3?style=social)](https://github.com/OpenVDN/vdn-minimax-h3) | [![Project](https://img.shields.io/badge/-Project-blue)](https://huggingface.co/OpenVDN/vdn-minimax-h3) | [![HuggingFace](https://img.shields.io/badge/-HuggingFace-yellow)](https://huggingface.co/OpenVDN/vdn-minimax-h3)  
  Keywords: denoising, distillation, dit, video diffusion, video generation, video to video, video-to-video  
- **[Copy What Is Seen, Generate What Is Not: Training-Free Anomaly-Aware Video Restoration](https://arxiv.org/abs/2609.18836v1)**  
  Authors: Zhida Qu, Shengchao Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.18836v1.pdf)  
  Keywords: video editing, video restoration  
- **[MDN-Control: Mask-Depth-Noise Guided Region Control for Multi-Subject Video Editing](https://arxiv.org/abs/2609.16475v1)**  
  Authors: Jiayi Yu, Xi Ye, Lina Wang, Yunkun Xia  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.16475v1.pdf)  
  Keywords: temporal consistency, video editing  
- **[Unified Agentic Video Editing Across Levels of Complexity and Creativity](https://arxiv.org/abs/2609.12769v1)**  
  Authors: Surabhi S. Nath, Kim Ferres, Milan Petrović, Lion Schulz  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.12769v1.pdf)  
  Keywords: cinematic, creative, video editing  
- **[Vidu S2: Real-Time Interactive, Editable, and Spatial Video Generation](https://arxiv.org/abs/2609.11638v1)**  
  Authors: Jintao Zhang, Kai Jiang, Jintao Chen, Xu Wang, Deyuan Liu, Jungang Li, Dechuang Chen, Ming Lin, Jingjiang Zhou, Haopeng Jin, Qi Jia, Xiaohang Wang, Yaole Wang, Zhanqiang Zhang, Ran Li, Zhengkun Huang, Shuyue Xiong, Yuji Wang, Zikun Dai, Hui He, Yang Luo, Mang Ning, Weiqi Feng, Chengyang Ye, Xinyue Lin, Min Zhao, Hongzhou Zhu, Hengkai Tan, Zeyuan Wang, Chendong Xiang, Kaiwen Zheng, Zhijie Deng, Fan Bao, Jianfei Chen, Jun Zhu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.11638v1.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://vidu.com/vidu-stream)  
  Keywords: avatar, interactive, style, video editing, video generation  
- **[Agentic Visual Generation: From Generative Models to Agentic Control](https://arxiv.org/abs/2609.06758v1)**  
  Authors: Yinming Huang, Shuyuan Tu, Xi Yan, Jiahao Zhan, Zihan Yang, Zhen Xing, Hui Zhang, Tiehua Zhang, Yu-Gang Jiang, Zuxuan Wu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.06758v1.pdf)  
  Keywords: video editing  

### Video Inpainting & Completion

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
- **[SimWAM: A Simple World Action Model for End-to-End Autonomous Driving](https://arxiv.org/abs/2608.07468v4)**  
  Authors: Zongchuang Zhao, Xin Zhou, Tianyang Xu, Zhengyang Sun, Kaixuan Zhou, Yu Wu, Honglin Li, Dingkang Liang, Xiang Bai  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.07468v4.pdf) | [![GitHub](https://img.shields.io/github/stars/H-EmbodVis/SimWAM?style=social)](https://github.com/H-EmbodVis/SimWAM)  
  Keywords: autonomous driving, driving, dynamics, efficient, flow matching, trajectory, video generation, video prediction  
- **[MirrorWorld: Taming Video Diffusion Models for Mirror Reflection Generation](https://arxiv.org/abs/2608.07463v1)**  
  Authors: Youjun Zhao, Alex Warren, Gary K. L. Tam, Rynson W. H. Lau  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.07463v1.pdf)  
  Keywords: benchmark, distillation, video diffusion, video inpainting, video synthesis  
- **[UniVVT: A Unified End-to-End Framework for High-Fidelity Video Virtual Try-on](https://arxiv.org/abs/2608.05745v2)**  
  Authors: Yushe Cao, Shikun Feng, Fei Shen, Haikuo Peng, Jianqiang Xia, Yiheng Zhu, Dianxi Shi, Chun Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.05745v2.pdf)  
  Keywords: dynamics, identity, video generation, video inpainting, virtual try-on  
- **[CrossScope: A Role-Asymmetric World Model for Joint Dual-Scope Surgical Video Prediction](https://arxiv.org/abs/2608.03211v1)**  
  Authors: Wanhao Liu, Jinsong Lin, Rulin Zhou, Chi Kit Ng, Wenbin Pan, Zhiqing Tang, Dongyue Li, Liwei Luo, Yanshen Wu, Panshuo Li, Zhiyong Xiong, Huxin Gao, Tamas Haidegger, Hongliang Ren  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2608.03211v1.pdf)  
  Keywords: benchmark, dynamics, video generation, video prediction, world model  

### Video Super-Resolution & Enhancement

*Showing the latest 50 out of 165 papers*

- **[Accelerating Video Diffusion via Training-Free Trajectory Routing](https://arxiv.org/abs/2609.30096v1)**  
  Authors: Mustafa Munir, Huy Vu, Shreyas Misra, Rohit Jena, Sajad Norouzi, Ali Taghibakhshi, Anis Ahmad, Anjul Patney, Pavlo Molchanov, Nima Tajbakhsh  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.30096v1.pdf)  
  Keywords: acceleration, architecture, denoising, distillation, efficient, evaluation, trajectory, video diffusion  
- **[Beyond Future Prediction: Denoising as Generative Adaptation for Robot Control](https://arxiv.org/abs/2609.28339v1)**  
  Authors: Zanyi Wang, Yuheng Lei, Dengyang Jiang, Ping Luo, Mengdi Wang, Zhixuan Liang, Shilong Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.28339v1.pdf)  
  Keywords: denoising, dit, trajectory, video generation  
- **[Information Capacity of Generative Video Compression: Quantifying the Rate-Compute Exchange at Identical Quality](https://arxiv.org/abs/2609.27493v1)**  
  Authors: Cheng Yuan, Jiawei Shao, Xuelong Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.27493v1.pdf)  
  Keywords: architecture, denoising  
- **[WorldCrafter: Consistent Video World Model with Implicit 3D-aware Memory](https://arxiv.org/abs/2609.24984v1)**  
  Authors: Wangbo Yu, Kunhao Liu, Wenbo Hu, Shenghai Yuan, Chaoran Feng, Haiyang Zhou, Yukun Huang, Yiran Wang, Wang Zhao, Yingmin Luo, Ying Shan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.24984v1.pdf)  
  Keywords: 3d-aware, camera control, denoising, distillation, interactive, streaming, video world model, world model  
- **[Why Do Video Diffusion Models Violate Physics? Unveiling the Flaws in Attention Mechanisms](https://arxiv.org/abs/2609.23658v1)**  
  Authors: Yueyan Li, Haibo Wang, Caixia Yuan, Xiaojie Wang  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.23658v1.pdf)  
  Keywords: denoising, driving, physical, physics, text to video, text-to-video, trajectory, video diffusion  
- **[4DGS-Fixer: Generative Sparse-View 4D Gaussian Splatting with Iterative Refinement Guided by Video Diffusion Priors](https://arxiv.org/abs/2609.21176v2)**  
  Authors: Haitao Huang, Shenghao Zhao, Boyuan Tian, Shin-Fang Chng, Songlin Yang, Sheila Lim, Huangying Zhan, Yi Xu, Anyi Rao, Frank Guan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.21176v2.pdf)  
  Keywords: benchmark, diffusion model, video diffusion, video restoration  
- **[Video DeltaNet: A Video-Native Hybrid Attention for Livestream Video Generation](https://arxiv.org/abs/2609.20744v2)**  
  Authors: Haocheng Xi, Yiming Xie, Hexu Zhao, Yiwen Zhang, Michael Liu, Thomas Creavin, Kurt Keutzer, Xiuyu Li, Zhaoyang Lv, Chenfeng Xu, Haiwen Feng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.20744v2.pdf) | [![GitHub](https://img.shields.io/github/stars/OpenVDN/vdn-minimax-h3?style=social)](https://github.com/OpenVDN/vdn-minimax-h3) | [![Project](https://img.shields.io/badge/-Project-blue)](https://huggingface.co/OpenVDN/vdn-minimax-h3) | [![HuggingFace](https://img.shields.io/badge/-HuggingFace-yellow)](https://huggingface.co/OpenVDN/vdn-minimax-h3)  
  Keywords: denoising, distillation, dit, video diffusion, video generation, video to video, video-to-video  
- **[DART: Distillation-Aware Reparameterization for Training-Free LoRA Reuse in Few-Step Video Diffusion Models](https://arxiv.org/abs/2609.20051v1)**  
  Authors: Shihong Li, Juntao Xu, JinCao, Maowen Tang, Jun Huang, Jintao Li  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.20051v1.pdf)  
  Keywords: denoising, distillation, trajectory, video diffusion, video generation  
- **[Recency Forcing: Bridging the Long-Horizon Gap in Autoregressive Video Generation](https://arxiv.org/abs/2609.19729v1)**  
  Authors: Tri Cao, Hung Nguyen, Phong Nguyen, Khoi Nguyen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.19729v1.pdf)  
  Keywords: autoregressive, autoregressive video, denoising, video generation  
- **[Copy What Is Seen, Generate What Is Not: Training-Free Anomaly-Aware Video Restoration](https://arxiv.org/abs/2609.18836v1)**  
  Authors: Zhida Qu, Shengchao Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.18836v1.pdf)  
  Keywords: video editing, video restoration  

### World Models & Simulation

*Showing the latest 50 out of 243 papers*

- **[Training Object Permanence in World Models](https://arxiv.org/abs/2609.28654v1)**  
  Authors: Haotian Zhang, Fengyuan Yu, Dezhi Luo, Haoran Sun, Zehong Zhao, Qingying Gao, Yihan Li, Siyuan An, Huayi Qin, Yilan Zhang, Zhengze Jiang, Pinyuan Feng, Renrui Zhang, Ziyu Guo, Letian Wang, Mengyue Yang, Kangfu Mei, Maijunxian Wang, Ran Ji, Vikash Kumar, Freda Shi, Chandra Sripada, Vincent C. Muller, Philip Torr, Alan Yuille, Nikolaus Kriegeskorte, Felix Juefei-Xu, Lvmin Zhang, Jieneng Chen, Yilun Du, Hokin Deng  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.28654v1.pdf)  
  Keywords: physical, video generation, world model  
- **[The Past Frames the Future: Memory for Autoregressive Video Generation](https://arxiv.org/abs/2609.28466v1)**  
  Authors: Harold Haodong Chen, Rongjin Guo, Disen Lan, Wen-Jie Shu, Hongfei Zhang, Hanzhe Hu, Shengtao Yao, Zixin Zhang, Guibin Zhang, Zhefan Rao, Jinxiu Liu, Yexin Liu, Rui Peng, Yuhao Liu, Bin Ren, Shuai Yang, Yukang Chen, Salman Khan, Ying-Cong Chen, Ser-Nam Lim, Rynson W. H. Lau, Nicu Sebe, Yu Cheng, Ming-Hsuan Yang, Qifeng Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.28466v1.pdf)  
  Keywords: autoregressive, autoregressive video, evaluation, interactive, physical, video generation  
- **[Don't Read the Log: Execution Traces Contaminate Verifiers in Video-Generation Agents](https://arxiv.org/abs/2609.28564v1)**  
  Authors: Jian Xu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.28564v1.pdf)  
  Keywords: benchmark, simulation, text to video, text-to-video, video generation  
- **[GameDirector: Decoupling Gameplay Logic from Rendering for Player-Configurable Game World Models](https://arxiv.org/abs/2609.25652v1)**  
  Authors: Zijun Lin, Zhiyang Deng, Yuzhe Wu, Bihan Wen, Yeying Jin  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.25652v1.pdf)  
  Keywords: controllable, dynamics, game, interactive, simulation, video world model, world model  
- **[WorldCrafter: Consistent Video World Model with Implicit 3D-aware Memory](https://arxiv.org/abs/2609.24984v1)**  
  Authors: Wangbo Yu, Kunhao Liu, Wenbo Hu, Shenghai Yuan, Chaoran Feng, Haiyang Zhou, Yukun Huang, Yiran Wang, Wang Zhao, Yingmin Luo, Ying Shan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.24984v1.pdf)  
  Keywords: 3d-aware, camera control, denoising, distillation, interactive, streaming, video world model, world model  
- **[DexTacWAM: A Visuo-Tactile World-Action Model for Dexterous Manipulation](https://arxiv.org/abs/2609.24976v1)**  
  Authors: Haoran Yuan, Zekai Wang, Boning Shao, Haoran Lu, Trevor Darrell, Ismini Lourentzou, Wei Zhan  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.24976v1.pdf)  
  Keywords: dynamics, efficient, video diffusion, world model  
- **[Omni Demand Understanding: A Benchmark for Contextual User-Intent Inference in Multimodal Interaction](https://arxiv.org/abs/2609.21392v1)**  
  Authors: Qi Chen, Yunfei Chu, Haolin He, Yifan Yang, Zihan Liu, Yuxuan Wang, Ziyang Ma, Ruiyang Xu, Meng Gao, Yinsong Yan, Ling Wang, Hui Wang, Wen Huang, Yiheng Chen, Guanrou Yang, Qiuqiang Kong, Jin Xu, Xie Chen  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.21392v1.pdf)  
  Keywords: benchmark, evaluation, interactive, video generation  
- **[Astronex-World 1.0: Real-Time Interactive World Model Foundation](https://arxiv.org/abs/2609.20034v1)**  
  Authors: Xin Zhou, Cong Miao  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.20034v1.pdf)  
  Keywords: autonomous driving, controllable, driving, dynamics, embodied, image to video, image-to-video, interactive, text to video, text-to-video, video world model, world model  
- **[StrucPhysVideo: Learning Physical Dynamics from Structured Captions and Robot Actions](https://arxiv.org/abs/2609.18430v1)**  
  Authors: Awomo-WM Team, :, Enhui Ma, Kaiwen Guo, Tingrui Zhang, Wei Song, Yingshui Tan, Jianhua Xu, Tong Zhang, Kaicheng Yu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.18430v1.pdf)  
  Keywords: action-conditioned, autoregressive, camera motion, denoising, distillation, dynamics, embodied, image to video, image-to-video, interactive, physical, physics, video prediction, video world model, world model  
- **[PhysStream: Streaming Physics-Grounded Video Generation with Structured Scene Memory and Fine-Grained Motion Control](https://arxiv.org/abs/2609.17521v2)**  
  Authors: Chuhao Chen, Peter Wonka, Chaoyang Wang, Chen Wang, Qiao Feng, Sergey Tulyakov, Lingjie Liu  
  Links: [![PDF](https://img.shields.io/badge/PDF-arXiv-b31b1b.svg)](https://arxiv.org/pdf/2609.17521v2.pdf) | [![Project](https://img.shields.io/badge/-Project-blue)](https://czzzzh.github.io/PhysStream)  
  Keywords: autoregressive, controllable, dynamics, image to video, image-to-video, interactive, motion control, physical, physical consistency, physics, streaming, trajectory, video generation, video synthesis  



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
