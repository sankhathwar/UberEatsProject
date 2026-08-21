# Day 5 – Hourly Demand Forecasting

## 1. Objective

The objective of Day 5 was to forecast future Uber Eats order demand using time-series forecasting techniques.

The analysis focused on:

- Hourly demand aggregation
- Demand pattern analysis
- Time-series decomposition
- Stationarity testing
- ARIMA forecasting
- Prophet forecasting
- Chronological train/test validation
- Model comparison
- Future demand forecasting

The target variable was hourly completed-order volume.

---

## 2. Dataset Preparation

The orders dataset contained 100,000 orders.

Order status distribution:

| Status | Orders |
|---|---:|
| Completed | 90,002 |
| Cancelled | 6,862 |
| Failed | 3,136 |

Only completed orders were used for demand forecasting.

### Hourly Demand Aggregation

Orders were grouped by hour using the order timestamp.

The resulting hourly demand dataset contained:

```text
13,081 hourly observations
