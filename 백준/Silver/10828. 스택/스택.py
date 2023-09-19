import sys
input = sys.stdin.readline
t = int(input())

my_stack = []
for i in range(t):
    str = input().split()
    case = str[0]
    if case == 'push':
        my_stack = [str[1]]+ my_stack

    elif case == 'pop':
        if(len(my_stack) == 0):
            print(-1)
        else :
            print(my_stack.pop(0))

    elif case == 'top':
        if(len(my_stack) == 0):
            print(-1)
        else:
            print(my_stack[0])

    elif case == 'size':
        print(len(my_stack))

    elif case == 'empty':
        if (len(my_stack) == 0):
            print(1)
        else:
            print(0)

