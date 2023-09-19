import sys
input = sys.stdin.readline

n, k = map(int, input().split())

# 찾고자하는 인덱스
idx = 0

# 리스트 생성
n_list = [i+1 for i in range(n)]
# len이 0이상일때 반복
print("<", end="")
while len(n_list) > 1 :
    # 인덱스를 계산
    idx = (idx + k -1) % len(n_list)
    print(n_list[idx], end=", ")
    del n_list[idx]
print(n_list[-1], end=">")

