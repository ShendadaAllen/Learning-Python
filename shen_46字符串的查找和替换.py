hello_str = "hello world"
# 1.判断是否以指定字符串开始
print(hello_str.startswith("hello"))
# 2.判断是否以指定字符串结束
print(hello_str.endswith("world"))
# 3.查找指定字符串
print(hello_str.find("wo"))
print(hello_str.find("abc"))#没有则返回-1
# 4.替换字符串
print(hello_str.replace("world", "python"))
# 执行完成返回新的字符串，不会改变原有的字符串



