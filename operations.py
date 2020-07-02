
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
    return items_in_stock

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
            items[i]["quantity"] -= quantity
            sold_items.append({"name": name, "quantity": quantity, "unit": items[i]["unit"], "unit_price":items[i]["unit_price"]})
    return items, sold_items

def get_costs(items):
    l_items = len(items)
    cost_per_product = [items[i]["quantity"] * items[i]["unit_price"] for i in range(l_items)]
    return sum(cost_per_product)

def get_income(sold_items):
    l_sold_items = len(sold_items)
    cost_per_product = [sold_items[i]["quantity"] * sold_items[i]["unit_price"] for i in range(l_sold_items)]
    return sum(cost_per_product)

def show_revenue(costs, income):
    revenue = income - costs
    return f"Revenue breakdown (PLN):\nIncome: {income}\nCosts: {costs}\n=======\nRevenue: {revenue}"
    


    
