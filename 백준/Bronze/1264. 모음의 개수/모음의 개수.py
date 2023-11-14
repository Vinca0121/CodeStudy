while True:
    s = input()
    if s == '#':
        break
    else:
        ans = 0
        for i in s.lower():
            if i in ['a', 'e', 'i', 'o', 'u']:
                ans += 1
        print(ans)