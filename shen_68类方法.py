class Tool:
    count = 1
    @classmethod
    def tool_count(cls):
        print("工具的数量是 %d" % Tool.count)
    def __init__(self, name):
        self.name = name
        Tool.count += 1
tool1 = Tool("刀")
tool2 = Tool("枪")
tool3 = Tool("棒")
Tool.tool_count()
print(Tool.count)

