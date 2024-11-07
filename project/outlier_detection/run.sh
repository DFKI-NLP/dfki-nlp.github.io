#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# Run the first Python script
python outlier_word.py

echo "## outlier_word.py is running.. ##"

# Run the second Python script
python outlier_doc.py

echo "## outlier_word.py is running.. ##"

# Run the third Python script
python try2.py

echo "## try2.py is running.. ##"