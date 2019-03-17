def demo(num_list):
    print("函数开始")
    num_list += num_list  #本质上是调用extend方法
    # 其中num_list += num_list不等于num_list= num_list+num_list
    print(num_list)
    print("函数完成")
gl_list = [1, 2, 3, 4]
demo(gl_list)
print(gl_list)


