from product import product_details

def test_product_details():
    expected_output = (
        "Product ID: P101\n"
        "Product Name: Keyboard\n"
        "Quantity: 10\n"
        "Price: 750"
    )
    assert product_details("P101", "Keyboard", 10, 750) == expected_output
