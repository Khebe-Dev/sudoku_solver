import sys

def read_input():
    try:
        input_filepath = sys.argv[1]
        with open(input_filepath, "r") as input_file:
            grid = input_file.read()
            return grid

    except Exception as e:
        print(f"Unexpected error: {e}") 
        
def format_grid(grid):
    sudoku_grid = []
    for lines in grid.splitlines():
        sudoku_grid.append([int(num) for num in lines.split()])
    return sudoku_grid

def display_grid(grid):
    for row in grid:
        print(" ".join(str(num) for num in row))

def is_valid(grid, row, col, num):
    for i in range(9):
        if grid[row][i] == num:
            return False
    
    for i in range(9):
        if grid[i][col] == num:
            return False

    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for rows in range(start_row, start_row + 3):
        for columnns in range(start_col, start_col + 3):
            if grid[rows][columnns] == num:
                return False

    return True

def solve_sudoku(grid):
    for row in range(9):
        for col in range(9):
            # empty cell find 
            if grid[row][col] == 0:
                # all num try to find valid
                for num in range(1, 10):
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num

                        print(f"Placing {num} at position ({row + 1}, {col + 1}):")
                        display_grid(grid)
                        print("\n")

                        # repeat process ...
                        if solve_sudoku(grid): 
                            return True
                        
                        # since number combination is not solve_sudoku, erase and restart process (backtrack)
                        grid[row][col] = 0
                return False
    return True

def write_output(grid):
    try:
        output_file = sys.argv[3]
        with open(output_file, "w") as output:
            for row in grid:
                output.write(" ". join(str(num) for num in row) + "\n")
    except Exception as e:
        print(f"Unexpected error: {e}")


def main():
    if len(sys.argv) != 4:
        print("Usage: python3 solve.py path/to/puzzle.txt -o path/to/solved_puzzle.txt")
   
    # read input file, format function for code use, display function for user understanding
    grid = read_input()
    sudoku_grid = format_grid(grid)
    print(f"Solving puzzle from path/to/puzzle.txt: \n")
    display_grid(sudoku_grid)

    # empty cell find, try valid num 
    if solve_sudoku(sudoku_grid):
        print("Solved puzzle to path/to/solved_puzzle.txt")
        write_output(sudoku_grid)
    else:
        print("No solution generated")


if __name__ == "__main__":
        main()