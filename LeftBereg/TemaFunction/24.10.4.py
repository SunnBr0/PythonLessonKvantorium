def power (base,exp):
    if exp == 0:
        return 1
    else:
        res = base*power(base,exp-1)
        return res
    
print(power(2,4))
print(power(3,3))