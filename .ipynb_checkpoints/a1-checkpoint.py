

# High-Difficulty Python Practice Questions 
# 1. Customer Filtering

# You are given:

# customers = [
#     {"name": "Ram", "age": 25, "purchase": 1500},
#     {"name": "Sita", "age": 40, "purchase": 8000},
#     {"name": "Hari", "age": 35, "purchase": 500},
#     {"name": "Gita", "age": 29, "purchase": 3000}
# ]

# Find all customers whose age is between 25 and 40 (inclusive) and whose purchase amount is greater than 1000 and print it in a list.

customers = [
    {"name": "Ram", "age": 25, "purchase": 1500},
    {"name": "Sita", "age": 40, "purchase": 8000},
    {"name": "Hari", "age": 35, "purchase": 500},
    {"name": "Gita", "age": 29, "purchase": 3000}
]

filtered_customers = [customer for customer in customers if 25 <= customer["age"] <= 40 and customer["purchase"] > 1000]
print(filtered_customers)

