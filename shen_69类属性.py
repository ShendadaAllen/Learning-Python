class Tool:
    count = 0
    def __init__(self, name):
        self.name = name
        Tool.count += 1
tool1 = Tool("刀")
tool1 = Tool("枪")
tool1 = Tool("棍")
print(Tool.count)
