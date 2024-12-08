import sys

# sys.argv = ["solve.py", "path/to/puzzle.txt", "-o", "path/to/solved_puzzle.txt"]

def main():
    # call open input file 
    grid = open_input_file()
    print(f"Solving puzzle from path/to/puzzle.txt: \n{grid}\n")

    # call format grid 
    print(format_grid(grid))



def open_input_file():
    try:
        input_filepath = sys.argv[1]
        with open(input_filepath, "r") as input_file:
            grid = input_file.read().strip()
            return grid

    except FileNotFoundError:
        print(f"Error: File '{input_filepath}' not found")
    except IndexError:
        print("Error: Missing input file argument.")
    except Exception as e:
        print(f"Unexpected error: {e}") 

def format_grid(grid):
    sudoku_grid = []
    for lines in grid.splitlines():
        # remove empty space, convert to integer of list
        line_parts = list(map(int, lines.split()))
        sudoku_grid.append(line_parts)

    return sudoku_grid


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 solve.py path/to/puzzle.txt") #-o path/to/solved_puzzle.txt
    else:
        main()