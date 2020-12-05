# 自定义with

class Open:
    # 双下划线函数统称为魔术方法
    def __enter__(self):
        print("__enter__ open")

    def __exit__(self, type, value, trace):
        print("__exit__ close")

    def __call__(self):
        pass


with Open() as f:
    pass

# 上下文协议
