import sys
input = sys.stdin.readline
n, k = map(int, input().split())

n_list = [i+1 for i in range(n)]

ans = []
while len(n_list) >= k:
    # k번째 값 찾기
    ans.append(n_list[k-1])
    # k번째 값 이후 부터를 앞으로 보냄
    n_list = n_list[k:] + n_list[:k-1]
    # 맨 뒤에꺼 삭제    del n_list[-1]

for i in range(len(n_list)):
    p = k % len(n_list)
    if p>0:
        ans.append(n_list[p-1])
        n_list = n_list[p:] + n_list[:p-1]
    else :
        ans.append(n_list[-1])
        n_list = n_list[:-1]

    # 뒤에 남은 거 다 추가 (수정필요)
print('<', end="")
for i in range(len(ans) -1):
    print(ans[i], end=", ")
print(ans[-1], end="")
print('>', end=" ")
