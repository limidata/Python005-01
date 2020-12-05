# 自定义异常
class UserInputError(Exception):
    def __init__(self, ErrorInfo):
        super.__init__(self, ErrorInfo)
        self.errorinfo = ErrorInfo

    def __str__(self):
        return self.errorinfo


userinput = 'a'

try:
    if(not userinput.isdigit()):
        # 如果输入的不是数字，抛出异常
        raise UserInputError('用户输入错误')
except UserInputError as ue:
    print(ue)
finally:
    # 删除变量
    del userinput
