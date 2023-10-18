from itertools import combinations
import sys
input = sys.stdin.readline


def search(mb_list):
    # 비둘기집 원리에 의해 16가지의 MBTI가 3번씩 나오지 않는 방법은 최대 32개까지다.
    # 33개가 되는 순간 겹치는 MBTI가 반드시 1개는 생긴다.
    ans = float('inf')
    if len(mb_list) > 32:
        return 0
    combs = combinations(mb_list, 3)
    for com in combs:
        count = 0
        for i in range(4):
            if com[0][i] != com[1][i]:
                count += 1
        # 두번째랑 세번째를 비고
        for i in range(4):
            if com[1][i] != com[2][i]:
                count += 1
        # 첫번째랑 세번째를 비고
        for i in range(4):
            if com[0][i] != com[2][i]:
                count += 1
        if count == 0:
            return 0
        else:
            ans = min(ans, count)

    return ans
t = int(input().rstrip())

for _ in range(t):
    # n 명의 사람이 존재
    n = int(input().rstrip())
    mb_list = list(map(str, input().rstrip().split()))
    print(search(mb_list))