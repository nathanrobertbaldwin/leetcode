import math


def find_largest_prime_factor(num):
    # Start a list of primes. You know 2 is prime, so seed it. This allows you to start testing new primes at 3, going by 2.
    primes = [2]
    # Every number is divisible by 1.
    largest_prime_factor = 1

    for i in range(3, num + 1, 2):
        # assume the next test number is prime
        is_prime = True
        # if the next num is divisible by any prime, then next num is not itself prime
        for prime in primes:
            if prime > math.sqrt(num):
                break
            if i % prime == 0:
                is_prime = False
                break

        if is_prime == True:
            # if we find a new prime, we append it to the list of primes
            primes.append(i)
            # if num is itself divisible by i, then i is the next largest prime factor
            if num % i == 0:
                largest_prime_factor = i

    return largest_prime_factor


# print(find_largest_prime_factor(600851475143))


def find_primes(num):
    primes = [2]

    for i in range(3, int(math.sqrt(num)) + 1, 2):
        is_prime = True

        for prime in primes:

            if i % prime == 0:
                is_prime = False
                break

        if is_prime == True:
            primes.append(i)

    return primes


def find_largest_prime_factor(num):
    primes_factors_less_than_sqrt = find_primes(num)
    factorization = []

    while num > 1:
        for prime in primes_factors_less_than_sqrt:
            if num % prime == 0:
                factorization.append(prime)
                num = num / prime

    return factorization


# print(find_primes(600851475143))
print(find_largest_prime_factor(600851475143))
