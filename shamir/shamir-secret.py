from random import randint

def generatePolynomial(secret, minimum, prime):
    polynomial = [secret]
    for _ in range(minimum - 1):
        polynomial.append(randint(1, prime // 2))
    return polynomial

def calculateShares(sharesNum, prime, polynomial):
    points = []
    for i in range(1, sharesNum + 1):
        pointValue = polynomial[0]
        for j in range(len(polynomial) - 1, 0, -1):
            pointValue += ((polynomial[j] * (i**(j))) % prime)
            #pointValue = (polynomial[j] * pow(i, j, prime))
        points.append([i, pointValue])
    return points

def gcdExtended(a, b):
    x = 0
    lastX = 1
    y = 1
    lastY = 0
    while b != 0:
        quot = a // b
        a, b = b, a % b
        x, lastX = lastX - quot * x, x
        y, lastY = lastY - quot * y, y
        
    return lastX, lastY

def getInverse(nominator, denominator, prime):
    inv, _ = gcdExtended(denominator, prime)
    return nominator * inv

def multiply(values):
    product = 1
    for v in values:
        product *= v
    return product

def lagrange(x, y, prime):
    searchPoint = 0
    numerators = []
    denominators = []
    
    for i in range(len(x)):
        rem = list(x)
        current = rem[i]
        rem = rem[:i] + rem[i + 1:]

        numerators.append(multiply([searchPoint - o for o in rem]))
        denominators.append(multiply([current - o for o in rem]))
    #print(numerators)
    #print(denominators)

    denominatorProd = multiply(denominators)
    sumval = 0
    for i in range(len(x)):
        sumval += getInverse((numerators[i] * denominatorProd * y[i]) % prime, denominators[i], prime)
    #print(sumval)

    return (getInverse(sumval, denominatorProd, prime) + prime) % prime

def recoverSecret(shares, prime):
    x = []
    y = []
    for i in range(len(shares)):
        x.append(shares[i][0])
        y.append(shares[i][1])

    return lagrange(x, y, prime)

if __name__ == "__main__":
    secret = int(input("Sekret: "))
    n = int(input("Liczba udzialow: "))
    t = int(input("Minimum: "))
    prime = (2 ** 41) - 1

    assert n >= t, "Liczba udzialow nie moze byc mniejsza od minimum"
    assert prime > secret, "Sekret nie moze byc wiekszy od liczby pierwszej"

    polynomial = generatePolynomial(secret, t, prime)
    #polynomial = [1234, 166, 94]
    print(polynomial)

    shares = calculateShares(n, prime, polynomial)
    print(shares)
    pointsToUse = shares[:t]
    #pointsToUse = [[2, 1942], [4, 3402], [5, 4414]]

    print(f'Sekret: {recoverSecret(pointsToUse, prime)}')
    