'''
상위폴더에 우클릭 -> Mark Directory As... -> Sources Root
'''
from class_sample import Shop, PCroom
from class_sample import User, Something, Food, Drink

lotteria = Shop('롯데리아', '패스트푸드점', '신사역')
xeno = PCroom('제노', 'PC방', '신사역', 1300)
xeno.shop_info()


user = User('이한영')
s = Something('알수없는 무언가')
f = Food('햄버거')
d = Drink('제로콜라')

# 다형성을 사용하지 않은 경우
# user.eat_something(s)
# user.eat_food(f)
# user.eat_drink(d)

# 다형성을 사용한 경우
user.eat(s)
user.eat(f)
user.eat(d)