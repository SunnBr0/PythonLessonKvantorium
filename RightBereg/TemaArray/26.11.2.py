products =  {"яблоко": 50,"молоко":10,"мандарины":20,"яйца":60}
resultSum = 0
print("Магазин ,вот список продуктов: ")
for product , price in products.items():
    print(f"{product} - {price} изумрудов.")
while True : 
    valueProduct = input("Введите название товара или стоп: ").lower()
    if valueProduct =="стоп":
        break
    if valueProduct in products:
        countProduct = int(input("Введите количество: "))
        resultSum += countProduct *  products[valueProduct]
    else:
        print("У жителя не такого товара")
print(f"Общая сумма покупки: {resultSum}")
