def convert_ascii(X):
    """
    Semua string harus lowercase

    Semua karakter selain alphabet akan diubah menjadi spasi
    """
    if isinstance(X, str):
        x = ord(X)
        if (x < 97 or x > 122):
            x = 0 
        else:
            x -= 96
    elif isinstance(X, int):
        x = X
        if x == 0 :
            x += 32 # ascii untuk spasi
        else:
            x += 96
        x = chr(x)
    return x

def i2osp(x, x_len):
    """converts a nonnegative integer(x) to an octet string(output) of a
   specified length(x_len)
    Args:
        x (integer): nonnegative integer to be converted
        x_len (integer): intended length of the resulting octet string
    Raises:
        ValueError: integer too large
    Returns:
        [String]: corresponding octet string of length xLen
    """
    if x >= 27 ** x_len:
        raise ValueError("integer too large")
    digits = []

    while x:
        digits.append(int(x % 27))
        x //= 27 # floor division operator

    for i in range(x_len - len(digits)): # note that one or more leading digits will be zero if x is less than 256^(xLen-1)
        digits.append(0)
    digits = digits[::-1]
    block_text = []
    for i in range(x_len):
        block_text.append(convert_ascii(digits[i]))
    return "".join(block_text)

def os2ip(X):
    """
    Mengubah semua oktet string ke dalam bentuk integer

    Args:
        X (string): oktet string yang akan diconvert

    Returns:
        integer: corresponding nonnegative integer
    """
    X = X[::-1] # Membalik array
    x = 0
    for i in range(len(X)):
        x += convert_ascii(X[i]) * 27 ** i
    return x

# Untuk testing
if __name__=="__main__":
    m = "Hari Minggu"
    m = m.lower()
    # print(os2ip(m))
    # print(i2osp(os2ip(m), 3))