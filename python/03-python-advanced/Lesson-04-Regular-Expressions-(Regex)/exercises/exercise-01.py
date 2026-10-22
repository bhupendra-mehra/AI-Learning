import re

text = """
Customer: Bhupendra Mehra
Email: bhupendra@example.com
Phone: +91-9876543210
Order: ORD12345
Amount: ₹25999
"""

# Extract customer name
customer = re.search(r"Customer:\s*(.+)", text)

# Extract email
email = re.search(r"Email:\s*([\w.-]+@[\w.-]+\.\w+)", text)

# Extract phone number
phone = re.search(r"Phone:\s*(\+\d{1,3}-\d{10})", text)

# Extract order number
order = re.search(r"Order:\s*(ORD\d+)", text)

# Extract amount
amount = re.search(r"Amount:\s*₹(\d+)", text)


if customer:
    print("Customer:", customer.group(1))

if email:
    print("Email:", email.group(1))

if phone:
    print("Phone:", phone.group(1))

if order:
    print("Order:", order.group(1))

if amount:
    print("Amount:", amount.group(1))