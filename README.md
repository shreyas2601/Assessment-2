# Assessment-2
# ETRM Data Analysis with Pandas & Visualization
## Project Overview

This project demonstrates the ingestion, transformation, and analysis of synthetic ETRM (Energy Trading & Risk Management) trade data using Python, Pandas, and visualization libraries such as Matplotlib and Seaborn. It covers data from multiple formats, performs exploratory data analysis (EDA), and presents insights through visualizations.

The purpose of this project is to practice real-world data handling, cleaning, and visualization workflows while gaining insights from trading datasets.

## Folder Structure
```
Assignment2/
│
├── data/
│   ├── etrm_trades.csv
│   ├── etrm_trades.json
│   ├── etrm_trades.xlsx
│   ├── etrm_trades.txt
│   ├── etrm_trades.html
│   └── etrm_trades.xml
│
├── data_analysis/
│   ├── data_analysis_csv.ipynb
│   ├── data_analysis_json.ipynb
│   ├── data_analysis_excel.ipynb
│   ├── data_analysis_txt.ipynb
│   ├── data_analysis_html.ipynb
│   └── data_analysis_xml.ipynb
│
├── exercises/
│   ├── dataframes.py
│   ├── list_comprehension.py
│   ├── palindrome.py
│   ├── product.py
│   └── random_array.py
│
├── README.md
```

## Steps Performed
### 1. Data Ingestion

Loaded six different file formats into Pandas DataFrames:

CSV ```(etrm_trades.csv)```

JSON ```(etrm_trades.json)```

Excel ```(etrm_trades.xlsx)```

TXT ```(pipe-delimited, etrm_trades.txt)```

HTML ```(etrm_trades.html)```

XML ```(etrm_trades.xml)```

Verified column names and data types for consistency across datasets.

### 2. Data Cleaning & Transformation

Converted ```DeliveryStart``` and ```DeliveryEnd``` columns to ```datetime ```type.

Checked for missing or inconsistent values and handled them.

### 3. Exploratory Data Analysis (EDA)

**Average price per commodity**
**Distribution of trades by currency**

**Trade periodicity breakdown** (Daily, Weekly, Monthly, etc.)

### 4. Data Visualization

Visualizations using Matplotlib and Seaborn:

**Bar Chart** – Volume by Trader

**Pie Chart** – Trades by Currency

**Line Chart** – Average Price Trend by Delivery Start Date

**Histogram** – Distribution of Notional Values (Price × Volume)

**Heatmap** – Commodity vs. Trader Trade Counts

### Insights

Commodities with the highest average price and volume.

Most frequently traded currencies.

Patterns in trade periodicity across commodities and traders.

Top traders by trade volume.

Correlations between commodities and traders in trade frequency.

## How to Run

  Clone the repository:

```git clone <repository_url>```

Open the notebooks in the``` data_analysis``` folder and run sequentially to reproduce the analysis and visualizations.

Python scripts in the ```exercises``` folder can be run independently for practice exercises.

## Dependencies

Python >= 3.10

Pandas

NumPy

Matplotlib

Seaborn

Plotly (optional)

openpyxl (for Excel)

lxml or xmltodict (for XML)

## Author

**Shreyas Deshpande**
