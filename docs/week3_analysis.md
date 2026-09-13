# Week 3 — Advanced Data Analysis & Visualization

## 1. Overview

Week 3 extends the logistics analytics workflow from preprocessing into exploratory data analysis (EDA), visualization, interpretation and operational recommendations. A hypothetical dataset of 600 shipments was simulated for the exercise.

The analytical objective is not simply to create charts, but to answer operational questions: where delays occur, what drives transportation cost, how performance varies by operating zone, and which variables could support later predictive models.

## 2. Dataset variables

| Variable | Type | Logistics meaning |
|---|---|---|
| Shipment_ID | Categorical | Unique shipment reference |
| Zone | Categorical | North, South, East, West or Central operating region |
| Transport_Mode | Categorical | Truck, Van or Two-Wheeler |
| Shipment_Volume_kg | Numeric | Shipment size |
| Distance_km | Numeric | Delivery distance |
| Delivery_Time_hr | Numeric | End-to-end delivery duration |
| Transport_Cost_INR | Numeric | Estimated transportation cost |
| On_Time | Boolean | Whether the shipment met its simulated target |

## 3. Analytical questions

1. What is the typical delivery time and shipment size?
2. How widely do delivery times vary?
3. Does longer distance correspond to higher transport cost?
4. Which zones show slower delivery performance?
5. Which numerical variables have strong relationships?
6. Where are potential operational outliers or bottlenecks?
7. Which features should be considered for future predictive modeling?

## 4. EDA performed

1. Descriptive statistics using count, mean, median, standard deviation, minimum and maximum.
2. Delivery-time distribution analysis.
3. Distance-versus-cost relationship analysis.
4. Zone-level delivery-time comparison.
5. Transport-mode comparison.
6. Correlation analysis across numerical variables.
7. Outlier and exception interpretation.
8. Translation of analytical findings into operational recommendations.

## 5. Descriptive statistics

Central tendency is important because logistics managers need a baseline for normal operations. Mean delivery time provides an overall average, while median delivery time is less sensitive to unusually long shipments. Standard deviation indicates how variable performance is.

For operational reporting, these statistics should be accompanied by segment-level analysis because a good overall average can hide a poorly performing zone or transport mode.

## 6. Visualization choices

| Visualization | Logistics question | Why it is useful |
|---|---|---|
| Histogram | What does normal delivery performance look like? | Reveals concentration, spread and long-delay tails |
| Scatter plot | How does distance relate to cost? | Shows relationship, spread and unusual observations |
| Bar chart | Which zones have slower delivery times? | Makes category comparisons easy |
| Correlation matrix | Which numerical variables move together? | Supports relationship discovery and feature selection |

## 7. Visualization 1 — Delivery-Time Distribution

The histogram shows how delivery times are distributed across shipments. A concentrated central range represents typical operating behavior, while a long right-side tail can indicate delayed shipments or unusual operational conditions.

**Operational use:** Management can define investigation thresholds for unusually slow shipments and then examine route, zone, transport mode and shipment characteristics.

## 8. Visualization 2 — Distance vs Transport Cost

The scatter plot compares route distance with transportation cost. An upward relationship is expected because longer journeys generally require more resources. Variation around that relationship can indicate the influence of shipment volume, transport mode and other operating conditions.

**Operational use:** Distance can be incorporated into cost estimation, route planning and scenario analysis.

## 9. Visualization 3 — Zone-Level Delivery Performance

Average delivery time is compared across operating zones. Segmenting the KPI prevents overall averages from hiding local bottlenecks.

**Operational use:** A consistently slower zone can be investigated for traffic exposure, dispatch timing, route design, workload concentration, distance mix or resource availability.

## 10. Visualization 4 — Correlation Analysis

The correlation matrix summarizes linear relationships among shipment volume, distance, delivery time and transport cost.

Correlation can help identify useful modeling variables, but it does not establish causation. Operational decisions should therefore combine statistical evidence with domain knowledge.

## 11. Transport-mode analysis

Transport mode should be evaluated using more than cost alone. A higher-cost mode may still be valuable if it provides faster service, greater capacity or better coverage.

Recommended comparison dimensions:

- Average cost per shipment
- Average delivery time
- On-time rate
- Average shipment volume
- Distance profile
- Utilization or capacity, when available

## 12. Key analytical insights

- Longer routes generally require higher transportation expenditure in the simulated data.
- Zone-level comparison can expose bottlenecks hidden by an overall average KPI.
- Unusually long delivery times and high costs should be investigated as operational exceptions rather than automatically deleted.
- Transport mode should be evaluated together with cost, capacity and service performance.
- Distance, shipment volume and transport mode are useful candidate features for future cost and demand models.
- Visual analysis makes operational variation easier to communicate to non-technical decision-makers.

## 13. Potential bottlenecks

Potential bottlenecks indicated by the simulated analysis include:

1. **Geographical delays:** some zones have higher average delivery time.
2. **Long-distance cost pressure:** transportation expenditure increases as route distance increases.
3. **Operational exceptions:** extreme delivery times can disproportionately affect service-level KPIs.
4. **Resource mismatch:** transport modes may have different cost and service characteristics.

These are hypotheses for operational investigation, not proof of root cause.

## 14. Recommendations

1. Monitor delivery time and on-time performance by zone.
2. Include route distance and shipment volume in future cost models.
3. Investigate repeated high-delay shipments instead of treating every outlier as a data error.
4. Evaluate route alternatives for underperforming zones against baseline KPIs.
5. Compare transport modes using both cost and service outcomes.
6. Build a recurring dashboard covering volume, delivery time, cost and service level.
7. Establish KPI thresholds that trigger operational review.
8. Feed validated Week 3 features into later forecasting and optimization experiments.

## 15. Suggested next-stage modeling

### Demand forecasting
Aggregate shipment volume by day or week and compare baseline forecasting methods before introducing more complex models.

### Cost prediction
Use distance, volume and transport mode as candidate predictors of transportation cost. Compare baseline regression with nonlinear models where justified.

### Delivery-risk prediction
If actual promised and delivered timestamps become available, create a late-delivery target and evaluate classification using precision, recall and suitable ranking metrics.

### Route optimization
Use distance, capacity, service windows and vehicle constraints to formulate a vehicle-routing problem. Compare optimized routes against a baseline using cost, distance and service-level KPIs.

## 16. Validation and data leakage

For future prediction tasks, the train/test split must respect time where the goal is forecasting future operations. Preprocessing steps that learn parameters from data, such as scaling or imputation, should be fitted on training data and then applied to validation/test data.

## 17. Python workflow

The Week 3 Python implementation follows this sequence:

**Load → Validate → Describe → Group → Correlate → Visualize → Interpret → Recommend**

Example:

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("logistics_shipments.csv")

numeric = [
    "Shipment_Volume_kg",
    "Distance_km",
    "Delivery_Time_hr",
    "Transport_Cost_INR",
]

print(df[numeric].describe())
print(df[numeric].agg(["mean", "median"]))
print(df[numeric].corr())

plt.hist(df["Delivery_Time_hr"], bins=30)
plt.xlabel("Delivery Time (hours)")
plt.ylabel("Shipments")
plt.title("Delivery-Time Distribution")
plt.show()

zone_time = df.groupby("Zone")["Delivery_Time_hr"].mean().sort_values()
zone_time.plot(kind="bar")
plt.ylabel("Average Delivery Time (hours)")
plt.title("Average Delivery Time by Zone")
plt.show()
```

## 18. Decision framework

A useful logistics analytics process should connect every chart to a decision:

**Observation → Business implication → Action → KPI → Follow-up**

Example:

**Observation:** One zone has persistently higher delivery time.  
**Implication:** Service reliability may be constrained locally.  
**Action:** Review route design and dispatch patterns.  
**KPI:** Average delivery time and on-time rate.  
**Follow-up:** Compare the KPI before and after intervention.

## 19. Limitations

The Week 3 dataset is hypothetical and was created for academic demonstration. It should not be interpreted as evidence about a real logistics company. Simulated relationships are useful for demonstrating analytical methods but must be replaced with validated operational data before business decisions are made.

## 20. Reproducibility

The accompanying Week 3 DOCX contains the full narrative, embedded charts, methodology, code illustration and recommendations. The dataset is synthetic and intended for academic demonstration only.

## 21. Conclusion

The Week 3 analysis demonstrates how exploratory data analysis and visualization can convert shipment records into operational insight. Descriptive statistics establish a baseline, distributions reveal normal behavior and exceptions, group comparisons expose geographical differences, and relationship plots help identify potential cost drivers.

The key principle is that visualization should answer a logistics question rather than simply display a chart. The resulting insights can guide further work in demand forecasting, delivery-risk prediction, segmentation and route optimization. When combined with validated operational data, these methods can support better resource allocation, service reliability and transportation cost management.
