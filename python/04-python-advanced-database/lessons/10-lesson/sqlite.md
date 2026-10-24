# Lesson 11 — Part 1: SQLite with Python

Goal: Learn how to connect Python to SQLite, create tables, perform CRUD operations, and inspect database records.

We'll use a small Employee Management example. This will be a standalone practice project, so your existing e-commerce application and its MySQL database remain untouched.

## 1. What is SQLite?

SQLite is a lightweight relational database that stores data in a local file instead of requiring a separate database server.

employees.db

A database file stored on your computer

Python's built-in `sqlite3` module

Employee table

ID · Name · Department · Salary

Unlike MySQL or PostgreSQL, SQLite normally doesn't require you to install or run a separate database server. Python includes the `sqlite3` module, so you can start practicing without installing an additional database driver.

## 2. SQLite vs MySQL vs PostgreSQL

| Feature         | SQLite                        | MySQL                    | PostgreSQL                            |
| --------------- | ----------------------------- | ------------------------ | ------------------------------------- |
| Architecture    | Embedded                      | Client-server            | Client-server                         |
| Storage         | Local database file           | Database server storage  | Database server storage               |
| Separate server | Not required                  | Required                 | Required                              |
| Best suited for | Local apps, prototypes, tests | Web applications         | Complex applications and advanced SQL |
| Python access   | `sqlite3`                     | `mysql-connector-python` | `psycopg` or SQLAlchemy               |

The key idea: SQL concepts transfer between these databases, but connection setup, SQL dialect details, and concurrency behavior can differ.

## 3. Create the practice project

We'll use your existing `.venv` but create a separate folder.

From your terminal:

```
cd /var/www/html/advanced-python-database/ecommerce-db

mkdir -p lessons/lesson11/sqlite
cd lessons/lesson11/sqlite
```

Create the Python file:

```
nano employee_management.py
```

## 4. Complete Python code — Employee Management

Paste this entire code into `employee_management.py`.

```
    with get_connection() as connection:        cursor = connection.execute(            "DELETE FROM employees WHERE id = ?",            (employee_id,),        )        if cursor.rowcount:            print("Employee deleted.")        else:            print("Employee not found.")def main():    create_table()    while True:        print("\n--- Employee Management ---")        print("1. Add employee")        print("2. View employees")        print("3. Update employee salary")        print("4. Delete employee")        print("5. Exit")        choice = input("Choose an option: ").strip()        try:            if choice == "1":                name = input("Name: ").strip()                department = input("Department: ").strip()                salary = float(input("Salary: "))                if not name or not department or salary < 0:                    print("Enter valid employee details.")                    continue                add_employee(name, department, salary)            elif choice == "2":                get_employees()            elif choice == "3":                employee_id = int(input("Employee ID: "))                salary = float(input("New salary: "))                if salary < 0:                    print("Salary cannot be negative.")                    continue                update_employee(employee_id, salary)            elif choice == "4":                employee_id = int(input("Employee ID: "))                delete_employee(employee_id)            elif choice == "5":                print("Exiting application.")                break            else:                print("Invalid choice. Select 1-5.")        except ValueError:            print("Invalid input. Enter a valid number.")        except sqlite3.IntegrityError as error:            print(f"Database constraint error: {error}")if __name__ == "__main__":    main()
```

Save in Nano using `Ctrl+O`, press `Enter`, and exit with `Ctrl+X`.

## 5. Run the application

You are already using a virtual environment in your e-commerce project. Activate it if needed:

```
source /var/www/html/advanced-python-database/ecommerce-db/.venv/bin/activate
```

Run the script from the SQLite practice directory:

```
python employee_management.py
```

You'll see this menu:

```
--- Employee Management ---
1. Add employee
2. View employees
3. Update employee salary
4. Delete employee
5. Exit
Choose an option:
```

Try these operations in order:

1. Choose `1` and add `Rahul`, `IT`, `50000`.
2. Choose `1` again and add `Priya`, `HR`, `45000`.
3. Choose `2` to view both employees.
4. Choose `3`, enter employee ID `1`, and set salary to `55000`.
5. Choose `2` again to verify the change.
6. Choose `4` and delete employee ID `2`.
7. Choose `2` to verify that only Rahul remains.

Your database file will be created automatically at:

```
lessons/lesson11/sqlite/employees.db
```

## 6. Understand the important code

| Code                                  | Meaning                                                                                   |
| ------------------------------------- | ----------------------------------------------------------------------------------------- |
| `sqlite3.connect(DB_PATH)`            | Opens or creates the database file                                                        |
| `CREATE TABLE IF NOT EXISTS`          | Creates the table only if it doesn't exist                                                |
| `INSERT INTO`                         | Adds a record                                                                             |
| `SELECT`                              | Reads records                                                                             |
| `UPDATE`                              | Modifies existing records                                                                 |
| `DELETE`                              | Removes records                                                                           |
| `?` placeholders                      | Safely bind values to SQL statements                                                      |
| `with get_connection() as connection` | Commits successful changes and rolls back on exceptions when the connection context exits |

One important detail: the connection context manager does not close the connection automatically. For this short practice script, we should improve `get_connection()` or use a dedicated connection context that also closes the connection in a production-quality implementation. We'll keep that improvement in mind before treating this as production code.

## 7. Your practical exercise

After the application works, complete these tasks:

Exercise checklist

0/5

Add an employee named Amit in the Finance department with a salary of 60000.

Display all employees and verify their IDs.

Update Amit's salary to 65000.

Try updating an employee ID that does not exist.

Exit and rerun the application; confirm that the records persist.

When you're done, tell me whether the application runs successfully or share any error. Then we'll continue with Lesson 11 — Part 2: PostgreSQL with Python, where we'll connect to a real database server and repeat the CRUD workflow.