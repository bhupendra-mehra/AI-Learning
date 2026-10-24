
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "employees.db"


def get_connection():
    """Connect to the SQLite database."""
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def create_table():
    """Create the employees table if it doesn't exist."""
    with get_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                department TEXT NOT NULL,
                salary REAL NOT NULL CHECK (salary >= 0)
            )
        """)


def add_employee(name, department, salary):
    """Insert a new employee."""
    with get_connection() as connection:
        cursor = connection.execute(
            """
            INSERT INTO employees (name, department, salary)
            VALUES (?, ?, ?)
            """,
            (name, department, salary),
        )
        print(f"Employee added. ID: {cursor.lastrowid}")


def get_employees():
    """Retrieve all employees."""
    with get_connection() as connection:
        employees = connection.execute(
            "SELECT id, name, department, salary FROM employees ORDER BY id"
        ).fetchall()

    for employee in employees:
        print(dict(employee))


def update_employee(employee_id, salary):
    """Update an employee's salary."""
    with get_connection() as connection:
        cursor = connection.execute(
            "UPDATE employees SET salary = ? WHERE id = ?",
            (salary, employee_id),
        )

        if cursor.rowcount:
            print("Employee updated.")
        else:
            print("Employee not found.")


def delete_employee(employee_id):
    """Delete an employee by ID."""
    with get_connection() as connection:
        cursor = connection.execute(
            "DELETE FROM employees WHERE id = ?",
            (employee_id,),
        )

        if cursor.rowcount:
            print("Employee deleted.")
        else:
            print("Employee not found.")


def main():
    create_table()

    while True:
        print("\n--- Employee Management ---")
        print("1. Add employee")
        print("2. View employees")
        print("3. Update employee salary")
        print("4. Delete employee")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                name = input("Name: ").strip()
                department = input("Department: ").strip()
                salary = float(input("Salary: "))

                if not name or not department or salary < 0:
                    print("Enter valid employee details.")
                    continue

                add_employee(name, department, salary)

            elif choice == "2":
                get_employees()

            elif choice == "3":
                employee_id = int(input("Employee ID: "))
                salary = float(input("New salary: "))

                if salary < 0:
                    print("Salary cannot be negative.")
                    continue

                update_employee(employee_id, salary)

            elif choice == "4":
                employee_id = int(input("Employee ID: "))
                delete_employee(employee_id)

            elif choice == "5":
                print("Exiting application.")
                break

            else:
                print("Invalid choice. Select 1-5.")

        except ValueError:
            print("Invalid input. Enter a valid number.")

        except sqlite3.IntegrityError as error:
            print(f"Database constraint error: {error}")


if __name__ == "__main__":
    main()
