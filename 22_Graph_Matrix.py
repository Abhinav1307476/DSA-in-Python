class Graph_Matrix:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0] * self.vertices for _ in range(self.vertices)]  # Initialize adjacency matrix with zeros

    def add_edge(self, source, destination):
        if source < 0 or source >= self.vertices or destination < 0 or destination >= self.vertices:
            print("Source and destination must be valid vertex indices.")
        else:
            self.graph[source][destination] = 1
            # self.graph[destination][source] = 1  # For undirected graph

    def display(self):
        for row in self.graph:
            print(row)

g = Graph_Matrix(5)
g.add_edge(0, 1)
g.add_edge(0, 4)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.display()