class Product:
    """Class that describes a product (contains price, description, dimension, quantity)"""

    def __init__(self, price=0, descrip="description", dimen="dimension", quantity=0):
        dimen_dictionary = {"dimension", "XS", "S", "M", "L", "XL"}
        if not isinstance(price, (int, float)) or not isinstance(descrip, str) or not isinstance(quantity, int):
            raise TypeError
        if price < 0 or quantity < 0:
            raise ValueError
        if dimen not in dimen_dictionary:
            raise ValueError("acceptable dimension input: dimension, XS, S, M, L, XL")
        self.price = price
        self.description = descrip
        self.dimension = dimen
        self.quantity = quantity


class Customer:
    """Class that describes a customer (contains surname, name, patronymic, phone number)"""

    def __init__(self, surname="surname", name="name", patronym="patronymic", number="phone number"):
        if not isinstance(surname or name or patronym or number, str):
            raise TypeError
        self.surname = surname
        self.name = name
        self.patronymic = patronym
        self.number = number


class Order:
    """Class that contains data about the customer and products, calculates the total order value"""
    order_number = 0

    def __init__(self, customer, *products):
        if not isinstance(customer, Customer):
            raise ValueError
        self.customer = customer
        self.__total = 0
        for product in products:
            if not isinstance(product, Product):
                raise ValueError
            self.product = product
            self.__total += product.quantity * product.price
        Order.order_number += 1

    def get_total(self):
        return f'order №{Order.order_number}: {self.__total}'


product1 = Product(1.33, "description", "XL", 5)
product2 = Product(2, "description", "XS", 10)
customer = Customer()
order = Order(customer, product1, product2)
print(order.get_total())
