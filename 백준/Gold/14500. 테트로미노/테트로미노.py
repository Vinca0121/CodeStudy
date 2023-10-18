sero, garo = map(int, input().split())
my_map = []
for _ in range(sero):
    my_map.append(list(map(int, input().split())))

def flat():
    global ans
    # 일직선으로 세워져 있는 경우
    x = 0
    y = 0
    if sero >= 4 and garo >= 1:
        x = garo # 5
        y = sero - 3 # 2

    # 세로의 횟수만큼 반복할거야 2 ( i : 0 1 )
    for i in range(y):
        # 가로의 횟수만큼 반복할거야 5 (j : 0 1 2 3 4 )
        for j in range(x):
            # 4개씩 더할거야
                # 1열 계산 2열 계산 ... idx 4 즉, 5까지는 정상
                # 5를 벗어나는 경우는? 행을 한칸씩 밀고, j를 0부터 시작해야함
            temp_ans = my_map[0+i][j] + my_map[1+i][j] + my_map[2+i][j] + my_map[3+i][j]
            ans = max(temp_ans, ans)

    # 일직선으로 누워져 있는 경우 (ㅡ)
    if garo >= 4 and sero >= 1:
        x = garo - 3 # 2
        y = sero # 5
        for i in range(y):
            for j in range(x):
                temp_ans = my_map[i][0+j] + my_map[i][1+j] + my_map[i][2+j] + my_map[i][3+j]
                ans = max(temp_ans, ans)

def gun():
    global ans
    x = 0
    y = 0
    if sero >= 3 and garo >= 2:
        x = garo - 1
        y = sero - 2
        for i in range(y):
            for j in range(x):
                temp_ans1 = my_map[0 + i][j] + my_map[1 + i][j] + my_map[2 + i][j] + my_map[2 + i][j + 1]
                temp_ans2 = my_map[2 + i][j] + my_map[2 + i][j+1] + my_map[1 + i][j+1] + my_map[0 + i][j + 1]
                temp_ans3 = my_map[0 + i][j] + my_map[1 + i][j] + my_map[2 + i][j] + my_map[0 + i][j + 1]
                temp_ans4 = my_map[0 + i][j] + my_map[2 + i][j+1] + my_map[1 + i][j+1] + my_map[0 + i][j + 1]
                ans = max(temp_ans1, temp_ans2, temp_ans3, temp_ans4, ans)

    if sero >= 2 and garo >= 3:
        x = garo - 2
        y = sero - 1
        for i in range(y):
            for j in range(x):
                temp_ans1 = my_map[i][0 + j] + my_map[i][1 + j] + my_map[i][2 + j] + my_map[i+1][0 + j]
                temp_ans2 = my_map[i][0 + j] + my_map[i][1 + j] + my_map[i][2 + j] + my_map[i+1][2 + j]
                temp_ans3 = my_map[i+1][0 + j] + my_map[i+1][1 + j] + my_map[i+1][2 + j] + my_map[i][0 + j]
                temp_ans4 = my_map[i+1][0 + j] + my_map[i+1][1 + j] + my_map[i+1][2 + j] + my_map[i][2 + j]
                ans = max(temp_ans1, temp_ans2, temp_ans3, temp_ans4, ans)

def z():
    global ans
    x = 0
    y = 0
    if sero >= 3 and garo >= 2:
        x = garo - 1
        y = sero - 2
        for i in range(y):
            for j in range(x):
                temp_ans1 = my_map[0 + i][j] + my_map[1 + i][j] + my_map[1 + i][j+1] + my_map[2 + i][j + 1]
                temp_ans2 = my_map[1 + i][j] + my_map[2 + i][j] + my_map[1 + i][j + 1] + my_map[0 + i][j + 1]
                ans = max(temp_ans1, temp_ans2, ans)


    if sero >= 2 and garo >= 3:
        x = garo - 2
        y = sero - 1
        for i in range(y):
            for j in range(x):
                temp_ans1 = my_map[1 + i][j] + my_map[1 + i][j + 1] + my_map[0 + i][j+1] + my_map[0 + i][j + 2]
                temp_ans2 = my_map[0 + i][j] + my_map[0 + i][j + 1] + my_map[1 + i][j + 1] + my_map[1 + i][j + 2]
                ans = max(temp_ans1, temp_ans2, ans)

def fu():
    global ans
    x = 0
    y = 0
    if sero >= 3 and garo >= 2:
        x = garo - 1
        y = sero - 2
        for i in range(y):
            for j in range(x):
                temp_ans1 = my_map[0 + i][j] + my_map[1 + i][j] + my_map[2 + i][j] + my_map[1 + i][j + 1]
                temp_ans2 = my_map[0 + i][j+1] + my_map[1 + i][j+1] + my_map[2 + i][j+1] + my_map[1 + i][j + 0]
                ans = max(temp_ans1, temp_ans2, ans)

    if sero >= 2 and garo >= 3:
        x = garo - 2
        y = sero - 1
        for i in range(y):
            for j in range(x):
                temp_ans1 = my_map[i+1][0 + j] + my_map[i+1][1 + j] + my_map[i+1][2 + j] + my_map[i][1 + j]
                temp_ans2 = my_map[i][0 + j] + my_map[i][1 + j] + my_map[i][2 + j] + my_map[i+1][1 + j]
                ans = max(temp_ans1, temp_ans2, ans)

def square():
    global ans
    x = 0
    y = 0
    if sero >= 2 and garo >= 2:
        x = garo - 1
        y = sero - 1
        for i in range(y):
            for j in range(x):
                temp_ans = my_map[i+0][0 + j] + my_map[i+0][1 + j] + my_map[i+1][0 + j] + my_map[i+1][1 + j]
                ans = max(temp_ans, ans)


global ans
ans = 0

flat()
gun()
z()
fu()
square()

print(ans)