class Game:
    top_score = 0
    def __init__(self, player_name):
        self.name = player_name
    @staticmethod
    def show_help():
        print("帮助信息：让僵尸进入大门")
    @classmethod
    def show_top_score(cls):
        print("历史记录是：%d" % cls.top_score)
    def start_game(self):
        print("%s 开始游戏了" % self.name)
game = Game("小明")
Game.show_help()
Game.show_top_score()
game.start_game()