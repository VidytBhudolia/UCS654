# Sampling Techniques for Imbalanced Classification

## Overview
This project analyzes the performance of various sampling techniques to handle imbalanced datasets for credit card fraud detection. The analysis compares 5 different sampling methods across 5 classification models.

## Dataset
- **File**: Creditcard_data.csv
- **Initial Class Distribution**: Highly imbalanced (763:9)
- **Features**: 30 numerical features
- **Target**: Binary classification (Class 0 and Class 1)

## Sampling Techniques
1. **Technique_A**: NearMiss (Under-sampling)
2. **Technique_B**: ADASYN (Adaptive Synthetic Sampling)
3. **Technique_C**: BorderlineSMOTE (Borderline Synthetic Minority Over-sampling)
4. **Technique_D**: EditedNearestNeighbours (Cleaning technique)
5. **Technique_E**: SMOTETomek (Combined over and under-sampling)

## Classification Models
1. **Model_1**: Gradient Boosting Classifier
2. **Model_2**: Gaussian Naive Bayes
3. **Model_3**: AdaBoost Classifier
4. **Model_4**: Ridge Classifier
5. **Model_5**: Linear Discriminant Analysis

## Methodology
- Created 5 different train-test splits with varying test sizes (25%, 30%, 35%, 30%, 25%)
- Applied each sampling technique to balance training data
- Trained each model on resampled data
- Evaluated using accuracy metric
- Results averaged across all splits

## Results
The analysis generates:
- Accuracy comparison heatmap
- Best sampling technique identification for each model
- Bar chart showing optimal techniques
- Average performance comparison
- CSV file with detailed results

## Requirements
- Python 3.x
- pandas
- numpy
- scikit-learn
- imbalanced-learn
- matplotlib
- seaborn

## Usage
Run the Jupyter notebook `sampling_analysis.ipynb` to execute the complete analysis. Results are saved in the `results/` directory.

## Key Findings
- EditedNearestNeighbours (Technique_D) performed best across all models
- Average accuracy ranged from 40% (NearMiss) to 98% (EditedNearestNeighbours)
- Proper sampling technique selection significantly impacts model performance on imbalanced data
