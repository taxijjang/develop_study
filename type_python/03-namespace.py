"""
#* namespace : 개체를 구분할 수 있는 범위
#* __dict__ : 네임스페이스를 확인할 수 있다.
#*  dir() : 네임스페이스의 key 값을 확인할 수 있다.
#*  __doc__ : class의 주석을 확인한다.
#* __class__ : 어떤 클래스로 만들어진 인스턴스인지 확인할 수 있다.
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


# instance
siri = Robot(name='siri', code=12423232)
# instance
jarvis = Robot(name='jarvis', code=32342323)
# instance
bixby = Robot(name='bixby', code=54434322)

print(Robot.__dict__)
# {'__module__': '__main__', 'population': 3, '__init__': <function Robot.__init__ at 0x7fbe9c10d560>, 'say_hi': <function Robot.say_hi at 0x7fbe9c10d5f0>, 'cal_add': <function Robot.cal_add at 0x7fbe9c10d680>, 'die': <function Robot.die at 0x7fbe9c10d710>, 'how_many': <classmethod object at 0x7fbe9766e410>, '__dict__': <attribute '__dict__' of 'Robot' objects>, '__weakref__': <attribute '__weakref__' of 'Robot' objects>, '__doc__': None}

print(siri.__dict__)
# {'name': 'siri', 'code': 12423232}

print(jarvis.__dict__)
# {'name': 'jarvis', 'code': 32342323}

print(siri.name)
print(bixby.name)

siri.cal_add(2, 3)
# siri의 namespace에는 cal_add가 없는데 어떻게 사용이 가능한건가?
# instance namespace에 없다면 해당 class의 namespace로 넘어가 찾는다.

print(siri.population)
# 위에서 작성한 원리를 이용하여 class 변수에 접근이 가능하다.

# Robot.say_hi()
# say_hi는 class의 namespace에 들어가 있기때문에 이렇게도 사용할 수 있지 않을까?
#  <module>
#     Robot.say_hi()
# TypeError: say_hi() missing 1 required positional argument: 'self'
# class method가 아니고 instance method라고 오류를 알려준다.

Robot.say_hi(siri)
siri.say_hi()

# dir은 instance가 사용할 수 있는 모든 값을 알려준다.
print(dir(siri))
print(dir(Robot))

# 클래스에 작성된 주석을 확인하는 magic method
# [Robot Class]
#    Author : 택윤
#    Role : ????
print(Robot.__doc__)

# instance가 어떤 class로 생성되었는지 확인
# <class '__main__.Robot'>
print(siri.__class__)
