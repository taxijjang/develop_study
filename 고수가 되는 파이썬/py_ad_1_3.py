"""
Section 1
Multithreading - Thread(1) - Basic
Keyword - Threading basic
"""

import logging
import threading
import time


# 스레드 실행 함수
def thread_func(name):
    logging.info(f"Sub-Thread {name}: starting")
    time.sleep(3)
    logging.info(f"Sub-Thread {name}: finishing")


# 메인 영역
if __name__ == "__main__":
    # Logging format 설정
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main-Thread: before creating thread")

    # 함수 인자 확인
    x = threading.Thread(target=thread_func, args=('First',))

    logging.info("Main-Thread: before running thread")

    # 서브 스레드 시작
    x.start()

    # 주석 전후 결과
    # join은 자식 thread의 작업을 기다림
    x.join()

    logging.info("Main-Tread: wait for the thread to finish")

    logging.info("Main-Thread: all done")
