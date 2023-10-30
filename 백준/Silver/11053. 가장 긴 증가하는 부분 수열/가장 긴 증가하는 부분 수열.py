n = int(input())
numbers = list(map(int, input().split()))
dp = [1] * n

# 시작 지점을 모든 곳으로 잡는다.
for i in range(n):
    # 자신의 시작 지점 보다 뒤를 비교한다.
    for j in range(i):
         # 만약 dp[i] 번째의 값이 해당 뒤에있는 숫자보다 큰 경우
         if numbers[i] > numbers[j]:
             # dp의 값을 갱신 (현재 dp의 값 vs 뒤에 있는 숫자의 dp 값 + 해당 숫자를 포함하는 값(+1)
             dp[i] = max(dp[i], dp[j]+1)

# 각 숫자에 대한 dp가 저장됨
print(max(dp))
