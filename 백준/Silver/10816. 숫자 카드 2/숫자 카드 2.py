import sys

input = sys.stdin.readline

a = int(input())
dic = {}
li = list(map(int, input().split()))
b = int(input())
li1 = list(map(int, input().split()))
for i in li1:
    dic[i] = 0

for i in li:
    if i in dic:
        dic[i] += 1

for i in li1:
    print(dic[i], end=' ')