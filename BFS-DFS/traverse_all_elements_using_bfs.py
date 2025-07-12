class Graph:
    def __init__(self, vertex_count):
        self.vertex_count = vertex_count
        self.adj_list = {vertex:[] for vertex in range(vertex_count) } 

    def add_edge(self, start, end):
        if 0 <= start < self.vertex_count and 0 <= end < self.vertex_count:
            self.adj_list[start].append(end)
            self.adj_list[end].append(start)
        
class Queue:
    def __init__(self):
        self.queue = []
    
    def insert_into_queue(self, data):
        self.queue.append(data)

    def pop_from_queue(self):
        if len(self.queue) > 0:
           self.queue.pop(0)

    def get_front(self):
        if len(self.queue) > 0:
            return self.queue[0]
        

class BFS:
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
    
    def traverse_using_bfs(self):
        self.vertices_using_bfs = []
        q = Queue()
        q.insert_into_queue(0)
        self.vertices_status[0] = True
        while len(q.queue) > 0:
            vertex = q.get_front()
            q.pop_from_queue()
            self.vertices_using_bfs.append(vertex)
            for v in self.g.adj_list[vertex]:
                if not self.vertices_status[v]:
                    q.insert_into_queue(v)
                    self.vertices_status[v] = True
        return self.vertices_using_bfs

bfs = BFS()
print("List of Traversed Vertices ::", bfs.traverse_using_bfs())