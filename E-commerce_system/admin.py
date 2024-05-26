class Admin:
    def __init__(self, admin_id, admin_name, admin_password):
        self.__admin_id = admin_id
        self.__admin_name = admin_name
        self.__admin_password = admin_password

    def update_product_price(self, product, new_price):
        return product.update_price(new_price)

    def update_product_stock(self, product, unit):
        return product.update_stock(unit)
