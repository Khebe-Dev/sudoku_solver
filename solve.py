# steps
# readme : rules of the game

# create grid 9x9 with small blocks k
    # open puzzle 
    # print to user
# loop rows, col and boxes for possible play k
    # print hint to player
# input from player j
    # check validity no.
    # if wrong:
    # print message and give hint again
    # if right:
    # update grid wiht input and print grid back 
# rep until solved
# solved print in actual boxes j
    # maybe for loop -- range(len(bot))
    # if ... raw % 3 == 0
    # f-string print "|" + end = " "


def validity(grid,num,pos):
    #check row
    for i in range(len(grid[0])):
        if grid[pos[0]][i] == num and pos[1] != i:
            return False
        
    #check column
    for i in range(len(grid)):    
        if grid[i][pos[1]] == num and pos[0] != i:
            return False
    
    #check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for raw in range(box_y * 3, box_y * 3 + 3):
        for col in range(box_x * 3, box_x * 3 + 3):
            if grid[raw][col] == num and (raw,col) != pos:
                return False
    return True
def print_grid(grid):

    for i in range(len(grid)):
        if i % 3 == 0 and i != 0:
            print("--------------------")
            
        for j in range(len(grid[0])):
            if j % 3 == 0 and j != 0:
                print("|", end="")
            if j == 8:
                print(grid[i][j])
            else:
                print(str(grid[i][j]) + " ", end="")

def empty_spaces(grid):
    """ 
    checking for spaces in the grid that are equal to zero 
    """
    for col in range(len(grid)):
        for raw in range(len(grid[0])):
            if grid [col][raw] == 0:
                return col , raw
        return None         
	