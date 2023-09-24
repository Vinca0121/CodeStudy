from collections import deque

garo, sero = map(int, input().split())

my_map = []
visited = []
my_que = deque()
for i in range(sero):
    my_map.append(list(map(int, input().split())))
    visited.append([False] * garo)

def find_date(my_map):
    date = 0
    # 맵 전체를 돌면서 1 인경우를 찾고, 1의 상하좌우 배추의 좌표를 큐에 추가한다. 이것이 1일차이다.
    # 이미 기존 익은 배츄이거나 자리를 쓸 수 없는 경우 추가하지 않는다. 하지만 점검했으므로 visited에는 추가한다.
    for i in range(sero):
        for j in range(garo):
            if my_map[i][j] == 1:
                visited[i][j] = True
                # 상
                if 0 <= i - 1 < sero and 0 <= j < garo:
                    visited[i - 1][j] = True
                    if my_map[i - 1][j] == 0:
                        my_que.appendleft((i - 1, j))
                # 하
                if 0 <= i + 1 < sero and 0 <= j < garo:
                    visited[i + 1][j] = True
                    if my_map[i + 1][j] == 0:
                        my_que.appendleft((i + 1, j))
                # 좌
                if 0 <= i < sero and 0 <= j - 1 < garo:
                    visited[i][j - 1] = True
                    if my_map[i][j - 1] == 0:
                        my_que.appendleft((i, j - 1))
                # 우
                if 0 <= i < sero and 0 <= j + 1 < garo:
                    visited[i][j + 1] = True
                    if my_map[i][j + 1] == 0:
                        my_que.appendleft((i, j + 1))
    date += 1

    # 2일차.
    # 큐에 새로운 배츄 좌표가 있다면, 모든 좌표를 꺼내서 검사한다.
    while my_que:
        temp_list = list(my_que)
        my_que.clear()
        for i, j in temp_list:
            my_map[i][j] = 1
            # 해당 배츄의 상하좌우를 검사하여 배츄(0)이라면 이를 큐에 넣는다.
            # 이 때, 검사된 배츄는 방문하지 않은 경우만 해당된다.
            # 실제 맵 또한 변경한다.
            # 상
            if 0 <= i - 1 < sero and 0 <= j < garo:
                if not visited[i - 1][j] and my_map[i - 1][j] == 0:
                    visited[i - 1][j] = True
                    my_que.appendleft((i - 1, j))
                    my_map[i-1][j] = 1
            # 하
            if 0 <= i + 1 < sero and 0 <= j < garo:
                if not visited[i + 1][j] and my_map[i + 1][j] == 0:
                    visited[i + 1][j] = True
                    my_que.appendleft((i + 1, j))
                    my_map[i + 1][j] = 1
            # 좌
            if 0 <= i < sero and 0 <= j - 1 < garo:
                if not visited[i][j-1] and my_map[i][j - 1] == 0:
                    visited[i][j-1] = True
                    my_que.appendleft((i, j - 1))
                    my_map[i][j-1] = 1
            # 우
            if 0 <= i < sero and 0 <= j + 1 < garo:
                if not visited[i][j+1] and my_map[i][j + 1] == 0:
                    visited[i][j+1] = True
                    my_que.appendleft((i, j + 1))
                    my_map[i][j+1] = 1
        # 2일차가 끝
        date += 1
        # n일차를 반복한다.
    return date

date = find_date(my_map)

# 반복문을 탈출했으나, 배열 내 0의 값이 있는 경우
if 0 in (tomato for row in my_map for tomato in row):
    print(-1)

else:
    print(date-1)


