import products
import store


def start(best_buy):
    while True:
        print("""
   Store Menu
   ----------
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
""")
        choice = input("Please choose a number: ").strip()

        if choice == "1":
            print("------")
            all_products = best_buy.get_all_products()
            for i, product in enumerate(all_products, 1):
                print(f"{i}. ", end="")
                product.show()
            print("------")

        elif choice == "2":
            print("------")
            print(f"Total of {best_buy.get_total_quantity()} items in store.")
            print("------")

        elif choice == "3":
            all_products = best_buy.get_all_products()
            print("------")
            for i, product in enumerate(all_products, 1):
                print(f"{i}. ", end="")
                product.show()
            print("------")

            shopping_list = []
            print("When you want to finish order, enter empty text.")

            ordering = True
            while ordering:
                product_input = input("Which product # do you want? ").strip()
                if product_input == "":
                    ordering = False
                    continue

                quantity_input = input("What amount do you want? ").strip()
                if quantity_input == "":
                    ordering = False
                    continue

                try:
                    product_num = int(product_input)
                    quantity = int(quantity_input)

                    if product_num < 1 or product_num > len(all_products):
                        print("Error: invalid product number.")
                    elif quantity < 1:
                        print("Error: quantity must be at least 1.")
                    else:
                        shopping_list.append((all_products[product_num - 1], quantity))
                        print("Product added to list!")

                except ValueError:
                    print("Error: please enter valid numbers.")

            if shopping_list:
                try:
                    total = best_buy.order(shopping_list)
                    print("********")
                    print(f"Order made! Total payment: ${total}")
                    print("********")
                except Exception as e:
                    print(f"Error while making order: {e}")
            else:
                print("No products were added to the order.")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


def main():
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]
    best_buy = store.Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()
