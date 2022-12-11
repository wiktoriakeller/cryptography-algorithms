import random
from math import sqrt

def sieve_of_eratosthenes(n):
    primes = [True for _ in range(n+1)]
    for i in range(2, sqrt(n) + 1):
        if (primes[i] == True):
            for j in range(i * i, n, i):
                primes[j] = False
 
    numbers = []
    for i in range(2, n + 1):
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

min = 100
max = 500

n = 4999
print(f"Prime number n: {n}")

# primitive root modulo n
g = find_smallest_primitive_root(4999)
print(f"Primitive root modulo n: {g}")
print(f"Check if primitive root modulo n is valid: {check_if_primitive_root(g, n)}")

# Alice long term keys
long_term_private_a = random.randint(min, max)
print(f"Alice, long term private key: {long_term_private_a} ")

long_term_public_a = pow(g, long_term_private_a, n)
print(f"Alice, long term public key: {long_term_public_a} sending to Bob")

# Bob long term keys
long_term_private_b = random.randint(min, max)
print(f"Bob long term private key: {long_term_private_b}")

long_term_public_b = pow(g, long_term_private_b, n)
print(f"Bob, long term public key: {long_term_public_b}, sending to Alice")

# Alice short term keys
short_term_private_a = random.randint(min, max)
print(f"Alice, short term private key: {short_term_private_a} ")

short_term_public_a = pow(g, short_term_private_a, n)
print(f"Alice, short term public key: {short_term_public_a} sending to Bob")

# Bob long term keys
short_term_private_b = random.randint(min, max)
print(f"Bob short term private key: {short_term_private_b}")

short_term_public_b = pow(g, short_term_private_b, n)
print(f"Bob, short term public key: {short_term_public_b}, sending to Alice")

# Alice shared secret 
power_a = short_term_public_b * pow(long_term_public_b, short_term_public_b)
exponent_a = short_term_private_a + (long_term_private_a * short_term_public_a)
shared_secret_a = pow(power_a, exponent_a, n)
print(f"Alice, shared secret: {shared_secret_a}")

# Bob shared secret
power_b = short_term_public_a * pow(long_term_public_a, short_term_public_a)
exponent_b = short_term_private_b + (long_term_private_b * short_term_public_b)
sahred_secret_b = pow(power_b, exponent_b, n)
print(f"Bob, shared secret: {sahred_secret_b}")

assert shared_secret_a == sahred_secret_b
