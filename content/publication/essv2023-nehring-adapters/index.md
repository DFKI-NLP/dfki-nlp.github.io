---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Adapters for Resource-Efficient Deployment of NLU Models"
authors: ["Jan Nehring", "Nils Feldhus", "Akhyar Ahmed"]
date: 2023-03-03
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: 2023-03-03

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: "Studientexte zur Sprachkommunikation: Elektronische Sprachsignalverarbeitung 2023"
publication_short: "ESSV 2023"

abstract: "Modern Transformer-based language models such as BERT are huge and, therefore, expensive to deploy in practical applications. In environments such as commercial chatbot-as-a-service platforms that deploy many NLP models in parallel, less powerful models with a smaller number of parameters are an alternative to transformers to keep deployment costs down, at the cost of lower accuracy values. This paper compares different models for Intent Detection concerning their memory footprint, quality of Intent Detection, and processing speed. Many taskspecific Adapters can share one large transformer model with the Adapter framework.  The deployment of 100 NLU models requires 1 GB of memory for the proposed BERT+Adapter architecture, compared to 41.78 GB for a BERT-only architecture."
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

url_pdf: "https://www.essv.de/pdf/2023_217_224.pdf"
url_code: "https://github.com/jnehring/ESSV2023-Adapters-for-Resource-Efficient-Deployment-of-NLU-models"
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
