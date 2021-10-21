class BINARY_TREE:
    """Class that contains information about product prices (product code, price of 1 product)"""

    def __init__(self, code, price):
        if not isinstance(code, int) or not isinstance(price, (int, float)):
            raise TypeError
        if not code and not price:
            raise ValueError("no data")
        if price < 0 or code < 1:
            raise ValueError("price can't be less than zero and code can't be less than one")
        self.left = None
        self.right = None
        self.code = code
        self.price = price

    def insert(self, code, price):
        """Method that inserts the product to a binary tree"""
        if self.code:
            if code == self.code:
                raise ValueError("there's already the same one")
            if code < self.code:
                if self.left is None:
                    self.left = BINARY_TREE(code, price)
                else:
                    self.left.insert(code, price)
            elif code > self.code:
                if self.right is None:
                    self.right = BINARY_TREE(code, price)
                else:
                    self.right.insert(code, price)
        else:
            self.code = code

    def search(self, code):
        """Method that search of the product in a binary tree"""
        if code < self.code:
            if self.left is None:
                print("not found")
            return self.left.search(code)
        elif code > self.code:
            if self.right is None:
                print("not found")
            return self.right.search(code)
        else:
            return self.price

    def cost(self, code, quantity):
        """Method that calculates total cost of the product in a certain amount"""
        if not isinstance(code and quantity, int):
            raise TypeError
        if not code and not quantity:
            raise ValueError("no data")
        if quantity < 0 or code < 1:
            raise ValueError("quantity can't be less than zero and code can't be less than one")
        cost = quantity * self.search(code)
        return cost


products1 = BINARY_TREE(1, 15.99)
products1.insert(2, 9)
products1.insert(3, 4.99)
products1.insert(4, 4.49)
products1.insert(5, 10)
print("enter code of the product and needed quantity(with a comma in between):", end=' ')
try:
    code1, quantity1 = map(int, input().split(','))
    print("cost of product", code1, "in quantity of", quantity1, "=",
          "{:,.2f}".format(products1.cost(code1, quantity1)))
except:
    print("error. invalid data")
