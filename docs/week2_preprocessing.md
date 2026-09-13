# Week 2 — Data Collection, Cleaning & Preprocessing

## Objective

Build a trustworthy data foundation for later logistics analytics and machine-learning tasks.

## Reference dataset

The project uses the public UCI Online Retail dataset as a demand-analysis reference. It provides transaction-level information including invoice, product, quantity, timestamp, price, customer and country fields.

## End-to-end pipeline

Raw data → Schema validation → Data profiling → Duplicate assessment → Missing-value analysis → Cancellation/return classification → Range checks and outlier detection → Feature engineering → Scaling when required → Quality validation → Analysis-ready data

## Cleaning strategy

### Missing values
Missing identifiers are not automatically replaced. Treatment depends on whether the downstream analysis requires a reliable identifier.

### Duplicates
Exact duplicates are measured first, then removed when justified. Row counts are recorded before and after cleaning.

### Returns and cancellations
Cancellation and return records are separated so that negative or reversed transactions do not silently distort positive-demand estimates.

### Outliers
IQR and quantile-based rules can flag unusual quantity and price values. Every flagged record should be investigated before removal because large legitimate orders are possible.

### Normalization and standardization
Scaling is applied only to features and algorithms that need it. For predictive modeling, learned transformations must be fitted on training data only to prevent data leakage.

## Quality checklist

- Expected columns present
- Data types validated
- Missingness profiled
- Duplicates assessed
- Cancellations classified
- Numeric ranges checked
- Outliers flagged
- Derived features validated
- Final schema documented
- Processing is reproducible
