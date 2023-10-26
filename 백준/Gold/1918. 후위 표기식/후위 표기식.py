
opers = []
ans = []
string = input()

for s in string:
    if s == "*" or s =="/":
        # 연산자와 가중치를 저장

        # 나보다 낮은 놈이 나올 때 까지 정답으로 가시지요
        while opers:
            # 나와 같은신 분이군요 정답으로 가시지요!
            if opers[-1][1] == 2:
                ans.append(opers.pop()[0])
            # ( 또는 문자열 인 경우 패스하겠습니다
            else:
                break
        opers.append([s, 2])

    elif s == "+" or s =="-":
        # 연산자와 가중치를 저장
        # 나랑 같거나 높은 놈이면 정답으로 가시지요
        while opers:
            if opers[-1][1] >= 1:
                ans.append(opers.pop()[0])
            # ( 라면 패스하겠습니다.
            else:
                break
        opers.append([s,1])

    elif s == "(":
        opers.append([s,0])
    elif s == ")":
        # 열린괄호가 나올 때 까지 연산자를 전부 정답에 뽑아내서 저장하기
        while opers:
            operation = opers.pop()[0]
            if operation == '(':
                break
            else:
                ans.append(operation)
    # 일반 문자열
    else:
        # 그냥 넣는다.
        ans.append(s)


# 모든 연산자를 뽑아내서 ans에 저장
while opers:
    ans.append(opers.pop()[0])

for i in ans:
    print(i,end="")
