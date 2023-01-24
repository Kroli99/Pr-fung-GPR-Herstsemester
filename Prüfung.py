#2 a)
#lst = [x for x in range(n) if x % 3 == 0]

#2 b)
#lst = [x**3 for x in range(n)]

def is_prime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

#3 a)
def next_prime(n):
    n = n + 1
    while is_prime(n) == False:
        n = n + 1
    return n

print(next_prime(37))

#3 b)
def prime_dist(start, dist):
    if is_prime(start) == False:
        first_prime = next_prime(start)
        second_prime = next_prime(first_prime)
    else:
        first_prime = start
        second_prime = next_prime(first_prime)
    while second_prime - first_prime < dist and second_prime < 10 * start:
        first_prime = next_prime(first_prime)
        second_prime = next_prime(second_prime)
    return first_prime, second_prime

print(prime_dist(3, 6))
