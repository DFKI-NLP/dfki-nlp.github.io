---
# Documentation: https://sourcethemes.com/academic/docs/managing-content/

title: "MobIE: A German Dataset for Named Entity Recognition, Entity Linking and Relation Extraction in the Mobility Domain"
authors: [Leonhard Hennig, Phuc Tran Truong, Aleksandra Gabryszak]
date: 2021-07-23T00:00:00+00:00
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: 2021-07-23T11:36:10+02:00

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: "Proceedings of KONVENS 2021"
publication_short: "KONVENS 2021"

abstract: ""

# Summary. An optional shortened abstract.
summary: "We describe the MobIE dataset of German mobility texts annotated for NER, EL and RE."

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

url_pdf: https://github.com/DFKI-NLP/MobIE/blob/master/Konvens_2021_Daystream_Corpus.pdf
url_code: https://github.com/DFKI-NLP/MobIE
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
projects: [Daystream,Cora4NLP]

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: ""
---
We present MobIE, a German-language dataset, which is human-annotated with 20 coarse- and fine-grained entity types and entity linking information for geographically linkable entities. The dataset consists of 3,541 social media texts and traffic reports with 104K tokens, and contains 23,4K annotated entities, 15k of which are linked to a knowledge base. A subset of the dataset is human-annotated with seven mobility-related, n-ary relation types, while the remaining documents are annotated using a weakly-supervised labeling approach implemented with the Snorkel framework. To the best of our knowledge, this is the first German-language dataset that combines annotations for NER, EL and RE, and thus can be used for joint and multi-task learning of these fundamental information extraction tasks. We make MobIE public at https://github.com/dfki-nlp/mobie.
