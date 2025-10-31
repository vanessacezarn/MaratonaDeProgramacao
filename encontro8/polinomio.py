def collatz_polinomio(polinomio):
    """
    polinomio é representado como um conjunto de expoentes.
    Exemplo: {0,1,3} representa P(x) = x^3 + x + 1
    """
    passos = 0
    
    while polinomio != {0}:  # até P(x) = 1
        if 0 in polinomio:  # tem termo constante
            novo = set()
            # P(x) * x → soma 1 no expoente
            for exp in polinomio:
                novo.add(exp + 1)
            # Soma P(x)
            for exp in polinomio:
                if exp in novo:
                    novo.remove(exp)  # coeficiente virou 2 → descarta
                else:
                    novo.add(exp)
            # Soma 1 → adiciona expoente 0
            if 0 in novo:
                novo.remove(0)  # coeficiente virou 2 → descarta
            else:
                novo.add(0)
            polinomio = novo
        else:  # divide por x
            polinomio = {exp - 1 for exp in polinomio}
        
        passos += 1
    
    return passos


# --- Entrada ---
N = int(input().strip())
coef = list(map(int, input().split()))

# Converte coeficientes em conjunto de expoentes
# coef[0] = aN, coef[-1] = a0
expoentes = {N - i for i, c in enumerate(coef) if c == 1}

# --- Saída ---
print(collatz_polinomio(expoentes))
