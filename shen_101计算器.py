while True:
    jisuan = input("请输入一个计算公式[Q;q]退出：").strip()
    if jisuan == "q" or jisuan == "Q":
        break
    print(eval(jisuan))
