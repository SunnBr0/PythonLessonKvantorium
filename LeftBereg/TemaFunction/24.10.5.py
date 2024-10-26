def algoritmEvcklid(numOne,numTwo):
    while True:
        if numTwo != numOne:
            if numOne > numTwo:
                numOne -= numTwo
            else:
                numTwo -= numOne
        else:
            return numOne
    
print(algoritmEvcklid(121,110))