s = input().strip()
n = len(s)
for pulo in range(n // 2, 0, -1):
    if n % pulo == 0:
        bloco = s[:pulo]
        vezes = n // pulo
        if bloco * vezes == s:
            print(bloco)
            break
else:
    print("-1")