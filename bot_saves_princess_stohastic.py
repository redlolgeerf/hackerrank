# -*- coding: utf-8 -*-
import curses
import time

import bot_saves_princess_3
import generate_field
import locale


def paint_field(field, screen):
    # вывод текста
    for line_number, line in enumerate(field[2:]):
        screen.addstr(line_number + 1, 1, line)

    # обновление экрана
    screen.refresh()
    time.sleep(0.5)

n = 10
m = 5

bot_x, bot_y, targets = generate_field.gen_coordinates(n, m)

field = generate_field.draw_field(n, bot_x, bot_y, targets)
field = field.split('\n')
moves = bot_saves_princess_3.moves(field, 'd')

locale.setlocale(locale.LC_ALL, '')
stdscr = curses.initscr()

paint_field(field, stdscr)

for move in moves:
    if move == 'RIGHT':
        bot_x += 1
    elif move == 'LEFT':
        bot_x -= 1
    elif move == 'DOWN':
        bot_y += 1
    elif move == 'UP':
        bot_y -= 1
    elif move == 'CLEAN':
        targets.remove((bot_x, bot_y))

    field = generate_field.draw_field(n, bot_x, bot_y, targets)
    field = field.split('\n')

    paint_field(field, stdscr)

curses.endwin()
print('Game won!')
