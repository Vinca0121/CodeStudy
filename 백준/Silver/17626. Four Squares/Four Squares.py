def min_square_sums(n):
    dp = [0] + [float('inf')] * n

    squares = [i**2 for i in range(1, int(n**0.5)+1)]

    for i in range(1, n+1):
        for square in squares:
            if square > i:
                break
            dp[i] = min(dp[i], dp[i-square] + 1)

    return dp[n]

n = int(input())
print(min_square_sums(n))