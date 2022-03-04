"""
# composition
# 다른 클래스의 일부 메서드를 사용하고 싶지만, 상속은 하고 싶지 않을 경우
# 1. 부모 클래스가 변하면 자식 클래는 계속 수정되어야 한다.
# 2. 부모 클래스의 메서드를 오버라이딩 하는 경우 내부 구현 방식의 얕은 이해로 오류가 생길 가능성 증가.
    오버라이딩 하려는 메서드가 여러 군데에서 사용중일때 이 모든것을 이해하지 않고 오버라이딩을 할 수 가능성이 있다.

컴포지션이란, 상속과 다르게 단순히 사용한다는 개념이다. 즉,
기존의 상속 개념에서의 자식클래스가 부모클래스의 모든 속성을 물려받는게 아니라,
자식클래스가 필요한 속성만 부모클래스로부터 가져와 사용하는 것이다.
일반적으로 상속은 암시적 선언이라고 하며, 컴포지션은 명시적 선언이라고 한다.
출처: https://doorbw.tistory.com/234 [Tigercow.Door]
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
        self.cal_add(1, 3)
        print(f'Grettings. my masters call me {self.__name}')

    def cal_add(self, a, b):
        return a + b + 1

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


class BixbyCal:
    def __init__(self, name, age=None):
        self.Robot = Robot(name, age)

    def cal_add(self, a, b):
        return self.Robot.cal_add(a, b)
