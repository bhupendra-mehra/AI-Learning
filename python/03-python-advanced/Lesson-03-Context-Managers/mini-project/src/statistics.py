# # statistics.py

# ## Purpose

# Display project statistics.

# Keeping this separate allows us to change how statistics are displayed without modifying the export or filtering logic.

# ---

# # Implementation

# ```python
def display_statistics(total_generated, total_exported):

    print("\n" + "=" * 50)

    print("Export Summary")

    print("=" * 50)

    print(f"Products Generated : {total_generated}")
    print(f"Products Exported  : {total_exported}")

    print("\nExport Completed Successfully")

    print("=" * 50)
# ```

# ---

# Why a Separate Module?

# Today it prints to the console.

# Later we could:

# * Write to a log file.
# * Save statistics to a database.
# * Send notifications.
# * Publish metrics to monitoring systems.

# No other module would need to change.
