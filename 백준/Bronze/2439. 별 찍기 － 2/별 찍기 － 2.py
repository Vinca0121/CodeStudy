n = int(input())

for i in range(1, n+1):
    # 공백출력
    for j in range(n-i):
        print(" ",end="")
    # 별 출력
    for k in range(i):
        print('*',end="")
    print()