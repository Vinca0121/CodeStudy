from collections import deque
go = [[-1,0],[1,0],[0,-1],[0,1]]
sero, garo = map(int,input().split())
my_map = []

p = (-1,-1)
for i in range(sero):
    row = list(input())
    if 'I' in row :
        p = (i,row.index('I'))
    my_map.append(row)


visited = [[False for _ in range(garo)] for _ in range(sero)]
my_que = deque()
my_que.append(p)
visited[p[0]][p[1]] = True
ans = 0
while my_que:
    i, j = my_que.popleft()
    for g in go:
        r = i + g[0]
        c = j + g[1]
        if 0 <= r < sero and 0 <= c < garo and not visited[r][c]:
            visited[r][c] = True
            if my_map[r][c] == 'O':
                my_que.append((r,c))
            elif my_map[r][c] == 'P':
                my_que.append((r,c))
                ans += 1

if ans > 0:
    print(ans)
else:
    print('TT')