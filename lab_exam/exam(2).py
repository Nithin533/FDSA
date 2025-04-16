from collections import deque

class Graph:
    def __init__(self):
       
        self.graph = {}

    def add(self, u, v):
        
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        
       
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self, start_vertex):
       
        if start_vertex not in self.graph:
            print(f"Error: {start_vertex} is not in the graph!")
            return
        
        visited = set()  
        queue = deque([start_vertex]) 
        visited.add(start_vertex)  

        print(f"BFS Traversal starting from {start_vertex}:")
        
        while queue:
            
            vertex = queue.popleft()
            print(vertex, end=" ")  

          
            for neighbor in self.graph.get(vertex, []):
                if neighbor not in visited:
                    visited.add(neighbor)  
                    queue.append(neighbor) 

# Example usage:

graph = Graph()
graph.add(0,2)
graph.add(1, 3)
graph.add(2, 4)
graph.add(3, 5)
graph.add(4, 6)

graph.bfs(0)
