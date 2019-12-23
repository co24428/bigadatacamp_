print(__name__, type(__name__))  # __main__ <class 'str'>

# __name__은 2가지 값으로 변경된다
# 이것을 이용해 유기적인 코드를
# 작성할 수 있다. ( 선택적 코드 진행 )
# __main__ <class 'str'>    => 해당파일에서 실행시
# test6 <class 'str'>       => 외부에서 당겨서 실행 시