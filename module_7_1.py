# Задача "Учёт товаров"

class Product:
    def __init__(self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)
        # self.line = str()

    def __str__(self):
        # self.line = f'{self.name}, {self.weight}, {self.category}'
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'
        # super().__init__()

    def get_products(self):
        file = open(self.__file_name, 'r')
        products = file.read()
        file.close()
        return products

    def add(self, *products):
        # Product.line = Shop.get_products(self)
        current_products = self.get_products()
        file = open(self.__file_name, 'a')
        # for i in range(0, len(products)):
        for product in products:
            # if Product.__str__(products[i]) in Product.line:
            if str(product) not in current_products:
                file.write(str(product) + '\n')
                current_products += str(product) + '\n'
                # product_line = str.split(Product.__str__(products[i]))
                # print(f'Продукт {''.join(product_line)} уже есть в магазине.')
            else:
                # file.write(Product.__str__(products[i]) + '\n')
                print(f'Продукт {product} уже есть в магазине.')
        file.close()
        return


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2)  # __str__
s1.add(p1, p2, p3)
print(s1.get_products())
