# 환경변수 or 게임 데이터 -> 프로그램에 영향을 미치는 고정값(임계값) 상수로 빼고
# 향후에는 *.py 바깥쪽으로 빼서 저장(파일 or 디비 or 서버)
# **고정값들은 바깥으로 뺀다**
GAME_TITLE_LEN_MAX = 20
PLAYER_NAME_LEN_MAX = 15
GAME_LEVEL_MIN = 1
GAME_LEVEL_MAX = 9

# 들여쓰기로 묶어줘서 True면 실행, False면 생략
if True:
    # 요구 사항
        # 절차적 프로그램 실습
        # 간단한 게임을 구현하여
        # 긴 단위의 프로그램을 작성하고, 절차적 프로그램을 이해한다
        # 머드 게임 스타일로 터미널에서 입력하면서 게임을 진행
        # 목적, 파이썬 타입, 연산 조건, 반복, 흐름제어 등을 프로그램을 개발하면서
        # 심화학습한다.
        # ---------------------------------------------------------
        # step 1 게임이 시작하면 "Enjoy Custom Game world"라는 문구를 출력한다.
        # step 2
        #   2.1 "게임 제목을 입력하시오, 단 20자 이내로 입력 가능합니다." 문구 출력
        #       -> 매번 입력을 대기할 때마다 해당 프롬프트를 출력하겠다.
        #   2.2 사용자가 입력할 때까지 무제한으로 대기한다
        #   2.3 아무것도 입력하지 않고 엔터를 치면 "정확하게 입력하세요!" 출력하고 다시 입력 대기한다
        #   2.4 20자 이상 입력하면 "20자가 초과되었습니다." 출력하고, 다시 입력 대기한다.
        #   2.5 20자 이내로 입력하면 gameTitle이라는 변수에 게임 제목을 담고 다음 3단계로 진입한다.
        # step 3
        #   3-1 "플레이어의 닉네임을 입력하시오, 단 15자로 제한한다"
        #   3-2 "입력에 대한 처리는 step 2와 동일하다"
        #   3-3 플레이어의 이름은 player_name이라는 변수에 담는다.
        # step 4
        #   4-1 "게임 난이도를 입력하시오, 단 1~9까지 정수 형태로 제한한다."
        #   4-2 입력에 대한 처리는 step 2와 동일하나, 정수가 아니면 에러를 출력한다.
        #   4-3 게임 난이도는 game_level이라는 변수에 담는다.

    # step 1
    print("Enjoy Custom Game world")

    # step 2
        #   2.2 사용자가 입력할 때까지 무제한으로 대기한다 -> 무한루프  => 순서상 2.2가 우선되게 됨(매번 입력으로 가정했기 때문)
        #   2.1 "게임 제목을 입력하시오, 단 20자 이내로 입력 가능합니다." 문구 출력
        #       -> 매번 입력을 대기할 때마다 해당 프롬프트를 출력하겠다.
        #   2.3 아무것도 입력하지 않고 엔터를 치면 "정확하게 입력하세요!" 출력하고 다시 입력 대기한다
        #   2.4 20자 이상 입력하면 "20자가 초과되었습니다." 출력하고, 다시 입력 대기한다.
        #   2.5 20자 이내로 입력하면 gameTitle이라는 변수에 게임 제목을 담고 다음 3단계로 진입한다.

        #   2.3 아무것도 입력하지 않고 엔터를 치면 
        #       2.3.1 "정확하게 입력하세요!" 출력하고 다시 입력 대기한다
        #       + 스페이스 바 누른 것도 체크 -> input에서 strip 실행
        #   2.4 20자 이상 입력하면 
        #       2.4.1 "20자가 초과되었습니다." 출력하고, 다시 입력 대기한다.
        #   2.5 20자 이내로 입력하면 
        #       2.5.1 gameTitle이라는 변수에 게임 제목을 담고 다음 3단계로 진입한다.

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
        #   3-1 "플레이어의 닉네임을 입력하시오, 단 15자로 제한한다"
        #   3-2 "입력에 대한 처리는 step 2와 동일하다"
        #   3-3 플레이어의 이름은 player_name이라는 변수에 담는다.

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
        #   4-1 "게임 난이도를 입력하시오, 단 1~9까지 정수 형태로 제한한다."
        #   4-2 입력에 대한 처리는 step 2와 동일하나, 정수가 아니면 에러를 출력한다.
        #   4-3 게임 난이도는 game_level이라는 변수에 담는다.

        # 조건 순서를 잘 맞춰라 ( 꼭 )
        # 빈도 순, 나오는 케이스의 범위를 점점 줄어드는 순서
        # <이 코드에서>
        # 공백 >> 정수형 >> 1~9 범위 >> 정확하게

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

    ############################################################
    # if 두 개 쓸 때 -> 반복문의 "continue"!!!

    # while 1:
    #     tmp = input('게임 난이도를 입력하시오,\n \
    #         단 %s~%s까지 정수 형태로 제한한다. : \n'%(GAME_LEVEL_MIN, GAME_LEVEL_MAX)).strip()
    #     if not tmp:
    #         print("정확하게 입력하세요!")
    #         continue # 기억합니다
    #     elif not tmp.isnumeric():
    #         print("잘못된 입력입니다. 숫자를 입력해주세요") 
    #         continue # 기억합니다

    #     tmp_int = int(tmp)
    #     if tmp_int < GAME_LEVEL_MIN or tmp_int > GAME_LEVEL_MAX:
    #         print("잘못된 입력입니다. %s~%s 사이의 난이도를 입력해주세요"%(GAME_LEVEL_MIN, GAME_LEVEL_MAX))
    #     else:
    #         game_level = tmp_int
    #         break

    ############################################################
    # if만 쓸 때 -> 반복문의 "continue"!!!!!!

    # while 1:
    #     tmp = input('게임 난이도를 입력하시오,\n \
    #         단 %s~%s까지 정수 형태로 제한한다. : \n'%(GAME_LEVEL_MIN, GAME_LEVEL_MAX)).strip()
    #     if not tmp:
    #         print("정확하게 입력하세요!")
    #         continue # 기억합니다
    #     elif not tmp.isnumeric():
    #         print("잘못된 입력입니다. 숫자를 입력해주세요") 
    #         continue # 기억합니다

    #     tmp_int = int(tmp)
    #     if tmp_int < GAME_LEVEL_MIN or tmp_int > GAME_LEVEL_MAX:
    #         print("잘못된 입력입니다. %s~%s 사이의 난이도를 입력해주세요"%(GAME_LEVEL_MIN, GAME_LEVEL_MAX))
    #         continue # 기억합니다
    #     game_level = tmp_int
    #     break

    ############################################################
    # 긍정 상황을 잡어서 처리 - 이렇게 할 수도 있다. - 예외처리!

    # while 1:
    #     try: # 오류가 발생하면 잡아서 처리 -> s/w가 다운되지 않는다.
    #         tmp = int(input('게임 난이도를 입력하시오,\n \
    #             단 %s~%s까지 정수 형태로 제한한다. : \n'%(GAME_LEVEL_MIN, GAME_LEVEL_MAX)).strip())
    #         if(1<=tmp<=9):
    #             game_level = tmp
    #         else:
    #             print("잘못된 입력입니다. %s~%s 사이의 난이도를 입력해주세요"%(GAME_LEVEL_MIN, GAME_LEVEL_MAX))
        
    #     except Exception as e:
    #         print(e.with_traceback)
    #         print("잘못된 입력입니다. %s~%s 사이의 난이도를 입력해주세요"%(GAME_LEVEL_MIN, GAME_LEVEL_MAX))

    print ('Game Level : ', game_level)

# step 5
print( '-'* 20)
print('현재까지 입력 상황')
print('gameTitle : ', gameTitle)
print('player_name : ', player_name)
print('game_level : ', game_level)
print( '-'* 20)