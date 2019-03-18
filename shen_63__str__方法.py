class Cat:
    def __init__(self, name):
        self.name = name
        print("%s 我来了" % self.name)

    def __del__(self):
        print("%s 我去了" % self.name)
    def __str__(self): # 必须返回一个字符串，就是这个类的返回值，不打印内存地址
        return "我是谁"

tom = Cat("Tom")

print(tom)


