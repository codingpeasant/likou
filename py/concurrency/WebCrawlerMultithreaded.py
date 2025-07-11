# https://leetcode.ca/2019-04-25-1242-Web-Crawler-Multithreaded/

from collections import defaultdict, deque
from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Condition, Lock, Thread
import threading
from time import sleep
from typing import List


class HtmlParser:
    def __init__(self, urls: list[str], edges: list[list[int]]):
        self.graph = defaultdict(list)
        for a, b in edges:
            self.graph[urls[a]].append(urls[b])
        print(self.graph)

    def get_links_on_page(self, url: str):
        print(f"getting urls for {url}")
        sleep(0.5)  # takes a bit time
        return self.graph[url]

    def get_html_content(self, url: str):
        print(f"getting html for {url}")
        sleep(1)  # takes a bit longer time
        return url


class Solution:
    def crawlBFS(self, startUrl: str, htmlParser: "HtmlParser") -> List[str]:
        seen = set(
            [startUrl]
        )  # Keep track of seen URLs to avoid re-crawling the same URL
        taskQ = deque([startUrl])
        while taskQ:
            url = taskQ.popleft()
            html = htmlParser.get_html_content(
                url
            )  # bottle neck 1 - also needs error handling and retry
            for link in htmlParser.get_links_on_page(html):  # bottle neck 2
                if link not in seen:
                    seen.add(link)
                    taskQ.append(link)
        return list(seen)

    def crawlConcurrency(self, startUrl: str, htmlParser: "HtmlParser") -> List[str]:
        seen = set([startUrl])
        taskQ = deque([startUrl])
        cond = Condition()
        threads = []
        stop_flag = False

        def worker():
            while True:
                with cond:
                    print(f"{threading.current_thread().name} is waiting...")
                    cond.wait_for(lambda: len(taskQ) > 0 or stop_flag)
                    if stop_flag:
                        print(f"{threading.current_thread().name} terminated")
                        break
                    if taskQ:
                        url = taskQ.popleft()
                    else:
                        continue
                # Do slow operations outside the lock!
                print(f"{threading.current_thread().name} picking up {url}")
                html = htmlParser.get_html_content(url)
                for link in htmlParser.get_links_on_page(html):
                    with cond:
                        if link not in seen:
                            seen.add(link)
                            taskQ.append(link)
                            cond.notify_all()
                print(f"{threading.current_thread().name} done")

        for i in range(5):
            t = Thread(target=worker, name=str(i))
            t.start()
            threads.append(t)

        # Wait for 10 seconds, then unblock all threads
        sleep(8)
        with cond:
            stop_flag = True
            cond.notify_all()
        for t in threads:
            t.join()

        return list(seen)

    def crawlThreadPool(self, startUrl: str, htmlParser: "HtmlParser") -> List[str]:
        seen = set([startUrl])
        lock = Lock()

        def crawl(url):
            html = htmlParser.get_html_content(url)
            links = htmlParser.get_links_on_page(html)
            new_links = []
            with lock:
                for link in links:
                    if link not in seen:
                        seen.add(link)
                        new_links.append(link)
            print(f"{threading.current_thread().name} done")
            return new_links

        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = []
            futures.append(executor.submit(crawl, startUrl))
            for future in as_completed(futures):
                for links in future.result():
                    futures.append(executor.submit(crawl, links))
        return list(seen)


htmlP = HtmlParser(
    [
        "http://news.yahoo.com",
        "http://news.yahoo.com/news",
        "http://news.yahoo.com/news/topics/",
        "http://news.google.com",
        "http://news.yahoo.com/us",
    ],
    [[2, 0], [2, 1], [3, 2], [3, 1], [0, 4]],
)

s = Solution()
# print(s.crawlBFS("http://news.yahoo.com/news/topics/", htmlP))
print(s.crawlConcurrency("http://news.yahoo.com/news/topics/", htmlP))
# print(s.crawlThreadPool("http://news.yahoo.com/news/topics/", htmlP))
