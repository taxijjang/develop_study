class A:
    def name(self):
        print('A')


class B(A):
    def name(self):
        print('B')


class C(A):
    def name(self):
        print('C')


class D(A, B, C):
    pass


d = D()


d.name()

print(D.__mro__)


### super()는 각 단계에서 다음 메서드를 찾기 때문에 First에서 super() 호출시
### Second의 __init__를 호출하게 된다.

class First:
    def __init__(self):
        super(First, self).__init__()
        print("first")


class Second:
    def __init__(self):
        super(Second, self).__init__()
        print("second")


class Third(First, Second):
    def __init__(self):
        super(Third, self).__init__()
        print("third")


third = Third()
"""
>>> second
>>> first
>>> third
"""
