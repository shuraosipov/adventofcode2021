def load_data():
    graph = {}
    with open('solutions/day12_input.txt', 'r') as f:
        for line in f:
            start, end = line.strip().split("-")
            if start not in graph:
                graph[start] = [end]
            else:
                graph[start].append(end)

    return graph

def find_all_paths(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in graph:
            return []
        paths = []
        for node in graph[start]:
            if node not in path:
                newpaths = find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths


# {'start': ['A', 'b'], 'A': ['c', 'b', 'end'], 'b': ['d', 'end']}
# start with parent - start
# for each child get subchilds and print child/subchild relation
# start,A,c,A,b,A,end

        

graph = load_data()
print(graph)

print(find_all_paths(graph, "start", "end"))

