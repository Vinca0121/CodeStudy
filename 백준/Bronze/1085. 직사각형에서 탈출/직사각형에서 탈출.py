x, y, w, h = map(int,input().split())
ans_list = []
ans_list.append(x)
ans_list.append(y)
ans_list.append(abs(x-w))
ans_list.append(abs(y-h))

print(min(ans_list))