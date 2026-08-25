---
title: 'Training-Free Character-Length Control in Summarization with Diffusion Language Models'
authors:
- Steffen Castle
- Nils Feldhus
- Christopher Ebert
- Leonhard Hennig
- Sebastian Möller
date: '2026-08-29'
publishDate: '2026-08-25T13:10:18.998131Z'
publication_types:
- paper-conference
publication: '*Proceedings of the 2026 Conference on Empirical Methods in Natural Language Processing (EMNLP 2026)*'
abstract: 'Summarization with a fixed character length is important for tasks such as headline and article preview generation, where text must fit an exact space. Autoregressive language models (LMs) struggle with precise character-length control: training-based methods require task-specific fine-tuning, while zero-shot prompting strategies achieve only approximate compliance. We propose DELTA (Diffusion Expected Length Targeting Algorithm), a training-free inference-time method for masked diffusion LMs that estimates expected character length at each denoising step and dynamically inserts or removes masked positions to steer toward a target length. DELTA requires no fine-tuning and applies to any off-the-shelf masked diffusion LM. Across three summarization benchmarks, it reduces character-length errors by an order of magnitude compared to baselines while maintaining competitive summary quality.'
url_pdf: 
links:
- name: URL
  url: https://openreview.net/forum?id=JYhyrRfBiJ

---
