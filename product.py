def product_details(product_id, name, quantity, price):
    result = (
        f"Product ID: {product_id}\n"
        f"Product Name: {name}\n"
        f"Quantity: {quantity}\n"
        f"Price: {price}"
    )
    return result


if __name__ == "__main__":
    product_id = "P101"
    name = "Keyboard"
    quantity = 10
    price = 750
    print(product_details(product_id, name, quantity, price))
