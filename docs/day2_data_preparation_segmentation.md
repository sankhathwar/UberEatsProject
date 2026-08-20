# Day 2 – Data Preparation & Customer/Restaurant Segmentation

## 1. Objective

The objective of Day 2 was to prepare customer and restaurant-level analytical features and apply unsupervised machine learning techniques to identify behavioral patterns.

The following techniques were used:

- Feature Engineering
- Data Quality Validation
- Feature Selection
- StandardScaler
- K-Means Clustering
- Elbow Method
- Silhouette Score
- PCA
- DBSCAN
- Cluster Profiling
- Business Interpretation

---

# 2. Data Preparation

The synthetic datasets generated on Day 1 were used as the source data.

The following datasets were available:

- Customers
- Restaurants
- Orders
- Deliveries
- Reviews
- Drivers
- Payments

All datasets passed the basic data-quality checks performed during Day 1.

For customer and restaurant segmentation, transactional and operational data were aggregated to the customer and restaurant level.

Identifiers such as `customer_id` and `restaurant_id` were retained for identification and reporting but were excluded from machine learning features.

---

# 3. Customer Feature Engineering

The following customer-level features were created:

| Feature | Description |
|---|---|
| `total_orders` | Total number of orders placed by the customer |
| `avg_order_value` | Average monetary value per order |
| `total_spending` | Total amount spent by the customer |
| `ordering_frequency` | Customer ordering frequency |
| `avg_rating_given` | Average rating provided by the customer |
| `weekend_orders` | Number of orders placed on weekends |
| `late_night_orders` | Number of orders placed during late-night hours |

The resulting customer feature dataset contained:

- 10,000 customers
- 7 analytical features
- 0 missing values

The identifier `customer_id` was excluded before model training.

---

# 4. Customer Feature Analysis

The customer feature distributions were examined using descriptive statistics and correlation analysis.

Important observations:

- `total_orders` and `total_spending` had a strong positive relationship.
- `total_orders` and `weekend_orders` were positively related.
- `total_orders` and `late_night_orders` also showed a positive relationship.
- `avg_order_value` was relatively independent of total order count.
- `avg_rating_given` showed little relationship with most behavioral variables.

This indicated that customers differed primarily in engagement, spending, weekend behavior and late-night behavior.

---

# 5. Restaurant Feature Engineering

Restaurant-level features were created using orders, reviews and delivery data.

The following features were used:

| Feature | Description |
|---|---|
| `total_orders` | Total number of orders received by the restaurant |
| `revenue` | Total revenue generated from orders |
| `avg_rating` | Average customer rating received |
| `avg_preparation_time` | Average food preparation time |
| `cancellation_rate` | Percentage of orders cancelled |
| `avg_delivery_time` | Average delivery time associated with the restaurant |

The resulting dataset contained:

- 500 restaurants
- 6 analytical features
- 0 missing values

The identifiers were excluded from machine learning.

During feature selection, `avg_delivery_time` was excluded from the restaurant clustering model because it had extremely high correlation with `avg_preparation_time`.

The final restaurant clustering features were:

- `total_orders`
- `revenue`
- `avg_rating`
- `avg_preparation_time`
- `cancellation_rate`

---

# 6. Feature Scaling

StandardScaler was applied before clustering.

```python
StandardScaler()
