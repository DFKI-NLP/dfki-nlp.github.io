---
title: 'The Sum Is Less Than Its Parts: Decomposing the Attention Write by Source Detects Contextual Hallucinations'
authors:
- Steffen Castle
- Maximilian Dustin Nasert
- Christopher Ebert
- Leonhard Hennig
- Sebastian Möller
- Nils Feldhus
date: '2026-10-29'
publishDate: '2026-10-14T03:10:18.998131Z'
publication_types:
- paper-conference
publication: '*Proceedings of the 9th {B}lackbox{NLP} Workshop: Analyzing and Interpreting Neural Networks for {NLP}*'
abstract: "When a language model answers from a retrieved document, its attention heads mix evidence from the context with evidence from the model's own self-generated tokens and write the sum into the residual stream. We split each head's write into these two source-specific contributions before they are summed, and find that the two sides are complementary. The context write, read out along the model's unembedding, gives a training-free groundedness score, GroundHOG-U. The response write (its magnitude and directional agreement with the other residual writes) gives a supervised hallucination detector, GroundHOG. Across grounded-generation benchmarks and model families, GroundHOG beats prior internal-state detectors, and GroundHOG-U is the strongest training-free groundedness signal on the multi-model benchmarks."
url_pdf: https://openreview.net/pdf?id=YaVhAR7uT0
links:
- name: URL
  url: https://openreview.net/forum?id=YaVhAR7uT0

---
