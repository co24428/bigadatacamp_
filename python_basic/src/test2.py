# 트럼프 카드 => 타입 4개, 타입별 카드 13장
# 총 카드 수 = 13 * 4 = 52
CARD_TYPE = 4
CARD_PER_TYPE_SIZE = 13
TOTAL_CARD_COUNT = CARD_TYPE * CARD_PER_TYPE_SIZE

# 모든 카드 생성
all_cards = list(range(52))
print('카드의 타입수는', len(all_cards)//13)

#카드 타입 순서
seq = list('♠♢♥♣')
card_id = list('A23456789') + ['10'] + list('JQK')
print(card_id)

target_num = 13
print( seq[int(target_num/CARD_PER_TYPE_SIZE)])
print( card_id[target_num%CARD_PER_TYPE_SIZE])
