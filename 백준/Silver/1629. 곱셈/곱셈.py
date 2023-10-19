a, b, c = map(int, input().split())

# 반복적으로 (a^b) % c를 계산하는 함수
def mod_pow(a, b, c):
    result = 1
    a = a % c
    
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % c
        a = (a * a) % c
        b = b // 2
    
    return result

result = mod_pow(a, b, c)
print(result)