
counter = 0

Y = {}

with open('day8_input.txt', 'r') as f:
    counter = 0
    for line in f:
        new_line = line.split('|')
        signal_patterns = sorted(new_line[0].split(), key=len)
        output_values = new_line[1].split()
        
        outputs = []
        for i in output_values:
            outputs.append(i)
        Y[8] = max(signal_patterns)
        #print(signal_patterns)
        
        for signal_pattern in signal_patterns:
            
            signal = signal_pattern
            if len(signal) == 7:
                Y[8] = signal           
            if len(signal) == 2:
                Y[1] = signal               
            if len(signal) == 3:
                Y[7] = signal               
            if len(signal) == 4:
                Y[4] = signal               
            
            if len(signal) == 5:
                if set(signal + Y[1]) == set(signal): # find 3
                    Y[3] = signal
                elif set(signal + Y[4]) == set(Y[8]):
                     Y[2] = signal
                else:
                    Y[5] = signal

            if len(signal) == 6:
                if set(signal + Y[1]) != set(signal): # find 6
                    Y[6] = signal
                elif set(signal + Y[5]) == set(signal):
                    Y[9] = signal
                else:
                    Y[0] = signal

        print("Iteration #",counter)
        print(signal_patterns, new_line[1])  
        # for k,v in Y.items():
        #     print(k,v)
        
        output_value = []

        for o in outputs:
            value = sorted(o)
            #print(value)

            for k,v in Y.items():
                nv = sorted(v)
                #print(k,nv)
                if value == nv:
                    output_value.append(str(k))

        print("".join(output_value))
        counter +=1 


                
            
#print(outputs)

# for k,v in Y.items():
#     print(k,v)

# output_value = []

# for o in outputs:
#     value = sorted(o)
#     #print(value)

#     for k,v in Y.items():
#         nv = sorted(v)
#         #print(k,nv)
#         if value == nv:
#             output_value.append(str(k))

# print("".join(output_value))



#     for o in outputs:
#         if sorted(o) == nv:
#             output_value.append(k)


# print(output_value)
    





# number = []
# for o in outputs:
#     if o in Y.items():

        

                


                
#print(counter)


# Map wires to signals knowing signal patters for digits 1,4,7 and 8.
# In other words where to put signal 'a' -> 'g' on the wire?

# Example input
# acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
# cdfeb fcadb cdfeb cdbaf

# Start with a signal pattern for digit 1 - which is 'ab'
# Continue with a signal pattern for digit 7 - which is 'dab'
# When use signal pattern for digit 4 - which is 'eafb'
# Finalize with signal pattern for 8 - which is 'acedgfb'

# At this stage we know 4 digits and their corresponding signal patterns

# There are 6 signal patterns left:
# a) five-character patterns (gcdfa, fbcad, cdfbe) for digits 2,3 and 5
# b) and six-character (cefabd, cdfgeb, cagedb) patterns for digits 9,6 and 0

# And we do not know location of two signals - `c` and `g`
