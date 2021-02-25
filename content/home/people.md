---
# A "Meet the Team" section created with the People widget.
# This section displays people from `content/authors/` which belong to the `user_groups` below.
widget: people
headless: true
active: true
weight: 70

title: People
subtitle: 

content:
  user_groups: 
    - Principal Investigators
    - Researchers
    - PhD Students
    - Software Engineers
    - Visitors
    - Alumni


  # Default filter index (e.g. 0 corresponds to the first `filter_button` instance below).
  filter_default: 0

  # Filter toolbar (optional).
  # Add or remove as many filters (`filter_button` instances) as you like.
  # To show all items, set `tag` to "*".
  # To filter by a specific tag, set `tag` to an existing tag name.
  # To remove the toolbar, delete the entire `filter_button` block.
  filter_button:
  - name: All
    tag: '*'
  - name: Language Understanding
    tag: Language Understanding
  - name: Low-Resource Learning
    tag: Low-Resource Learning
  - name: Dialogue
    tag: Dialogue
  - name: Information Extraction
    tag: Information Extraction
  
design:
  # Show user's social networking links? (true/false)
  show_social: true
  # Show user's interests? (true/false)
  show_interests: true
  # Show user's role?
  show_role: false
  # Show user's organizations/affiliations?
  show_organizations: false

  background:
  # Apply a background color, gradient, or image.
  #   Uncomment (by removing `#`) an option to apply it.
  #   Choose a light or dark text color by setting `text_color_light`.
  #   Any HTML color name or Hex value is valid.
  
  # Background color.
  # color: "navy"
  
  # Background gradient.
  # gradient_start: "DeepSkyBlue"
  # gradient_end: "SkyBlue"
  
  # Background image.
  # image: "background.jpg"  # Name of image in `static/img/`.
  # image_darken: 0.6  # Darken the image? Range 0-1 where 0 is transparent and 1 is opaque.

  # Text color (true=light or false=dark).
  # text_color_light: true  
--- 
