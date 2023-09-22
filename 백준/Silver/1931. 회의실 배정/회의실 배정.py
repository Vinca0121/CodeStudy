# 시작시간과 거리를 저장

# 거리가 짧은순으로 저장
# 시작시간이 가장 적은 값을 선택 만약, 시작시간이 같은 경우 거리가 가장 짧은 경우를 선택

t = int(input())
t_list = []
for i in range(t):
    start, end = map(int, input().split())
    t_list.append((start, end))

# 끝나는 시간 순으로 정렬
t_list = sorted(t_list, key=lambda x : (x[1], x))

# 첫번째로 끝나는 시간
first_end = t_list[0][1]
lesson = 0
endtime = 0
for time in t_list:
    # 시작 시간이 이전 종료시간(endtime)보다 앞인 경우
    if time[0] >= endtime :
        endtime = time[1]
        lesson += 1

print(lesson)

