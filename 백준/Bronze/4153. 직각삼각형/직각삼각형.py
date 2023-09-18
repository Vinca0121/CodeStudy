import sys
input = sys.stdin.readline


while True:
    rect = list(map(int, input().split()))
    if rect[0] == 0:
        break
    rect = sorted(rect, reverse=True)
    if rect[0] ** 2 == (rect[1] ** 2) + (rect[2] ** 2):
        print('right')
    else:
        print('wrong')

