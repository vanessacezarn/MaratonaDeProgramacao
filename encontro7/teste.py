def gira_para_cima(x): return (x + 1) % 10
def gira_para_baixo(x): return (x - 1) % 10

n = int(input())
atual = list(map(int, input().split()))
senha = list(map(int, input().split()))

movimentos = 0

# Vamos resolver do último para o primeiro
for i in reversed(range(n)):
    if atual[i] == senha[i]:
        continue

    # Quantos giros para cima e para baixo são necessários?
    cima = (senha[i] - atual[i]) % 10
    baixo = (atual[i] - senha[i]) % 10

    # Escolhe o menor
    if cima <= baixo:
        movimentos += cima
        # Gira todos até o índice i para cima
        for j in range(i + 1):
            atual[j] = (atual[j] + cima) % 10
    else:
        movimentos += baixo
        # Gira todos até o índice i para baixo
        for j in range(i + 1):
            atual[j] = (atual[j] - baixo) % 10

print(movimentos)
