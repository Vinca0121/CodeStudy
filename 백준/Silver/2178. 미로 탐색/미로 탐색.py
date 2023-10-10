from collections import deque
# 상, 하, 좌, 우
go = [[-1,0],[1,0],[0,-1],[0,1]]

# 행, 열
n, m = map(int, input().split())
visited = [[False for _ in range(m)] for _ in range(n)]

my_map = []
for i in range(n):
    str = input()
    one_row = [int(s) for s in str]
    my_map.append(one_row)

my_que = deque()
def bfs(my_map):
    while my_que :
        r, c = my_que.popleft()
        # 큐에 연관된 애들을 추가
        # 현재 큐에 연관된 애들에 대해서 모두 반복함
        # 상하좌우 애들이 정상적으로 있다면 (벗어나지 않았다면)
        for i in go:
            row = r + i[0]
            col = c+ i[1]
            if 0 <= row < len(my_map) and 0 <= col < len(my_map[0]) and not visited[row][col]:
                # visited 표시도 해줌
                visited[row][col] = True
                # 상하좌우 애들 중 1이 나오는 애들이 있다면
                if my_map[row][col] ==  1:
                    # 상하좌우 연관된 애들을 값을 기존 값 +1 해줌
                    my_map[row][col] = my_map[r][c] + 1
                    # 상하좌우를 큐에 넣음
                    my_que.append((row,col))


visited[0][0] = True
my_que.append((0,0))
bfs(my_map)
print(my_map[n-1][m-1])
