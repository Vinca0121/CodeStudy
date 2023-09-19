import sys
input = sys.stdin.readline


global fibo_dic_0, fibo_dic_1
fibo_dic_0 = {}
fibo_dic_1 = {}

# 빈 40개의 딕셔너리 생성
for i in range(41):
    fibo_dic_0[i] = 0
    fibo_dic_1[i] = 0

def fibonacci(n):
    fibo_list = [0, 0]
    # 만약 해당 피보나치 수열이 비어있는 경우
    # 새로운 피보나치 값을 딕셔너리에 등록
    if fibo_dic_0[n] == 0 and fibo_dic_1[n] == 0:
        # 피보나치 값 계산
        if n == 0:
            fibo_list[0] += 1
            fibo_dic_0[n] = fibo_list[0]
            fibo_dic_1[n] = fibo_list[1]
            return fibo_list

        elif n == 1:
            fibo_list[1] += 1
            fibo_dic_0[n] = fibo_list[0]
            fibo_dic_1[n] = fibo_list[1]
            return fibo_list


        else :
            # 1, 2를 제외한 새로운 피보나치 fibo(n)을 저장
            fibo_list = [l1 + l2 for l1, l2 in zip(fibonacci(n-2), fibonacci(n-1))]

            fibo_dic_0[n] = fibo_list[0]
            fibo_dic_1[n] = fibo_list[1]
            return fibo_list
    # 이미 저장된 fibo(n)이 있는 경우
    else :
        fibo_list[0] = fibo_dic_0[n]
        fibo_list[1] = fibo_dic_1[n]
        return fibo_list


# 테스트 케이스만큼 반복
t = int(input())

for i in range(t):
    # 값을 받아옴
    enroll = int(input())
    # 피보나치 함수를 동작
    fibonacci(enroll)
    # enroll 값에 해당하는 0, 1값을 가져옴
    print(fibo_dic_0[enroll], fibo_dic_1[enroll])
