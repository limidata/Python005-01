# 写一个socket客户端
# 安装：pip3 install requests
import requests

r = requests.get("http://www.httpbin.org")
print(r.status_code)
print(r.headers)
# print(r.text)

