import random
from math import floor, sqrt

def sieve_of_eratosthenes(n):
    primes = [True for _ in range(n)]
    upper_bound = floor(sqrt(n) + 1)

    for i in range(2, upper_bound):
        if (primes[i] == True):
            for j in range(i * i, n, i):
                primes[j] = False
 
    numbers = []
    for i in range(2, n):
        if primes[i] == True:
            numbers.append(i)

    return numbers

def check_if_primitive_root(g, n):
    results = []

    # calculate all posible remainders of g^i mod n
    for i in range(1, n):
        result = pow(g, i, n)
        results.append(result)

    contains_all = True

    # check whether results contain all possible values between 1 and (n - 1)
    for i in range(1, n):
        if not (i in results):
            contains_all = False
            break
    return contains_all

def find_smallest_primitive_root(n):
    for i in range(2, n):
        candidate = i
        if check_if_primitive_root(candidate, n):
            return candidate

    return None

def encipher(message, p, g, y):
    # private key, ephemeral key
    k = random.randint(2, p - 2)
    print(f"Private key k: {k}")

    # public key
    a = pow(g, k, p)
    print(f"Public key a: {a}")

    decoded = bytearray(message, encoding="ascii")
    encrypted = []

    for m in decoded:
        encrypted.append(((m % p) * pow(y, k, p)) % p)

    return (a, encrypted)

def to_ascci(m):
    return m.to_bytes(1, byteorder="big").decode(encoding="ascii")

def decipher(encrypted, a, x, p):
    tmp = pow(a, p - 1 - x, p)

    plain = []
    for e in encrypted:
        m = ((e % p) * (tmp % p)) % p
        plain.append(to_ascci(m))

    return "".join(plain)

max_prime = 9999

# generate prime number
p = sieve_of_eratosthenes(max_prime)[-1]
print(f"Selected prime: {p}")

# generate primitive root mod p
g = find_smallest_primitive_root(p)
print(f"Primitive root modulo p (generator): {g}")

# private key
# p - 2 because randint includes both ends of range
x = random.randint(2, p - 2)
print(f"Private key x: {x}")

# public key
y = pow(g, x, p)
print(f"Public key y: {y}")

message = "Hello! :)"
print(f"Message: {message}")

a, encrypted = encipher(message, p, g, y)
print(f"Cipher: {encrypted}")

decrypted = decipher(encrypted, a, x, p)
print(f"Decrypted message: {decrypted}")
