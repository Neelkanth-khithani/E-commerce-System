class Order:
    def __init__(self, order_id, customer):
        self.order_id = order_id
        self._customer_name = customer.customer_name
        self.items = customer.view_cart()
        self.customer = customer
        self.total = sum(item[0]["Price"] * item[1] for item in self.items)

    def get_order_summary(self):
        summary = {
            "Order ID": self.order_id,
            "Customer": self._customer_name,
            "Items List": self.items,
            "Total": self.total
        }

        print("\nOrder Summary:\n")
        return summary
