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

def encipher(message, prime, generator, public_key):
  # private key for sender
  k = random.randint(2, prime - 2)
  
  # public key to decipher
  a = pow(generator, k, prime)
  
  encoded = str.encode(message)
  encrypted = (encoded * pow(public_key, k)) % prime
  return (a, encrypted)

def decipher(encrypted, decipher_key, private_key, prime):
  tmp = pow(decipher_key, prime - private_key - 1, prime)
  decipher = (encrypted * tmp) % prime
  return decipher
 
max_prime = 9999

# generate prime number
p = sieve_of_eratosthenes(max_prime)[-1]
print(f"Selected prime: {p}")

# generate prime root mod p
g = find_smallest_primitive_root(p)
print(f"Primitive root modulo p (generator): {g}")

# private key for receiver
# p - 2 because randint includes both ends of range
x = random.randint(2, p - 2)
print(f"Receiver private key: {x}")

# public key
y = pow(g, x, p)
print(f"Receiver public key: {y}")

message = 2035
print(f"Message: {message}")

decipher_key, encrypted = encipher(message, p, g, y)
decrypted = decipher(encrypted, decipher_key, x, p)
print(decrypted)
