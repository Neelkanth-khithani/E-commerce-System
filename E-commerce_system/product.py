class Product:
    def __init__(self, product_id, name_of_product, price_of_product, stock):
        self.product_id = product_id
        self._name_of_product = name_of_product
        self._price_of_product = price_of_product
        self._stock = stock

    def get_product_info(self):
        return {
            "Product Name": self._name_of_product,
            "Price": self._price_of_product
        }

    def update_stock(self, units):
        if self._stock + units >= 0:
            self._stock += units
            return True
        return False

    def update_price(self, new_price_of_product):
        if new_price_of_product > 0:
            self._price_of_product = new_price_of_product
            return True
        return False
