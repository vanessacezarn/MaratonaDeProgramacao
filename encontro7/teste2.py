n = int(input())
atual = list(map(int, input().split()))
senha = list(map(int, input().split()))

movimentos = 0
offset = 0  # Quantidade acumulada de giros aplicados a todos os cilindros

for i in reversed(range(n)):
    # Calcula valor atual considerando os giros acumulados
    valor_atual = (atual[i] + offset) % 10
    if valor_atual == senha[i]:
        continue

    cima = (senha[i] - valor_atual) % 10
    baixo = (valor_atual - senha[i]) % 10

    if cima <= baixo:
        movimentos += cima
        offset = (offset + cima) % 10
    else:
        movimentos += baixo
        offset = (offset - baixo) % 10

print(movimentos)
