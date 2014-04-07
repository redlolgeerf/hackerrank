# coding: utf-8

import time
import curses
import locale
import sys
import generate_field

locale.setlocale(locale.LC_ALL, '')
stdscr = curses.initscr()
# вывод текста
for x in range(2):
    field = generate_field.make_field()
    for line_number, line in enumerate(field):
        stdscr.addstr(line_number + 1, 1, line)

    # обновление экрана
    stdscr.refresh()
    time.sleep(1)
curses.endwin()
#for x in range(10):
#    # sys.stdout.write('Final count down %d' % x)
#    sys.stdout.write("%s%%   \r" % (field[:5]))
#    #sys.stdout.write("Download progress: %d%%   \r" % (x))
#    sys.stdout.flush()
#    time.sleep(2)
