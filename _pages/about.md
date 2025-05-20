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

Jiawei Liu (刘嘉威) is currently an associate research fellow with the Department of Automation, University of Science and Technology of China (中国科学技术大学), working with [Prof. Zheng-Jun Zha](https://auto.ustc.edu.cn/2021/0510/c25976a484878/page.htm) at [Multimodal Intelligence Lab (多模态智能实验室)](https://zhas-group.pages.dev/).

I received the B.S. degree from the Hefei University of Technology (HFUT) in 2013, and the Ph.D. degree from the University of Science and Technology of China (USTC) in 2019, respectively. During my PhD, I worked in [MSRA](https://www.msra.cn/) <img src="./images/microsoft.png" style="width: 4.5em;"> as a research intern, under the supervision of [Prof. Tao Mei](https://taomei.me/) from Oct. 2016 to Jan. 2017. My research interests span Computer Vision, Multimeida Analysis and Deep Learning, including Human-Centric Visual Understanding, Fake Media Content Analysis, Large Vision-Language Model, <em>etc</em>. I have published 40+ papers <a href='https://scholar.google.com/citations?user=sR7Sf2YAAAAJ'><img src="https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fjiaweiliu92%2Fjiaweiliu92.github.io@google-scholar-stats%2Fgs_data_shieldsio.json&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a> at the top international AI journals and conferences.

I am currently looking for highly motivated graduate students who are passionate about computer vision, deep learning, and related fields. If you have a strong academic background in mathematics, machine learning, or programming and are eager to engage in innovative research, I warmly invite you to apply to join my research group. Furthermore, if you are interested in exploring opportunities for **academic collaboration**, please do not hesitate to contact me at [jwliu6@ustc.edu.cn](mailto:jwliu6@ustc.edu.cn).

<span class='anchor' id='news'></span>
# 🔥 News
- *2025.04*: &nbsp;🎉🎉 One paper on image forgery detection and localizationn is accepted by <span style="color:skyblue">IJCAI</span> 2025. 
- *2025.02*: &nbsp;🎉🎉 One paper on test-time adaptation is accepted by <span style="color:skyblue">CVPR</span> 2025. 
- *2025.02*: &nbsp;🎉🎉 One paper on comprehensive image captioning is accepted by <span style="color:skyblue">CVPR</span> 2025. 
- *2025.01*: &nbsp;🎉🎉 One paper on person re-identification is accepted by <span style="color:skyblue">TIFS</span> 2025. 
- *2024.12*: &nbsp;🎉🎉 One paper on person re-identification is accepted by <span style="color:skyblue">CVM</span> 2025. 
- *2024.12*: &nbsp;🎉🎉 One paper on human-object interaction is accepted by <span style="color:skyblue">AAAI</span> 2025. 
- *2024.10*: &nbsp;🎉🎉 One paper on person re-identification is accepted by <span style="color:skyblue">ACM TOMM</span> 2024. 
- *2024.08*: &nbsp;🎉🎉 One paper on image forgery localization is accepted by <span style="color:skyblue">ECCV</span> 2024. 
- *2024.04*: &nbsp;🎉🎉 One paper on person re-identification is accepted by <span style="color:skyblue">ICME</span> 2024. 

<span class='anchor' id='publications'></span>
# 📝 Publications

## 📚 Human-Centric Visual Understanding
- ``CVM 2025`` [Multi-granularity and Multi-modal Prompt Learning for Person Re-Identification](https://link.springer.com/chapter/10.1007/978-981-96-5815-2_10), Hao Tong, **Jiawei Liu**, Yong Wu, Guozhi Zhao, Fanrui Zhang, Zheng-Jun Zha
- ``AAAI 2025`` [HOIMamba: Efficient Mamba-based Disentangled Progressive Learning for HOI Detection](https://ojs.aaai.org/index.php/AAAI/article/view/32972), Yongchao Xu, **Jiawei Liu**, Sen Tao, Qiang Zhang, Zheng-Jun Zha
- ``IEEE TIFS 2025`` [Advancing Visible-Infrared Person Re-Identification: Synergizing Visual-Textual Reasoning and Cross-Modal Feature Alignment](https://ieeexplore.ieee.org/document/10879282), Yuxuan Qiu, Liyang Wang, Wei Song, **Jiawei Liu**, Zhiping Shi, Na Jiang
- ``ACM TOMM 2024`` [Noise-Resistance Learning via Multi-Granularity Consistency for Unsupervised Domain Adaptive Person Re-Identification](https://dl.acm.org/doi/10.1145/3702328), Yangchun Zhu, Yufei Zheng, **Jiawei Liu**, Yao Li, Zheng-Jun Zha
- ``ICME 2024`` [Joint Visual-Textual Reasoning and Visible-Infrared Modality Alignment for Person Re-Identification](https://ieeexplore.ieee.org/document/10688362), Na Jiang, Yuxuan Qiu, Wei Song, **Jiawei Liu**, Zhiping Shi, Liyang Wang
- ``IJCV 2024`` [Exert Diversity and Mitigate Bias: Domain Generalizable Person Re-identification with a Comprehensive Benchmark](https://link.springer.com/article/10.1007/s11263-024-02124-5), Bingyu Hu, **Jiawei Liu**, Yufei Zheng, Kecheng Zheng, Zheng-Jun Zha
- `MMM 2024` [Cross-Modal Semantic Alignment Learning for Text-Based Person Search](https://link.springer.com/chapter/10.1007/978-3-031-53305-1_16), Wenjun Gan, **Jiawei Liu**, Yangchun Zhu, Yong Wu, Guozhi Zhao, Zheng-Jun Zha
- ``IEEE TMM 2023`` [Unleashing Knowledge Potential of Source Hypothesis for Source-Free Domain Adaptation](https://ieeexplore.ieee.org/abstract/document/10319072), Bingyu Hu, **Jiawei Liu**, Kecheng Zheng, Zheng-Jun Zha
- ``AAAI 2022`` [Debiased Batch Normalization via Gaussian Process for Generalizable Person Re-identification](https://ojs.aaai.org/index.php/AAAI/article/view/20065), **Jiawei Liu**, Zhipeng Huang, Liang Li, Kecheng Zheng, Zheng-Jun Zha
- ``AAAI 2022`` [Modality-Adaptive Mixup and Invariant Decomposition for RGB-Infrared Person Re-identification](https://ojs.aaai.org/index.php/AAAI/article/view/19987), Zhipeng Huang, **Jiawei Liu**, Liang Li, Kecheng Zheng, Zheng-Jun Zha
- ``CVPR 2022`` [Temporal Complementarity-Guided Reinforcement Learning for Image-to-Video Person Re-Identification](https://openaccess.thecvf.com/content/CVPR2022/papers/Wu_Temporal_Complementarity-Guided_Reinforcement_Learning_for_Image-to-Video_Person_Re-Identification_CVPR_2022_paper.pdf), Wei Wu, **Jiawei Liu**, Kecheng Zheng, Qibin Sun, Zheng-Jun Zha
- ``ARXIV 2021`` [Calibrated Feature Decomposition for Generalizable Person Re-Identification](https://arxiv.org/pdf/2111.13945), Kecheng Zheng, **Jiawei Liu**, Wei Wu, Liang Li, Zheng-Jun Zha [![](https://img.shields.io/github/stars/zkcys001/CFD?style=social&label=Code+Stars)](https://github.com//zkcys001/CFD)
- `ACM MM 2021` [Cluster and Scatter: A Multi-grained Active Semi-supervised Learning Framework for Scalable Person Re-identification](https://dl.acm.org/doi/abs/10.1145/3474085.3475435), Bingyu Hu, Zheng-Jun Zha, **Jiawei Liu**, Xierong Zhu, Hongtao Xie
- ``ACM MM 2021`` [Pose-Guided Feature Learning with Knowledge Distillation for Occluded Person Re-Identification](https://dl.acm.org/doi/abs/10.1145/3474085.3475610), Kecheng Zheng, Cuiling Lan, Wenjun Zeng, **Jiawei Liu**, Zhizheng Zhang, Zheng-Jun Zha
- ``ICME 2021`` [Adversarial Disentanglement and Correlation Network for Rgb-Infrared Person Re-Identification](https://ieeexplore.ieee.org/abstract/document/9428376), Bingyu Hu, **Jiawei Liu**, Zheng-Jun Zha
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
- ``PCM 2018`` [Temporal-Contextual Attention Network for Video-Based Person Re-identification](https://link.springer.com/chapter/10.1007/978-3-030-00776-8_14), Di Chen, Zheng-Jun Zha, **Jiawei Liu**, Hongtao Xie, Yongdong Zhang
- ``ACM MM 2016`` [Multi-Scale Triplet CNN for Person Re-Identification](https://dl.acm.org/doi/abs/10.1145/2964284.2967209), **Jiawei Liu**, Zheng-Jun Zha, QI Tian, Dong Liu, Ting Yao, Qiang Ling, Tao Mei

## 🌱 Fake Media Content Analysis
- `ECCV 2024` [Noise-assisted Prompt Learning for Image Forgery Detection and Localizatio](https://www.ecva.net/papers/eccv_2024/papers_ECCV/papers/01688.pdf), Dong Li, Jiaying Zhu, Xueyang Fu, Xun Guo, Yidi Liu, Gang Yang, **Jiawei Liu**, Zheng-Jun Zha
- `IJCAI 2024` [Natural Language-centered Inference Network for Multi-modal Fake News Detection](https://www.ijcai.org/proceedings/2024/281), Qiang Zhang, **Jiawei Liu**, Fanrui Zhang, Jingyi Xie, Zheng-Jun Zha [![](https://img.shields.io/github/stars/juices6/NLIN?style=social&label=Code+Stars)](https://github.com//juices6/NLIN)
- ``WWW 2024`` [ESCNet: Entity-enhanced and Stance Checking Network for Multi-modal Fact-Checking](https://dl.acm.org/doi/abs/10.1145/3589334.3645455), Fanrui Zhang, **Jiawei Liu**, Jingyi Xie, Qiang Zhang, Yongchao Xu, Zheng-Jun Zha [![](https://img.shields.io/github/stars/zfr00/ESCNet?style=social&label=Code+Stars)](https://github.com//zfr00/ESCNet)
- ``IEEE TIFS 2023`` [Adaptive Texture and Spectrum Clue Mining for Generalizable Face Forgery Detection](https://ieeexplore.ieee.org/abstract/document/10364845), **Jiawei Liu**, Jingyi Xie, Yang Wang, Zheng-Jun Zha
- ``ACM MM 2023`` [Hierarchical Semantic Enhancement Network for Multimodal Fake News Detection](https://dl.acm.org/doi/abs/10.1145/3581783.3612423), Qiang Zhang, **Jiawei Liu**, Fanrui Zhang, Jingyi Xie, Zheng-Jun Zha
- ``ACM MM 2023`` [ECENet: Explainable and Context-Enhanced Network for Muti-modal Fact verification](https://dl.acm.org/doi/abs/10.1145/3581783.3612183), Fanrui Zhang, **Jiawei Liu**, Qiang Zhang, Esther Sun, Jingyi Xie, Zheng-Jun Zha
- ``ARXIV 2023`` [Knowledge-enhanced Hierarchical Information Correlation Learning for Multi-modal Rumor Detection](https://arxiv.org/abs/2306.15946), **Jiawei Liu**, Jingyi Xie, Fanrui Zhang, Qiang Zhang, Zheng-Jun Zha
- `De-Factify2 2023` [Unimodal Feature-Enhanced and Cross-Modal Correlation Learning for Multi-Modal Fact Verification](https://ceur-ws.org/Vol-3555/paper16.pdf), Fanrui Zhang, Qiang Zhang, **Jiawei Liu Liu**, Sun Esther
- `CVPR 2023` [Edge-Aware Regional Message Passing Controller for Image Forgery Localization](https://openaccess.thecvf.com/content/CVPR2023/html/Li_Edge-Aware_Regional_Message_Passing_Controller_for_Image_Forgery_Localization_CVPR_2023_paper.html), Dong Li, Jiaying Zhu, Menglu Wang, **Jiawei Liu**, Xueyang Fu, Zheng-Jun Zha
- `ACM MM 2022` [JPEG Compression-aware Image Forgery Localization](https://dl.acm.org/doi/abs/10.1145/3503161.3547749), Menglu Wang, Xueyang Fu, **Jiawei Liu**, Zheng-Jun Zha
- `ARXIV 2022` [Label Noise-Resistant Mean Teaching for Weakly Supervised Fake News Detection](https://arxiv.org/abs/2206.12260), Jingyi Xie, **Jiawei Liu**, Zheng-Jun Zha

## 🚀 Large Vision-Language Model
- ``CVPR 2025`` [Benchmarking Large Vision-Language Models via Directed Scene Graph](https://arxiv.org/pdf/2412.08614), Fan Lu, Wei Wu, Kecheng Zheng, Shuailei Ma, Biao Gong, **Jiawei Liu**, Wei Zhai, Cao Yang, Yujun Shen, Zheng-Jun Zha \| [**Project**](https://github.com/LuFan31/CompreCap/) [![](https://img.shields.io/github/stars/LuFan31/CompreCap?style=social&label=Code+Stars)](https://github.com/LuFan31/CompreCap)
- `ARXIV 2024` [TagAlign: Improving Vision-Language Alignment with Multi-Tag Classification](https://arxiv.org/abs/2312.14149), Qinying Liu, Wei Wu, Kecheng Zheng, Zhan Tong, **Jiawei Liu**, Yu Liu, Wei Chen, Zilei Wang, Yujun Shen \| [**Project**](https://qinying-liu.github.io/Tag-Align/) [![](https://img.shields.io/github/stars/Qinying-Liu/TagAlign?style=social&label=Code+Stars)](https://github.com/Qinying-Liu/TagAlign)
- ``ICCV 2023`` [Regularized Mask Tuning: Uncovering Hidden Knowledge in Pre-trained Vision-Language Models](https://openaccess.thecvf.com/content/ICCV2023/papers/Zheng_Regularized_Mask_Tuning_Uncovering_Hidden_Knowledge_in_Pre-Trained_Vision-Language_Models_ICCV_2023_paper.pdf), Kecheng Zheng, Wei Wu, Ruili Feng, Kai Zhu, **Jiawei Liu**, Deli Zhao, Zheng-Jun Zha, Wei Chen, Yujun Shen \| [**Project**](https://wuw2019.github.io/R-AMT/) [![](https://img.shields.io/github/stars/wuw2019/R-AMT?style=social&label=Code+Stars)](https://github.com/wuw2019/R-AMT)

## 🎼 Others
- ``PAIN 2023`` [Deep Learning–guided Postoperative Pain Assessment in Children](https://journals.lww.com/pain/fulltext/2023/09000/deep_learning_guided_postoperative_pain_assessment.16.aspx), Jihong Fang, Wei Wu, **Jiawei Liu**, Sicheng Zhang
- ``ACM TOMM 2019`` [Spatiotemporal-Textual Co-Attention Network for Video Question Answering](https://dl.acm.org/doi/abs/10.1145/3320061), Zheng-Jun Zha, **Jiawei Liu**, Tianhao Yang, Yongdong Zhang

<span class='anchor' id='chinese-patents'></span>
# 💬 Chinese Patents
- *2025.03* 查正军; **刘嘉威**; 徐永超. 一种基于Mamba架构的人物交互检测方法. 发明专利. (专利号：CN202510261091.2)
- *2024.10* 查正军; **刘嘉威**; 张凡瑞; 张强. 一种基于实体增强和立场检查的多模态事实核查方法. 发明专利. (专利号：CN202410403673.5)
- *2024.10* **刘嘉威**; 赵国治; 吴勇; 贺强; 胡冰玉. 基于特征多样化和域自适应特征选择的鲁棒行人重识别方法. 发明专利. (专利号：CN202410070798.0)
- *2024.10* **刘嘉威**; 赵国治; 吴勇; 贺强; 甘文君. 一种基于跨模态语义对齐的文本行人重识别方法. 发明专利. (专利号：CN202410072896.8)
- *2023.11* 查正军; **刘嘉威**; 张强; 张凡瑞. 一种基于多层次语义增强的多模态假新闻检测方法. 发明专利. (专利号：CN202311298800.1)
- *2023.10* 查正军; 傅雪阳; 李东; 朱佳莹; **刘嘉威**. 基于边缘感知的区域消息传递控制的图像伪造定位方法. 发明专利. (专利号：CN202310346607.4)
- *2022.10* 查正军; **刘嘉威**; 王堃宇. 一种基于特征对齐的退化环境下的行人重识别方法. 发明专利. (专利号：CN202210792619.5)
- *2022.10* 查正军; **刘嘉威**; 吴蔚. 基于时序补偿引导的强化学习图像-视频行人重识别方法. 发明专利. (专利号：CN202210362412.4)
- *2022.10* 查正军; **刘嘉威**; 黄志鹏. 基于高斯过程的去偏批量归一化的鲁棒行人重识别方法. 发明专利. (专利号：CN202210193826.9)
- *2022.10* 查正军; **刘嘉威**; 黄志鹏. 基于模态自适应混合和不变性卷积分解的行人重识别方法. 发明专利. (专利号：CN202210155715.9)
- *2020.10* 刘武; **刘嘉威**; 梅涛; 郑可成. 检索目标的方法和装置. 发明专利. (专利号：CN202010215923.4)
- *2019.10* 查正军; **刘嘉威**. 行人再识别数据生成方法. 发明专利. (专利号：CN201910466234.8)

<span class='anchor' id='honors-and-awards'></span>
# 🎖 Honors and Awards
- *2024.07*, ACM MM2024 Workshop: Micro-Action Analysis Grand Challenge ([3rd Place Award](https://sites.google.com/view/micro-action/challenge/winners))
- *2023.03*, AAAI2023 Workshop: Defactify 2: Multimodal Fake News Detection ([4th Place Award](https://aiisc.ai/defactify2/))
- *2022.01*, Mozi Distinguished Youth Special Allowance of USTC
- *2020.01*, Special Research Assistantship of CAS
- *2019.06*, CAS Presidential Scholarship
- *2019.06*, Outstanding Graduates Scholarship, USTC
- *2018.09*, Individual Scholarship, USTC
- *2016.09*, Individual Scholarship, USTC

<span class='anchor' id='experiences'></span>
# 📖 Experiences
**Work Experiences:**
- *2021.12 - Present*, Associate Research Fellow, USTC, Collaborating with Prof. Zheng-Jun Zha
- *2019.10 - 2021.11*, Postdocral Research Fellow, USTC, Collaborating with Prof. Zheng-Jun Zha and [Prof. Yongdong Zhang](https://imcc.ustc.edu.cn/main.htm)
- *2019.08 - 2019.10*, Researcher, <span style="color:red">JD AILab</span>, Working with Prof. Tao Mei and [Prof. Wu Liu](https://faculty.ustc.edu.cn/liuwu/zh_CN/index.htm)
- *2016.10 - 2017.01*, Research Intern, <span style="color:red">MSRA</span>, Under the supervision of Prof. Tao Mei

**Educations:**
- *2014.09 - 2019.06*, <span style="color:red">Ph.D.</span> in the Department of Automation, University of Science and Technology of China
- *2009.08 - 2013.06*, <span style="color:red">B.S.</span> in the Department of Automation, Hefei University of Technology

<span class='anchor' id='fundings'></span>
# 💻 Fundings
- *2025.01 - 2028.12*, National Natural Science Foundation of China, General Program, PI (基金委面上基金项目, 主持)
- *2025.01 - 2026.12*, USTC Research Funds of the Double First-Class Initiative, PI (校青年创新重点基金项目, 主持)
- *2022.01 - 2024.12*, National Natural Science Foundation of China, Youth Program, PI (基金委青年基金项目, 主持)
- *2023.06 - 2024.12*，China Merchants Bank-USTC Laboratory Collaborative Project，PI (招商银行-中国科大实验室合作项目, 主持)
- *2021.01 - 2022.12*, USTC Research Funds of the Double First-Class Initiative, PI (校青年创新基金项目, 主持)
- *2021.01 - 2022.12*, China Postdoctoral Science Foundation, PI (中国博士后面上基金项目, 主持)
- *2024.08 - 2028.07*, Chinese Academy of Sciences Stable Support Basic Research Youth Team Program, Key Participant (中国科学院稳定支撑基础研究青年团队计划, 参与)
- *2025.01 - 2026.12*, USTC Research Funds of the Double First-Class Initiative, Key Participant (校融合专项基金项目, 参与)
- *2020.11 - 2023.10*, National Key R&D Program of China, Key Participant (科技创新2030-"新一代人工智能"重大项目, 参与)
- *2020.01 - 2023.12*, Joint Funds of the National Natural Science Foundation of China, Key Participant (基金委联合重点基金项目, 参与)
- *2017.01 - 2021.12*，National Key R&D Program of China, Key Participant (国家重点研发计划, 参与)

<span class='anchor' id='professional-activities'></span>
# 📸 Professional Activities
**Teaching:**
- *2022 Fall*, Graduate Course - Computer Vision (计算机视觉)
- *2023 Fall*, Graduate Course - Computer Vision (计算机视觉)
- *2024 Fall*, Graduate Course - Computer Vision (计算机视觉)
- *2025 Spring*, Undergraduate Course - Python and Deep Learning Basics (Python与深度学习基础) <!-- <span style="color:#000000;background-color:#DCFFB7"> *2025 Spring*, Undergraduate Course - Python and Deep Learning Basics (Python与深度学习基础) \[coming soon\] </span> -->

**Academic Service:**
- National Undergraduate Thesis (Design) Random Inspection and Evaluation Expert Database Expert
- [Member of CSIG Technical Committee on Multimedia](http://mm.csig.org.cn/?page_id=263 )
- Member of CSIG Technical Committee on Digital Media Forensics and Security

**Journal Reviewer:**
- IEEE Transactions on Pattern Analysis and Machine Intelligence
- International Journal of Computer Vision
- IEEE Transactions on Multimedia
- IEEE Transactions on Cybernetics
- IEEE Transactions on Image Processing
- IEEE Transactions on Emerging Topics in Computational Intelligence
- IEEE Transactions on Neural Networks and Learning Systems
- IEEE Transactions on Circuits and Systems for Video Technology
- ACM Transactions on Data Science
- ACM Transactions on Multimedia Computing Communications and Applications
- Neurocomputing
- Neural Networks
- Image and Vision Computing
- Computer Vision and Image Understanding
- IEEE Internet of Things Journal
- IEEE Signal Processing Letters
- Pattern Recognition Letters
- IEEE Sensors Letters
- Journal of Computer Science and Technology

**Conference Area Chair or Senior Program Committee:**
- Chinese Control Conference

**Conference Reviewer or Program Committee:**
- NeurIPS, CVPR, ICCV, ECCV, ICML, ICLR, ACM MM, IJCAI, AAAI, ICME, PRVC, ACCV
