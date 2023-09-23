def check_color(square):
    global w, b
    
    # black - 전체에서 0이 없다면
    if 0 not in (num for row in square for num in row):
        b += 1
    # white - 전체에서 1이 없다면
    elif 1 not in (num for row in square for num in row):
        w += 1

    else:
        # black 과 white가 섞여있는 경우
        # 반복문을 통해 4개로 나눈 사각형을 재귀를 통해서 호출
        for i in range(4):
            # 크기는 len(square) // 2
            # 리스트 제작 - 행의 수만큼 append
            new_square = []
            square_length = len(square) // 2
            if i == 0:  # 1사분면
                for j in range(square_length):
                    new_square.append(square[j][:square_length])              
            elif i == 1:  # 2사분면
                for j in range(square_length):
                    new_square.append(square[j][square_length:])
            elif i == 2:  # 3사분면
                for j in range(square_length):
                    new_square.append(square[j + square_length][:square_length])
            else:  # 4사분면
                for j in range(square_length):
                    new_square.append(square[j + square_length][square_length:])
                        
            check_color(new_square)

n = int(input())
my_map = []
for _ in range(n):
    my_map.append(list(map(int, input().split())))

global w, b
w = 0  # 0인 경우
b = 0  # 1인 경우

check_color(my_map)
print("{}\n{}".format(w, b))