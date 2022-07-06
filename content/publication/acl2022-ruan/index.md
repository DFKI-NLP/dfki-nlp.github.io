---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "HiStruct+: Improving Extractive Text Summarization with Hierarchical Structure Information"
authors: ["Qian Ruan", "Malte Ostendorff", "Georg Rehm"]
date: 2022-07-06T09:25:24+02:00
doi: "10.18653/v1/2022.findings-acl.102"

# Schedule page publish date (NOT publication's date).
publishDate: 2022-07-06T09:25:24+02:00

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: "Findings of the Association for Computational Linguistics: ACL 2022"
publication_short: "ACL 2022 Findings"

abstract: "Transformer-based language models usually treat texts as linear sequences. However, most texts also have an inherent hierarchical structure, i.e., parts of a text can be identified using their position in this hierarchy. In addition, section titles usually indicate the common topic of their respective sentences. We propose a novel approach to formulate, extract, encode and inject hierarchical structure information explicitly into an extractive summarization model based on a pre-trained, encoder-only Transformer language model (HiStruct+ model), which improves SOTA ROUGEs for extractive summarization on PubMed and arXiv substantially. Using various experimental settings on three datasets (i.e., CNN/DailyMail, PubMed and arXiv), our HiStruct+ model outperforms a strong baseline collectively, which differs from our model only in that the hierarchical structure information is not injected. It is also observed that the more conspicuous hierarchical structure the dataset has, the larger improvements our method gains. The ablation study demonstrates that the hierarchical position information is the main contributor to our model’s SOTA performance."

# Summary. An optional shortened abstract.
summary: ""

tags: []
categories: []
featured: false

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

url_pdf: "https://aclanthology.org/2022.findings-acl.102.pdf"
url_code: "https://github.com/QianRuan/histruct"
url_dataset:
url_poster:
url_project:
url_slides:
url_source:
url_video:

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder. 
# Focal points: Smart, Center, TopLeft, Top, TopRight, Left, Right, BottomLeft, Bottom, BottomRight.
image:
  caption: ""
  focal_point: ""
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects: []

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: ""
---
