
class Graph:
    def __init__(self, vertex_count):
        self.vertex_count = vertex_count
        self.adj_list = {vertex_num:[] for vertex_num in range(vertex_count)}

    def add_edge(self, start, end, weight):
        """To add an edge into the graph using adj. list representation"""
        if 0 <= start < self.vertex_count and 0 <= end < self.vertex_count:
            self.adj_list[start].append((end, weight))
            self.adj_list[end].append((start, weight))
        else:
            print("Invalid vertices")

    def remove_edge(self, start, end):
        """To remove an edge into the graph using adj. list representation"""
        if 0 <= start < self.vertex_count and 0 <= end < self.vertex_count:
            self.adj_list[start] = [(last, weight) for last, weight in self.adj_list[start] if end != last]
            self.adj_list[end] = [(begin, weight) for begin, weight in self.adj_list[end] if start != begin]
        else:
            print("Invalid Vertices")

    def has_edge(self, start, end):
        """To check an edge in Graph"""
        if 0 <= start < self.vertex_count and 0 <= end < self.vertex_count:
            if len(self.adj_list[start]) != 0 and len(self.adj_list[end]) != 0:
                vertex1 = [edges[0] for edges in self.adj_list[start] if edges[0] == end]
                vertex2 = [edges[0] for edges in self.adj_list[end] if edges[0] == start]
                print(f"{start} has an edge with vertex {vertex1}")
                print(f"{end} has an edge with vertex {vertex2}")
                return True  
            return False 
        else:
            print("Invalid Vertices")

    def print_adj_list(self):
        """To print the Adjacency list representation of Graph"""
        print(self.adj_list)


g = Graph(5)
g.add_edge(0, 1, 10)
g.add_edge(1, 2, 20)
g.add_edge(2, 3, 30)
g.add_edge(3, 4, 40)
g.add_edge(3, 0, 50)
g.remove_edge(3, 0)
g.has_edge(1, 2)
g.print_adj_list()