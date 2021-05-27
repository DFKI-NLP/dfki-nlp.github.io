---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Evaluating Document Representations for Content-based Legal Literature Recommendations"
authors: ["Malte Ostendorff", "Elliott Ash", "Terry Ruas", "Bela Gipp", "Julian Moreno-Schneider", "Georg Rehm"]
date: 2021-05-27T12:18:03+02:00
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: 2021-05-27T12:18:03+02:00

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: "Proceedings of the 18th International Conference on Artificial Intelligence and Law"
publication_short: "ICAIL 2021"

abstract: "Recommender systems assist legal professionals in finding relevant literature for supporting their case. Despite its importance for the profession, legal applications do not reflect the latest advances in recommender systems and representation learning research. Simultaneously, legal recommender systems are typically evaluated in small-scale user study without any public available benchmark datasets. Thus, these studies have limited reproducibility. To address the gap between research and practice, we explore a set of state-of-the-art document representation methods for the task of retrieving semantically related US case law. We evaluate text-based (e.g., fastText, Transformers), citation-based (e.g., DeepWalk, Poincaré), and hybrid methods. We compare in total 27 methods using two silver standards with annotations for 2,964 documents. The silver standards are newly created from Open Case Book and Wikisource and can be reused under an open license facilitating reproducibility. Our experiments show that document representations from averaged fastText word vectors (trained on legal corpora) yield the best results, closely followed by Poincaré citation embeddings. Combining fastText and Poincaré in a hybrid manner further improves the overall result. Besides the overall performance, we analyze the methods depending on document length, citation count, and the coverage of their recommendations. We make our source code, models, and datasets publicly available at this https URL. "

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

url_pdf: "https://ostendorff.org/assets/pdf/ostendorff2021.pdf"
url_code: "https://github.com/malteos/legal-document-similarity/"
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
