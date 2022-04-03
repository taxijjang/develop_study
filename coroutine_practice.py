def mul(a, b):
    # mul 함수가 끝나면 변수와 계산식은 사라진다
    c = a * b
    print(f'{c} - mul 함수')
    return c


def main():
    # mul 함수가 끝나면 다시 calc 함수로 돌아온다
    result = mul(1, 4)
    print(f'{result} - calc 함수')


main()

# calc가 메인 루틴(main routine)이면 add는 calc의 서브 루틴(sub routine)임


"""
>>> 코루틴 사용하기
- 메인 루틴에서 서브 루틴을 호출하면 서브 루틴의 코드를 실행한 뒤 다시 메인 루틴으로 돌아옴
- 서브 루틴이 끝나면 서브 루틴의 내용은 모두 사라짐
- 서브 루틴은 메인 루틴에 종속된 관계임
- 코루틴은 방식이 조금 다른데 코루틴(coroutin)은 cooperative routine를 의미하는데 서로 협력하는 루틴이라는 뜻임
- 메인 루틴과 서브 루틴처럼 종속된 관계가 아니라 서로 대등한 관계이며 특정 시점에 상대방의 코드를 실행

- 
"""

"""
>>> 코루틴에 값 보내기
- 코루틴은 제네레이터의 특별한 형태임
- 제너레이터는 yield로 값을 발생시켰지만 코루틴은 yield로 값을 받아올 수 있음
- 다음과 같이 코루틴에 값을 보내면서 코드를 실행할 때는 send 메서드를 사용함
- send 메서드가 보낸 값을 받아오려면 (yield) 형식으로 yield를 괄호로 묶어준 뒤 변수에 저장함

코루틴객체.send(값)
변수 = (yield)
"""


def number_coroutine():
    total = 0
    while True:  # 코루틴을 계속 유지하기 위해 무한 루프 사용
        x = (yield total)  # 코루틴 바깥에서 값을 받아옴, yield를 괄호로 묶어야 함
        total += x


co = number_coroutine()
print(next(co))  # 코루틴 안의 yield까지 코드 실행(최초 실행)

print(co.send(1))  # 코루틴에 숫자 1을 보냄
print(co.send(2))  # 코루틴에 숫자 2를 보냄
print(co.send(3))  # 코루틴에 숫자 3을 보냄

"""
>>> 제너레이터와 코루틴의 차이점을 정리
- 제너레이터는 next 함수(__next__ 메서드)를 반복 호출하여 값을 얻어내는 방식
- 코루틴은 next 함수(__next__ 메서드)를 한 번만 호출한 뒤 send로 값을 주고 받는 방식
"""


def test1():
    print('print 1')
    yield 1
    print('print 2')
    yield 2

g = test1()
print(type(g))
print(next(g))
print(next(g))