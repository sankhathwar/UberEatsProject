# Uber Eats Operational & Customer Intelligence System

## Here is the [PPT link](https://docs.google.com/presentation/d/16Ch8WEG8i1SOm8z6V8Lit_euRYdOSoILEYXgx1LZ6lk/edit?usp=sharing)

## Project Overview

This project is an end-to-end Machine Learning and Analytics solution for a food-delivery marketplace.

The objective is to use customer, restaurant, order, delivery, review, and payment data to identify customer behavior, understand operational performance, predict delivery outcomes, analyze customer sentiment, and forecast order demand.

The project is being developed as part of an ML-focused Data Analyst training capstone.

---

## Business Objectives

The system focuses on four major analytical and machine learning use cases:

### 1. Customer Segmentation

Identify distinct customer groups based on behavioral and transactional characteristics such as:

* Order frequency
* Total spending
* Average order value
* Recency
* Customer engagement
* Membership type

Potential use cases include customer targeting, retention campaigns, and loyalty strategies.

### 2. Customer Sentiment Analysis

Analyze customer reviews to identify positive, neutral, and negative customer sentiment.

The objective is to understand the major drivers of customer dissatisfaction and identify areas for operational improvement.

### 3. Delivery-Time Prediction

Predict delivery time using operational and contextual variables such as:

* Delivery distance
* Restaurant preparation time
* Traffic condition
* Weather
* Peak-hour demand
* Driver characteristics

The objective is to improve delivery-time estimation and operational planning.

### 4. Hourly Demand Forecasting

Forecast hourly order demand using historical order timestamps and marketplace patterns.

The objective is to support:

* Driver allocation
* Restaurant capacity planning
* Peak-hour operations
* Supply-demand balancing

---

## Technology Stack

* Python
* Pandas
* NumPy
* Scikit-learn
* NLTK / spaCy
* Statsmodels
* Prophet
* Matplotlib
* Seaborn
* SQL
* Git

---

## Project Structure

```text
uber-eats-ml-capstone/
│
├── data/
│   ├── raw/
│   │   ├── customers.csv
│   │   ├── restaurants.csv
│   │   ├── drivers.csv
│   │   ├── orders.csv
│   │   ├── deliveries.csv
│   │   ├── reviews.csv
│   │   └── payments.csv
│   │
│   └── processed/
│
├── notebooks/
│
├── src/
│   ├── __init__.py
│   ├── generate_data.py
│   └── validate_data.py
│
├── docs/
│   └── data_dictionary.md
│
├── prompts/
│   └── synthetic_data_prompt.md
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Dataset Architecture

The project contains seven related datasets.

```text
Customers
    │
    ▼
Orders ◄──── Restaurants
    │
    ├──────────────► Reviews
    │
    ├──────────────► Payments
    │
    ▼
Deliveries ◄──── Drivers
```

### Customers

Contains customer demographic and membership information.

### Restaurants

Contains restaurant location, cuisine, rating, pricing, and preparation-time information.

### Drivers

Contains driver demographic, vehicle, rating, experience, and city information.

### Orders

Central marketplace transaction table containing customer, restaurant, timestamp, order value, payment method, and order status.

### Deliveries

Contains delivery distance, preparation time, traffic, weather, tip, and actual delivery duration.

### Reviews

Contains customer ratings and review text for sentiment analysis.

### Payments

Contains order-level payment and transaction information.

---

## Synthetic Data Generation

The datasets were generated programmatically rather than manually created.

A fixed random seed is used to make the data generation process reproducible.

```text
RANDOM_SEED = 42
```

The data generator uses:

* Pandas
* NumPy
* Faker

The generator creates relationships between datasets using primary and foreign keys.

---

## Synthetic Data Design

The synthetic data was designed around the downstream ML requirements rather than generated as completely independent random values.

### Delivery Time

Delivery time is influenced by:

* Delivery distance
* Restaurant preparation time
* Traffic condition
* Weather
* Peak-hour demand
* Random operational noise

This allows machine learning models to learn meaningful relationships.

### Order Demand

Order timestamps contain realistic marketplace patterns:

* Lunch peak
* Dinner peak
* Higher weekend demand
* Lower early-morning demand

### Customer Reviews

Review ratings are influenced by delivery experience, while review text broadly reflects the rating.

Random variation is included to avoid creating a perfectly deterministic dataset.

---

## Data Quality Validation

The generated data is validated for:

* Missing values
* Duplicate records
* Duplicate primary keys
* Foreign-key integrity
* Valid categorical values
* Valid numerical ranges
* Realistic business relationships

Current validation results:

| Dataset     |    Rows |
| ----------- | ------: |
| Customers   |  10,000 |
| Restaurants |     500 |
| Drivers     |   1,000 |
| Orders      | 100,000 |
| Deliveries  |  90,002 |
| Reviews     |  54,001 |
| Payments    | 100,000 |

No missing values or duplicate records were found in the initial validation.

Foreign-key validation also returned zero invalid relationships.

---

## How to Run

### 1. Create the virtual environment

```bash
python3 -m venv .venv
```

### 2. Activate it

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Generate the datasets

```bash
python src/generate_data.py
```

### 5. Validate the generated data

```bash
python src/validate_data.py
```

---

## Development Workflow

The project uses Git for version control.

The primary development branch is:

```text
feature/uber-eats-pipeline
```

Development follows incremental commits so that data generation, validation, analysis, feature engineering, modelling, and business interpretation can be tracked separately.

---

## Planned ML Pipeline

```text
Raw Data
    ↓
Data Validation
    ↓
EDA
    ↓
Feature Engineering
    ↓
Model Development
    ↓
Model Evaluation
    ↓
Business Interpretation
    ↓
Recommendations
```

---

## Expected Business Outcomes

The final system will provide recommendations around:

* Customer targeting
* Customer retention
* Restaurant performance
* Delivery operations
* Driver allocation
* Customer experience
* Demand planning
* Marketplace efficiency

The final objective is not only to build accurate models, but to translate model outputs into actionable business decisions.
# UberEatsProject
