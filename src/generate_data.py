import os
from pathlib import Path

import numpy as np
import pandas as pd
from faker import Faker


# ============================================================
# CONFIGURATION
# ============================================================

RANDOM_SEED = 42

N_CUSTOMERS = 10_000
N_RESTAURANTS = 500
N_DRIVERS = 1_000
N_ORDERS = 100_000

START_DATE = "2025-01-01"
END_DATE = "2026-06-30"

OUTPUT_DIR = Path("data/raw")

np.random.seed(RANDOM_SEED)

fake = Faker("en_IN")
Faker.seed(RANDOM_SEED)
	
# ============================================================
# BUSINESS DIMENSIONS
# ============================================================

CITIES = [
    "Bangalore",
    "Chennai",
    "Hyderabad",
    "Mumbai",
    "Delhi",
    "Pune",
    "Kolkata",
    "Ahmedabad",
    "Jaipur",
    "Kochi",
]

CUISINES = [
    "Indian",
    "Chinese",
    "Italian",
    "Mexican",
    "Biryani",
    "South Indian",
    "North Indian",
    "Fast Food",
    "Desserts",
    "Healthy",
]

MEMBERSHIP_TYPES = [
    "Standard",
    "Gold",
    "Premium",
]

PAYMENT_METHODS = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Cash",
    "Wallet",
]

VEHICLE_TYPES = [
    "Bike",
    "Scooter",
    "Car",
]

TRAFFIC_CONDITIONS = [
    "Low",
    "Medium",
    "High",
]

WEATHER_CONDITIONS = [
    "Clear",
    "Cloudy",
    "Rainy",
    "Stormy",
]


# ============================================================
# CUSTOMER GENERATION
# ============================================================

def generate_customers(n=N_CUSTOMERS):
    customers = pd.DataFrame({
        "customer_id": [
            f"C{i:06d}" for i in range(1, n + 1)
        ],
        "age": np.random.randint(18, 71, n),
        "gender": np.random.choice(
            ["Male", "Female", "Other"],
            size=n,
            p=[0.48, 0.48, 0.04]
        ),
        "city": np.random.choice(
            CITIES,
            size=n
        ),
        "signup_date": pd.to_datetime(
            np.random.choice(
                pd.date_range(
                    START_DATE,
                    END_DATE,
                    freq="D"
                ),
                size=n
            )
        ),
        "membership_type": np.random.choice(
            MEMBERSHIP_TYPES,
            size=n,
            p=[0.60, 0.30, 0.10]
        )
    })

    return customers

# ============================================================
# RESTAURANT GENERATION
# ============================================================

def generate_restaurants(n=N_RESTAURANTS):

    restaurants = pd.DataFrame({
        "restaurant_id": [
            f"R{i:05d}" for i in range(1, n + 1)
        ],
        "restaurant_name": [
            fake.company()
            for _ in range(n)
        ],
        "city": np.random.choice(
            CITIES,
            size=n
        ),
        "cuisine": np.random.choice(
            CUISINES,
            size=n
        ),
        "restaurant_rating": np.round(
            np.clip(
                np.random.normal(4.0, 0.5, n),
                1,
                5
            ),
            2
        ),
        "avg_prep_time": np.random.randint(
            10,
            61,
            n
        ),
        "price_range": np.random.choice(
            ["Low", "Medium", "High"],
            size=n,
            p=[0.35, 0.50, 0.15]
        )
    })

    return restaurants

# ============================================================
# DRIVER GENERATION
# ============================================================

def generate_drivers(n=N_DRIVERS):

    drivers = pd.DataFrame({
        "driver_id": [
            f"D{i:05d}" for i in range(1, n + 1)
        ],
        "driver_age": np.random.randint(
            18,
            61,
            n
        ),
        "driver_rating": np.round(
            np.clip(
                np.random.normal(4.2, 0.4, n),
                1,
                5
            ),
            2
        ),
        "vehicle_type": np.random.choice(
            VEHICLE_TYPES,
            size=n,
            p=[0.50, 0.40, 0.10]
        ),
        "city": np.random.choice(
            CITIES,
            size=n
        ),
        "experience_years": np.round(
            np.random.uniform(0, 15, n),
            1
        )
    })

    return drivers

# ============================================================
# ORDER GENERATION
# ============================================================

def generate_orders(customers, restaurants, n=N_ORDERS):

    order_dates = pd.date_range(
        START_DATE,
        END_DATE,
        freq="h"
    )

    # Create hourly weights
    hours = order_dates.hour

    hour_weights = np.where(
        ((hours >= 12) & (hours <= 14)) |
        ((hours >= 19) & (hours <= 22)),
        3.0,
        np.where(
            (hours >= 1) & (hours <= 6),
            0.3,
            1.0
        )
    )

    # Weekend multiplier
    weekend_multiplier = np.where(
        order_dates.dayofweek >= 5,
        1.3,
        1.0
    )

    weights = hour_weights * weekend_multiplier
    weights = weights / weights.sum()

    selected_timestamps = np.random.choice(
        order_dates,
        size=n,
        p=weights
    )

    customer_ids = np.random.choice(
        customers["customer_id"],
        size=n
    )

    restaurant_ids = np.random.choice(
        restaurants["restaurant_id"],
        size=n
    )

    item_count = np.random.randint(
        1,
        9,
        n
    )

    order_amount = np.round(
        np.maximum(
            100,
            item_count * np.random.normal(
                180,
                40,
                n
            )
        ),
        2
    )

    orders = pd.DataFrame({
        "order_id": [
            f"O{i:06d}" for i in range(1, n + 1)
        ],
        "customer_id": customer_ids,
        "restaurant_id": restaurant_ids,
        "order_timestamp": selected_timestamps,
        "order_amount": order_amount,
        "item_count": item_count,
        "payment_method": np.random.choice(
            PAYMENT_METHODS,
            size=n,
            p=[0.45, 0.20, 0.15, 0.05, 0.15]
        ),
        "order_status": np.random.choice(
            ["Completed", "Cancelled", "Failed"],
            size=n,
            p=[0.90, 0.07, 0.03]
        )
    })

    return orders

# ============================================================
# DELIVERY GENERATION
# ============================================================

def generate_deliveries(orders, restaurants, drivers):

    completed_orders = orders[
        orders["order_status"] == "Completed"
    ].copy()

    n = len(completed_orders)

    driver_ids = np.random.choice(
        drivers["driver_id"],
        size=n
    )

    delivery_distance = np.round(
        np.random.gamma(
            shape=2.5,
            scale=2.0,
            size=n
        ),
        2
    )

    traffic = np.random.choice(
        TRAFFIC_CONDITIONS,
        size=n,
        p=[0.35, 0.45, 0.20]
    )

    weather = np.random.choice(
        WEATHER_CONDITIONS,
        size=n,
        p=[0.55, 0.25, 0.17, 0.03]
    )

    restaurant_prep_times = (
        completed_orders["restaurant_id"]
        .map(
            restaurants.set_index("restaurant_id")[
                "avg_prep_time"
            ]
        )
        .values
    )

    preparation_time = np.maximum(
        10,
        np.round(
            restaurant_prep_times +
            np.random.normal(0, 5, n)
        )
    ).astype(int)

    traffic_effect = np.select(
        [
            traffic == "Low",
            traffic == "Medium",
            traffic == "High"
        ],
        [
            0,
            10,
            25
        ]
    )

    weather_effect = np.select(
        [
            weather == "Clear",
            weather == "Cloudy",
            weather == "Rainy",
            weather == "Stormy"
        ],
        [
            0,
            3,
            10,
            20
        ]
    )

    peak_hour = (
        completed_orders["order_timestamp"]
 	    .dt.hour
        .between(12, 14)
        |
        completed_orders["order_timestamp"]
        .dt.hour
        .between(19, 22)
    )

    peak_effect = np.where(
        peak_hour,
        8,
        0
    )

    delivery_time = (
        5
        + (delivery_distance * 2.5)
        + (preparation_time * 0.5)
        + traffic_effect
        + weather_effect
        + peak_effect
        + np.random.normal(0, 5, n)
    )
    
    delivery_time = np.maximum(
        10,
        np.round(delivery_time)
    ).astype(int)

    tip_amount = np.round(
        np.maximum(
            0,
            completed_orders["order_amount"].values
            * np.random.uniform(0, 0.15, n)
        ),
        2
    )

    deliveries = pd.DataFrame({
        "delivery_id": [
            f"DL{i:06d}" for i in range(1, n + 1)
        ],
        "order_id": completed_orders["order_id"].values,
        "driver_id": driver_ids,
        "delivery_distance_km": delivery_distance,
        "preparation_time_min": preparation_time,
        "delivery_time_min": delivery_time,
        "traffic_condition": traffic,
        "weather": weather,
        "tip_amount": tip_amount,
        "delivery_status": "Completed"
    })

    return deliveries

# ============================================================
# REVIEW GENERATION
# ============================================================

def generate_reviews(orders, deliveries):

    completed_orders = orders[
        orders["order_status"] == "Completed"
    ].copy()

    review_count = int(
        len(completed_orders) * 0.60
    )

    reviewed_orders = completed_orders.sample(
        n=review_count,
        random_state=RANDOM_SEED
    )

    delivery_lookup = deliveries.set_index("order_id")

    review_rows = []

    positive_templates = [
        "The food was fresh and arrived quickly.",
        "Great experience, the food was delicious.",
        "Really happy with the delivery and service.",
        "The order arrived hot and on time.",
        "Excellent food and smooth delivery."
    ]

    neutral_templates = [
        "The food was okay, but the delivery took longer than expected.",
        "Average experience. Nothing particularly good or bad.",
        "The food was decent, but delivery could have been faster.",
        "The experience was acceptable.",
        "Food was fine, although there was some delay."
    ]

    negative_templates = [
        "The food arrived cold and the delivery was very late.",
        "Very disappointing experience.",
        "The order took far too long to arrive.",
        "The food quality was poor.",
        "The delivery was delayed and the food was not fresh."
    ]

    for _, order in reviewed_orders.iterrows():

        order_id = order["order_id"]
        delivery_time = delivery_lookup.loc[
            order_id,
            "delivery_time_min"
        ]

        if delivery_time <= 35:
            rating = np.random.choice([4, 5], p=[0.30, 0.70])
        elif delivery_time <= 50:
            rating = np.random.choice([3, 4, 5], p=[0.20, 0.50, 0.30])
        elif delivery_time <= 65:
            rating = np.random.choice([2, 3, 4], p=[0.20, 0.55, 0.25])
        else:
            rating = np.random.choice([1, 2, 3], p=[0.30, 0.50, 0.20])

        if rating >= 4:
            text = np.random.choice(
                positive_templates
            )
        elif rating == 3:
            text = np.random.choice(
                neutral_templates
            )
        else:
            text = np.random.choice(
                negative_templates
            )

        review_rows.append({
            "review_id": f"RV{len(review_rows) + 1:06d}",
            "order_id": order_id,
            "customer_id": order["customer_id"],
            "review_rating": rating,
            "review_text": text,
            "review_timestamp": (
   		 order["order_timestamp"]
    		+ pd.Timedelta(
        		minutes=np.random.randint(15, 121)
    		)
	)
        })

    return pd.DataFrame(review_rows)

# ============================================================
# PAYMENT GENERATION
# ============================================================

def generate_payments(orders, deliveries):

    payments = orders.copy()

    delivery_tip_lookup = deliveries.set_index(
        "order_id"
    )["tip_amount"]

    payments["tip_amount"] = (
        payments["order_id"]
        .map(delivery_tip_lookup)
        .fillna(0)
    )

    payments["payment_id"] = [
        f"P{i:06d}"
        for i in range(1, len(payments) + 1)
    ]

    payments["payment_status"] = np.random.choice(
        ["Success", "Failed", "Refunded"],
        size=len(payments),
        p=[0.95, 0.03, 0.02]
    )

    payments = payments[
        [
            "payment_id",
            "order_id",
            "customer_id",
            "payment_method",
            "order_amount",
            "tip_amount",
            "payment_status"
        ]
    ]

    return payments

# ============================================================
# VALIDATION
# ============================================================

def validate_data(
    customers,
    restaurants,
    drivers,
    orders,
    deliveries,
    reviews,
    payments
):

    print("\n" + "=" * 60)
    print("DATA VALIDATION REPORT")
    print("=" * 60)

    datasets = {
        "Customers": customers,
        "Restaurants": restaurants,
        "Drivers": drivers,
        "Orders": orders,
        "Deliveries": deliveries,
        "Reviews": reviews,
        "Payments": payments
    }

    for name, df in datasets.items():

        print(f"\n{name}")
        print(f"Rows: {len(df):,}")
        print(f"Columns: {len(df.columns)}")
        print(f"Missing values: {df.isna().sum().sum():,}")

    print("\nDuplicate primary keys:")

    print(
        "Customers:",
        customers["customer_id"].duplicated().sum()
    )

    print(
        "Restaurants:",
        restaurants["restaurant_id"].duplicated().sum()
    )

    print(
        "Drivers:",
        drivers["driver_id"].duplicated().sum()
    )

    print(
        "Orders:",
        orders["order_id"].duplicated().sum()
    )

    print(
        "Deliveries:",
        deliveries["delivery_id"].duplicated().sum()
    )

    print(
        "Reviews:",
        reviews["review_id"].duplicated().sum()
    )

    print(
        "Payments:",
        payments["payment_id"].duplicated().sum()
    )

    # Foreign key checks

    print("\nForeign-key validation:")

    invalid_order_customers = (
        ~orders["customer_id"].isin(
            customers["customer_id"]
        )
    ).sum()

    invalid_order_restaurants = (
        ~orders["restaurant_id"].isin(
            restaurants["restaurant_id"]
        )
    ).sum()

    invalid_delivery_orders = (
        ~deliveries["order_id"].isin(
            orders["order_id"]
        )
    ).sum()

    invalid_delivery_drivers = (
        ~deliveries["driver_id"].isin(
            drivers["driver_id"]
        )
    ).sum()

    print(
        "Invalid order → customer:",
        invalid_order_customers
    )

    print(
        "Invalid order → restaurant:",
        invalid_order_restaurants
    )

    print(
        "Invalid delivery → order:",
        invalid_delivery_orders
    )

    print(
        "Invalid delivery → driver:",
        invalid_delivery_drivers
    )

    print("\nValidation complete.")

# ============================================================
# SAVE DATA
# ============================================================

def save_data(datasets):

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    for filename, df in datasets.items():

        path = OUTPUT_DIR / filename

        df.to_csv(
            path,
            index=False
        )

        print(
            f"Saved {filename}: {len(df):,} rows"
        )

# ============================================================
# MAIN PIPELINE
# ============================================================

def main():

    print("Starting Uber Eats synthetic data generation...")

    customers = generate_customers()

    restaurants = generate_restaurants()

    drivers = generate_drivers()

    orders = generate_orders(
        customers,
        restaurants
    )

    deliveries = generate_deliveries(
        orders,
        restaurants,
        drivers
    )

    reviews = generate_reviews(
        orders,
        deliveries
    )

    payments = generate_payments(
        orders,
        deliveries
    )

    datasets = {
        "customers.csv": customers,
        "restaurants.csv": restaurants,
        "drivers.csv": drivers,
        "orders.csv": orders,
        "deliveries.csv": deliveries,
        "reviews.csv": reviews,
        "payments.csv": payments
    }

    save_data(datasets)

    validate_data(
        customers,
        restaurants,
        drivers,
        orders,
        deliveries,
        reviews,
        payments
    )

    print("\nData generation completed successfully.")


if __name__ == "__main__":
    main()


