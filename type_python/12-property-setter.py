"""
# [property]
# 인스턴스 변수 값을 사용해서 적절한 값으로 보내고 싶을 때
# 인스턴스 변수 값에 대한 유효성 검사 및 수정
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


droid = Robot('R2-D2', 2)
print(droid.name)