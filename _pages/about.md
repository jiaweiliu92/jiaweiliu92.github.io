---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

Jiawei Liu is currently an associate research fellow with the Department of Automation, University of Science and Technology of China (中国科学技术大学), working with Prof. Zheng-Jun Zha at [Multimodal Intelligence Lab (多模态智能实验室)](https://zhas-group.pages.dev/).

I received the B.S. degree from the Hefei University of Technology (HFUT) in 2013, and the Ph.D. degree from the University of Science and Technology of China (USTC) in 2019, respectively. During my PhD, I worked in MSRA as a research intern, under the supervision of [Prof. Tao Mei](https://taomei.me/) from Oct. 2016 to Jan. 2017. My research interests span Computer Vision, Multimeida Analysis and Deep Learning, including Human-Centric Visual Understanding, Fake Media Content Analysis, Large Vision-Language Model, <em>etc</em>. I have published 40+ papers at the top international AI journals and conferences. 

I am currently looking for highly motivated graduate students who are passionate about computer vision, deep learning, and related fields. If you have a strong academic background in mathematics, machine learning, or programming and are eager to engage in innovative research, I warmly invite you to apply to join my research group. Furthermore, if you are interested in exploring opportunities for **academic collaboration**, please do not hesitate to contact me at [jwliu6@ustc.edu.cn](mailto:jwliu6@ustc.edu.cn).

# 🔥 News
- *2024.08*: &nbsp;🎉🎉 One paper is accepted by ECCV 2024. 
- *2024.04*: &nbsp;🎉🎉 One paper is accepted by ICME 2024. 

# 📝 Publications 

## 📚 Human-Centric Visual Understanding 
- ``IJCV 2024`` [Exert Diversity and Mitigate Bias: Domain Generalizable Person Re-identification with a Comprehensive Benchmark](https://link.springer.com/article/10.1007/s11263-024-02124-5), Bingyu Hu, **Jiawei Liu**, Yufei Zheng, Kecheng Zheng, Zheng-Jun Zha
- `MMM 2024` [Cross-Modal Semantic Alignment Learning for Text-Based Person Search](https://link.springer.com/chapter/10.1007/978-3-031-53305-1_16), Wenjun Gan, **Jiawei Liu**, Yangchun Zhu, Yong Wu, Guozhi Zhao, Zheng-Jun Zha
- ``IEEE TMM 2023`` [Unleashing Knowledge Potential of Source Hypothesis for Source-Free Domain Adaptation](https://ieeexplore.ieee.org/abstract/document/10319072), Bingyu Hu, **Jiawei Liu**, Kecheng Zheng, Zheng-Jun Zha
- ``AAAI 2022`` [Debiased Batch Normalization via Gaussian Process for Generalizable Person Re-identification](https://ojs.aaai.org/index.php/AAAI/article/view/20065), **Jiawei Liu**, Zhipeng Huang, Liang Li, Kecheng Zheng, Zheng-Jun Zha
- ``AAAI 2022`` [Modality-Adaptive Mixup and Invariant Decomposition for RGB-Infrared Person Re-identification](https://ojs.aaai.org/index.php/AAAI/article/view/19987), Zhipeng Huang, **Jiawei Liu**, Liang Li, Kecheng Zheng, Zheng-Jun Zha
- ``CVPR 2022`` [Temporal Complementarity-Guided Reinforcement Learning for Image-to-Video Person Re-Identification](https://openaccess.thecvf.com/content/CVPR2022/papers/Wu_Temporal_Complementarity-Guided_Reinforcement_Learning_for_Image-to-Video_Person_Re-Identification_CVPR_2022_paper.pdf), Wei Wu, **Jiawei Liu**, Kecheng Zheng, Qibin Sun, Zheng-Jun Zha
- ``ARXIV 2021`` [Calibrated Feature Decomposition for Generalizable Person Re-Identification](https://arxiv.org/pdf/2111.13945), Kecheng Zheng, **Jiawei Liu**, Wei Wu, Liang Li, Zheng-jun Zha

## 🎙 Fake Media Content Analysis
- `IJCAI 2024` [Natural Language-centered Inference Network for Multi-modal Fake News Detection](https://www.ijcai.org/proceedings/2024/281), Qiang Zhang, **Jiawei Liu**, Fanrui Zhang, Jingyi Xie, Zheng-Jun Zha
- ``WWW 2024`` [ESCNet: Entity-enhanced and Stance Checking Network for Multi-modal Fact-Checking](https://dl.acm.org/doi/abs/10.1145/3589334.3645455), Fanrui Zhang, **Jiawei Liu**, Jingyi Xie, Qiang Zhang, Yongchao Xu, Zheng-Jun Zha
- ``IEEE TIFS 2023`` [Adaptive Texture and Spectrum Clue Mining for Generalizable Face Forgery Detection](https://ieeexplore.ieee.org/abstract/document/10364845), **Jiawei Liu**, Jingyi Xie, Yang Wang, Zheng-Jun Zha
- ``ACM MM 2023`` [Hierarchical Semantic Enhancement Network for Multimodal Fake News Detection](https://dl.acm.org/doi/abs/10.1145/3581783.3612423), Qiang Zhang, **Jiawei Liu**, Fanrui Zhang, Jingyi Xie, Zheng-Jun Zha
- ``ACM MM 2023`` [ECENet: Explainable and Context-Enhanced Network for Muti-modal Fact verification](https://dl.acm.org/doi/abs/10.1145/3581783.3612183), Fanrui Zhang, **Jiawei Liu**, Qiang Zhang, Esther Sun, Jingyi Xie, Zheng-Jun Zha
- ``ARXIV 2023`` [Knowledge-enhanced Hierarchical Information Correlation Learning for Multi-modal Rumor Detection](https://arxiv.org/abs/2306.15946), **Jiawei Liu**, Jingyi Xie, Fanrui Zhang, Qiang Zhang, Zheng-jun Zha
- `De-Factify2 2023` [Unimodal Feature-Enhanced and Cross-Modal Correlation Learning for Multi-Modal Fact Verification](https://ceur-ws.org/Vol-3555/paper16.pdf), Fanrui Zhang, Qiang Zhang, **Jiawei Liu Liu**, Sun Esther
- `CVPR 2023` [Edge-Aware Regional Message Passing Controller for Image Forgery Localization](https://openaccess.thecvf.com/content/CVPR2023/html/Li_Edge-Aware_Regional_Message_Passing_Controller_for_Image_Forgery_Localization_CVPR_2023_paper.html), Dong Li, Jiaying Zhu, Menglu Wang, **Jiawei Liu**, Xueyang Fu, Zheng-Jun Zha
- `ACM MM 2022` [JPEG Compression-aware Image Forgery Localization](https://dl.acm.org/doi/abs/10.1145/3503161.3547749), Menglu Wang, Xueyang Fu, **Jiawei Liu**, Zheng-Jun Zha
- `ARXIV 2022` [Label Noise-Resistant Mean Teaching for Weakly Supervised Fake News Detection](https://arxiv.org/abs/2206.12260), Jingyi Xie, **Jiawei Liu**, Zheng-Jun Zha
- `NeurIPS 2022` [GenerSpeech: Towards Style Transfer for Generalizable Out-Of-Domain Text-to-Speech](), Rongjie Huang, **Yi Ren**, et al.

## 🧑‍🎨 Large Vision-Language Model
- `ARXIV 2024` [TagAlign: Improving Vision-Language Alignment with Multi-Tag Classification](https://arxiv.org/abs/2312.14149), Qinying Liu, Wei Wu, Kecheng Zheng, Zhan Tong, **Jiawei Liu**, Yu Liu, Wei Chen, Zilei Wang, Yujun Shen \| [**Project**](https://qinying-liu.github.io/Tag-Align/) [![](https://img.shields.io/github/stars/Qinying-Liu/TagAlign?style=social&label=Code+Stars)](https://github.com/Qinying-Liu/TagAlign)
- ``ICCV 2023`` [Regularized mask tuning: Uncovering hidden knowledge in pre-trained vision-language models](https://openaccess.thecvf.com/content/ICCV2023/papers/Zheng_Regularized_Mask_Tuning_Uncovering_Hidden_Knowledge_in_Pre-Trained_Vision-Language_Models_ICCV_2023_paper.pdf), Kecheng Zheng, Wei Wu, Ruili Feng, Kai Zhu, **Jiawei Liu**, Deli Zhao, Zheng-Jun Zha, Wei Chen, Yujun Shen
- ``ACL 2023`` [CLAPSpeech: Learning Prosody from Text Context with Contrastive Language-Audio Pre-Training](), Zhenhui Ye, Rongjie Huang, **Yi Ren**, et al.
- ``ACL 2023`` [FluentSpeech: Stutter-Oriented Automatic Speech Editing with Context-Aware Diffusion Models](), Ziyue Jiang, Qian Yang, Jialong Zuo, Zhenhui Ye, Rongjie Huang, **Yi Ren** and Zhou Zhao
- ``ACL 2023`` [Revisiting and Incorporating GAN and Diffusion Models in High-Fidelity Speech Synthesis](), Rongjie Huang, **Yi Ren**, Ziyue Jiang, et al.
- ``ACL 2023`` [Improving Prosody with Masked Autoencoder and Conditional Diffusion Model For Expressive Text-to-Speech](), Rongjie Huang, Chunlei Zhang, **Yi Ren**, et al.
- `ICLR 2023` [Bag of Tricks for Unsupervised Text-to-Speech](https://openreview.net/forum?id=SbR9mpTuBn), **Yi Ren**, Chen Zhang, Shuicheng Yan
- `INTERSPEECH 2023` [StyleS2ST: zero-shot style transfer for direct speech-to-speech translation](https://arxiv.org/abs/2305.17732), Kun Song, **Yi Ren**, Yi Lei, et al.


## 🎙 Others
- ``PAIN 2023`` [Deep Learning–guided Postoperative Pain Assessment in Children](https://journals.lww.com/pain/fulltext/2023/09000/deep_learning_guided_postoperative_pain_assessment.16.aspx), Jihong Fang, Wei Wu, **Jiawei Liu**, Sicheng Zhang
- ``ACL 2023`` [CLAPSpeech: Learning Prosody from Text Context with Contrastive Language-Audio Pre-Training](), Zhenhui Ye, Rongjie Huang, **Yi Ren**, et al.
- ``ACL 2023`` [FluentSpeech: Stutter-Oriented Automatic Speech Editing with Context-Aware Diffusion Models](), Ziyue Jiang, Qian Yang, Jialong Zuo, Zhenhui Ye, Rongjie Huang, **Yi Ren** and Zhou Zhao
- ``ACL 2023`` [Revisiting and Incorporating GAN and Diffusion Models in High-Fidelity Speech Synthesis](), Rongjie Huang, **Yi Ren**, Ziyue Jiang, et al.
- ``ACL 2023`` [Improving Prosody with Masked Autoencoder and Conditional Diffusion Model For Expressive Text-to-Speech](), Rongjie Huang, Chunlei Zhang, **Yi Ren**, et al.
- `ICLR 2023` [Bag of Tricks for Unsupervised Text-to-Speech](https://openreview.net/forum?id=SbR9mpTuBn), **Yi Ren**, Chen Zhang, Shuicheng Yan


# 🎖 Honors and Awards
- *2021.10* Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2021.09* Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 

# 📖 Educations
- *2019.06 - 2022.04 (now)*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2015.09 - 2019.06*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 

# 💬 Invited Talks
- *2021.06*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2021.03*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.  \| [\[video\]](https://github.com/)

# 💻 Internships
- *2019.05 - 2020.02*, [Lorem](https://github.com/), China.
