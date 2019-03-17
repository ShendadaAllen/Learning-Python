def sum_num(*args):
    sum_n = 0
    for i in args:
        sum_n += i
    return sum_n


print(sum_num(1, 2, 3, 4))
