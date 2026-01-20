# TOPSIS Implementation

**TOPSIS** (Technique for Order of Preference by Similarity to Ideal Solution) is a multi-criteria decision-making algorithm that ranks alternatives based on their closeness to an ideal solution.

This repository contains two implementations of TOPSIS:

---

## Topsis Package (PyPI)

A fully-featured Python package uploaded to PyPI for easy installation and use.

### Installation

```bash
pip install topsis-vidyt-102303747
```

### Quick Start

```bash
topsis data.xlsx "0.2,0.2,0.2,0.2,0.2" "+,+,+,+,+" output.csv
```

### Command Line Usage

```bash
topsis <InputDataFile> <Weights> <Impacts> <OutputResultFile>
```

#### Arguments:
- **InputDataFile**: CSV or XLSX file (first column: identifiers, rest: numeric criteria)
- **Weights**: Comma-separated numeric weights (e.g., `"0.2,0.2,0.2,0.2,0.2"`)
- **Impacts**: Comma-separated impacts: `+` for benefit, `-` for cost (e.g., `"+,+,+,-,+"`)
- **OutputResultFile**: Output CSV file name

### Input Format

CSV/XLSX with structure:
```
Fund_Name,P1,P2,P3,P4,P5
M1,0.67,0.45,6.5,42.0,12.56
M2,0.60,0.36,3.3,53.3,14.47
M3,0.82,0.67,3.6,38.0,17.1
```

### Output Format

CSV with appended columns:
```
Fund_Name,P1,P2,P3,P4,P5,Topsis Score,Rank
M1,0.67,0.45,6.5,42.0,12.56,0.650000,2
M2,0.60,0.36,3.3,53.3,14.47,0.480000,5
M3,0.82,0.67,3.6,38.0,17.1,0.720000,1
```

### Python API

```python
import numpy as np
from topsis_package import topsis

data = np.array([
    [0.67, 0.45, 6.5, 42.0, 12.56],
    [0.60, 0.36, 3.3, 53.3, 14.47],
    [0.82, 0.67, 3.6, 38.0, 17.1],
])

weights = [0.2, 0.2, 0.2, 0.2, 0.2]
impacts = ["+", "+", "+", "+", "+"]

result = topsis(data, weights, impacts)
print("Scores:", result.scores)
print("Ranks:", result.ranks)
```

### Features

✓ Supports CSV and XLSX input files  
✓ Command-line interface  
✓ Python module for programmatic use  
✓ Comprehensive input validation  
✓ Proper error handling  

### Validation Rules

- Correct number of CLI arguments
- Weights are numeric and comma-separated
- Impacts are `+` or `-` only
- Input file exists (File not found handling)
- Input file has ≥3 columns (ID + ≥2 criteria)
- All criteria columns are numeric
- Number of weights = impacts = criteria columns
- At least one data row

### PyPI Project

📍 **PyPI Link**: https://pypi.org/project/topsis-vidyt-102303747/

📍 **Repository**: https://github.com/VidytBhudolia/UCS654-102303747

📍 **Requirements**: Python ≥3.7, numpy, pandas, openpyxl

---

## Topsis CLI (Standalone Script)

A standalone Python script version without installation requirements.

### Usage

```bash
python topsis.py <InputDataFile> <Weights> <Impacts> <OutputResultFile>
```

#### Example:
```bash
python topsis.py data.xlsx "0.2,0.2,0.2,0.2,0.2" "+,+,+,+,+" output.csv
```

### Requirements

- Python ≥3.7
- numpy
- pandas
- openpyxl

Install dependencies:
```bash
pip install numpy pandas openpyxl
```

### File Location

```
Topsis CLI/
├── topsis.py        # Main script
├── data.xlsx        # Sample input file
└── output.csv       # Sample output file
```

---

## TOPSIS Algorithm Steps

1. **Normalize** the decision matrix (vector normalization)
2. **Weight** each normalized column
3. **Determine ideal best and worst** based on impact type (+ or -)
4. **Calculate distances** to ideal best and worst solutions
5. **Compute closeness coefficient** = distance_to_worst / (distance_to_best + distance_to_worst)
6. **Rank** alternatives by descending score (1 = best)

---

## Comparison: Package vs CLI

| Feature | Package | CLI |
|---------|---------|-----|
| Installation | `pip install topsis-vidyt-102303747` | Copy `topsis.py` |
| Usage | `topsis ...` | `python topsis.py ...` |
| Python API | ✓ Yes | ✗ No |
| Version Control | PyPI managed | Manual |
| Updates | Via pip | Manual |
| Portability | Better (installed globally) | Good (single file) |

---

## Examples

### Example 1: Fund Comparison
```bash
topsis funds.xlsx "0.2,0.2,0.2,0.2,0.2" "+,+,+,-,+" ranked_funds.csv
```

### Example 2: Custom Weights & Impacts
```bash
topsis data.csv "1,2,3,1" "+,-,+,-" results.csv
```

---

## Error Handling

Clear error messages for:
```
Error: Input file not found
Error: Weights must be numeric and separated by commas
Error: Impacts must be either '+' or '-' and separated by commas
Error: Number of weights, impacts, and criteria columns must match
Error: Non-numeric value found in row X (criteria columns must be numeric)
```

---

## License

MIT License - See LICENSE file for details

---

## Author

**Vidyt** (Roll No: 102303747)

---

## Links

- **PyPI**: https://pypi.org/project/topsis-vidyt-102303747/
- **GitHub**: https://github.com/VidytBhudolia/UCS654-102303747
- **Issues**: https://github.com/VidytBhudolia/UCS654-102303747/issues

---

## Documentation

For detailed documentation, see:
- [Topsis Package README](./Topsis%20Package/README.md)
- [Package Source Code](./Topsis%20Package/topsis_package/)
- [CLI Script](./Topsis%20CLI/topsis.py)
