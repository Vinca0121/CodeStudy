n = int(input())

# 저장된 정답 리스트 (꺼내기 쉽게..)
ans_list = [0] * 12

# 이전 정답의 고정값
ans_list[1] = 1
ans_list[2] = 2
ans_list[3] = 4
ans_list[4] = 7

for i in range(5, 12):
                        # 4를 만드는 방법 # 3을 만드는 방법 # 2를 만드는 방법
                        # 각각 +1, +2, +3 을 해서 5를 만들 수 있기 때문
    ans_list[i] =  ans_list[i-1] + ans_list[i-2] + ans_list[i-3]


for _ in range(n):
    num = int(input())
    print(ans_list[num])