# 1. 숫자를 입력받아 해당하는 숫자 단수의 (x, y, z)형 튜플의 리스트로 곱할수1,2와 결과를 저장하는 함수 make_gugu(num) 작성
# ex) make_gugu(3) -> return [(3,1,3), (3,2,6), ....(3,9,27)]

# 2. 매개변수 print_type과 gugu_list를 가지며,  print_type에 따라 gugu_list를 단순출력 또는 '{} x {} = {}'형으로 출력해주는 함수 print_gugu(print_type, gugu_list) 작성
# ex) print_gugu('simple', <어떤리스트>) -> print((3,1,3),(3,2,6)...)
# print_type은 'simple'과 'normal'로 나눠지며, simple은 튜플을 그냥 출력, normal은 위의 format string형태로 출력

# 3. 매개변수 range, print_type, make_gugu_function, print_gugu_function을 가지고 range에 해당하는 범위의 구구단을 생성하고 출력하는 함수 gugu작성
# gugu함수에서는 매 단마다 줄바꿈 및 이번이 몇 단인지를 알려주는 문자열을 출력

# _function으로 끝나는 매개변수는 함수 자체를 전달
# ex) gugu(range(3,7), 'normal', make_gugu, print_gugu)
# ==== 3단 ====
# 3 x 1 = 3
# ...
# ==== 6단 ====
# 6 x 1 = 6
# ...
# 6 x 9 = 54

def make_gugu(num):
    return [(num, y, num * y) for y in range(1, 10)]

def print_gugu(print_type, gugu_list):
    def print_gugu_simple():
        for item in gugu_list:
            print(item)

    def print_gugu_normal():
        for x, y, z in gugu_list:
            print('{} x {} = {}'.format(x, y, z))

    if print_type == 'simple':
        print_gugu_simple()
    elif print_type == 'normal':
        print_gugu_normal()

def gugu_detail(range_, print_type, make_gugu_function, print_gugu_function):
    # range_변수에는 iterable한 range형 객체가 주어졌다고 가정
    for num in range_:
        print('{val:=^10s}'.format(val=' ' + str(num) + '단 '))
        
        # make_gugu_function을 이용해 (x,y,x*y)형태의 원소들을 갖는 리스트를 생성
        cur_gugu_list = make_gugu_function(num)
        # 생성한 리스트를 인자로 전달해 출력
        print_gugu_function(print_type, cur_gugu_list)

        print('')


gugu(range(2, 4), 'normal', make_gugu, print_gugu)
        
        


