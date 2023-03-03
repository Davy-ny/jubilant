from main import Product

try:
    product_price = input("Enter price \n")
    product_quantity = input("Enter quantity \n")
    product_description = input("Enter description \n")
    product_color = input("Enter color \n")

    Product.create(price=product_price, quantity=product_quantity, description=product_description, color=product_color)
    print("Product Created Successfully")
except:
    print("Failed to Create Product")
