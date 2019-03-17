poem = ["静夜思",
        "李白",
        "床前明月光",
        "疑是地上霜",
        "举头望明月",
        "低头思故乡"]
for poem_str in poem:
        # print("|%s|"% poem_str.center(10, "　"))# 居中对齐
        # print("|%s|"% poem_str.rjust(10, "　"))# 向右对齐
        print("|%s|"% poem_str.ljust(10, "　"))# 向左对齐