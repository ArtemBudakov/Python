##second degree of every figure from number
def square_digits(num):
    tmp = ([int(x) * int(x) for x in str(num)])
    result = ''.join(str(x) for x in tmp)
    print(result)
    return int(result)

##day and numbers
def am_I_afraid1(day, num):
    if day == 'Monday' and num == 12:
        return True
    if day == 'Tuesday' and num > 95:
        return True
    if day == 'Wednesday' and num == 34:
        return True
    if day == 'Thursday' and num == 0:
        return True
    if day == 'Friday' and num % 2 == 0:
        return True
    if day == 'Saturday' and num == 56:
        return True
    if day == 'Sunday' and num == 666 or num == -666:
        return True
    return False

##other solution
def am_I_afraid(day,num):
    return {
        'Monday':  num == 12,
        'Tuesday': num > 95,
        'Wednesday': num == 34,
        'Thursday': num == 0,
        'Friday': num % 2 == 0,
        'Saturday': num == 56,
        'Sunday': num == 666 or num == -666
    } [day] ## 'day' - is a key for value that we need

##The two oldest ages function/method needs to be completed.
# It should take an array of numbers as its argument and
# return the two highest numbers within the array.
# The returned value should be an array in the format [second oldest age, oldest age].
def two_oldest_ages1(ages):
    result = [0, 0]
    for value in ages:
        if value > result[0] and value <= result[1]:
            result[0] = value
        if value > result[0] and value > result[1]:
            result[0] = result[1]
            result[1] = value
    return result

def two_oldest_ages(ages):
    return sorted(ages)[-2:]

##print (am_I_afraid(day = input('write day\n'), num = int(input('write num\n'))))


def Eratosfen (N:int):
    """documentation"""
    List = [True] * N
    List[0] = List[1] = False
    for element_count in range (2, N):
        if List[element_count]:
            for next_elements in range (2 * element_count, N, element_count):
                List[next_elements] = False
    for element_count in range (N):
        if List[element_count]:
            print(element_count, '-', 'simple' )

##Eratosfen(int(input('write length N ')))


def polydivisible(number):
    """Polydivisible Numbers
    A polydivisible number is divisible in an unusual way.
    The first digit is cleanly divisible by 1, the first two digits are cleanly divisible by 2,
    the first three by 3, and so on.

    Example:
        1      /1 = 1    // Works
        12     /2 = 6    // Works
        123    /3 = 41   // Works
        1232   /4 = 308  // Works
        12322  /5 = 2464.4         // Doesn't work
        123220 /6 = 220536.333...  // Doesn't work
    """
    try:
        int(number)
    except:
        print ('x is incorrect number')
        return False

    for x in range(1, len(number) + 1):
        print ('number for test = ', number[:int(x)])
        print ('x = ', x)
        print ((int(number[:x]) % x))

        if (int(number[:x]) % x):
            print ('what')
            return False
        else:
            print ("work")
    return True
        ##print ("doesn't work" if (int(number[:x]) % x) else 'work')

##polydivisible(input('write a number '))


def calculate_damage(your_type, opponent_type, attack, defense):
    """  Your task is to calculate the damage
    that a particular move would do using the following formula:
    Super effective: 2x damage
    Neutral: 1x damage
    Not very effective: 0.5x damage
    damage = 50 * (attack / defense) * effectiveness
    fire > grass
    fire < water
    fire = electric
    water < grass
    water < electric
    grass = electric
    """
    dmg = 50 * (attack / defense) * effictiveness(your_type, opponent_type)
    return dmg

def effictiveness (your_type, opponent_type):
    coefficient={
        'fire': 1,
        'water': 2,
        'grass': 3,
        'electric': 4
    }
    power_fire={
        'fire': 0.5,
        'water': 0.5,
        'grass': 2,
        'electric': 1
    }
    power_water={
        'fire': 2,
        'water': 0.5,
        'grass': 0.5,
        'electric': 0.5
    }
    power_grass={
        'fire': 0.5,
        'water': 2,
        'grass': 0.5,
        'electric': 1
    }
    power_electric={
        'fire': 1,
        'water': 2,
        'grass': 1,
        'electric': 0.5
    }

    if (coefficient.get(your_type)) == 1:
        return power_fire.get(opponent_type)
    elif (coefficient.get(your_type)) == 2:
        return power_water.get(opponent_type)
    elif (coefficient.get(your_type)) == 3:
        return power_grass.get(opponent_type)
    elif (coefficient.get(your_type)) == 4:
        return power_electric.get(opponent_type)

##print (calculate_damage(your_type=input('your type is '), opponent_type=input('opponent type is '),
##                        attack=int(input('attack = ')), defense=int(input('defence = '))))

""" very clever solution below

from math import ceil
D = {"fire": "grass", "water": "fire", "grass": "water", "electric": "water"}
def calculate_damage(a, b, n, m):
    return ceil(50 * (n / m) * (2 if D[a] == b else 0.5 if D[b] == a or a == b else 1))

also can be simple dictionary if did like below
effectiveness = {
    "electric":{
      "electric": 0.5,
      "fire": 1,
      "grass": 1,
      "water": 2
    },
    "fire":{
      "electric": 1,
      "fire": 0.5,
      "grass": 2,
      "water": 0.5
    }
"""

def next_num(number):
    """Given a non-negative number, return the next bigger polydivisible number,
     or an empty value like null or Nothing.
    """
    for x in range(1, len(number) + 1):

        if (int(number[:x]) % x):
            print ('not divisible')
            print('remains=', (int(number[:x]) % x), 'X=', x, 'number=', number[:x])
            return next_polydivisible(number)
        ##else:
            ##print("work\n")
    return print(number, ' is polydivisible number and divider is ', x)

def next_polydivisible (number):
    while int(number) <= 3608528850368400786036725:
        number = str(number)
        for x in range(1, len(str(number)) + 1):
            ##print('number for test = ', number[:int(x)])
            ##print('x = ', x)

            if (int(number[:x]) % x):
                number = int(number) + 1
                ##print('number is ', number, ' and type is ', type(number), ' type X is ', type (x))
                break

            elif (int(number) % len(str(number))) == 0 and x == len(str(number)):
                print ('what is it = ', (int(number) % x), ' number = ', number, ' x = ', x)
                return print('next polydivisible number is ', number, 'divider is ', x)


    return print ('not enough polydivisible numbers')

for i in range (0, 1, 3608528850368400786036726):
    next_num(str(i))


##next_num(input('write a number '))