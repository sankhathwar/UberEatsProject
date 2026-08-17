                    ┌──────────────┐
                    │  Customers   │
                    └──────┬───────┘
                           │
                           │ customer_id
                           ▼
                    ┌──────────────┐
                    │    Orders    │
                    └───┬──────┬───┘
                        │      │
             restaurant_id     │ order_id
                        │      │
                        ▼      ▼
                ┌──────────┐  ┌──────────────┐
                │Restaurant│  │  Deliveries  │
                └──────────┘  └──────┬───────┘
                                     │
                                  driver_id
                                     │
                                     ▼
                               ┌──────────┐
                               │ Drivers  │
                               └──────────┘

Orders ──────────► Reviews
Orders ──────────► Payments
