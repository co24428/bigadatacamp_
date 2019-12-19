GAME_TITLE_LEN_MAX = 20
PLAYER_NAME_LEN_MAX = 15
GAME_LEVEL_MIN = 1
GAME_LEVEL_MAX = 9


if True:

    # step 1
    print("Enjoy Custom Game world")

    # step 2
    # 게임 제목
    while 1: # 무한루프는 break 필수!
        # 엔터키 칠 때까지 코드를 진행하지 않는다.
        tmp = input("게임 제목을 입력하시오,\n \
            단 %s자 이내로 입력 가능합니다. : \n"%(GAME_TITLE_LEN_MAX)).strip()

        # tmp == '', len(tmp) == 0
        if  not tmp: # 공백일 때, 스페이스 바 누른 것도 체크 -> input에서 strip 실행
            print("정확하게 입력하세요!")
        elif len(tmp) > GAME_TITLE_LEN_MAX: # 20자 초과
            print(GAME_TITLE_LEN_MAX + "자가 초과되었습니다.")
        else:
            gameTitle = tmp
            break # 3단계 진입

    # 스코프 - 변수의 사용 가능한 범위
    # 파이썬에서는 함수, 클래스 외부는 무조건 전역변수
    print ('Game Title : ', gameTitle)

    # step 3
    # 플레이어 이름
    while 1:
        tmp = input('플레이어의 닉네임을 입력하시오,\n \
            단 %s자로 제한한다. : \n'%(PLAYER_NAME_LEN_MAX)).strip()

        if not tmp:
            print("정확하게 입력하세요!")
        elif len(tmp) > PLAYER_NAME_LEN_MAX:
            print(PLAYER_NAME_LEN_MAX + "자가 초과되었습니다.")
        else:
            player_name = tmp
            break
    print ('player Name : ', player_name)

    # step 4
    # 게임 난이도
    while 1:
        tmp = input('게임 난이도를 입력하시오,\n \
            단 %s~%s까지 정수 형태로 제한한다. : \n'%(GAME_LEVEL_MIN, GAME_LEVEL_MAX)).strip()
        if not tmp:
            print("정확하게 입력하세요!")
        elif not tmp.isnumeric():
            print("잘못된 입력입니다. 숫자를 입력해주세요") 
        else:
            tmp_int = int(tmp)
            if tmp_int > GAME_LEVEL_MAX or tmp_int < GAME_LEVEL_MIN:
                print("잘못된 입력입니다. %s~%s 사이의 난이도를 입력해주세요"%(GAME_LEVEL_MIN, GAME_LEVEL_MAX))
            else:
                game_level = tmp_int
                break

    print ('Game Level : ', game_level)

# step 5
print( '-'* 20)
print('현재까지 입력 상황')
print('gameTitle : ', gameTitle)
print('player_name : ', player_name)
print('game_level : ', game_level)
print( '-'* 20)