def isSafe(M, row, col, visited):
    global ROW, COL

    return ((row >= 0) and (row < ROW) and (col >= 0) and (col < COL) and (M[row][col] and not visited[row][col]))


def DFS(M, row, col, visited, count):
    global ROW, COL
    n_row = [-1, -1, -1, 0, 0, 1, 1, 1]
    n_col = [-1, 0, 1, -1, 1, -1, 0, 1]
    visited[row][col] = True
    for k in range(8):
        if isSafe(M, row+n_row[k], col+n_col[k], visited):
            count[0] += 1
            DFS(M, row+n_row[k], col+n_col[k], visited,count)


def largestRegion(M):
    global ROW, COL
    visited=[[0] * COL for i in range(ROW)]

    result=-999999999

    for i in range(ROW):
        for j in range(COL):
            if (M[i][j] and not visited[i][j]):
                count=[1]
                DFS(M, i, j, visited, count)

                result=max(result, count[0])
    return result





ROW=4
COL=5
M=[[0, 0, 1, 1, 0],
     [0 ,0, 1, 1, 0],
     [0, 0, 0, 0, 0],
     [0, 0, 0, 0, 1]]

print(largestRegion(M))
