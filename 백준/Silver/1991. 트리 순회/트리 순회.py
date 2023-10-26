n = int(input())
dic = {}
for _ in range(n):
    s, n1, n2 = map(str, input().split())
    dic[s] = [n1,n2]

global ans
ans = ""
def f_visited(start):
    global ans
    # 중간을 먼저 방문한다.
    ans = ans + start
    # 이후 왼쪽을 방문한다.
    left = dic[start][0]
    if left != '.':
        f_visited(left)

    # 이후 오른쪽을 방문한다.
    right = dic[start][1]
    if right != '.':
        f_visited(right)

def m_visited(start):
    global ans
    # 왼쪽을 먼저 방문한다.
    left = dic[start][0]
    if left != '.':
        m_visited(left)
    # 중간을 방문한다.
    ans = ans + start
    # 이후 오른쪽을 방문한다.
    right = dic[start][1]
    if right != '.':
        m_visited(right)
def l_visited(start):
    global ans
    # 왼쪽을 먼저 방문한다.
    left = dic[start][0]
    if left != '.':
        l_visited(left)

    # 이후 오른쪽을 방문한다.
    right = dic[start][1]
    if right != '.':
        l_visited(right)

    # 중간을 방문한다.
    ans = ans + start

f_visited('A')
ans = ans +"\n"
m_visited('A')
ans = ans +"\n"
l_visited('A')
print(ans)