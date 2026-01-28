# TOPSIS CLI

Standalone Python script implementation of TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) - no installation required.

## Quick Start

```bash
python topsis.py data.xlsx "0.2,0.2,0.2,0.2,0.2" "+,+,+,+,+" output.csv
```

## Usage

```bash
python topsis.py <InputFile> <Weights> <Impacts> <OutputFile>
```

**Arguments:**
- `InputFile`: CSV or XLSX file (first column = names, rest = numeric criteria)
- `Weights`: Comma-separated numbers (e.g., `"0.2,0.2,0.2,0.2,0.2"`)
- `Impacts`: `+` (benefit) or `-` (cost), comma-separated (e.g., `"+,+,+,-,+"`)
- `OutputFile`: Output CSV file name

## Input Format

```csv
Fund_Name,P1,P2,P3,P4,P5
M1,0.67,0.45,6.5,42.0,12.56
M2,0.60,0.36,3.3,53.3,14.47
M3,0.82,0.67,3.6,38.0,17.1
```

## Output Format

Adds two columns: `Topsis Score` and `Rank`

```csv
Fund_Name,P1,P2,P3,P4,P5,Topsis Score,Rank
M3,0.82,0.67,3.6,38.0,17.1,0.720000,1
M1,0.67,0.45,6.5,42.0,12.56,0.650000,2
```

## Requirements

```bash
pip install -r requirements.txt
```

Dependencies: `numpy`, `pandas`, `openpyxl`

## Features

✓ No package installation needed  
✓ CSV and XLSX support  
✓ Comprehensive error handling  
✓ Clear error messages  

## Example

The folder includes:
- `data.xlsx` - Sample input file
- `output.csv` - Sample output file
- `topsis.py` - Main script
