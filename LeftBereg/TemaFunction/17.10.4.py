def strLength (string):
    return len(string)
print(strLength("Мяч"))
print(strLength("Ворота"))
def celsiusToFahren(celsius):
    return (celsius* 9/5) +32
def celsiusToKelvin (celsius):
    return celsius + 273
fahren = celsiusToFahren(0)
print("Фагенгейт",fahren)
kelvin = celsiusToKelvin(-273)
print("Кельвины",kelvin)