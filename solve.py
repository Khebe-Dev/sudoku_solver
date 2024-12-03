import sys

# sys.argv = ["solve.py", "path/to/puzzle.txt", "-o", "path/to/solved_puzzle.txt"]

def main(filename):
    try:
        filename = sys.argv[1]
        with open(filename, "r") as input:
            grid = input.read()
        print(grid)

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 solve.py path/to/puzzle.txt") #-o path/to/solved_puzzle.txt
    else:
        main(sys.argv[1])