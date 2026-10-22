# generator.py

## Purpose

# This module is responsible for generating product data.

# It acts as the data source of the application. In a real e-commerce system, this data could come from:

# * MySQL
# * PostgreSQL
# * Magento REST API
# * GraphQL API
# * CSV files
# * Elasticsearch/OpenSearch

# For this project, we'll generate products dynamically.

# ---

# # Responsibilities

# This module should:

# * Generate products one at a time.
# * Never create a large list.
# * Return products using `yield`.
# * Simulate a large product catalog.

# ---

# Implementation

# ```python
import random

CATEGORIES = [
    "Electronics",
    "Fashion",
    "Books",
    "Home",
    "Sports"
]


def generate_products(total_products):

    for product_id in range(1, total_products + 1):

        product = {
            "id": product_id,
            "name": f"Product-{product_id:05}",
            "category": random.choice(CATEGORIES),
            "price": round(random.uniform(100, 5000), 2),
            "stock": random.randint(0, 100)
        }

        yield product
# ```

# ---

# Code Walkthrough

## Categories

# ```python
# CATEGORIES = [...]
# ```

# A simple list of categories used to assign random categories to products.

# ---

# ## Product IDs

# ```python
# for product_id in range(1, total_products + 1):
# ```

# Products are generated one by one.

# No list is created.

# ---

# ## Product Dictionary

# Each product contains:

# ```python
# {
#     "id": 1,
#     "name": "Product-00001",
#     "category": "Electronics",
#     "price": 1299.99,
#     "stock": 52
# }
# ```

# This closely resembles the type of structured data you'll work with in Magento, APIs, and AI pipelines.

# ---

# ## `yield`

# ```python
# yield product
# ```

# This returns one product and pauses execution until the next product is requested.

# ---

# # Example Usage

# ```python
# from generator import generate_products

# products = generate_products(5)

# for product in products:
#     print(product)
# ```

# Example output:

# ```text
# {
#  'id': 1,
#  'name': 'Product-00001',
#  'category': 'Books',
#  'price': 1450.75,
#  'stock': 63
# }

# {
#  'id': 2,
#  'name': 'Product-00002',
#  'category': 'Electronics',
#  'price': 899.99,
#  'stock': 14
# }
# ```

# The values will differ each time because category, price, and stock are generated randomly.

# ---

# # Best Practices

# * Keep data generation separate from filtering and exporting.
# * Return dictionaries instead of formatted strings.
# * Generate records lazily using `yield`.
# * Use descriptive field names.

# ---

# # Possible Improvements

# Later in the roadmap we could replace this simulated data with:

# * Database queries.
# * Magento REST API responses.
# * CSV readers.
# * OpenSearch results.
# * AI-generated product descriptions.

# No other part of the application would need to change because all downstream modules simply consume product dictionaries.
