# 🚗 Sprint 4 – Used Vehicles Dashboard & EDA  
**TripleTen Software Development Tool – Sprint 4**

This repository contains a robust dashboard application and exploratory data analysis (EDA) toolkit for analyzing a dataset of over 51,000 used vehicles listed in the United States. Built using **Panel**, **Plotly**, and **Pandas**, the project showcases data preprocessing, missing value restoration, visual exploration, and interactive selection tools.

## 📁 Project Structure

- `app.py` – Panel dashboard script with dynamic brand/model selectors and multiple visualizations.
- `EDA.ipynb` – A notebook offering additional data exploration, feature engineering, and visual summaries.
- `vehicles_us.csv` – Source dataset used for the analysis and dashboard.

## 🛠 Data Handling & Assumptions

Missing values are handled as follows:
- **`is_4wd`**: Filled with `0` assuming missing entries are non-4WD.
- **`paint_color`**: Replaced with `'Unknown'`.
- **`model_year`, `odometer`, `cylinders`**: Filled with the median value of the same model group to preserve contextual relevance.

These assumptions aim to preserve as much data as possible, enhancing analysis without arbitrary row removal.

## 📊 Dashboard Features

- **Interactive Selectors**: Choose brand and model dynamically.
- **Summarized Insights**: Display of average price, days listed, and vehicle type.
- **Visual Analytics**:
  - Histogram of price distribution
  - Histogram of odometer values
  - Scatter plots: price vs. model year, price vs. odometer
  - Histogram of paint color distribution (NEW)
  - Global scatter plot: price vs. odometer for all vehicles (NEW)
- **Data Preview**: Snapshot of the dataset after preprocessing.

## 💻 Usage

### Installation
Install required packages:
```bash
pip install pandas panel plotly
```

### Run the Dashboard
```bash
panel serve app.py --autoreload
```

### Jupyter Tip
To render a Plotly plot (e.g., histogram of paint colors) in a Jupyter Notebook:
```python
import plotly.express as px
fig = px.histogram(vehicles_df, x="paint_color", title="Distribution of Paint Colors")
fig.show()
```

## 📄 Dataset Overview

- **Listings**: 51,525 vehicles
- **Price Range**: $1 to $375,000
- **Year Range**: 1908 to 2019 (Median: 2011)
- **Top Model**: Ford F-150 (2,796 listings)
- **Common Conditions**: excellent, good, like new, fair, salvage, new
- **Common Cylinders**: 4, 6, 8

## ✅ Goals

- Practice interactive dashboard development
- Apply data restoration techniques
- Conduct scalable and reproducible exploratory analysis
