import sys
input = sys.stdin.readline

my_n = int(input())
my_list = list(map(int, input().split()))

ans_n = int(input())
ans_list = list(map(int, input().split()))

dic = {}

for i in my_list:
    if i in dic :
        dic[i] += 1
    else :
        dic[i] = 1

for i in ans_list:
    if i in dic :
        print(dic[i], end=" ")
    else:
        print(0, end=" ")