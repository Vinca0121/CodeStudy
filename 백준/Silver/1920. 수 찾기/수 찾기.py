# 풀
pool_n = int(input())
pool_list = list(map(int, input().split()))
pool_list.sort()

# 찾을 숫자들
test_n = int(input())
test_list = list(map(int, input().split()))


def binarySearch(star, pool_list):
    left = 0
    right = len(pool_list)-1

    while left <= right:
        middle_idx = (left+right) // 2
        middle_num = pool_list[middle_idx]
        if star == middle_num:
            return True
        elif star < middle_num :
            right = middle_idx - 1
        elif star > middle_num :
            left = middle_idx + 1
    return False

for num in test_list:
    ans = binarySearch(num, pool_list)
    if ans :
       print(1)
    else :
        print(0)