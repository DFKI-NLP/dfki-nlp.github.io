---
# Documentation: https://wowchemy.com/docs/managing-content/

title: "Automatic Extraction of Medication Mentions from Tweets—Overview of the BioCreative VII Shared Task 3 Competition"
authors: [Davy Weissenbacher, Karen O’Connor, Siddharth Rawal, Yu Zhang, Richard Tzong-Han Tsai, Timothy Miller, Dongfang Xu, Carol Anderson, Bo Liu, Qing Han, Jinfeng Zhang, Igor Kulev, Berkay Köprü, Raul Rodriguez-Esteban, Elif Ozkirimli, Ammer Ayach, Roland Roller, Stephen Piccolo, Peijin Han, V G Vinod Vydiswaran, Ramya Tekumalla, Juan M Banda, Parsa Bagherzadeh, Sabine Bergler, João F Silva, Tiago Almeida, Paloma Martinez, Renzo Rivera-Zavala, Chen-Kai Wang, Hong-Jie Dai, Luis Alberto Robles Hernandez, Graciela Gonzalez-Hernandez]
date: 2023-02-15T10:33:03+02:00
doi: "10.1093/database/baac108"

# Schedule page publish date (NOT publication's date).
publishDate: 2023-04-23T10:33:03+02:00

# Publication type.
# Legend: 0 = Uncategorized; 1 = Conference paper; 2 = Journal article;
# 3 = Preprint / Working Paper; 4 = Report; 5 = Book; 6 = Book section;
# 7 = Thesis; 8 = Patent
publication_types: ["2"]

# Publication name and optional abbreviated publication name.
publication: "Database"
publication_short: "Database"

abstract: "This study presents the outcomes of the shared task competition BioCreative VII (Task 3) focusing on the extraction of medication names from a Twitter user’s publicly available tweets (the user’s ‘timeline’). In general, detecting health-related tweets is notoriously challenging for natural language processing tools. The main challenge, aside from the informality of the language used, is that people tweet about any and all topics, and most of their tweets are not related to health. Thus, finding those tweets in a user’s timeline that mention specific health-related concepts such as medications requires addressing extreme imbalance. Task 3 called for detecting tweets in a user’s timeline that mentions a medication name and, for each detected mention, extracting its span. The organizers made available a corpus consisting of 182 049 tweets publicly posted by 212 Twitter users with all medication mentions manually annotated. The corpus exhibits the natural distribution of positive tweets, with only 442 tweets (0.2\\%) mentioning a medication. This task was an opportunity for participants to evaluate methods that are robust to class imbalance beyond the simple lexical match. A total of 65 teams registered, and 16 teams submitted a system run. This study summarizes the corpus created by the organizers and the approaches taken by the participating teams for this challenge. The corpus is freely available at https://biocreative.bioinformatics.udel.edu/tasks/biocreative-vii/track-3/. The methods and the results of the competing systems are analyzed with a focus on the approaches taken for learning from class-imbalanced data."
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

url_pdf: "https://doi.org/10.1093/database/baac108"
url_code: ""
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
projects: [PRIMA-AI, vALID]

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: ""
---
