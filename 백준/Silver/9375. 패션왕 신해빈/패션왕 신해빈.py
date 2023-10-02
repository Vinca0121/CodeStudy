from itertools import combinations
# 테스트 수
t = int(input())

for i in range(t):
    # 옷
    clothes = {}
    # 의상의 수
    n = int(input())
    for _ in range(n):
        # 옷과 옷의 종류를 받음
        _, case = map(str, input().split())

        # 옷의 종류별로 개수를 딕셔너리로 저장
        if case not in clothes:
            clothes[case] = 1
        else:
            clothes[case] += 1

    # 정답 초기값
    sum = 1
    # 각 옷의 개수를 곱함 (단, 곱할때는 옷의 종류가 선택되지 않은 경우를 포함하므로 +1)
    for c in clothes.values():
        sum *= (c+1)

    # 전체 벗은 경우를 뺌
    print(sum-1)