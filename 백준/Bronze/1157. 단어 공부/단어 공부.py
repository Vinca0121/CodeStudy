str = input().upper()

dic = {}
for s in str:
    if s in dic:
        dic[s] += 1
    else:
        dic[s] = 1

max_word = [-1, ""]
for key, value in dic.items():
    if max_word[0] < value:
        max_word[0] = value
        max_word[1] = key
    elif max_word[0] == value:
        max_word[1] = max_word[1]+key

if len(max_word[1]) > 1:
    print("?")
else:
    print(max_word[1])