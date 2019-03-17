has_ticket = False
knife_length = 10
if has_ticket:
    print('准备安检')
    if knife_length <20:
        print('请上车')
    else:
        print('刀太长，不宜通过')
else:
    print('请先买票')

