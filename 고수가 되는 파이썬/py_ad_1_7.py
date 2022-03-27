"""
Section 1
Multithreading - Thread(5) - Prod vs Cons Using Queue
Keyword - 생산자 소비자 패턴(Producer/Consumer pattern)
"""

"""
Producer-Consumer Pattern
(1). 멀티스레드 디자인 패턴의 정석
(2). 서버 측 프로그래밍 핵심
(3). 주로 허리역활 중요

Python Event 객체
(1). Flag 초기화(0)
(2). Set() -> 1, Clear() -> 0, wait(1 -> 리턴, 0 -> 대기), isSet() -> 현 플래그 상태 return
"""

import concurrent.futures
import logging
import queue
import random
import threading
import time


# 생산자
def producer(queues, events):
    """ 네트워크 대기 상태라 가정(서버) """
    while not events.is_set():
        message = random.randint(1, 11)
        logging.info(f'Producer got message: {message}')
        queues.put(message)

    logging.info('Producer received event Exiting')


# 소비자
def consumer(queues, events):
    """ 응답 받고 소비하는 것으로 가정 or DB 저장"""
    while not events.is_set() or not queues.empty():
        message = queues.get()
        logging.info(f'Consumer storing message: {message}, (size={queues.qsize()}')

    logging.info('Cunsumer received event Exiting')


if __name__ == '__main__':
    # Logging format 설정
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    # 사이즈 중요
    pipeline = queue.Queue(maxsize=10000000)

    # 이벤트 플래그 초기 값 0
    event = threading.Event()

    # With Context 시작
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        executor.submit(producer, pipeline, event)
        executor.submit(consumer, pipeline, event)

    # 실행 시간 조정
        time.sleep(10)

        logging.info("Main: about to set event")

    # 프로그램 종료
        event.set()
