def gcd(x, y):
    while y:
        x, y = y, x % y

    return x

def extend_gcd(x, y):
    if x == 0:
        return y, 0, 1

    gcd, a, b = extend_gcd(y % x, x)

    return gcd, b - (y // x) * a, a

def mod_inv(x, p):
    return pow(x, -1, p)

def cubic_root(x):
    h = 1

    while h**3 < x:
        h *= 2

    l = h // 2
    m = 0

    while l < h:
        m = l + (h - l) // 2

        if m**3 < x and l < m:
            l = m
        elif m**3 > x and h > m:
            h = m
        else:
            return m

    return m + 1

def get_factors(n):
    if n % 2 == 0:
        return 2, n // 2

    for i in range(3, n, 2):
        if n % i == 0:
            return i, n // i

def phi(p, q):
    return (p-1) * (q-1)
