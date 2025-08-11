n = int(input())

vogais = "aeiou"

for _ in range(n):
    frase = input().strip()  # tira espaços extras no começo/fim
    palavras = frase.split()  # separa palavras ignorando múltiplos espaços

    flag = True  # assume que a frase é válida

    for p in palavras:
        p = p.lower()

        tamanho = len(p)

        if tamanho == 1:
            # nenhuma regra, palavra válida
            continue

        elif tamanho > 5:
            # deve começar e terminar com vogal
            if p[0] not in vogais or p[-1] not in vogais:
                flag = False
                break

        else:
            # palavra com tamanho entre 2 e 5
            # deve começar com consoante e terminar com vogal
            if p[0] in vogais or p[-1] not in vogais:
                flag = False
                break

    print("SIM" if flag else "NAO")