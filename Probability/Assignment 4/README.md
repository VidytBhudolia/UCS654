# Assignment 4 - Learning Probability Density Functions Using Data (GAN)

## Overview
This assignment learns the probability density function of transformed NO₂ data using a Generative Adversarial Network without assuming any predefined distribution.

## Approach
- Transform data using roll number-based function: `z = x + a*sin(b*x)`
- Train a GAN to learn the distribution directly from data
- Generator creates samples from random noise
- Discriminator distinguishes between real and generated samples
- Extract PDF from generated samples using histogram

## Requirements
- Python 3.x with tf environment activated
- Libraries: tensorflow, numpy, pandas, matplotlib (already in tf environment)

## Dataset Setup
1. Download dataset from Kaggle: https://www.kaggle.com/datasets/shrutibhargava94/india-air-quality-data
2. Extract the zip file
3. Copy `india-air-quality-data.csv` to this folder (Assignment 4)

## Usage
1. Ensure dataset is in Assignment 4 folder
2. Activate tf environment: `conda activate tf`
3. Open `assignment4.ipynb` in Jupyter/VS Code
4. Run all cells sequentially (training takes ~3-5 minutes)
5. Output: gan_pdf.png comparing real vs generated distributions

## Files
- `assignment4.ipynb` - Main notebook with GAN implementation
- `gan_pdf.png` - Output visualization (generated after running)
- `README.md` - This file

## Key Hyperparameters
- Epochs: 3000
- Batch size: 64
- Noise dimension: 10
- Learning rate: 0.0004
