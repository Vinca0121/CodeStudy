N = int(input())
M = int(input())
S = input()

cnt = 0
ans = 0
j = 1
while j < M - 1:
    if S[j-1] == 'I' and S[j] == 'O' and S[j+1] == 'I':
        cnt += 1
        if cnt == N:
            cnt -= 1
            ans += 1
        j += 1
    else:
        cnt = 0
    j += 1

print(ans)