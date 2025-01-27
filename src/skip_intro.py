from Entity.player import Player
from Item.item_list import potion1
from Interface.main import start_interface
from curses import wrapper


player = Player(name="Dargia",hp=100, atk_value=10, crit_chance=0.1, crit_damage=2.0)


player.inventory.add_item(potion1)


wrapper(start_interface, player)

'''Bugs encontrados:
->Chegar no LVL 10 e ganhar XP enquanto LVL 10 causa o seguinte erro: 
Traceback (most recent call last):
  File "c:\Users\Alunos\Downloads\Ecos da Lua\jogo-python\src\skip_intro.py", line 13, in <module>
    wrapper(start_interface, player)
    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Alunos\AppData\Local\Programs\Python\Python313\Lib\curses\__init__.py", line 94, in wrapper
    return func(stdscr, *args, **kwds)
  File "c:\Users\Alunos\Downloads\Ecos da Lua\jogo-python\src\Interface\main.py", line 303, in start_interface
    if not combat_system.start_combat(player, enemy):
           ~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^
  File "c:\Users\Alunos\Downloads\Ecos da Lua\jogo-python\src\Combat\combat.py", line 44, in start_combat
    return self.stop_combat(player, enemy, victory=True)
           ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "c:\Users\Alunos\Downloads\Ecos da Lua\jogo-python\src\Combat\combat.py", line 117, in stop_combat
    lvl_up, exp_ganho = player.gain_exp(enemy.exp_range)
    ^^^^^^^^^^^^^^^^^
TypeError: cannot unpack non-iterable NoneType object
PS C:\Users\Alunos\Downloads\Ecos da Lua\jogo-python>

-> Usar uma poção ao ter mais de 10 items no inventário crasha o jogo.
-> Funcionalidade de mostrar inventário na vila para de funcionar aleatoriamente.
'''