# 모듈 내부에는 변수, 함수, 클래스 등이 여러개 존재할 수 있다.
# 변수
pi = 3.14
name = '블라블라'
# 함수
def add(a,b):
    return a+b
# 클래스
class A():
    def __init__(self):
        print('생성')

if __name__ == '__main__':
    # 테스트
    print('본 모듈의 개발자가 직접 구동시 작동')
    print(add(1,2))
    A()
else:
    # 제 3자가 이 모듈을 가져다가 사용할때
    # __name__ => 파일명 => mod
    # 'mod' == '__main__' => False가 되니 else 코드를 타게 된다
    pass