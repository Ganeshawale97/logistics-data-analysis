# Week 3 — Advanced Data Analysis & Visualization

## Overview

Week 3 extends the logistics analytics workflow from preprocessing into exploratory data analysis (EDA), visualization, interpretation and operational recommendations. A hypothetical dataset of 600 shipments was simulated for the exercise.

## Dataset variables

- Shipment_ID — unique shipment reference
- Zone — North, South, East, West or Central
- Transport_Mode — Truck, Van or Two-Wheeler
- Shipment_Volume_kg — shipment size
- Distance_km — delivery distance
- Delivery_Time_hr — delivery duration
- Transport_Cost_INR — estimated transportation cost
- On_Time — whether the shipment met its simulated target

## EDA performed

1. Descriptive statistics using count, mean, median, standard deviation, minimum and maximum.
2. Delivery-time distribution analysis.
3. Distance-versus-cost relationship analysis.
4. Zone-level delivery-time comparison.
5. Correlation analysis across numerical variables.
6. Operational interpretation of delays, cost drivers and geographical variation.

## Visualization choices

| Visualization | Logistics question |
|---|---|
| Histogram | What does normal delivery performance look like, and are there long-delay observations? |
| Scatter plot | How does route distance relate to transportation cost? |
| Bar chart | Which operating zones have slower average deliveries? |
| Correlation matrix | Which numerical variables move together and may be useful for modeling? |

## Key analytical insights

- Longer routes generally require higher transportation expenditure in the simulated data.
- Zone-level comparison can expose bottlenecks hidden by an overall average KPI.
- Unusually long delivery times and high costs should be investigated as operational exceptions rather than automatically deleted.
- Transport mode should be evaluated together with cost, capacity and service performance.
- Distance, shipment volume and transport mode are useful candidate features for future cost and demand models.

## Recommendations

- Monitor delivery time and on-time performance by zone.
- Include route distance and shipment volume in future cost models.
- Investigate repeated high-delay shipments and compare them with route, mode and dispatch conditions.
- Evaluate route alternatives for underperforming zones against baseline KPIs.
- Build a recurring dashboard covering volume, delivery time, cost and service level.

## Reproducibility

The accompanying Week 3 DOCX contains the full narrative, embedded charts, methodology, code illustration and recommendations. The dataset is synthetic and intended for academic demonstration only.
