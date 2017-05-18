def print_call_func():
    '단순히 "call_func"라는 문자열을 출력해준다'
    pass


def execute_another_function(#매개변수 필요):
    '매개변수로 주어진 함수를 실행한다'
    pass


# execute_another_function함수에 print_call_func함수를 인자로 전달하여 실행해본다
f1 = print_call_func
execute_another_function(f1)

