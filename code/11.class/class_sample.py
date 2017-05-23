"""
public
    외부에서 제한없이 접근/수정 가능

protected
    외부에서는 접근 불가능, 상속받은 클래스에서는 접근 가능
    
private
    내부에서만 접근/수정 가능
        -> 외부 접근 가능하도록 property사용
"""


class Shop:
    description = 'Python Shop Class'

    def __init__(self, name, shop_type, address):
        self.name = name
        self._shop_type = shop_type
        self.address = address

    def shop_info(self):
        print('상점 ({})\n  유형: {}\n  주소: {}'.format(
            self.name,
            # self._Shop__shop_type
            self._shop_type,
            self.address
        ))

    @property
    def shop_type(self):
        return self._shop_type

    @shop_type.setter
    def shop_type(self, new_shop_type):
        available_type_set = {
            '패스트푸드점',
            '편의점',
            'PC방'
        }
        if new_shop_type in available_type_set:
            self._shop_type = new_shop_type
        else:
            print('{}은 허용되지 않습니다'.format(new_shop_type))

    @classmethod
    def change_description(cls, description):
        cls.description = description

    @staticmethod
    def print_hello():
        print('hello')


class PCroom(Shop):
    def __init__(self, name, shop_type, address, price):
        super().__init__(name, shop_type, address)
        self.price = price

    def shop_info(self):
        print('PC방 ({})\n  유형: {}\n  주소: {}\n  요금: {}'.format(
            self.name,
            # self._Shop__shop_type
            self._shop_type,
            self.address,
            self.price
        ))


# 다형성 및 덕타이핑
# 다형성: 동일한 실행이지만, 다른 동작을 수행할 수 있도록 허용하는 것
class User:
    def __init__(self, name):
        self.name = name

    def eat(self, anything):
        anything.eat()

    def eat_something(self, something):
        something.eat()

    def eat_food(self, food):
        food.eat()

    def eat_drink(self, drink):
        drink.eat()


class Something:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print('{}는 무엇인지 몰라 먹을 수 없다!'.format(self.name))


class Food(Something):
    def eat(self):
        print('{}을 먹었다. 배가 부르다!'.format(self.name))


class Drink(Something):
    def eat(self):
        print('{}을 마셨다. 갈증이 해소된다!'.format(self.name))


# 자신만의 클래스 만들기
class 무언가:
    def __init__(self, 값1, 값2, 값3):
        self.속성1 = 값1
        self.속성2 = 값2
        self.속성3 = 값3

    def 메서드1(self):
        pass

    def 메서드2(self):
        pass

    def 메서드3(self):
        pass
