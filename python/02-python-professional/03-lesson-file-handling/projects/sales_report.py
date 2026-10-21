from pathlib import Path
import csv
import json


class SalesReport:

    def __init__(self):
        self.sales = []
        self.summary = {}

        self.sales_file = Path("sales.csv")
        self.text_report = Path("report.txt")
        self.json_report = Path("report.json")

    def read_sales(self):

        if not self.sales_file.exists():
            raise FileNotFoundError(f"{self.sales_file} not found.")

        with open(self.sales_file, "r", newline="") as file:

            reader = csv.DictReader(file)

            for row in reader:

                try:
                    sale = {
                        "Product": row["Product"],
                        "Quantity": int(row["Quantity"]),
                        "Price": float(row["Price"])
                    }

                    self.sales.append(sale)

                except ValueError:
                    print(f"Skipping invalid row: {row}")

                except KeyError as e:
                    raise KeyError(f"Missing required column: {e}")

    def calculate_summary(self):

        if not self.sales:
            raise ValueError("No sales data available.")

        total_quantity = 0
        total_sales = 0
        highest_sale = 0
        lowest_sale = None

        highest_product = ""
        lowest_product = ""

        for sale in self.sales:

            sale_amount = sale["Quantity"] * sale["Price"]

            total_quantity += sale["Quantity"]
            total_sales += sale_amount

            if sale_amount > highest_sale:
                highest_sale = sale_amount
                highest_product = sale["Product"]

            if lowest_sale is None or sale_amount < lowest_sale:
                lowest_sale = sale_amount
                lowest_product = sale["Product"]

        sales_count = len(self.sales)

        total_sales = round(total_sales, 2)
        average_sale = round(total_sales / sales_count, 2)

        self.summary = {
            "total_products": sales_count,
            "total_quantity": total_quantity,
            "total_sales": total_sales,
            "highest_sale": {
                "Product": highest_product,
                "Amount": highest_sale
            },
            "lowest_sale": {
                "Product": lowest_product,
                "Amount": lowest_sale
            },
            "average_sale": average_sale
        }

    def display_report(self):

        print("\n========== SALES REPORT ==========\n")

        print(f"Total Products : {self.summary['total_products']}")
        print(f"Total Quantity : {self.summary['total_quantity']}")
        print(f"Total Sales    : {self.summary['total_sales']}")

        print(
            f"Highest Sale   : "
            f"{self.summary['highest_sale']['Product']} "
            f"(${self.summary['highest_sale']['Amount']})"
        )

        print(
            f"Lowest Sale    : "
            f"{self.summary['lowest_sale']['Product']} "
            f"(${self.summary['lowest_sale']['Amount']})"
        )

        print(f"Average Sale   : {self.summary['average_sale']}")

        print("\n==================================")

    def save_text_report(self):

        report = f"""========== SALES REPORT ==========

Total Products : {self.summary['total_products']}
Total Quantity : {self.summary['total_quantity']}
Total Sales    : {self.summary['total_sales']}
Highest Sale   : {self.summary['highest_sale']['Product']} (${self.summary['highest_sale']['Amount']})
Lowest Sale    : {self.summary['lowest_sale']['Product']} (${self.summary['lowest_sale']['Amount']})
Average Sale   : {self.summary['average_sale']}

==================================
"""

        with open(self.text_report, "w") as file:
            file.write(report)

        print(f"Text report saved successfully: {self.text_report}")

    def save_json_report(self):

        with open(self.json_report, "w") as file:
            json.dump(self.summary, file, indent=4)

        print(f"JSON report saved successfully: {self.json_report}")


def main():

    try:

        report = SalesReport()

        report.read_sales()

        report.calculate_summary()

        report.display_report()

        report.save_text_report()

        report.save_json_report()

    except FileNotFoundError as e:
        print(f"Error: {e}")

    except KeyError as e:
        print(f"Error: {e}")

    except ValueError as e:
        print(f"Error: {e}")

    except Exception as e:
        print(f"Unexpected Error: {e}")


if __name__ == "__main__":
    main()