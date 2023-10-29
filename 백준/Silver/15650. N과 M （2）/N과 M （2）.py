n, m = map(int, input().split())

# 출력할 수열이 저장된 리스트
visited = [[0,0]]
# visited에 값을 넣음
for i in range(1, n+1):
    # 숫자, Bool
    visited.append([i,False])

# 정답 값을 찾은 경우 출력
def printer():
    for v in visited[1:]:
        # 방문값이 True라면 출력 (순차적으로 사전순으로 출력된다)
        if v[1]:
            print(v[0], end=" ")
    print("")


# 반복에서 제외 될 인덱스를 포함, 카운터 개수
def dfs(idx, count):
    if count == m:
        printer()
        return 0

    # 인덱스를 제외하고 반복문을 수행하며 찾음
    for i in range(idx, n+1):
        # 해당 숫자를 방문하지 않았다면
        if not visited[i][1]:
            # 출력될 숫자 리스트를 토글하는 부분
            visited[i][1] = True
            # 해당 숫자를 통해서 방문을 수행
            dfs(i, count + 1)
            # 숫자의 방문이 종료된 경우 -> 다시 해당 숫자를 다른 곳에서 쓸 수 있도록 해줌
            visited[i][1] = False




dfs(1,0)

