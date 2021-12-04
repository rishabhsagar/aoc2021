from pathlib import Path

def get_data(input_file):
    with open(Path("./data/")/input_file) as f:
        data = f.readlines()
        data = [ x.rstrip('\n') for x in data ]
    return data


# Define movement functions
def go_forward(value):
    # move h_pos by value, depth by (bearing * value), bearing remains same
    return ((coords[0] + value), coords[1] + (coords[2] * value), coords[2])

def go_down(value):
    # change only bearing down by value
    return ((coords[0], coords[1], coords[2] + value))

def go_up(value):
    # change only bearing down by value
    return ((coords[0], coords[1], coords[2] - value))

# Set the initial coordinates
coords = (0, 0,0) # (h_pos, depth, bearing)

if __name__ == "__main__":

    input_file = "i01.data"
    data = get_data(input_file)

    step_map = {"forward": go_forward, "down": go_down, "up": go_up}

    for i, step in enumerate(data, start=1):
        instruction, value = [x for x in step.split() ]
        value = int(value)

        # execute parsed instructions
        coords = step_map[instruction](value)
        print("After step", i, "executing", step, "status is", coords)
    
    print("Final coords", coords)
    print(coords[0] * coords[1])