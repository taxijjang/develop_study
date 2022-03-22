"""
Section 1
Multithreading = Python`s GIL
Keyword - CPython, 메모리관리, GIL 사용 이유
"""

"""

Gil(Global Interpreter Lock)
    python의 실행 원리
    - python.py 코드를 내부적으로 Cpython이 해석해서 byte code로 변환
    python code가 byte code로 변환
    (1). CPython -> Python(bytecode) 실행시 여러 thread 사용할 경
        단일 스레드만이 python object에 접근하게 제한하는 mutex
    (2). Cpython 메모리 관리가 취약(부족하기) 때문(즉, Tread-safe)
    (3). cpu의 성능도 좋고 단일 스레드로 충분히 빠르다.
    (4). multi process를 사용 가능(Numpy/ Scipy)등 Gil 외부 영역에서 효율적인 코딩이 가능
    (5). 병렬 처리는 Multiprocessing, asyncio 선택지 다양한.
    (6). thread 동시성 완벽 처리를 위해 -> Jython, IronPython, Stackless Python 등이 존재
    
    
"""