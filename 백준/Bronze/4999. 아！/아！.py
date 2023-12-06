# 사용자로부터 입력 받기
jaehwan_says = input().strip()  # 재환이가 낼 수 있는 "aaah"
doctor_wants = input().strip()  # 의사가 원하는 "aah"

# 재환이가 낼 수 있는 "aaah"와 의사가 원하는 "aah"의 길이를 비교
if len(jaehwan_says) >= len(doctor_wants):
    print("go")  # 병원에 갈 수 있음
else:
    print("no")  # 병원에 갈 수 없음
