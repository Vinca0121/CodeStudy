import sys
input = sys.stdin.readline
from collections import deque

# 상하좌우 이동 방향 설정
go = [[-1,0],[1,0],[0,-1],[0,1]]
sero, garo = map(int, input().rstrip().split())

visited = [[[0 for _ in range(garo)] for _ in range(sero)] for _ in range(2)]

my_map = []
for _ in range(sero):
    row = [int(s) for s in input().rstrip()]
    my_map.append(row)

my_queue = deque()
def bfs():
    # 큐가 살아있을 때까지 반복한다.
    while my_queue:
        wall, r1, c1 = my_queue.popleft()
        # 최종 목적지에 도착하였다면
        if r1 == sero-1 and c1 == garo-1 :
            return visited[wall][r1][c1]

        for g in go:
            row = r1 + g[0]
            col = c1 + g[1]
            # 벗어나지 않은 경우에만 수행
            if 0 <= row < sero and 0 <= col < garo:
                # 벽을 부수지 않는 경우 (길 + 방문할 수 있는 경우(0) )
                if my_map[row][col] == 0 and visited[wall][row][col] == 0:
                    visited[wall][row][col] = visited[wall][r1][c1] + 1
                    my_queue.append((wall, row, col))

                # 벽을 부수고 이동하는 경우 (벽 + 아직 안 부순 경우)
                if my_map[row][col] == 1 and wall == 0:
                    visited[1][row][col] = visited[0][r1][c1] + 1
                    my_queue.append((1,row,col))
    # 큐를 다 돌았지만 해당 위치로 빠져나가지 못한경우
    return -1
my_queue.append((0,0,0))
visited[0][0][0] = 1
print(bfs())

