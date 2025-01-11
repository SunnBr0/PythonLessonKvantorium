class Temperature:
    def __init__(self,celsius):
        self.celsius = celsius
    def celsiusAtfarenheit(self):
        return self.celsius *1.8 + 32
    def farenheitAtcelsius(self,value):
        return (value-32) *5 /9
    def celsiusAtKelvin(self):
        return self.celsius + 273
    def farenheitAtKelvin(self,value):
        # return (value -273 )*1.8 + 32
        return  (value*5)/9+459.67
temp = Temperature(20)
valueF = temp.celsiusAtfarenheit()
print(f"Фаренгейты: {valueF}")
valueC = temp.farenheitAtcelsius(valueF)
print(f"Цельсии: {valueC}")
valueC = temp.celsiusAtKelvin()
print(f"Кельвины: {valueC}")
print(f"Из Фаренгейтов в Кельвины: {temp.farenheitAtKelvin(valueF)}")