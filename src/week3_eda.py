"""Week 3 EDA and visualization example.

This script demonstrates the analysis structure used in the Week 3 report.
The report uses a synthetic logistics dataset with shipment volume,
distance, delivery time, transport cost, zone and transport mode.
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load a prepared shipment dataset.
df = pd.read_csv("data/processed/logistics_shipments.csv")

# 1. Descriptive statistics
numeric = [
    "Shipment_Volume_kg",
    "Distance_km",
    "Delivery_Time_hr",
    "Transport_Cost_INR",
]
print(df[numeric].describe())
print(df[numeric].agg(["mean", "median"]))

# 2. Correlation
print(df[numeric].corr())

# 3. Delivery-time distribution
plt.figure(figsize=(8, 5))
plt.hist(df["Delivery_Time_hr"], bins=30)
plt.xlabel("Delivery Time (hours)")
plt.ylabel("Number of Shipments")
plt.title("Distribution of Delivery Times")
plt.tight_layout()
plt.show()

# 4. Distance vs cost
plt.figure(figsize=(8, 5))
plt.scatter(df["Distance_km"], df["Transport_Cost_INR"], alpha=0.45)
plt.xlabel("Distance (km)")
plt.ylabel("Transport Cost (INR)")
plt.title("Distance vs Transport Cost")
plt.tight_layout()
plt.show()

# 5. Zone comparison
zone_time = df.groupby("Zone")["Delivery_Time_hr"].mean().sort_values()
plt.figure(figsize=(8, 5))
plt.bar(zone_time.index, zone_time.values)
plt.xlabel("Zone")
plt.ylabel("Average Delivery Time (hours)")
plt.title("Average Delivery Time by Zone")
plt.tight_layout()
plt.show()
