from Crypto.PublicKey import RSA
from Crypto.Util import number
import random

aMillion = 90
bMillion = 150
M = 200

# generate private and public key
bitsNum = 1024
keyPair = RSA.generate(bits=bitsNum)
publicKey = keyPair.public_key()
print("A generated private and public keys, send public key to B")

# generate random x
x = random.randint(0, 10000)
print(f"B generated x: {x}")

# encipher x with public key
c = pow(x, publicKey.e, publicKey.n)
print(f"B Enciphered C: {c}")

m = c - bMillion + 1
print(f"B calculated m: {m} and send it to A")

Z = []
p = 2
while True:
  p = number.getPrime(keyPair.size_in_bits() // 2)
  Y = [pow((m + j - 1), keyPair.d, keyPair.n) for j in range(1, M + 1)]
  Z = [y % p for y in Y]

  reducedProperly = True
  for i in range(0, len(Z)):
    for j in range(0, len(Z)):
      if i != j and abs(Z[i] - Z[j]) < 2:
        reducedProperly = False
        break
    if not(reducedProperly):
      break

  if reducedProperly:
    break

print("A calculated Z")

W = []
for i in range(0, len(Z)):
  num = Z[i]
  if (i + 1) >= aMillion:
    num += 1
  W.append(num)

print("A calculated W and send it to B")
if x % p == W[bMillion - 1]:
  print("A is richer")
else:
  print("B is richer")