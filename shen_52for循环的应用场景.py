students =[{"name": "张三",
            "age": 18,
            "weight": 50},
           {"name": "李四",
            "age": 24,
            "weight": 60}
]
target = "李四"
for i in students:
    if i["name"] == target:
        print("找到了%s" % target)
        print("%s的年龄是%d，体重是%.2f" % (target, i["age"], i["weight"]))

        break
else:
    print("对不起，没有%s这个人" % target)