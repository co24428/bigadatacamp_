GAME_TITLE_LEN_MAX = 20
PLAYER_NAME_LEN_MAX = 15
GAME_LEVEL_MIN = 1
GAME_LEVEL_MAX = 9


print("Enjoy Custom Game world")

# 게임 제목
while 1:

    tmp = input("게임 제목을 입력하시오,\n \
         단 %s자 이내로 입력 가능합니다. : \n"%(GAME_TITLE_LEN_MAX)).strip()

    if  not tmp: 
        print("정확하게 입력하세요!")
    elif len(tmp) > GAME_TITLE_LEN_MAX:
        print(GAME_TITLE_LEN_MAX + "자가 초과되었습니다.")
    else:
        gameTitle = tmp
        break

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
            print("잘못된 입력입니다. %s~%s 사이의 난이도를 입력해주세요"%(GAME_LEVEL_MIN , GAME_LEVEL_MAX))
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