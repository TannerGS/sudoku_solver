board = [
    [0,0,0,2,6,0,7,0,1],
    [6,8,0,0,7,0,0,9,0],
    [1,9,0,0,0,4,5,0,0],
    [8,2,0,1,0,0,0,4,0],
    [0,0,4,6,0,2,9,0,0],
    [0,5,0,0,0,3,0,2,8],
    [0,0,9,3,0,0,0,7,4],
    [0,4,0,0,5,0,0,3,6],
    [7,0,3,0,1,8,0,0,0]
]

# Solve
def solve(bd):        
    find = find_empty(bd) 
    
    if not find:
        return True
    else:
        row, col = find
        
    for i in range(1, 10):
        if valid(bd, i, (row, col)):
            bd[row][col] = i
            
            if solve(bd):
                return True
            
            bd[row][col] = 0
        
    return False

# Validate
def valid(bd, num, pos):
    # Check Row
    for i in range(len(bd[0])):
        if bd[pos[0]][i] == num and pos[1] != i:
            return False
        
    # Check Column
    for i in range(len(bd)):
        if bd[i][pos[1]] == num and pos[0] != i:
            return False
        
    # Check Square
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bd[i][j] == num and (i, j) != pos:
                return False
            
    return True

# Print Board
def print_board(bd):
    for i in range(len(bd)):
        if i % 3 == 0 and i != 0:
            print('------------------------')
        for j in range(len(bd[0])):
            if j % 3 == 0 and j != 0:
                print(' | ', end='')
            if j == 8:
                print(bd[i][j])
            else:
                print(str(bd[i][j]) + ' ', end='')

# Find Empty
def find_empty(bd):
    for i in range(len(bd)):
        for j in range(len(bd[0])):
            if bd[i][j] == 0:
                return (i, j)
    
    return False
            
print('\n' + 'Starting Sudoku Board' + '\n')
print_board(board)
solve(board)
print('\n' + '--------------------' + '\n')
print( '\n' + 'Solved Sudoku Board' + '\n')
print_board(board)
print('\n' + '--------------------' + '\n')
