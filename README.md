# Sprint4-Software_dev_tool-
Software developemen tool tripleten sprint4

# Create the README.md content based on the user's project
readme_content = """# 🚗 Used Vehicles Dashboard & Exploratory Analysis

This repository provides a comprehensive interactive dashboard and exploratory data analysis (EDA) of a dataset containing over 51,000 used vehicles listed for sale in the United States. The project is built with **Panel** and **Plotly**, and includes data wrangling, visualization, and summarization tools for insights into pricing trends, vehicle conditions, and market dynamics.

## 📁 Project Structure

- `app.py` – A Panel-based interactive dashboard for exploring used vehicle data by brand and model, including visualizations for price distribution, odometer readings, model year, and more.
- `EDA.ipynb` – A Jupyter Notebook providing in-depth exploratory data analysis, including data cleaning, summary statistics, and exploratory visualizations.

## 📊 Dashboard Features

- **Brand & Model Selector**: Filter data interactively by car brand and model.
- **Summary Panel**: Get average price, listing duration, and vehicle type for the selected model.
- **Dynamic Visualizations**:
  - Price Distribution
  - Odometer Distribution
  - Price vs Model Year
  - Price vs Odometer
- **Data Preview**: View a snapshot of the raw dataset.

## 📦 Requirements

Install dependencies using pip:

```bash
pip install pandas panel plotly
