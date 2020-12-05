# 使用request库爬取豆瓣影评
import requests
from pathlib import *
import sys

from requests.api import head

ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.52'
header = {'user-agent': ua}

url = 'https://movie.douban.com/top250'

try:
    response = requests.get(url, headers=header)
except requests.exceptions.ConnectTimeout as e:
    print(f"requests库超时 {e}")
    sys.exit(1)

# 将网页内容改为存入文件
print(response.text)

# 获得python脚本的绝对路径
# __file__ 表示当前脚本文件
p = Path(__file__)
pyfile_path = p.resolve().parent
print(f'pyfile_path = {pyfile_path}')

# 建立新的目录
html_path = pyfile_path.joinpath('html')
print(f'html_path = {html_path}')

if not html_path.is_dir():
    Path.mkdir(html_path)
page = html_path.joinpath('douban.html')

# 上下文管理器
try:
    with open(page, 'w', encoding='utf-8') as f:
        f.write(response.text)
except FileNotFoundError as e:
    print(f'文件无法打开, {e}')
except IOError as e:
    print(f'读写文件出错, {e}')
except Exception as e:
    print(e)
