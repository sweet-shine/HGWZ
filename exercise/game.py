
class Game:

    def __init__(self, hp, power):
        self.hp = hp
        self.power = power

    def fight(self, enemy_hp, enemy_power):

        final_hp = self.hp - enemy_power
        enemy_final_hp = enemy_hp - self.power

        if final_hp > enemy_final_hp:
            print("我赢了")
        elif final_hp < enemy_final_hp:
            print("敌人赢了")
        else:
            print("平局")

class HouYi(Game):

    def __init__(self):
        super().__init__(1000, 200)
        self.defence = 100

    def houyi_fight(self, enemy_hp, enemy_power):
        final_hp = self.hp + self.defence - enemy_power
        enemy_final_hp = enemy_hp - self.power

        if final_hp > enemy_final_hp:
            print("我赢了")
        elif final_hp < enemy_final_hp:
            print("敌人赢了")
        else:
            print("平局")

hp = 1000
power = 200
# game = Game(hp, power)
#
# game.fight(1000, 300)
houyi = HouYi()
houyi.houyi_fight(1000, 200)