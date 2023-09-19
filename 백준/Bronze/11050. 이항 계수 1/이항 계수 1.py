n, k = map(int, input().split())


son = mom = 1
for _ in range(k):
    son = son * n
    n -= 1

while k > 0:
    mom = mom * k
    k -= 1
print(son//mom)