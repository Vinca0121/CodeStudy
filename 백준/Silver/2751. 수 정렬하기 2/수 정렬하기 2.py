import sys
input = sys.stdin.readline
n = int(input())

l = []
for i in range(n):
    l.append(int(input()))

l.sort()
l = list(str(i) for i in l)

sys.stdout.write("\n".join(l))