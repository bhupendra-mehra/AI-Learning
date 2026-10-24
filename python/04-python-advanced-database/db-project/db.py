import os
import mysql.connector

from dotenv import load_dotenv

load_dotenv()


def get_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT", 3306)),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )


# connection = get_connection()

# cursor = connection.cursor()

# print("-----------Multiple Records--------------")

# cursor.execute("SELECT id,email FROM customers ORDER BY id ASC LIMIT 10")

# customers = cursor.fetchall()

# for customer in customers:
#     print(customer)

# print("-----------Single Record--------------")

# cursor.execute("SELECT id,email FROM customers WHERE id = 5 LIMIT 1")

# customer = cursor.fetchone()

# print(customer)

# print("-----------Linmited Records(Rows)--------------")

# cursor.execute("SELECT id , email from customers LIMIT 20")

# customers = cursor.fetchmany(5)

# for customer in customers:
#     print(customer)


# print("--------------Query Construction----------------")

# customer_id = 5

# query = """
# SELECT
#     id,
#     CONCAT(first_name, " ", last_name) AS name,
#     email
# FROM customers
# WHERE id > %s
# AND created_at > %s
# LIMIT 5
# """

# cursor.execute(query, (customer_id,"2026-01-01"))
# print("Executed Query:", cursor.statement)

# customers = cursor.fetchall()

# for customer in customers:
#     print(customer)

# print("------INSERT QUERY PRODUCT---------------")
# query = """
# INSERT INTO products
# (category_id, sku, name, price, stock_quantity, created_at, updated_at)
# VALUES (%s, %s, %s, %s, %s, NOW(), NOW())
# """

# values = (
#     3,
#     "USB001",
#     "USB Cable",
#     500.00,
#     100
# )

# cursor.execute(query, values)

# connection.commit()   

# print("------UPDATE QUERY PRODUCT---------------")

# query = """
# UPDATE products
# SET price = %s
# WHERE id = %s
# """

# values = (
#     65000,
#     2
# )

# cursor.execute(query, values)

# connection.commit()

# print("------DELETE QUERY PRODUCT---------------")

# query = """
# DELETE FROM products
# WHERE id = %s
# """

# cursor.execute(
#     query,
#     (2,)
# )

# connection.commit()

#print("---Python Transaction Example Pattern--------")

# try:
#     cursor.execute(order_query, order_values)

#     cursor.execute(item_query, item_values)

#     cursor.execute(stock_query, stock_values)

#     connection.commit()

# except Exception:
#     connection.rollback()
#     raise


#print("---Exception Handling--------")

connection = None
cursor = None

try:
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute(
        "SELECT id, name FROM products"
    )

    products = cursor.fetchall()

    for product in products:
        print(product["id"]," ", product["name"])

except mysql.connector.Error as error:
    print(f"Database error: {error}")

finally:
    if cursor:
        cursor.close()

    if connection:
        connection.close()




