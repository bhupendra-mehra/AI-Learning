# Lesson 10 – Module 3

## Dictionaries

**Estimated Time:** 35–40 minutes

---

# 1. What is a Dictionary?

A **Dictionary** stores data in **Key : Value** pairs.

Instead of storing only values like a list:

```python
products = ["Laptop", 50000]
```

Store meaningful information:

```python
product = {
    "name": "Laptop",
    "price": 50000
}
```

---

# 2. Dictionary Properties

* ✅ Key-Value pairs
* ✅ Mutable (Can be updated)
* ✅ Keys must be unique
* ✅ Values can be duplicated

---

# 3. Creating a Dictionary

```python
employee = {
    "name": "Bhupendra",
    "age": 37,
    "city": "Mumbai"
}
```

---

# 4. Accessing Values

```python
print(employee["name"])

print(employee["age"])
```

Output

```text
Bhupendra

37
```

---

# 5. Updating Values

```python
employee["city"] = "Pune"
```

Result

```python
{
    "name":"Bhupendra",
    "age":37,
    "city":"Pune"
}
```

---

# 6. Adding New Key

```python
employee["salary"] = 85000
```

Result

```python
{
    "name":"Bhupendra",
    "age":37,
    "city":"Mumbai",
    "salary":85000
}
```

---

# 7. Removing Values

```python
employee.pop("city")
```

Result

```python
{
    "name":"Bhupendra",
    "age":37
}
```

---

# 8. Loop Through Dictionary

### Keys

```python
for key in employee:
    print(key)
```

Output

```text
name

age

city
```

---

### Values

```python
for value in employee.values():
    print(value)
```

Output

```text
Bhupendra

37

Mumbai
```

---

### Key & Value Together

```python
for key, value in employee.items():
    print(key, value)
```

Output

```text
name Bhupendra

age 37

city Mumbai
```

This is the most commonly used approach.

---

# 9. Common Methods

| Method     | Purpose             |
| ---------- | ------------------- |
| `keys()`   | Get all keys        |
| `values()` | Get all values      |
| `items()`  | Get key-value pairs |
| `pop()`    | Remove a key        |
| `get()`    | Read value safely   |

---

# 10. `get()` vs `[]`

Suppose:

```python
employee = {
    "name": "Bhupendra"
}
```

Using:

```python
print(employee["salary"])
```

Result

```text
KeyError
```

Using:

```python
print(employee.get("salary"))
```

Result

```text
None
```

### Best Practice

When you're not sure a key exists, use:

```python
employee.get("salary")
```

This avoids runtime errors.

---

# Nested Dictionary

```python
employee = {
    "name": "Bhupendra",
    "address": {
        "city": "Mumbai",
        "country": "India"
    }
}
```

Access:

```python
print(employee["address"]["city"])
```

Output

```text
Mumbai
```

---

# AI Example

LLM Response

```python
response = {
    "model": "gpt-5.5",
    "tokens": 250,
    "answer": "Hello!"
}
```

Access:

```python
print(response["answer"])
```

---

# Magento Example

Product

```python
product = {
    "sku": "ABC123",
    "name": "Laptop",
    "price": 50000,
    "status": "Enabled"
}
```

Access

```python
print(product["sku"])
```

Exactly like Magento REST API responses.

---

# Best Practices

✅ Use meaningful keys

Good

```python
"name"

"price"

"quantity"
```

Bad

```python
"a"

"x"

"abc"
```

---

Use

```python
get()
```

when the key might not exist.

---

# Exercises

## Exercise 1

Create a dictionary:

```python
student = {
    "name": "Bhupendra",
    "age": 37,
    "city": "Mumbai"
}
```

Print:

* Name
* City

---

## Exercise 2

Update:

```text
city → Pune
```

Add:

```text
profession → Magento Developer
```

Print the dictionary.

---

## Exercise 3

Remove:

```text
age
```

Print the updated dictionary.

---

## Exercise 4

Loop through the dictionary using:

```python
items()
```

Print:

```text
name : Bhupendra
city : Pune
profession : Magento Developer
```

---

## Exercise 5

Create:

```python
product = {
    "sku": "ABC123",
    "name": "Laptop",
    "price": 50000
}
```

Print:

```python
product.get("price")
```

Then try:

```python
product.get("qty")
```

Observe the output.

---

# Mini Project

## Employee Information System

Requirements

Create a dictionary:

```python
employee = {
    "id":101,
    "name":"Bhupendra",
    "department":"IT",
    "salary":85000
}
```

Display all employee information using:

```python
for key, value in employee.items():
```

---

# Where You'll Use This in AI Agent Development

This is probably the **most frequently used collection** in AI.

You'll use dictionaries for:

* JSON responses
* OpenAI API responses
* Magento REST/GraphQL responses
* Tool outputs
* Agent memory
* Configuration
* Function parameters (`**kwargs`)

If you become comfortable with dictionaries, you'll find working with APIs and AI SDKs much easier.

---

## Module Outcome

After this module, you'll be able to:

* ✅ Create dictionaries.
* ✅ Read, update, and remove values.
* ✅ Loop through key-value pairs.
* ✅ Use `get()` safely.
* ✅ Understand JSON structures returned by APIs.

---

⏱️ **Estimated completion time:** **30–40 minutes**

Once you complete these exercises, we'll finish Lesson 10 with the **Inventory Management System** project, which combines **lists, dictionaries, loops, and functions** into one practical application.
