n = int(input())  # 계단의 개수


stairs = []
for i in range(n):
    stairs.append(int(input()))
def max_score(stairs):
    if len(stairs) == 1:
        return stairs[0]
    elif len(stairs) == 2:
        return stairs[0] + stairs[1]
    else:
        dp = [0]*len(stairs)
        dp[0] = stairs[0]
        dp[1] = stairs[0] + stairs[1]
        dp[2] = max(stairs[1] + stairs[2], stairs[0] + stairs[2])
        for i in range(3, len(stairs)):
            dp[i] = max(dp[i-3] + stairs[i-1] + stairs[i], dp[i-2] + stairs[i])
        return dp[-1]


print(max_score(stairs))