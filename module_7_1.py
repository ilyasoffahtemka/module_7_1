class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        try:
            with open(self.__file_name, 'r') as file:
                return file.read().strip()
        except FileNotFoundError:
            return ""  # Возвращаем пустую строку, если файл ещё не существует

    def add(self, *products):

        current_products = self.get_products().splitlines()
        product_names = {line.split(', ')[0] for line in current_products}

        with open(self.__file_name, 'a') as file:
            for product in products:
                if product.name in product_names:
                    print(f"Продукт {product} уже есть в магазине")
                else:
                    file.write(str(product) + '\n')
                    product_names.add(product.name)


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)

s1.add(p1, p2, p3)

print(s1.get_products())