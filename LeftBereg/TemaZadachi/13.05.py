# Цифровой корень числа — это сумма его цифр, сведённая к одной цифре.
# 9875 => 9+8+7+5 = 29 =>2+9 = 11=> 1+1 = 2 
# Пример 
# Ввод: 
# 9875
# Вывод:
# 2
number = int(input())
while number >= 10:
    valueSum = 0
    while number > 0:
        valueSum += number % 10 
        number = number // 10
    number = valueSum
print(number)