def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test span"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)


if __name__ == "__main__":
    scope_test()
    print("In global scope:", spam)


'''
기억하자 !
- 파이썬 변수에 대입되는 객체는 데이터 타입에 따라 변할 수 있거나 (mutable) 변할 수 없는 immutable 성질을 갖는다.
- 위 성질에 따라 객체 변경시 서로 다르게 동작하니, 주의하여 사용해야 한다.
- 클래스/인스턴스 변수, 글로벌/로컬 변수는 서로 다은 유효 범위(scope)를 갖는다. 단, mutable 여부에 따라 예상치 못하게 변경될 수 있다.
- 어떤 변수를 써야 할 지 애매하다면, 유효 범위가 좁은 변수(인스턴스, 로컬)를 사용하는 것이 안전하다.
- 변수를 내부용으로 강제하고 싶다면, 변수 이름을 언더스코어(_)로 시작하자.
- 글로벌 변수 사용은 가능한 피하자.
- 파이썬 코딩 스타일 가이드(PEP 8)를 꼭 따르자.
'''