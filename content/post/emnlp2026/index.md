---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "7 papers by DFKI-SLT authors accepted to EMNLP 2026"
subtitle: ""
summary: ""
authors: []
tags: []
categories: []
date: 2026-08-25
lastmod: 2026-08-25
featured: false
draft: false

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Projects (optional).
#   Associate this post with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `projects = ["internal-project"]` references `content/project/deep-learning/index.md`.
#   Otherwise, set `projects = []`.
projects: []
---

Two papers from researchers in the DFKI-NLP group have been accepted as Main papers at the [2026 Conference on Empirical Methods in Natural Language Processing (EMNLP 2026)](https://2026.emnlp.org/), and one as a Findings paper. In addition, one paper was accepted to the [BlackboxNLP workshop](https://blackboxnlp.github.io/2026/), and 3 more papers from our group's [Speech and Language Technology lab](https://www.dfki.de/en/web/research/research-departments/speech-and-language-technology) were accepted as Main or Findings. EMNLP will take place October 24 –29 in Budapest, Hungary. 

The first paper, titled "Training-Free Character-Length Control in Summarization with Diffusion Language Models", introduces a training-free inference-time method for masked diffusion LMs that estimates expected character length at each denoising step and dynamically inserts or removes masked positions to steer toward a target length. The proposed approach requires no fine-tuning and applies to any off-the-shelf masked diffusion LM. Across three summarization benchmarks, it reduces character-length errors by an order of magnitude compared to baselines while maintaining competitive summary quality. The second paper analyses evaluation trends from 2020 to 2025 across 4 major NLP conferences, in particular the adoption of LLM-as-a-judge in comparison to human evaluation. Based on an automatic and human-verified approach to extracting evaluation approaches, metrics and criteria from more than 3300 NLG papers, it identifies systemic evaluation challenges and proposes an evaluation checklist to guide metric selection, construct validity and LLM-as-a-judge deployment. The third paper proposes an approach for hybrid differential privacy text de-identification in medical texts.

{{< cite page="/publication/yang-emnlp2026-nlgeval" view="4" >}}
{{< cite page="/publication/castle-emnlp2026-diffusion" view="4" >}}
{{< cite page="/publication/baroud-emnlp2026-dpipi" view="4" >}}

Additional papers:

- [Janzen et al. "Gendered Prompting and LLM Code Review: How Gender Cues in the Prompt Shape Code Quality and Evaluation"](https://arxiv.org/abs/2603.24359)
- [Jakob et al. "Exploring Confirmation Bias: LLMs Perceive Democratic Claims as More Truthful Independently of their Content"]()
- [Ahmad et al. "Does Finetuning with Scientific Data Increase Hallucinations? A Multi-domain Factuality Evaluation of LLMs"](https://arxiv.org/abs/2606.21359v2)
- [Castle et al. "The Sum Is Less Than Its Parts: Decomposing the Attention Write by Source Detects Contextual Hallucinations"]()

