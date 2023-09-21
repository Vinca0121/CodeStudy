def make_one(n):
    # 숫자 0과 1은 0으로 고정
    min_list = [0] * (n+1)
    # 2부터 10까지 반복하며 각 숫자의 최소 도달 횟수를 저장 (bottom-up)
    for i in range(2, n+1):
        # 내 이전 (i-1)번째 보다 연산이 한번 더 일어나는 게 국룰 (+1)
        min_list[i] = min_list[i-1] +1
        # 국룰이 위배되는 경우 이전 값을 x2 또는 x3으로 도달 할 수 있다면?
        # 도달한 값에서 연산을 한번만 (x2 또는 x3)하면 된다는 것
        if i % 2 == 0:
            ## 여기서의 +1은 x2 연산자 1번을 추가한다는 뜻
            min_list[i] = min(min_list[i], min_list[i//2] + 1)
        if i % 3 == 0:
            # 여기서의 +1은 x3 연산자를 1번 사용한다는 뜻
            min_list[i] = min(min_list[i], min_list[i//3] + 1)

    # bottom up 방식으로 n개를 다 구하고, 값을 추출
    return min_list[n]

n = int(input())
print(make_one(n))

