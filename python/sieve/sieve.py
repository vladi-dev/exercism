def sieve(lim):
    non_prime = []
    return [x for x in range(2, lim + 1) if x not in non_prime and [non_prime.append(y) for y in range(x, lim + 1, x)]]
