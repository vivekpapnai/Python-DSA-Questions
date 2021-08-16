def mazeHelper(i, j, n, maze, solutionPath):
    if i == n - 1 or j == n - 1:
        solutionPath[i][j] = 1
        for i in range(n):
            print(solutionPath[i])
        return
    if i < 0 or j < 0 or i >= n or j >= n or maze[i][j] == 0 or solutionPath[i][j] == 1:
        return
    solutionPath[i][j] = 1
    mazeHelper(i + 1, j, n, maze, solutionPath)
    mazeHelper(i, j + 1, n, maze, solutionPath)
    mazeHelper(i - 1, j, n, maze, solutionPath)
    mazeHelper(i, j - 1, n, maze, solutionPath)
    solutionPath[i][j] = 0
    return


def mazePath(maze):
    n = len(maze)
    solutionPath = [[0 for j in range(n)] for x in range(n)]
    mazeHelper(0, 0, n, maze, solutionPath)
    return


n = int(input())
maze = []
for i in range(n):
    x = [int(x) for x in input().split()]
    maze.append(x)
mazePath(maze)
