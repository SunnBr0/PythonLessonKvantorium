f = open('third.txt', 'w',encoding="utf-8")
# f = open('third.txt', 'w',encoding="utf-8")
for i in range(1040, 1200):
  f.write(chr(i))
  f.write('\n')
f.close()