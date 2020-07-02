import operations as op

items = [{"name" : "Krzesło",  "quantity" : 50, "unit" : "pc", "unit_price" : 200},\
        {"name" : "Stół",  "quantity" : 20, "unit" : "pc", "unit_price" : 500},\
        {"name" : "Stołek",  "quantity" : 99, "unit" : "pc", "unit_price" : 90}]

sold_items = []
operation_dict = {"exit": op.close_application, "show":op.get_items, "add":op.add_item, "sell":op.sell_items, "show_revenue": op.show_revenue}

while True:
    operation_type = input("What would you like to do? Type one of: exit, show, add, sell, show_revenue: ")
    if operation_type == "exit":
        op.close_application()
        break
    elif operation_type == "sell":
        op.sell_items(items, sold_items)
    elif operation_type == "show_revenue":
        costs = op.get_costs(items)
        income = op.get_income(sold_items)
        print(op.show_revenue(costs, income))
    elif operation_type == "show":
        print(op.get_items(items))
    elif operation_type == "add":
        op.add_item(items)
        op.get_items(items)
        