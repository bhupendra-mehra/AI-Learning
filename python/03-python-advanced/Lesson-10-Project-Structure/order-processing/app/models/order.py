from dataclasses import dataclass,field
from datetime import datetime
from zoneinfo import ZoneInfo


@dataclass
class Order:

    order_id : str
    customer : str
    amount : float
    category : str
    quantity : int = 1
    status : str = "pending"
    tags : list[str] = field(default_factory = list)
    created_at : datetime  = field(
        default_factory=lambda: datetime.now(
            ZoneInfo("Asia/Kolkata")
        )
    )

    def __post_init__(self) -> None:
        self.customer = self.customer.strip()
        self. category = self.category.strip()

    def total_price(self) -> float:
        return self.amount * self.quantity   

    def total_with_tax(self , tax : float) -> float:
        return self.amount + tax


