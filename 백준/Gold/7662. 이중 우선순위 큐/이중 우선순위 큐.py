import heapq
import sys
input = sys.stdin.readline
t = int(input().rstrip())

for _ in range(t):
    oper_len = int(input())
    my_heap_min = []
    my_heap_max = []
    exist = dict()
    for _ in range(oper_len):
        oper, num = map(str, input().rstrip().split())
        num = int(num)
        if oper == "I":
            heapq.heappush(my_heap_min, num)
            heapq.heappush(my_heap_max, -num)
            if num in exist:
                exist[num] += 1
            else:
                exist[num] = 1

        elif oper == "D":
            if num == -1:
                while my_heap_min and exist[my_heap_min[0]] == 0:
                    heapq.heappop(my_heap_min)
                if my_heap_min:
                    exist[my_heap_min[0]] -= 1
                    heapq.heappop(my_heap_min)
            elif num == 1:
                while my_heap_max and exist[-my_heap_max[0]] == 0:
                    heapq.heappop(my_heap_max)
                if my_heap_max:
                    exist[-my_heap_max[0]] -= 1
                    heapq.heappop(my_heap_max)

    while my_heap_min and exist[my_heap_min[0]] == 0:
        heapq.heappop(my_heap_min)
    while my_heap_max and exist[-my_heap_max[0]] == 0:
        heapq.heappop(my_heap_max)

    if my_heap_min and my_heap_max:
        print("{0} {1}".format(-heapq.heappop(my_heap_max), heapq.heappop(my_heap_min)))
    else:
        print("EMPTY")
