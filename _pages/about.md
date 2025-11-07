---
permalink: /
title: "Ziwei Wang — BCI & Machine Learning"
excerpt: "Ph.D. candidate at HUST · Brain–Computer Interfaces · Machine Learning · Smart Healthcare"
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

I am a Ph.D. candidate in the School of Artificial Intelligence & Automation at Huazhong University of Science and Technology (HUST), supervised by [Prof. Dongrui Wu](https://lab.bciml.cn/). My work lies at brain–computer interfaces and machine learning for smart healthcare. I study EEG decoding under distribution shift and data scarcity, focusing on cross-subject/domain generalization, knowledge-driven data generation, and cross-species/modality seizure detection. Looking ahead, I am building **large-scale EEG foundation models** that are parameter-efficient, privacy-aware, and transferable across species, tasks, populations, and sensing modalities, with an emphasis on clinical reliability and deployment.

My research interests include Brain–Computer Interfaces and Machine Learning. I have published 8 first-author papers, five on CAS Q1/Top iournals <a href='https://scholar.google.com/citations?user=fjlXqvQAAAAJ&hl=en'>google scholar citations <strong><span id='total_cit'>130+</span></strong></a>.

# 🔥 News
- *2025.10*: &nbsp;🎉 Awarded **National Ph.D. Scholarship**; Ministry of Education of China.
- *2025.10*: &nbsp;🏅 Named **HUST Model Student of Merit (Pacesetter)** (**Highest Student Honor**); Huazhong University of Science and Technology. [Media coverage](https://mp.weixin.qq.com/s/euTiOZLJ2kkt3wenn1wq-A?scene=1)
- *2025.09*: &nbsp;🎉 Awarded **Ant Group InTech Scholarship** (Global Top 10; Top 2 in Digital Medicine); Ant Group / Ant Science and Technology Award. [Zhejiang Daily](https://zjrb.zjol.com.cn/html/2025-09/14/content_3851946.htm?div=-1), [Media coverage](https://aia.hust.edu.cn/info/1524/10644.htm)
- *2025.08*: &nbsp;🏆 **World Robot Contest — BCI**, National Second Prize; Chinese Institute of Electronics.
- *2025.05*: &nbsp;🎤 Oral at **China Systems Science Conference**: *Cross-species & cross-modality seizure detection via multi-space alignment*; Kunming, China.
- *2025.04*: &nbsp;📝 Paper accepted **IEEE JBHI (in press)**: *DBConformer: Dual-branch Convolutional Transformer for EEG decoding* (DOI: 10.1109/JBHI.2025.3622725).
- *2024.12*: &nbsp;🖼️ Poster at **First China Brain–Computer Intelligence Conference**: *Channel Reflection: Knowledge-Driven Data Augmentation for EEG-Based BCIs*; Hangzhou, China.
- *2024.12*: &nbsp;🖼️ Poster at **SAAC 2025**: *Channel Reflection: Knowledge-Driven Data Augmentation for EEG-Based BCIs*; Wuhan, China.
- *2024.10*: &nbsp;🎉 Awarded **National Ph.D. Scholarship**; Ministry of Education of China.
- *2024.09*: &nbsp;🎤 Oral at **Alibaba Cloud Yunqi Conference** (AI for Science showcase): *EEG-based Automatic Seizure Detection*; Hangzhou, China.
- *2024.08*: &nbsp;🏅 Selected for **Huanao “Top-10 BCI Highlights in China”**; Haihe Laboratory of BCI & Human–Machine Integration.
- *2024*: &nbsp;✅ **IOP Trusted Reviewer**; IOP Publishing.
- *2023.11*: &nbsp;🎤 **ICONIP Tutorial**: *Transfer Learning for EEG-based Brain–Computer Interfaces*; Changsha, China.
- *2023.08*: &nbsp;🏆 **World Robot Contest — BCI**, National First Prize; Chinese Institute of Electronics.
- *2022.03*: &nbsp;🎉 **IEEE Computational Intelligence Society Scholarship** (Global Top 5); IEEE CIS.

# 📝 Publications 

<!-- NSR 2025 -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NSR 2025</div><img src='images/CST.png' alt="nsr-2025" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Canine EEG helps human: Cross-species and cross-modality epileptic seizure detection via multi-space alignment](https://academic.oup.com/nsr/article/12/6/nwaf086/8052010)

**Z. Wang**, S. Li, D. Wu*, *National Science Review*, vol.12, no.6, p. nwaf086, 2025. (CAS Q1 Top journal)

[**Supplementary Material**](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/nsr/12/6/10.1093_nsr_nwaf086/2/nwaf086_supplemental_file.pdf?Expires=1765547375&Signature=cUzKn4rWgXszOpTemiCAPdLlT2oxigE4MDzUjM~sFCTgd21BMm32YVi~4KsjLS4RC1teCu34FX3bq361szPcu0aJcQ4YCi-euBiRB5tLcZbIfRRgKQb7xK0ZX28XcSksk14b9ZvsSQjIcjpcq~04nSJlYsV6HqEt~o9Yhw6EBAIs1fJPW7Ne3l8l0k3QjAAnwkJnAuFKxXxwPP3GOqGsg7x-JFug3TwE45IlbkULJXCa3JsAx6sfuCA6LN9yjzeXashToGW1VpzJxlB2Mc1yiwu897-Lvz1H8cIOwlfvmyeruAKg3-UZ2naWXyPTQBFwU8e~5tGT3Z900VSlCUe7Vg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA) <strong><span class='show_paper_citations' data='nsr2025-wang'></span></strong>
- Cross-species (human/canine) and cross-modality (scalp/intracranial) transfer via multi-space alignment; The 1-st systematic validation for epileptic seizure detection.
</div>
</div>

<!-- IEEE JBHI 2025 -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">IEEE JBHI 2025</div><img src='images/DBConformer.png' alt="jbhi-2025-dbconformer" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[DBConformer: Dual-branch Convolutional Transformer for EEG decoding](https://doi.org/10.1109/JBHI.2025.3622725)

**Z. Wang**, H. Wang, T. Jia, X. He, S. Li, and D. Wu*, *IEEE Journal of Biomedical and Health Informatics*, 2025, Early access. DOI: 10.1109/JBHI.2025.3622725. (CAS Q1 Top journal)
- Parallel spatio–temporal branches with convolutional and Transformer modules for robust, interpretable EEG decoding.
</div>
</div>

<!-- Neural Networks 2024 -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Neural Networks 2024</div><img src='images/CR.png' alt="nn-2024-channel-reflection" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Channel Reflection: Knowledge-Driven Data Augmentation for EEG-Based BCIs]()

**Z. Wang**†, S. Li†, J. Luo, J. Liu, and D. Wu*, *Neural Networks*, vol.176, p.106351, 2024. (CAS Q1 Top journal)
- Knowledge-driven EEG data augmentation by utilizing neuroscience prior knowledge for brain signal decoding.
</div>
</div>

<!-- KBS 2025 -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">KBS 2025</div><img src='images/CSDA.png' alt="kbs-2025-tf-aug" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Time-frequency transform based EEG data augmentation for brain-computer interfaces]()

**Z. Wang**, S. Li, X. Chen, and D. Wu*, *Knowledge-Based Systems*, vol.311, p.113074, 2025. (CAS Q1 Top journal)
- Time–frequency transformation based EEG data augmentation to enrich EEG patterns and improve cross-subject decoding robustness.
</div>
</div>

<!-- KBS 2025 -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">KBS 2025</div><img src='images/MVCNet.png' alt="kbs-2025-mvcnet" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[MVCNet: Multi-view contrastive network for motor imagery classification](https://www.sciencedirect.com/science/article/pii/S0950705125012468)

**Z. Wang**, S. Li, X. Chen, and D. Wu*, *Knowledge-Based Systems*, vol.328, p.114205, 2025. (CAS Q1 Top journal)
- Multi-view contrastive learning for MI-EEG feature learning and performance enhancement.
</div>
</div>

<!-- JNE 2023 -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">JNE 2023</div><img src='images/TASA.png' alt="jne-2023-uda" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Unsupervised Domain Adaptation for Cross-Patient Seizure Classification](https://iopscience.iop.org/article/10.1088/1741-2552/ad0859/meta)

**Z. Wang**, W. Zhang, S. Li, X. Chen, and D. Wu*, *Journal of Neural Engineering*, vol.20, no.6, p.066002, 2023. (CAA Class-A journal)
- UDA framework mitigating patient shift for epileptic seizure detection.
</div>
</div>

<!-- IEEE CIS Student Grant 2021 -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">IEEE CIS 2021</div><img src='images/CIS_Grant.png' alt="ieee-cis-2021-student-grant" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[EEG-Based Seizure Prediction Using Transfer Learning](https://cis.ieee.org/images/files/Documents/GrantRecipientsReports/2021/CIS_Wang.pdf)

**Z. Wang** and D. Wu*, *IEEE Computational Intelligence Society*, Student Grant Paper, 2021. (Global Top 5)
- Transfer learning pipeline for children’s epilepsy prediction; awarded IEEE CIS Student Research Grant (global top 5).
</div>
</div>


# 🎖 Honors and Awards
- *2025.09* **Ant Group InTech Scholarship** (Global Top 10; Top 2 in Digital Medicine); Ant Group / Ant Science and Technology Award
- *2025.10* **National Ph.D. Scholarship**; Ministry of Education of the People’s Republic of China
- *2024.10* **National Ph.D. Scholarship**; Ministry of Education of the People’s Republic of China
- *2025.10* **HUST Model Student of Merit (Pacesetter)** (highest student honor at HUST); Huazhong University of Science and Technology
- *2020.10* **Undergraduate National Scholarship**; Ministry of Education of the People’s Republic of China
- *2021.06* **Outstanding Graduate of Hunan Province**; Hunan Provincial Department of Education
- *2022.02* **IEEE Computational Intelligence Society Scholarship** (Global Top 5); IEEE Computational Intelligence Society
- *2023.08* **World Robot Contest — BCI, National First Prize**; Chinese Institute of Electronics
- *2025.08* **World Robot Contest — BCI, National Second Prize**; Chinese Institute of Electronics
- *2021.07* **World Robot Contest — BCI, National Second Prize**; Chinese Institute of Electronics
- *2025.01* **Huanao “Top-10 BCI Highlights in China”** (National Top 10); Haihe Laboratory of BCI & Human–Machine Integration (provincial–ministerial joint platform)
- *2024.12* **IOP Trusted Reviewer**; Institute of Physics (IOP Publishing)
- *2021.06* **Outstanding Graduate**; Central South University
- *2020.12* **Special-Class Scholarship**; Central South University


# 📖 Educations
- *2021.09 - now*, Ph.D. (MS–Ph.D. program), **Huazhong University of Science and Technology (HUST)**, Intelligent Science & Technology (Advisor: Prof. Dongrui Wu) 
- *2017.09 - 2021.06*, B.Eng., **Central South University (CSU)**, Measurement, Control Technology & Instruments 

# 💬 Invited Talks
- *2025.05*, **China Systems Science Conference (CSSC)** — **Oral**: *Cross-species & cross-modality seizure detection via multi-space alignment*; Kunming, China.
- *2024.12*, **First China Brain–Computer Intelligence Conference** — **Poster**: *Channel Reflection: Knowledge-Driven Data Augmentation for EEG-Based BCIs*; Hangzhou, China.
- *2024.12*, **SAAC 2025** — **Poster**: *Channel Reflection: Knowledge-Driven Data Augmentation for EEG-Based BCIs*; Wuhan, China.
- *2024.09*, **Alibaba Cloud Yunqi Conference** (AI for Science showcase) — **Oral**: *EEG-based Automatic Seizure Detection*; Hangzhou, China.
- *2023.11*, **ICONIP 2023 — Tutorial**: *Transfer Learning for EEG-based Brain–Computer Interfaces*; Changsha, China.

# 💻 Internships
- *2022.10 - 2023.04*, [Alibaba Cloud](https://www.alibabacloud.com/), China.
  - **Anomaly-aware data augmentation with prior knowledge:** designing **five augmentation operators** leveraging **N-grams** and **TF-IDF** to augment positive-class samples, increasing data availability and improving the **generalization** of fault-detection models.
  - **Long-sequence forecasting with Transformer:** Quantified anomaly-feature importance to identify **salient/sparse queries**, and designed a **SparseAttention** module to handle long sequences more efficiently.
  - **Domain-generalized MoE architecture:** Addressed substantial temporal and device-level distribution shifts in server-fault data by designing a **domain-generalized Mixture-of-Experts** model for robust prediction under distribution shift.
  - Authorized patent (student first author).

