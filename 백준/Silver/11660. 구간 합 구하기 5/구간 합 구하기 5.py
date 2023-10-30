import sys
input = sys.stdin.readline
row, t = map(int, input().rstrip().split())

my_map = [list(map(int, input().rstrip().split())) for _ in range(row)]
stack_sum = [[0 for _ in range(row+1)] for _ in range(row)]

# 누적합을 채운다.
for i in range(row):
    for j in range(row):
        stack_sum[i][j+1] = stack_sum[i][j] + my_map[i][j]
for _ in range(t):
    #      0     1        2   3
    # 시작 row, col / 종료 row, col
    case = list(map(int, input().rstrip().split()))

    # 행 만큼 반복
    summery = 0
    for i in range(case[2]-case[0]+1):
        #  열을 전부 더한다.
        summery += stack_sum[case[0]-1+i][case[3]] - stack_sum[case[0]-1+i][case[1]-1]
    print(summery)
