star = int(input())
num = 0
value = 666
## 666이 숫자열에 포함되면 +1
while True:
    if '666' in str(value):
        num += 1

    if num == star:
        print(value)
        break

    value += 1

## star 값에 도달하면 종료