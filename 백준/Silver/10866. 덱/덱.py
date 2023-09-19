from collections import deque
import sys
input = sys.stdin.readline
t = int(input())


my_deque = []

for i in range(t):
    str = input().split()
    case = str[0]
    if case == 'push_front':
        my_deque = [str[1]] + my_deque

    elif case == 'push_back':
        my_deque = my_deque + [str[1]]

    elif case == 'pop_front':
        if(len(my_deque) == 0):
            print(-1)
        else :
            print(my_deque[0])
            del my_deque[0]

    elif case == 'pop_back':
        if(len(my_deque) == 0):
            print(-1)
        else :
            print(my_deque[-1])
            del my_deque[-1]

    elif case == 'front':
        if(len(my_deque) == 0):
            print(-1)
        else:
            print(my_deque[0])

    elif case == 'back':
        if(len(my_deque) == 0):
            print(-1)
        else:
            print(my_deque[-1])

    elif case == 'size':
        print(len(my_deque))

    elif case == 'empty':
        if (len(my_deque) == 0):
            print(1)
        else:
            print(0)

