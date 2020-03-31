import pygame
import sys

blocks = 3
block_size = 110
margin = 10
height = width = block_size
gray = (80, 80, 80)
blue = (0, 0, 255)
red = (255, 0, 0)
purple = (145, 119, 163)
black = (255, 255, 255)

size = (370, 470)
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption('tic tac toe')


field = [
    [0, 1, 0],
    [0, 2, 0],
    [0, 0, 0]
]


def start():
    global player
    player = True
    global field
    field = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    return


def py_screen(color, x, y, width, height, geometry):
    pygame.draw.rect(screen, color, (x, y, width, height))


def game():
    while True:
        for row in range(3):   # drawing
            for col in range(3):
                x = col * width + (col + 1) * margin
                y = row * height + (row + 1) * margin  # 100 for button "start again"
                if field[row][col] == 0:
                    color = gray
                elif field[row][col] == 1:
                    color = red
                    pygame.draw.aaline(screen, black, (x + 10, y + 10), (x + 90, y + 90))
                else:
                    color = blue
                pygame.draw.rect(screen, color, (x, y, width, height))
        pygame.draw.rect(screen, purple, (10, 370, 350, 90))  # button "start again"
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # exit
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.MOUSEBUTTONDOWN:  # button click
                global player
                x_mouse, y_mouse = pygame.mouse.get_pos()
                column = int(x_mouse //(width + margin))
                row = int(y_mouse //(height + margin))
                # print(f'x={x_mouse}, y={y_mouse}')
                # print(row, column, 'field is', field[row][column], 'player is', player)
                if field[row][column] == 0 and player == True:
                    player = False
                    field[row][column] = 1
                elif field[row][column] == 0 and player == False:
                    player = True
                    field[row][column] = 2
        if (check_win(field)) == True:
            break


def check_win(field):
    for row in field:
        if row[0] == row[1] == row[2] != 0:
            print('win a player with - ' + str(row[0]))
            return True
    for column in range(3):
        if field[0][column] == field[1][column] == field[2][column] != 0:
            print('win a player with - ' + str(field[0][column]))
            return True
    if field[0][0] == field[1][1] == field [2][2] != 0:
        print('win a player with - ' + str(field[0][0]))
        return True
    if field[0][2] == field[1][1] == field[2][0] != 0:
        print('win a player with - ' + str(field[0][2]))
        return True
    drown = 0
    for row in range(3):
        for column in range(3):
            if field[row][column] == 0:
                break
            else:
                drown += 1
    if drown == len(field)*3:
        print('drown game')
        return True

    return


start()
game()