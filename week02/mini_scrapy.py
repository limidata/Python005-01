# 模拟Scrapy拆分爬虫框架
# conda install lxml
import requests
from lxml import etree
from queue import Queue
import threading
import json


class CrawlThread(threading.Thread):
    def __init__(self, thread_id, queue):
        super().__init__()
        self.thread_id = thread_id
        self.queue = queue
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.52'}

    # 重写run方法
    def run(self):
        print(f"启动线程：{self.thread_id}")
        self.scheduler()
        print(f"结束线程：{self.thread_id}")

    # 模拟任务调度
    def scheduler(self):
        # 队列为空不处理
        while not self.queue.empty():
            page = self.queue.get()
            print(f"下载线程：{self.thread_id}, 下载页面：{page}")
            url = f"https://book.douban.com/top250?start={page*25}"

            # downloader 下载器
            try:
                response = requests.get(url, headers=self.headers)
                dataQueue.put(response.text)
            except Exception as e:
                print("下载出现异常", e)


class ParserThread(threading.Thread):
    def __init__(self, thread_id, queue, file):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.queue = queue
        self.file = file

    def run(self):
        print(f"启动线程：{self.thread_id}")
        while flag:
            try:
                item = self.queue.get(False)  # 参数为False时队列为空，抛出异常
                if not item:
                    continue
                self.parse_data(item)
                self.queue.task_done()  # get后检测是否会阻塞
            except Exception as e:
                pass
        print(f"结束线程：{self.thread_id}")

    # 解析网页内容
    def parse_data(self, item):
        try:
            html = etree.HTML(item)
            books = html.xpath('//div[@class="pl2"]')
            for book in books:
                try:
                    title = book.xpath("./a/text()")
                    link = book.xpath('./a/@href')
                    response = {
                        'title': title,
                        'link': link
                    }
                    # 解析方法和scrapy相同，再构造一个json
                    json.dump(response, fp=self.file, ensure_ascii=False)
                except Exception as e:
                    print("book error", e)
        except Exception as e:
            print("page error", e)


if __name__ == '__main__':

    # 定义存放网页的任务队列
    pageQueue = Queue(20)
    for page in range(0, 11):
        pageQueue.put(page)

    # 定义存放解析数据的任务队列
    dataQueue = Queue()

    # 爬虫程序
    crawl_threads = []
    crawl_name_list = ['crawl_1', 'crawl_2', 'crawl_3']
    for thread_id in crawl_name_list:
        thread = CrawlThread(thread_id, pageQueue)
        thread.start()
        crawl_threads.append(thread)

    # 将结果保存到一个json文件中
    with open('book.json', 'a', encoding='utf-8') as pipeline_f:

        # 解析线程
        parse_thread = []
        parser_name_list = ['parse_1', 'parse_2', 'parse_3']
        flag = True
        for thread_id in parser_name_list:
            thread = ParserThread(thread_id, dataQueue, pipeline_f)
            thread.start()
            parse_thread.append(thread)

        # 结束crawl线程
        for t in crawl_threads:
            t.join()

        # 结束parse线程
        flag = False
        for t in parse_thread:
            t.join()

    print('退出主线程')
