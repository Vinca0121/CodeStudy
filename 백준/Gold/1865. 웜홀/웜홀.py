import sys

input = sys.stdin.readline
t = int(input().rstrip())

def bellman():
    cycle = False
    for i in range(n):
        for sn, en, weight in graph:
            if dis[sn] != float('inf') and dis[en] > dis[sn] + weight:
                dis[en] = dis[sn] + weight
                if i == n - 1:
                    cycle = True
    return cycle

for _ in range(t):
    n, m, w = map(int, input().rstrip().split())
    graph = []
    dis = [0] * (n + 1)

    for _ in range(m):
        sn, en, weight = map(int, input().rstrip().split())
        graph.append((sn, en, weight))
        graph.append((en, sn, weight))

    for _ in range(w):
        sn, en, weight = map(int, input().rstrip().split())
        graph.append((sn, en, -weight))

    cycle = bellman()
    print("YES" if cycle else "NO")