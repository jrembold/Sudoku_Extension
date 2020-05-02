### Generating the solution board ###

import random

# set numbers to letter in a dictionary so that we can shift the key 
abc = {'a': 1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6}


def Shift_dictionary( ):
    '''
    This function shifts the abc dictionary by a random number.

    input:
        none
    output:
        abc (dict): shifted num dictionary
    '''
    shift = random.randint(1,6)
    for key in abc:
        abc[key] += shift
        if abc[key] > 6:
            abc[key] -= 6
    return abc


def Apply_shift(abcnew):
    '''
    Applies shift to the known sudoku solution.

    input:
        abcnew (dict): shifted dictionary
    output:
        rows (tuple): tuple of lists with shifted row elements
    '''
    r1 = [abcnew['d'], abcnew['e'], abcnew['f'], abcnew['b'], abcnew['a'], abcnew['c']]
    r2 = [abcnew['c'], abcnew['a'], abcnew['b'], abcnew['e'], abcnew['d'], abcnew['f']]
    r3 = [abcnew['e'], abcnew['d'], abcnew['c'], abcnew['a'], abcnew['f'], abcnew['b']]
    r4 = [abcnew['f'], abcnew['b'], abcnew['a'], abcnew['c'], abcnew['e'], abcnew['d']]
    r5 = [abcnew['b'], abcnew['f'], abcnew['e'], abcnew['d'], abcnew['c'], abcnew['a']]
    r6 = [abcnew['a'], abcnew['c'], abcnew['d'], abcnew['f'], abcnew['b'], abcnew['e']]
    rows = [r1, r2, r3, r4, r5, r6]
    return rows


def Mix_rows(rowsnew):
#     '''
#     Mixes the rows. 

#     input:
#         rowsnew (tuple): tuple of rows with shifted values
#     output:
#         rowsmixed (tuple): the same rows but in a different order

#     '''
#     rowsmixed = ( )
#     mix = random.randint(0,6)
#     for i in range(0,6):
#         row = i + 1
#         if (mix + row) >= 6:
#             newmix = mix - 6
#             rowsmixed += (rowsnew[i+ newmix], )
#         else:
#             rowsmixed += (rowsnew[i+ mix], )

#     return rowsmixed
    return rowsnew


def Generate_unique_board( ):
    ''' 
    runs the above functions

    input:
        none
    output:
        UniqueBoard (tuple): tuple of rows
    '''
    newdict = Shift_dictionary( )
    shiftedabc = Apply_shift(newdict)
    UniqueBoard = Mix_rows(shiftedabc)
    f = open('answertext2.txt', 'w')
    f.write(str(UniqueBoard))
    f.close()
    return UniqueBoard

def read_text(textfile):
    o = open(textfile, 'r')
    for line in o:
        fixed_answer = line

    s = fixed_answer.split(',')
    l1 = []
    for i in s:
        l1.append(i.strip(']'))
    l2 = []
    for q in l1:
        l2.append(q.strip(' ['))
    nums = []
    for l in l2:
        nums.append(int(l))

    r1 = nums[:6]
    r2 = nums[6:12]
    r3 = nums[12:18]
    r4 = nums[18:24]
    r5 = nums[24:30]
    r6 = nums[30:36]
    all = [r1, r2, r3, r4, r5, r6]
    return all




###  Remove random numbers from solution to show the board  ###
#sol = Generate_unique_board()
def Partial_solution(solution, difficulty):
    '''
    Revomves 

    '''
    #difficulty = input("Input easy, medium or hard: ")
    if difficulty == "easy":
        amount_to_be_removed = 36 - random.randint(17,20)
    elif difficulty == 'medium':
        amount_to_be_removed = 36 - random.randint(13,17)
    elif difficulty == 'hard':
        amount_to_be_removed = 36 - random.randint(10,13)
    partial = solution.copy()
    for i in range(0, amount_to_be_removed):
        randomi = random.randint(0,5)
        randomj = random.randint(0,5)
        partial[randomi][randomj] = 0
    return partial


#Generate_unique_board()
#full = read_text('answertext2.txt')
#part = Partial_solution(read_text('answertext2.txt'),'hard')
#print(part)

def Hint_Generator(partial,full):
    blanks = ()
    for i in range(0,6):
        for j in range(0,6):
            if partial[i][j] == 0:
                blanks += ((i,j),)
    coords = random.choice(blanks)
    r = coords[0]
    c = coords[1]
    val = full[r][c]

    partial[r][c] = val
    return partial

def Check_for_Completion(partial):
    complete = False
    for i in range(0,6):
        for j in range(0,6):
            if partial[i][j] == 0:
                complete = False
                break
            else:
                complete = True
    return complete


#print(Check_for_Completion(part))

#print(full)
#print(Hint_Generator(part, full))





