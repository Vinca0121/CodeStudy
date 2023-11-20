while True:
    strs = input()
    if strs == '0':
        break
    ans = 2
    for s in strs:
        if s == '1':
            ans += 2
        elif s == '0':
            ans += 4
        else:
            ans += 3
    ans += len(strs)-1
    print(ans)