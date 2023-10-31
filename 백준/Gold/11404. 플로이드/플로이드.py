import sys
input = sys.stdin.readline
node = int(input().rstrip())
my_map = [[0 for _ in range(node+1)] for _ in range(node+1)]

for _ in range(int(input().rstrip())):
    # 버스는 단방향 그래프이다.
    s, e, w = map(int, input().rstrip().split())
    # 더 짧은 값이 들어오면 더 짧은 값으로 갱신
    # 현재 길이 없는 경우
    if my_map[s][e] == 0:
        my_map[s][e] = w
    # 현재 길에 이미 값이 있는 경우
    else:
        my_map[s][e] = min(my_map[s][e], w)

# 플로이드 워셜 진행
# 전체 노드에 대해서 반복(해당 노드가 중심이 되는 경우 업데이트)
for mid in range(1, node+1):
    # 중심 노드를 두고, 전체 노드를 반복하며 알고리즘을 업데이트 한다
    for i in range(1, node+1):
        for j in range(1, node+1):
            if i!=j and my_map[i][mid] != 0 and my_map[mid][j] !=0:
                # 현재 갈 수 있는 방법이 정해지지 않은 경우
                if my_map[i][j] == 0:
                    my_map[i][j] = my_map[i][mid] + my_map[mid][j]
                # 현재 노드를 통해서 가는 경우가 기존 가는 방법보다 더 적은 거리로 갈 수 있다면.
                else:
                    my_map[i][j] = min(my_map[i][j], my_map[i][mid] + my_map[mid][j])

for i in my_map[1:]:
    print(*i[1:])