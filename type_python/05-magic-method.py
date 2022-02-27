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
        print('yes!')


droid1 = Robot("R2-D2", code=123123)
droid1.say_hi()

print(dir(droid1))
print(droid1)

droid1()