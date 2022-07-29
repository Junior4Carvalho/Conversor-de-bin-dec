numB = input('entre com binario: ')
numD = 0
aux = len(numB) - 1
print(aux, len(numB))
for x in numB:
    if x == '1':
        numD += 2 ** aux
        aux -= 1    
        print("o que tá acontecendo aqui ", numB, numD, aux, x)
    else:
        aux -= 1
        print("O que tá acontecendo no else", numB, numD, aux, x)
        continue
print(numD)

#Copyright-@Junior4Carvalho
