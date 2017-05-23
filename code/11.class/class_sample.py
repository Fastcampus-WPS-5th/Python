class Shop:
    description = 'Python Shop Class'

    def __init__(self, name, shop_type, address):
        self.name = name
        self.__shop_type = shop_type
        self.address = address

    def shop_info(self):
        print('상점 ({})\n  유형: {}\n  주소: {}'.format(
            self.name,
            # self._Shop__shop_type
            self.__shop_type,
            self.address
        ))

    @property
    def shop_type(self):
        return self.__shop_type

    @shop_type.setter
    def shop_type(self, new_shop_type):
        available_type_set = {
            '패스트푸드점',
            '편의점',
            'PC방'
        }
        if new_shop_type in available_type_set:
            self.__shop_type = new_shop_type
        else:
            print('{}은 허용되지 않습니다'.format(new_shop_type))

    @classmethod
    def change_description(cls, description):
        cls.description = description

    @staticmethod
    def print_hello():
        print('hello')


class PCroom(Shop):
    pass
