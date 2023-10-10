import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().rstrip().split()))
trees.sort()

left = 0
right = max(trees)
result = 0

while left <= right:
    mid = (left + right) // 2
    total = 0
    for tree in trees:
        if tree > mid:
            total += tree - mid
    
    if total >= m:
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)