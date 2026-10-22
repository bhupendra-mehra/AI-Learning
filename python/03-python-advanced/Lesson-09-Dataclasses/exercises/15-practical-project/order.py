from dataclasses import dataclass,field

@dataclass
class Order:
    order_id :str
    customer : str
    amount : float
    status : str = "pending"
    tags : list[str] = field(default_factory=list)

    def __post_init__(self):
        self.customer = self.customer.strip()

    def apply_discount(self , percentage:float) -> float:
        return self.amount - (
            self.amount*percentage/100
        )


order = Order("1111","    Bhupendra Mehra   ",100,"completed")

#add tags into order
#order.tags.append("test") 

order_amount = order.apply_discount(10)

print(order_amount)

print(order.customer)


order = Order(
    order_id="ORD1001",
    customer="  Bhupendra Mehra  ",
    amount=25000.0
)


print(order)

print("Customer:", order.customer)
print("Status:", order.status)
print("Tags:", order.tags)

print(
    "After 10% discount:",
    order.apply_discount(10)
)