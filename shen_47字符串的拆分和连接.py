poem_str = "静夜思\t李白\t床前明月光\t\t疑是地上霜\t\n举头望明月\t低头思故乡"
# print(poem_str)
# 1.拆分字符串
poem_list = poem_str.split()  # 拆分成一个列表
print(poem_list)
# 2.合并字符串
result = " ".join(poem_list)  # 合并成一个字符串
print(result)