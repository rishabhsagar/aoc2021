from pathlib import Path

if __name__ == "__main__":
    inc_counter = int()
    print(f"Reading the data file")
    with open(Path("data")/"i01.data") as f:
        data = [ int(x.rstrip('\n')) for x in f.readlines() ]
        for i, v in enumerate(data):
            window = data[i:(i+3)]
            if len(window) == 3:
                if i == 0:
                    prev_window = sum(window)
                else:
                    if sum(window) > prev_window:
                        inc_counter = inc_counter + 1
                    prev_window = sum(window)
    print("Total increases", inc_counter)
