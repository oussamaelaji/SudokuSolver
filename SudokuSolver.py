import time
def solver(matrix):
    for i in matrix:
        if 0 in i:
            Not_filled=True
            break
        else:
            Not_filled=False
    if Not_filled:
        fillnext = find_unassigned(matrix)
        posvals = possibleValues(matrix, fillnext)
        for value in posvals:
            matrix[fillnext[0]][fillnext[1]] = value
            if solver(matrix):
                return matrix
            else:
                matrix[fillnext[0]][fillnext[1]] = 0
    else:
        return True

def possibleValues(matrix, pos, bSize=3):
    val = []
    box = []
    column = [row[pos[1]] for row in matrix]
    x=(pos[0]//bSize)*bSize
    y=(pos[1]//bSize)*bSize
    for i in range(x,x+3):
        for j in range(y,y+3):
            box.append(matrix[i][j])
    for iter in range(1,10):
        if not iter in matrix[pos[0]] and not iter in column and not iter in box:
            val.append(iter)
    return val

def find_unassigned(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == 0:
                return (i, j)    
def sudoku(m):
    for i in range(len(m)):
        if i%3 == 0 and i!=0:
            print("- - - - - - - - - - - -")
        for j in range(len(m[0])):
            if j%3==0 and j!=0:
                print(" | ", end="")
            if m[i][j]!=0:
                if j==8:
                    print(m[i][j])
                else:
                    print(f"{m[i][j]} ", end="")
            else:
                if j==8:
                    print("-")
                else:
                    print("- ", end="")
matrix = [
    [0,0,1,0,0,4,2,0,0],
    [0,0,0,6,3,0,0,0,0],
    [0,0,0,0,1,0,0,0,0],
    [7,0,6,0,4,0,8,3,0],
    [0,5,0,0,0,0,0,0,7],
    [0,0,2,5,0,0,0,6,0],
    [8,9,0,0,0,0,0,0,0],
    [3,0,0,0,6,0,0,5,0],
    [0,0,0,0,0,8,0,0,4]
]
time1 = time.perf_counter()
sudoku(matrix)
print("=======================")
sudoku(solver(matrix))
time2 = time.perf_counter()
print(f"Elapsed time : {time2 - time1:0.4f} seconds")