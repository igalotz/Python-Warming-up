
next_id = 1


class Product(object):

    def __init__(self, description, name, price, quantity):
        global next_id


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


        self.id_num = next_id
        next_id += 1


    @property
    def get_id(self):
        return self.id_num



    def get_total_sum(self):
        if self.quantity >=3:
            sum = self.price * self.quantity
            discount = sum * 0.2
            sum -= discount
            return sum
        else:
            sum = self.price * self.quantity
            return sum



earphones = Product("To jest dobry produkt","słuchawki", 20.0, 2)
apple = Product("bio owoc","jabłko", 2.0, 5)

# print(apple.get_total_sum())
# apple.get_id
# earphones.get_id




class ShoppingCart(object):
    def __init__(self):
        self.shopping_cart_content = []


#ważna funkcja, która wyszukuje nam dana instancje po id!
    def find_product(self, product_id):
        for prod in self.shopping_cart_content:
            if prod.id_num == product_id:
                return prod

    def add_product(self, new_product):
        self.shopping_cart_content.append(new_product)

    def remove_product(self, product_id):
        prod_to_remove = self.find_product(product_id)
        if prod_to_remove in self.shopping_cart_content:
            self.shopping_cart_content.remove(prod_to_remove)
        else:
            print("Nie ma takiego produktu")

    def change_product_quantity(self, product_id, new_quantity):
        prod_to_change = self.find_product(product_id)
        if prod_to_change in self.shopping_cart_content:
            prod_to_change.quantity = new_quantity

    def print_receipt(self):
        to_pay = 0.0
        for product in self.shopping_cart_content:
            print("id produktu: {}| nazwa: {}| cena za szt: {} zł | ilość:{} || cena {}".format(product.id_num, product.name,product.price,product.quantity, product.get_total_sum()))
            to_pay += product.get_total_sum()
        print("Razem do zapłaty: {}".format(to_pay))




d = ShoppingCart()
d.add_product(apple)
d.add_product(earphones)
# print(d.find_product(2))
# d.remove_product(1)

# print(d.shopping_cart_content)
d.change_product_quantity(2,10)
# print(apple.quantity)

d.print_receipt()






