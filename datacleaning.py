
import pandas as pd
import numpy as np

# Load both datasets
file_path = r"online+retail+ii\online_retail_II.xlsx"

df1 = pd.read_excel(file_path, sheet_name="Year 2009-2010")
df2 = pd.read_excel(file_path, sheet_name="Year 2010-2011")

def clean_data(df):

    # 1. Handle missing values
    df = df.dropna(subset=["Description"]).copy()

    # 2. Remove duplicate records
    df = df.drop_duplicates()

    # 3. Remove cancelled transactions
    df["Invoice"] = df["Invoice"].astype(str)
    df = df[~df["Invoice"].str.startswith("C")]

    # 4. Handle invalid values
    df = df[(df["Quantity"] > 0) & (df["Price"] > 0)]

    # 5. Convert data types
    df["InvoiceDate"] = pd.to_datetime(
        df["InvoiceDate"], errors="coerce"
    )
    df = df.dropna(subset=["InvoiceDate"])

    # 6. Create Revenue column
    df["Revenue"] = df["Quantity"] * df["Price"]

    return df

# Clean both datasets
cleaned_df1 = clean_data(df1)
cleaned_df2 = clean_data(df2)

# Display results
print("DATA CLEANING RESULTS")

for name, original, cleaned in [
    ("Dataset 1", df1, cleaned_df1),
    ("Dataset 2", df2, cleaned_df2)
]:
    print(f"\n{name}")
    print("Original Shape:", original.shape)
    print("Cleaned Shape:", cleaned.shape)
    print("Missing Values:\n", cleaned.isnull().sum())

# Save cleaned datasets
cleaned_df1.to_csv("cleaned_retail_2009_2010.csv", index=False)
cleaned_df2.to_csv("cleaned_retail_2010_2011.csv", index=False)

print("\nBoth datasets cleaned successfully!")


# ==========================================
# 4. COMPARATIVE STATISTICAL ANALYSIS
# ==========================================

import pandas as pd
import numpy as np

def statistical_analysis(df, name):

    print("\nSTATISTICAL ANALYSIS:", name)

    measures = {
        "Mean Revenue": df["Revenue"].mean(),
        "Median Revenue": df["Revenue"].median(),
        "Mode Revenue": df["Revenue"].mode().iloc[0],
        "Standard Deviation": df["Revenue"].std(),
        "Variance": df["Revenue"].var(),
        "Mean Quantity": df["Quantity"].mean(),
        "Median Quantity": df["Quantity"].median(),
        "Mode Quantity": df["Quantity"].mode().iloc[0]
    }

    for measure, value in measures.items():
        print(f"{measure}: {value:.2f}")

    return measures


# Calculate statistical measures
stats1 = statistical_analysis(cleaned_df1, "Dataset 1 (2009-2010)")
stats2 = statistical_analysis(cleaned_df2, "Dataset 2 (2010-2011)")

# Comparative statistical table
comparison = pd.DataFrame({
    "Dataset 1": stats1,
    "Dataset 2": stats2
})

print("\nCOMPARATIVE STATISTICAL TABLE")
print(comparison.round(2))




# ==========================================
# 5. DATA ANALYTICS TECHNIQUES
# 5.1 DESCRIPTIVE ANALYTICS
# ==========================================

def descriptive_analysis(df, name):

    print("\nDESCRIPTIVE ANALYTICS:", name)

    total_revenue = df["Revenue"].sum()
    total_quantity = df["Quantity"].sum()
    total_transactions = df["Invoice"].nunique()
    average_price = df["Price"].mean()

    print("Total Sales Revenue:", round(total_revenue, 2))
    print("Total Quantity Sold:", total_quantity)
    print("Number of Transactions:", total_transactions)
    print("Average Product Price:", round(average_price, 2))

    monthly_sales = df.groupby(
        df["InvoiceDate"].dt.to_period("M")
    )["Revenue"].sum()

    print("\nMonthly Sales Performance:")
    print(monthly_sales)

    return monthly_sales


monthly1 = descriptive_analysis(
    cleaned_df1, "Dataset 1"
)

monthly2 = descriptive_analysis(
    cleaned_df2, "Dataset 2"
)




# ==========================================
# 5.2 COMPARATIVE ANALYTICS
# ==========================================

comparison_data = pd.DataFrame({
    "Dataset": ["2009-2010", "2010-2011"],

    "Total Revenue": [
        cleaned_df1["Revenue"].sum(),
        cleaned_df2["Revenue"].sum()
    ],

    "Total Quantity": [
        cleaned_df1["Quantity"].sum(),
        cleaned_df2["Quantity"].sum()
    ],

    "Transactions": [
        cleaned_df1["Invoice"].nunique(),
        cleaned_df2["Invoice"].nunique()
    ],

    "Average Price": [
        cleaned_df1["Price"].mean(),
        cleaned_df2["Price"].mean()
    ]
})

print("\nCOMPARATIVE BUSINESS PERFORMANCE")
print(comparison_data.round(2).to_string(index=False))



# ==========================================
# 5.3 PATTERN IDENTIFICATION
# ==========================================

def identify_patterns(df, name):

    print("\nPATTERN IDENTIFICATION:", name)

    # Frequently purchased products
    print("\nTop 10 Frequently Purchased Products:")
    print(
        df.groupby("Description")["Quantity"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    # Highest revenue-generating products
    print("\nTop 10 Revenue Generating Products:")
    print(
        df.groupby("Description")["Revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    # Customer purchasing behaviour
    customer_sales = df.dropna(
        subset=["Customer ID"]
    ).groupby("Customer ID")["Revenue"].sum()

    print("\nTop 10 Customers by Revenue:")
    print(customer_sales.sort_values(
        ascending=False
    ).head(10))

    # Country-wise revenue
    print("\nTop 10 Countries by Revenue:")
    print(
        df.groupby("Country")["Revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )


identify_patterns(cleaned_df1, "Dataset 1")
identify_patterns(cleaned_df2, "Dataset 2")



import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# LINE CHART - MONTHLY SALES TREND
# ==========================================

plt.figure(figsize=(12, 5))

plt.plot(
    monthly1.index.astype(str),
    monthly1.values,
    marker="o",
    label="2009-2010"
)

plt.plot(
    monthly2.index.astype(str),
    monthly2.values,
    marker="o",
    label="2010-2011"
)

plt.title("Monthly Sales Revenue Comparison")
plt.xlabel("Month")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("monthly_sales_trend.png", dpi=300)
plt.show()



# ==========================================
# BAR CHART - SALES COMPARISON
# ==========================================

fig, axes = plt.subplots(1, 2, figsize=(11, 5))

# Revenue comparison
axes[0].bar(
    ["2009-2010", "2010-2011"],
    comparison_data["Total Revenue"]
)
axes[0].set_title("Total Revenue Comparison")
axes[0].set_ylabel("Revenue")

# Quantity comparison
axes[1].bar(
    ["2009-2010", "2010-2011"],
    comparison_data["Total Quantity"]
)
axes[1].set_title("Total Quantity Sold")
axes[1].set_ylabel("Quantity")

plt.tight_layout()
plt.savefig("sales_comparison.png", dpi=300)
plt.show()


# ==========================================
# BAR CHART - SALES COMPARISON
# ==========================================

fig, axes = plt.subplots(1, 2, figsize=(11, 5))

# Revenue comparison
axes[0].bar(
    ["2009-2010", "2010-2011"],
    comparison_data["Total Revenue"]
)
axes[0].set_title("Total Revenue Comparison")
axes[0].set_ylabel("Revenue")

# Quantity comparison
axes[1].bar(
    ["2009-2010", "2010-2011"],
    comparison_data["Total Quantity"]
)
axes[1].set_title("Total Quantity Sold")
axes[1].set_ylabel("Quantity")

plt.tight_layout()
plt.savefig("sales_comparison.png", dpi=300)
plt.show()



# ==========================================
# BOX PLOT - REVENUE DISTRIBUTION
# ==========================================

plt.figure(figsize=(9, 5))

sns.boxplot(
    data=[
        cleaned_df1["Revenue"],
        cleaned_df2["Revenue"]
    ]
)

plt.xticks(
    [0, 1],
    ["2009-2010", "2010-2011"]
)

plt.title("Revenue Distribution Comparison")
plt.ylabel("Revenue")
plt.xlabel("Dataset")

plt.tight_layout()
plt.savefig("revenue_boxplot.png", dpi=300)
plt.show()



# ==========================================
# HISTOGRAM - SALES DISTRIBUTION
# ==========================================

plt.figure(figsize=(10, 5))

plt.hist(
    cleaned_df1["Revenue"],
    bins=50,
    alpha=0.6,
    label="2009-2010"
)

plt.hist(
    cleaned_df2["Revenue"],
    bins=50,
    alpha=0.6,
    label="2010-2011"
)

plt.title("Sales Revenue Distribution")
plt.xlabel("Revenue")
plt.ylabel("Frequency")
plt.legend()

plt.tight_layout()
plt.savefig("sales_histogram.png", dpi=300)
plt.show()


# B1.1 - Statistical Measures

def calculate_statistics(df, name):

    revenue = df["Revenue"]

    statistics = {
        "Mean": revenue.mean(),
        "Median": revenue.median(),
        "Mode": revenue.mode().iloc[0],
        "Minimum": revenue.min(),
        "Maximum": revenue.max(),
        "Q1 (25%)": revenue.quantile(0.25),
        "Q2 (50%)": revenue.quantile(0.50),
        "Q3 (75%)": revenue.quantile(0.75),
        "Range": revenue.max() - revenue.min(),
        "Variance": revenue.var(),
        "Standard Deviation": revenue.std(),
        "IQR": revenue.quantile(0.75) -
               revenue.quantile(0.25)
    }

    print("\n", name)

    for measure, value in statistics.items():
        print(f"{measure}: {value:.2f}")

    return statistics


# Calculate measures for both datasets
stats1 = calculate_statistics(
    cleaned_df1, "Dataset 1 (2009-2010)"
)

stats2 = calculate_statistics(
    cleaned_df2, "Dataset 2 (2010-2011)"
)

# Comparative table
comparison_stats = pd.DataFrame({
    "Dataset 1": stats1,
    "Dataset 2": stats2
})

print("\nCOMPARATIVE STATISTICAL ANALYSIS")
print(comparison_stats.round(2))




# ==========================================
# B1.2 - MODEL COMPARISON AND BEST MODEL
# ==========================================

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error, r2_score

def compare_models(df, name):

    # Prepare daily sales data
    daily = df.groupby(
        df["InvoiceDate"].dt.date
    )["Revenue"].sum().reset_index()

    daily.columns = ["Date", "Revenue"]
    daily["Date"] = pd.to_datetime(daily["Date"])

    # Extract features
    daily["Day"] = daily["Date"].dt.day
    daily["Month"] = daily["Date"].dt.month
    daily["Year"] = daily["Date"].dt.year
    daily["DayOfWeek"] = daily["Date"].dt.dayofweek

    X = daily[["Day", "Month", "Year", "DayOfWeek"]]
    y = daily["Revenue"]

    # Time-based train-test split
    split = int(len(daily) * 0.8)

    X_train, X_test = X.iloc[:split], X.iloc[split:]
    y_train, y_test = y.iloc[:split], y.iloc[split:]

    # Models
    models = {
        "Linear Regression": LinearRegression(),
        "Decision Tree": DecisionTreeRegressor(
            max_depth=5, random_state=42
        ),
        "Random Forest": RandomForestRegressor(
            n_estimators=100,
            max_depth=10,
            random_state=42,
            n_jobs=-1
        )
    }

    results = []

    for model_name, model in models.items():

        model.fit(X_train, y_train)
        predictions = model.predict(X_test)

        mae = mean_absolute_error(y_test, predictions)
        rmse = np.sqrt(
            mean_squared_error(y_test, predictions)
        )
        r2 = r2_score(y_test, predictions)

        results.append({
            "Model": model_name,
            "MAE": mae,
            "RMSE": rmse,
            "R2 Score": r2
        })

    result_df = pd.DataFrame(results)

    # Rank models: lower MAE/RMSE and higher R2
    result_df["MAE Rank"] = result_df["MAE"].rank()
    result_df["RMSE Rank"] = result_df["RMSE"].rank()
    result_df["R2 Rank"] = result_df["R2 Score"].rank(
        ascending=False
    )

    result_df["Average Rank"] = result_df[
        ["MAE Rank", "RMSE Rank", "R2 Rank"]
    ].mean(axis=1)

    result_df = result_df.sort_values("Average Rank")

    print("\nMODEL COMPARISON:", name)
    print(result_df.round(3).to_string(index=False))

    best_model = result_df.iloc[0]["Model"]

    print("\nBEST MODEL:", best_model)

    return result_df


# Compare models on both datasets
comparison1 = compare_models(
    cleaned_df1, "Dataset 1 (2009-2010)"
)

comparison2 = compare_models(
    cleaned_df2, "Dataset 2 (2010-2011)"
)

# Combined comparison
print("\nFINAL MODEL COMPARISON")

print("\nDataset 1:")
print(comparison1[["Model", "MAE", "RMSE", "R2 Score"]])

print("\nDataset 2:")
print(comparison2[["Model", "MAE", "RMSE", "R2 Score"]])
