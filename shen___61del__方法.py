class Cat:
    def __init__(self, name):
        self.name = name
        print("%s 我来了" % self.name)

    def __del__(self):
        print("%s 我去了" % self.name)

tom = Cat("Tom")

del tom # del执行优先于__del__,所以会紧跟着执行__del__方法
print("-"*50)
