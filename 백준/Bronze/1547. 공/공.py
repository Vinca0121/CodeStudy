n = int(input())

master = 1
for _ in range(n):
    a, b = map(int, input().split())
    if a == master :
        master = b
    elif b == master:
        master = a
print(master)
