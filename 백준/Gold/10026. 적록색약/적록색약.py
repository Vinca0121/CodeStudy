import sys
sys.setrecursionlimit(10**6)
# 상하좌우 갈 수 있는 경로
go = [[-1,0], [1,0], [0,-1], [0,1]]
def dfs(my_map, i, j):
    # 내 상하좌우의 애들을 비교함. 만일 같은 색상인 경우 visited로 체크하고 재귀를 호출함
    color = my_map[i][j]
    for g in go:
        ni = i + g[0]
        nj = j + g[1]
        if 0 <= ni < len(my_map) and 0 <= nj < len(my_map[0]) and not visited[ni][nj] and my_map[ni][nj] == color:
            visited[ni][nj] = True
            dfs(my_map, ni, nj)

n = int(input())

# 색약이 아닌 경우
my_map_F = []
# 색약인 경우
my_map_T = []
for _ in range(n):
    row = list(input())
    my_map_F.append(row)
    # R면 G로 변경 아닌 경우, 그대로 씀 (적 == 녹)
    row_T = ['G' if i == 'R' else i for i in row]
    my_map_T.append(row_T)

visited = [[False for _ in range(len(my_map_T[0]) + 1)] for _ in range(len(my_map_T) + 1)]

# 한 dfs가 완전히 종료되면 case가 1증가한 것임
case = 0
for i in range(len(my_map_T)):
    for j in range(len(my_map_T[0])):
        if not visited[i][j]:
            visited[i][j] = True
            dfs(my_map_F,i,j)
            case += 1

print(case, end=" ")

visited = [[False for _ in range(len(my_map_T[0]) + 1)] for _ in range(len(my_map_T) + 1)]

# 한 dfs가 완전히 종료되면 case가 1증가한 것임
case = 0
for i in range(len(my_map_T)):
    for j in range(len(my_map_T[0])):
        if not visited[i][j]:
            visited[i][j] = True
            dfs(my_map_T,i,j)
            case += 1
print(case)