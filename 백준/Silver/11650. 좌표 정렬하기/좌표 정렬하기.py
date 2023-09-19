n = int(input())


n_list = []
for i in range(n):
    temp = list(map(int, input().split()))
    n_list.append(temp)

n_list = sorted(n_list, key = lambda x : (x[0], x[1]))

for i in n_list:
    print(i[0], i[1])