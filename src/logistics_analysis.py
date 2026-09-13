"""
Week 1 Logistics Data Analysis — starter implementation.
Demonstrates transaction cleaning, daily demand aggregation,
feature engineering, and a simple forecasting baseline.
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

df = pd.read_excel("Online Retail.xlsx")
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
df["Revenue"] = df["Quantity"] * df["UnitPrice"]
df["IsCancellation"] = df["InvoiceNo"].astype(str).str.startswith("C")

df = df.drop_duplicates()
df.loc[df["Quantity"] <= 0, "Quantity"] = np.nan

daily = (
    df[~df["IsCancellation"]]
    .dropna(subset=["Quantity", "StockCode"])
    .assign(Date=lambda x: x["InvoiceDate"].dt.normalize())
    .groupby(["Date", "StockCode"], as_index=False)["Quantity"]
    .sum()
)

daily = daily.sort_values(["StockCode", "Date"])
g = daily.groupby("StockCode")["Quantity"]
daily["lag_1"] = g.shift(1)
daily["lag_7"] = g.shift(7)
daily["rolling_7"] = g.shift(1).rolling(7).mean().reset_index(level=0, drop=True)
daily["dow"] = daily["Date"].dt.dayofweek
daily["month"] = daily["Date"].dt.month

model_df = daily.dropna()
features = ["lag_1", "lag_7", "rolling_7", "dow", "month"]

split = int(len(model_df) * 0.8)
X_train, X_test = model_df[features].iloc[:split], model_df[features].iloc[split:]
y_train, y_test = model_df["Quantity"].iloc[:split], model_df["Quantity"].iloc[split:]

model = RandomForestRegressor(n_estimators=200, random_state=42, n_jobs=-1)
model.fit(X_train, y_train)
pred = model.predict(X_test)

print("MAE:", mean_absolute_error(y_test, pred))
