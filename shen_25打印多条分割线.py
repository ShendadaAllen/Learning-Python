# import shen_打印分割线
#
# i = 1
# while i <= 5:
#     shen_打印分割线.print_line('*', 50)
#     i += 1


def print_lines(char, times):
    """打印多条分割线
    :param char: 分割字符
    :param times: 多少次
    """
    i = 1
    while i <= 5:
        print(char*times)
        i += 1


print_lines('*', 50)


