class Test:
    def __new__(cls, *args, **kwargs):
        print("重写了new方法")
        return super().__new__(cls)
    def __init__(self):
        print("结束")


print(Test())