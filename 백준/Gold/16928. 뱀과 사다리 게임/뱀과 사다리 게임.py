from collections import deque

def bfs(my_map):
    visited = [False] * 101  # 방문 여부를 저장할 리스트
    visited[1] = True
    queue = deque()
    queue.append((1, 0))  # 시작 위치와 주사위 횟수

    while queue:
        current_position, roll = queue.popleft()
        # 주사위 눈(1부터 6)에 대해 이동을 탐색
        for dice in range(1, 7):
            new_position = current_position + dice
            # 목적지(100)에 도달하면 종료
            if new_position == 100:
                return roll + 1

            if new_position < 100:
                # 뱀 또는 사다리 위치로 이동
                if my_map[new_position] != 0:
                    new_position = my_map[new_position]

                if not visited[new_position]:
                    visited[new_position] = True
                    queue.append((new_position, roll + 1))

ladder, snake = map(int, input().split())
my_map = [0] * 101

for _ in range(ladder + snake):
    start, end = map(int, input().split())
    my_map[start] = end

print(bfs(my_map))  # BFS를 호출하여 최단 경로를 찾음
