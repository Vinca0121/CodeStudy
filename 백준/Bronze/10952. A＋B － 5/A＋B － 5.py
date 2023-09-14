# T번의 반복을 통해 테스트 케이스를 처리
while True:
    A, B = map(int, input().split())
    if(A != 0 and B != 0):
        print(A + B)
    else:
        break
