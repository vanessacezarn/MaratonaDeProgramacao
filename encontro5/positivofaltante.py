n = int(input())
numeros = [int(x) for x in input().split(' ')]
numeros.sort()

numeros_copia = numeros.copy()

for nl in numeros_copia:
    if nl <= 0:
        numeros.remove(nl)

numeros.append(99999999)

for x in range(len(numeros)-1):
    if numeros[0] != 1:
        print('1')
        break
    else:
        if numeros[x+1]-numeros[x] != 1 and numeros[x+1]-numeros[x] != 0:
            print(numeros[x] + 1)
            break

