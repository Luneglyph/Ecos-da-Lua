from character import *
from weapon import *
from combat import *
import os


player = Player (name="Dargia", hp=100, atk=10)
enemy = Enemy (name="Goblin", hp=100, atk=5)

combat_encounter(player,enemy)

#To do list:
#Transformar o combate em batalha por turnos
#Implementar defesa como atributo
#Elaborar a formula de defesa
#Implementar combate na exploração do mapa
#Implementar encontros de combate aleatórios ao explorar o mapa
#Preencher lista de inimigos
#Implementar método para escolher um inimigo aleatorio da lista de inimigos ao iniciar combate baseado no terreno.
#Elaborar interface de exploração de mapa
#Elaborar interface de combate e/ou vincula-la na interface de exploração de mapa.