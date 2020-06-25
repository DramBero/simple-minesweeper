# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 09:48:33 2020

@author: Teodoro_Bagwell
"""

from termcolor import cprint
import random
import re
import time


def create_mine_map(mines, map_size_x, map_size_y):
    map_full = [[0] * map_size_x for i in range(map_size_y)]
    mine_coords = []
    while len(mine_coords) != mines:
        x_axis = random.randint(0, len(map_full[0]) - 1)
        y_axis = random.randint(0, len(map_full) - 1)
        coords = [x_axis, y_axis]
        if coords not in mine_coords:
            mine_coords.append(coords)
    for i in range(len(mine_coords)):
        map_full[mine_coords[i][1]][mine_coords[i][0]] = '*'
    for i in range(len(map_full)):
        for j in range(len(map_full[i])):
            if map_full[i][j] == '*':
                continue
            if j - 1 >= 0:
                if map_full[i][j - 1] == '*':
                    map_full[i][j] = map_full[i][j] + 1
            if j + 1 <= len(map_full[i]) - 1:
                if map_full[i][j + 1] == '*':
                    map_full[i][j] = map_full[i][j] + 1
            if i - 1 >= 0:
                if map_full[i - 1][j] == '*':
                    map_full[i][j] = map_full[i][j] + 1
                if j - 1 >= 0:
                    if map_full[i - 1][j - 1] == '*':
                        map_full[i][j] = map_full[i][j] + 1
                if j + 1 <= len(map_full[i]) - 1:
                    if map_full[i - 1][j + 1] == '*':
                        map_full[i][j] = map_full[i][j] + 1
            if i + 1 <= len(map_full) - 1:
                if map_full[i + 1][j] == '*':
                    map_full[i][j] = map_full[i][j] + 1
                if j - 1 >= 0:
                    if map_full[i + 1][j - 1] == '*':
                        map_full[i][j] = map_full[i][j] + 1
                if j + 1 <= len(map_full[i]) - 1:
                    if map_full[i + 1][j + 1] == '*':
                        map_full[i][j] = map_full[i][j] + 1
    for i in range(len(map_full)):
        for j in range(len(map_full[i])):
            if map_full[i][j] == 0:
                map_full[i][j] = '.'
    return map_full
            

def clear_zero(screen, map_full, com2, com1):
    screen[com2][com1] = map_full[com2][com1]
    if map_full[com2][com1] != '.':
        screen[com2][com1] = map_full[com2][com1]
        return screen
    if com2 - 1 >= 0:
        if screen[com2 - 1][com1] == '~':
            screen = clear_zero(screen, map_full, com2 - 1, com1)
    if com2 + 1 <= len(map_full) - 1:
        if screen[com2 + 1][com1] == '~':
            screen = clear_zero(screen, map_full, com2 + 1, com1)
    if com1 - 1 >= 0:
        if screen[com2][com1 - 1] == '~':
            screen = clear_zero(screen, map_full, com2, com1 - 1)
        if com2 - 1 >= 0:
            if screen[com2 - 1][com1 - 1] == '~':
                screen = clear_zero(screen, map_full, com2 - 1, com1 - 1)
        if com2 + 1 <= len(map_full) - 1:
            if screen[com2 + 1][com1 - 1] == '~':
                screen = clear_zero(screen, map_full, com2 + 1, com1 - 1)
    if com1 + 1 <=len(map_full[0]) - 1:
        if screen[com2][com1 + 1] == '~':
            screen = clear_zero(screen, map_full, com2, com1 + 1)
        if com2 - 1 >= 0:
            if screen[com2 - 1][com1 + 1] == '~':
                screen = clear_zero(screen, map_full, com2 - 1, com1 + 1)
        if com2 + 1 <= len(map_full) - 1:
            if screen[com2 + 1][com1 + 1] == '~':
                screen = clear_zero(screen, map_full, com2 + 1, com1 + 1)
    return screen


def render_screen(screen, map_full, full=False):
    print()
    cprint('  ', 'white', 'on_grey', end='')
    for i in range(len(screen[0])):
        if i > 9:
            break
        cprint(' ', 'white', 'on_grey', end='')
        cprint(i, 'white', 'on_grey', end='')
        cprint(' ', 'white', 'on_grey', end='')
    cprint('\n--', 'yellow', 'on_grey', end='')
    for i in range(len(screen[0])):
        cprint('---', 'yellow', 'on_grey', end='')
    print('')
    if full:
        for i in range(len(screen)):
            for j in range(len(screen[i])):
                if screen[i][j] != 'X':
                    if screen[i][j] == 'F':
                        if map_full[i][j] == '*':
                            screen[i][j] = 'FR'
                        else:
                            screen[i][j] = 'FW'
                    else:
                        screen[i][j] = map_full[i][j]
    for i in range(len(screen)):
        if i < 10:
            cprint(i, 'white', 'on_grey', end='')
            cprint('|', 'yellow', 'on_grey', end='')
        else:
            cprint(' |', 'yellow', 'on_grey', end='')
        for j in screen[i]:
            if j == 1:
                cprint(' ', 'grey', 'on_white',end = '')
                cprint(j, 'blue', 'on_white',end = '')
                cprint(' ', 'grey', 'on_white',end = '')
            elif j == 2:
                cprint(' ', 'grey', 'on_white',end = '')
                cprint(j, 'green', 'on_white',end = '')
                cprint(' ', 'grey', 'on_white',end = '')
            elif j == 3:
                cprint(' ', 'grey', 'on_white',end = '')
                cprint(j, 'red', 'on_white',end = '')
                cprint(' ', 'grey', 'on_white',end = '')
            elif j == 4:
                cprint(' ', 'grey', 'on_white',end = '')
                cprint(j, 'magenta', 'on_white',end = '')
                cprint(' ', 'grey', 'on_white',end = '')
            elif j == 5:
                cprint(' ', 'grey', 'on_white',end = '')
                cprint(j, 'cyan', 'on_white',end = '')
                cprint(' ', 'grey', 'on_white',end = '')
            elif j == 6:
                cprint(' ', 'grey', 'on_white',end = '')
                cprint(j, 'yellow', 'on_white',end = '')
                cprint(' ', 'grey', 'on_white',end = '')
            elif j == 'F':
                cprint(' ', 'grey', 'on_green',end = '')
                cprint('F', 'red', 'on_green',end = '')
                cprint(' ', 'grey', 'on_green',end = '')
            elif j == 'FR':
                cprint(' ', 'grey', 'on_green',end = '')
                cprint('F', 'red', 'on_green',end = '')
                cprint(' ', 'grey', 'on_green',end = '')
            elif j == 'FW':
                cprint(' ', 'grey', 'on_red',end = '')
                cprint('F', 'white', 'on_red',end = '')
                cprint(' ', 'grey', 'on_red',end = '')
            elif j == '~':
                cprint(' ', 'grey', 'on_yellow',end = '')
                cprint(j, 'grey', 'on_yellow', end = '')
                cprint(' ', 'grey', 'on_yellow',end = '')
            elif j == '.':
                cprint(' ', 'grey', 'on_white',end = '')
                cprint('.', 'grey', 'on_white', end = '')
                cprint(' ', 'grey', 'on_white',end = '')
            elif j == '*':
                cprint(' ', 'grey', 'on_blue',end = '')
                cprint('*', 'grey', 'on_blue', end = '')
                cprint(' ', 'grey', 'on_blue',end = '')
            elif j == 'X':
                cprint(' ', 'grey', 'on_red',end = '')
                cprint('X', 'grey', 'on_red', end = '')
                cprint(' ', 'grey', 'on_red',end = '')
            else:
                cprint(' ', 'grey', 'on_white',end = '')
                cprint(j, 'grey', 'on_white',end = '')
                cprint(' ', 'grey', 'on_white',end = '')
        print('')
    print()


def main_game():
    hi_score = 999999999
    while True:
        print('##############################################')
        cprint('    MINESWEEPER', 'red')
        print('    by Teodoro_Bagwell')
        print('##############################################')
        if hi_score != 999999999:
            print('Current Hi-Score is:', hi_score, 'seconds.')
        command = input('Input \'e\' to exit, or \'p\' to play.\n> ')
        if command == 'e' or command == 'E':
            break
        elif command == 'p' or command == 'P':
            map_size_y = 0
            map_size_x = 0
            mines = 0
            while not map_size_y:
                command = input('How many rows do you want on the map?\n> ')
                if command.isdigit():
                    if int(command) > 0:
                        map_size_y = int(command)
                    else:
                        print('Wrong input!')
                else:
                    print('Wrong input!')
            while not map_size_x:
                command = input('How many columns do you want on the map?\n> ')
                if command.isdigit():
                    if int(command) > 0:
                        map_size_x = int(command)
                    else:
                        print('Wrong input!')
                else:
                    print('Wrong input!')
            while not mines:
                command = input('How many mines do you want on the map?\n> ')
                if command.isdigit():
                    if int(command) > 0 and \
                    int(command) < map_size_x * map_size_y:
                        mines = int(command)
                    else:
                        print('Wrong input!')
                else:
                    print('Wrong input!')
            map_full = create_mine_map(mines, map_size_x, map_size_y)
            screen = [['~'] * map_size_x for i in range(map_size_y)]
            start = time.time()
            while True:
                if sum(row.count('~') for row in screen) + \
                sum(row.count('F') for row in screen)<= mines:
                    end = time.time()
                    render_screen(screen, map_full, full=True)
                    print('##############################################')
                    print('  Congratulations! You won!')
                    if end - start < hi_score:
                        hi_score = int(end - start)
                        cprint('  New Hi-Score!', 'green')
                    print('  It took you', hi_score, 'sec to clear the field.')
                    print('##############################################\n')
                    break
                render_screen(screen, map_full, full=False)
                print('Input the x, y coordinates as two numbers')
                print('separated by comma (5,3)')
                print('Add \'f\' before the coordinates to put a flag (f5,3)')
                print('or \'u\' to remove a flag (u5,3).')
                command = input('Input \'e\' to exit to menu.\n > ')
                flag = False
                unflag = False
                if command == 'e' or command == 'E':
                    break
                if command.startswith('f'):
                    command = command[1:]
                    flag = True
                elif command.startswith('u'):
                    command = command[1:]
                    unflag = True
                comobj = re.search(r'(\d+),(\d+)', command, re.M|re.I)
                try:
                    com1 = int(comobj.group(1))
                    com2 = int(comobj.group(2))
                except:
                    print('Wrong input!')
                    continue
                if flag:
                    if screen[com2][com1] == '~':
                        screen[com2][com1] = 'F'
                        continue
                    else:
                        print('You can\'t put a flag here.')
                        continue
                if unflag:
                    if screen[com2][com1] == 'F':
                        screen[com2][com1] = '~'
                        continue
                    else:
                        print('There is no flag here.')
                        continue
                if map_full[com2][com1] == '*':
                    screen[com2][com1] = 'X'
                    render_screen(screen, map_full, full=True)
                    end = time.time()
                    print('##############################################')
                    print('Game over! You stepped on a mine!')
                    print('You played for', int(end - start), 'seconds.')
                    print('##############################################\n')
                    break
                else:
                    clear_zero(screen, map_full, com2, com1)
        else: 
            print('Wrong input!')


main_game()
        
