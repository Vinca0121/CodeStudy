import sys
input = sys.stdin.readline



def vps(s):
    my_stack = []

    for i in s:
        if i == '(':
            my_stack.append(i)
        elif i == ')':
            if len(my_stack) == 0 :
                return "NO"
            my_stack.pop()

    if len(my_stack) == 0:
        return "YES"
    else:
        return "NO"



t = int(input())
for _ in range(t):
    s = input()
    print(vps(s))


