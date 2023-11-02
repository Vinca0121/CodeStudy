# 제곱의 크기
b = int(input())
# 피보나치 수열의 행렬
matrix =[[1,1], [1,0]]

def mul_matrix(mat1, mat2):
    res = [[0 for _ in range(2)] for _ in range(2)]

    for i in range(2):
        for j in range(2):
            for k in range(2):
                res[i][j] += mat1[i][k] * mat2[k][j] % 1000000007
    return res

# 분할정복을 이용한 거듭제곱
# 분할정복
def power(matrix, b):
    if b == 1:  # b의 값이 1이 될 때까지 재귀
        return matrix

    # 이전 제곱 수 계산 (3^5 = 3 * 3^2 * 3^2) -> 이 경우 tml 는 3^2
    tmp = power(matrix, b // 2)
    # 홀수
    if b % 2 == 1:
        # 홀수이므로 3개를 해야함 (3^5 = 3 * 3^2 * 3^2)
        return mul_matrix(matrix, mul_matrix(tmp, tmp))  # b가 홀수인 경우

    else:
        # 짝수이므로 2개만 있으면 됨
        return mul_matrix(tmp, tmp)  # b가 짝수인 경우

ans_matrix = power(matrix, b)
# 출력
print(ans_matrix[0][1] % 1000000007)