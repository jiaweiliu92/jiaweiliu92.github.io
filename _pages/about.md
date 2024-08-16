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
- `ACM MM 2021` [Cluster and Scatter: A Multi-grained Active Semi-supervised Learning Framework for Scalable Person Re-identification](https://dl.acm.org/doi/abs/10.1145/3474085.3475435), Bingyu Hu, Zheng-Jun Zha, **Jiawei Liu**, Xierong Zhu, Hongtao Xie
- ``ACM MM 2021`` [Pose-Guided Feature Learning with Knowledge Distillation for Occluded Person Re-Identification](https://dl.acm.org/doi/abs/10.1145/3474085.3475610), Kecheng Zheng, Cuiling Lan, Wenjun Zeng, **Jiawei Liu**, Zhizheng Zhang, Zheng-Jun Zha
- ``ICME 2021`` [Adversarial Disentanglement and Correlation Network for Rgb-Infrared Person Re-Identification](https://ieeexplore.ieee.org/abstract/document/9428376), Bingyu Hu, **Jiawei Liu**, Zheng-jun Zha
- ``IJCAI 2021`` [Multi-Scale Spatial-Temporal Integration Convolutional Tube for Human Action Recognition](https://www.ijcai.org/Proceedings/2020/0105.pdf), Haoze Wu, **Jiawei Liu**, Xierong Zhu, Meng Wang, Zheng-Jun Zha
- ``CVPR 2021`` [Spatial-Temporal Correlation and Topology Learning for Person Re-Identification in Videos](https://openaccess.thecvf.com/content/CVPR2021/html/Liu_Spatial-Temporal_Correlation_and_Topology_Learning_for_Person_Re-Identification_in_Videos_CVPR_2021_paper.html), **Jiawei Liu**, Zheng-Jun Zha, Wei Wu, Kecheng Zheng, Qibin Sun
- ``ACM MM 2020`` [Dual Context-Aware Refinement Network for Person Search](https://static.aminer.cn/storage/pdf/acm/20/mm/10.1145/3394171.3413878.pdf), **Jiawei Liu**, Zheng-Jun Zha, Richang Hong, Meng Wang, Yongdong Zhang
- `ACM MM 2020` [ASTA-Net: Adaptive Spatio-Temporal Attention Network for Person Re-Identification in Videos](https://dl.acm.org/doi/abs/10.1145/3394171.3413843), Xierong Zhu, **Jiawei Liu**, Haoze Wu, Meng Wang, Zheng-Jun Zha
- ``ACM MM 2020`` [A Structured Graph Attention Network for Vehicle Re-Identification](https://dl.acm.org/doi/abs/10.1145/3394171.3413607), Yangchun Zhu, Zheng-Jun Zha, Tianzhu Zhang, **Jiawei Liu**, Jiebo Luo
- ``ACM MM 2020`` [Hierarchical Gumbel Attention Network for Text-based Person Search](https://dl.acm.org/doi/10.1145/3394171.3413864), Kecheng Zheng, Wu Liu, **Jiawei Liu**, Zheng-Jun Zha, Tao Mei
- ``ARXIV 2020`` [Temporal Attribute-Appearance Learning Network for Video-based Person Re-Identification](https://arxiv.org/pdf/2009.04181), **Jiawei Liu**, Xierong Zhu, Zheng-Jun Zha
- ``IJCAI 2020`` [Co-Saliency Spatio-Temporal Interaction Network for Person Re-Identification in Videos](https://www.ijcai.org/proceedings/2020/0141.pdf), **Jiawei Liu**, Zheng-Jun Zha, Xierong Zhu, Na Jiang
- ``IEEE TMM 2020`` [Adversarial Attribute-Text Embedding for Person Search With Natural Language Query](https://ieeexplore.ieee.org/abstract/document/8985326), Zheng-Jun Zha, **Jiawei Liu**, Di Chen, Feng Wu
- ``ACM MM 2019`` [Deep Adversarial Graph Attention Convolution Network for Text-Based Person Search](https://dl.acm.org/doi/abs/10.1145/3343031.3350991), **Jiawei Liu**, Zheng-Jun Zha, Richang Hong, Meng Wang, Yongdong Zhang
- ``IJCAI 2019`` [Mutually Reinforced Spatio-Temporal Convolutional Tube for Human Action Recognition](https://www.ijcai.org/proceedings/2019/136), Haoze Wu, **Jiawei Liu**, Zheng-Jun Zha, Zhenzhong Chen, Xiaoyan Sun
- ``ACM TOMM 2019`` [Dense 3D-Convolutional Neural Network for Person Re-Identification in Videos](https://dl.acm.org/doi/abs/10.1145/3231741), **Jiawei Liu**, Zheng-Jun Zha, Xuejin Chen, Zilei Wang, Yongdong Zhang
- ``MMM 2019`` [Adaptive Alignment Network for Person Re-identification](https://link.springer.com/chapter/10.1007/978-3-030-05716-9_2), Xierong Zhu, **Jiawei Liu**, Hongtao Xie, Zheng-Jun Zha
- ``CVPR 2019`` [Adaptive Transfer Network for Cross-Domain Person Re-Identification](https://openaccess.thecvf.com/content_CVPR_2019/html/Liu_Adaptive_Transfer_Network_for_Cross-Domain_Person_Re-Identification_CVPR_2019_paper.html), **Jiawei Liu**, Zheng-Jun Zha, Di Chen, Richang Hong, Meng Wang
- ``ACM MM 2018`` [CA3Net: Contextual-Attentional Attribute-Appearance Network for Person Re-Identification](https://dl.acm.org/doi/abs/10.1145/3240508.3240585), **Jiawei Liu**, Zheng-Jun Zha, Hongtao Xie, Zhiwei Xiong, Yongdong Zhang
- ``ACM MM Asia 2018`` [Temporal-Contextual Attention Network for Video-Based Person Re-identification](https://link.springer.com/chapter/10.1007/978-3-030-00776-8_14), Di Chen, Zheng-Jun Zha, **Jiawei Liu**, Hongtao Xie, Yongdong Zhang
- ``ACM MM 2016`` [Multi-Scale Triplet CNN for Person Re-Identification](https://dl.acm.org/doi/abs/10.1145/2964284.2967209), **Jiawei Liu**, Zheng-Jun Zha, QI Tian, Dong Liu, Ting Yao, Qiang Ling, Tao Mei


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

## 🧑‍🎨 Large Vision-Language Model
- `ARXIV 2024` [TagAlign: Improving Vision-Language Alignment with Multi-Tag Classification](https://arxiv.org/abs/2312.14149), Qinying Liu, Wei Wu, Kecheng Zheng, Zhan Tong, **Jiawei Liu**, Yu Liu, Wei Chen, Zilei Wang, Yujun Shen \| [**Project**](https://qinying-liu.github.io/Tag-Align/) [![](https://img.shields.io/github/stars/Qinying-Liu/TagAlign?style=social&label=Code+Stars)](https://github.com/Qinying-Liu/TagAlign)
- ``ICCV 2023`` [Regularized Mask Tuning: Uncovering Hidden Knowledge in Pre-trained Vision-Language Models](https://openaccess.thecvf.com/content/ICCV2023/papers/Zheng_Regularized_Mask_Tuning_Uncovering_Hidden_Knowledge_in_Pre-Trained_Vision-Language_Models_ICCV_2023_paper.pdf), Kecheng Zheng, Wei Wu, Ruili Feng, Kai Zhu, **Jiawei Liu**, Deli Zhao, Zheng-Jun Zha, Wei Chen, Yujun Shen

## 🎙 Others
- ``PAIN 2023`` [Deep Learning–guided Postoperative Pain Assessment in Children](https://journals.lww.com/pain/fulltext/2023/09000/deep_learning_guided_postoperative_pain_assessment.16.aspx), Jihong Fang, Wei Wu, **Jiawei Liu**, Sicheng Zhang
- ``ACM TOMM 2019`` [Spatiotemporal-Textual Co-Attention Network for Video Question Answering](https://dl.acm.org/doi/abs/10.1145/3320061), Zheng-Jun Zha, **Jiawei Liu**, Tianhao Yang, Yongdong Zhang

# 💬 Chinese Patents
- *2021.06*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet. 
- *2021.03*, Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus ornare aliquet ipsum, ac tempus justo dapibus sit amet.  \| [\[video\]](https://github.com/)

# 🎖 Honors and Awards
- *2024.7* ACM MM2024 Workshop: Micro-Action Analysis Grand Challenge ([1st Place Award](https://sites.google.com/view/micro-action/challenge/winners))
- *2023.3* AAAI2023 Workshop: Defactify 2: Multimodal Fake News Detection ([4th Place Award](https://aiisc.ai/defactify2/))
- *2022.1* Mozi Distinguished Youth Special Allowance of USTC
- *2020.1* Special Research Assistantship of CAS
- *2019.6* CAS Presidential Scholarship
- *2019.6* Outstanding Graduates Scholarship, USTC
- *2018.9* Individual Scholarship, USTC
- *2016.9* Individual Scholarship, USTC

# 📖 Experiences
- *2021.12 - Present*, Associate Research Fellow, USTC, Collaborating with Prof. Zheng-Jun Zha
- *2019.10 - 2021.11*, Postdocral Research Fellow, USTC, Collaborating with Prof. Zheng-Jun Zha and Prof. Yongdong Zhang
- *2019.8 - 2019.10*, Researcher, <span style="color:red">JD AILab</span>, working with Prof. Tao Mei and Prof. Wu Liu
- *2016.10 - 2017.1*, Research Intern, <span style="color:red">MSRA</span>, under the supervision of Prof. Tao Mei
- *2014.9 - 2019.6*, **Ph.D** in the Department of Automation, University of Science and Technology of China
- *2009.8 - 2013.6*, **B.S.** in the Department of Automation, Hefei University of Technology

# 💻 Internships
- *2019.05 - 2020.02*, [Lorem](https://github.com/), China.
