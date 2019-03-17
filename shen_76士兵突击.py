class Gun():
    def __init__(self, model):
        self.model = model
        self.bullet_count = 0
    def add_bullet(self, count):
        self.bullet_count += count
    def shoot(self):
        if self.bullet_count <= 0:
            print("没子弹了")
            return
        self.bullet_count -= 1
        print("开火,还剩子弹[%d]" % self.bullet_count)

class Slodier:
    def __init__(self, name):
        self.name = name
        self.gun = None

    def fire(self):
        if self.gun == None:
            print("没枪")
            return
        self.gun.shoot()

ak47 = Gun("ak47")
ak47.add_bullet(10)
xusanduo = Slodier("许三多")
xusanduo.gun =ak47
xusanduo.fire()





