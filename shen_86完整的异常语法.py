
try:
    num = int(input("请输入分母："))
    num2 = 10/num
    print("%.2f" % num2)
# except ZeroDivisionError:
#     print("分母不能是0")
except ValueError:
    print("分母不能是空，字母或特殊字符")
except Exception as result:
    print("未知错误：%s" % result)
else:
    print("尝试成功")
finally:
    print("无论是否有异常都会执行的代码")




