"""
public
    외부에서 제한없이 접근/수정 가능

protected
    외부에서는 접근 불가능, 상속받은 클래스에서는 접근 가능
    
private
    내부에서만 접근/수정 가능
        -> 외부 접근 가능하도록 property사용
"""


class Shop2:
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
