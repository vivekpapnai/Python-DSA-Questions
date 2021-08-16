import random


def start_game():
    mat = [[int(0) for j in range(4)] for i in range(4)]
    return mat


def add_new_2(mat):
    r = random.randint(0, 3)
    c = random.randint(0, 3)
    while mat[r][c] != 0:
        r = random.randint(0, 3)
        c = random.randint(0, 3)
    mat[r][c] = 2


def compress(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([0]*4)

    for i in range(4):
        pos = 0
        for j in range(4):
            if mat[i][j] != 0:
                new_mat[i][pos] = mat[i][j]
                pos += 1
    return new_mat

def get_curr_state(mat):
    """ checking if 2048 present in the matrix and u have won or not """
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 2048:
                return 'won'
    """ checking if an empty space is available in the matrix """
    for i in range(0,4):
        for j in range(0,4):
            if mat[i][j] == 0:
                return 'GAME NOT OVER'
    """checking if any row or col can be merged to create an 
        empty space for the first 3 row and column"""

    for i in range(3):
        for j in range(3):
            if mat[i][j] == mat[i][j + 1] or mat[i][j] == mat[i + 1][j]:
                return 'GAME NOT OVER'

    """ checking the any column can be merged in last row """
    for j in range(3):
        if mat[3][j] == mat[3][j+1]:
            return 'GAME NOT OVER'
    """ checking the any row can be merged in last column """
    for i in range(3):
        if mat[i][3] == mat[i+1][3]:
            return 'GAME NOT OVER'

    """ if all above cases fails then you have lost in the game """
    return 'LOST'

mat = start_game()
add_new_2(mat)
get_curr_state(mat)