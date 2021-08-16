import math


def is_prime(n):
    if n <= 1:
        return False

    max_div = math.floor(math.sqrt(n))
    for i in range(2, 1 + max_div):
        if n % i == 0:
            return False
    return True


def Secret_Code(z):
    # prime_numbers = Get_Prime(z)
    li = [2]
    j = 0
    for i in range(3, n):
        if is_prime(i):
            li.append(i)
            x = li[j] * li[j + 1]
            j += 1
            if x > z:
                x = x_prev
                break
            x_prev = x
    return x


t = int(input())
for i in range(1, t + 1):
    n = int(input())
    print("Case #", i, sep="", end=": ")
    print(Secret_Code(n))
