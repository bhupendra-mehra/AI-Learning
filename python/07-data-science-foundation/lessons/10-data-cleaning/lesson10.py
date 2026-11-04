
from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "messy_orders.csv"

CLEAN_FILE = BASE_DIR / "clean_orders.csv"
REVIEW_FILE = BASE_DIR / "orders_requiring_review.csv"
JSON_FILE = BASE_DIR / "clean_orders.json"

REQUIRED_COLUMNS = [
    "OrderID",
    "CustomerEmail",
    "Product",
    "Category",
    "OrderDate",
    "Price",
    "Quantity",
    "Status",
]

ALLOWED_STATUSES = {"Completed", "Pending", "Cancelled", "Shipped"}


def main():
    # 1. Load and inspect the raw dataset.
    df = pd.read_csv(INPUT_FILE)

    print("=== RAW DATA ===")
    print(df)
    print("\nRaw shape:", df.shape)
    print("\nMissing values:")
    print(df.isna().sum())

    # 2. Check that required columns exist.
    missing_columns = set(REQUIRED_COLUMNS) - set(df.columns)

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {sorted(missing_columns)}"
        )

    # 3. Standardize text fields.
    text_columns = [
        "OrderID",
        "CustomerEmail",
        "Product",
        "Category",
        "Status",
    ]

    for column in text_columns:
        df[column] = df[column].astype("string").str.strip()

    df["OrderID"] = df["OrderID"].replace("", pd.NA)
    df["CustomerEmail"] = df["CustomerEmail"].str.lower()
    df["Product"] = df["Product"].str.title()
    df["Category"] = df["Category"].str.title()
    df["Status"] = df["Status"].str.title()

    # 4. Convert numeric fields safely.
    # Malformed values become missing values, not fabricated numbers.
    df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
    df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")

    # 5. Parse dates. Invalid dates become NaT.
    df["OrderDate"] = pd.to_datetime(
        df["OrderDate"],
        errors="coerce",
        format="mixed",
    )

    # 6. Remove exact duplicate rows.
    exact_duplicate_count = int(df.duplicated().sum())
    df = df.drop_duplicates().copy()

    # 7. Detect repeated order IDs.
    # This assumes OrderID uniquely identifies one order.
    duplicate_order_mask = df.duplicated(
        subset=["OrderID"],
        keep="first",
    )
    duplicate_orders = df[duplicate_order_mask].copy()
    df = df[~duplicate_order_mask].copy()

    # 8. Validate business rules.
    valid_email = df["CustomerEmail"].str.fullmatch(
        r"[^@\s]+@[^@\s]+\.[^@\s]+",
        na=False,
    )

    valid_order_id = df["OrderID"].notna()
    valid_product = df["Product"].notna() & df["Product"].ne("")
    valid_category = df["Category"].notna() & df["Category"].ne("")
    valid_date = df["OrderDate"].notna()
    valid_price = df["Price"].notna() & df["Price"].ge(0)
    valid_quantity = (
        df["Quantity"].notna()
        & df["Quantity"].gt(0)
        & df["Quantity"].mod(1).eq(0)
    )
    valid_status = df["Status"].isin(ALLOWED_STATUSES)

    # Add a reason for every rejected row.
    reasons = pd.Series("", index=df.index, dtype="string")

    checks = {
        "missing_order_id": valid_order_id,
        "invalid_email": valid_email,
        "missing_product": valid_product,
        "missing_category": valid_category,
        "invalid_date": valid_date,
        "missing_or_negative_price": valid_price,
        "invalid_quantity": valid_quantity,
        "unknown_status": valid_status,
    }

    for reason, passed in checks.items():
        failed = ~passed
        reasons.loc[failed] = reasons.loc[failed].apply(
            lambda current: (
                f"{current}; {reason}" if current else reason
            )
        )

    rejected = df[reasons.ne("")].copy()
    rejected["ReviewReason"] = reasons.loc[reasons.ne("")]

    clean_mask = reasons.eq("")
    clean = df[clean_mask].copy()

    # 9. Calculate revenue only for valid records.
    clean["Revenue"] = clean["Price"] * clean["Quantity"]

    # 10. Verify the clean dataset before exporting.
    assert clean["OrderID"].notna().all()
    assert clean["CustomerEmail"].notna().all()
    assert clean["OrderDate"].notna().all()
    assert clean["Price"].notna().all()
    assert clean["Price"].ge(0).all()
    assert clean["Quantity"].gt(0).all()
    assert clean["Quantity"].mod(1).eq(0).all()
    assert clean["Status"].isin(ALLOWED_STATUSES).all()
    assert clean["OrderID"].is_unique
    assert clean["Revenue"].notna().all()

    # 11. Export valid and rejected records separately.
    clean.to_csv(CLEAN_FILE, index=False)
    rejected.to_csv(REVIEW_FILE, index=False)

    # JSON is useful when preparing a payload for an API.
    clean.to_json(
        JSON_FILE,
        orient="records",
        date_format="iso",
        indent=2,
    )

    # 12. Report the results.
    print("\n=== CLEAN DATA ===")
    print(clean[REQUIRED_COLUMNS + ["Revenue"]])

    print("\n=== CLEANING SUMMARY ===")
    print("Rows loaded:", len(pd.read_csv(INPUT_FILE)))
    print("Exact duplicate rows found:", exact_duplicate_count)
    print("Repeated order IDs removed:", len(duplicate_orders))
    print("Valid rows:", len(clean))
    print("Rows requiring review:", len(rejected))
    print("Total valid revenue:", clean["Revenue"].sum())

    print("\n=== REJECTED ROW REASONS ===")
    if rejected.empty:
        print("No rejected rows.")
    else:
        print(rejected[["OrderID", "ReviewReason"]].to_string(index=False))

    print("\n=== SAVED FILES ===")
    print(CLEAN_FILE.name)
    print(REVIEW_FILE.name)
    print(JSON_FILE.name)


if __name__ == "__main__":
    main()
