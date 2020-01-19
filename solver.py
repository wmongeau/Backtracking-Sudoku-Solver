import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, height=650, width = 650)
canvas.pack()

frame = tk.Frame(root,bg='blue')
frame.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.8)

label = tk.Label(root,text="Sudoku Solver")
label.pack()

entry=tk.Entry(frame)
entry.pack()


button = tk.Button(root, text = "Solve")
button.pack()

root.mainloop()

grid = [
        [0,7,0,9,3,8,0,1,0],
        [0,8,0,0,0,0,0,5,0],
        [0,0,0,0,0,0,0,0,0],
        [0,6,0,0,0,0,0,9,0],
        [0,0,0,0,7,0,0,0,0],
        [0,9,0,3,2,5,0,7,0],
        [9,0,2,0,5,0,6,0,7],
        [0,0,0,4,0,7,0,0,0],
        [0,0,4,0,0,0,5,0,0]
    ]

visitedPositions = []

def validRow(row, value):    
    if value not in row:
        return True
    return False

def validColumn(column, value):
    if value not in column:
      return True
    return False
    
def validSquare(square, value):
    if value not in square:
        return True
    return False

def getRow(currentPosition):
    return grid[currentPosition[0]]

def getColumn(currentPosition):
    column = [0] * 10
    i = 0 
    for row in grid:
        column[i]=row[currentPosition[1]]
        i+=1
    return column

def getSquare(currentPosition):
    if currentPosition[0] < 3 :
        row = 1
    if currentPosition[0] >=3 and currentPosition[0] <6:
        row = 4
    if currentPosition[0] >=6:
        row = 7
    if currentPosition[1] < 3 :
        column = 1
    if currentPosition[1] >=3 and currentPosition[1] <6:
        column = 4
    if currentPosition[1] >=6:
        column = 7
    square = [
        grid[row-1][column -1], grid[row-1][column],grid[row-1][column+1],
        grid[row][column -1], grid[row][column], grid[row][column+1],
        grid[row+1][column -1], grid[row+1][column],grid[row+1][column+1]
    ]
    return square

def backtrack():
    newPosition =  visitedPositions.pop()
    solve(newPosition, True)

def getNextPosition(currentPosition):
    if currentPosition[0]<8:
        return (currentPosition[0]+1,currentPosition[1])
    else:
        return (0,currentPosition[1]+1)

def solve(currentPosition, backtracking = False):
    value = grid[currentPosition[0]][currentPosition[1]]
    if value != 0 and not backtracking:
        nextPosition = getNextPosition(currentPosition)
        solve(nextPosition)
    
    valid = False
    row = getRow(currentPosition)
    column = getColumn(currentPosition)
    square = getSquare(currentPosition)
    while not valid:
        value=value+1
        if value>=10:
            grid[currentPosition[0]][currentPosition[1]] = 0
            backtrack()
        else:
            if validRow(row,value) and validColumn(column, value) and validSquare(square, value):
                valid = True
        grid[currentPosition[0]][currentPosition[1]]=value    
    visitedPositions.append(currentPosition)
    nextPosition = getNextPosition(currentPosition)
    solve(nextPosition)

# def main():

#     f=open("sudoku.txt","w+")
#     f.write("Puzzle:\n")
#     for row in grid:
#         for num in row:
#             f.write('%s' %num)
#         f.write('\n')
    
#     try:
#         solve((0,0))
#     except:
#         pass
#     finally:
#         f.write("\n")
#         f.write("Solution:\n")
#         for row in grid:
#             for num in row:
#                 f.write('%s' %num)
#             f.write('\n')

#     f.close()
# if __name__ == "__main__":
#     main()
