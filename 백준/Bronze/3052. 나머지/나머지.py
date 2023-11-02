my_list = [int(input()) for _ in range(10)]
for i in range(10):
    my_list[i] = my_list[i] % 42

my_set = set(my_list)
print(len(my_set))