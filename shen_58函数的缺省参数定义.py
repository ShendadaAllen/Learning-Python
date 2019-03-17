# def print_info(name, gender=True):
#     gender_text = "男生"
#     if not gender:
#         gender_text = "女生"
#     print("%s是%s" % (name, gender_text))
# print_info("小明")
# print_info("小红", False)

def print_info(name, gender="男生"):
    print("%s是%s" % (name, gender))
print_info("小明")
print_info("小红", "女生")
