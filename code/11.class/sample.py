class Jibsa:
    def __init__(self, name):
        self.name = name


class Goyangyi:
    simkoong_demage = 20
    normal_demage = 10

    def __init__(self, name):
        self.name = name

    def attack(self, user):
        if user.name == "김희진":
            print('고양이 ({})는 {}에게 애교작렬로 {}의 데미지를 줬다.'.format(
                self.name,
                user.name,
                self.simkoong_demage
            ))
        else:
            print('고양이 ({})는 {}에게 할퀴기로 {}의 데미지를 줬다.'.format(
                self.name,
                user.name,
                self.normal_demage
            ))


g1 = Goyangyi('피카츄')
g2 = Goyangyi('꼬부기')
j1 = Jibsa('김희진')
j2 = Jibsa('이한영')

g1.attack(j1)
g1.attack(j2)
g2.attack(j1)
g2.attack(j2)
