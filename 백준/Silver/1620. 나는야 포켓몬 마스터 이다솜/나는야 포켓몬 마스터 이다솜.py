import sys
input = sys.stdin.readline

# 포켓몬 개수 n, 문제의 개수 m
n, m = map(int, input().split())

dic = {}
dic2 = {}
# 포켓몬 등록
for i in range(n):
    poke_name = input().rstrip('\n')
    dic[i+1] = poke_name
    dic2[poke_name] = i+1


for _ in range(m):
    s = input().rstrip('\n')
    if s.isdigit():
        print(dic[int(s)])
    else:
        print(dic2[s])