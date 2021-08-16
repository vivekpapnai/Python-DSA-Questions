def spclTrip(n):
    count = 0
    for c in range(1, n + 1):
        for b in range(c, n + 1, c):
            if b%c == 0:
                for a in range(c, n + 1, b):
                    if a % b == c:
                        count += 1

    return count


t = int(input())
for i in range(t):
    n = int(input())
    print(spclTrip(n))
