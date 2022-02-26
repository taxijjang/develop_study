"""
- 강의 노트

__init__
- 강의에서 등장한 __init__ 메서드는 생성자 함수라고 하며 인스턴스가 만들어질 때 인스턴스를 초기화합니다.

- __init__ 메서드는 특별한 기능이 있는 매직 메서드중 하나이며 함수 이름을 다른 이름으로 바꿀 수 없습니다.

- 매직 메서드는 나중에 깊게 설명해드립니다.

- 관련 문서 : https://docs.python.org/3/reference/datamodel.html?highlight=__init__#object.__init__

attribute
- 인스턴스에는 데이터(속성값)와 메서드(속성메서드)로 이루어지는 클래스 attribute가 있습니다.
- 메서드는 함수인데, 그 첫 번째 파라미터는 호출된 인스턴스 자신(self)입니다. -> 후에 강의에서 증명합니다.

- attribute는 점(.) 뒤에 나오는 모든 이름입니다. 인스턴스.attribute, 인스턴스.attribute( )

심화 내용 (지금 다 이해하실 필요 없습니다. 후에 강의를 보시고 다시 글을 읽어주세요. :)
- 클래스 인스턴스 생성이란 함수 표기법 (my_func( ))을 사용하여 초기 상태의 객체를 생성하는 것입니다.

- Cal라는 클래스가 있다고 가정합시다. Cal( )을 호출하여 인스턴스를 생성하는데 이때  Cal( )을 생성자라고 합니다.

- 이 생성자를 호출하면 Cal.__new__( )라는 매직 메서드가 호출되어 인스턴스가 할당되고 그 다음 Cal.__init__( ) 메서드가 인스턴스를 초기화합니다.
"""


class Cal:
    # 생성자: 메모리에 올라오는 순간 즉시 실행된다.
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b


# Instancef
cal1 = Cal(1, 2)
cal2 = Cal(3, 4)

print(cal1.a)
print(cal1.b)
print(cal1.add())

cal1.a = 7

print(cal2.a)
print(cal2.b)
