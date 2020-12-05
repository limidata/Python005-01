#!usr/bin/env python

import requests
from time import sleep
from lxml import etree


def get_neweekly(url):
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.52'
    header = {'user-agent': ua}

    response = requests.get(url, headers=header)

    selector = etree.HTML(response.text)
    book_name = selector.xpath('//a[@class="u-book-name"]/text()')
    book_image = selector.xpath('//img[@class="u-book-cover"]/@src')

    print(f"name = {book_name}, image = {book_image}")

    books = dict(zip(book_name, book_image))
    for i in books:
        text = f'名称： {i}\r\n图片：{books[i].strip()}\r\n'
        with open('book.txt', 'a+') as f:
            f.write(text)


if __name__ == '__main__':
    urls = tuple(
        f'http://www.neweekly.com.cn/book?currentPage={i+1}'for i in range(2))
    for page in urls:
        get_neweekly(page)
        sleep(1)
