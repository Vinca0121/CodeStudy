a, b = map(int, input().split())

# a_list를 set으로 변경하여 데이터 검색을 빠르게 수행할 수 있도록 합니다.
a_set = set(input().rstrip() for _ in range(a))

result = sorted(name for name in (input().rstrip() for _ in range(b)) if name in a_set)

print(len(result))  # 찾은 이름의 총 수 출력
for name in result:
    print(name)  # 찾은 이름 출력