import pygame
import sys

blocks = 3
block_size = 110
margin = 10
height = width = block_size
gray = (80, 80, 80)

size = (370, 370)
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption('tic tac toe')


field = [
    [0, 1, 0],
    [0, 2, 0],
    [0, 0, 0]
]

def start():
    global field
    field = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    return


def empty_slot(field):
    empty_slot_count = False
    for row in range (3):
        for slot in range (3):
            if field[row][slot] == 0:
                print(row, slot)
                empty_slot_count = True
    if empty_slot_count == False:
        return stop_game(field)
    return


def game():
    while True:
        #empty_slot(field)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x_mouse, y_mouse = pygame.mouse.get_pos()
                #print(f'x={x_mouse}, y={y_mouse}')
                coloumn = x_mouse //(width + margin)
                row = y_mouse //(height + margin)
        for row in range(3):
            for col in range(3):

                x = col * width + (col + 1) * margin
                y = row * height + (row + 1) * margin
                pygame.draw.rect(screen, gray, (x, y, width, height))
        pygame.display.update()

def check_win(field):
    for row in field:
        if row[0] == row[1] == row[2] != 0:
            return print('win a player with - ' + row[0])
    for coloumn in range (3):
        if field[0, coloumn] == field[1, coloumn] == field[2, coloumn] != 0:
            return print ('win a player with - ' + field[0, coloumn])
    if field[0,0] == field [1,1] == field [2,2] != 0:
        return print('win a player with - ' + field[0,0])
    if field[0,2] == field[1,1] == field[2,0] != 0:
        return print('win a player with - ' + field[0,2])
    return

def stop_game(field):
    resoult = check_win(field)
    if resoult == None:
        return print('drown game')
    return resoult


game ()