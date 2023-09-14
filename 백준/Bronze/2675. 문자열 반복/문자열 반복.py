count =int(input())

main_list = []
for i in range(count):
    str_list = input().split()
    num = int(str_list[0])
    word = str_list[1]
    main_list.append([num, word])

for list in main_list: # [3, abc]
    for j in list[1]: # abc
        for k in range(list[0]) : # 3번 반복
            print(j, end="")
    print("")
