"""
상속 (inheritance)
부모 Class의 속성값과 행위(methods)을 그대로 상속 받고 행위(methods)의 일부분을 수정해야 할 경우
상속받은 자식 Class에서 해당 행위(methods)만 다시 수정하여 사용할 수 있도록 한다.
또한 자식 Class에서 추가적으로 속성값이나 행위(methods)를 정의할 수 있게 한다.

1. 부모 클래스가 갖는 모든 메서드와 속성이 자식 클래스에 그대로 상속된다.

2. 자식 클래스에서 별도의 메서드나 속성을 추가할 수 있다. <<<

3. 메서드 오버라이딩

4. Super( )

5. Python의 모든 클래스는 object 클래스를 상속한다. : 모든 것은 객체이다.

6, mro( ) : 상속 관계를 보여준다.

"""


class Robot:
    """
    [Robot Class]
    Author : 택윤
    Role : ????
    """
    population = 0

    # 생성자 함수
    def __init__(self, name, code):
        self.name = name  # 인스턴스 변수
        self.code = code  # 인스턴스 변수
        Robot.population += 1

    def __str__(self):
        return f'{self.name} robot!!'

    def __call__(self):
        print('call')
        return f'{self.name} is call!!'

    # 인스턴스 메서드
    def say_hi(self):
        # code
        print(f'Grettings. my masters call me {self.name}')

    # 인스턴스 메서드
    def cal_add(self, a, b):
        return a + b

    # 인스턴스 메서드
    def die(self):
        print(f'{self.name} is being destroyed!')
        Robot.population -= 1
        if Robot.population == 0:
            print(f'{self.name} was the last one.')
        else:
            print(f'There are still {Robot.population} robots working.')

    # 클래스 메서드
    @classmethod
    def how_many(cls):
        print(f'We have {cls.population}!')

    # 스태틱 메서드
    @staticmethod
    def are_you_robot():
        print(f'{Robot.population} num!')
        print('yes!')


class Siri(Robot):
    def call_me(self):
        print("네?")

    def cal_mul(self, a, b):
        self.a = a
        return a * b

    @classmethod
    def hello_apple(cls):
        print(f'{cls} hello apple!!')


siri = Siri(name='siri', code=123123)

siri.call_me()

print(siri.cal_mul(7, 8))

print(siri.a)

Siri.hello_apple()
