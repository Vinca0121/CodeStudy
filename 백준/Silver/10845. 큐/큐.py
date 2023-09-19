import sys
input = sys.stdin.readline
t = int(input())

my_queue = []
for i in range(t):
    str = input().split()
    case = str[0]
    if case == 'push':
        my_queue = [str[1]] + my_queue

    elif case == 'pop':
        if(len(my_queue) == 0):
            print(-1)
        else :
            print(my_queue[-1])
            del my_queue[-1]

    elif case == 'front':
        if(len(my_queue) == 0):
            print(-1)
        else:
            print(my_queue[-1])

    elif case == 'back':
        if(len(my_queue) == 0):
            print(-1)
        else:
            print(my_queue[0])

    elif case == 'size':
        print(len(my_queue))

    elif case == 'empty':
        if (len(my_queue) == 0):
            print(1)
        else:
            print(0)

