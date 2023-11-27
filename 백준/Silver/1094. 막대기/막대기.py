def bitmask(ans):
    numbers = [64]
    while True:
        if sum(numbers) == ans:
            return len(numbers)
        smallest = numbers[-1] // 2
        if ans <= sum(numbers) - numbers[-1] + smallest:
            numbers.pop()
            numbers.append(smallest)
        # 버리는 경우 작아지면 그대로 넣음
        else:
            numbers.pop()
            numbers.append(smallest)
            numbers.append(smallest)


a = int(input())
print(bitmask(a))
