import sys
from collections import deque
input = sys.stdin.readline


def search(start, end):
    mim_visit = [0] * 200001
    visited = [False] * 200001
    my_q.appendleft(start)
    visited[start] = True

    while my_q:
        place = my_q.pop()
        if place == end :
            return mim_visit[place]

        for new_place in [place * 2, place -1, place +1]:
            if 0 <= new_place <= 100000 and not visited[new_place]:
                my_q.appendleft(new_place)
                mim_visit[new_place] = mim_visit[place] +1
                visited[new_place] = True

# 시작 숫자 start, 도착 숫자 end
start, end = map(int, input().split())
my_q = deque()
print(search(start, end))