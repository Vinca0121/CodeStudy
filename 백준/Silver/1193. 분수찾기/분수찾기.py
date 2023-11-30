def find_fraction(x):
    diagonal = 1
    while x > diagonal:
        x -= diagonal
        diagonal += 1
    
    if diagonal % 2 == 0:
        numerator = x
        denominator = diagonal - x + 1
    else:
        numerator = diagonal - x + 1
        denominator = x

    return f"{numerator}/{denominator}"

# X 값 입력
X = int(input())

# X에 해당하는 분수 출력
result = find_fraction(X)
print(result)
