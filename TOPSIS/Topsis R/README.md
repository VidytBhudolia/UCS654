# TOPSIS R Implementation

TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) implementation using R programming language.

## Overview

Native R implementation for users who prefer R over Python. Includes data analysis, visualization, and TOPSIS algorithm implementation.

## Usage

### Jupyter Notebook with R Kernel

```bash
# Install R kernel for Jupyter
# Open Topsis.ipynb in Jupyter Notebook
# Run cells sequentially
```

### RStudio

Open `Topsis.ipynb` or extract R code to run in RStudio environment.

## Requirements

Install required R packages:

```r
install.packages(c("dplyr", "tidyr", "ggplot2"))
```

See `requirements.txt` for package list.

## Features

✓ Native R implementation  
✓ Data manipulation with dplyr  
✓ Visualization with ggplot2  
✓ Interactive notebook format  
✓ Compatible with R ecosystem  

## Algorithm

1. Normalize decision matrix
2. Apply weights to criteria
3. Calculate ideal best and worst
4. Compute distances and scores
5. Rank alternatives

## Files

- `Topsis.ipynb` - Main R notebook with TOPSIS implementation
- `requirements.txt` - R package dependencies
