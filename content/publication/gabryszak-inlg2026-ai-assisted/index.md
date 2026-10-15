---
title: 'AI-Assisted Length-Constrained Summarization in News Agency Workflows'
authors:
- Aleksandra Gabryszak
- Damian Jaspar
- Shushen Manakhimova
- Leonhard Hennig
date: '2026-10-17'
publishDate: '2026-10-14T03:10:18.998131Z'
publication_types:
- paper-conference
publication: '*Non-archival poster presentation at INLG 2026*'
abstract: 'Large language models are used for text transformation, yet are often evaluated outside editorial workflows. We present a case study from a German news agency: AI-assisted, length-constrained summarization with an editing tool integrated into the editorial process. Editors often need to shorten articles to fixed character limits to fit publication layouts. We developed a tool that generates summaries for target character lengths within a tolerance: it iteratively checks and revises output length until it meets the tolerance or iteration limit. Moreover, generation is predominantly extractive, using abstractive reformulation when necessary and aiming to preserve factual accuracy, newsworthiness, and editorial style. After LLM generation, editors use a side-by-side view showing retained source content, helping them assess faithfulness. They then adjust the summary to the required length and correct content. After finalizing text, editors rate the LLM output on a five-point publishability scale and select problem categories such as style, coherence, missing or distorted information, hallucinations, and redundancy, with additional issues entered as free text. The tool logs time on task, target and tolerance lengths, and source, generated, and final texts. The system has been deployed at the agency. Initial evaluations with Claude Sonnet indicate high summary quality on average, with about half of the summaries rated as immediately publishable. Missing information emerged as the most common issue, while coherence and redundancy problems were rare. We also observe strong adherence to target lengths, with average deviations well below the ±100-character tolerance and most outputs requiring limited iterative refinement. Early feedback from editors suggests that the tool can support efficient newsroom workflows and reduce editing effort, particularly for shorter texts. The ongoing evaluation will extend these findings to additional test instances, editors, and models, and will include a usability study.'
url_pdf: 
links:
- name: URL
  url: https://openreview.net/forum?id=FXv1y2CZjM 

---
