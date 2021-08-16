"""You are given N, and for a given N x N chessboard, find a way to place N queens such that no queen can attack
any other queen on the chess board.
A queen can be killed when it lies in the same row, or same column, or the same diagonal of any of the other queens.
You have to print all such configurations.
Input Format :
Line 1 : Integer N
Output Format :
One Line for every board configuration.
Every line will have N*N board elements printed row wise and are separated by space
Note : Don't print anything if there isn't any valid configuration.
Constraints :
1<=N<=10
Sample Input 1:
4
Sample Output 1 :
0 1 0 0 0 0 0 1 1 0 0 0 0 0 1 0
0 0 1 0 1 0 0 0 0 0 0 1 0 1 0 0 """


def isSafe(row, col, n, solution):
    # checking for above vertical column we have to check only three condition as we are going row by row
    i = row - 1
    while i >= 0:
        if solution[i][col] == 1:
            return False
        i = i - 1
    # going left upward diagonally direction
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if solution[i][j] == 1:
            return False
        i -= 1
        j -= 1
    i = row - 1
    j = col + 1
    while i >= 0 and j < n:
        if solution[i][j] == 1:
            return False
        i -= 1
        j += 1
    return True


def nQueenHelper(row, n, solution):
    if row == n:
        for i in range(n):
            for j in range(n):
                print(solution[i][j], end=" ")
        print()
        return
    for col in range(n):
        if isSafe(row, col, n, solution) is True:
            solution[row][col] = 1
            nQueenHelper(row + 1, n, solution)
            solution[row][col] = 0

    return


def nQueen(n):
    solution = [[0 for j in range(n)] for i in range(n)]
    nQueenHelper(0, n, solution)
    return


n = int(input())
nQueen(n)
