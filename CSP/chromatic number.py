def chromatic_number(graph):
    colors = {} # to store the color of each vertex
    
    def is_valid(vertex, color):
        for adjacent_vertex in graph[vertex]:
            if adjacent_vertex in colors and colors[adjacent_vertex] == color:
                return False
        return True
    
    def backtrack(vertex):
        if vertex is None:
            return True
        
        for color in range(1, len(graph)+1):
            if is_valid(vertex, color):
                colors[vertex] = color
                if backtrack(next_vertex(vertex)):
                    return True
                colors.pop(vertex)
        
        return False
    
    def next_vertex(vertex):
        for next_vertex in graph:
            if next_vertex not in colors:
                return next_vertex
        return None
    
    # start with any vertex and backtrack to color the rest
    start_vertex = list(graph.keys())[0]
    backtrack(start_vertex)
    
    # find the number of colors used
    return max(colors.values())

# example usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E'],
    'D': ['B', 'C', 'E', 'F'],
    'E': ['C', 'D', 'F'],
    'F': ['D', 'E']
}
print(chromatic_number(graph)) # output: 3
