class Product(object):
    next_id = 1
    def __init__(self, name, description, price, quantity):

        if isinstance(name, str):
            self.name = name
        else:
            raise ValueError("Must be a string!")

        if isinstance(description, str):
            self.description = description
        else:
            raise ValueError("Must be a string!")

        if isinstance(price, float) and price > 0.01:
            self.price = price
        else:
            raise ValueError('Must be a float!')

        if isinstance(quantity, int) and quantity > 0:
            self.quantity = quantity
        else:
            raise ValueError('Must be a number!')

        
        self.id_num = Product.next_id
        Product.next_id += 1

    @property
    def get_id(self):
        print("Id of this product is {}".format(self.id_num))

    def get_total_sum(self):
        sum = self.price * self.quantity
        return sum



earphones = Product("To jest dobry produkt","słuchawki", 20.0, 2)
apple = Product("bio owoc","jabłko", 2.0, 5)

print(apple.get_total_sum())
apple.get_id
earphones.get_id

