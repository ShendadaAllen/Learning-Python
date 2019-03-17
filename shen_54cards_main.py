import cards_tools

while True:
    cards_tools.memu()
    action_str = input("请选择操作功能：").strip()
    print("你选择的操作功能是【%s】" % action_str)
    if action_str in ["1", "2", "3", "0"]:
        if action_str == "1":
            cards_tools.new_cards()
        elif action_str == "2":
            cards_tools.show_all()
        elif action_str == "3":
            cards_tools.search_cards()
        elif action_str == "0":
            print("退出系统，欢迎下次使用")
            break

    else:
        print("你选择的功能不正确，请重新选择")
