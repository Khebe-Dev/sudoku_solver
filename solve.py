import sys

# sys.argv = ["solve.py", "path/to/puzzle.txt", "-o", "path/to/solved_puzzle.txt"]

def main():
    # call open input file 
    grid = open_input_file()
    print(f"Unsolved sudoko puzzle: \n{grid}\n")

    # call validity for simple check
    validity(grid)

def open_input_file():
    try:
        filename = sys.argv[1]
        with open(filename, "r") as input_file:
            grid = input_file.read()
            return grid

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
    except IndexError:
        print("Error: Missing input file argument.")
    except Exception as e:
        print(f"Unexpected error: {e}") 

def validity(grid):
    for lines in grid.splitlines():
        # remove empty space, convert to integer of list
        lines = list(map(int, lines.replace(" ", "")))
        print(lines)
        



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 solve.py path/to/puzzle.txt") #-o path/to/solved_puzzle.txt
    else:
        main()