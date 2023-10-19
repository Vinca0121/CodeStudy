a, b, c = map(int, input().split())
# b는 제곱할 수가 된다.
def pow(b):
    if b == 0:
        return 1
    # 홀수
    if b % 2 == 1:
        h_pow = pow(b // 2)
        return (a * h_pow * h_pow) % c
    # 짝수
    else:
        h_pow = pow(b // 2)
        return (h_pow * h_pow) % c
print(pow(b))
