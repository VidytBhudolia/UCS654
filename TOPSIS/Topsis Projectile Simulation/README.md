# Model Comparison with TOPSIS

Rank 8 regression models on projectile motion dataset using TOPSIS for multi-criteria decision making.

## Problem

Predict horizontal range given: launch_angle, initial_velocity, mass, drag_coefficient, gravity

## Models

Linear Regression, Ridge, Decision Tree, Random Forest, Gradient Boosting, SVR, KNN, MLP

## TOPSIS Criteria

- MAE (30%) - minimize
- RMSE (30%) - minimize  
- R² (25%) - maximize
- Training_Time (15%) - minimize

## Results

Top 3 models:
1. Gradient Boosting (0.87)
2. Decision Tree (0.77)
3. Random Forest (0.72)

Gradient Boosting wins with best accuracy (MAE: 4.82, RMSE: 7.31, R²: 0.98) and reasonable speed.

## Files

- `Model_Comparison_TOPSIS.ipynb` - Main notebook
- `data/simulation_data.csv` - Dataset (generated)
- `results/model_topsis_scores.png` - Visualization (generated)

## Usage

```bash
jupyter notebook Model_Comparison_TOPSIS.ipynb
```

Run all cells to generate dataset, train models, apply TOPSIS, and create visualization.

## Dependencies

numpy, pandas, matplotlib, scikit-learn, topsis_package

- Hwang, C.L. & Yoon, K. (1981). "Multiple Attribute Decision Making: Methods and Applications"
- Behzadian, M. et al. (2012). "A state-of-the-art survey of TOPSIS applications"
- Scikit-learn documentation: https://scikit-learn.org/

---

**Version**: 1.0  
**Last Updated**: January 2026  
**License**: Educational Use
