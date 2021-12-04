from pathlib import Path

if __name__ == "__main__":
    print(f"Reading the data file")
    with open(Path("data")/"i01.data") as f:
        prev_line = int(f.readline().rstrip('\n'))
        increases = 0
        for line in f:
            current_line = int(line.rstrip('\n'))
            if  current_line > prev_line:
                increases = increases + 1
            prev_line = current_line
    
    print(f"Total number of increases: {increases}")