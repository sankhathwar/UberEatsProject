# Synthetic Data Generation Prompt — Uber Eats ML Capstone

## P — Persona

You are a senior Data Engineer and Machine Learning Engineer specializing in food-delivery and marketplace analytics.

You have experience designing realistic synthetic datasets for customer analytics, restaurant analytics, delivery operations, NLP, machine learning, and demand forecasting.

Your priority is to create data that is:

* Realistic
* Internally consistent
* Reproducible
* Suitable for exploratory data analysis
* Suitable for machine learning
* Suitable for SQL analysis
* Representative of a food-delivery marketplace

Do not generate arbitrary independent random values. Create meaningful relationships between variables so that downstream ML models can learn realistic patterns.

---

## T — Task

Create a production-style Python script named `generate_data.py` that generates synthetic Uber Eats marketplace data.

The script must generate seven related CSV datasets:

1. customers.csv
2. restaurants.csv
3. drivers.csv
4. orders.csv
5. deliveries.csv
6. reviews.csv
7. payments.csv

Save all generated files inside:

`data/raw/`

The script must be reproducible using a fixed random seed.

Use Python with:

* pandas
* numpy
* Faker
* Python standard library

Do not require external APIs or internet access.

---

## C — Context

### Business Domain

The project represents a food-delivery marketplace similar to Uber Eats.

The generated datasets will later be used for:

1. Customer segmentation
2. Customer sentiment analysis
3. Delivery-time prediction
4. Hourly order-demand forecasting
5. SQL-based marketplace analysis
6. Business KPI analysis

---

## Dataset Size

Generate approximately:

| Dataset     |     Rows |
| ----------- | -------: |
| Customers   |   10,000 |
| Restaurants |      500 |
| Drivers     |    1,000 |
| Orders      |  100,000 |
| Deliveries  | ~100,000 |
| Reviews     |  ~60,000 |
| Payments    | ~100,000 |

Generate data between:

`2025-01-01` and `2026-06-30`

---

## Geographic Coverage

Use these Indian cities:

* Bangalore
* Chennai
* Hyderabad
* Mumbai
* Delhi
* Pune
* Kolkata
* Ahmedabad
* Jaipur
* Kochi

---

# Dataset Schemas

## Customers

Columns:

* customer_id
* age
* gender
* city
* signup_date
* membership_type

Constraints:

* customer_id must be unique
* age should generally be between 18 and 70
* membership_type should contain Standard, Gold, and Premium
* signup_date must be before the customer's orders

---

## Restaurants

Columns:

* restaurant_id
* restaurant_name
* city
* cuisine
* restaurant_rating
* avg_prep_time
* price_range

Constraints:

* restaurant_id must be unique
* restaurant_rating must be between 1 and 5
* avg_prep_time should generally be between 10 and 60 minutes
* restaurants should belong to one of the supported cities

Cuisines may include:

* Indian
* Chinese
* Italian
* Mexican
* Biryani
* South Indian
* North Indian
* Fast Food
* Desserts
* Healthy

---

## Drivers

Columns:

* driver_id
* driver_age
* driver_rating
* vehicle_type
* city
* experience_years

Constraints:

* driver_id must be unique
* driver_age should generally be between 18 and 60
* driver_rating must be between 1 and 5
* vehicle_type may include Bike, Scooter, and Car
* experience_years must be non-negative

---

## Orders

Columns:

* order_id
* customer_id
* restaurant_id
* order_timestamp
* order_amount
* item_count
* payment_method
* order_status

Constraints:

* order_id must be unique
* customer_id must reference an existing customer
* restaurant_id must reference an existing restaurant
* order_timestamp must fall within the project date range
* order_amount must be positive for completed orders
* item_count should generally be between 1 and 8
* payment_method may include UPI, Credit Card, Debit Card, Cash, and Wallet
* order_status may include Completed, Cancelled, and Failed

Create realistic hourly demand patterns:

* Lunch peak around 12 PM–2 PM
* Dinner peak around 7 PM–10 PM
* Higher demand on weekends
* Lower demand during early morning hours

---

## Deliveries

Columns:

* delivery_id
* order_id
* driver_id
* delivery_distance_km
* preparation_time_min
* delivery_time_min
* traffic_condition
* weather
* tip_amount
* delivery_status

Constraints:

* delivery_id must be unique
* order_id must reference an existing order
* driver_id must reference an existing driver
* distance must be positive
* preparation time must be positive
* delivery time must be positive

Delivery time must not be generated independently.

Create a realistic relationship:

delivery_time_min should increase with:

* delivery_distance_km
* preparation_time_min
* traffic congestion

Delivery time should also generally increase during:

* peak hours
* rainy weather

Driver rating and restaurant rating may have smaller effects.

Include realistic random noise so the relationship is not perfectly deterministic.

Traffic values:

* Low
* Medium
* High

Weather values:

* Clear
* Cloudy
* Rainy
* Stormy

---

## Reviews

Columns:

* review_id
* order_id
* customer_id
* review_rating
* review_text
* review_timestamp

Constraints:

* Generate reviews primarily for completed orders
* review_rating must be between 1 and 5
* review_timestamp must be after the order timestamp
* customer_id and order_id must reference existing records

Generate approximately 60% as many reviews as completed orders.

The review text should broadly correspond to the review rating.

Examples:

Rating 5:
"The food arrived hot and the delivery was very quick. Great experience."

Rating 3:
"The food was okay, but the delivery took longer than expected."

Rating 1:
"The order arrived very late and the food was cold. Very disappointing."

Do not make every review identical or perfectly deterministic.

Create variation in wording, sentence structure, food quality, delivery experience, packaging, and service.

---

## Payments

Columns:

* payment_id
* order_id
* customer_id
* payment_method
* order_amount
* tip_amount
* payment_status

Constraints:

* payment_id must be unique
* order_id must reference an existing order
* customer_id must reference the correct customer
* order_amount should match the corresponding order
* tip_amount should match the corresponding delivery where applicable
* payment_status may include Success, Failed, and Refunded

---

# Few-Shot Examples

Use the following examples as guidance for realistic relationships.

### Example 1 — Delivery Time

Input characteristics:

distance = 2 km
preparation_time = 15 minutes
traffic = Low
weather = Clear

Expected behavior:

delivery_time should generally be relatively low.

---

### Example 2 — Difficult Delivery

Input characteristics:

distance = 10 km
preparation_time = 35 minutes
traffic = High
weather = Rainy

Expected behavior:

delivery_time should generally be substantially higher.

---

### Example 3 — Positive Review

Input:

rating = 5
delivery_time = 25 minutes

Example output:

"The food was fresh and arrived quickly. Really happy with the experience."

---

### Example 4 — Negative Review

Input:

rating = 1
delivery_time = 75 minutes

Example output:

"The delivery took far too long and the food arrived cold. Very disappointing."

---

### Example 5 — Demand Pattern

Input:

Saturday, 20:00

Expected behavior:

Order probability should be higher than:

Tuesday, 04:00

Do not hard-code the exact same order count for every peak period. Add natural variation.

---

# Data Quality Requirements

The script must include validation checks after generation.

Validate:

1. Row counts
2. Duplicate primary keys
3. Missing values
4. Foreign-key relationships
5. Invalid ratings
6. Invalid dates
7. Negative monetary values
8. Negative delivery distances
9. Invalid categorical values

Print a concise validation report.

---

# Realism Requirements

Introduce realistic variability.

Do not generate perfectly uniform distributions.

Examples:

* Some restaurants should receive significantly more orders than others.
* Some customers should order frequently while others order rarely.
* Some drivers should have higher ratings than others.
* Weekend demand should differ from weekday demand.
* Lunch and dinner should have higher demand.
* Traffic should influence delivery time.
* Weather should influence delivery time.
* Higher-value orders may have somewhat higher tips.
* Customer review ratings should broadly correlate with delivery experience.
* Cancellations should be relatively uncommon but present.

---

# Reproducibility

Use fixed random seeds.

The script should produce the same dataset when executed with the same seed.

Use a clearly defined constant such as:

`RANDOM_SEED = 42`

---

# Code Quality Requirements

Create clean, modular Python code.

Use separate functions such as:

* generate_customers()
* generate_restaurants()
* generate_drivers()
* generate_orders()
* generate_deliveries()
* generate_reviews()
* generate_payments()
* validate_data()
* save_data()

Use meaningful variable names.

Add comments explaining important business logic.

Avoid unnecessary loops where vectorized Pandas/NumPy operations are more appropriate.

The script should be executable using:

`python src/generate_data.py`

---

# Expected Output Format

Return the complete Python implementation for:

`src/generate_data.py`

Then provide a short explanation containing:

1. Dataset generation approach
2. Relationships between tables
3. How realism was introduced
4. How reproducibility was achieved
5. How validation was implemented

Do not generate the CSV files directly in the response.

Generate the Python script that creates them.
