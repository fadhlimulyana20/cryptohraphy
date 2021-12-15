def gcd(a: int, b: int) -> int:
    if a == 0:
        return b
    return gcd(b%a, a)


if __name__=="__main__":
    print("Testing Helper")
    print("Gcd(2,3): {}".format(gcd(2,3)))