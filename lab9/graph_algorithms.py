from collections import deque
import heapq

# Step 1: Implement the Graph Class

class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, vertex1, vertex2, weight=1):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph[vertex1].append((vertex2, weight))
        self.graph[vertex2].append((vertex1, weight))  # For undirected graph
    
    def print_graph(self):
        for vertex in self.graph:
            print(f"{vertex}: {', '.join([f'{neighbor}({weight})' for neighbor, weight in self.graph[vertex]])}")


# Step 2: Implement Depth-First Search (DFS)

    def dfs(self, start_vertex):
        visited = set()
        self._dfs_recursive(start_vertex, visited)
    
    def _dfs_recursive(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=' ')
        
        for neighbor, _ in self.graph[vertex]:
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited)


# Step 3: Implement Breadth-First Search (BFS)

    def bfs(self, start_vertex):
        visited = set()
        queue = deque([start_vertex])
        visited.add(start_vertex)

        while queue:
            vertex = queue.popleft()
            print(vertex, end=' ')

            for neighbor, _ in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)


# Step 4: Implement a Method to Find All Paths

    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in self.graph:
            return []
        paths = []
        for neighbor, _ in self.graph[start_vertex]:
            if neighbor not in path:
                new_paths = self.find_all_paths(neighbor, end_vertex, path)
                for new_path in new_paths:
                    paths.append(new_path)
        return paths


# Step 5: Implement a Method to Check if the Graph is Connected

    def is_connected(self):
        if not self.graph:
            return True
        start_vertex = next(iter(self.graph))
        visited = set()
        self._dfs_recursive(start_vertex, visited)
        return len(visited) == len(self.graph)


# Step 6: Implement a Method to Find the Shortest Path Using BFS

    def find_shortest_path(self, start_vertex, end_vertex):
        # Check if both vertices are in the graph
        if start_vertex not in self.graph or end_vertex not in self.graph:
            return None
        visited = {start_vertex}  # Set to keep track of visited vertices
        queue = deque([(start_vertex, [start_vertex])])  # Queue for BFS, holding current vertex and path

        while queue:
            current_vertex, path = queue.popleft()  # Dequeue an element

            # If we've reached the end vertex, return the path
            if current_vertex == end_vertex:
                return path

            # Explore neighbors
            for neighbor, _ in self.graph[current_vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)  # Mark neighbor as visited
                    queue.append((neighbor, path + [neighbor]))  # Enqueue neighbor and the new path

        return None  # No path found


# Step 7: Implement a Method to Detect Cycles

    def has_cycle(self):
        visited = set()  # Set to track visited vertices
        for vertex in self.graph:
            # If the vertex has not been visited, check for cycles
            if vertex not in visited:
                if self._has_cycle_dfs(vertex, visited, -1):
                    return True  # Cycle found
        return False  # No cycles found

    def _has_cycle_dfs(self, vertex, visited, parent):
        visited.add(vertex)  # Mark current vertex as visited
        
        for neighbor, _ in self.graph[vertex]:
            # If neighbor has not been visited, recursively check for cycles
            if neighbor not in visited:
                if self._has_cycle_dfs(neighbor, visited, vertex):
                    return True
            # If the neighbor is visited and not the parent, a cycle exists
            elif neighbor != parent:
                return True
        return False  # No cycles found


# Step 8: Implement Dijkstra's Algorithm to Find the Shortest Path in a Weighted Graph

    def dijkstra(self, start_vertex):
        # Check if the starting vertex is in the graph
        if start_vertex not in self.graph:
            return None
        
        # Initialize distances to all vertices as infinity and set the starting vertex distance to 0
        distances = {vertex: float('inf') for vertex in self.graph}
        distances[start_vertex] = 0
        priority_queue = [(0, start_vertex)]  # Min-heap for priority queue

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)  # Get vertex with the smallest distance

            # Skip processing if the current distance is greater than the recorded distance
            if current_distance > distances[current_vertex]:
                continue

            # Explore neighbors
            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight  # Calculate new distance
                
                # Update distance if the new distance is shorter
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))  # Add neighbor to the priority queue

        return distances  # Return shortest distances from the start vertex


# Step 9: Implement a Method to Determine if the Graph is Bipartite

    def is_bipartite(self):
        color = {}  # Dictionary to store colors of vertices
        for vertex in self.graph:
            if vertex not in color:  # Check uncolored vertices
                if not self._is_bipartite_dfs(vertex, color, 0):  # Start coloring with color 0
                    return False  # Not bipartite
        return True  # All vertices can be colored in two colors


    def _is_bipartite_dfs(self, vertex, color, c):
        color[vertex] = c  # Assign color to the vertex
        for neighbor, _ in self.graph[vertex]:
            if neighbor not in color:  # If neighbor is not colored, color it with opposite color
                if not self._is_bipartite_dfs(neighbor, color, 1 - c):
                    return False  # Not bipartite
            elif color[neighbor] == c:  # If neighbor has the same color, it's not bipartite
                return False
        return True  # All neighbors can be colored properly


# Test the Graph class (Step 1)
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.print_graph()


# Test DFS (Step 2)
print("\nDFS starting from vertex 0:")
g.dfs(0)


# Test BFS (Step 3)
print("\nBFS starting from vertex 0:")
g.bfs(0)


# Test finding all paths (Step 4)
print("\nAll paths from vertex 0 to vertex 3:")
all_paths = g.find_all_paths(0, 3)
for path in all_paths:
    print(' -> '.join(map(str, path)))


# Test if the graph is connected (Step 5)
print("\nIs the graph connected?", g.is_connected())

# Add a disconnected vertex and test again
g.add_vertex(4)
print("After adding a disconnected vertex:")
print("Is the graph connected?", g.is_connected())


# Test finding the shortest path (Step 6)
print("\nShortest path from vertex 0 to vertex 3:")
shortest_path = g.find_shortest_path(0, 3)
if shortest_path:
    print(' -> '.join(map(str, shortest_path)))
else:
    print("No path found.")


# Test for cycle detection (Step 7)
print("\nDoes the graph contain a cycle?", g.has_cycle())

# Add an edge to create a cycle and test again (Step 7)
g.add_edge(4, 0, 7)
print("After adding an edge to create a cycle:")
print("Does the graph contain a cycle?", g.has_cycle())


# Test Dijkstra's algorithm (Step 8)
print("\nShortest distances from vertex 0 using Dijkstra's algorithm:")
distances = g.dijkstra(0)
for vertex, distance in distances.items():
    print(f"Vertex {vertex}: Distance {distance}")


# Test for bipartiteness (Step 9)
print("\nIs the graph bipartite?", g.is_bipartite())

# Create a non-bipartite graph and test again (Step 9)
g.add_edge(4, 5)
g.add_edge(5, 1)
print("After adding edges to create a non-bipartite graph:")
print("Is the graph bipartite?", g.is_bipartite())
