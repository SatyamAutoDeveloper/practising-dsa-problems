class Graph:
    def __init__(self, vertno):
        self.vertex_count = vertno
        self.adj_matrix = [[0]*vertno for _ in range(vertno)]
        

    def add_edge(self, verti, hori, weight=0):
        """To add an edge b/w two vertices"""
        if 0 <= verti < self.vertex_count and 0 <= hori < self.vertex_count :
            self.adj_matrix[verti][hori] = weight
            self.adj_matrix[hori][verti] = weight
        else:
            print("Invalid vertices")

    def remove_edge(self, verti, hori):
        """To remove an edge b/w two vertices"""
        if 0 <= verti < self.vertex_count and 0 <= hori < self.vertex_count :
            self.adj_matrix[verti][hori] = 0
            self.adj_matrix[hori][verti] = 0
        else:
            print("Invalid vertices")

    def has_edge(self, verti, hori):
        """To check an edge b/w two vertices"""
        if 0 <= verti < self.vertex_count and 0 <= hori < self.vertex_count :
            if self.adj_matrix[verti][hori] != 0:
                print("Yes, there is an edge b/w vertices ::", self.adj_matrix[verti][hori])
                return True
            return False
        else:
            print("Invalid vertices")

    def print_adj_matrix(self):
        """To print the graph using adjacency matrix representation"""
        for verti in range(0, self.vertex_count):
            row = []
            for hori in range(0, self.vertex_count):
                row.append(self.adj_matrix[verti][hori])
            print(row)
        

g = Graph(5)
g.add_edge(0, 1, 10)
g.add_edge(1, 2, 11)
g.add_edge(2, 3, 12)
g.add_edge(3, 4, 30)
g.add_edge(0, 3, 20)
g.remove_edge(3, 4)
print("has edge ::", g.has_edge(0, 3))
print("has edge ::", g.has_edge(4, 2))
g.print_adj_matrix()
