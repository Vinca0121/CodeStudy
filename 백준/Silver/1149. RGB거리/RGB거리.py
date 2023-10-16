n = int(input())

dp = [[float('inf')] * 3 for _ in range(n+1)]

cost_list = [[0,0,0]]

for _ in range(n):
    cost_list.append(list(map(int, input().split())))

dp[1] = cost_list[1]

# 3번째 줄 까지 쭉 간다.
for i in range(2, n+1):
    # 각 순서 3번 만큼 전부 업데이트 시켜준다. R, G, B 시작 각각
    for j in range(3):
        # 업데이트 시키는 방법은 자신을 제외하고, 2번씩 비교한다. (0으로 가는 경우 1, 2만 가능)
        for k in range(3):
            if j != k:
                # 현재 새기의 최소 VS 이전 새기인데 나와 겹치지 않는 이전 새기 2번 + 현재 숫자
                dp[i][j] = min(dp[i][j],  dp[i-1][k] + cost_list[i][j])

# 최종 결과는 마지막 집을 칠한 후의 최소 비용
print(min(dp[n]))