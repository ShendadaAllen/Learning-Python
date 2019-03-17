def measure():
    print("测量开始")
    temp = 39
    wetness = 50
    print("测量结束")
    return temp, wetness
g_temp, g_wetness  = measure()
print("温度的结果是%s" % g_temp)
print("湿度的结果是%s" % g_wetness)
