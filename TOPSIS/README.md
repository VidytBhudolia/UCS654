# TOPSIS Implementation

**TOPSIS** (Technique for Order of Preference by Similarity to Ideal Solution) - A multi-criteria decision-making algorithm that ranks alternatives based on closeness to ideal solution.

## 📦 Implementations

### 1. [Topsis Package](./Topsis%20Package/) - PyPI Library
Python package for general TOPSIS analysis. **[Install →](https://pypi.org/project/topsis-vidyt-102303747/)**

```bash
pip install topsis-vidyt-102303747
topsis data.xlsx "0.2,0.2,0.2,0.2,0.2" "+,+,+,+,+" output.csv
```

**Features:** CLI + Python API, CSV/XLSX support, validation  
**Use for:** General decision-making, automated workflows

### 2. [Topsis Web](./Topsis%20Web/) - Streamlit App
Web interface for TOPSIS analysis. **[Live Demo →](https://topsis-vidyt.streamlit.app/)**

**Features:** File upload, real-time validation, download results, email delivery  
**Use for:** Non-coders, quick analysis, sharing with teams

### 3. [Topsis CLI](./Topsis%20CLI/) - Standalone Script
No installation Python script for TOPSIS.

```bash
python topsis.py data.xlsx "0.2,0.2,0.2,0.2,0.2" "+,+,+,+,+" output.csv
```

**Features:** Single file, no pip install required  
**Use for:** Quick runs, environments without package manager

## 🎯 Applications

### 4. [Topsis Text Classification](./Topsis%20Text%20Classification/)
Ranks sentiment analysis models using TOPSIS.

**Models:** DistilBERT, BERT, RoBERTa (5 models)  
**Criteria:** Accuracy, F1 Score, Inference Time, Model Size  
**Dataset:** IMDB reviews (200 balanced samples)

### 5. [Topsis Projectile Simulation](./Topsis%20Projectile%20Simulation/)
Optimizes projectile motion parameters using physics simulations.

**Features:** Trajectory analysis, multi-parameter optimization  
**Use for:** Physics/Engineering applications

### 6. [Topsis R](./Topsis%20R/)
TOPSIS implementation in R language.

**Features:** Native R, dplyr/ggplot2, Jupyter notebook  
**Use for:** R ecosystem users

---

## 🚀 Quick Start

| User Type | Recommended | Command |
|-----------|-------------|---------|
| End User | [Web App](https://topsis-vidyt.streamlit.app/) | Just upload file in browser |
| Developer | Package | `pip install topsis-vidyt-102303747` |
| Quick Task | CLI Script | `python topsis.py data.xlsx ...` |
| ML Engineer | Text Classification | Open Jupyter notebook |
| R User | R Implementation | Open Topsis.ipynb |

## 📊 Algorithm Steps

1. **Normalize** decision matrix (vector normalization)
2. **Weight** each criterion
3. **Find ideal best/worst** based on impacts (+/-)
4. **Calculate distances** to ideal solutions
5. **Compute scores** = distance_worst / (distance_best + distance_worst)
6. **Rank** alternatives (1 = best)

## 📁 Project Structure

```
TOPSIS/
├── README.md                       # This file
├── Topsis Package/                 # PyPI library (CLI + API)
├── Topsis Web/                     # Streamlit web app
├── Topsis CLI/                     # Standalone script
├── Topsis Text Classification/     # ML model ranking
├── Topsis Projectile Simulation/   # Physics optimization
└── Topsis R/                       # R implementation
```

## 🔗 Links

- **PyPI**: https://pypi.org/project/topsis-vidyt-102303747/
- **Web App**: https://topsis-vidyt.streamlit.app/
- **GitHub**: https://github.com/VidytBhudolia/UCS654

## 👤 Author

**Vidyt Bhudolia** (Roll No: 102303747)

---

*For detailed documentation, see README files in individual folders.*
