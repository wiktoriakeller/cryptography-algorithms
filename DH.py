import random
from math import sqrt

def sieveOfEratosthenes(n):
    prime = [True for i in range(n+1)]
    for i in range(2, sqrt(n) + 1):
        if (prime[i] == True):
            for j in range(i * i, n, i):
                prime[j] = False
 
    numbers = []
    for i in range(2, n + 1):
        if prime[i] == True:
            numbers.append(i)

    return numbers

def checkIfPrimitiveRoot(g, n):
    results = []
    for i in range(1, n):
        result = pow(g, i, n)
        results.append(result)

    containsAll = True
    for i in range(1, n):
        if not (i in results):
            containsAll = False
            break
    return containsAll

def findSmallestPrimitiveRoot(n):
    for i in range(2, n):
        candidate = i
        if checkIfPrimitiveRoot(candidate, n):
            return candidate

    return None

min = 100
max = 500

#print(findSmallestPrimitiveRoot(4999))
#liczba pierwsza
n = 4999
print(f"Liczba pierwsza n: {n}")

#pierwiastek pierwotny modulo n
g = 7
print(f"Pierwiastek pierwotny g: {g}")
print(f"Sprawdzenie czy pierwiastek pierwotny modulo n jest prawidlowy: {checkIfPrimitiveRoot(g, n)}")

x = random.randint(min, max)
X = pow(g, x, n)
print(f"Strona A, X: {X}")

y = random.randint(min, max)
Y = pow(g, y, n)
print(f"Strona B, Y: {Y}")

sessionA = pow(Y, x, n)
print(f"Klucz sesji, strona A: {sessionA}")

sessionB = pow(X, y, n)
print(f"Klucz sesji, strona B: {sessionB}")
