---
permalink: /
title: "Ziwei Wang | Neural Signal Intelligence"
layout: home
excerpt: "Ph.D. candidate at HUST developing generalizable learning methods and foundation models for neural signals."
author_profile: false
---

<div class="zw-home">
  <section id="about" class="zw-hero" aria-labelledby="home-title">
    <div class="zw-portrait-column">
      <div class="zw-portrait-frame">
        <img src="{{ '/images/CV.jpg' | relative_url }}" alt="Portrait of Ziwei Wang">
      </div>
      <div class="zw-focus-note">
        <span class="zw-live-dot" aria-hidden="true"></span>
        <span>Brain–computer interfaces · AI for science · trustworthy biomedical AI</span>
      </div>
    </div>

    <div class="zw-hero-copy">
      <p class="zw-eyebrow">Academic homepage · Huazhong University of Science and Technology</p>
      <h1 id="home-title">Ziwei Wang <span>王紫薇</span></h1>
      <p class="zw-role">Ph.D. Candidate in Intelligent Science and Technology</p>
      <h2>Building AI that learns across brains, modalities, and species.</h2>
      <p class="zw-lead">
        I develop data-efficient, robust, and generalizable learning methods for neural signals under limited labels,
        strong heterogeneity, and distribution shifts. My research spans cross-species and cross-modality transfer,
        interpretable EEG decoding, multimodal learning, and physiologically grounded data generation.
      </p>

      <dl class="zw-identity-list">
        <div>
          <dt>Advisor</dt>
          <dd><a href="https://scholar.google.com/citations?user=UYGzCPEAAAAJ&hl=en" target="_blank" rel="noopener">Prof. Dongrui Wu</a>, NSFC Distinguished Young Scholar, IEEE Fellow, and Editor-in-Chief of <em>IEEE Transactions on Fuzzy Systems</em></dd>
        </div>
        <div>
          <dt>Based in</dt>
          <dd>Wuhan, China</dd>
        </div>
        <div>
          <dt>Open to</dt>
          <dd>Research collaborations, invited talks, and research internships</dd>
        </div>
      </dl>

      <div class="zw-hero-actions" aria-label="Profile links">
        <a class="zw-button zw-button-primary" href="https://scholar.google.com/citations?user=fjlXqvQAAAAJ&hl=en" target="_blank" rel="noopener">Google Scholar <span aria-hidden="true">↗</span></a>
        <a class="zw-button" href="https://github.com/wzwvv" target="_blank" rel="noopener">GitHub <span aria-hidden="true">↗</span></a>
        <a class="zw-text-link" href="mailto:vivi@hust.edu.cn">vivi@hust.edu.cn</a>
      </div>
    </div>

    <div class="zw-metrics" aria-label="Research highlights">
      <div class="zw-metric">
        <strong>&gt;97%</strong>
        <span>Cross-species seizure-detection AUC</span>
      </div>
      <div class="zw-metric">
        <strong>20+</strong>
        <span>Generated datasets</span>
      </div>
      <div class="zw-metric">
        <strong>2,000+</strong>
        <span>Open-dataset downloads</span>
      </div>
      <div class="zw-metric">
        <strong>RMB 340K</strong>
        <span>Competitive funding as PI</span>
      </div>
    </div>
  </section>

  <section class="zw-section zw-vision" aria-labelledby="vision-title">
    <div class="zw-section-heading">
      <p class="zw-section-kicker">Research vision</p>
      <h2 id="vision-title">From neural-signal decoding to general models for brain-disorder care</h2>
    </div>
    <div class="zw-vision-grid">
      <p>
        My long-term goal is to build trustworthy cross-species, multimodal, and multitask foundation models for
        brain-disorder screening, prognosis, treatment-response monitoring, and rehabilitation.
      </p>
      <p>
        I am particularly interested in shared neural representations across epilepsy, Alzheimer’s disease,
        hypoxic–ischemic encephalopathy (HIE), amyotrophic lateral sclerosis (ALS), and related neurological disorders.
      </p>
    </div>
    <div class="zw-topic-pills" aria-label="Research topics">
      <span>Cross-species transfer</span>
      <span>Multimodal foundation models</span>
      <span>Trustworthy EEG decoding</span>
      <span>Generative neural data</span>
      <span>Brain-disorder intelligence</span>
    </div>
  </section>

  <section id="research" class="zw-section" aria-labelledby="research-title">
    <div class="zw-section-heading zw-heading-split">
      <div>
        <p class="zw-section-kicker">Research</p>
        <h2 id="research-title">Three connected layers of neural intelligence</h2>
      </div>
      <p class="zw-section-intro">My work connects transfer, decoding, and data generation into a unified path toward general-purpose neural models.</p>
    </div>

    <div class="zw-research-grid">
      <article class="zw-research-card zw-card-blue">
        <span class="zw-card-index">01</span>
        <p class="zw-card-label">Generalization</p>
        <h3>Cross-Species and Cross-Domain Neural Decoding</h3>
        <p>Transfer neural knowledge across subjects, patients, datasets, devices, modalities, and species when target labels are scarce.</p>
        <ul>
          <li>Multi-space alignment across canine/human and intracranial/scalp EEG</li>
          <li>Unsupervised cross-patient adaptation</li>
          <li>Cross-dataset knowledge distillation and online adaptation</li>
        </ul>
        <a href="#cross-domain" target="_self">Explore representative work <span aria-hidden="true">↓</span></a>
      </article>

      <article class="zw-research-card zw-card-teal">
        <span class="zw-card-index">02</span>
        <p class="zw-card-label">Representation</p>
        <h3>Generalizable and Interpretable Neural Decoders</h3>
        <p>Design EEG-specific architectures that explicitly model temporal dynamics, channel topology, frequency structure, and modality reliability.</p>
        <ul>
          <li>Dual-branch temporal–spatial Conformers</li>
          <li>Multi-view contrastive representation learning</li>
          <li>Frequency-aware and reliability-aware multimodal fusion</li>
        </ul>
        <a href="#neural-decoders" target="_self">Explore representative work <span aria-hidden="true">↓</span></a>
      </article>

      <article class="zw-research-card zw-card-gold">
        <span class="zw-card-index">03</span>
        <p class="zw-card-label">Data foundation</p>
        <h3>Data Generation for Neural Foundation Models</h3>
        <p>Build physiologically grounded augmentation, generation, denoising, and evaluation methods for scalable neural-model pretraining.</p>
        <ul>
          <li>Knowledge-guided and time–frequency augmentation</li>
          <li>Diffusion and flow-based neural-signal generation</li>
          <li>Benchmarks for realism, utility, physiology, and privacy</li>
        </ul>
        <a href="#data-foundations" target="_self">Explore representative work <span aria-hidden="true">↓</span></a>
      </article>
    </div>
  </section>

  <section id="news" class="zw-section" aria-labelledby="news-title">
    <div class="zw-section-heading zw-heading-split">
      <div>
        <p class="zw-section-kicker">Updates</p>
        <h2 id="news-title">Selected news</h2>
      </div>
      <p class="zw-section-intro">Recent publications, open resources, funding, and recognition.</p>
    </div>

    <ol class="zw-news-list">
      <li><time datetime="2026-10">Oct. 2026</time><p><a href="https://arxiv.org/abs/2610.08817" target="_blank" rel="noopener">DenoFlow</a>, a flow-matching framework for SSVEP denoising under real physiological artifacts, is available as a preprint.</p></li>
      <li><time datetime="2026-09">Sep. 2026</time><p>Released preprints on <a href="https://arxiv.org/abs/2609.11341" target="_blank" rel="noopener">cross-modal Diffusion Transformers</a> and <a href="https://arxiv.org/abs/2609.11372" target="_blank" rel="noopener">reliability-aware multimodal fusion</a>.</p></li>
      <li><time datetime="2026-06">Jun. 2026</time><p><a href="https://ieeexplore.ieee.org/abstract/document/11554397/" target="_blank" rel="noopener">CKD</a> was accepted by <em>IEEE Transactions on Biomedical Engineering</em>.</p></li>
      <li><time datetime="2026-06">Jun. 2026</time><p>Received the Excellent Scientific and Technical Paper Award from the Hubei Association for Science and Technology (湖北省科协优秀科技论文奖).</p></li>
      <li><time datetime="2026-04">Apr. 2026</time><p>Released the <a href="https://zenodo.org/records/19333249" target="_blank" rel="noopener">CHSZ pediatric epilepsy EEG dataset</a>, collected with Wuhan Children’s Hospital.</p></li>
      <li><time datetime="2026-02">Feb. 2026</time><p>Selected for the Top 10 Advances in Brain–Computer Interfaces in China (中国脑机接口十大进展).</p></li>
      <li><time datetime="2025-12">Dec. 2025</time><p>Awarded two PI-led research grants totaling RMB 340,000 from NSFC and CAST.</p></li>
      <li><time datetime="2025-09">Sep. 2025</time><p>Named one of ten worldwide recipients of the Ant Group InTech Scholarship.</p></li>
    </ol>
  </section>

  <section id="publications" class="zw-section zw-publications-section" aria-labelledby="publications-title">
    <div class="zw-section-heading zw-heading-split">
      <div>
        <p class="zw-section-kicker">Selected publications</p>
        <h2 id="publications-title">A research program, not a list of papers</h2>
      </div>
      <div class="zw-publication-legend">
        <span><sup>*</sup> Equal contribution</span>
        <span><sup>#</sup> Corresponding author</span>
        <a href="https://scholar.google.com/citations?user=fjlXqvQAAAAJ&hl=en" target="_blank" rel="noopener">Complete list ↗</a>
      </div>
    </div>

    {% for group in site.data.ziwei_publications %}
      <div id="{{ group.id }}" class="zw-publication-group">
        <div class="zw-group-heading">
          <p>{{ group.eyebrow }}</p>
          <h3>{{ group.title }}</h3>
          <span>{{ group.summary }}</span>
        </div>

        <div class="zw-publication-list">
          {% for pub in group.publications %}
            <article class="zw-publication-card">
              <div class="zw-publication-visual">
                {% if pub.image %}
                  <img src="{{ pub.image | relative_url }}" alt="Visual summary for {{ pub.title }}" loading="lazy">
                {% else %}
                  <div class="zw-publication-fallback" aria-hidden="true"><span>{{ pub.mark }}</span></div>
                {% endif %}
              </div>
              <div class="zw-publication-copy">
                <div class="zw-publication-meta">
                  <span class="zw-venue">{{ pub.venue_short }}</span>
                  <span class="zw-status zw-status-{{ pub.status | slugify }}">{{ pub.status }}</span>
                </div>
                <h4>{{ pub.title }}</h4>
                <p class="zw-authors">{{ pub.authors }}</p>
                <p class="zw-journal">{{ pub.venue }}</p>
                <p class="zw-publication-description">{{ pub.description }}</p>
                <div class="zw-publication-links">
                  {% if pub.paper %}<a href="{{ pub.paper }}" target="_blank" rel="noopener">Paper <span aria-hidden="true">↗</span></a>{% endif %}
                  {% if pub.code %}<a href="{{ pub.code }}" target="_blank" rel="noopener">Code <span aria-hidden="true">↗</span></a>{% endif %}
                  {% if pub.data %}<a href="{{ pub.data }}" target="_blank" rel="noopener">Data <span aria-hidden="true">↗</span></a>{% endif %}
                </div>
              </div>
            </article>
          {% endfor %}
        </div>
      </div>
    {% endfor %}
  </section>

  <section id="experience" class="zw-section" aria-labelledby="experience-title">
    <div class="zw-section-heading">
      <p class="zw-section-kicker">Trajectory</p>
      <h2 id="experience-title">Education, funding, and industry experience</h2>
    </div>

    <div class="zw-trajectory-grid">
      <div class="zw-trajectory-column">
        <h3>Education</h3>
        <ol class="zw-timeline">
          <li>
            <span class="zw-timeline-year">2023–Present</span>
            <div><strong>Huazhong University of Science and Technology</strong><span>Ph.D. in Intelligent Science and Technology</span></div>
          </li>
          <li>
            <span class="zw-timeline-year">2021–2023</span>
            <div><strong>Huazhong University of Science and Technology</strong><span>M.S. in Intelligent Science and Technology</span></div>
          </li>
          <li>
            <span class="zw-timeline-year">2017–2021</span>
            <div><strong>Central South University</strong><span>B.Eng. in Measurement and Control Technology and Instrumentation</span></div>
          </li>
        </ol>
      </div>

      <div class="zw-trajectory-column">
        <h3>Research funding as PI</h3>
        <div class="zw-funding-card">
          <div><span>NSFC</span><strong>RMB 300,000</strong></div>
          <h4>Cross-Species Multimodal EEG General Representation and Foundation Models</h4>
          <p>Young Student Basic Research Program (国家自然科学基金青年学生基础研究项目), Grant 625B2077, 2026–2027.</p>
        </div>
        <div class="zw-funding-card">
          <div><span>CAST</span><strong>RMB 40,000</strong></div>
          <h4>General-Purpose EEG Foundation Models</h4>
          <p>Young Elite Scientists Sponsorship Program, Doctoral Student Track (中国科协青年人才托举工程博士生专项), 2026–2027.</p>
        </div>
      </div>

      <div class="zw-trajectory-column">
        <h3>Industry experience</h3>
        <div class="zw-industry-card">
          <div class="zw-company-row"><strong>Alibaba Cloud</strong><span>Oct. 2022–Apr. 2023</span></div>
          <p>Algorithm Research Intern, Cloud-Server Failure Prediction</p>
          <ul>
            <li>Proposed SparseAttention for efficient long-sequence forecasting.</li>
            <li>Designed a domain-generalized mixture-of-experts architecture for temporal and device shifts.</li>
            <li>Developed five anomaly-aware augmentation operators using N-grams and TF–IDF.</li>
          </ul>
        </div>
      </div>
    </div>

    <div class="zw-open-science">
      <div>
        <p class="zw-section-kicker">Open science</p>
        <h3>Reusable data, code, and benchmarks</h3>
      </div>
      <p>The open CHSZ dataset contains EEG recordings from 27 children with epilepsy and has received more than 2,000 downloads. Representative implementations are maintained openly on GitHub.</p>
      <div>
        <a href="https://zenodo.org/records/19333249" target="_blank" rel="noopener">Dataset ↗</a>
        <a href="https://github.com/wzwvv" target="_blank" rel="noopener">All repositories ↗</a>
      </div>
    </div>
  </section>

  <section id="honors" class="zw-section" aria-labelledby="honors-title">
    <div class="zw-section-heading zw-heading-split">
      <div>
        <p class="zw-section-kicker">Recognition</p>
        <h2 id="honors-title">Selected honors and academic service</h2>
      </div>
      <p class="zw-section-intro">Recognition spanning research originality, academic excellence, open science, and community service.</p>
    </div>

    <div class="zw-honors-grid">
      <article><span>2025</span><h3>Ant Group InTech Scholarship</h3><p>One of ten recipients worldwide.</p></article>
      <article><span>2020, 2024–2026</span><h3>National Scholarship (国家奖学金)</h3><p>Four-time recipient across undergraduate and Ph.D. study.</p></article>
      <article><span>2025</span><h3>Excellent Scientific and Technical Paper</h3><p>Hubei Association for Science and Technology.</p></article>
      <article><span>2025</span><h3>Merit Student Pacesetter</h3><p>Highest student honor at HUST.</p></article>
      <article><span>2022</span><h3>IEEE CIS Student Grant</h3><p>One of five recipients worldwide.</p></article>
      <article><span>2023–2025</span><h3>National BCI Recognition</h3><p>Top 10 Advances 2025, Top 10 Highlights 2024, and National First Prize at the 2023 World Robot Contest BCI Competition.</p></article>
    </div>

    <div class="zw-service-panel">
      <div>
        <p class="zw-section-kicker">Academic service</p>
        <h3>Reviewer across AI, biomedical engineering, and neural engineering</h3>
      </div>
      <p>
        Reviewer for <em>Artificial Intelligence Review</em>, <em>IEEE Reviews in Biomedical Engineering</em>,
        <em>IEEE Transactions on Fuzzy Systems</em>, <em>IEEE JBHI</em>, <em>IEEE TNSRE</em>,
        <em>Knowledge-Based Systems</em>, <em>Neurocomputing</em>, <em>Journal of Neural Engineering</em>,
        <em>Scientific Reports</em>, ICONIP, and IEEE SMC. Recognized as an IOP Trusted Reviewer in 2024.
      </p>
    </div>
  </section>

  <section id="collaborators" class="zw-section" aria-labelledby="collaborators-title">
    <div class="zw-section-heading zw-heading-split">
      <div>
        <p class="zw-section-kicker">People</p>
        <h2 id="collaborators-title">Selected collaborators</h2>
      </div>
      <p class="zw-section-intro">I have been fortunate to collaborate with researchers across transfer learning, neural decoding, multimodal learning, and biomedical AI.</p>
    </div>

    <div class="zw-collaborator-grid">
      {% for person in site.data.collaborators %}
        {% if person.url %}<a class="zw-collaborator-card" href="{{ person.url }}" target="_blank" rel="noopener">{% else %}<div class="zw-collaborator-card zw-collaborator-static">{% endif %}
          <span class="zw-collaborator-avatar" aria-hidden="true">{{ person.initials }}</span>
          <span class="zw-collaborator-info">
            <strong>{{ person.name }}</strong>
            <small>{{ person.stage }}</small>
            {% if person.venue %}<em>{{ person.venue }}</em>{% endif %}
          </span>
          {% if person.url %}<span class="zw-collaborator-arrow" aria-hidden="true">↗</span>{% endif %}
        {% if person.url %}</a>{% else %}</div>{% endif %}
      {% endfor %}
    </div>
  </section>

  <section id="contact" class="zw-contact" aria-labelledby="contact-title">
    <div>
      <p class="zw-section-kicker">Contact</p>
      <h2 id="contact-title">Let’s discuss neural intelligence that can generalize.</h2>
      <p>I welcome conversations about cross-species learning, neural foundation models, brain-disorder intelligence, open datasets, and research internships.</p>
    </div>
    <div class="zw-contact-links">
      <a href="mailto:vivi@hust.edu.cn"><span>Email</span><strong>vivi@hust.edu.cn</strong></a>
      <a href="https://scholar.google.com/citations?user=fjlXqvQAAAAJ&hl=en" target="_blank" rel="noopener"><span>Research</span><strong>Google Scholar ↗</strong></a>
      <a href="https://github.com/wzwvv" target="_blank" rel="noopener"><span>Open source</span><strong>github.com/wzwvv ↗</strong></a>
      <a href="https://orcid.org/0000-0003-1324-2298" target="_blank" rel="noopener"><span>Research ID</span><strong>ORCID ↗</strong></a>
    </div>
  </section>

  <footer class="zw-footer">
    <p>© 2026 Ziwei Wang. Last updated October 2026.</p>
    <a href="#about" target="_self">Back to top ↑</a>
  </footer>
</div>
