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
    if is_prime(n) == True:
        n = n + 1
    while is_prime(n) != True:
        n = n + 1
    return n

print(next_prime(37))

#3 b)
def prime_dist(start, dist):
    new_prime = 0
    if is_prime(start) == True:
        new_prime = next_prime(start)
        if new_prime - start < dist and new_prime < 10 * start:
            new_prime = next_prime(new_prime)
        elif new_prime - start >= dist:
            return (start, new_prime)

print(prime_dist(3, 6))