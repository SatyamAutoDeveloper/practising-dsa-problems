class Graph:
    def __init__(self, vertex_count):
        self.vertex_count = vertex_count
        self.adj_list = {vertex:[] for vertex in range(vertex_count) } 

    def add_edge(self, start, end):
        if 0 <= start < self.vertex_count and 0 <= end < self.vertex_count:
            self.adj_list[start].append(end)
            self.adj_list[end].append(start)
        
class Stack:
    def __init__(self):
        self.stack = []
    
    def insert_into_stack(self, data):
        self.stack.append(data)

    def pop_from_stack(self):
        if len(self.stack) > 0:
           self.stack.pop()

    def get_top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        

class DFS:
    def __init__(self):
        self.g = Graph(6)
        self.g.add_edge(0, 1)
        self.g.add_edge(0, 2)
        self.g.add_edge(1, 3)
        self.g.add_edge(2, 4)
        self.g.add_edge(3, 5)
        self.g.add_edge(4, 5)
        print(self.g.adj_list)
        self.vertices_status = [False for _ in range(self.g.vertex_count)]
    
    def traverse_using_dfs(self):
        self.vertices_using_dfs = []
        s = Stack()
        s.insert_into_stack(0)
        self.vertices_status[0] = True
        while len(s.stack) > 0:
            vertex = s.get_top()
            s.pop_from_stack()
            self.vertices_using_dfs.append(vertex)
            for v in self.g.adj_list[vertex]:
                if not self.vertices_status[v]:
                    s.insert_into_stack(v)
                    self.vertices_status[v] = True
        return self.vertices_using_dfs

dfs = DFS()
print("List of Traversed Vertices ::", dfs.traverse_using_dfs())