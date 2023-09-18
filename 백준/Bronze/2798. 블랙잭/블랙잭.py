import sys
from itertools import combinations
input = sys.stdin.readline
t, ans = map(int, (input().split()))

cards = list(map(int, input().split()))
# 5 21
# 5 6 7 8 9

best_sum = 0
combinations_list = list(combinations(cards, 3))

for list in combinations_list:
    sum_ = sum(list)
    # 정답
    if (sum_ <= ans and sum_ > best_sum):
        best_sum = sum_

print(best_sum)