class Product:
    def __init__(self, product_name, price, quantity_in_stock):
        self.product_name = product_name
        self.price = price
        self.quantity_in_stock = quantity_in_stock

    def display_product_info(self):
        print(f"Product Name: {self.product_name}")
        print(f"Price: {self.price}")
        print(f"Quantity in Stock: {self.quantity_in_stock}")


class ShoppingCart:
    total_carts = 0

    def __init__(self):
        self.items = []
        ShoppingCart.total_carts += 1

    def add_to_cart(self, product, quantity):
        if product.quantity_in_stock >= quantity:
            self.items.append((product, quantity))
            product.quantity_in_stock -= quantity
            print(f"{quantity} {product.product_name} added to cart.")
        else:
            print("Insufficient stock.")

    def remove_from_cart(self, product):
        for i, item in enumerate(self.items):
            if item[0] == product:
                self.items.pop(i)
                product.quantity_in_stock += item[1]
                print(f"{product.product_name} removed from cart.")
                break
        else:
            print("Product not found in cart.")

    def display_cart(self):
        print("Your Cart:")
        for product, quantity in self.items:
            print(f"{quantity} {product.product_name}")

    def calculate_total(self):
        total = 0
        for product, quantity in self.items:
            total += product.price * quantity
        return total


product1 = Product("blender", 10000, 5)
product2 = Product("flat iron", 25000, 10)
product3 = Product("oven", 300000, 20)

cart1 = ShoppingCart()
cart2 = ShoppingCart()


cart1.add_to_cart(product1, 2)
cart1.add_to_cart(product2, 3)
cart2.add_to_cart(product3, 5)


cart1.display_cart()
print("Total:", cart1.calculate_total())
print()
cart2.display_cart()
print("Total:", cart2.calculate_total())