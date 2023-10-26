n = int(input())
graph = []
dp = [[0] * i for i in range(1, n+1)]
for i in range(n):
    row = list(map(int, input().split()))
    graph.append(row)

# 자신의 기존 인덱스이거나 한칸 더 갈 수 있다.

dp[0][0] = graph[0][0]
# 전체 n 만큼 반복
for i in range(1, n):
    # 해당 행에 있는 숫자 만큼 반복
    for j in range(i+1):
        # 맨 왼쪽에 있는 친구인 경우 부모의 첫번째 값만을 선택 가능하다.
        if j == 0:
            dp[i][j] = dp[i-1][0] + graph[i][j]
        # 맨 오른쪽에 있는 친구의 경우 부모의 맨 마지막 값만 선택 가능.
        elif j == i:
            dp[i][j] = dp[i-1][-1] + graph[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + graph[i][j]

print(max(dp[n-1]))

