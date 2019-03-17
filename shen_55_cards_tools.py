cards_list = []
def memu():
    print("""
********************************************
欢迎使用名片管理系统
1.新增名片
2.显示全部
3.搜索名片
0.退出系统
********************************************""")
def new_cards():
    print("-"*50)
    print("新增名片")
    name = input("请输入姓名：")
    age = input("请输入年龄：")
    qq = input("请输入QQ号码：")
    phone = input("请输入电话：")
    cards_dict = {"name": name,
                  "age": age,
                  "qq": qq,
                  "phone": phone}
    cards_list.append(cards_dict)
    print("名片创建成功")
    print(cards_list)
def show_all():
    print("-" * 50)
    print("显示全部")
    if len(cards_list) == 0:
        print("没有名片，请添加")
        return
    for i in ["姓名", "年龄", "QQ", "电话"]:
        print(i, end="\t\t")
    print("")
    for cards_dict in cards_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (cards_dict["name"],
              cards_dict["age"],
              cards_dict["qq"],
              cards_dict["phone"]))
def search_cards():
    print("-" * 50)
    print("搜索名片")
    find_name = input("请输入搜索的用户：".strip())
    for cards_dict in cards_list:
        if cards_dict["name"] == find_name:
            print("姓名\t\t年龄\t\tQQ\t\t电话")
            print("="*50)
            print("%s\t\t%s\t\t%s\t\t%s" % (cards_dict["name"],
                                            cards_dict["age"],
                                            cards_dict["qq"],
                                            cards_dict["phone"]))
            deal_card(cards_dict)
            break
    else:
        print("抱歉，没有找到%s" % find_name)
def deal_card(find_dict):
    print(find_dict)
    action_str = input("请选择要执行的操作 "
                       "[1] 修改 [2] 删除 [0] 返回上级菜单 ")
    if action_str == "1":
        find_dict["name"] = input_card_info(find_dict["name"],
                                            "姓名(回车不修改)：".strip())
        find_dict["age"] = input_card_info(find_dict["age"],
                                           "年龄(回车不修改)：".strip())
        find_dict["qq"] = input_card_info(find_dict["qq"],
                                          "QQ(回车不修改)：".strip())
        find_dict["phone"] = input_card_info(find_dict["phone"],
                                             "电话(回车不修改)：".strip())
        print("修改名片成功")
    elif action_str == "2":
        cards_list.remove(find_dict)
        print("删除名片成功")
    elif action_str == "0":
        print("返回上级菜单")
    else:
        print("输入不正确，请重新输入")
def input_card_info(dict_value, tip_message):
    # 1.提示用户输入内容
    result_str = input(tip_message)
    if len(result_str) > 0:
        return result_str
    else:
        return dict_value



    # 2.针对用户输入进行判断，如果用户输入内容，直接返回结果

    # 3.如果没有输入内容，返回字典原有内容






