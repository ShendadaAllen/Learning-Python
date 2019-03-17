class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    def __str__(self):
        return "我的名字是%s，体重%.2f公斤" % (self.name, self.weight)
    def run(self):
        print("%s爱跑步，跑步锻炼身体" % self.name)
        self.weight += 0.5
    def eat(self):
        print("%s爱吃鸡屁股，吃了长身体" % self.name)
        self.weight -= 1


xm = Person("小明", 75)
xm.run()
xm.eat()
print(xm)

