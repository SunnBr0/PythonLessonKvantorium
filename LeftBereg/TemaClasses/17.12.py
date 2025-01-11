class MathUtils:
    @staticmethod
    def sum(numberOne,numberTwo):
        return numberOne + numberTwo
    @staticmethod
    def multiplication(numberOne,numberTwo):
        return numberOne * numberTwo
    @staticmethod
    def division(numberOne,numberTwo):
        return numberOne / numberTwo
    @staticmethod
    def pow(digit,stepen):
        number = 1
        for _ in range(1,stepen+1):
            number *= digit
        return number
    @staticmethod
    def factorial(digit):
        number = 1
        for i in range(1,digit+1):
            number *= i
        return number
print(f"Сумма {MathUtils.sum(10,2)}")
print(f"Произведение {MathUtils.multiplication(10,2)}")
print(f"Деление {MathUtils.division(10,2)}")
print(f"Степень {MathUtils.pow(4,2)}")
print(f"Факториал {MathUtils.factorial(5)}")