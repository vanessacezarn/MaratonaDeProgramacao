import time
def ciclo(indice, n):
    try:
        if  linhas[indice] == n:
            cima(indice, n)
            direita(indice, n)
            baixo(indice, n)
            esquerda(indice, n)
    except IndexError as e:
        pass
    except RecursionError:
        pass

def cima(indice, n):
    ciclo(indice - largura, n)

def baixo(indice, n):
    ciclo(indice + largura, n)

def direita(indice, n):
    ciclo(indice + 1, n)

def esquerda(indice, n):
    ciclo(indice - 1, n)

altura, largura = map(int, input().split())
linhas = []

for a in range(altura):
    linha = [int(x) for x in input().split()]
    linhas.extend(linha)
print(len(linhas))


indices=[]
for i in range((altura*largura)-1):
    if linhas[i] != -1:
        ciclo(i, linhas[i])
        print("b")



