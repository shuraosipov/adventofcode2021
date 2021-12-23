def load_data() -> str:
    with open('solutions/day16_input.txt', 'r') as f:
        return f.readline().strip()

def hex_to_deci(hex_string) -> str:
    binary_string = str()
    for c in hex_string:
        binary_string += hex_to_deci_map[c]
    return binary_string

def get_version(packet, start_index) -> int:
    return int(packet[start_index+0:start_index+3],2)

def get_type_id(packet, start_index) -> int:
    return int(packet[start_index+3:start_index+6],2)

def get_len_type_id(packet, start_index) -> int:
    return int(packet[start_index+6],2)

def get_literal_value(packet, start_index) -> str:
    return int(packet[start_index+1:start_index+5], 2)

def get_length_of_the_sub_packets_in_bits(binary_string, start_index, len) -> int:
    return int(binary_string[start_index+7:start_index+7+len], 2)

def parse(binary_string, i, packet_depth):
    global answer1
    packet_version = get_version(binary_string, i)
    answer1 += packet_version
    type_id = get_type_id(binary_string, i)

    if type_id == 4: # Calculating literal value
        i += 6
        literal_value = 0
        while True:
            literal_value = literal_value*16 + get_literal_value(binary_string, i)
            i += 5 
            if binary_string[i-5] == '0':
                return literal_value, i
    else:
        len_id = get_len_type_id(binary_string, i)
        packets = []
        if len_id == 0:
            len_bits = get_length_of_the_sub_packets_in_bits(binary_string, i, len=15)
            start_i = i+7+15
            i = start_i
            while True:
                v, next_i = parse(binary_string, i, packet_depth+1)
                packets.append(v)
                i = next_i
                if next_i - start_i == len_bits:
                    break
        else:
            num_of_packets =get_length_of_the_sub_packets_in_bits(binary_string, i, len=11)
            i += 7+11
            for t in range(num_of_packets):
                v, next_i = parse(binary_string, i, packet_depth+1)
                packets.append(v)
                i = next_i
        
        if type_id == 0:
            return sum(packets), i
        elif type_id == 1:
            ans = 1
            for v in packets:
                ans *= v
            return ans, i
        elif type_id == 2:
            return min(packets), i
        elif type_id == 3:
            return max(packets), i
        elif type_id == 5:
            return (1 if packets[0] > packets[1] else 0), i
        elif type_id == 6:
            return (1 if packets[0] < packets[1] else 0), i
        elif type_id == 7:
            return (1 if packets[0] == packets[1] else 0), i
        else:
            assert False, type_id

hex_to_deci_map = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}

binary_string = hex_to_deci(load_data())
answer1 = 0      
value, next_i  = parse(binary_string, 0, 0)
print(answer1)
print(value)
