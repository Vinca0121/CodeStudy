import sys
input = sys.stdin.readline
n = int(input().rstrip())

numbers = list(map(int, input().rstrip().split()))
ans_dic = {}
for num in numbers:
    ans_dic[num] = -1

temp_set = set(numbers)
# 중복을 제거하고 정렬된 리스트를 만듬
sort_numbers = sorted(list(temp_set))

# n보다 작은 수가 몇개 있는지 세는 함수
index_dict = {num: idx for idx, num in enumerate(sort_numbers)}
def count(num):
    ans_dic[num] = index_dict[num]

for i, num in enumerate(numbers):
    # 세지 않은 경우만 계산
    if ans_dic[num] == -1:
        count(num)

    print(ans_dic[num], end=' ')
