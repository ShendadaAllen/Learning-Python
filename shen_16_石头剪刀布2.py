import random

player = int(input('请输入你要出的拳头/(1)布/(2)石头/(3)剪刀：'))
computer = random.randint(1,3)
if player == computer:
    print('平局')
elif ((computer == 3 and player == 2) or
      (computer == 2 and player == 1)or
      (computer == 1 and player == 3)):
    print('恭喜，你赢了')
else:
    print('你输了')
