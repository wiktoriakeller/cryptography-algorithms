import random
from math import sqrt, floor

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

# calculate shared secret using long term and short term keys
# e.g. person Alice: (bob short term key x bob long term key^(bob short term key))
#to the power (alice short term private key + alice long term private key x alice short term public key)
def get_shared_secret(send_short_public, send_long_public, my_short_private, my_short_public, my_long_private, n):
    power = send_short_public * pow(send_long_public, send_short_public)
    exponent = my_short_private + (my_long_private * my_short_public)
    shared_secret = pow(power, exponent, n)
    return shared_secret

min_key = 100
max_key = 500
max_prime = 9999

n = sieve_of_eratosthenes(max_prime)[-1]
print(f"Prime number n: {n}")

# primitive root modulo n
g = find_smallest_primitive_root(n)
print(f"Primitive root modulo n: {g}")
print(f"Check if primitive root modulo n is valid: {check_if_primitive_root(g, n)}")

# Alice long term keys
long_term_private_a = random.randint(min_key, max_key)
print(f"Alice, long term private key: {long_term_private_a} ")

long_term_public_a = pow(g, long_term_private_a, n)
print(f"Alice, long term public key: {long_term_public_a} sending to Bob")

# Bob long term keys
long_term_private_b = random.randint(min_key, max_key)
print(f"Bob long term private key: {long_term_private_b}")

long_term_public_b = pow(g, long_term_private_b, n)
print(f"Bob, long term public key: {long_term_public_b}, sending to Alice")

# Alice short term keys
short_term_private_a = random.randint(min_key, max_key)
print(f"Alice, short term private key: {short_term_private_a} ")

short_term_public_a = pow(g, short_term_private_a, n)
print(f"Alice, short term public key: {short_term_public_a} sending to Bob")

# Bob long term keys
short_term_private_b = random.randint(min_key, max_key)
print(f"Bob short term private key: {short_term_private_b}")

short_term_public_b = pow(g, short_term_private_b, n)
print(f"Bob, short term public key: {short_term_public_b}, sending to Alice")

# Alice shared secret 
shared_secret_a = get_shared_secret(short_term_public_b, long_term_public_b, short_term_private_a, short_term_public_a, long_term_private_a, n)
print(f"Alice, shared secret: {shared_secret_a}")

# Bob shared secret
shared_secret_b = get_shared_secret(short_term_public_a, long_term_public_a, short_term_private_b, short_term_public_b, long_term_private_b, n)
print(f"Bob, shared secret: {shared_secret_b}")

assert shared_secret_a == shared_secret_b
