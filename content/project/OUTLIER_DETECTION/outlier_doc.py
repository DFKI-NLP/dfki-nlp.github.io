from flask import Flask, request, render_template_string
import pandas as pd
import re
import math
import nltk
from nltk.corpus import stopwords
from autocorrect import Speller
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import io
import base64
from matplotlib.figure import Figure
import numpy as np
import mpld3
from mpld3 import plugins
import spacy
import plotly.express as px
import ipywidgets as widgets
from IPython.display import display, HTML
import matplotlib.patches as patches


# Load the spaCy language model
nlp = spacy.load('en_core_web_sm')

# Download the stopwords corpus if not already downloaded
nltk.download('stopwords')

app = Flask(__name__)


# Function to check if a token is a noun or a proper noun
def is_noun_or_proper_noun(token):
    return token.pos_ in {'NOUN', 'PROPN'}


# Function to calculate the Outlier Score (OS) and Inverse Document Frequency (IDF)
def calculate_OS_IDF(collection):
    # Initialize dictionaries to store document frequencies (DF) and inverse document frequencies (IDF)
    document_frequencies = {}
    inverse_document_frequencies = {}
    # Tokenize documents into terms using spaCy
    tokenized_documents = [nlp(doc) for doc in collection]

    # Extract all noun and proper noun terms from each document
    noun_terms_documents = []
    for doc in tokenized_documents:
        noun_terms = [token.text for token in doc if is_noun_or_proper_noun(token)]
        noun_terms_documents.append(noun_terms)
        unique_terms = set(noun_terms)
        for term in unique_terms:
            document_frequencies[term] = document_frequencies.get(term, 0) + 1
    # Total number of documents (each row counts as one document)
    total_documents = len(collection)

    # Calculate IDF score for each term
    for term, df in document_frequencies.items():
        inverse_document_frequencies[term] = round(math.log(total_documents / (1 + df)), 2)

    # Calculate average IDF per document (each row counts as one document)
    average_term_idf_per_document = []
    max_idf_scores = []
    rarest_terms = []

    for doc in noun_terms_documents:
        doc_idf_values = [inverse_document_frequencies.get(term, 0) for term in doc]
        if doc_idf_values:
            avg_idf = round(sum(doc_idf_values) / len(doc_idf_values), 2)  # Fixed to divide by len(doc_idf_values)
            sorted_terms = sorted(set(doc), key=lambda term: -inverse_document_frequencies.get(term, 0))
            rarest_term = ', '.join(sorted_terms[:10])
            max_idf = [f"{inverse_document_frequencies.get(term, 0):.2f}" for term in sorted_terms[:10]]
        else:
            avg_idf = 0
            max_idf = [f"{0:.2f}" for _ in range(10)]
            rarest_term = ""
        average_term_idf_per_document.append(f"{avg_idf:.2f}")
        max_idf_scores.append(max_idf)
        rarest_terms.append(rarest_term)

    return average_term_idf_per_document, max_idf_scores, rarest_terms


# Function to preprocess each document
def preprocess_document(doc):
    # Remove annotations like [** ... **]
    doc = re.sub(r'\[\*\*.*?\*\*\]', ' ', doc)

    # Remove standalone numbers
    doc = re.sub(r'\b\d+\b', ' ', doc)

    # Remove special characters except letters, digits, and spaces
    doc = re.sub(r'[^a-zA-Z0-9\s]', ' ', doc)

    # Replace multiple spaces with a single space
    doc = re.sub(r'\s+', ' ', doc)

    # Convert to lowercase
    doc = doc.lower()

    # Remove stopwords from the set of stop words
    stop_words = set(stopwords.words('english'))
    tokens = doc.split()
    filtered_tokens = [word for word in tokens if word not in stop_words]  # Filter out stop words

    # Reconstruct the document from filtered tokens
    doc = ' '.join(filtered_tokens)

    # Return the cleaned document
    return doc.strip()


# Function to correct spelling using autocorrect library
def autocorrect_spelling(doc):
    spell = Speller(fast=True)
    return spell(doc)


@app.route('/')
def index():
    return render_template_string("""
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Outlier Analyzer</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">

    <style>
        .container {
            margin-top: 50px;
        }
        .card-header {
            background-color: #66cc00;
            color: white;
        }
        .card-body {
            background-color: #f8f9fa; /* Light gray background */
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="text-center mb-4">Outlier Document</h1>
        <div class="card">
            <div class="card-header">
                <h4 class="card-title">Upload CSV</h4>
            </div>
            <div class="card-body">
                <form method="post" action="/upload" enctype="multipart/form-data" id="uploadForm">
                    <div class="form-group">
                        <input type="file" name="file" class="form-control-file" id="fileInput">
                    </div>
                    <div class="form-check">
                        <input class="form-check-input" type="checkbox" name="enable_automatic_correction" value="1" id="enableCorrectionCheckbox">
                        <label class="form-check-label" for="enableCorrectionCheckbox">
                        Enable Automatic Spelling Correction
                        </label>

                    </div>
                    <!-- Added tooltip to the upload button -->
                    <button type="submit" class="btn btn-primary" data-toggle="tooltip"  data-placement="right" title="Upload only one column CSV file!" id="uploadButton" disabled>Upload</button>
                </form>
                <div id="alertMessage" class="alert alert-danger mt-2" style="display: none;"></div>
            </div>
        </div>
    </div>
    <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
    <script>
        // Activate Bootstrap tooltips
        $(document).ready(function(){
            $('[data-toggle="tooltip"]').tooltip();

            // Enable the upload button only if a file is selected
            $('#fileInput').on('change', function() {
                if ($(this).val()) {
                    $('#uploadButton').prop('disabled', false);
                    $('#alertMessage').hide();
                } else {
                    $('#uploadButton').prop('disabled', true);
                }
            });

            // Form submission handler
            $('#uploadForm').on('submit', function(event) {
                const fileInput = $('input[name="file"]');
                const file = fileInput[0].files[0];
                if (!file) {
                    event.preventDefault();
                    $('#alertMessage').text('No file provided').show();
                } else if (!file.name.endsWith('.csv')) {
                    event.preventDefault();
                    $('#alertMessage').text('Please upload a CSV file').show();
                }
            });
        });
    </script>
</body>
</html>

    """)


@app.route('/upload', methods=['POST'])
def upload_csv():
    try:
        file = request.files['file']
        if not file:
            return render_template_string("""
                        <script>
                            window.onload = function() {
                                alert('No file provided');
                                window.history.back();
                            }
                        </script>
                    """)

        if not file.filename.endswith('.csv'):
            return render_template_string("""
                       <script>
                           window.onload = function() {
                               alert('Please upload a CSV file');
                               window.history.back();
                           }
                       </script>
                   """)

        # Read the CSV file
        df = pd.read_csv(file)

        # Check for single column
        if len(df.columns) != 1:
            return render_template_string("<h2>Please provide only a one-column dataset</h2>")

        # Store original text before preprocessing
        original_documents = df.iloc[:, 0].tolist()

        enable_automatic_correction = request.form.get('enable_automatic_correction') == '1'

        # Apply preprocessing and optional autocorrection
        preprocessed_documents = df.iloc[:, 0].apply(preprocess_document).tolist()

        if enable_automatic_correction:
            preprocessed_documents = [autocorrect_spelling(doc) for doc in preprocessed_documents]

        average_idf_scores, max_idf_scores, rarest_terms = calculate_OS_IDF(preprocessed_documents)

        output_df = pd.DataFrame({
            'Index': range(1, len(preprocessed_documents) + 1),
            'Original Text': original_documents,
            'Preprocessed Text': preprocessed_documents,
            'Rarity Score': average_idf_scores,
            'Rarest Terms': rarest_terms,
            'Term Rarity Score': max_idf_scores

        })

        def calculate_thresholds(df):
            mean_value = df['Rarity Score'].mean()
            std_dev_value = df['Rarity Score'].std()
            thresholds = {
                "First Standard Deviation Outlier Analysis": mean_value + 1 * std_dev_value,
                "Second Standard Deviation Outlier Analysis": mean_value + 2 * std_dev_value,
                "Third Standard Deviation Outlier Analysis": mean_value + 3 * std_dev_value
            }
            return thresholds

        def filter_data(df, option):
            if option == "Default" or option == "Reset":
                return df
            thresholds = calculate_thresholds(df)
            if option in thresholds:
                threshold = thresholds[option]
                filtered_df = df[df['Rarity Score'] >= threshold]
                return filtered_df

        dropdown = widgets.Dropdown(
            options=[
                'Default',
                'Reset',
                'First Standard Deviation Outlier Analysis',
                'Second Standard Deviation Outlier Analysis',
                'Third Standard Deviation Outlier Analysis'
            ],
            value='Default',
            description='Analysis:'
        )

        button = widgets.Button(description="Update Table")

        output = widgets.Output()

        # Function to display the initial data table
        def initial_display():
            with output:
                display(HTML(output_df.to_html(escape=False)))

        # Function to update the displayed table based on the selected option from the dropdown
        def update_display(b):
            output.clear_output()
            selected_option = dropdown.value
            filtered_df = filter_data(output_df, selected_option)
            with output:
                display(HTML(filtered_df.to_html(escape=False)))

        # Button click event handler
        def on_button_clicked(b):
            update_display(None)

        # Bind the button click event to the handler
        button.on_click(on_button_clicked)

        # Show the initial display of the output
        initial_display()

        # Calculate the statistics for the histogram
        rarity_scores = output_df['Rarity Score'].astype(float)
        mean_score = rarity_scores.mean()
        median_score = rarity_scores.median()
        std_dev_score = rarity_scores.std()

        # Store mean and standard deviation for future use
        stored_mean_score = mean_score
        stored_std_dev_score = std_dev_score

        thresholds = {
            "First Standard Deviation Outlier Analysis": mean_score + std_dev_score,
            "Second Standard Deviation Outlier Analysis": mean_score + 2 * std_dev_score,
            "Third Standard Deviation Outlier Analysis": mean_score + 3 * std_dev_score
        }

        # Create histogram plot with fixed size
        fig = Figure(figsize=(10, 6))  # Set a fixed size, e.g., 10 inches by 6 inches
        ax = fig.subplots()
        counts, bins, patches = ax.hist(rarity_scores, bins='auto', color='green', alpha=0.7, edgecolor='black')

        # Calculate the counts for each standard deviation range
        std_dev1_count = sum(rarity_scores >= mean_score + std_dev_score)
        std_dev2_count = sum(rarity_scores >= mean_score + 2 * std_dev_score)
        std_dev3_count = sum(rarity_scores >= mean_score + 3 * std_dev_score)

        # Plot mean and median lines
        ax.axvline(mean_score, color='blue', linestyle='--', linewidth=2)
        ax.axvline(median_score, color='orange', linestyle='--', linewidth=2)

        # Standard Deviation Lines without labels
        ax.axvline(mean_score + std_dev_score, color='yellow', linestyle='--', linewidth=2)
        ax.axvline(mean_score - std_dev_score, color='yellow', linestyle='--', linewidth=2)
        ax.axvline(mean_score + 2 * std_dev_score, color='yellow', linestyle='--', linewidth=2)
        ax.axvline(mean_score - 2 * std_dev_score, color='yellow', linestyle='--', linewidth=2)
        ax.axvline(mean_score + 3 * std_dev_score, color='yellow', linestyle='--', linewidth=2)
        ax.axvline(mean_score - 3 * std_dev_score, color='yellow', linestyle='--', linewidth=2)


        # Set axis limits to ensure the mean lines and shaded areas are visible
        ax.set_xlim([min(rarity_scores) - 1, max(rarity_scores) + 1])
        ax.set_ylim([0, max(counts) + 5])

        # Adjust x-axis ticks to show increments of 0.5 for more precise reading
        x_ticks = np.arange(np.floor(min(rarity_scores)) - 1, np.ceil(max(rarity_scores)) + 1, 0.5)
        ax.set_xticks(x_ticks)

        ax.set_title('Document Rarity Score Frequencies')
        ax.set_xlabel('Document Rarity Score')
        ax.set_ylabel('Frequency')

        # Add text labels with colored squares inside the histogram
        # Mean
        ax.add_patch(plt.Rectangle((0.76, 0.91), 0.03, 0.03, transform=ax.transAxes, color="blue", clip_on=False))
        ax.text(0.80, 0.92, 'Mean:', transform=ax.transAxes, fontsize=10,
                verticalalignment='center', horizontalalignment='left',
                bbox=dict(facecolor='none', edgecolor='none'))
        ax.text(0.91, 0.92, f'{mean_score:.2f}', transform=ax.transAxes, fontsize=10,
                verticalalignment='center', horizontalalignment='left',
                bbox=dict(facecolor='none', edgecolor='none'))

        # Median
        ax.add_patch(plt.Rectangle((0.76, 0.86), 0.03, 0.03, transform=ax.transAxes, color="orange", clip_on=False))
        ax.text(0.80, 0.87, 'Median:', transform=ax.transAxes, fontsize=10,
                verticalalignment='center', horizontalalignment='left',
                bbox=dict(facecolor='none', edgecolor='none'))
        ax.text(0.91, 0.87, f'{median_score:.2f}', transform=ax.transAxes, fontsize=10,
                verticalalignment='center', horizontalalignment='left',
                bbox=dict(facecolor='none', edgecolor='none'))

        # Std Dev
        ax.add_patch(plt.Rectangle((0.76, 0.81), 0.03, 0.03, transform=ax.transAxes, color="yellow", clip_on=False))
        ax.text(0.80, 0.82, 'Std Dev:', transform=ax.transAxes, fontsize=10,
                verticalalignment='center', horizontalalignment='left',
                bbox=dict(facecolor='none', edgecolor='none'))
        ax.text(0.91, 0.82, f'{std_dev_score:.2f}', transform=ax.transAxes, fontsize=10,
                verticalalignment='center', horizontalalignment='left',
                bbox=dict(facecolor='none', edgecolor='none'))

        # Convert the plot to a PNG image and then to a base64 string
        buf = io.BytesIO()
        fig.savefig(buf, format='png')
        buf.seek(0)
        histogram_png = base64.b64encode(buf.getvalue()).decode('utf-8')
        buf.close()

        # Create SVG container for the histogram image with fixed dimensions
        fixed_width = fig.get_size_inches()[0] * fig.dpi
        fixed_height = fig.get_size_inches()[1] * fig.dpi

        histogram_html = f'''
        <div style="text-align: center;">
            <svg width="{fixed_width}" height="{fixed_height}">
                <image xlink:href="data:image/png;base64,{histogram_png}" width="{fixed_width}" height="{fixed_height}"></image>
            </svg>
        </div>
        '''

        # Ensure rarity_scores is passed to JavaScript
        histogram_html += f'<script>const rarity_scores = {rarity_scores.tolist()};</script>'

        # Display the result
        histogram_html

        def generate_color_gradient(scores, max_alpha=0.8, alpha_gap=0.05):
            max_score = max(scores)
            sorted_scores = sorted(scores, reverse=True)

            colors = []
            for score in scores:
                rank = sorted_scores.index(score)
                alpha = max_alpha - rank * alpha_gap
                if alpha < 0:
                    alpha = 0
                color = f'rgba(255, 0, 0, {alpha})'  # Red color with varying transparency
                colors.append(color)

            return colors

        def highlightTerms(text, terms, scores):
            term_scores_map = {term: score for term, score in zip(terms, scores)}
            sorted_terms = sorted(terms, key=lambda term: -term_scores_map[term])
            scores_sorted = [term_scores_map[term] for term in sorted_terms]
            colors = generate_color_gradient(scores_sorted)

            term_color_map = {term: colors[i] for i, term in enumerate(sorted_terms)}

            return ' '.join(
                [
                    f"<span style='background-color: {term_color_map[word]};'>{word}</span>" if word in term_color_map else word
                    for word in text.split()
                ]
            )

        # for i, row in output_df.iterrows():
        # terms = row['Rarest Terms'].split(', ')
        # term_scores = row['Term Rarity Score']
        # original_text = row['Original Text']
        # highlighted_text = apply_highlighting(original_text, terms, term_scores)
        # output_df.at[i, 'Original Text'] = highlighted_text

        dropdown_html = f"""
        <div class="form-group">
            <label for="analysisDropdown">Select Analysis Type:</label>
            {dropdown}
            <button class="btn btn-primary" onclick="document.getElementById('updateTableButton').click();">Update Table</button>
        </div>
        """

        output_html = output_df.to_html(index=False, classes="table table-striped table-hover table-responsive",
                                        escape=False)

        output_html = output_html.replace(
            '<th>Rarity Score</th>',
            '<th>'
            + '<div class="dropdown">'
            + '<button class="btn btn-secondary dropdown-toggle" type="button" id="rarityDropdown" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">'
            + '<b data-toggle="tooltip" title="Click to sort rarity scores">Rarity <br> Score</b> <i class="fas fa-filter" style="color: white;"></i>'
            + '</button>'
            + '<div class="dropdown-menu" aria-labelledby="rarityDropdown">'

            + '<a class="dropdown-item" href="#" onclick="sortTable(\'rarity\', \'ascending\')">Ascending</a>'
            + '<a class="dropdown-item" href="#" onclick="sortTable(\'rarity\', \'descending\')">Descending</a>'
            + '</div></div></th>'
        )

        output_html = output_html.replace(
            '<th>Rarest Terms</th>',
            '<th>'
            + '<div class="dropdown">'
            + '<button class="btn btn-secondary dropdown-toggle" type="button" id="termsDropdown" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">'
            + '<b id="rarestTermsHeaderText" data-toggle="tooltip" title="Click to filter rarest terms">10 Rarest Terms</b> <i class="fas fa-filter" style="color: white;"></i>'
            + '</button>'
            + '<div class="dropdown-menu" aria-labelledby="termsDropdown">'
            + "".join(
                [f'<a class="dropdown-item" href="#" onclick="showTopTerms(event, {i}, \'default\')">{i}</a>' for i in
                 range(1, 11)]) +
            '</div></div></th>'
        )

        output_html = output_html.replace('<th>Original Text</th>', '<th>Original Text</th>')
        output_html = output_html.replace('<table', '<div class="table-responsive"><div class="container"><table')
        output_html = output_html.replace('</table>', '</table></div></div>')

        return render_template_string("""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>CSV Analyzer</title>
                <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
                <style>
                body {
            background: linear-gradient(135deg, #f5f7fa, #c3cfe2);
            color: #333;
            font-family: 'Arial', sans-serif;
        }
        h1 {
            font-size: 3rem;
            text-transform: uppercase;
            letter-spacing: 5px;
            color: #4a4a4a;
            display: flex;
            align-items: center;
            justify-content: center;
            position: relative;
            animation: fadeIn 2s ease-in-out;
        }
        h1:before, h1:after {
            content: '';
            flex: 1;
            height: 4px;
            background: #66cc00;
            margin: 0 10px;
            animation: slideIn 1s forwards;
        }
        @keyframes slideIn {
            from { width: 0; }
            to { width: 100%; }
        }
        .form-group {
            margin-top: 20px;
            animation: fadeIn 2s ease-in-out 0.5s;
        }
        .form-control-range {
            width: 100%;
            cursor: pointer;
        }
        #num_terms_label {
            font-size: 1.2rem;
            font-weight: bold;
            color: #66cc00;
        }
                    .container {
                        margin-top: 50px;
                    }
                    .highlight {
                        background-color: rgba(255, 0, 0, 0.3); /* Red color with alpha transparency */
                    }
                    .table-container {
            margin-top: 30px;
            overflow-x: auto;
            animation: fadeIn 2s ease-in-out 1s;
        }
        .table {
            width: 100%;
            border-collapse: collapse;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .table th, .table td {
            padding: 15px;
            text-align: left;
            border: 1px solid #343a40;
            animation: fadeIn 2s ease-in-out;
            border-bottom: 1px solid #ddd;
        }
        .table th {
            background-color: #66cc00;
            color: white;
            position: sticky;
            position: -webkit-sticky;
            top: 0;
            z-index: 1;
            border: 1px solid black;
        }

        .table-wrapper {
  max-height: 400px; /* Adjust as needed */
  overflow-y: auto;
}

.table-wrapper table {
  width: 100%;
  border-collapse: collapse;
}

.table-wrapper thead {
  position: sticky;
  top: 0;
  background: white; /* Adjust as needed */
  z-index: 1;
}


                    .th:nth-child(even),td:nth-child(2) {
                        max-width: 300px; /* Adjust the width as per your requirement */
                        overflow: hidden;
                        text-overflow: ellipsis;
                        white-space: normal; /* Allow text to wrap */
                        word-wrap: break-word; /* Ensure long words break into new lines */
                        background-color: rgb(215, 244, 223);
                    }

                    .th:nth-child(even),td:nth-child(3) {
                        background-color: rgb(240, 255, 240);
                    }
                    .th:nth-child(even),td:nth-child(1) {
                        background-color: rgb(240, 255, 240);
                    }
                    .th:nth-child(even),td:nth-child(5) {
                        background-color: rgb(240, 255, 240);
                    }
                    .th:nth-child(even),td:nth-child(4) {
                        background-color: rgb(215, 244, 223);
                    }
                    .th:nth-child(even),td:nth-child(6) {
                        background-color: rgb(215, 244, 223);
                    }

                    .table, .table th, .table td {
                    border: 1px solid #343a40 !important; /* Darker border color */
                    }
                    .table th, .table td {
                    border-width: 1px !important; /* Ensures the border width is consistent */
                    }

                    .dropdown-menu {
                        background-color: #f8f9fa; /* Light gray background */
                    }
                    .dropdown-item {
                        color: #333; /* Dark gray text */
                    }
                    .navbar {
                        background-color: #66cc00; /* Navbar background color */
                    }
                    .navbar-brand {
                        color: white !important; /* Navbar brand text color */
                    }
                    .navbar-nav .nav-link {
                        color: white !important; /* Navbar link text color */
                    }
                    .btn-secondary.dropdown-toggle {
                        background-color: #66cc00 !important; /* Dropdown toggle button background color */
                        border-color: #66cc00 !important; /* Dropdown toggle button border color */
                    }
                    .dropdown-menu a.dropdown-item {
                        color: #333 !important; /* Dropdown item text color */
                    }
                    .dropdown-menu a.dropdown-item:hover {
                        background-color: #f0f0f0 !important; /* Hover background color for dropdown items */
                    }
                    .overlay {
                        position: fixed;
                        display: none;
                        width: 100%;
                        height: 100%;
                        top: 0;
                        left: 0;
                        right: 0;
                        bottom: 0;
                        background-color:  rgba(0,0,0,0.5);
                        z-index: 2;
                        cursor: pointer;
                    }
                    .overlay-content {
                        position: absolute;
                        top: 50%;
                        left: 50%;
                        transform: translate(-50%, -50%);
                        text-align: center;
                        color: white;
                    }
                    .progress-overlay {
                        position: fixed;
                        display: none;
                        width: 100%;
                        height: 100%;
                        top: 0;
                        left: 0;
                        right: 0;
                        bottom: 0;
                        background-color: rgba(0,0,0,0.7);
                        z-index: 3;
                    }
                    .progress-container {
                        position: absolute;
                        top: 50%;
                        left: 50%;
                        transform: translate(-50%, -50%);
                        text-align: center;
                        color: white;
                        font-size: 20px;
                    }

                    .dropbtn {
  background-color: #4CAF50;
  color: white;
  padding: 16px;
  font-size: 16px;
  border: none;
  cursor: pointer;
}

.dropdown {
  position: relative;
  display: inline-block;
}

.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f9f9f9;
  min-width: 230px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
}

.dropdown-content a {
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: block;
}

.dropdown-content a:hover {background-color: #f1f1f1;}

.dropdown:hover .dropdown-content {
  display: block;
}

.dropdown:hover .dropbtn {
  background-color: #3e8e41;
}
                </style>
            </head>
            <body>

                <nav class="navbar navbar-expand-lg">
                    <a class="navbar-brand" href="/">CSV Analyzer</a>
                    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                    </button>
                </nav>


                <div class="container">
                    <h1 class="text-center mb-4">Outliers Analysis</h1>
                    <div class="progress-overlay" id="progressOverlay">
                        <div class="progress-container">
                            <p id="progressMessage">Generating Outlier Analysis</p>
                            <div class="progress">
                                <div class="progress-bar progress-bar-striped progress-bar-animated" role="progressbar" id="progressBar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100"></div>
                            </div>
                        </div>
                    </div>
                    <form method="post" action="/upload">
                        <div class="overlay" id="overlay2">
                            <div class="overlay-content">
                                <p>You have the option to select the rarest terms and sort the rarity score by clicking on their icons.</p>
                            </div>
                        </div>


<div class="dropdown">
    <button class="btn btn-secondary dropdown-toggle" type="button" id="analysisDropdownButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
        Select Analysis Type
    </button>
    <div class="dropdown-menu" aria-labelledby="analysisDropdownButton">
        <a class="dropdown-item" href="#" onclick="updateTable('Default')">Default</a>
        <a class="dropdown-item" href="#" onclick="updateTable('First Standard Deviation Outlier Analysis')">First Standard Deviation Outlier Analysis</a>
        <a class="dropdown-item" href="#" onclick="updateTable('Second Standard Deviation Outlier Analysis')">Second Standard Deviation Outlier Analysis</a>
        <a class="dropdown-item" href="#" onclick="updateTable('Third Standard Deviation Outlier Analysis')">Third Standard Deviation Outlier Analysis</a>
    </div>
</div>
<input type="hidden" id="selectedOption" name="selectedOption" value="Default">

<div id="histogramContainer">
    {{ histogram_html|safe }}
</div>
<div id="histogramLabelContainer"></div>

                    {{ table_html|safe }}
                        </div>
                    </form>

                <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
                <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"></script>
                <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
<script src="https://d3js.org/d3.v6.min.js"></script>

                <script>


                const meanScore = {{ stored_mean_score }};
    const stdDevScore = {{ stored_std_dev_score }};


    function drawBox(ax, threshold, color, label) {
    ax.axvline(threshold, color=color, linestyle='-', linewidth=2, label=label)
    ax.axvspan(threshold, max(rarity_scores) + 1, color=color, alpha=0.1)
}

    function updateDropdownButtonText(selectedText) {
        const dropdownButton = document.getElementById('analysisDropdown');
        dropdownButton.innerText = selectedText;
    }

    function updateTable(option) {
    document.getElementById('selectedOption').value = option; // Store selected option value
    const dropdownButton = document.getElementById('analysisDropdownButton');
    dropdownButton.textContent = option;

    let threshold;
    if (option === 'First Standard Deviation Outlier Analysis') {
        threshold = meanScore + stdDevScore;
    } else if (option === 'Second Standard Deviation Outlier Analysis') {
        threshold = meanScore + 2 * stdDevScore;
    } else if (option === 'Third Standard Deviation Outlier Analysis') {
        threshold = meanScore + 3 * stdDevScore;
    }

    if (option === 'Default') {
        resetTable();
        clearBoxes(); // Ensure boxes are cleared when "Default" is selected
    } else if (threshold !== undefined) {
        filterAndDisplayTable(threshold);
        updateHistogramWithCounts(option, threshold);
    }
}





    function resetTable() {
        const rows = Array.from(document.querySelectorAll('table tbody tr'));
        rows.forEach(row => {
            row.style.display = ''; // Show all rows
        });

        // Remove histogram label if it exists
        const histogramLabel = document.getElementById('histogramLabel');
        if (histogramLabel) {
            histogramLabel.remove();
        }
    }

function drawBoxes(thresholds) {
    const svg = d3.select("#histogram svg");
    svg.selectAll(".threshold-box").remove(); // Clear previous boxes
    thresholds.forEach(threshold => {
        svg.append("rect")
            .attr("class", "threshold-box")
            .attr("x", xScale(threshold))
            .attr("y", 0)
            .attr("width", xScale(d3.max(rarity_scores) + 1) - xScale(threshold))
            .attr("height", height)
            .style("fill", "red")
            .style("fill-opacity", 0.1)
            .style("stroke", "red")
            .style("stroke-width", 1);
    });
}

function clearBoxes() {
    const svg = d3.select("#histogramContainer svg");
    svg.selectAll(".threshold-box, .threshold-line").remove(); // Clear all threshold boxes and lines
}


function updateHistogramWithCounts(option, threshold) {
    const count = document.querySelectorAll('table tbody tr td:nth-child(4)').length;
    const countAboveThreshold = Array.from(document.querySelectorAll('table tbody tr td:nth-child(4)')).filter(td => parseFloat(td.innerText) >= threshold).length;
    const histogramLabelContainer = document.getElementById('histogramLabelContainer');
    const histogramLabel = document.getElementById('histogramLabel');

    let score;
    let color;
    let shiftAmount = 0;

    if (option === 'First Standard Deviation Outlier Analysis') {
        score = meanScore + stdDevScore;
        color = 'red';
        shiftAmount = 33;  
    } else if (option === 'Second Standard Deviation Outlier Analysis') {
        score = meanScore + 2 * stdDevScore;
        color = 'red';
         shiftAmount = 4;   
    } else if (option === 'Third Standard Deviation Outlier Analysis') {
        score = meanScore + 3 * stdDevScore;
        color = 'red';
         shiftAmount = -24;  
    } else {
        score = null;
    }

    const labelText = `
        <div class="alert alert-info mt-3 text-center" role="alert">
            <strong>${option}:</strong> 
            <span class="badge badge-pill badge-primary">${countAboveThreshold}</span> 
            out of 
            <span class="badge badge-pill badge-secondary">${count}</span> 
            documents 
            (Least Score: <span class="badge badge-pill badge-success">${score ? score.toFixed(2) : 'N/A'}</span>)
        </div>`;

    if (histogramLabel) {
        histogramLabel.innerHTML = labelText;
    } else {
        const labelElement = document.createElement('div');
        labelElement.id = 'histogramLabel';
        labelElement.innerHTML = labelText;
        labelElement.style.textAlign = 'center';  // Center the text
        histogramLabelContainer.appendChild(labelElement);
    }

    d3.select("#histogramContainer svg").selectAll(".threshold-line, .threshold-box").remove();

    if (score !== null) {
        const svg = d3.select("#histogramContainer svg");
        const svgHeight = +svg.attr("height");
        const svgWidth = +svg.attr("width");

        const xScale = d3.scaleLinear()
            .domain([Math.min(...rarity_scores) - 1, Math.max(...rarity_scores) + 1])
            .range([0, svgWidth]);

        const margin = 1.5 * 37.7953;  // Adjusted margin for better visualization
        const bottomMarginAdjustment = 66;  // Adjust this value as needed
        const topMarginAdjustment = 74;     // Adjust this value as needed
        const rightMarginAdjustment = 101;   // Adjust this value as needed

        // Apply the shift to the xPosition
        const xPosition = xScale(score) + shiftAmount;

        // Draw the shaded area
        svg.append("rect")
            .attr("class", "threshold-box")
            .attr("x", xPosition)
            .attr("y", topMarginAdjustment)
            .attr("width", xScale(Math.max(...rarity_scores) + 1) - xPosition - rightMarginAdjustment)
            .attr("height", svgHeight - topMarginAdjustment - bottomMarginAdjustment)
            .style("fill", color)
            .style("fill-opacity", 0.1)
            .style("stroke", color)
            .style("stroke-width", 1);

        svg.append("line")
            .attr("class", "threshold-line")
            .attr("x1", xPosition)
            .attr("x2", xPosition)
            .attr("y1", svgHeight - bottomMarginAdjustment)
            .attr("y2", topMarginAdjustment)
            .style("stroke", color)
            .style("stroke-width", 2);
    } else { 
        clearBoxes();
    }
}





function filterAndDisplayTable(threshold) {
    const rows = Array.from(document.querySelectorAll('table tbody tr'));
    const filteredRows = rows.filter(row => parseFloat(row.cells[3].innerText) >= threshold);
    const hiddenRows = rows.filter(row => parseFloat(row.cells[3].innerText) < threshold);

    // Show filtered rows
    filteredRows.forEach(row => {
        row.style.display = '';
    });

    // Hide non-filtered rows
    hiddenRows.forEach(row => {
        row.style.display = 'none';
    });

    // Update count directly
    updateHistogramWithCounts(filteredRows.length, rows.length, threshold);
}



                    $(function () {
                        $('[data-toggle="tooltip"]').tooltip();
                    });

                    // Show progress overlay
                    $("#progressOverlay").fadeIn(1000, function() {
                        var progress = 0;
                        var interval = setInterval(function() {
                            var progressInt = parseInt(progress);
                            $("#progressBar").css("width", progressInt + "%").attr("aria-valuenow", progressInt);
                            $("#progressMessage").text("Generating Outlier Analysis - " + progressInt + "%");
                            progress += Math.random() * 10;
                            if (progress >= 100) {
                                clearInterval(interval);
                                $("#progressOverlay").fadeOut(1000);
                                // Show overlay2 after progress overlay finishes
                                $("#overlay2").fadeIn(1000, function() {
                                    // Hide overlay2 after 3 seconds
                                    setTimeout(function() {
                                        $("#overlay2").fadeOut(1000);
                                    }, 3000);
                                });
                            }
                        }, 300);
                    });




                    function showTopTerms(event, count, order) {
    const header = $('#rarestTermsHeaderText');
    header.text(count + ' Rarest Terms');
    const table = $('table').get(0);
    const rows = Array.from(table.rows).slice(1); // Skip the header row

    rows.forEach(row => {
        const termsCell = row.cells[4];
        const terms = termsCell.getAttribute('data-original-terms').split(', ');
        const termScoresCell = row.cells[5];
        const termScores = JSON.parse(termScoresCell.getAttribute('data-original-scores'));

        const sortedIndices = termScores.map((score, index) => index)
            .sort((a, b) => termScores[b] - termScores[a]);

        const topTerms = sortedIndices.slice(0, count).map(index => terms[index]);
        const topScores = sortedIndices.slice(0, count).map(index => parseFloat(termScores[index]).toFixed(2));

        termsCell.innerText = topTerms.join(', ');
        termScoresCell.innerText = topScores.join(', '); // Changed this line

        const originalTextCell = row.cells[2];
        const originalText = originalTextCell.getAttribute('data-original-text');
        const updatedText = highlightTerms(originalText, topTerms, topScores);
        originalTextCell.innerHTML = updatedText;
    });

    event.preventDefault();
}


function highlightTerms(text, terms, scores) {
    const termScoresMap = {};
    terms.forEach((term, index) => {
        termScoresMap[term] = scores[index];
    });
    const sortedTerms = terms.slice().sort((a, b) => termScoresMap[b] - termScoresMap[a]);
    const sortedScores = sortedTerms.map(term => termScoresMap[term]);
    const colors = generateColorGradient(sortedScores);

    const termColorMap = {};
    sortedTerms.forEach((term, index) => {
        termColorMap[term] = colors[index];
    });

    return text.split(' ').map(word => {
        return termColorMap[word] ? `<span style="background-color: ${termColorMap[word]};">${word}</span>` : word;
    }).join(' ');
}

function generateColorGradient(scores, maxAlpha = 0.8, alphaGap = 0.05) {
    const maxScore = Math.max(...scores);
    const sortedScores = [...scores].sort((a, b) => b - a);

    return scores.map(score => {
        const rank = sortedScores.indexOf(score);
        let alpha = maxAlpha - rank * alphaGap;
        if (alpha < 0) alpha = 0;
        return `rgba(255, 0, 0, ${alpha})`;
    });
}

// Ensure original terms and scores are stored in data attributes when the table is generated
$(document).ready(function() {
    $('table tbody tr').each(function() {
        const originalTextCell = $(this).find('td:eq(2)');
        const termsCell = $(this).find('td:eq(4)');
        const termScoresCell = $(this).find('td:eq(5)');



        termsCell.attr('data-original-terms', termsCell.text());
        const termScores = JSON.parse(termScoresCell.text()).map(score => parseFloat(score).toFixed(2));
        termScoresCell.attr('data-original-scores', JSON.stringify(termScores));
        originalTextCell.attr('data-original-text', originalTextCell.text());

        const terms = termsCell.text().split(', ');

        const originalText = originalTextCell.text();
        const highlightedText = highlightTerms(originalText, terms, termScores);
        originalTextCell.html(highlightedText);
    });
});

$(document).ready(function () {
        $('[data-toggle="tooltip"]').tooltip();

        // Ensure original rarity scores are stored in data attributes when the table is generated
        $('table tbody tr').each(function () {
            const rarityScoreCell = $(this).find('td:eq(3)');
            rarityScoreCell.attr('data-original-rarity', rarityScoreCell.text());
        });
    });

    function sortTable(column, order) {
        const table = $('table').get(0);
        const rows = Array.from(table.rows).slice(1); // Skip the header row
        const tbody = table.tBodies[0];

        if (column === 'rarity') {
            rows.sort((rowA, rowB) => {
                const cellA = parseFloat(rowA.cells[3].innerText);
                const cellB = parseFloat(rowB.cells[3].innerText);
                return order === 'ascending' ? cellA - cellB : cellB - cellA;
            });

            // Clear the table body
            while (tbody.firstChild) {
                tbody.removeChild(tbody.firstChild);
            }

            // Append sorted rows
            rows.forEach(row => tbody.appendChild(row));
        } else if (order === 'default') {
            // Reset to default order
            rows.sort((rowA, rowB) => {
                const cellA = parseFloat($(rowA).find('td:eq(3)').attr('data-original-rarity'));
                const cellB = parseFloat($(rowB).find('td:eq(3)').attr('data-original-rarity'));
                return cellA - cellB;
            });

            // Clear the table body
            while (tbody.firstChild) {
                tbody.removeChild(tbody.firstChild);
            }

            // Append rows in the default order
            rows.forEach(row => tbody.appendChild(row));
        }
    }
                </script>
            </body>
            </html>
            """, table_html=output_html, histogram_html=histogram_html, stored_mean_score=stored_mean_score,
                                      stored_std_dev_score=stored_std_dev_score)




    except Exception as e:
        return f"An error occurred: {str(e)}"


if __name__ == '__main__':
    app.run(port=8086, debug=True)
