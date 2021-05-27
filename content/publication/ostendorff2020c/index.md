---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Aspect-based Document Similarity for Research Papers"
authors: ["Malte Ostendorff", "Terry Ruas", "Till Blume", "Bela Gipp", "Georg Rehm"]
date: 2020-12-27T12:17:32+02:00
doi: "10.18653/v1/2020.coling-main.545"

# Schedule page publish date (NOT publication's date).
publishDate: 2020-12-27T12:17:32+02:00

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: "Proceedings of the 28th International Conference on Computational Linguistics"
publication_short: "COLING 2020"

abstract: "Traditional document similarity measures provide a coarse-grained distinction between similar and dissimilar documents. Typically, they do not consider in what aspects two documents are similar. This limits the granularity of applications like recommender systems that rely on document similarity. In this paper, we extend similarity with aspect information by performing a pairwise document classification task. We evaluate our aspect-based document similarity for research papers. Paper citations indicate the aspect-based similarity, i.e., the section title in which a citation occurs acts as a label for the pair of citing and cited paper. We apply a series of Transformer models such as RoBERTa, ELECTRA, XLNet, and BERT variations and compare them to an LSTM baseline. We perform our experiments on two newly constructed datasets of 172,073 research paper pairs from the ACL Anthology and CORD-19 corpus. Our results show SciBERT as the best performing system. A qualitative examination validates our quantitative results. Our findings motivate future research of aspect-based document similarity and the development of a recommender system based on the evaluated techniques. We make our datasets, code, and trained models publicly available. "

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

url_pdf: "https://ostendorff.org/assets/pdf/ostendorff2020c.pdf"
url_code: "https://github.com/malteos/aspect-document-similarity"
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
