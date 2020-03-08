
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
                print (row, slot)
                empty_slot_count = True
    if empty_slot_count == False:
        return stop_game(field)
    return


def game():
    while True:
        empty_slot(field)


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
