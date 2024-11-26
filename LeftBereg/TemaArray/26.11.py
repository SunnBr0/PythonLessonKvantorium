products = {
    "колбаса" : 150,
    "хлеб": 50,
    "сыр": 125,
    "чай": 100
}
resultSum = 0
print("<Вы попали в магазин>")
for product,price in products.items():
    print(f"Товар {product} - по цене {price} изумрудов")