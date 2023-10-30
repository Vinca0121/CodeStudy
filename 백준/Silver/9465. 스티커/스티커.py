def max_sticker_score(n, stickers):
    dp = [[0 for _ in range(n)] for _ in range(2)]
    dp[0][0] = stickers[0][0]
    dp[1][0] = stickers[1][0]

    for i in range(1, n):
        dp[0][i] = max(dp[1][i - 1] + stickers[0][i], dp[0][i - 1])
        dp[1][i] = max(dp[0][i - 1] + stickers[1][i], dp[1][i - 1])

    return max(dp[0][n - 1], dp[1][n - 1])

# 입력 처리 및 결과 출력
t = int(input())  # 테스트 케이스의 수
for _ in range(t):
    n = int(input())  # 스티커 열의 수
    stickers = [list(map(int, input().split())) for _ in range(2)]
    result = max_sticker_score(n, stickers)
    print(result)