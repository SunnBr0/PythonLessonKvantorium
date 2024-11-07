def algoritmEvcklid(numOne,numTwo):
    while True:
        if numTwo != numOne:
            if numOne>numTwo :
                numOne -= numTwo
            else:
                numTwo -=numOne
        else:
            return numOne

print(algoritmEvcklid(128,80))
print(algoritmEvcklid(36,12))
print(algoritmEvcklid(645,381))