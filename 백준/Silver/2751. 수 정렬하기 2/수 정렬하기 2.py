# 병합 정렬 Algorithm
import sys
input = sys.stdin.readline

def merge_sort(arr):
    if len(arr) == 1:
        return arr


    # 배열을 반으로 쪼갬
    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    # 재귀를 통한 정렬 수행
    # left, right를 통해서 최종적으로 오름차순 정렬된 값을 가져와
    # 수행하는 건 모든 값이 단일 리스트가 될때까지 들어가
    # 즉, len = 1이 될 때까지 각 숫자들을 끝까지 가서 비교
    left_arr = merge_sort(left_arr)
    right_arr = merge_sort(right_arr)

    # 병합
    result_arr = []
    i = j = 0
    while True:
        try:
            if left_arr[i] < right_arr[j]:
                result_arr.append(left_arr[i])
                i += 1
            else:
                result_arr.append(right_arr[j])
                j += 1
        except IndexError:
            result_arr.extend(left_arr[i:])
            result_arr.extend(right_arr[j:])
            break

    return result_arr


n = int(input())

number_arr = []
for _ in range(n):
    number_arr.append(int(input()))

sorted_arr = merge_sort(number_arr)

# 출력 버퍼 설정
output_buffer = []
for i in sorted_arr:
    output_buffer.append(str(i))

# 출력
sys.stdout.write('\n'.join(output_buffer))