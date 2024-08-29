class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    def add_edge(self, v1, v2):
        vertices = self.adj_list.keys()
        if v1 in vertices and v2 in vertices:
            self.adj_list[v1].append[v2]
            self.adj_list[v2].append[v1]
            return True
        return False

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])