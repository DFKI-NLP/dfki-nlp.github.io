# Add a publication / edit a post
Clone the website repo:
```bash
git clone git@github.com:DFKI-NLP/dfki-nlp.github.io.git
```

Create a new publication, e.g. by copying an old one:
```bash
cp -r content/publication/acl2022-repl4nlp-chen-fewie/ content/publication/<your-new-folder-name>
```
And edit the files index.md and cite.bib.
Then just commit and push. Check whether the commit was built correctly (e.g. here: https://github.com/DFKI-NLP/dfki-nlp.github.io/actions)

Add / update a news post:
```bash
cp -r content/post/acl2022 content/post/<new-post>
```
and edit index.md
Then just commit and push. Check whether the commit was built correctly (e.g. here: https://github.com/DFKI-NLP/dfki-nlp.github.io/actions)

# How-To (with Hugo)

For local testing, install Hugo, following the instructions here https://docs.hugoblox.com/getting-started/install-hugo/ 

Note: You can install hugo in a Conda environment with 'conda install go' followed by 'pip install hugo'.

Clone the website repo:
```bash
git clone git@github.com:DFKI-NLP/dfki-nlp.github.io.git
```

Serve the website locally (reachable at http://localhost:1313/):
```bash
hugo server
```


## Publish Website

To publish your changes, add and commit all your changes (make sure the website looks as expected with hugo server):
```bash
git commit -m "Added my latest NeurIPS publication"
git push origin src
```

IMPORTANT: Only push to the src branch!
The repository contains a Github action that automatically builds and publishes the static page to the master branch.
