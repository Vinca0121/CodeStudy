my_list = list(input())

start_char = 'a'
end_char = 'z'

start_num = ord(start_char)
end_num = ord(end_char)

for num in range(start_num, end_num + 1):
    if chr(num) in my_list:
        print(my_list.index(chr(num)), end=" ")
    else:
        print(-1, end=' ')
