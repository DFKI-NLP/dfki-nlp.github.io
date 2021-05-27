---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Pairwise Multi-Class Document Classification for Semantic Relations between Wikipedia Articles"
authors: ["Malte Ostendorff", "Terry Ruas", "Moritz Schubotz", "Georg Rehm", "Bela Gipp"]
date: 2020-08-27T12:17:42+02:00
doi: "10.1145/3383583.3398525"

# Schedule page publish date (NOT publication's date).
publishDate: 2020-08-22T12:17:42+02:00

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: "Proceedings of the ACM/IEEE Joint Conference on Digital Libraries"
publication_short: "JCDL 2020"

abstract: "Many digital libraries recommend literature to their users considering the similarity between a query document and their repository. However, they often fail to distinguish what is the relationship that makes two documents alike. In this paper, we model the problem of finding the relationship between two documents as a pairwise document classification task. To find the semantic relation between documents, we apply a series of techniques, such as GloVe, Paragraph-Vectors, BERT, and XLNet under different configurations (e.g., sequence length, vector concatenation scheme), including a Siamese architecture for the Transformer-based systems. We perform our experiments on a newly proposed dataset of 32,168 Wikipedia article pairs and Wikidata properties that define the semantic document relations. Our results show vanilla BERT as the best performing system with an F1-score of 0.93, which we manually examine to better understand its applicability to other domains. Our findings suggest that classifying semantic relations between documents is a solvable task and motivates the development of recommender systems based on the evaluated techniques. The discussions in this paper serve as first steps in the exploration of documents through SPARQL-like queries such that one could find documents that are similar in one aspect but dissimilar in another. "

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

url_pdf: "https://ostendorff.org/assets/pdf/ostendorff2020.pdf"
url_code: "https://github.com/malteos/semantic-document-relations"
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
