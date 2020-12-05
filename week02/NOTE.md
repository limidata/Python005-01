# 学习笔记



## 异常信息与异常捕获

- 异常信息在 Traceback 信息的最后一行，有不同的类型
- 捕获异常可以使用 try ... except 语法
- try ... except 支持多重异常处理



### 常见的异常类型

1. LookupError 下的 IndexError 和 KeyError
2. IOError
3. NameError
4. TypeError
5. AttributeError
6. ZeroDivisionError



### 代码演示

- 不处理异常，发生异常时，后续程序不在执行。

```python
1/0
# 发生异常，后续的程序不再执行
print('never see me')
```

- 处理异常

```python
try:
    1/0
except Exception as e:
    print(e)
```

- 捕获异常时再次异常处理

```python
try:
    1/0
except Exception as e:
    try:
        1/0
    except Exception as ex:
        pass # 不做处理
    print(e)
```

- 捕获多异常

```python
try:
    # your code
except (ZeroDivisionError, Exception) as e:
    print(e)
```

- 使用raise关键字抛出自定义异常

参考 `p4_inputerror.py`

美化异常输出，先安装 pip install pretty_errors

```python
import pretty_errors

def foo():
    1/0

foo()
```

- 文件IO异常
```python
with open('a.txt', encoding='utf8') as file2:
    data = file2.read()
```

- 自定义with
参考 `p7_custom_with.py`


## 重构：增加程序的健壮性

参考 `requests_v2.py`

## 使用自顶向下的设计思维拆分项目代码

什么是自顶向下设计？

- 从`整体分析`一个比较`复杂`的大问题
- 分析方法可以重用
- 拆分到你能解决的范畴

## 模拟Scrapy拆分爬虫框架

参考 `mini_scrapy.py`