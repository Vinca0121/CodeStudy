import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    while my_que:
        r, c = my_que.popleft()
        # 정답으로부터의 거리
        ans_len = ans_list[r][c]
        # 상
        if 0 <= r-1 < sero and 0 <= c < garo and not visited[r-1][c]:
            visited[r-1][c] = True
            if my_map[r-1][c] == 1:
                ans_list[r-1][c] = ans_len + 1
                # 큐에 넣어줌
                my_que.append([r-1, c])
        # 하
        if 0 <= r+1 < sero and 0 <= c < garo and not visited[r+1][c]:
            visited[r+1][c] = True
            if my_map[r + 1][c] == 1:
                ans_list[r + 1][c] = ans_len + 1
                my_que.append([r+1, c])
        # 좌
        if 0 <= r < sero and 0 <= c-1 < garo and not visited[r][c-1]:
            visited[r][c-1] = True
            if my_map[r][c-1] == 1:
                ans_list[r][c-1] = ans_len + 1
                my_que.append([r, c-1])
        # 우
        if 0 <= r < sero and 0 <= c+1 < garo and not visited[r][c+1]:
            visited[r][c+1] = True
            if my_map[r][c+1] == 1:
                ans_list[r][c+1] = ans_len + 1
                my_que.append([r, c+1])


# 세로, 가로
sero, garo = map(int, input().rstrip().split())

# 최단거리 리스트 -> 도달할 수 없는 곳은 -1로 고정
ans_list = [[-1] * garo for i in range(sero)]

# 방문여부 리스트
visited = [[False] * garo for i in range(sero)]


# 맵을 입력 받으면서, 시작지점의 좌표룰 찾음
start_r_idx = start_c_idx = -1
my_map = []
for i in range(sero):
    one_row = list(map(int, input().rstrip().split()))
    # 시작 지점의 좌표를 아직 찾지 못한 경우
    if start_c_idx == -1:
        try:
            # 시작 지점의 좌표를 저장
            start_c_idx = one_row.index(2)
            start_r_idx = i
        except:
            pass
    my_map.append(one_row)

# 큐 생성
my_que = deque()
# 시작 지점의 좌표를 넣음
my_que.append([start_r_idx, start_c_idx])
# 방문 했음을 표시
visited[start_r_idx][start_c_idx] = True
# 시작 지점의 거리는 0
ans_list[start_r_idx][start_c_idx] = 0

# 방문 시작
bfs()

# 거리가 표시된 정답 리스트에 갈 수 없는 땅 0을 채워 넣음.
for i in range(sero):
    for j in range(garo):
        if my_map[i][j] == 0 :
            ans_list[i][j] = 0

# 정답 출력 (맨 끝 공백 처리)
for i in range(sero):
    print(*ans_list[i])

