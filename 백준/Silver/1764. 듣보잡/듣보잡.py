a_set = set()
ans_list = []

a ,b = map(int, input().split())

for _ in range(a):
    a_set.add(input().strip())

for _ in range(b):
    name = input().strip()
    if name in a_set:
        ans_list.append(name)

ans_list.sort()
print(len(ans_list))
for n in ans_list:
    print(n)
