import random

GAME_TITLE_LEN_MAX = 20
PLAYER_NAME_LEN_MAX = 15
GAME_LEVEL_MIN = 1
GAME_LEVEL_MAX = 9
IS_DEV_MODE = True

if not IS_DEV_MODE: # release 버전의 코드가 작동

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
else: # test or dev(개발) 버전으로 코드가 작동
    # 매번 입력받아 테스트하기 시간이 많이 소요되므로, 값을 고정하여 개발
    gameTitle   = "test game"
    player_name = "guest"
    game_level  = 1

# step 5
print( '-'* 20)
print('현재까지 입력 상황')
print('gameTitle : ', gameTitle)
print('player_name : ', player_name)
print('game_level : ', game_level)
print( '-'* 20)

# step 6
# 인트로
'''
========================================
+           게임제목(중앙정렬)           +
+              1v : 레벨값              +
+        "플레이어 이름"의 연대기        +
========================================
            press any key!!
'''
# print("{0:=^40}".format(""))
print("="*40)
print("+{0:^38}+".format(gameTitle))
print("+{0:^38}+".format("lv : "+str(game_level)))
print("+{0:^34}+".format(player_name+"의 연대기")) # 한글은 2byte다
print("="*40)
print("{0:^40}".format("press any key!!"))
# 노가다 >> print(" "*12,"press any key!!"," "*13)

# step 7
# 카드 게임
# 트럼프 카드의 종류 -> 4타입, 타입별로 13장의 카드가 존재
# A는 합산값의 *2을 한다 : ex) A, 3 => (1+3)*2
# J => 11, Q => 12, K => -5
'''
♠  : A, 2 ~ 10, J, Q, K
♣  : A, 2 ~ 10, J, Q, K
♥  : A, 2 ~ 10, J, Q, K
♢ : A, 2 ~ 10, J, Q, K
'''

# 전체 룰
# 1. 게임이 시작하면 카드를 섞는다 => 셔플 
#                                     =>random 모듈을 활용(외장함수, 구현을 위해 사용)
# 2. 카드를 순서대로 나 1장(0), 컴퓨터 1장(1), 나 1장(2), 컴퓨터 1장(3) 배치 (순서대로 뽑는다)
# 3. 플레이어는 최대 2장까지 더 받을 수 있다.
#    다시 나 한장(4,6), 컴퓨터 1장(5,7) -> 최대 2번까지 가능
# 4. 승패 => 내가 가진 카드 중 최대값 2개를 합산해서, 특별 기능이 있다면 추가 계산해서
#    높은 쪽이 승리한다.
# 5. 한번에 이기면 (내 카드의 합 - 컴퓨터 카드의 합)*100점, 카드를 한 번 받으면 20점씩 마이너스.
# 6. 카드를 받으면 1. 카드를 더 받겠습니까? 2. 아니면 승부를 내겠습니까?
# 7. 다시 하시겠습니까? yes => 다시 1번부터 시작, no => game over!! > 종료

# ** 여기서는 상위 장만 사용하므로 셔플 후 나머지는 버려도 된다.
# 특징(feature)를 잡아서 자료구조를 잘 잡아라.
# 최대한 간편하게, 정수로 처리할 수 있게끔( 패턴 파악 )

#유저 누계 점수
user_score = 0
game_start = True

print("-"*22)
print("User current score : %s "%(user_score))
print("-"*22)

while game_start:
    card_deck = list()
    card_mark = list("♠♢♥♣")
    card_id = list('A23456789') + ['10'] + list('JQK')
    
    card_dic = dict()
    for key in card_id:card_dic[ key ] = card_id.index( key ) +1
    # card_dic = {
    #     'A':1,
    #     '2':2,
    #     '3':3,
    #     '4':4,
    #     '5':5,
    #     '6':6,
    #     '7':7,
    #     '8':8,
    #     '9':9,
    #     '10':10,
    #     'J':11,
    #     'Q':12,
    #     'K':13
    # }

    for i in card_mark:
        for j in range(0,13):
            card_deck.append(i+ card_id[j])
            
    # random.seed(1)
    random.shuffle(card_deck)
    use_cards = card_deck[:8]

    user_hand = list()
    com_hand = list()
    card_phase = 1
    for i in range(2):
            user_hand.append(use_cards.pop())
            com_hand.append(use_cards.pop())

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


    # user의 포인트 계산
    user_final_point = 0
    for i in range(0,len(user_hand)-1):
        for j in range(i+1,len(user_hand)):
            user_point_1 = card_dic[user_hand[i][1:]]
            user_point_2 = card_dic[user_hand[j][1:]]
            tmp = user_point_1 + user_point_2

            if user_point_1 == 1 or user_point_2 == 1:
                tmp = tmp * 2
            if user_point_1 == 13 or user_point_2 == 13:
                tmp = tmp -18
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
            if com_point_1 == 13 or com_point_2 == 13:
                tmp = tmp -18
            if com_final_point < tmp:
                com_final_point = tmp


    print("user : %s"%user_final_point)
    print("com  : %s"%com_final_point)

    # 승부 계산 후 스코어 할당

    if user_final_point > com_final_point:
        tmp = (user_final_point - com_final_point) * 100 - (card_phase - 1) *20
        user_score += tmp
        print("축하합니다. 이겼습니다. %s score를 획득했습니다."%tmp)
    elif user_final_point == com_final_point:
        print("무승부입니다.")
    else:
        print("졌습니다.")


    
    print("-"*22)
    print("User current score : %s "%(user_score))
    print("-"*22)
    more_game = input("다시 하시겠습니까? (yes / no) : ")
    if more_game == "yes":
        pass
    else:
        game_start = False
        print("Game over!! \n ** Final score : %s"%(user_score))



# 5. 한번에 이기면 (내 카드의 합 - 컴퓨터 카드의 합)*100점, 카드를 한 번 받으면 20점씩 마이너스.
# -> 지면 0점
# 7. 다시 하시겠습니까? yes => 다시 1번부터 시작, no => game over!! > 종료