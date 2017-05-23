__all__ = (
    'SubwaySandwichOrder',
    'Worker',
    'Customer',
)


class Subway:
    """서브웨이 매장"""

    def __init__(self, money=None):
        self.money = 10000000 if money is None else money


class Customer:
    def __init__(self, number):
        self.money = 100000
        self.number = number


class SubwaySandwichOrder:
    """서브웨이 샌드위치를 주문하는 클래스다"""
    SET_DICT = {
        True: '세트메뉴',
        False: '단품'
    }

    def __init__(self, customer, bread_type, meat, sauce, price, is_set_menu=None):
        '주문시 필수적으로 골라야 하는 것들'
        self.customer = customer
        self.bread_type = bread_type
        self._meat = meat
        self.sauce = sauce
        self.price = price
        self.is_set = is_set_menu
        if is_set_menu is None:
            is_set = input('세트로 하실래요? (y/N):')
            self.is_set = True if is_set.lower() == 'y' else False
        print('빵은 {}, 고기는 {}, 소스는 {}를 선택했습니다. {}이며, 가격은 {}입니다.'.format(
            self.bread_type,
            self._meat,
            self.sauce,
            '{}'.format(self.SET_DICT[self.is_set]),
            self.price))

    def choose_set(self, is_set):
        '세트인지 단품인지 결정하기'
        self.is_set = is_set
        print('주문번호 {}번 고객님은 {}를 선택했습니다'.format(
            self.customer.number,
            '{}'.format(self.SET_DICT[self.is_set]),
        ))

    def choose_cookie(self, cookie_type):
        '세트일 경우 쿠키 종류 선택하기'
        if self.is_set:
            self.cookie_type = cookie_type
            print('주문번호 {}번 고객님은 {}쿠키를 선택했습니다.'.format(self.customer.number, self.cookie_type))
        else:
            print('단품고객은 쿠키를 선택할 수 없습니다.')

    @property
    def meat(self):
        return self._meat

    @meat.setter
    def meat(self, new_meat):
        '고기 종류를 변경하기'
        self._meat = new_meat
        available_meat = {
            '미트볼',
            '튜나',
            '에그마요',
        }
        if new_meat in available_meat:
            print('고기 종류를 {}로 변경하였습니다.'.format(self._meat))
        else:
            print('그런 메뉴는 없습니다.')


class Worker(SubwaySandwichOrder):
    '서브웨이 직원 클래스'
    worker_money = 100000000

    def __init__(self, worker_money):
        '계산을 하기 위해 돈 속성을 추가해준다.'
        self.work_money = worker_money

    def notice_price(self, price):
        '가격 정보 알리기'
        self.price = price
        print('주문하신 샌드위치의 가격은 {}원 입니다'.format(self.price))

    def get_paid(cls, price):
        '손님이 낸 돈 받기'
        cls.worker_money += price
        print('샌드위치값으로 {}원을 받았습니다'.format(price))

# class Customer(SubwaySandwichOrder):
#     customer_money = 10000
#
#     def __init__(self, bread_type, meat, sauce, price, customer_num, money):
#         super().__init__(bread_type, meat, sauce, price)
#         '고객번호와 가진 돈을 초기화 속성으로 지정해주기'
#         self.customer_num = customer_num
#         self.money = money
#
#     def pay(cls, price):
#         '샌드위치값 계산하기'
#         cls.customer_money -= price
#         print('{}원을 계산하고 {}원이 남았습니다'.format(price, cls.customer_money))
