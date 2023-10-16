n, k = map(int, input().split())
w = []  # Weight
v = []  # Value

for _ in range(n):
    weight, value = map(int, input().split())
    w.append(weight)
    v.append(value)

dp = [0] * (k + 1)

for i in range(n):
    for j in range(k, 0, -1):
        if w[i] <= j:
            dp[j] = max(dp[j], dp[j - w[i]] + v[i])

print(dp[k])
