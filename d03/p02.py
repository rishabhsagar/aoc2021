from pathlib import Path

input_file = "i01.data"
with open(Path("./data/")/input_file) as f:
    data = f.readlines()
    data = [ x.rstrip('\n') for x in data ]
digit_len = len(data[0])
diag_len = len(data)
print(f"Read {diag_len} records, each {digit_len} long.")

def get_mcb_at(index, remaining_data):
    num_ones = sum([ int(x[index]) for x in remaining_data])
    num_zeros = len(remaining_data) - num_ones
    if num_ones >= num_zeros:
        return '1'
    else:
        return '0'

def get_lcb_at(index, remaining_data):
    if get_mcb_at(index, remaining_data) == '1':
        return '0'
    else:
        return '1'

if __name__ == "__main__":
    remaining_data = data

    # Find the O2 generator rating
    for i in range(digit_len):
        msb = get_mcb_at(i, remaining_data)
        # filter for mcb appearing at index i
        remaining_data = list(filter(lambda x: x[i] == msb, remaining_data))
        if len(remaining_data) == 1:
            int_o2_gen = int(remaining_data[0], 2)
            print(f"Result found for O2 generator rating {remaining_data[0]} = {int_o2_gen}")
            break

    # Find the Co2 rating
    remaining_data = data
    for i in range(digit_len):
        lsb = get_lcb_at(i, remaining_data)
        #filter for lsb at this index i
        remaining_data = list(filter(lambda x: x[i] == lsb, remaining_data))
        if len(remaining_data) == 1:
            int_co2_gen = int(remaining_data[0], 2)
            print(f"Result found for CO2 generator rating {remaining_data[0]} = {int_co2_gen}")
            break
    
    print(f"Life support rating {int_o2_gen * int_co2_gen}")