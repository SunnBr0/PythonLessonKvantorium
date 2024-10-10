# and , or , not
age = 18 
hasPrava = True

if age >=21 and hasPrava:
    print("Вы можете водить машину")
else:
    print("Вы не можете водить машину")

hasTicket =False
Vip = False
if hasTicket or Vip :
    print("Вы можете войти на концерт.")
else:
    print("Вы не можете войти на концерт.")

isRain = True
if (not isRain):
    print("Идём гулять")
else:
    print("Не идём гулять")
print(not isRain)