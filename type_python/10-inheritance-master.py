"""
상속 (inheritance)
부모 Class의 속성값과 행위(methods)을 그대로 상속 받고 행위(methods)의 일부분을 수정해야 할 경우
상속받은 자식 Class에서 해당 행위(methods)만 다시 수정하여 사용할 수 있도록 한다.
또한 자식 Class에서 추가적으로 속성값이나 행위(methods)를 정의할 수 있게 한다.

1. 부모 클래스가 갖는 모든 메서드와 속성이 자식 클래스에 그대로 상속된다.

2. 자식 클래스에서 별도의 메서드나 속성을 추가할 수 있다.

3. 메서드 오버라이딩

4. Super( )

5. Python의 모든 클래스는 object 클래스를 상속한다. : 모든 것은 객체이다. <<<

6, mro( ) : 상속 관계를 보여준다. <<<

"""
import tkinter


class Robot(object):
    """
    [Robot Class]
    Author : 택윤
    Role : ????
    """
    population = 0

    # 생성자 함수
    def __init__(self, name):
        self.name = name  # 인스턴스 변수
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
    def call_me(self):
        print("네?")

    def cal_mul(self, a, b):
        return a * b


print(Siri.mro())  # [<class '__main__.Siri'>, <class '__main__.Robot'>, <class 'object'>]

print(Robot.mro())  # [<class '__main__.Robot'>, <class 'object'>]

print(object)

print(dir(object))

print(object.__name__)

print(int.mro())


class A:
    def hi(self):
        print('a')


class B:
    def hi(self):
        print('b')


class C:
    def hi(self):
        print('c')


# 다중 상속 했을때는 왼쪽이 제일 상단 D -> C -> B -> A
class D(C, B, A):
    pass


print(D.mro())

d = D()

d.hi()