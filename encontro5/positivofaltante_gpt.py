n = int(input())  # lê a quantidade de elementos
numeros = list(map(int, input().split()))  # lê os elementos da lista

num_set = set(numeros)  # cria um conjunto para buscas rápidas

for i in range(1, n + 2):  # percorre de 1 até n+1 (inclusive)
    if i not in num_set:    # se i não está no conjunto, é o menor que falta
        print(i)
        break