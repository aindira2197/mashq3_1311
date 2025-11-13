class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.__stock = stock

    def purchase(self, quantity):
        if quantity <= self.__stock:
            self.__stock -= quantity
            print(f"{quantity} ta {self.name} xarid qilindi.")
        else:
            print("Sotuvda yo‘q.")

    def get_stock(self):
        return self.__stock


class InventoryManager:
    def __init__(self, product):
        self.product = product

    def add_stock(self, amount):
        if amount > 0:
            self.product._Product__stock += amount
            print(f"{amount} ta mahsulot qo‘shildi.")
        else:
            print("Yaroqsiz miqdor!")
