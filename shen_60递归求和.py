
def sum_num(num):
    if num == 1:
        return num
    else:
        return num + sum_num(num - 1)


result = sum_num(100)
print(result)
