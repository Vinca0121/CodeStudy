while True:
    number = input()
    if number[0] == '0':
        break
    if number[::-1] == number :
        print("yes")
    else :
        print("no")
