#!/usr/bin/env python
# 路径处理

import os

path = '/usr/local/a.txt'

# 获取文件名
os.path.basename(path)

# 获取目录名
os.path.dirname(path)

# 是否存在
os.path.exists('/etc/passwd')

# 是否为文件
os.path.isfile('/etc/passwd')

# 是否为目录
os.path.isdir('/etc/passwd')

# 连接路径
os.path.join('a', 'b')
os.path.join('/a', 'b')
