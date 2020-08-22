import csv

class Product:
    def __init__(self):
        pass
    

    def __str__(self):
        return f"{self.name}, {self.unit}, {self.unit_price}, {self.quantity}"

    def create(self, data):
        self.product = data
        return self.product

class Warehouse:
    def __init__(self):
        self.products = {}

    def all(self):
        return self.products

    def add(self, product):
        if product["name"] in self.products: 
            if self.products[product["name"]]["unit_price"] == product["unit_price"]:
                old_quantity = self.products[product["name"] ]["quantity"]
                self.products[product["name"] ]["quantity"] = int(old_quantity) + product["quantity"]
                return self.products
        self.products[product["name"]] = product  # not working yet as products is a set
        return self.products

    def sell(self, product_name, quantity):
        old_quantity = self.products[product_name]["quantity"]
        self.products[product_name]["quantity"] = int(old_quantity) - int(quantity)
        return self.products


    def export(self):
        with open('Warehouse.csv', mode='w') as csv_file:
            fieldnames = ['name', 'unit', 'unit_price', 'quantity']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            for product in self.products:
                writer.writerow({"name":self.products[product]["name"],
                "unit":self.products[product]["unit"],
                "unit_price":self.products[product]["unit_price"],
                "quantity":self.products[product]["quantity"]})


    def load(self):
        with open('Warehouse.csv', mode='r') as csv_file:
            try:
                csv_reader = csv.DictReader(csv_file)
                self.products = {rows["name"]:rows for rows in csv_reader}
            except FileNotFoundError:
                self.products = {}
        return self.products


products = Warehouse()
new_product = Product()