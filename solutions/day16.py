def load_data() -> str:
    with open('solutions/day16_input.txt', 'r') as f:
        return f.readline().strip()

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


def is_multiple_of_4(n) -> bool:
    if n & 3 == 0:
        return True
    return False

def hex_to_deci(hex_string) -> str:
    binary_string = str()
    for c in hex_string:
        binary_string += hex_to_deci_map[c]
    return binary_string

def get_packet_version(packet) -> int:
    return int(packet[:3],2)

def get_packet_type_id(packet) -> int:
    return int(packet[3:6],2)

def get_length_type_id(packet) -> int:
    return int(packet[7],2)

def get_literal_value(packet) -> str:
    packet = packet[6:]
    literal_value_with_binary_representation = []
    for i in range(0, len(packet), 5):
        five_bits = packet[i:i+5]
        first_bit = five_bits[0]
        four_bits = five_bits[1:]        
        
        if first_bit == '0':
            literal_value_with_binary_representation.append(four_bits)
            return "".join(literal_value_with_binary_representation)
            
        literal_value_with_binary_representation.append(four_bits)

def convert_literal_value_to_decimal(literal_value) -> int:
    return int(literal_value, 2)


def get_length_of_the_sub_packets_in_bits(packet, length=15) -> int:
    return int(packet[7:7+length],2)


def find_sub_packets(packet, length_of_the_sub_packets_in_bits):

    pass

binary_string = hex_to_deci(load_data())
packet_version = get_packet_version(binary_string)
packet_type_id = get_packet_type_id(binary_string)

if packet_type_id == 4:
    print("Calculating literal value")
    literal_value = get_literal_value(binary_string)
    print(literal_value)
    print(convert_literal_value_to_decimal(literal_value))

else:

    print("Calculating operator packet that contains one or more packets.")
    length_type_id = get_length_type_id(binary_string)

    if length_type_id == 0:
        print("Calculating the total length in bits of the sub-packets contained by this packet")
        print("The packet version",packet_version)
        print("The packet type ID",packet_type_id)
        print("The length type ID",length_type_id)
        print("The length of the sub-packets in bits", get_length_of_the_sub_packets_in_bits(binary_string, length=15))


    elif length_type_id == 1:
        print("Calculating number of sub-packets immediately contained by this packet")

print(convert_literal_value_to_decimal(get_literal_value('11010001010')))
print(convert_literal_value_to_decimal(get_literal_value('0101001000100100')))



        






