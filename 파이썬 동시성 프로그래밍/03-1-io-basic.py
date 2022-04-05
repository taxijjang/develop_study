import requests
import time
import os
import threading
from concurrent.futures import ThreadPoolExecutor


def fetcher(session, url):
    print(f"{os.getpid()} process | {threading.get_ident()} url : {url}")
    with session.get(url) as response:
        return response.text


def main():
    urls = ["htltps://naver.com", "https://google.com", "https://instagram.com"] * 10

    with requests.Session() as session:
        result = [fetcher(session, url) for url in urls]
        print(result)


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(end - start)
