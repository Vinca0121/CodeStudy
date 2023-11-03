t = int(input())
for _ in range(t):
    my_list = list(input())
    sum = 0
    c = 1
    for i in my_list:
        if i == 'O':
            sum += c
            c += 1
        else:
            c = 1
    print(sum)