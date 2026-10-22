import re

text = """
Customer: Bhupendra Mehra
Email: [bhupendra@example.com](mailto:bhupendra@example.com)
Phone: +91-9876543210
Order: ORD12345
Amount: ₹25999
"""

# Step 1: Extract data

customer = re.search(
    r"^Customer:\s*(.*)$",
    text,
    re.MULTILINE
).group(1)

email = re.search(
    r"^Email:\s*(.*)$",
    text,
    re.MULTILINE
).group(1)

phone = re.search(
    r"^Phone:\s*(.*)$",
    text,
    re.MULTILINE
).group(1)

order = re.search(
    r"^Order:\s*(.*)$",
    text,
    re.MULTILINE
).group(1)

amount = re.search(
    r"^Amount:\s*(.*)$",
    text,
    re.MULTILINE
).group(1)


# Step 2: Validate

# Extract actual email address from Markdown
email_match = re.search(
    r"\[([\w.+-]+@[\w.-]+)\]",
    email
)

email_address = email_match.group(1) if email_match else ""

email_valid = bool(
    re.fullmatch(
        r"[\w.+-]+@[\w.-]+\.\w+",
        email_address
    )
)

phone_valid = bool(
    re.fullmatch(
        r"\+\d{2}-\d{10}",
        phone
    )
)

order_valid = bool(
    re.fullmatch(
        r"ORD\d{5}",
        order
    )
)


# Step 3: Clean amount

amount = re.sub(r"[₹,\s]", "", amount)


# Step 4: Print

print("=" * 10, "CUSTOMER ORDER", "=" * 10)

print(f"Customer : {customer}")
print(f"Email    : {email_address}")
print(f"Phone    : {phone}")
print(f"Order    : {order}")
print(f"Amount   : {amount}")

print(f"Email    : {'Valid' if email_valid else 'Invalid'}")
print(f"Phone    : {'Valid' if phone_valid else 'Invalid'}")
print(f"Order    : {'Valid' if order_valid else 'Invalid'}")