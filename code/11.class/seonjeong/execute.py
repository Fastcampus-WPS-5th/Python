from models import *

customer1 = Customer(1)

order1 = SubwaySandwichOrder(customer1, '파마산', '미트볼', '바베큐', 4000, False)
order1.choose_set(True)
order1.choose_cookie('초코칩')

# worker1 = Worker(100000000)
# worker1.notice_price(4000)
#
# customer1 = Customer('파마산', '미트볼', '바베큐', 4000, '1', 10000)
# worker1.get_paid(4000)
# customer1.pay(4000)
# customer1.meat('튜나')
