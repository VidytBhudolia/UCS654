# Assignment 3 - Learning Probability Density Functions Using Roll Number

## Overview
This assignment learns the parameters of a probability density function using NO₂ data from the India Air Quality dataset by fitting a parametric function.

## Approach
- Transform data using roll number-based function: `z = x + a*sin(b*x)`
- Fit Gaussian-like PDF: `p(z) = c · exp(-λ(z - μ)²)`
- Use scipy curve_fit to estimate parameters λ, μ, and c

## Requirements
- Python 3.x with tf environment activated
- Libraries: numpy, pandas, matplotlib, scipy (already in tf environment)

## Dataset Setup
1. Download dataset from Kaggle: https://www.kaggle.com/datasets/shrutibhargava94/india-air-quality-data
2. Extract the zip file
3. Copy `india-air-quality-data.csv` to this folder (Assignment 3)

## Usage
1. Ensure dataset is in Assignment 3 folder
2. Activate tf environment: `conda activate tf`
3. Open `assignment3.ipynb` in Jupyter/VS Code
4. Run all cells sequentially
5. Output: fitted.png showing empirical vs fitted PDF

## Files
- `assignment3.ipynb` - Main notebook
- `fitted.png` - Output visualization (generated after running)
- `README.md` - This file
