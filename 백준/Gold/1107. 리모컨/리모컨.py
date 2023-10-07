# 먼저 사용할 수 있는 숫자는 다음과 같다.
number_list = list(i for i in range(10))
# 목적지 값을 받는다.
dest = int(input())
# 목적지의 값을 리스트 형태로 넣는다.
dest_list = []
dest2 = dest
while dest2 > 0:
    dest_list.append(dest2 % 10)
    dest2 //= 10
if dest == 0:
    dest_list.append(0)

dest_list.reverse()

# 최대와 최소의 값이 들어갈 리스트를 생성한다.
min_ans = []
max_ans = []

# 제외할 숫자를 받고, 제외시킨다.
n = int(input())
if n > 0:
    del_num = list(map(int, input().split()))
    for i in del_num:
        number_list.remove(i)

number_list.sort()
# 정답이 될 수 있는 리스트
ans_list = []
# 0. 100에서 + 또는 - 해서 갈 수 있는 경우
ans_list.append(abs(100 - dest))

# 1. 작은 경우
def min_case():
    if len(number_list) == 1 and number_list[0] == 0:
        min_ans.append(0)
        return 0

    for i in range(len(dest_list)):
        if dest_list[i] in number_list:
            min_ans.append(dest_list[i])
        # 쓸 수 없는 숫자가 나온다.
        else :
            is_plus = False
            # 한 치수 더 작은 숫자를 찾아 넣는다.
            for num in reversed(number_list):
                if num < dest_list[i]:
                    min_ans.append(num)
                    is_plus = True
                    break
            # 한 치수 더 작은 숫자를 찾은 경우에 가장 큰 숫자들로 뒤를 채운다.
            if is_plus:
                for _ in range(i+1, len(dest_list)):
                    min_ans.append(max(number_list))
                return 0

            # 한 치수 작은 숫자를 찾지 못한 경우
            else :
                is_plus_2 = False
                # 내 앞에 기존에 숫자가 있다면 내 앞 숫자를 한치수 더 작은 숫자로 끼운다
                if len(min_ans) > 0:
                    last_num = min_ans.pop()
                    for num in reversed(number_list):
                        if num < last_num:
                            min_ans.append(num)
                            is_plus_2 = True
                            break
                    # 갈아 끼우기에 성공했다면, 나머지 숫자는 강력하게 채운다.
                    if is_plus_2 :
                        for _ in range(i, len(dest_list)):
                            min_ans.append(max(number_list))
                        return 0
                    # 갈아 끼우기에 실패 했다면, 해결 방법이 없다. 싹다 날린뒤 한칸 줄여 강하게 채운다.
                    else:
                        min_ans.clear()
                        for _ in range(len(dest_list) - 1):
                            min_ans.append(max(number_list))
                        return 0

                # 내 앞에 숫자가 없다면 내가 첫 기수이다. 싹다 날린뒤 한 칸 줄여 강하게 채운다
                else :
                    min_ans.clear()
                    for _ in range(len(dest_list)-1):
                        min_ans.append(max(number_list))
                    return 0

def max_case():
    if len(number_list) == 1 and number_list[0] == 0:
        max_ans.append(0)
        return 0

    for i in range(len(dest_list)):
        if dest_list[i] in number_list:
            max_ans.append(dest_list[i])

        # 쓸 수 없는 숫자가 나오는 경우
        else :
            is_plus = False
            # 해당 숫자보다 한 치수 크게한다
            for num in number_list:
                if num > dest_list[i]:
                    max_ans.append(num)
                    is_plus = True
                    break
            # 한 치수 크게하기에 성공한 경우
            if is_plus:
                # 나머지는 다 제일 작은 거로
                for _ in range(i+1, len(dest_list)):
                    max_ans.append(min(number_list))
                return 0
            # 한 치수 크게하기에 실패한 경우
            else:
                is_plus_2 = False
                # 내앞 기수의 숫자가 있다면 기존 기수의 값을 한 치수 크게 하고
                # 나머지를 작은 값으로 채운다.
                if len(max_ans) > 0:
                    last_num = max_ans.pop()
                    for num in number_list:
                        if num > last_num:
                            max_ans.append(num)
                            is_plus_2 = True
                            break
                    # 갈아끼우기에 성공했다면 작게 나머지 값을 채운다.
                    if is_plus_2 :
                        for _ in range(i, len(dest_list)):
                            max_ans.append(min(number_list))
                        return 0
                    # 갈아끼우기에 실패했다면 방법은 없다.
                    # 가장작은 값으로 길이를 늘린 채 채워준다.
                    else:
                        # 기존 값들을 싹 다 버리고
                        max_ans.clear()
                        # 0이 아닌, 가장 작은 숫자를 앞에 박는다.
                        number_set = set(number_list)
                        number_set.discard(0)
                        max_ans.append(min(number_set))
                        # 0을 포함한 가장 작은 숫자들을 꽉 채운다
                        for _ in range(len(dest_list)):
                            max_ans.append(min(number_list))
                        return 0
                # 한 치수키우기에 실패했고, 내가 첫 기수였다.
                else:
                    # 0이 아닌, 가장 작은 숫자를 앞에 박는다.
                    number_set = set(number_list)
                    number_set.discard(0)
                    max_ans.append(min(number_set))
                    # 0을 포함한 가장 작은 숫자들을 꽉 채운다
                    for _ in range(len(dest_list)):
                        max_ans.append(min(number_list))
                    return 0


# 가능한 숫자가 없는경우, 최대/최소 수를 찾을 수 없으므로 생략
if len(number_list) > 0:
    min_case()
    max_case()




# 목적지까지와의 거리 계산
def cal_length(mm_ans, dest):
    if len(mm_ans) > 0 :
        sum = 0
        for i, num in enumerate(mm_ans):
            sum += num * 10 ** (len(mm_ans)-1-i)
        ans_list.append(abs(sum-dest)+len(str(sum)))

cal_length(min_ans,dest)
cal_length(max_ans,dest)

print(min(ans_list))