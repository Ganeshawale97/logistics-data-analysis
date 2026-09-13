# Logistics Data Dictionary

## UCI Online Retail

| Column | Type | Meaning |
|---|---|---|
| InvoiceNo | String | Transaction/invoice identifier; cancellations are commonly prefixed with C |
| StockCode | String | Product identifier |
| Description | String | Product description |
| Quantity | Integer | Units in the transaction |
| InvoiceDate | Datetime | Transaction date and time |
| UnitPrice | Float | Unit price in GBP |
| CustomerID | Identifier | Customer identifier; some values are missing |
| Country | Category | Customer country |

## Derived fields

- IsCancellation — identifies cancellation-related invoices.
- Revenue — Quantity multiplied by UnitPrice.
- Date — normalized calendar date.
- Year, Month, DayOfWeek — time features for trend and seasonality analysis.

## Data-quality rules

1. Validate expected columns and data types.
2. Parse InvoiceDate and inspect invalid values.
3. Assess exact duplicates before removing them.
4. Separate cancellations and returns from positive demand.
5. Do not invent customer identifiers for missing CustomerID values.
6. Check positive ranges for quantity and unit price in the demand table.
7. Flag extreme values before deciding whether they are errors or genuine large orders.
