import heapq
import sys

input = sys.stdin.readline
n = int(input().rstrip())

abs_heap = []

for _ in range(n):
    num = int(input().rstrip())
    if num == 0:
        if len(abs_heap) > 0:
            _, result = heapq.heappop(abs_heap)
            print(result)
        else:
            print(0)
    else:
        heapq.heappush(abs_heap, (abs(num), num))
