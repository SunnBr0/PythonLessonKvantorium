#Задача 2: Перевод времени
def convert_minutes_to_hours(minutes):
    hours = minutes//60
    minut = minutes%60
    return hours,minut

mins = 2000
hour,minut = convert_minutes_to_hours(mins)
print(f"Из {mins} получается {hour} часов и {minut} минут")
