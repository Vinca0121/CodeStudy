while True:
    a, b, c = map(str, input().split())
    if a == '#':
        break
    if int(b) > 17 or int(c) > 79:
        print(a, "Senior")
    else:
        print(a, "Junior")
