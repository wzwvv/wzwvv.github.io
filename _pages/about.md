---
permalink: /
title: "Ziwei (Vivi) Wang — BCI & EEG"
excerpt: "Ph.D. candidate at HUST · Brain–Computer Interfaces · EEG decoding · Cross-species seizure detection"
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

I am a third-year Ph.D. candidate in the School of Artificial Intelligence & Automation (Digital Medicine) at Huazhong University of Science and Technology (HUST), advised by Prof. Dongrui Wu. My research centers on brain–computer interfaces and machine learning, with focuses on EEG decoding, cross-subject/domain generalization, knowledge-driven data generation, and cross-species/cross-modality seizure detection. I develop principled methods—such as multi-space alignment, dual-branch convolutional Transformers, and test-time/transfer learning—to improve robustness, interpretability, and clinical reliability. Looking ahead, my primary research thrust is to build large-scale EEG foundation models that are data- and parameter-efficient, privacy-aware, and transferable across tasks, populations, and sensing modalities.

My research interest includes Brain-Computer Interfaces and Machine Learning. I have published 8 papers at the top international BCI journal with total <a href='https://scholar.google.com/citations?user=fjlXqvQAAAAJ&hl=en'>google scholar citations <strong><span id='total_cit'>130+</span></strong></a> (You can also use google scholar badge <a href='https://scholar.google.com/citations?user=fjlXqvQAAAAJ&hl=en'><img src="https://img.shields.io/endpoint?url={{ url | url_encode }}&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>).


# 🔥 News
- *2025.09*: &nbsp;🎉 Awarded **Ant Group InTech Scholarship** (global top 10; Digital Medicine). 
- *2025.05*: &nbsp;Oral at **China Systems Science Conference**: *Cross-species & cross-modality seizure detection via multi-space alignment*.
- *2025.04*: &nbsp;Paper accepted **IEEE JBHI (in press)**: *DBConformer: Dual-branch Convolutional Transformer for EEG decoding* (DOI: 10.1109/JBHI.2025.3622725).
- *2024.12*: &nbsp;Poster at **China Brain–Computer Intelligence Conference**: *Channel Reflection: Knowledge-Driven Data Augmentation for EEG-based BCIs*.
- *2024.09*: &nbsp;Invited **Alibaba Cloud Yunqi Conference** (AI for Science showcase): *EEG-based Automatic Seizure Detection*.
- *2023.11*: &nbsp;**ICONIP Tutorial**: *Transfer Learning for EEG-based Brain–Computer Interfaces*.

# 📝 Publications 

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">NSR 2025</div><img src='images/CST.png' alt="nsr-2025" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Canine EEG helps human: Cross-species and cross-modality epileptic seizure detection via multi-space alignment](https://academic.oup.com/nsr/article/12/6/nwaf086/8052010)

**Z. Wang**, S. Li, D. Wu*, *National Science Review*, vol.12, no.6, p. nwaf086, 2025. (CAS Q1 Top journal)

[**Supplementary Material**](https://oup.silverchair-cdn.com/oup/backfile/Content_public/Journal/nsr/12/6/10.1093_nsr_nwaf086/2/nwaf086_supplemental_file.pdf?Expires=1765547375&Signature=cUzKn4rWgXszOpTemiCAPdLlT2oxigE4MDzUjM~sFCTgd21BMm32YVi~4KsjLS4RC1teCu34FX3bq361szPcu0aJcQ4YCi-euBiRB5tLcZbIfRRgKQb7xK0ZX28XcSksk14b9ZvsSQjIcjpcq~04nSJlYsV6HqEt~o9Yhw6EBAIs1fJPW7Ne3l8l0k3QjAAnwkJnAuFKxXxwPP3GOqGsg7x-JFug3TwE45IlbkULJXCa3JsAx6sfuCA6LN9yjzeXashToGW1VpzJxlB2Mc1yiwu897-Lvz1H8cIOwlfvmyeruAKg3-UZ2naWXyPTQBFwU8e~5tGT3Z900VSlCUe7Vg__&Key-Pair-Id=APKAIE5G5CRDK6RD3PGA) <strong><span class='show_paper_citations' data='nsr2025-wang'></span></strong>
- Cross-species (human/canine) and cross-modality (scalp/intracranial) transfer with multi-space alignment; first systematic validation for seizure detection.
</div>
</div>

- [DBConformer: Dual-branch Convolutional Transformer for EEG decoding](https://doi.org/10.1109/JBHI.2025.3622725), **Z. Wang**, H. Wang, T. Jia, X. He, S. Li, and D. Wu*, *IEEE JBHI*, 2025, DOI: 10.1109/JBHI.2025.3622725, Early access. (CAS Q1 Top journal)
- [Channel Reflection: Knowledge-Driven Data Augmentation for EEG-Based BCIs](), **Z. Wang**†, S. Li† , J. Luo, J. Liu, and D. Wu*, *Neural Networks*, vol.176, p.106351, 2024. (CAS Q1 Top journal)
- [Time-frequency transform based EEG data augmentation for brain-computer interfaces](), **Z. Wang**, S. Li, X. Chen, and D. Wu*, *Knowledge-Based Systems*, vol. 311, p. 113074, 2025. (CAS Q1 Top journal)
- [MVCNet: Multi-view contrastive network for motor imagery classification](https://www.sciencedirect.com/science/article/pii/S0950705125012468), **Z. Wang**, S. Li, X. Chen, and D. Wu*, *Knowledge-Based Systems*, vol.328, p.114205, 2025. (CAS Q1 Top journal)
- [Unsupervised Domain Adaptation for Cross-Patient Seizure Classification](https://iopscience.iop.org/article/10.1088/1741-2552/ad0859/meta), **Z. Wang**, W. Zhang, S. Li, X. Chen, and D. Wu*, *Journal of Neural Engineering*, vol. 20, no.6, p.066002, 2023. (CAA Class-A journal)
- [EEG-Based Seizure Prediction Using Transfer Learning](https://cis.ieee.org/images/files/Documents/GrantRecipientsReports/2021/CIS_Wang.pdf), **Z. Wang** and D. Wu*, *IEEE Computational Intelligence Society*, Student Grant Paper, 2021. (Global Top 5)

# 🎖 Honors and Awards
- *2025.09* **Ant Group InTech Scholarship** (Global Top 10; Digital Medicine Top 2); Ant Group/Ant Science and Technology Award
- *2025.10* **National Ph.D. Scholarship**; Ministry of Education of China
- *2025.10* **HUST Model of Merit Student** (The Highest Student Honor of HUST); Huazhong University of Science and Technology  
- *2024.10* **National Ph.D. Scholarship**; Ministry of Education of China  
- *2024.08* **Huanao Top-10 BCI Highlights in China**; Haihe Laboratory of BCI & Human–Machine Integration  
- *2023.08* **World Robot Contest – BCI**, National 1st Prize; Chinese Institute of Electronics
- *2025.08* **World Robot Contest – BCI**, National 2nd Prize; Chinese Institute of Electronics
- *2021.07* **World Robot Contest – BCI**, National 2nd Prize; Chinese Institute of Electronics
- *2020.10* **Undergraduate National Scholarship**, Ministry of Education of China  

# 📖 Educations
- *2021.09 - now*, Ph.D. (MS–Ph.D. program), **Huazhong University of Science and Technology (HUST)**, Intelligent Science & Technology (Advisor: Prof. Dongrui Wu) 
- *2017.09 - 2021.06*, B.Eng., **Central South University (CSU)**, Measurement, Control Technology & Instruments 

# 💬 Invited Talks
- *2024.09*, Alibaba Cloud **Yunqi Conference**, *EEG-based Automatic Seizure Detection* (AI for Science Showcase). 
- *2023.11*, **ICONIP Tutorial**, *Transfer Learning for EEG-based Brain–Computer Interfaces*.

# 💻 Internships
- *2022.10 - 2023.04*, [Alibaba Cloud](https://www.alibabacloud.com/), China.
