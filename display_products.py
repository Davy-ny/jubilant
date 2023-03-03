from main import Product

products = Product.select()
for product in products:
    print(product.product_price, product.product_quantity, product.product_description, product.product_color)
