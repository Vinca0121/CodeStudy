import sys
sys.setrecursionlimit(10**6)
def dfs(start, length):
    # 만약 마지막까지 도달했다면

    # 깊이 우선 탐색 수행
    # print(start, length)
    for en, w in graph[start]:
        # 방문 체크
        if not visited[en]:
            visited[en] = True
            dfs(en, length+w)
    # 마지막에 도달한 경우
    if end_node[1] < length:
        end_node[0] = start
        end_node[1] = length

n = int(input())

graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
for _ in range(n-1):
    sn, en, w = map(int, input().split())
    graph[sn].append((en,w))
    graph[en].append((sn,w))


#  종료노드, 종료 값
end_node = [-1, -float('inf')]
# 1을 시작으로하여 종료 노드가 어딘지 저장함
visited[1] = True
dfs(1, 0)

# print("종료 : ",end_node)
# 구해진 종료 노드를 통해서 구함
end_node[1] = -float('inf')
visited = [False for _ in range(n+1)]
visited[end_node[0]] = True
dfs(end_node[0], 0)

# print("종료2차 : ",end_node)
print(end_node[1])