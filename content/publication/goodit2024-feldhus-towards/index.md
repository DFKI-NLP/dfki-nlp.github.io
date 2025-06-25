---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Towards Modeling and Evaluating Instructional Explanations in Teacher-Student Dialogues"
authors: ["Nils Feldhus", "Aliki Anagnostopoulou", "Qianli Wang", "Milad Alshomary", "Henning Wachsmuth", "Daniel Sonntag", "Sebastian Möller"]
date: 2024-09-04
doi: "10.1145/3677525.3678665"

# Schedule page publish date (NOT publication's date).
publishDate: 2024-09-04

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["1"]

# Publication name and optional abbreviated publication name.
publication: "Proceedings of the 2024 International Conference on Information Technology for Social Good"
publication_short: "GoodIT'24"

abstract: "For dialogues in which teachers explain difficult concepts to students, didactics research often debates which teaching strategies lead to the best learning outcome. In this paper, we test if LLMs can reliably annotate such explanation dialogues, s.t. they could assist in lesson planning and tutoring systems. We first create a new annotation scheme of teaching acts aligned with contemporary teaching models and re-annotate a dataset of conversational explanations about communicating scientific understanding in teacher-student settings on five levels of the explainee’s expertise: ReWIRED contains three layers of acts (Teaching, Explanation, Dialogue) with increased granularity (span-level). We then evaluate language models on the labeling of such acts and find that the broad range and structure of the proposed labels is hard to model for LLMs such as GPT-3.5/-4 via prompting, but a fine-tuned BERT can perform both act classification and span labeling well. Finally, we operationalize a series of quality metrics for instructional explanations in the form of a test suite, finding that they match the five expertise levels well."
# Summary. An optional shortened abstract.
summary: ""

tags: [Interpretability]
categories: []
featured: false

# Custom links (optional).
#   Uncomment and edit lines below to show custom links.
# links:
# - name: Follow
#   url: https://twitter.com
#   icon_pack: fab
#   icon: twitter

url_pdf:
url_code: 
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
projects: [XAINES]

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: ""
---
