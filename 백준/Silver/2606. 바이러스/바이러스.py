n = int(input())
connect = int(input())

dic = {}

for i in range(n):
    dic[i + 1] = set()
for i in range(connect):
    a, b = map(int, input().split())
    dic[a].add(b)
    dic[b].add(a)


global infect
infect = 0
def dfs(num, visited):
    global infect
    # 1부터 시작
    if num not in visited:
        visited.add(num)
        infect += 1
        for i in dic[num]:
            dfs(i,visited)


visited = set()
dfs(1, visited)
print(infect-1)
