# # main.py

# ## Purpose

# `main.py` is the entry point of the application.

# Its responsibility is **not** to generate, filter, or export products directly. Instead, it coordinates the workflow by calling the appropriate modules in sequence.

# This separation of concerns makes the application easier to maintain, test, and extend.

# ---

# # Responsibilities

# * Configure the application.
# * Generate products.
# * Filter products.
# * Export products.
# * Display statistics.

# ---

#Don't use decorators simply because you can. Use them where they provide meaningful value.so we use it only
# in export_products function , not in generate_products and filter_products

# # Implementation

# ```python
from src.generator import generate_products
from src.filter import filter_products
from src.exporter import export_products
from src.statistics import display_statistics
from src.config import TOTAL_PRODUCTS,EXPORT_FILE,DEFAULT_CATEGORY,MIN_PRICE,IN_STOCK_ONLY


def main():

    print("Generating Products...")
    print("Filtering Products...")
    print("Exporting Products...\n")

    # Step 1 – Generate Products
    products = generate_products(TOTAL_PRODUCTS)

    # Step 2 – Apply Filters
    filtered_products = filter_products(
        products,
        DEFAULT_CATEGORY,
        MIN_PRICE,
        IN_STOCK_ONLY
    )

    # Step 3 – Export Products
    exported_count = export_products(
        filtered_products,
        EXPORT_FILE
    )

    print()
    print("=" * 40)
    print("Export Summary")
    print("=" * 40)
    print(f"Products Generated : {TOTAL_PRODUCTS}")
    print(f"Products Exported  : {exported_count}")
    print("Export Completed Successfully")
    print("=" * 40)


    # Step 4 – Display Statistics
    display_statistics(
        TOTAL_PRODUCTS,
        exported_count
    )


if __name__ == "__main__":
    main()
# ```

# ---

# # Execution Flow

# ```text
# Start
#    │
#    ▼
# Generate 10,000 Products
#    │
#    ▼
# Filter Products
# (Category = Electronics)
# (Price >= 1000)
# (Stock > 0)
#    │
#    ▼
# Export Matching Products
#    │
#    ▼
# Display Statistics
#    │
#    ▼
# End
# ```

# ---

# # Expected Console Output

# ```text
# Generating Products...
# Filtering Products...
# Exporting Products...

# ==================================================
# Export Summary
# ==================================================
# Products Generated : 10000
# Products Exported  : 784

# Export Completed Successfully
# ==================================================
# ```

# > **Note:** The exported count will vary each time because the category, price, and stock values are generated randomly.

# ---

# # Expected Output File

# Example:

# ```text
# 7, Product-00007, Electronics, 1520.50, 35
# 15, Product-00015, Electronics, 4899.99, 12
# 28, Product-00028, Electronics, 2350.75, 6
# ```

# Each line represents one exported product.

# ---

# # Why This Design?

# Notice how `main.py` contains almost no business logic.

# Instead of:

# ```python
# Generate
# ↓

# Filter
# ↓

# Write File
# ↓

# Print
# ```

# all inside one file,

# we have:

# ```text
# main.py
#     │
#     ├── generator.py
#     ├── filter.py
#     ├── exporter.py
#     └── statistics.py
# ```

# Each module has one responsibility.

# This follows the **Single Responsibility Principle (SRP)**, one of the SOLID design principles that you'll study later.

# ---

# # Project Architecture

# ```text
#                  main.py
#                      │
#      ┌───────────────┼───────────────┐
#      │               │               │
# generator.py     filter.py     exporter.py
#                                          │
#                                          ▼
#                                   products.txt

#                      │
#                      ▼
#               statistics.py
# ```

# ---

# # Design Benefits

# * Easy to read.
# * Easy to test.
# * Easy to maintain.
# * Easy to extend.
# * Each module has one responsibility.
# * Generator pipeline is preserved throughout.

# ---

# # Future Improvements

# This project can later evolve into:

# * CSV export using Python's `csv` module.
# * Excel export using `openpyxl`.
# * Database-backed product generation.
# * REST API integration.
# * Magento API integration.
# * FastAPI endpoint for downloads.
# * Multi-threaded exports.
# * Logging with decorators (after Lesson 02).
# * Background task processing.

# ```
# ```
