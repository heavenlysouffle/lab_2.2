class Product:
    """Class that describes a product (contains name, price, description, dimension)"""

    def __init__(self, price, descrip, dimen):
        dimen_dictionary = {"XS", "S", "M", "L", "XL"}
        if not isinstance(price, (int, float)) or not isinstance(descrip, str):
            raise TypeError
        if not descrip or not dimen:
            raise ValueError("no data")
        if price < 0:
            raise ValueError("price cannot be less than zero")
        if dimen not in dimen_dictionary:
            raise ValueError("acceptable dimension input: XS, S, M, L, XL")
        self.price = price
        self.__description = descrip
        self.__dimension = dimen


class Customer:
    """Class that describes a customer (contains surname, name, patronymic, phone number)"""

    def __init__(self, surname, name, patronym, phone):
        if not surname or not name or not patronym or not phone:
            raise ValueError("no data")
        self.__surname = surname
        self.__name = name
        self.__patronymic = patronym
        self.__number = phone


class Order:
    """Class that contains data about the customer and products, calculates the total order value"""
    __order_number = 0

    def __init__(self, customer = None):
        if not isinstance(customer, Customer):
            raise TypeError
        self.__customer = customer
        self.__products = []
        Order.__order_number += 1

    def add(self, product):
        """Method of class Order that add the product to order"""
        if not isinstance(product, Product):
            raise TypeError
        self.__products.append(product)

    def remove(self, product):
        """Method of class Order that remove the product from order"""
        if not isinstance(product, Product):
            raise TypeError
        if not self.__products:
            raise ValueError("no data")
        self.__products.remove(product)

    def get_total(self):
        """Method of class Order that counts and returns the total price of the order"""
        total = 0
        for product in self.__products:
            total += product.price
        return f'order №{Order.__order_number}: {"{:,.2f}".format(total)}'


product1 = Product(5.99, "description1", "S")
product2 = Product(12, "description2", "XL")
customer1 = Customer("Bykova", "Polina", "Olegovna", 3452345768)
order1 = Order(customer1)
order1.add(product1)
order1.add(product2)
print(order1.get_total())
order1.remove(product2)
print(order1.get_total())
