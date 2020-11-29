#!/usr/bin/env python

from pathlib import Path

# 实例化
p = Path()
p.resolve()

# 传入路径
path = '/usr/local/1.tar.gz'
p = Path(path)
p.absolute

# 获取文件名
p.name

# 获取文件后缀
p.stem
p.suffix

# 获取Linux系统下多重扩展名
p.suffixes


for i in p.parents:
    print(i)


# 取出路径的各个部分
p.parts