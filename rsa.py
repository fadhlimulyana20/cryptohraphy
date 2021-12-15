from helper.extended_gcd import naive_mod_inverse
from helper.gcd import gcd


def generate_public_key(p: int, q: int):
    # Hitung n = p*q
    # p dan q adalah bilangan prima
    n = p*q
    e = None    
    phi = (p-1)*(q-1) # = Φ(n)
    # Mencari e
    # But e Must be 
    # An integer.
    # Not be a factor of n. 
    # 1 < e < Φ(n) [Φ(n) is discussed below], 
    # Let us now consider it to be equal to 3.
    # Mencari co prime of Φ(n)
    for i in range(phi):
        if i != 0 and i > 1:
            if gcd(i, phi) == 1:
                e = i
                break
    return [n, e] 

def generate_private_key(p: int, q:int, e:int):
    # Menghitung Φ(n) = (P-1)(Q-1)
    fi_n = (p-1)*(q-1)

    # Menghitung private key d
    # d = (k*Φ(n) + 1) / e, k adalah bilangan integer
    d = naive_mod_inverse(e, fi_n)

    return d

def encrypt_data(plain_text, n: int, e:int)->float:
    # Mengubah plain_text ke ascii
    # plain_ascii = ""
    # for i in plain_text:
    #     ascii_num = ord(i)
    #     print("debug_ascii_ord: {}".format(ascii_num))
    #     ascii_num_str = str(ascii_num)
    #     plain_ascii += ascii_num_str

    # plain_ascii_num = int(plain_ascii)
    # print("plain acii num: {}".format(plain_ascii_num))

    # Menghitung c
    # c = pow(89,e) mod n
    print(plain_text)
    m = pow(plain_text, e)
    print(m)
    c: float = m%n

    return c

def decrypt_data(c: int, d: int, n: int):
    # Decrypted Data = pow(c,d) mod n. 
    m = pow(c, d)
    # print(m)
    f = m%n
    # print(f)

    return f

if __name__=="__main__":
    p = 61
    q = 53

    public_key = generate_public_key(p, q)
    private_key = generate_private_key(p, q, public_key[1])

    print(public_key)
    print(private_key)

    c = encrypt_data(103104, public_key[0], public_key[1])
    print(c)

    # print("Encrypted Data: {}".format(encrypt_data("2weqwewqewqei2-0uq9u2-3ke sip yes yes Hura Hura", public_key[0], public_key[1])))
    print("Decrypted Data: {}".format(decrypt_data(c, private_key, public_key[0])))
    