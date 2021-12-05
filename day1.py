# How many measurements are larger than the previous measurement?

with open('day1_input.txt', 'r') as f:
    measurements = []
    for value in f:
        measurements.append(int(value.rstrip("\n")))

def compare_measurements(measurements):
    """
    Iterate over a sequence of measurements and compare each measurement with previous one.
    There is no measurement before the first measurement.
    
    Return a dict like this:

    result = {
        0: [199, '(N/A - no previous measurement)'],
        1: [200, '(increased)'],
        2: [208, '(decreased)'],
        ...
    }
    """

    result = {}
    previous = None

    for i,m in enumerate(measurements):
        if i == 0:
            previous = m
            result[i] = [m, '(N/A - no previous measurement)']
        else:
            if m > previous:
                result[i] = [m, '(increased)']
            elif m == previous:
                result[i] = [m, '(no change)']
            else:
                result[i] = [m, '(decreased)']
            previous = m
    
    return result



def calculate_total(result: dict) -> int:
    """
    How many measurements are larger than the previous measurement?

    Find all elements where value contains `(increased)` keyword.
    Return number of such elemetns.

    """
    total = 0
    
    for i in result.values():
        if i[1] == '(increased)':
            total += 1

    return total

def get_sum_of_three_measurement_sliding_window(measurements):
    """
    We take a list of measurements as an input.
    And we construct a new list containing sums of a three-measurement sliding window.
    """
    result = []
    windows_size = 3
    for i in range(len(measurements) - windows_size + 1):
        slice = measurements[i: i + windows_size]
        result.append(sum(slice))
    
    return result


sums_of_three_measurement_sliding_window = get_sum_of_three_measurement_sliding_window(measurements)
result = compare_measurements(sums_of_three_measurement_sliding_window)
print(calculate_total(result))




    




    








