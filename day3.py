# What are the power consumption and life support rating of the submarine?

import pandas as pd 

def convert_binary_to_decimal(binary_number):
    return int(int("".join(binary_number), 2))

def get_gamma_epsilon_rate(df):
    gamma_rate = []
    epsilon_rate = []
    
    for col in df.columns:
        gamma_rate.append(df[col].value_counts().idxmax())
        epsilon_rate.append(df[col].value_counts().idxmin())

    gamma_rate_decimal = int(int("".join(gamma_rate), 2))
    epsilon_rate_decimal = int(int("".join(epsilon_rate), 2))

    return (gamma_rate_decimal, epsilon_rate_decimal)


def calculate_power_consumption(gamma_epsilon_rate):
    return gamma_epsilon_rate[0] * gamma_epsilon_rate[1]


def find_oxygen_generator_rating(df):
    for col in df.columns:
        if df[col].count() == 2:
            df = df.loc[df[col].str.startswith('1')]
        elif df[col].count() == 1:
            break
        else:
            if df[df[col] == '1'].shape[0] == df[df[col] == '0'].shape[0]:
                 df = df.loc[df[col].str.startswith('1')]
            elif df[col].value_counts().idxmax() == '1':
                df = df.loc[df[col].str.startswith('1')]
            elif df[col].value_counts().idxmax() == '0':
                df = df.loc[df[col].str.startswith('0')]
    return df.to_string(header=False,index=False,index_names=False).split(' ')

def find_CO2_scrubber_rating(df):
    for col in df.columns:

        if df[col].count() == 2:
            df = df.loc[df[col].str.startswith('0')]
        elif df[col].count() == 1:
            break
        else:
            if df[df[col] == '1'].shape[0] == df[df[col] == '0'].shape[0]:
                df = df.loc[df[col].str.startswith('0')]
            elif df[col].value_counts().idxmin() == '1':
                df = df.loc[df[col].str.startswith('1')]
            elif df[col].value_counts().idxmin() == '0':
                df = df.loc[df[col].str.startswith('0')]
    return df.to_string(header=False,index=False,index_names=False).split(' ')

def find_life_support_rating(oxygen_generator_rating, CO2_scrubber_rating):
    return oxygen_generator_rating * CO2_scrubber_rating

with open('day3_input.txt', 'r') as f:
    data = []
    for value in f:
        data.append(list(value.rstrip('\n')))

"""
Part One
"""
df = pd.DataFrame(data)
gamma_epsilon_rate = get_gamma_epsilon_rate(df)
power_consumption = calculate_power_consumption(gamma_epsilon_rate)
print("Power consumption of the submarine is", power_consumption)


"""
Part Two
"""

oxygen_generator_rating_binary = find_oxygen_generator_rating(df)
oxygen_generator_rating_decimal = convert_binary_to_decimal(oxygen_generator_rating_binary)

CO2_scrubber_rating_binary = find_CO2_scrubber_rating(df)
CO2_scrubber_rating_deimal = convert_binary_to_decimal(CO2_scrubber_rating_binary)

life_support_rating = find_life_support_rating(oxygen_generator_rating_decimal, CO2_scrubber_rating_deimal)
print("Life support rating of the submarine is", life_support_rating)