# 테스트 케이스의 개수 T를 입력 받음
T = int(input())

# T번의 반복을 통해 테스트 케이스를 처리
for _ in range(T):
    # A와 B를 입력 받음
    A, B = map(int, input().split())
    
    # A와 B를 더한 결과를 출력
    print(A + B)