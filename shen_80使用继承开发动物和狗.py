class Animal:
    def __init__(self,name):
        self.name = name
    def eat(self):
        print("吃---")
    def drink(self):
        print("喝---")
    def run(self):
        print("跑---")
    def sleep(self):
        print("睡---")
    def fly(self):
        print("飞la")
class Xtq(Animal):
    def fly(self):
        print("飞")
xiaotq = Xtq("哮天犬")
xiaotq.fly()
