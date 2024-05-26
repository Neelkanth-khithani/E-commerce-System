from product import Product
from customer import Customer
from order import Order
from admin import Admin

product1 = Product("P100", "Laptop", 45000, 40)
product2 = Product("P200", "Phone", 20000, 30)
product3 = Product("P700", "Smartwatch", 12000, 49)

admin = Admin("AD@8752B", "Mr. Raj M.", "password@123")
admin.update_product_stock(product2, 3)

customer1 = Customer("C3020", "Mr. Rahul Patel", "rahul1999@gmail.com")
customer2 = Customer("C4570", "Mrs. Laxmi K.", "klaxmi45@gmail.com")

customer1.add_to_cart(product2, 1)
customer1.view_cart()
order1 = Order("OD1234", customer1)
print(order1.get_order_summary())

customer2.add_to_cart(product3, 2)
customer2.view_cart()
order2 = Order("OD7834", customer2)
print(order2.get_order_summary())
