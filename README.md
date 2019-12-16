# How-To

First, install Hugo (https://gohugo.io/):
```bash
wget https://github.com/gohugoio/hugo/releases/download/v0.59.1/hugo_extended_0.59.1_Linux-64bit.tar.gz
tar -xvf hugo_extended_0.59.1_Linux-64bit.tar.gz
sudo mv hugo /usr/local/bin/
```

Clone the website repo:
```bash
git clone git@github.com:DFKI-NLP/dfki-nlp.github.io.git
```

Init all submodules in the repo:
```bash
cd dfki-nlp.github.io
git submodule update --init --recursive
```

Serve the website locally (reachable at http://localhost:1313/):
```bash
hugo server
```

## Add a publication

Assuming that we are in the top-level directory, create a new publication entry:
```bash
hugo new --kind publication publication/<my-publication>
```

Go to `content > publication > <my-publication>` and edit `index.md`.
Here is an example: https://raw.githubusercontent.com/DFKI-NLP/dfki-nlp.github.io/src/content/publication/Fine-tuning-Pre-Trained-Transformer-Language-Models-to-Distantly-Supervised-Relation-Extraction/index.md

If you add a file called `cite.bib` with a bibtex entry, hugo will create a cite button.
File (e.g. poster) can be added to the directory and linked to a "poster" button (see example).
Links to the paper and/or demo can be added as well.

More details can be found here: https://sourcethemes.com/academic/docs/managing-content/#manually
There is also a way to automatically create a publication from bibtex but it did not work for me: https://sourcethemes.com/academic/docs/managing-content/#automatically

## Publish Website

To publish your changes, add and commit all your changes (make sure the website looks as expected with hugo server):
```bash
git commit -m "Added my latest NeurIPS publication"
git push origin src
```

IMPORTANT: Only push to the src branch!
The repository contains a Github action that automatically builds and publishes the static page to the master branch.