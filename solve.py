import sys
# sys.argv = ["solve.py", "path/to/puzzle.txt", "-o", "path/to/solved_puzzle.txt"]

def main(filename):

    try:

        filename = sys.argv[1]
        with open(filename, "r") as input_file:
            grid = input_file.read().strip()

        # Remove spaces or other non-numeric characters
        box_grid = ''.join(filter(str.isdigit, grid))

        
        if len(box_grid) != 81:
            print("Error: The input Sudoku grid is not valid")


        grid = [[int(box_grid[row * 9 + col]) for col in range(9)] for row in range(9)]

        print("Input Sudoku Grid:")
        print_grid(grid)

        if solve(grid):
            print("\nSolved Sudoku Grid:")
            print_grid(grid)
        else:
            print("\nThis Sudoku puzzle cannot be solved.")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
    except Exception as e:
        print(f"Error: {e}")

def solve(grid):

    find = find_empty(grid)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if validity(grid, i, (row, col)):
            grid[row][col] = i
            if solve(grid):
                return True
            grid[row][col] = 0

    return False

def validity(grid, num, pos):

    # Check row
    for i in range(len(grid[0])):
        if grid[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(grid)):
        if grid[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if grid[i][j] == num and (i, j) != pos:
                return False
    # print(f"this is puzzle:  \n{grid}")
    for line in grid:
        print(line)
    print(f"position: {pos}")
    print(f"number puzzle: {num}")
            
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

def find_empty(grid):

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 0:
                return (row, col)
    return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 solve.py path/to/puzzle.txt")
    else:
        main(sys.argv[1])