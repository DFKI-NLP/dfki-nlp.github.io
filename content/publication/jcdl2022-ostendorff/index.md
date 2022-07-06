---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Specialized Document Embeddings for Aspect-based Similarity of Research Papers"
authors: ["Malte Ostendorff", "Till Blume", "Terry Ruas", "Bela Gipp", "Georg Rehm"]
date: 2022-07-06T09:33:03+02:00
doi: "10.1145/3529372.3530912"

# Schedule page publish date (NOT publication's date).
publishDate: 2022-07-06T09:33:03+02:00

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: "Proceedings of the ACM/IEEE Joint Conference on Digital Libraries 2022"
publication_short: "JCDL 2022"

abstract: "Document embeddings and similarity measures underpin content-based recommender systems, whereby a document is commonly represented as a single generic embedding. However, similarity computed on single vector representations provides only one perspective on document similarity that ignores which aspects make two documents alike. To address this limitation, aspect-based similarity measures have been developed using document segmentation or pairwise multi-class document classification. While segmentation harms the document coherence, the pairwise classification approach scales poorly to large scale corpora. In this paper, we treat aspect-based similarity as a classical vector similarity problem in aspect-specific embedding spaces. We represent a document not as a single generic embedding but as multiple specialized embeddings. Our approach avoids document segmentation and scales linearly w.r.t. the corpus size. In an empirical study, we use the Papers with Code corpus containing 157, 606 research papers and consider the task, method, and dataset of the respective research papers as their aspects. We compare and analyze three generic document embeddings, six specialized document embeddings and a pairwise classification baseline in the context of research paper recommendations. As generic document embeddings, we consider FastText, SciBERT, and SPECTER. To compute the specialized document embeddings, we compare three alternative methods inspired by retrofitting, fine-tuning, and Siamese networks. In our experiments, Siamese SciBERT achieved the highest scores. Additional analyses indicate an implicit bias of the generic document embeddings towards the dataset aspect and against the method aspect of each research paper. Our approach of aspect-based document embeddings mitigates potential risks arising from implicit biases by making them explicit. This can, for example, be used for more diverse and explainable recommendations."

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

url_pdf: "https://arxiv.org/pdf/2203.14541"
url_code: "https://github.com/malteos/aspect-document-embeddings"
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
