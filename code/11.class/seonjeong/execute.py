from models import *

subway_sinsa = Subway('신사역점')
worker = Worker(
    subway=subway_sinsa,
    name='박보영'
)
customer1 = Customer(1, '이한영')
# Customer내부에서 해야할 것
# 주문하기(어떤 직원에게)
#   쿠키 선택하기
# 종류 바꾸기(어떤 직원에게, 어떤 Order를)
order1 = SubwaySandwichOrder(customer1, '파마산', '미트볼', '바베큐', 4000, False)
# order1.choose_set(True)
order1.choose_set(False)
order1.choose_cookie('초코칩')
order1.meat = '튜나'

worker.notice_price(order1)
worker.get_paid(order1, 8000)
# customer1.pay(4000)
# customer1.meat('튜나')
