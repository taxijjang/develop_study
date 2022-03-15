import asyncio
import time


async def say_something(dealy: int, words: str) -> None:
    print(f'Before: {words}')
    await asyncio.sleep(dealy)
    print(f'After: {words}')


async def main():
    """
    비동기지만 동기처럼 동작을 한다..
    start: 01:05:38
    Before: First task started.
    After: First task started.
    Before: Second task started.
    After: Second task started.
    Finished: 01:05:38
    :return:
    """

    print(f'start: {time.strftime("%X")}')
    await say_something(1, 'First task started.')
    await say_something(1, 'Second task started.')

    print(f'Finished: {time.strftime("%X")}')


async def main2():
    """
    비동스럽게 동작
    Starting Tasks:: 01:30:04
    Before: First task started.
    Before: Second task started.
    After: First task started.
    After: Second task started.
    Finished Tasks: 01:30:05
    :return:
    """

    print(f'Starting Tasks:: {time.strftime("%X")}')
    task1 = asyncio.create_task(say_something(1, 'First task started.'))
    task2 = asyncio.create_task(say_something(1, 'Second task started.'))

    await task1
    await task2

    print(f'Finished Tasks: {time.strftime("%X")}')


# asyncio.run(main())
asyncio.run(main2())
