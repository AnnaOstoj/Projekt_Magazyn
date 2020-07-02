
def close_application():
    exit()

def get_items(items):
    
    l_items = len(items)
    items_in_stock = "Name\t\tQuantity\tUnit\t\tUnit Price (PLN)\n"\
                    +"----\t\t--------\t----\t\t----------------\n"

    for i in range(l_items):
        item_name = items[i]["name"]
        item_quantity = items[i]["quantity"]
        item_unit = items[i]["unit"]
        item_unit_price = items[i]["unit_price"]

        items_in_stock += "{}\t\t{:<}\t\t{:<}\t\t{:<}\n".format(item_name, item_quantity, item_unit, item_unit_price)
    return print(items_in_stock)

def add_item(items):
    # get input from user
    item_name = input("Item name: ")
    item_quantity = input("Item quantity: ")
    item_unit = input("Item unit: ")
    item_unit_price = input("Item unit price: ")

    items.append({"name": item_name, "quantity": item_quantity, "unit": item_unit, "unit_price":item_unit_price})
    return items

def sell_items(items, sold_items):
    name = input("Sold item name: ")
    quantity = float(input("Sold item quantity: "))
    l_items = len(items)
    for i in range(l_items):
        if items[i]["name"] == name:
            new_quantity = float(items[i]["quantity"]) - quantity
            items[i]["quantity"] = new_quantity
            sold_items.append({"name": name, "quantity": quantity, "unit": items[i]["unit"], "unit_price":items[i]["unit_price"]})
    return items, sold_items

def get_costs(items):
    l_items = len(items)
    cost_per_product = [float(items[i]["quantity"]) * float(items[i]["unit_price"]) for i in range(l_items)]
    return sum(cost_per_product)

def get_income(sold_items):
    l_sold_items = len(sold_items)
    cost_per_product = [float(sold_items[i]["quantity"]) * float(sold_items[i]["unit_price"]) for i in range(l_sold_items)]
    return sum(cost_per_product)

def show_revenue(items, sold_items):
    income = get_income(sold_items)
    costs = get_costs(items)
    revenue = income - costs
    return print(f"Revenue breakdown (PLN):\nIncome: {income}\nCosts: {costs}\n=======\nRevenue: {revenue}")
    
def export_items_to_csv(items, file_path = "C:/Users/aniak/Desktop/magazyn.csv"):

    import csv

    with open(file_path, 'w', newline='') as csvfile:
        fieldnames = ['name', 'quantity', 'unit', 'unit_price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(len(items)):
            writer.writerow(items[i])

def export_sales_to_csv(sold_items, file_path = "C:/Users/aniak/Desktop/sales.csv"):
    import csv

    with open(file_path, 'w', newline='') as csvfile:
        fieldnames = ['name', 'quantity', 'unit', 'unit_price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(len(sold_items)):
            writer.writerow(sold_items[i])

def load_items_from_csv(items, file_path = "C:/Users/aniak/Desktop/magazyn.csv"):
    import csv
    
    items.clear()
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            items.append(row)
    return items

    
