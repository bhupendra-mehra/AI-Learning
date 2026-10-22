from collections import namedtuple

User = namedtuple("User", ["name", "age", "role"])

user = User("Bhupendra", 37, "Magento Developer")

print(user.name)
print(user.age)
print(user.role)