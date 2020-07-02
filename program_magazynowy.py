import operations as op
import sys

operation_dict = {"exit": op.close_application, "show":op.get_items, "add":op.add_item, "sell":op.sell_items,\
         "show_revenue": op.show_revenue, "save":op.export_items_to_csv, "load":op.load_items_from_csv}
items = []
sold_items = []
while True:
    operation_type = input("What would you like to do? Type one of: exit, show, add, sell, show_revenue, save, load: ")
    
    if operation_type == "exit":
        op.close_application()
        break

    elif operation_type == "sell":
        op.sell_items(items, sold_items)

    elif operation_type == "show_revenue":
        op.show_revenue(items, sold_items)

    elif operation_type == "show":
        op.get_items(items)

    elif operation_type == "add":
        op.add_item(items)
        op.get_items(items)

    elif operation_type == "save":
        op.export_items_to_csv(items, sys.argv[1])
        op.export_sales_to_csv(sold_items, sys.argv[2])

    elif operation_type == "load":
        op.load_items_from_csv(items, sys.argv[1])
        op.get_items(items)
