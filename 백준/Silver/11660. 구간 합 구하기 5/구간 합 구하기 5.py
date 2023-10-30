import sys

input = sys.stdin.readline

row, t = map(int, input().split())
my_map = [list(map(int, input().split())) for _ in range(row)]

# 누적 합을 계산할 배열 초기화
prefix_sum = [[0] * (row + 1) for _ in range(row)]

for i in range(row):
    for j in range(row):
        prefix_sum[i][j + 1] = prefix_sum[i][j] + my_map[i][j]

for _ in range(t):
    case = list(map(int, input().split()))

    summery = 0
    for i in range(case[0] - 1, case[2]):
        # 누적 합을 활용하여 열의 합을 계산
        summery += prefix_sum[i][case[3]] - prefix_sum[i][case[1] - 1]

    print(summery)
