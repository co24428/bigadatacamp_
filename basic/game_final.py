import random
import time # 시간

GAME_TITLE_LEN_MAX = 20
PLAYER_NAME_LEN_MAX = 15
GAME_LEVEL_MIN = 1
GAME_LEVEL_MAX = 9
IS_DEV_MODE = True

if not IS_DEV_MODE: # release 버전의 코드

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
    print ('Game Title : ', gameTitle)

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
                print("잘못된 입력입니다. %s~%s 사이의 난이도를 입력해주세요"%(GAME_LEVEL_MIN, GAME_LEVEL_MAX))
            else:
                game_level = tmp_int
                break
    print ('Game Level : ', game_level)
else: 
    gameTitle   = "test game"
    player_name = "guest"
    game_level  = 1

# step 5
if IS_DEV_MODE: # 개발 시에만 작동
    print( '-'* 20)
    print('현재까지 입력 상황')
    print('gameTitle : ', gameTitle)
    print('player_name : ', player_name)
    print('game_level : ', game_level)
    print( '-'* 20)

# step 6
# 인트로
print("="*40)
print("+{0:^38}+".format(gameTitle))
print("+{0:^38}+".format("lv : "+str(game_level)))
print("+{0:^34}+".format(player_name+"의 연대기"))
print("="*40)
print("{0:^40}".format("press enter key!!"))
while True:input();break

# step 7
# 카드 게임

#초기 설정
user_score = 0 # 유저 누계 점수
game_start = True

print("-"*22)
print("User current score : %s "%(user_score))
print("-"*22)

card_deck = list()
card_mark = list("♠♢♥♣")
card_id = list('A23456789') + ['10'] + list('JQK')

card_dic = dict()
for key in card_id:card_dic[ key ] = card_id.index( key ) +1
card_dic["K"] = -5

card_deck = [i+j for i in card_mark for j in card_id]
       
while game_start:
    shuffled_deck = card_deck[:]
    random.shuffle(shuffled_deck)
    use_cards = shuffled_deck[:8]

    user_hand = list()
    com_hand = list()
    card_phase = 1
    for i in range(2):
            user_hand.append(use_cards.pop())
            com_hand.append(use_cards.pop())
    #게임성
    msg ='''
        나의 카드: {}, {} vs com의 카드 : {}, [hidden]
    '''.format(user_hand[0], user_hand[1], com_hand[0])
    print(msg)
    x = 1
    while True:
        time.sleep(0.5)
        print(".", end=" ")
        x += 1
        if x>5: print(); break
    
    while card_phase <= 2:
        print('현재 플레이어의 손패 : ')
        print(user_hand)
        choice = input("1. 카드를 더 받겠습니까?\n2. 승부를 내겠습니까?   (1 or 2) : ")

        if choice == '1':
            user_hand.append(use_cards.pop())
            com_hand.append(use_cards.pop())
            card_phase = card_phase + 1
        else:
            break
    # 게임성
    x = 1
    while True:
        time.sleep(0.5)
        print(".", end="")
        x += 1
        if x>5: print(); break

    # user의 포인트 계산
    user_final_point = 0
    for i in range(0,len(user_hand)-1):
        for j in range(i+1,len(user_hand)):
            user_point_1 = card_dic[user_hand[i][1:]]
            user_point_2 = card_dic[user_hand[j][1:]]
            tmp = user_point_1 + user_point_2

            if user_point_1 == 1 or user_point_2 == 1:
                tmp = tmp * 2
            if user_final_point < tmp:
                user_final_point = tmp

    # com의 포인트 계산
    com_final_point = 0
    for i in range(0,len(com_hand)-1):
        for j in range(i+1,len(com_hand)):
            com_point_1 = card_dic[com_hand[i][1:]]
            com_point_2 = card_dic[com_hand[j][1:]]
            tmp = com_point_1 + com_point_2

            if com_point_1 == 1 or com_point_2 == 1:
                tmp = tmp * 2
            if com_final_point < tmp:
                com_final_point = tmp

    print("user : %s"%user_final_point)
    print("com  : %s"%com_final_point)

    # 승부 계산 후 스코어 할당
    if user_final_point > com_final_point:
        get_score = (user_final_point - com_final_point) * 100 - (card_phase - 1) *20
        user_score += tmp
        print("축하합니다. 이겼습니다. %s score를 획득했습니다."%get_score)
    elif user_final_point < com_final_point:
        get_score = -10
        print("아쉽습니다. 졌습니다. %s score를 잃었습니다."%get_score)
    else:
        print("무승부입니다.")

    print("-"*22)
    print("User current score : %s "%(user_score))
    print("-"*22)
    while True:
        more_game = input("다시 하시겠습니까? (1. yes / 2.  no) : ").upper.strip
        if more_game == "1" or more_game == "Y" or more_game == "YES":
            break
        elif more_game == "2" or more_game == "N" or more_game == "NO":
            game_start = False
            print("Game over!! \n ** Final score : %s"%(user_score))
            break
        else:
            print("정확히 입력해주세요!")
