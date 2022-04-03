"""
CPU 바운드
- 프로그램이 실행될 때 실행 속도가 CPU 속도에 의해 제한됨을 의미한다.
- 정말 복잡한 수학 수식을 계산하는 경우에 컴퓨터의 실행속도가 느려진다.
"""


def cpu_bound_func(number: int):
    total = 1
    arrange = range(1, number + 1)
    for i in arrange:
        for j in arrange:
            for k in arrange:
                total += i + j + k


"""
I/O 바운드
- 여기서 I는 Input을 의미하고 O는 Output을 의미한다.
- 프로그램이 실행될 때 실행 속도가 I/O에 의해 제한됨을 의미한다.
- 사용자가 입력을 하고 해당하는 입력에 대해 더하기 100을 한 결과값을 출력해주는 프로그램을 가정할 때
- 사용자가 키보드로 숫자를 입력하는 경우 뿐만 아니라.
  컴퓨터와 컴퓨터끼리 통신을 할 때에도 I/O 바운드가 발생
"""

"""
블로킹
- 바운드에 의해 코드가 멈추게 되는 현상이 일어나는 것
"""

def io_bound_func():
    print("값을 입력해주세요.")
    input_value = input()
    return int(input_value) + 100


if __name__ == "__main__":
    # CPU 바운드
    result = cpu_bound_func(50)
    print(result)

    # I/O 바운드
    result = io_bound_func()
    print(result)
