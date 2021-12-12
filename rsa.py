def generate_public_key(p: int, q: int):
    # Hitung n = p*q
    # p dan q adalah bilangan prima
    n = p*q
    e = None

    # Mencari e
    # But e Must be 

    # An integer.
    # Not be a factor of n. 
    # 1 < e < Φ(n) [Φ(n) is discussed below], 
    # Let us now consider it to be equal to 3.

    for i in range(n):
        if i != 0:
            if n%i == 0:
                e = i
                break
    
    return [n, e]

def generate_private_key(p: int, q:int, e:int, k:int):
    # Menghitung Φ(n) = (P-1)(Q-1)
    fi_n = (p-1)*(q-1)

    # Menghitung private key d
    # d = (k*Φ(n) + 1) / e, k adalah bilangan integer
    d = (k*fi_n + 1)/e

    return d

def encrypt_data(plain_text: str, n: int, e:int)->float:
    # Mengubah plain_text ke ascii
    plain_ascii = ""
    for i in plain_text:
        ascii_num = ord(i)
        ascii_num_str = str(ascii_num)
        plain_ascii += ascii_num_str
    
    plain_ascii_num = int(plain_ascii)
    # print(plain_ascii_num)

    # Menghitung c
    # c = pow(89,e) mod n
    m: float = pow(plain_ascii_num, e)
    c: float = m%n

    return c

def decrypt_data(c: int, d: int, n: int):
    # Decrypted Data = pow(c,d) mod n. 
    m = pow(c, d)
    print(m)
    f = m%n
    print(f)

    return f

if __name__=="__main__":
    p = 3
    q = 7

    public_key = generate_public_key(p, q)
    private_key = generate_private_key(p, q, public_key[1], 2)

    c = encrypt_data("hi", public_key[0], public_key[1])

    print("Encrypted Data: {}".format(encrypt_data("2weqwewqewqei2-0uq9u2-3ke sip yes yes Hura Hura", public_key[0], public_key[1])))
    print("Decrypted Data: {}".format(decrypt_data(c, private_key, public_key[0])))
    