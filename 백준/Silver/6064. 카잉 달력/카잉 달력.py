def cal(m, n, x, y):
    year = x  # x부터 시작
    while year <= m * n:  # 모든 가능한 해에 대해 반복
        if (year - 1) % m + 1 == x and (year - 1) % n + 1 == y:
            return year
        year += m
    return -1



t = int(input())

case_list = []
for _ in range(t):
    case_list.append(tuple(map(int, input().split())))

for i in case_list:
    m, n, x, y = i
    print(cal(m, n, x, y))

