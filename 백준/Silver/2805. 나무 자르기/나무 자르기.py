import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().rstrip().split()))
trees.sort()


left = 0
right = trees[-1]
max_tall = 0
while left <= right:
    mid = (left + right) // 2
    cutting_sum = 0

    for t in trees:
        if t > mid :
            cutting_sum += (t - mid)

    # 벌목하는 범위를 더 타이트하게 만들었을 때도 정답이 나오는가를 테스트
    if cutting_sum > m:
        max_tall = mid
        left = mid + 1

    elif cutting_sum < m:
        right = mid - 1

    else:
        max_tall = mid
        break
    
print(max_tall)