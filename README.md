# Statistical Characterization and Comparative Data Analysis of Two Real-World Datasets

## 1. Project Overview
This project performs statistical characterization and comparative data analysis on two real-world retail datasets from the Online Retail II dataset. It analyzes sales performance, customer purchasing patterns and revenue trends using Python and machine learning techniques.

## 2. Objectives
- Clean and preprocess the two retail datasets.
- Identify and classify variables based on measurement levels.
- Calculate statistical measures such as mean, median, mode and standard deviation.
- Compare sales revenue, quantity and transactions.
- Develop and evaluate machine learning models for sales prediction.

## 3. Datasets
**Dataset:** Online Retail II

- Dataset 1: Year 2009–2010
- Dataset 2: Year 2010–2011

**Source:** UCI Machine Learning Repository  
https://doi.org/10.24432/C5CG6D

## 4. Technologies Used
- Python 3
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- VS Code

## 5. Data Preprocessing
The following steps were performed:
1. Handling missing values.
2. Removing duplicate records.
3. Removing cancelled transactions.
4. Handling invalid quantity and price values.
5. Converting date columns into the correct format.
6. Creating a Revenue column.

## 6. Statistical and Data Analysis
- Measures of central tendency: Mean, Median and Mode.
- Measures of location: Quartiles and Percentiles.
- Measures of dispersion: Range, Variance, Standard Deviation and IQR.
- Descriptive and comparative sales analysis.
- Product-wise, customer-wise and country-wise pattern identification.

## 7. Machine Learning Models
The following regression models were implemented:
1. Linear Regression
2. Decision Tree Regression
3. Random Forest Regression

**Evaluation Metrics:**
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

Random Forest Regression achieved the best average ranking among the three regression models in the implemented comparison.

## 8. Project Outputs
The project generates the following visualizations:
- Monthly Sales Trend
- Sales Comparison
- Revenue Distribution Boxplot
- Sales Distribution Histogram

## 9. Project Structure
```text
Online-Retail-Analysis/
│
├── online+retail+ii/
│   └── online_retail_II.xlsx
│
├── datacleaning.py
├── cleaned_retail_2009_2010.csv
├── cleaned_retail_2010_2011.csv
├── monthly_sales_trend.png
├── revenue_boxplot.png
├── sales_comparison.png
├── sales_histogram.png
├── requirements.txt
└── README.md
```

## 10. How to Run the Project

1. Install Python 3.
2. Install the required libraries:
```bash
pip install -r requirements.txt
```
3. Open the project folder in VS Code.
4. Ensure the Excel dataset is inside the `online+retail+ii` folder.
5. Run the Python file:
```bash
python datacleaning.py
```
6. View the generated statistical results, model comparisons and visualizations.

## 11. Conclusion
This project demonstrates the application of statistical analysis, data visualization and machine learning techniques to real-world retail datasets. It provides insights into sales performance, customer purchasing patterns and predictive analytics.

---
**Academic Project – B.Tech Computer Science and Engineering**