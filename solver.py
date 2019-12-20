grid = [
        [5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]
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
    if currentPosition[1] >=3 and currentPosition[0] <6:
        column = 4
    if currentPosition[1] >=6:
        column = 7
    square = [
        [grid[row-1][column -1], grid[row-1][column],grid[row-1][column+1]],
        [grid[row][column -1], grid[row][column], grid[row][column+1]],
        [grid[row+1][column -1], grid[row+1][column],grid[row+1][column+1]]
    ]
    return square

def backtrack():
    newPosition =  visitedPositions.pop()
    solve(newPosition)

def getNextPosition(currentPosition):
    if currentPosition[0]<8:
        return (currentPosition[0]+1,currentPosition[1])
    else:
        return (0,currentPosition[1]+1)


def solve(currentPosition):
    value = grid[currentPosition[0]][currentPosition[1]]
    if value != 0:
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
    if nextPosition[0] >=9 and nextPosition[1]>=9:
        return True
    else:
        print("------------------------------------------")
        for row in grid:
            print(row)
        solve(nextPosition)

def main():
    for row in grid:
        print(row)
    
    solve((0,0))

    for row in grid:
       print(row)

if __name__ == "__main__":
    main()

