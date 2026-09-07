from products import Product, NonStockedProduct, LimitedProduct
from promotions import SecondHalfPrice, ThirdOneFree, PercentDiscount
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
        print(f"{i}. ", end="")
        product.show()
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
            product_number = int(product_number)

            if product_number < 1 or product_number > len(products_list):
                print("Invalid product number. Please try again.")
                continue

            selected_product = products_list[product_number - 1]

        except (ValueError, IndexError):
            print("Invalid product number. Please try again.")
            continue

        try:
            amount = int(input("What amount do you want? : "))

            if amount <= 0:
                print("Quantity must be greater than 0.")
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

    # setup initial stock of inventory
    # setup initial stock of inventory
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250),
                    NonStockedProduct("Windows License", price=125),
                    LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
                    ]

    # Create promotion catalog
    second_half_price = SecondHalfPrice("Second Half price!")
    third_one_free = ThirdOneFree("Third One Free!")
    thirty_percent = PercentDiscount("30% off!", percent=30)

    # Add promotions to products
    product_list[0].set_promotion(second_half_price)
    product_list[1].set_promotion(third_one_free)
    product_list[3].set_promotion(thirty_percent)
    best_buy = Store(product_list)

    start(best_buy)


if __name__ == "__main__":
    main()