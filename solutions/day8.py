def find_1_4_7_8():
    for signal in signal_patterns:
        if len(signal) in [7,2,3,4]:
            if len(signal) == 7:
                Y[8] = signal           
            elif len(signal) == 2:
                Y[1] = signal               
            elif len(signal) == 3:
                Y[7] = signal               
            elif len(signal) == 4:
                Y[4] = signal

def find_0_2_3_5_6_9():
    for signal in signal_patterns:
        if len(signal) in [5,6]:
            if len(signal) == 5:
                if set(signal + Y[1]) == set(signal):
                    Y[3] = signal
                elif set(signal + Y[4]) == set(Y[8]):
                        Y[2] = signal
                else:
                    Y[5] = signal

            elif len(signal) == 6:
                if set(signal + Y[1]) != set(signal):
                    Y[6] = signal
                elif set(signal + Y[5]) == set(signal):
                    Y[9] = signal
                else:
                    Y[0] = signal

def find_output():
    output_value = []
    for o in output_values:
        value = sorted(o)

        for k,v in Y.items():
            nv = sorted(v)
            if value == nv:
                output_value.append(str(k))
    value = "".join(output_value)
    results_p2.append(int(value))


Y = {}
results_p1 = 0
results_p2 = []

with open('day8_input.txt', 'r') as f:
    for line in f:
        new_line = line.split('|')
        signal_patterns = sorted(new_line[0].split(), key=len)
        output_values = new_line[1].split()

        for value in output_values:
            if len(value) in [2,4,3,7]:
                results_p1 += 1

        find_1_4_7_8()               
        find_0_2_3_5_6_9()
        find_output()

print("Part One: ", results_p1)
print("Part Two: ", sum(results_p2))