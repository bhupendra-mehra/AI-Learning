# # exporter.py

# ## Purpose

# This module exports products to a text file.

# It doesn't know where the products came from or how they were filtered. It simply writes every product it receives.

# This separation makes the module reusable.

# ---

# # Responsibilities

# * Accept a generator of products.
# * Write each product to a file.
# * Return the number of exported products.

# ---

# # Implementation

# ```python
import os

def export_products(products, filename):

    os.makedirs(os.path.dirname(filename), exist_ok=True)

    exported_count = 0

    with open(filename, "w") as file:

        for product in products:

            file.write(
                f"{product['id']}, "
                f"{product['name']}, "
                f"{product['category']}, "
                f"{product['price']}, "
                f"{product['stock']}\n"
            )

            exported_count += 1

    return exported_count
# ```

# ---

# # Why Return the Count?

# Instead of printing:

# ```python
# Exported 125 products
# ```

# inside this module,

# we return:

# ```python
# exported_count
# ```

# Then `main.py` decides how to display it.

# This is a common design principle:

# > **Business logic should not control user interface output.**

# ---

# # Best Practices

# * Export only.
# * No filtering.
# * No data generation.
# * No printing.
# * Return useful information to the caller.
