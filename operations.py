
def close_application():
    exit()

def get_items(items):
    
    l_items = len(items)
    items_in_stock = "Name\t\tQuantity\tUnit\t\tUnit Price (PLN)\n"\
                    +"----\t\t--------\t----\t\t----------------\n\n"

    for i in range(l_items):
        item_name = items[i]["name"]
        item_quantity = items[i]["quantity"]
        item_unit = items[i]["unit"]
        item_unit_price = items[i]["unit_price"]

        items_in_stock += "{}\t\t{:<}\t\t{:<}\t\t{:<}\n".format(item_name, item_quantity, item_unit, item_unit_price)
    return items_in_stock

