#Practical Example with mypy
#sudo apt install mypy
#run below command
#mypy type_check.py
# type_check.py:13: error: Argument 1 to "calculate_total" has incompatible type "str"; expected "float"  [arg-type]
# Found 1 error in 1 file (checked 1 source file)
def calculate_total(
    price: float,
    quantity: int
) -> float:

    return price * quantity


total = calculate_total(
    "1000.0",
    3
)

print(total)