def solution(players, callings):
    # 선수와 인덱스를 매핑하는 딕셔너리 생성
    player_dic = {player: i for i, player in enumerate(players)}

    # 각 호출에 따라 자리를 바꿈
    for call in callings:
        # 현재 인덱스 추출
        i = player_dic[call]

        # 추월이 가능한지 확인 (1등이 아닌 경우)
        if i > 0:
            # 앞의 선수와 자리 바꾸기
            front_player = players[i - 1]
            players[i - 1], players[i] = players[i], front_player

            # 딕셔너리 업데이트
            player_dic[call] = i - 1
            player_dic[front_player] = i

    return players
