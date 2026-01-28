# Text Classification TOPSIS Analysis

## Overview
This project performs sentiment analysis on the IMDB dataset using multiple Hugging Face pre-trained models and ranks them using the TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) method.

## Objective
Compare and rank different sentiment analysis models based on their:
- **Accuracy**: Correctness of predictions
- **F1 Score**: Balance between precision and recall
- **Inference Time**: Speed of making predictions (lower is better)
- **Model Size**: Memory footprint in MB (smaller is better)

## Models Evaluated
1. `distilbert-base-uncased-finetuned-sst-2-english`
2. `textattack/bert-base-uncased-SST-2`
3. `siebert/sentiment-roberta-large-english`
4. `cardiffnlp/twitter-roberta-base-sentiment`
5. `nlptown/bert-base-multilingual-uncased-sentiment`

## Dataset
- **Source**: IMDB Movie Reviews Dataset
- **Test Set**: 200 samples (100 positive, 100 negative)
- **Train Set**: 1000 samples (used for reference)

## TOPSIS Methodology
- **Weights**: [0.3, 0.3, 0.2, 0.2] for [Accuracy, F1, Inference_Time, Model_Size_MB]
- **Impacts**: 
  - (+) for Accuracy and F1 Score (higher is better)
  - (-) for Inference Time and Model Size (lower is better)

## Results
The notebook displays final rankings with TOPSIS scores for each model. Lower inference time and model size combined with high accuracy and F1 scores result in better rankings.

## Usage
1. Ensure dependencies are installed: `pip install -r requirements.txt`
2. Open `text_classification_topsis.ipynb` in Jupyter Notebook
3. Run all cells to execute the analysis
4. View the final results table showing TOPSIS-ranked models

## Requirements
- Python 3.10+
- torch
- transformers
- datasets
- pandas
- numpy
- topsis_package (from local Topsis Package folder)

## Output
Console output displays:
- Device being used (GPU/CPU)
- Number of test samples loaded
- Models being tested
- Per-model performance metrics
- Final TOPSIS-ranked results table
