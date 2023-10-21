sum = 1
for _ in range(3):
    sum *= int(input())

nums = [0 for _ in range(10)]

for s in str(sum):
    nums[int(s)] += 1

for i in nums:
    print(i)