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

polydivisible(input('write a number '))

def some_for_tetst():
    pass

def some_for_test_two():
    pass
#comment