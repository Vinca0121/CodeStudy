list1 = list(map(int, input().split()))
sum = 0
for i in list1:
    sum += i ** 2

print((sum % 10))
    