def mod_inverse(a: int, m: int):
    x = 0
    y = 0
    g = gcd_extended(a, m, x, y)
    if g != 1:
        return None
    else:
        res = (x%m + m) % m
        return res

def gcd_extended(a: int, b: int, x: int, y:int):
    # Base Case
    if a == 0:
        x = 0
        y = 0
        return b
    # Buat variabel untuk mengisi nilai rekursi
    x1 = 0
    y1 = 0
    gcd = gcd_extended(b%a, a, x1, y1)
    # Memperbarui x dan y menggunakan nilai hasil rekursi
    x = y1 - int(b/a) * x1
    y = x1

    return gcd

def naive_mod_inverse(a: int, m: int):
    for i in range(m):
        if ((a%m) * (i%m))%m == 1:
            return i

# Untuk testing
if __name__=="__main__":
    a = 7
    m = 3120
    # print(mod_inverse(a, m))
    print(naive_mod_inverse(59,1120))