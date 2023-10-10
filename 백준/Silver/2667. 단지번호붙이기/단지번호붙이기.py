from collections import deque
# 상, 하, 좌, 우
go = [[-1,0],[1,0],[0,-1],[0,1]]

n = int(input())
visited = [[False for _ in range(n)] for _ in range(n)]

ans_list = []

my_map = []
for _ in range(n):
    str = input()
    row = [int(s) for s in str]
    my_map.append(row)

global sum

def dfs(i,j):
    global sum
    for g in go:
        row = i + g[0]
        col = j + g[1]
        if 0 <= row < n and 0 <= col < n and not visited[row][col]:
            visited[row][col] = True
            if my_map[row][col] == 1:
                dfs(row,col)
                sum += 1

# 단지 수
dan = 0
for i in range(n):
    for j in range(n):
        if my_map[i][j] == 1 and not visited[i][j]:
            dan += 1
            sum = 1
            visited[i][j] = True
            dfs(i,j)
            ans_list.append(sum)

print(dan)
for i in sorted(ans_list):
    print(i)