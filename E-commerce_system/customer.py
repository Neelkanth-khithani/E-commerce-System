class Customer:
    def __init__(self, customer_id, customer_name, customer_email_id):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.customer_email_id = customer_email_id
        self.cart = []

    def add_to_cart(self, product, quantity):
        return self.cart.append((product, quantity))

    def view_cart(self):
        return [(item[0].get_product_info(), item[1]) for item in self.cart]
