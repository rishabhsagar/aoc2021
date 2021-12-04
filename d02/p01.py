from pathlib import Path

def get_data(input_file):
    with open(Path("./data/")/input_file) as f:
        data = f.readlines()
        data = [ x.rstrip('\n') for x in data ]
    return data


# Define movement functions
def go_forward(dist):
    return ((coords[0] + dist), coords[1])

def go_down(dist):
    return (coords[0], coords[1] + dist)

def go_up(dist):
    return (coords[0], coords[1] - dist)

# Set the initial coordinates
coords = (0,0) # (h_dist, depth)

if __name__ == "__main__":

    input_file = "i01.data"
    data = get_data(input_file)

    step_map = {"forward": go_forward, "down": go_down, "up": go_up}

    for step in data:
        instruction, value = [x for x in step.split() ]
        value = int(value)

        # execute parsed instructions
        coords = step_map[instruction](value)
    
    print("Final coords", coords)
    print(coords[0] * coords[1])