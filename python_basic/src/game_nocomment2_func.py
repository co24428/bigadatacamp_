# 1. 모듈 가져오기
import random # 모듈가져오기
import time   # 시간

# 2. 전역변수 정의
GAME_TITLE_LEN_MAX  = 20
PLAYER_NAME_LEN_MAX = 15
GAME_LEVEL_MIN      = 1
GAME_LEVEL_MAX      = 9
IS_DEV_MODE         = False
types = list('♠◆♥♣')
nums  = list('A23456789')+['10']+list('JQK')
cards = [ i+j for i in types for j in nums ]
score_table = dict()
for key in nums:score_table[ key ] = nums.index( key ) +1
score_table[ 'K' ]  = -5
player_name         = None
game_level          = 0 
myTotalScore        = 0

# 3. 함수들 나열
# 함수 지향적 프로그램은 반드시(대체적으로) 시작점이 존재한다
# 시작점 엔트리 포인트!!
def main():
    step1()
    # step2() 안의 gameTitle과 서로 다른 변수이다. 
    #   => 편의성 이름만 동일하게 사용(이후 코드 수정 최소화)
    gameTitle = step2()
    step3()
    step4()
    step5()
    step6(gameTitle)
    step7()

def step1():
    print( "Enjoy Custom Game world" )

def step2():
    while True:
        tmp = input("게임 제목을 입력하시오, 단 {}자 \이내로 입력 가능합니다. => ".format(GAME_TITLE_LEN_MAX)).strip()       
        if not tmp:
            print("정확하게 입력하세요!")
        elif len(tmp)>GAME_TITLE_LEN_MAX:
            print(GAME_TITLE_LEN_MAX + "자가 초과되었습니다.") 
        else:
            gameTitle = tmp
            break
    # gameTitle은 절차적 코드에서는 그냥 사용해도 되나,
    # 함수지향적을 전개해서 함수 내부로 가면 지역변수가 된다.
    # 함수밖에서 사용이 불가하므로, 1. 값을 리턴하거나, 
    #                             2. 전역 변수로 빼야한다.
    return gameTitle

def step3():
    while True:
        global player_name
        tmp = input("플레이어의 닉네임을 입력하시오, 단 %s자로 제한한다\n=>" % PLAYER_NAME_LEN_MAX).strip()
        if not tmp:
            print("정확하게 입력하세요!")
        elif len(tmp)>PLAYER_NAME_LEN_MAX:
            print("%s자가 초과되었습니다." % PLAYER_NAME_LEN_MAX) 
        else:
            player_name = tmp
            break
    # step4

def step4():
    while True:
        global game_level

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

def step5():pass
def step6(gameTitle):
    print('='*40)
    print('+{0:^38}+'.format(gameTitle))
    print('+{0:^38}+'.format( 'lv : %s' % game_level ))
    print('+{0:^34}+'.format( '"%s"의 연대기' % player_name ))
    print('='*40)
    print('{0:^40}'.format('press enter key!!'))
    while True:input();break # 한줄에 여러문장을 기술할때는 구분자로 ; 사용
def step7():
    isOneGaming = True
    while isOneGaming:
        gamecards = cards[:]
        random.shuffle(gamecards)
        my_cards  = gamecards[:8:2]
        my_first_cards = my_cards[:2]
        com_cards = gamecards[1:9:2]
        com_first_cards= com_cards[:2]

        cnt = 0 # 카드를 추가로 준 횟수
        isGaming = True # 게임중이다
        while isGaming:
            msg = '''
                나의카드:%s, %s  vs 컴의카드 : %s, [HIDEN]
            ''' % ( my_first_cards[0], my_first_cards[1], com_first_cards[0] )
            print( msg )
            # 게임성을 데코레이션 정도로 2초정도 대기시킨다
            x = 1
            while True:
                time.sleep(0.5)
                print('-'*x)
                x += 1
                if x == 4:break
            choice = input( '1. 카드를 더 받겠습니까? 아니면 2. 승부를 내겠습니까?' )
            if choice == '1' and cnt <2:
                cnt += 1
                my_first_cards  = my_cards[:2+cnt]
                com_first_cards = com_cards[:2+cnt]
            elif choice == '2':
                # 비교시 A는 합산값의 *2을 한다 : 
                # ex) A, 3 => (1+3)*2 = 8점
                # 저장= (내점수-컴점수)*100 + 카드를 더 받은 횟수*(-20)    
                myScore  = 0
                comScore = 0
                for n in my_first_cards:  myScore += score_table[ n[1:] ]
                for n in com_first_cards: comScore += score_table[ n[1:] ]
                print('myScore',myScore)
                print('comScore',comScore)
                
                if myScore > comScore:
                    # 점수 산출 및 표시
                    myGetScore = (myScore-comScore)*100 + cnt*(-20)
                    # 내점수에 합산
                    myTotalScore += myGetScore
                    print('축하합니다. %s점 획득하였습니다. 현재 총 %s점입니다.' % (myGetScore,myTotalScore) )
                    print('You Win, try again? 1.yes, 2.no')
                elif myScore < comScore:
                    # 점수 산출 및 표시
                    myGetScore = -5 # 지면 5점 뺀다
                    # 내점수에 합산
                    myTotalScore += myGetScore
                    print('아쉽습니다. %s점 잃었습니다. 현재 총 %s점입니다.' % (myGetScore,myTotalScore) )
                    print('You Lose, try again? 1.yes, 2.no')
                else:
                    # 점수 산출 및 표시
                    myGetScore = 0
                    print('아~ 비겼네요.. 점수 변동없습니다.' )
                    print('무승부, try again? 1.yes, 2.no')
                # 게임 저장
                # 1 혹은 2를 입력받으면 게임을 끝내거나, 게임을 다시        
                while True:
                    # 대문자 소문자 어떤것을 넣던 OK
                    # 내부적으로는 결정한다(어느쪽으로 처리할것인지)
                    c_number = input().strip().lower()
                    if c_number=='1' or c_number=='y' or c_number=='yes':
                        # 현재 게임 한판 종료
                        isGaming = False
                        # 현재 계속할지 말지 입력을 종료
                        break
                    elif c_number=='2' or c_number=='n' or c_number=='no':
                        # 현재 게임 한판 종료
                        isGaming = False
                        # 게임 전체를 종료
                        isOneGaming = False
                        # 현재 계속할지 말지 입력을 종료
                        break
                    else:
                        print('정확하게 1.yes, 2.no 중에 하나를 입력하세요')
            else:
                print('정확하게 1 or 2를 입력하세요')
                if cnt == 2:
                    print('이미 추가 카드를 다 받았습니다. 2번만 선택할수 있습니다.')

    print( 'bye bye ~ \ngame over!!' )

# 4. 프로그램 시작
#
    # # __name__ 이 변수는 그냥 사용이 가능하고, 값이 
    # # 프로그램을 구동하는 방식에 따라 2가지로 변경된다
    # # 1) python 파일명.py로 구동하면 => __name__ => '__main__' 세팅됨
    # # 2) 누군가가 파일명.py를 가져와서 사용하면 => __name__ => '파일명'
    # print( '__name__ => ', __name__ )
    # if __name__ == '__main__':
main()