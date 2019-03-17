while True:
    try:
        num = int(input("请输入分母："))
        num2 = 10/num
        print("%.2f" % num2)
        break
    except ZeroDivisionError:
        print("分母不能是0")
    except ValueError:
        print("分母不能是空，字母或特殊字符")


