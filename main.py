from products import Product
from store import Store


def show_menu():
    print(
        """
        Store Menu
        __________
        1. List all products in store
        2. Show total amount in store
        3. Make an order
        4. Quit
        """
    )


def show_products(store: Store):
    print("______")

    for i, product in enumerate(store.get_all_products(), start=1):
        print(
            f"{i}. {product.name}, "
            f"Price: {product.price}, "
            f"Quantity: {product.quantity}"
        )

    print("______")


def show_total_quantity(store: Store):
    print(f"Total of {store.get_total_quantity()} items in store")


def make_order(store: Store):
    products_list = store.get_all_products()
    shopping_list = []

    show_products(store)

    print("When you want to finish order, enter empty text.")

    while True:
        product_number = input("Which product # do you want? : ")

        if product_number == "":
            break

        try:
            selected_product = products_list[int(product_number) - 1]
        except (ValueError, IndexError):
            print("Invalid product number. Please try again.")
            continue

        try:
            amount = int(input("What amount do you want? : "))

            if amount <= 0:
                print("Quantity must be greater than 0.")
                continue

            if amount > selected_product.get_quantity():
                print("Not enough stock available.")
                continue

        except ValueError:
            print("Please enter a valid number.")
            continue

        shopping_list.append((selected_product, amount))
        print("Product added to list!")

    try:
        total_price = store.order(shopping_list)

        print("********")
        print(f"Order mode! Total payment: ${total_price}")

    except ValueError as error:
        print(f"Order failed: {error}")

def start(store: Store):
    while True:
        show_menu()

        choice = input("Please choose a number: ")

        if choice == "1":
            show_products(store)

        elif choice == "2":
            show_total_quantity(store)

        elif choice == "3":
            make_order(store)

        elif choice == "4":
            break


def main():
    """The main command-line interface."""

    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = Store(product_list)

    start(best_buy)


if __name__ == "__main__":
    main()