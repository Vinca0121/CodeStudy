o_size = int(input())
length = int(input())
str = input()


target_ioi = "I"
for i in range(o_size):
    target_ioi += "O"
    target_ioi += "I"

ans = 0
target_len = len(target_ioi)
for i in range(len(str)):
    if str[i:target_len+i] == target_ioi:
        ans += 1

print(ans)


