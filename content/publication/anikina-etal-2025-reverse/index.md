---
title: 'Reverse Probing: Evaluating Knowledge Transfer via Finetuned Task Embeddings for Coreference Resolution'
authors:
- Tatiana Anikina
- Arne Binder
- David Harbecke
- Stalin Varanasi
- Leonhard Hennig
- Simon Ostermann
- Sebastian Möller
- Josef van Genabith
date: '2025-03-17'
publication_types:
- paper-conference
publication: '*Proceedings of the 10th Workshop on Representation Learning for NLP (RepL4NLP-2025)*'
publication_short: RepL4NLP 2025
abstract: In this work, we reimagine classical probing to evaluate knowledge transfer from simple source to more complex target tasks. Instead of probing frozen representations from a complex source task on diverse simple target probing tasks (as usually done in probing), we explore the effectiveness of embeddings from multiple simple source tasks on a single target task. We select coreference resolution, a linguistically complex problem requiring contextual understanding, as focus target task, and test the usefulness of embeddings from comparably simpler tasks tasks such as paraphrase detection, named entity recognition, and relation extraction. Through systematic experiments, we evaluate the impact of individual and combined task embeddings. Our findings reveal that task embeddings vary significantly in utility for coreference resolution, with semantic similarity tasks (e.g., paraphrase detection) proving most beneficial. Additionally, representations from intermediate layers of fine-tuned models often outperform those from final layers. Combining embeddings from multiple tasks consistently improves performance, with attention-based aggregation yielding substantial gains. These insights shed light on relationships between task-specific representations and their adaptability to complex downstream tasks, encouraging further exploration of embedding-level task transfer.

url_pdf: https://openreview.net/pdf?id=V4ssTPCogS
links:
- name: URL
  url: https://openreview.net/forum?id=V4ssTPCogS
---
