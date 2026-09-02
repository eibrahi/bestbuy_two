from products import Product
from store import Store

# Setup initial stock of inventory
product_list = \
    [
    Product("MacBook Air M2", price=1450, quantity=100),
    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    Product("Google Pixel 7", price=500, quantity=250),
    ]

# Create store with initial products
best_buy = Store(product_list)

def start(store:Store):
    """Start the store command-line interface."""
    while True:
        print(
            '''
            Store Menue
            ___________
            1. List all products in store
            2. Show total amount in store
            3. Make an order
            4. Quit'''
        )

        choice = input("Please choose a number: ")
        if choice == "1":
            # Display all active products
            print("______")
            for i, product in enumerate(store.get_all_products(), start=1):
                print(f"{i}. {product.name}, Price: {product.price}, Quantity: {product.quantity}")
            print("______")

        elif choice == "2":
            # Display total inventory quantity
            print(f"Total of {store.get_total_quantity()} items in store")

        elif choice == "3":
            # Create a new shopping list
            products_list = store.get_all_products()
            shopping_list = []

            print("______")
            for i, product in enumerate(products_list, start=1):
                print(f"{i}. {product.name}, Price: {product.price}, Quantity: {product.quantity}")
            print("______")
            print("When you want to finish order, enter empty text.")

            while True:
                product_number = input("Which product # do you want? : ")

                if product_number == "":
                    break
                amount = int(input("What amount do you want? : "))

                selected_product = products_list[int(product_number) - 1]

                # Add selected product and quantity to the order
                shopping_list.append((selected_product, amount))

                print("Product added to list!")

            total_price = store.order(shopping_list)

            print("********")
            print(f"Order mode! Total pyment: ${total_price}")


        elif choice == "4":
            break

"""Start the store command-line interface."""
start(best_buy)
