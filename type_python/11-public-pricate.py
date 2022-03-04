"""
캡슐화 (encapsulation)
객체(object)의 속성과 행위(method)를 하나로 묶고, 구현된 일부를 감추어 은닉한다.(은닉 hiding)


* public vs private

메소드, 변수 앞에 __ (언더바 2개)를 선언해주면
private가 되서 외부에서 접근이 불가능하다!!!
"""


class Robot:
    """
    Robot Class
    """
    population = 0

    # 생성자 함수
    def __init__(self, name, age):
        self.name = name  # 인스턴스 변수
        self._age = age
        Robot.population += 1

    # 인스턴스 메서드
    def say_hi(self):
        # code
        print(f'Grettings. my masters call me {self.name}')

    # 인스턴스 메서드
    def cal_add(self, a, b):
        return a + b

    # 클래스 메서드
    @classmethod
    def how_many(cls):
        print(f'We have {cls.population}!')


class Siri(Robot):
    def __init__(self, name, age):
        super().__init__(name, age)

    @property
    def age(self):
        return self.__age

ss = Robot('yes', 8)

ssss = Siri('a', 9)
print(ssss._age)