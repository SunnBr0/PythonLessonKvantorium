products = {"колбаса" : 150,"хлеб": 50,"сыр": 125,"чай": 100}
resultSum = 0
print("<Вы попали в магазин>")
for product,price in products.items():
    print(f"Товар {product} - по цене {price} изумрудов")
while True:
    valueProduct = input("Название товара или стоп: ").lower()
    if valueProduct == "стоп":
        break
    if valueProduct in products:
        countProduct = int(input("Введите количество: "))
        resultSum += countProduct* products[valueProduct]
    else:
        print("Такого товара нет в магазине ")
print(f"Итоговая стоимость {resultSum}")