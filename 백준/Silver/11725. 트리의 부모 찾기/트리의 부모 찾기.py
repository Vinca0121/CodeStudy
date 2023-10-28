import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(start):
    # 1을 기준으로 dfs를 수행하며 각 루트노드(이전 노드)를 기록한다.
    for node in my_graph[start]:
        # 방문하지 않았다면 0
        if parents[node] == 0 :
            # 부모 노드는 현재 노드가 된다.
            parents[node] = start
            # 해당 노드로 또 수행
            dfs(node)
            
n = int(input().rstrip())

my_graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    s, e = map(int, input().rstrip().split())
    my_graph[s].append(e)
    my_graph[e].append(s)

parents = [0] * (n+1)

dfs(1)

for i in parents[2:]:
    print(i)