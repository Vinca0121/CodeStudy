n, m = map(int, input().split())

# 순서를 고려하지 않으므로 stack을 사용한다.
my_stack = []
visited = [False] * (n)
my_list =  sorted(list(map(int, input().split())))


def printer():
    for s in my_stack:
        print(s,end=" ")
    print()
def dfs(count):
    if count == m:
        printer()
        return
    # 모든 값에 대해서 반복하며 3개를 만듬
    for i in range(n):
        # 방문하지 않았다면
        if not visited[i]:
            visited[i] = True
            my_stack.append(my_list[i])
            dfs(count + 1)
            my_stack.pop()
            visited[i] = False


# 어차피..다 돌아야하므로 필요없다
dfs(0)

