---
title: 'From Facts to Hypotheses: Joint Detection of Biomedical Relations and Epistemic Commitment Using LLMs'
authors:
- Aleksandra Gabryszak
- Phuc Tran Truong
- Arne Binder
- Nikola Milosevic
- Felix-Sebastian Keese
- Astrid Rheinländer
- Philippe Thomas
date: '2026-05-11'
publishDate: '2024-09-21T13:10:18.998131Z'
publication_types:
- paper-conference
publication: '*Proceedings of the Fifteenth Language Resources and Evaluation Conference (LREC 2026)*'
abstract: 'Determining the factual status of biomedical statements, whether affirmed, negated, or uncertain, is essential for accurate understanding. To support research in this area, we introduce BioRelFact, a publicly available, expert-annotated dataset of 1,767 English biomedical sentences labeled with nine relation types and five levels of epistemic commitment. Using this dataset, we evaluate eight large language models (LLMs) from the GPT, Qwen, and Gemma families for joint relation extraction and epistemic classification. Among the evaluated models, GPT-OSS-20B performs best in both tasks (F1 77.3 for relation, 65.3 for commitment), followed by GPT-4o (75.9 and 60.2), while Qwen3-8B (Thinking) shows strong performance despite its smaller size (74.6 and 57.2). Domain adaptation has mixed effects: relative to their general-purpose counterparts, MedGemma-27B improves (+3.6 F1 for relation, +4.4 for factuality), whereas Qwen2.5-Aloe-Beta-7B declines (–4.3 and –3.5, respectively). Moreover, definition-based few-shot prompts consistently yield the best results for most models, and an explorative analysis of prediction errors suggests which specific linguistic features may drive model confusions.'
url_dataset: https://github.com/bayer-group/biomed-relation-factuality-detection
url_pdf: http://www.lrec-conf.org/proceedings/lrec2026/pdf/2026.lrec2026-1.602.pdf
links:
- name: URL
  url: https://lrec.elra.info/lrec2026-main-602

---

---

> **Repository note:**  
> The repository link included in the proceedings version is outdated.  
> The official public repository for this paper is:
> https://github.com/bayer-group/biomed-relation-factuality-detection
