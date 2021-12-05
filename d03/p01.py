from pathlib import Path

input_file = "i01.data"
with open(Path("./data/")/input_file) as f:
    data = f.readlines()
    data = [ x.rstrip('\n') for x in data ]
data_len = len(data)

def get_mcb_at(index):
    num_ones = sum([ int(x[index]) for x in data])
    num_zeros = data_len - num_ones
    if num_ones >= num_zeros:
        return '1'
    else:
        return '0'

if __name__ == "__main__":
    gamma_rate = str()
    epsilon_rate = str()
    #Each binary number has 5 digits
    for i in range(12):
        gamma_rate = gamma_rate + get_mcb_at(i)
    
    epsilon_rate = ''.join('1' if x=='0' else '0' for x in gamma_rate)

    int_gamma = int(gamma_rate, 2)
    int_epsilon = int(epsilon_rate, 2)
    ans = int_gamma * int_epsilon
    print(f"Gamma rate ({gamma_rate}) is {int_gamma}")
    print(f"Gamma rate ({epsilon_rate}) is {int_epsilon}")
    print(f"Power consumption is {ans}")