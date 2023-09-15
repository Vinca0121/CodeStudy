T = int(input())
word_list = []
for _ in range(T):
    word_list.append(input())
# print(word_list)
#
# for i in range(T-1):
#     for j in range(T-1-i):
#         if len(word_list[i]) > len(word_list[i+j+1]):
#             temp = word_list[i]
#             word_list[i] = word_list[i+j+1]
#             word_list[i+j+1] = temp
#
#
once_list = []
[once_list.append(a) for a in word_list if a not in once_list]

sorted_list = sorted(once_list, key=lambda x: (len(x), x))

for i in sorted_list:
    print(i)


