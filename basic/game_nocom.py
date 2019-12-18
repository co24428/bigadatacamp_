print("Enjoy Custom Game world")

# 게임 제목
while 1: 
    tmp = input("게임 제목을 입력하시오,\n \
         단 20자 이내로 입력 가능합니다. : \n").strip()

    if not tmp:
        print("정확하게 입력하세요!")
    elif len(tmp) > 20:
        print("20자가 초과되었습니다.")
    else:
        gameTitle = tmp
        break
print ('Game Title : ', gameTitle)

# 플레이어 이름
while 1:
    tmp = input('플레이어의 닉네임을 입력하시오,\n \
        단 15자로 제한한다. : \n').strip()

    if not tmp:
        print("정확하게 입력하세요!")
    elif len(tmp) > 15:
        print("15자가 초과되었습니다.")
    else:
        player_name = tmp
        break
print ('player Name : ', player_name)

# 게임 난이도
while 1:
    tmp = input('게임 난이도를 입력하시오,\n \
        단 1~9까지 정수 형태로 제한한다. : \n').split()
    if tmp.isnumeric():
        tmp_int = int(tmp)
        if tmp_int > 9 or tmp_int < 1:
            print("잘못된 입력입니다. 1~9 사이의 난이도를 입력해주세요")
        else:
            game_level = tmp_int
            break
    elif not tmp:
        print("정확하게 입력하세요!")
    else:
        print("잘못된 입력입니다. 숫자를 입력해주세요")

print ('Game Level : ', game_level)
