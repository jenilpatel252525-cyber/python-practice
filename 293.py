from collections import Counter

def prime_factors(n):
    i = 2
    factors = Counter()
    
    while i * i <= n:
        while n % i == 0:
            factors[i] += 1
            n //= i
        i += 1
    
    if n > 1:
        factors[n] += 1
    
    return factors


def lcm(a, b):
    fa = prime_factors(a)
    fb = prime_factors(b)
    
    # result prime powers
    result = 1
    
    # union of primes
    for p in set(fa.keys()) | set(fb.keys()):
        result *= p ** max(fa[p], fb[p])
    
    return result

def gcd(a, b):
    fa = prime_factors(a)
    fb = prime_factors(b)
    
    # result prime powers
    result = 1
    
    # union of primes
    for p in set(fa.keys()) & set(fb.keys()):
        result *= p ** min(fa[p], fb[p])
    
    return result

def lcm(a, b):
    return abs(a*b) // gcd(a, b)
