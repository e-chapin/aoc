# https://stackoverflow.com/a/37058745
def divisors(n):
    # get factors and their counts
    factors = {}
    nn = n
    i = 2
    while i*i <= nn:
        while nn % i == 0:
            factors[i] = factors.get(i, 0) + 1
            nn //= i
        i += 1
    if nn > 1:
        factors[nn] = factors.get(nn, 0) + 1

    primes = list(factors.keys())

    # generates factors from primes[k:] subset
    def generate(k):
        if k == len(primes):
            yield 1
        else:
            rest = generate(k+1)
            prime = primes[k]
            for factor in rest:
                prime_to_i = 1
                # prime_to_i iterates prime**i values, i being all possible exponents
                for _ in range(factors[prime] + 1):
                    yield factor * prime_to_i
                    prime_to_i *= prime

    # in python3, `yield from generate(0)` would also work
    for factor in generate(0):
        yield factor

max = 36000000
house = 1
print('2015 Day 20 Part 1')
while True:
    sum = 0
    for d in divisors(house):
        sum += 10*d
    if sum >= max:
        print(house)
        break
    house += 1

house = 1
elfs = {}
print('2015 Day 20 Part 2')
while True:
    sum = 0
    for d in divisors(house):
        elfs[d] = elfs.setdefault(d, 0) + 1
        if elfs[d] > 50:
            continue
        sum += 11*d
    if sum >= max:
        print(house)
        break
    house += 1
