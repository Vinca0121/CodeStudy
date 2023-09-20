from collections import deque

# 상하좌우 이동 좌표
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 배추 밭을 탐색하여 그룹 형성 함수
def find_group(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    group = 1

    while queue:
        cx, cy = queue.popleft()

        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and field[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = True
                group += 1

    return group

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    for _ in range(K):
        X, Y = map(int, input().split())
        field[Y][X] = 1

    white_worms = 0
    for i in range(N):
        for j in range(M):
            if field[i][j] == 1 and not visited[i][j]:
                white_worms += 1
                find_group(i, j)

    print(white_worms)