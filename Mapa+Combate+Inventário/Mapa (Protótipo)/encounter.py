from random import randint, choices
from character import Enemy, enemy_list1, enemy_list2, enemy_list3, enemy_list4, enemy_list5


def roll_encounter(stage:int, chance:int) -> 'Enemy':
    if randint(1, 1000) <= chance:
        match stage:
            case 1:
                enemy_list = enemy_list1
            case 2:
                enemy_list = enemy_list2
            case 3:
                enemy_list = enemy_list3
            case 4:
                enemy_list = enemy_list4
            case 5:
                enemy_list = enemy_list5

        enemies, weigths = zip(*enemy_list)
        return choices(enemies, weigths)


if __name__ == '__main__':
    print(roll_encounter(stage=1, chance=20))