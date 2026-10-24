from app.database import SessionLocal
from app.models.customer import Customer

session = SessionLocal()

customer = Customer(
    name = "Bhupendra",
    email = "bhupendra.mehra@coforge.com"
)

session.add(customer)

session.commit()

print(f"Customer created with ID: {customer.id}")

session.close()