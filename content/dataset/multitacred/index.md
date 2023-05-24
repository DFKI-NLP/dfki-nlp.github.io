---
title: The MultiTACRED dataset
#summary: "MultiTACRED is a multilingual version of the large-scale [TAC Relation Extraction Dataset](https://nlp.stanford.edu/projects/tacred). It covers 12 typologically diverse languages from 9 language families, and was created by machine-translating the instances of the original TACRED dataset and automatically projecting their entity annotations. You can find the paper [here](https://arxiv.org/abs/2305.04582) and the code used for creating dataset here: https://github.com/DFKI-NLP/MultiTACRED"
summary: "MultiTACRED is a multilingual version of the large-scale [TAC Relation Extraction Dataset](https://nlp.stanford.edu/projects/tacred). It covers 12 typologically diverse languages from 9 language families, and was created by machine-translating the instances of the original TACRED dataset and automatically projecting their entity annotations. For details of the original TACRED's
data collection and annotation process, see the [Stanford paper](https://aclanthology.org/D17-1004/). Translations are
syntactically validated by checking the correctness of the XML tag markup. Any translations with an invalid tag
structure, e.g. missing or invalid head or tail tag pairs, are discarded (on average, 2.3% of the instances).

Languages covered are: Arabic, Chinese, Finnish, French, German, Hindi, Hungarian, Japanese, Polish,
 Russian, Spanish, Turkish. Intended use is supervised relation classification. Audience - researchers.

The dataset will be released via the LDC (link will follow).

Please see [our ACL paper](https://arxiv.org/abs/2305.04582) for full details. You can find the Github repo containing the translation and experiment code here [https://github.com/DFKI-NLP/MultiTACRED](https://github.com/DFKI-NLP/MultiTACRED)."

tags:
- Relation Extraction
- Multilinguality
- Transfer Learning

date: 2023-05-24T00:00:00+00:00

# Optional external URL for project (replaces project detail page).
external_link: https://github.com/DFKI-NLP/MultiTACRED

image:
  caption: 
  focal_point: Center
---
