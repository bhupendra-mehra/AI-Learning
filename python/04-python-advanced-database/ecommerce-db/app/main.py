
from app.exceptions.application import ApplicationError
from app.services.order_service import create_order
from app.services.product_service import (
    create_product,
    delete_product,
    get_product,
    get_products,
    update_product_price,
)


def main():

    options = [
        "1. Create Product",
        "2. Update Product",
        "3. Get Product",
        "4. Get Products List",
        "5. Delete Product",
        "6. Create Order",
        "7. Exit",
    ]

    while True:

        print("\n===== E-Commerce Management System =====")

        for option in options:
            print(option)

        try:

            selected_option = int(input("\nSelect an option: "))

            # Create Product
            if selected_option == 1:

                category_id = int(input("Enter Category Id: "))

                sku = input("Enter SKU: ")

                name = input("Enter product name: ")

                price = float(input("Enter product price: "))

                quantity = int(input("Enter Quantity: "))

                is_created = create_product(category_id, sku, name, price, quantity)

                if is_created:
                    print("Product successfully created.")
                else:
                    print("Product creation failed.")

            # Update Product
            elif selected_option == 2:

                product_id = int(input("Enter Product Id: "))

                price = float(input("Enter product price: "))

                is_updated = update_product_price(product_id, price)

                if is_updated:
                    print("Product updated successfully.")
                else:
                    print("Product was not updated.")

            # Get Product
            elif selected_option == 3:

                product_id = int(input("Enter Product Id: "))

                product = get_product(product_id)

                if product is None:

                    print("Product not found.")

                else:

                    print(
                        f"\nProduct ID: {product.id}\n"
                        f"Name: {product.name}\n"
                        f"Price: {product.price}\n"
                        f"Quantity: {product.stock_quantity}"
                    )

            # Get Products
            elif selected_option == 4:

                products = get_products()

                if not products:

                    print("No products found.")

                else:

                    for product in products:

                        print(
                            f"ID: {product.id}, "
                            f"Name: {product.name}, "
                            f"Price: {product.price}, "
                            f"Stock: {product.stock_quantity}"
                        )

            # Delete Product
            elif selected_option == 5:

                product_id = int(input("Enter Product Id: "))

                is_deleted = delete_product(product_id)

                if is_deleted:

                    print("Product deleted successfully.")

                else:

                    print("Product deletion failed.")

            # Create Order
            elif selected_option == 6:

                customer_id = int(input("Enter Customer Id: "))

                product_id = int(input("Enter Product Id: "))

                quantity = int(input("Enter Purchase Quantity: "))

                try:

                    order_id = create_order(customer_id, product_id, quantity)

                    print(f"Order created successfully. " f"Order ID: {order_id}")

                except ApplicationError as e:

                    print(
                        f"Order could not be created: "
                        f"{e.message} "
                        f"(Code: {e.code})"
                    )

            # Exit
            elif selected_option == 7:

                print("Program terminated.")

                break

            else:

                print("Please select a valid option.")

        except ValueError:

            print("Please enter a valid number.")

        except KeyboardInterrupt:

            print("\nProgram terminated.")

            break


if __name__ == "__main__":
    main()
