class Graph_Adjacency_List:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = {i: [] for i in range(vertices)}  # Initialize adjacency list as a dictionary

    def add_edge(self, source, destination):
        if source < 0 or source >= self.vertices or destination < 0 or destination >= self.vertices:
            print("Source and destination must be valid vertex indices.")
        else:
            if destination not in self.graph[source]:  # Avoid duplicate edges
                self.graph[source].append(destination)
                self.graph[destination].append(source)  # For undirected graph

    def display(self):
        for vertex, neighbors in self.graph.items():
            print(f"{vertex}: {neighbors}")

    def dfs_with_stack(self, src):
        visited = [False] * self.vertices
        stack = [src]

        while stack:
            node = stack.pop()
            if not visited[node]:
                print(node, end=" ")
                visited[node] = True
                for neighbor in reversed(self.graph[node]):
                    if not visited[neighbor]:
                        stack.append(neighbor)

g = Graph_Adjacency_List(10)
g.add_edge(1, 3)
g.add_edge(1, 2)
g.add_edge(2, 5)
g.add_edge(2, 4)
g.add_edge(4, 6)
g.add_edge(4, 8)
g.add_edge(8, 9)
g.add_edge(9, 7)
g.add_edge(7, 3)
g.add_edge(7, 6)

g.display()
g.dfs_with_stack(1)  # Start DFS from vertex 1
