n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    up = 1
    for i in range(a):
        up *= b
        b -= 1
    low = 1
    for i in range(1, a+1):
        low *= i

    print(up//low)