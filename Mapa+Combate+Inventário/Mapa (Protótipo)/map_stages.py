#map_stages.py (Modularização de fases diferentes)

from map import Map
from tile import *

class ForestMap(Map):
    def __init__(self, largura, altura):
        super().__init__(largura, altura)
    
    def create_map(self):
        self.init_map_info = [[Tile("_", ANSI_GREEN) for _ in range(self.largura)] for _ in range(self.altura)]
        self.copy_map()
        self.explore_process = [[0 for _ in range(self.largura)] for _ in range(self.altura)]

    def setup_terreno(self):
        self.gerar_terreno(montanha, 3, 3, 6)
        self.gerar_terreno(floresta, 4, 5, 12)
        self.gerar_terreno(areia, 3, 2, 5)
        self.gerar_terreno(tronco, 6, 1, 1)
        self.gerar_terreno(flores, 4, 3, 6)
        self.gerar_terreno(arbusto, 6, 1, 5)
        self.gerar_terreno(agua, 4, 5, 8)

class DesertMap(Map):
    def __init__(self, largura, altura):
        super().__init__(largura, altura)
    
    def create_map(self):
        self.init_map_info = [[Tile("_", ANSI_YELLOW) for _ in range(self.largura)] for _ in range(self.altura)]
        self.copy_map()
        self.explore_process = [[0 for _ in range(self.largura)] for _ in range(self.altura)]

    def setup_terreno(self):
        self.gerar_terreno(montanha, 2, 3, 6)
        self.gerar_terreno(areia, 6, 5, 10)
        self.gerar_terreno(arbusto, 4, 2 ,5)
        self.gerar_terreno(floresta, 3, 3, 5)
        self.gerar_terreno(duna, 6, 5, 10)
        self.gerar_terreno(tronco, 6, 1, 2)
        self.gerar_terreno(agua, 2, 2, 5) 

class SnowMap(Map):
    def __init__(self, largura, altura):
        super().__init__(largura, altura)
    
    def create_map(self):
        self.init_map_info = [[Tile("_", ANSI_WHITE) for _ in range(self.largura)] for _ in range(self.altura)]
        self.copy_map()
        self.explore_process = [[0 for _ in range(self.largura)] for _ in range(self.altura)]

    def setup_terreno(self):
        self.gerar_terreno(montanha_gelo, 4, 3, 7)
        self.gerar_terreno(tundra, 5, 5, 12)
        self.gerar_terreno(agua, 3, 4, 6)
        self.gerar_terreno(floresta, 2, 3, 5)

class SwampMap(Map):
    def __init__(self, largura, altura):
        super().__init__(largura, altura)
    
    def create_map(self):
        self.init_map_info = [[Tile("_", ANSI_GREEN) for _ in range(self.largura)] for _ in range(self.altura)]
        self.copy_map()
        self.explore_process = [[0 for _ in range(self.largura)] for _ in range(self.altura)]

    def setup_terreno(self):
        self.gerar_terreno(pantano, 5, 4, 8)
        self.gerar_terreno(agua, 5, 3, 7)
        self.gerar_terreno(floresta, 3, 3, 5)

class FireMap(Map):
    def __init__(self, largura, altura):
        super().__init__(largura, altura)
    
    def create_map(self):
        self.init_map_info = [[Tile("_", ANSI_DARK_GRAY) for _ in range(self.largura)] for _ in range(self.altura)]
        self.copy_map()
        self.explore_process = [[0 for _ in range(self.largura)] for _ in range(self.altura)]

    def setup_terreno(self):
        self.gerar_terreno(magma, 6, 4, 10)
        self.gerar_terreno(pedra_vulc, 5, 3, 8)
