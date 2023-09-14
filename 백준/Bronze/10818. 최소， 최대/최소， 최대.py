count_num = int(input())
count_list = input().split()
count_list = [int(n) for n in count_list]
print(min(count_list), max(count_list),sep=" ")