from collections import deque
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

    def bfs_with_queue(self, src):
        visited = [False] * self.vertices
        queue = deque([src])
        visited[src] = True

        while queue:
            node = queue.popleft()
            print(node, end=" ")
            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

g = Graph_Adjacency_List(8)
g.add_edge(1, 3)
g.add_edge(1, 2)
g.add_edge(2, 4)
g.add_edge(3, 4)
g.add_edge(4, 5)
g.add_edge(5, 6)
g.add_edge(6, 7)

g.display()
g.bfs_with_queue(1)  # Start BFS from vertex 1
