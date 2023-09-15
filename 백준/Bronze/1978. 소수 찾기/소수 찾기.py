t = int(input())
t_list = list(map(int, input().split()))

# 소수의 개수 구하기
def is_prime(n):
    if n == 1 :
        return False
    elif n == 2 or n == 3 :
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6
    return True


count = 0
for i in t_list:
    if is_prime(i):
        count += 1

print(count)
