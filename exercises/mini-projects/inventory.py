def inventory(product_name, quantity):
    if quantity >= 10:
        return product_name + " is high stock"
    elif quantity >= 5:
        return product_name + " is middle stock"
    elif quantity >= 1:
        return product_name + " is low stock"
    else:
        return product_name + " is out of stock"
