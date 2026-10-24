from pathlib import Path

from sqlalchemy import Float, String, create_engine, select
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column

DB_PATH = Path(__file__).parent / "employees_orm.db"
DATABASE_URL = f"sqlite:///{DB_PATH.as_posix()}"

engine = create_engine(DATABASE_URL, echo=False)


class Base(DeclarativeBase):
    """Base class for SQLAlchemy ORM models."""


class Employee(Base):
    """Employee database model."""

    __tablename__ = "employees"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    department: Mapped[str] = mapped_column(String(100), nullable=False)
    salary: Mapped[float] = mapped_column(Float, nullable=False)

    def __repr__(self):
        return (
            f"Employee(id={self.id}, name={self.name!r}, "
            f"department={self.department!r}, salary={self.salary:.2f})"
        )


def create_table():
    """Create the employees table if it doesn't exist."""
    Base.metadata.create_all(engine)


def add_employee(name, department, salary):
    """Insert a new employee."""
    try:
        with Session(engine) as session, session.begin():
            employee = Employee(
                name=name,
                department=department,
                salary=salary,
            )
            session.add(employee)
            session.flush()
            employee_id = employee.id

        print(f"Employee added successfully. ID: {employee_id}")

    except SQLAlchemyError as error:
        print(f"Database error while adding employee: {error}")


def get_employees():
    """Retrieve and display all employees."""
    try:
        with Session(engine) as session:
            statement = select(Employee).order_by(Employee.id)
            employees = session.scalars(statement).all()

            if not employees:
                print("No employees found.")
                return

            for employee in employees:
                print(employee)

    except SQLAlchemyError as error:
        print(f"Database error while retrieving employees: {error}")


def update_employee(employee_id, salary):
    """Update an employee's salary."""
    try:
        with Session(engine) as session, session.begin():
            employee = session.get(Employee, employee_id)

            if employee is None:
                print("Employee not found.")
                return

            employee.salary = salary

        print("Employee salary updated successfully.")

    except SQLAlchemyError as error:
        print(f"Database error while updating employee: {error}")


def delete_employee(employee_id):
    """Delete an employee."""
    try:
        with Session(engine) as session, session.begin():
            employee = session.get(Employee, employee_id)

            if employee is None:
                print("Employee not found.")
                return

            session.delete(employee)

        print("Employee deleted successfully.")

    except SQLAlchemyError as error:
        print(f"Database error while deleting employee: {error}")


def read_non_empty(prompt):
    """Read a required text value."""
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("This field cannot be empty.")


def read_employee_id():
    """Read a valid positive employee ID."""
    while True:
        try:
            employee_id = int(input("Employee ID: "))
            with Session(engine) as session:
                employee = session.get(Employee, employee_id)

            if employee_id > 0 and employee is not None and employee.id:
                return employee_id

            print("Invalid Employee ID.")

        except ValueError:
            print("Please enter a valid integer.")


def read_salary(prompt):
    """Read a non-negative salary."""
    while True:
        try:
            salary = float(input(prompt))

            if salary >= 0:
                return salary

            print("Salary cannot be negative.")

        except ValueError:
            print("Please enter a valid number.")


def main():
    create_table()

    while True:
        print("\n--- Employee Management (SQLAlchemy ORM) ---")
        print("1. Add employee")
        print("2. View employees")
        print("3. Update employee salary")
        print("4. Delete employee")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                name = read_non_empty("Name: ")
                department = read_non_empty("Department: ")
                salary = read_salary("Salary: ")

                add_employee(name, department, salary)

            elif choice == "2":
                get_employees()

            elif choice == "3":
                employee_id = read_employee_id()
                salary = read_salary("New salary: ")

                update_employee(employee_id, salary)

            elif choice == "4":
                employee_id = read_employee_id()
                delete_employee(employee_id)

            elif choice == "5":
                print("Exiting application.")
                break

            else:
                print("Invalid choice. Select 1-5.")

        except (KeyboardInterrupt, EOFError):
            print("\nExiting application.")
            break


if __name__ == "__main__":
    try:
        main()
    finally:
        engine.dispose()
