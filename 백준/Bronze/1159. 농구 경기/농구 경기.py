a = int(input())
my_dic = {}
for _ in range(a):
    s = input()[0]
    if s in my_dic:
        my_dic[s] += 1
    else:
        my_dic[s] = 1
happy = False
for key in sorted(my_dic.keys()):
    if my_dic[key] >= 5:
        print(key, end="")
        happy = True
if not happy:
    print("PREDAJA")