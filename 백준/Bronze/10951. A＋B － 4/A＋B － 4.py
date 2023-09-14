while True:
    # A와 B를 입력 받음
    try :
        A, B = map(int, input().split())
        # A와 B를 더한 결과를 출력
        print(A + B)
    except:
        break