a, b = map(int, input().split())
my_list = list(map(int, input().split()))
my_list = [i-a*b for i in my_list]
for i in my_list:
    print(i, end=" ")