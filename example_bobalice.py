# Description of this example is provided in NTRU.md

from old_ntru import *
import numpy as np

# Bob

n = 31
p = 3
q = 1013

print("Bob Will Generate his Public Key using Parameters")
print("N=", n, "p=", p, "q=", q)
Bob = Ntru(n, p, q)
f = [1, 1, -1, 0, -1, 1]
g = [-1, 0, 1, 1, 0, 0, -1]
d = 2
print("f(x)= ", f)
print("g(x)= ", g)
print("d   = ", d)
Bob.genPublicKey(f, g, 2)
pub_key = Bob.getPublicKey()
print("Public Key Generated by Bob: ", pub_key)
print("-------------------------------------------------")
# Alice
Alice = Ntru(7, 29, 491531)
Alice.setPublicKey(pub_key)


# msg=[1,1,1,1,1,1,1]
# msg0 = "Hello World!"
# msg1 = list(msg0.encode('ascii'))
# msg2 = tuple(msg1)
# print(msg2)
# msg = np.poly(msg2)
msg = "bcd"

print("Alice's Original Message   : ", msg)
ranPol = [-1, -1, 1, 1]
print("Alice's Random Polynomial  : ", ranPol)
encrypt_msg = Alice.encrypt(msg, ranPol)
print("Encrypted Message          : ", encrypt_msg)
print("-------------------------------------------------")
# BOB
print("Bob decrypts message sent to him")
print("Decrypted Message          : ", Bob.decrypt(encrypt_msg))
