def printSuduku(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print()
    return


def findEmptyLocation(board, l):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                l[0] = i
                l[1] = j
                return True
    return False


def isRowAvailable(row, board, num):
    for i in range(9):
        if board[row][i] == num:
            return True
    return False


def isColAvailable(col, board, num):
    for i in range(9):
        if board[i][col] == num:
            return True
    return False


def isBoxAvailable(row, col, board, num):
    for i in range(3):
        for j in range(3):
            if board[i + row][j + col] == num:
                return True
    return False


def checkLocationSafe(board, row, col, num):
    return not isRowAvailable(row, board, num) and not isColAvailable(col, board, num) and not isBoxAvailable(
        row - row % 3, col - col % 3, board, num)
    #     return True


def solveSudoku(board):
    # Implement Your Code Here
    n = len(board)
    l = [0, 0]

    if not findEmptyLocation(board, l):
        return True

    row = l[0]
    col = l[1]
    for num in range(1, 10):
        if checkLocationSafe(board, row, col, num):
            board[row][col] = num

            if solveSudoku(board):
                return True
            board[row][col] = 0
    return False


board = [[int(ele) for ele in input().split()] for i in range(9)]
ans = solveSudoku(board)
if ans is True:
    printSuduku(board)
    print('true')
else:
    print('false')
