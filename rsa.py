from helper.ascii_converter import i2osp, os2ip
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

def encrypt_data(plain_text: str, n: int, e:int, block_length: int)->float:
    # Mengubah semua karakter menjadi lowercase
    p_text = plain_text.lower() 
    # Menyiapkan list untuk menyimpan block text
    c = [] 
    block = ([p_text[i : i + block_length] for i in range(0, len(p_text), block_length)])
    print(block)
    print("Converted Block:", end=" ")
    for i in block:
        converted_block = os2ip(i) # Syarat converted block haru berada di 1 < converted_block < n-1
        print(converted_block, end=", ")
        # Rumus encrypt RSA => C=(P^e)mod(n).
        m = pow(converted_block, e)
        c_val: float = m%n
        c.append(c_val)
    print('')
    return c

def decrypt_data(c, d: int, n: int, block_length: int):
    # Menyiapkan list untuk menyimpa block text
    block_text = []
    print("Unconverted Block:", end=" ")
    for i in c:
        # Decrypted Data = pow(c,d) mod n. 
        m = pow(i, d)
        # print(m)
        f = m%n
        # print(f)
        print(f, end=", ")
        block_text.append(i2osp(f, block_length))
    print("")
    return block_text

if __name__=="__main__":
    # Memilih 2 bilangan prima yang besar
    p = 271
    q = 173

    # Menentukan block length untuk memecah string
    block_length = 3

    public_key = generate_public_key(p, q)
    private_key = generate_private_key(p, q, public_key[1])

    print("[n, e]:", public_key)
    print("d:", private_key)

    message = "Halo apa kabar dunia"
    print("Message =", message)
    
    # encrpyt
    cipher = encrypt_data(message, public_key[0], public_key[1], block_length)
    print("Encrypted: ", cipher)

    # Decrypt
    plain = decrypt_data(cipher, private_key, public_key[0], block_length)
    print("Decrypted: ", plain)
    