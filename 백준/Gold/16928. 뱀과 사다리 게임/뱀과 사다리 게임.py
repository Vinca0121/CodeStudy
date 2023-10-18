from collections import deque
ladder, snake = map(int, input().split())

# 전체 범위
my_map = [0] * 101
# 순간 이동 위치를 지정
for _ in range(ladder):
    start, end = map(int, input().split())
    my_map[start] = end

for _ in range(snake):
    start, end = map(int, input().split())
    my_map[start] = end

# 방문 여부 표시
visited = [False] * 101
queue = deque()
# 시작 위치 (0,0)
queue.append((1,0))
visited[1] = True

def bfs():
    while queue:
        current_position, roll = queue.popleft()
        # 1~6 주사위에 대한 값에 대해서 수행
        for dice in range(1, 7):
            new_position = current_position + dice
            # 목적지(100)에 도달하면 종료
            if new_position == 100:
                return roll+1
            # 목적지보다 적은 경우만 갈 수 있음
            elif new_position < 100:

                # 목적지에 순간이동 포탈이 있는 경우.
                if my_map[new_position] != 0 and not visited[new_position]:
                    visited[new_position] = True
                    new_position = my_map[new_position]
                    visited[new_position] = True
                    queue.append((new_position, roll + 1))

                # 목적지가 일반 발판인 경우
                elif my_map[new_position] == 0 and not visited[new_position]:
                    # 새로운 포지션으로 도착했으므로 방문을 True로 설정
                    visited[new_position] = True
                    queue.append((new_position, roll + 1))


print(bfs())  # BFS를 호출하여 최단 경로를 찾음
