import statistics


n = int(input())
t = [int(x) for x in input().split(" ")]

t.sort()

moda = statistics.mode(t)

contador = 0
for l in t:
    if l == moda:
        contador+= 1

print(contador)