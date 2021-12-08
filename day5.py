result = {}

with open('day5_input.txt', 'r') as f:
    for line in f:
        start, end = line.split(" -> ")
        x1,y1 = start.split(",")
        x2,y2 = end.split(",")

        x1 = int(x1.strip())
        y1 = int(y1.strip())
        x2 = int(x2.strip())
        y2 = int(y2.strip())

        if x1 == x2:
           print("Generating points for horisontal line", line)
           for i in range(min(y1,y2),max(y1,y2) + 1):
               point = (x1,i)
               if point not in result:
                   result[point] = 0
               result[point] += 1

        elif y1 == y2:
            print("Generating points for vertical line", line)
            for i in range(min(x1,x2),max(x1,x2) + 1):
               point = (i,y1)
               
               if point not in result:
                   result[point] = 0
               result[point] += 1

# How many points do at least two lines overlap?
print(sum(value >= 2  for value in result.values()))
            

        



