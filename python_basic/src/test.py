# 단위 테스트용
import random

# print(random.randint(1, 3) ) # Integer from 1 to 10, endpoints included

ori_data = [1,2,3,4,5]
target_data = ori_data[:]
# 난 항상 일정하게 섞기는 값을 원한다 -> 난수가 항상 일정하게 나온다. -> seed 고정
# seed를 고정하면 난수가 나오는 순서가 동일 
# => 일정한 결과를 낼 수 있다
# => 항상 같은 결과가 나오는 실험환경 구축 가능
# => 변수를 바꿔가면서 영향성 등등 분석할 수 있다. -> 딥러닝
# seed를 고정하지 않으면, 현재 시간으로 설정된다.
random.seed(12) 

random.shuffle(target_data) # 섞기 함수
print(ori_data)
print(target_data)