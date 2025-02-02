import curses

def show_map(window, previous_view=None):
    # Configuração de cores
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(6, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(7, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(8, curses.COLOR_MAGENTA, curses.COLOR_BLACK)

    TERRAIN_COLORS = {
        '≈' : curses.color_pair(1), # lago/rio
        '♣' : curses.color_pair(2), # floresta
        '_' : curses.color_pair(3), # planicie
        '≋' : curses.color_pair(4), # magma
        '▲' : curses.color_pair(5), # montanha
        '∼' : curses.color_pair(6), # deserto
        '⌂' : curses.color_pair(7), #vila
        '|' : curses.color_pair(8), # boss
        '-' : curses.color_pair(8),
        '[' : curses.color_pair(8),
        ']' : curses.color_pair(8),
        '∖' : curses.color_pair(8),
        "⁄" : curses.color_pair(8),
        '`' : curses.color_pair(8),
        '´' : curses.color_pair(8),
        '▶' : curses.color_pair(8),
        '⁂' : curses.color_pair(8)
    }

    ascii_map = [
        "_____________________________________________________________________________________≈≈≈≈≈________⌂___⌂______",
        "_____________________________________________________________________≈≈≈_____≈≈≈≈≈≈≈≈≈≈≈__⌂⌂⌂____⌂___⌂⌂⌂___⌂_",
        "_________________________________________________________________≈≈≈______≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈______⌂⌂⌂⌂__⌂⌂_⌂⌂___",
        "__________________________________________________________________≈≈≈__≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈___⌂⌂_____⌂⌂_⌂⌂⌂_⌂_",
        "________________________________________________________≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈___________⌂⌂___⌂⌂___",
        "___________________∼∼______∼∼∼∼∼∼∼____∼∼∼___________≈≈≈≈______≈≈≈≈≈_____≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈__♣_⌂⌂___⌂__⌂⌂⌂___",
        "________________________∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼______∼∼∼____≈≈≈≈__♣♣♣♣♣♣____________≈≈≈≈≈≈≈≈≈≈____♣♣♣___⌂⌂_⌂⌂⌂⌂_⌂⌂⌂__",
        "______________________∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼___≈≈≈≈______________♣♣♣♣♣♣________♣♣____♣♣♣♣_⌂⌂_⌂_____⌂⌂⌂__⌂__",
        "__________________________∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼___≈≈≈≈_______♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣_____♣♣♣♣_____⌂__⌂⌂⌂____⌂_____",
        "______________________________∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼∼______≈≈≈≈___♣♣_________♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣_______⌂⌂⌂_____⌂______",
        "_____________________∼∼∼∼________∼∼_____∼∼∼∼∼∼∼_____≈≈≈____________♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣_⌂⌂__⌂__⌂⌂________",
        "_____________________________________________________≈≈≈≈____♣♣______♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣______⌂__⌂________",
        "________________________▲____________≈≈≈≈__________≈≈≈≈____________♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣___⌂___________⌂____",
        "_______________________▲▲▲__▲______≈≈≈≈≈≈≈≈___≈≈≈≈≈≈≈≈_______________♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣___________________",
        "__________________▲__▲▲▲▲▲▲▲▲▲______≈≈≈___≈≈≈≈≈≈____≈≈≈________________♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣______________________",
        "_________________▲▲▲▲▲▲▲▲▲__▲▲▲▲____________________≈≈≈≈≈_______♣♣♣♣♣♣♣_______♣♣♣♣♣♣♣♣♣♣♣____________________",
        "____________________▲▲▲▲____▲▲_________________________≈≈≈≈_______________♣♣♣________________________________",
        "_______________________________________________≋≋≋______≈≈≈≈______________________▲_________▲________________",
        "______________________________≋≋≋≋____≋≋≋≋≋≋≋____________≈≈≈≈≈≈_________▲________▲▲▲___▲_____________________",
        "______________________________≋≋≋≋≋≋≋≋≋≋≋___≋≋≋__________≈≈≈≈______________▲____▲▲▲▲▲_▲▲▲____________________",
        "___________|▶________≋≋≋_____≋≋≋≋≋≋≋≋≋≋≋______≋≋________≈≈≈≈_______▲____▲▲▲__▲▲▲▲▲▲▲▲▲▲▲__▲__________________",
        "_____[-]---|---[-]__________≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋≋____________≈≈≈≈≈________▲_▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲▲________________",
        "_____| |´´⁄ ∖``| |_____≋≋≋__≋≋≋≋≋≋≋≋______≋≋≋≋___________≈≈≈≈≈≈≈_______▲▲▲_________▲▲▲▲▲▲____________________",
        "_____| | ⁄ ⁂ ∖ | |________________________________________≈≈≈≈≈≈≈≈≈≈≈≈______▲▲▲__________▲▲__________________",
        "_____|_|_|___|_|_|_____________________________________≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈_______________________________________",
        "___________________________________________________________≈≈≈≈≈≈≈≈≈≈≈≈≈≈____________________________________",
        "_________________________________________________________________≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈≈___________________________"
    ]
    # legenda
    captions = [
        ("1. ⌂ - Vila do Alvorecer", curses.color_pair(7)),
        ("2. ♣ - Floresta dos Ecos", curses.color_pair(2)),
        ("3. ∼ - Dunas do Desolado", curses.color_pair(6)),
        ("4. ▲ - Terra Congelada", curses.color_pair(5)),
        ("5. ≈ - Pântano das Águas Místicas", curses.color_pair(1)),
        ("6. ≋ - Fornalha do Apocalipse", curses.color_pair(4)),
        ("7. ⁂ - Fortaleza de...", curses.color_pair(8))
    ]

    # Obter dimensões da tela
    max_y, max_x = window.getmaxyx()

    # limpar janela
    window.clear()
    window.box()    

    # posição do mapa
    start_y = 1
    start_x = (max_x - len(ascii_map[0])) // 2

    # Desenhar o mapa
    for y, line in enumerate(ascii_map):
        for x, char in enumerate(line):
            try:
                window.addch(y + start_y, x + start_x, char, TERRAIN_COLORS.get(char, curses.color_pair(6)))
            except curses.error:
                pass

    # posição da legenda
    caption_y = start_y + len(ascii_map) + 1
    caption_x = start_x

    for i, (text, color) in enumerate(captions):
        row = i // 3
        col = i % 3

        try:
            window.addstr(caption_y + row,
                          caption_x + (col * (max_x // 3)) + (col * 1),
                          text, color)
        except curses.error:
            break

    # Atualizar a janela
    window.refresh()

    # Aguardar input do usuário
    while True:
        key = window.getch()
        if key in [ord('1'), ord('2'), ord('3'), ord('4'), ord('5'), ord('6'), ord('7')]:
            return int(chr(key))
        elif key in [27, ord('q'), ord('Q')]:  # ESC ou Q para sair
            return previous_view if previous_view else 'village'
    
    return 0
