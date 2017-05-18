def print_call_func():
    '단순히 "call_func"라는 문자열을 출력해준다'
    print('call_func')


def execute_another_function(another_function):
    '매개변수로 주어진 함수를 실행한다'
    another_function()


# execute_another_function함수에 print_call_func함수를 인자로 전달하여 실행해본다

#f1 = print_call_func
#execute_another_function(f1)

#f2 = print_call_func()
#execute_another_function(f2)


# 1. msg라는 매개변수를 갖는 함수를 정의, 해당 함수는 print(msg)를 실행하는 또 다른 함수를 생성해서 리턴해준다
# 1의 함수명은 return_print_function으로 작성

# 2. execute_another_function에서 위의 함수를 호출해서 만든 함수를 변수 f1에 할당 후, f1변수를 인자로 전달하여 실행

def return_print_function(msg):
    # 이 내부에서 새로운 함수를 생성 (def 어떤함수)하고
    # 아래에서 리턴해주셔야합니다
    def return_function():
        print(msg)

    #return return_function

print(return_print_function)
print(return_print_function('test'))


f1 = return_print_function('이걸출력해주세요')
f1()
#execute_another_function(f1)

