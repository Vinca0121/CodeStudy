import sys

input = sys.stdin.readline


def test():
    opers = input().strip()
    n = int(input().strip())
    my_list = input().strip()

    if n > 0:
        my_list = list(map(int, my_list[1:-1].split(",")))
    else:
        my_list = []

    is_reversed = False
    error_code = False
    left_idx = 0
    right_idx = len(my_list)

    for oper in opers:
        if oper == "R":
            is_reversed = not is_reversed
        elif oper == "D":
            if left_idx < right_idx:
                if is_reversed:
                    right_idx -= 1
                else:
                    left_idx += 1
            else:
                print("error")
                error_code = True
                return 0

        # 에러가 발생하지 않은 경우만 결과 출력
    result_array = my_list[left_idx:right_idx]

    if is_reversed:
        result_array = result_array[::-1]

    if not error_code:
        print('[' + ','.join(map(str, result_array)) + ']')


t = int(input().strip())
for _ in range(t):
    test()
