from collections import deque

def search(my_que, garo, sero, h, visited):
    global day
    # 다음 날짜 번지에 들어갈 애들을 추가
    while my_que :
        next_que = deque()
        # 현재 날짜의 큐에 있는 애들을 싹 다 뺌
        while my_que:
            i, j, k = my_que.popleft()
            for go in golist:
                dep = i + go[0]
                row = j + go[1]
                col = k + go[2]
                if 0 <= dep < h and 0 <= row < sero and  0 <= col < garo and not visited[dep][row][col]:
                    visited[dep][row][col] = True
                    if dim3_map[dep][row][col] == 0:
                        dim3_map[dep][row][col] = 1
                        # 다음 큐에다가 추가
                        next_que.append((dep, row, col))
        # 현재 큐를 다 빼면 1일 추가
        day += 1

        # 다음 날짜 큐가 있다면, 다음 큐를 실행함
        if len(next_que) > 0:
            my_que = next_que

    # 다음 큐가 존재하지 않는다면 칠해진 곳이 없는지 판단
    for dim2 in dim3_map:
        for dim1 in dim2:
            if 0 in dim1:
                return -1

    # 날짜를 반환
    return day


# 높이/행/열
golist = [[-1, 0, 0], [1, 0, 0], [0, -1, 0], [0, 1, 0], [0, 0, -1], [0, 0, 1]]
garo, sero, h = map(int, input().split())

all_clear = True
global day
day = -1

dim3_map = []
for i in range(h):
    dim2_map = []
    for j in range(sero):
        dim1_map = list(map(int, input().split()))
        dim2_map.append(dim1_map)
        if 0 in dim1_map:
            all_clear = False
    dim3_map.append(dim2_map)

visited = [[[False for _ in range(garo)] for _ in range(sero)] for _ in range(h)]
my_que = deque()


# 초기값 세팅 (시작 지점 세팅)
for i in range(h):
    for j in range(sero):
        for k in range(garo):
            if dim3_map[i][j][k] == 1:
                # 높이, 세로, 가로
                my_que.append((i,j,k))
                visited[i][j][k] = True


if all_clear:
    print(0)
else:
    print(search(my_que, garo, sero, h, visited))
