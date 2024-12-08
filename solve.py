import sys

def read_input():
    try:
        input_filepath = sys.argv[1]
        with open(input_filepath, "r") as input_file:
            grid = input_file.read()
            return grid

    except Exception as e:
        print(f"Unexpected error: {e}") 
        sys.exit(1)

def format_grid(grid):
    sudoku_grid = []
    for lines in grid.splitlines():
        sudoku_grid.append([int(num) for num in lines.split()])
    return sudoku_grid

def display_grid(grid):
    for row in grid:
        print(" ".join(str(num) for num in row))

# def is_valid(grid, row, col, num):
#     for i in range(9):

# def row_check(sudoku_grid):
#     for sudoku_grid in range(10):
#         if set(sudoku_grid)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 solve.py path/to/puzzle.txt -o path/to/solved_puzzle.txt")
        sys.exit(1)
   
    # read input file, format function for code use, display function for user understanding
    grid = read_input()
    sudoku_grid = format_grid(grid)
    print(f"Solving puzzle from path/to/puzzle.txt: \n")
    display_grid(sudoku_grid)

 

if __name__ == "__main__":
        main()