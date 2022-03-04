"""
# polymorphism - 다형성
# 여러 형태를 가질 수 있도록 한다. 즉, 객체를 부품화 할 수 있도록 한다.
# 같은 형태의 코드가 다른 동작을 하도록 하는 것
"""


class Robot:
    """
    Robot Class
    """
    __population = 0

    def __init__(self, name, age):
        self.__name = name  # 인스턴스 변수
        self.__age = age
        Robot.__population += 1

    @property
    def name(self):
        return f"yoon {self.__name}"

    @property
    def age(self):
        return self.age

    @age.setter
    def age(self, new_age):
        if new_age < 0:
            raise ValueError('invalid range to age!')
        self.__age = new_age

    def __say_hi(self):
        print(f'Grettings. my masters call me {self.__name}')

    def cal_add(self, a, b):
        return a + b

    @classmethod
    def how_many(cls):
        print(f'We have {cls.__population}!')


class Siri(Robot):
    def say_apple(self):
        print('hello my apple')


class SiriKo(Robot):
    def say_apple(self):
        print('안녕하세요')


class Bixby(Robot):
    def say_samsung(self):
        print('안녕하세요')
