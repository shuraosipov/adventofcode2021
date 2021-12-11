
counter = 0

with open('day8_input.txt', 'r') as f:
    for line in f:
        new_line = line.split('|')
        signal_patterns = new_line[0].split()
        output_values = new_line[1].split()

        for value in output_values:

            if len(value) in [2,4,3,7]:
                counter += 1

                
print(counter)


            
                
                    



        