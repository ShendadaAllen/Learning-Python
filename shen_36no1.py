name_list = ['zhangsan', 'lisi', 'wangwu']
name_list.append('王五')
print(name_list)
print(name_list[2])
name_list[1] = '张三'
print(name_list)
name_list.remove('zhangsan')
print(name_list)
print(name_list.index('wangwu'))
name_list.pop()
print(name_list)
del name_list[1]
print(name_list)
name_list.extend([1, 7, 3, 8, 5, 6])
print(name_list)
print(name_list.count(1))
name_list.remove('张三')
print(name_list)
name_list.sort(reverse=True)
print(name_list)
name_list.reverse()
print(name_list)
print(len(name_list))

