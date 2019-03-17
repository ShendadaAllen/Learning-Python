player = input('请输入你要出的拳： ')
computer = '石头'
if player == '石头':
    print('电脑出的拳是：%s。玩家出的拳是：%s'%(computer,player))
    print('平局')
elif player == '剪刀':
    print('电脑出的拳是：%s。玩家出的拳是：%s' % (computer, player))
    print('电脑赢了')
else:
    print('电脑出的拳是：%s。玩家出的拳是：%s' % (computer, player))
    print('你赢了')
