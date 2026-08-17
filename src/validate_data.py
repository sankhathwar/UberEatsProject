import pandas as pd
import numpy as np


DATA_PATH = "data/raw"


def load_data():

    customers = pd.read_csv(
        f"{DATA_PATH}/customers.csv"
    )

    restaurants = pd.read_csv(
        f"{DATA_PATH}/restaurants.csv"
    )

    drivers = pd.read_csv(
        f"{DATA_PATH}/drivers.csv"
    )

    orders = pd.read_csv(
        f"{DATA_PATH}/orders.csv",
        parse_dates=["order_timestamp"]
    )

    deliveries = pd.read_csv(
        f"{DATA_PATH}/deliveries.csv"
    )

    reviews = pd.read_csv(
        f"{DATA_PATH}/reviews.csv",
        parse_dates=["review_timestamp"]
    )

    payments = pd.read_csv(
        f"{DATA_PATH}/payments.csv"
    )

    return (
        customers,
        restaurants,
        drivers,
        orders,
        deliveries,
        reviews,
        payments
    )


def check_basic_quality(
    customers,
    restaurants,
    drivers,
    orders,
    deliveries,
    reviews,
    payments
):

    print("\n" + "=" * 60)
    print("BASIC DATA QUALITY")
    print("=" * 60)

    datasets = {
        "customers": customers,
        "restaurants": restaurants,
        "drivers": drivers,
        "orders": orders,
        "deliveries": deliveries,
        "reviews": reviews,
        "payments": payments
    }

    for name, df in datasets.items():

        print(f"\n{name}")

        print("Shape:", df.shape)

        print(
            "Missing:",
            df.isna().sum().sum()
        )

        print(
            "Duplicate rows:",
            df.duplicated().sum()
        )


def check_order_distribution(orders):

    print("\n" + "=" * 60)
    print("ORDER DISTRIBUTION")
    print("=" * 60)

    orders["hour"] = (
        orders["order_timestamp"]
        .dt.hour
    )

    orders["day_of_week"] = (
        orders["order_timestamp"]
        .dt.day_name()
    )

    print("\nOrders by hour:")

    print(
        orders["hour"]
        .value_counts()
        .sort_index()
    )

    print("\nOrders by day:")

    print(
        orders["day_of_week"]
        .value_counts()
    )

    print("\nOrder status:")

    print(
        orders["order_status"]
        .value_counts(
            normalize=True
        )
        .round(3)
    )


def check_delivery_relationships(
    orders,
    deliveries
):

    print("\n" + "=" * 60)
    print("DELIVERY RELATIONSHIPS")
    print("=" * 60)

    delivery_data = deliveries.merge(
        orders[
            [
                "order_id",
                "order_timestamp"
            ]
        ],
        on="order_id",
        how="left"
    )

    delivery_data["hour"] = (
        pd.to_datetime(
            delivery_data["order_timestamp"]
        ).dt.hour
    )

    print("\nDelivery time by traffic:")

    print(
        delivery_data
        .groupby("traffic_condition")
        ["delivery_time_min"]
        .mean()
        .round(2)
    )

    print("\nDelivery time by weather:")

    print(
        delivery_data
        .groupby("weather")
        ["delivery_time_min"]
        .mean()
        .round(2)
    )

    print("\nDelivery time by traffic and weather:")

    print(
        delivery_data
        .groupby(
            [
                "traffic_condition",
                "weather"
            ]
        )["delivery_time_min"]
        .mean()
        .round(2)
    )

    print("\nCorrelation with delivery distance:")

    print(
        delivery_data[
            [
                "delivery_distance_km",
                "preparation_time_min",
                "delivery_time_min"
            ]
        ].corr()["delivery_time_min"]
        .round(3)
    )


def check_reviews(
    reviews,
    deliveries
):

    print("\n" + "=" * 60)
    print("REVIEW ANALYSIS")
    print("=" * 60)

    print("\nReview rating distribution:")

    print(
        reviews["review_rating"]
        .value_counts()
        .sort_index()
    )

    print("\nReview rating percentages:")

    print(
        reviews["review_rating"]
        .value_counts(
            normalize=True
        )
        .sort_index()
        .round(3)
    )


def check_payments(payments):

    print("\n" + "=" * 60)
    print("PAYMENT ANALYSIS")
    print("=" * 60)

    print("\nPayment methods:")

    print(
        payments["payment_method"]
        .value_counts(
            normalize=True
        )
        .round(3)
    )

    print("\nPayment status:")

    print(
        payments["payment_status"]
        .value_counts(
            normalize=True
        )
        .round(3)
    )


def main():

    (
        customers,
        restaurants,
        drivers,
        orders,
        deliveries,
        reviews,
        payments
    ) = load_data()

    check_basic_quality(
        customers,
        restaurants,
        drivers,
        orders,
        deliveries,
        reviews,
        payments
    )

    check_order_distribution(
        orders
    )

    check_delivery_relationships(
        orders,
        deliveries
    )

    check_reviews(
        reviews,
        deliveries
    )

    check_payments(
        payments
    )

    print("\nValidation completed.")


if __name__ == "__main__":
    main()
