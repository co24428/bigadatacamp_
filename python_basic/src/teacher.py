GAME_TITLE_LEN_MAX  = 20
PLAYER_NAME_LEN_MAX = 15
GAME_LEVEL_MIN      = 1
GAME_LEVEL_MAX      = 9
IS_DEV_MODE         = True

if not IS_DEV_MODE: # release 버전의 코드가 작동
    # step1
    print( "Enjoy Custom Game world" )
    # step2 
    while True:
        tmp = input("게임 제목을 입력하시오, 단 {}자 \이내로 입력 가능합니다. => ".format(GAME_TITLE_LEN_MAX)).strip()       
        if not tmp:
            print("정확하게 입력하세요!")
        elif len(tmp)>GAME_TITLE_LEN_MAX:
            print(GAME_TITLE_LEN_MAX + "자가 초과되었습니다.") 
        else:
            gameTitle = tmp
            break
    print( 'gameTitle', gameTitle )
    # step 3
    while True:
        tmp = input("플레이어의 닉네임을 입력하시오, 단 %s자로 제한한다\n=>" % PLAYER_NAME_LEN_MAX).strip()
        if not tmp:
            print("정확하게 입력하세요!")
        elif len(tmp)>PLAYER_NAME_LEN_MAX:
            print("%s자가 초과되었습니다." % PLAYER_NAME_LEN_MAX) 
        else:
            player_name = tmp
            break
    # step4
    while True:
        tmp = input("게임 난이도를 입력하시오, 단 %d~%d까지 정수 형태로 제한한다" % (GAME_LEVEL_MIN, GAME_LEVEL_MAX)).strip()
        if not tmp:
            print('정확하게 입력하세요')
            continue
        if not tmp.isnumeric():
            print('1-9까지 사이값으로 정확하게 입력하세요')
            continue
        tmp = int(tmp)
        if tmp>9 or tmp<1:
            print('1-9까지 사이값으로 정확하게 입력하세요')
            continue    
        game_level = tmp
        break
else:# test or dev(개발) 버전으로 코드가 작동
    # 매번 입력받아서 테스트하기 시간이 많아 소요되므로, 값을 고정하여 개발
    gameTitle   = 'test game'
    player_name = 'guest'
    game_level  = 1

# step 5
print( '-'*20 )
print( '현재 까지 입력 상황' )
print( 'gameTitle',   gameTitle )
print( 'player_name', player_name )
print( 'game_level',  game_level )
print( '-'*20 )

# step 6
# 인트로 (가로길이 40칸)
'''
========================================
+           게임제목(중앙정렬)           +
+                lv 레벨값              +
+       "플레이어이름"의 연대기          +
========================================
            press any key!!
'''
print('='*40)
print('+{0:^38}+'.format(gameTitle))
print('+{0:^38}+'.format( 'lv : %s' % game_level ))
print('+{0:^34}+'.format( '"%s"의 연대기' % player_name ))
print('='*40)
print('{0:^40}'.format('press any key!!'))

# step 7
# 카드 게임
# 트럼프 카드 종류 -> 4타입, 타입별로 13장의 카드가 존재
# A는 합산값의 *2을 한다 : ex) A, 3 => (1+3)*2 = 8점
# J=>11, Q=>12, K=-5
'''
♠ : A,2 ~ 10, J, Q, K
♥ : A,2 ~ 10, J, Q, K
♣ : A,2 ~ 10, J, Q, K
◆ : A,2 ~ 10, J, Q, K
'''
# 전체룰
# 1. 게임이 시작하면 카드를 섞는다 => 셔플 => random 모듈을 활용(외장함수, 구현을 위해 사용)
types = list('♠◆♥♣')
nums  = list('A23456789')+['10']+list('JQK')
# 카드 초기화
cards = [ i+j for i in types for j in nums ]
# 점수표 초기화
score_table = dict()
for key in nums:score_table[ key ] = nums.index( key ) +1
import random
random.shuffle(cards)
# 2. 카드를 순서대로 나한장(0), 컴퓨터 한장(1), 나한장(2), 컴퓨터 한장(3) 배치(순서대로 뽑는다)
my_cards  = cards[:8:2]
my_first_cards = my_cards[:2]
com_cards = cards[1:9:2]
com_first_cards= com_cards[:2]


# 플레그 변수:변수로 흐름을 제어한다 => cnt
cnt = 0 # 카드를 추가로 준 횟수
while True:
    choice = input( '1. 카드를 더 받겠습니까? 아니면 2. 승부를 내겠습니까?' )
    if choice == '1' and cnt <2:
        # 3. 플레이어는 최대 2장까지 더 받을수 있다
        #    다시 나한장(4,6), 컴퓨터 한장(5,7) -> 최대 2번까지 가능
        #my_first_cards = my_cards[:3]
        #com_first_cards= com_cards[:3]
        cnt += 1
        # 2->3, 3->4, 4->1번 선택불가
        my_first_cards  = my_cards[:2+cnt]
        com_first_cards = com_cards[:2+cnt]
    elif choice == '2':
        # 판정을 위해 점수를 획득
        myScore  = 0
        comScore = 0
        # 4. 승패 => 내가 가진 카드중 최대값 2개를 합산해서, 특별기능이 있다면 추가 계산해서
        #    높은쪽이 승리한다
        # 5. 한번에 이기면 (내카드의합-컴퓨터카드의합)*100, 카드르 한번 받으면 20점씩 깐다
        for n in my_first_cards:  myScore += score_table[ n[1:] ]
        for n in com_first_cards: comScore += score_table[ n[1:] ]

        print('myScore',myScore)
        print('comScore',comScore)
        
        # 6. 카드를 받으면 1. 카드를 더 받겠습니까? 아니면 2. 승부를 내겠습니까?
        # 7. 다시 하시겠습니까? yes => 다시 1번부터 시작, no-> game over!! 종료
        if myScore > comScore:
            print('You Win, try again? 1.yes, 2.no')
        elif myScore < comScore:
            print('You Lose, try again? 1.yes, 2.no')
        else:
            print('무승부, try again? 1.yes, 2.no')
        break
    else:
        print('정확하게 1 or 2를 입력하세요')
        if cnt == 2:
            print('이미 추가 카드를 다 받았습니다. 2번만 선택할수 있습니다.')
