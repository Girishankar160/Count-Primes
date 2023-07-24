def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return
    return True

def prime_count(n):
    count = 0
    for num in range(2, n):
        if is_prime(num):
            count += 1
    return count
print(prime_count(int(input())))