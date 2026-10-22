from dataclasses import dataclass,field


@dataclass
class Product:
    name : str
    price :float
    category : str
    quantity : int = 1
    tags: list[str] = field(default_factory = list)

    def __post_init__(self):
        self.name = self.name.strip()
        self.category = self.category.strip()

    
    def total_price(self):
        return self.price * self.quantity


product = Product(
    name="  Laptop  ",
    price=60000.0,
    category="  Electronics  ",
    quantity=2
)

print(product)
print(product.total_price())

    