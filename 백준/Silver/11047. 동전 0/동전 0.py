# 동전 수 n, 정답 k
n, k = map(int, input().split())

# 동전
coins = []
for i in range(n):
    coins.append(int(input()))

# 동전을 내림차순으로 정렬
coins.sort(reverse=True)

# 필요한 동전 개수 계산
count = 0
for coin in coins:
    if k >= coin:
        count += k // coin
        k %= coin

print(count)
