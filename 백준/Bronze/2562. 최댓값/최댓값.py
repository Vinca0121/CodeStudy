n_list = []
max_number = 0
max_index = 0
for i in range(9):
    n_list.append(int(input()))
    if(n_list[i] > max_number):
        max_number = n_list[i]
        max_index = i+1

print(max_number)
print(max_index)
