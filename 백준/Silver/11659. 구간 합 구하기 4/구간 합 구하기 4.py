import sys
input = sys.stdin.readline

n_list = []
# 숫자의 개수 n, 연산의 횟수 3
n, t = map(int,input().split())

n_list = list(map(int, input().split()))

# 1 부터 3까지의 합 저장
# 2부터 4번까지으 합 저장

ans_list = [0] * (n+1)

# n까지의 합을 저장
for i in range(n):
    ans_list[i+1] = ans_list[i] + n_list[i]


for _ in range(t):
    n1, n2 = map(int, input().split())
    print(ans_list[n2] - ans_list[n1-1])