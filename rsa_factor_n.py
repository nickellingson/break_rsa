# Cracking RSA, trial
from sympy.ntheory import factorint
from Crypto.Util.number import inverse

def trial_division(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return i, n // i
    return None, None

def trial_div_2(n):
    factors = factorint(n)
    p, q = list(factors.keys())
    print(f"p = {p}, q = {q}")
    return p, q

def compute_private(p, q, e):
    phi = (p - 1) * (q - 1)
    d = inverse(e, phi)
    return d

if __name__=="__main__":
    # result = trial_division(340282366920938460843936948965011886881)
    # print(result)

    n = 340282366920938460843936948965011886881
    e = 65537
    p, q = trial_div_2(n)
    pk = compute_private(p, q, e)
    print(pk)

