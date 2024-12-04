import sys

# sys.argv = ["solve.py", "path/to/puzzle.txt", "-o", "path/to/solved_puzzle.txt"]

def main():
    try:
        filename = sys.argv[1]
        with open(filename, "r") as input_file:
            for lines in input_file:
                lines = lines.strip()
                print(lines)

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found")
    except IndexError:
        print("Error: Missing input file argument.")
    except Exception as e:
        print(f"Unexpected error: {e}")



if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 solve.py path/to/puzzle.txt") #-o path/to/solved_puzzle.txt
    else:
        main()