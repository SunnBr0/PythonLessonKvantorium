def strLength(string):
    return len(string)
print(strLength("Мяч"))
print(strLength("Ворота"))
def celsiusToFahren(celsius):
    return (celsius*1.8)+32
print(celsiusToFahren(0))
print(celsiusToFahren(30))
def celsiusToKelvin(celsius):
    return celsius + 273
kelvin = celsiusToKelvin(-273)
print("kelvin: ",kelvin)