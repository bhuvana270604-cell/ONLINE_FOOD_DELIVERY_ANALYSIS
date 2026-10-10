# Online Food Delivery Analysis

## Project Overview

This project analyzes online food delivery orders using Python and Streamlit. The dashboard displays order statistics, city-wise orders, average order value, delivery time, restaurant ratings, and data quality checks.

## Objectives

- Analyze online food delivery orders.
- Explore orders across cities.
- Calculate average order value and delivery time.
- Analyze restaurant ratings.
- Check missing values and duplicate records.
- Present results through an interactive dashboard.

## Technologies Used

- Python
- Pandas
- Streamlit
- MySQL (optional database import)
- SQLAlchemy
- PyMySQL

## Dataset Overview

- Total records: 7,096
- Total columns: 28
- Missing values in the cleaned CSV: 0
- Duplicate rows in the cleaned CSV: 0

Dataset: `online_food_delivery_cleaned.csv`

## Dashboard Features

- Total Orders, Cities, and Restaurants
- Average Order Value
- Average Delivery Time
- Average Restaurant Rating
- Top Cities by Number of Orders
- Missing Values check
- Duplicate Rows check
- Column data types overview

## Project Files

- `app.py` — Streamlit dashboard.
- `online_food_delivery_cleaned.csv` — Dataset used by the dashboard.
- `mysql_import.py` — Optional script to import data into MySQL.
- `online_food_delivery_analysis.png` — Project-related image.

## How to Run

Install the required packages:

```bash
pip install streamlit pandas
```

Run the dashboard from the project folder:

```bash
streamlit run app.py
```

## Data Quality Note

The dashboard checks missing values and duplicate rows in the supplied cleaned CSV. The current CSV contains no missing values or duplicate rows. The original raw dataset and original cleaning notebook are not included in this repository.

## Conclusion

This project demonstrates how Python, Pandas, and Streamlit can be used to analyze online food delivery data and present useful information through an interactive dashboard.