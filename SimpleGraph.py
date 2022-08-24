class Vertex:

    def __init__(self, val):
        self.Value = val


class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size

    def AddVertex(self, v):
        new_vertex = Vertex(v)
        new_index = 0
        while new_index < self.max_vertex:
            if not self.vertex[new_index]:
                break
            new_index += 1
        self.vertex[new_index] = new_vertex
        j = 0
        while j <= new_index:
            self.m_adjacency[j][new_index] = 0
            self.m_adjacency[new_index][j] = 0
            j += 1

    def RemoveVertex(self, v):
        i = v
        while i < self.max_vertex - 1:
            self.vertex[i] = self.vertex[i + 1]
            i += 1
        self.vertex[self.max_vertex - 1] = None
        x = 0

        while x < self.max_vertex - 1:
            y = v + 1
            while y < self.max_vertex - 1:
                self.m_adjacency[y][x] = self.m_adjacency[y + 1][x]
                y += 1
            x += 1

        y = 0
        while y < self.max_vertex - 1:
            x = v + 1
            while x < self.max_vertex - 1:
                self.m_adjacency[y][x] = self.m_adjacency[y][x + 1]
                x += 1
            y += 1

    def IsEdge(self, v1, v2):
        return True if self.m_adjacency[v1][v2] == 1 else False


    def AddEdge(self, v1, v2):
        self.m_adjacency[v1][v2] = 1
        self.m_adjacency[v2][v1] = 1

    def RemoveEdge(self, v1, v2):
        self.m_adjacency[v1][v2] = 0
        self.m_adjacency[v2][v1] = 0

    def EvenTrees(self):
        edges_to_break = []
        matrix = [row[:] for row in self.m_adjacency]

        y = 0
        while y < self.max_vertex:
            x = y + 1
            while x < self.max_vertex:
                if matrix[y][x] == 0:
                    x += 1
                    continue
                matrix[y][x] = 0
                matrix[x][y] = 0
                supposed_tree = [y]
                self.create_subtree_recursive(x, supposed_tree, matrix)
                if len(supposed_tree) % 2 == 0:
                    edges_to_break.append(y)
                    edges_to_break.append(x)
                else:
                    matrix[y][x] = 1
                    matrix[x][y] = 1
                x += 1
            y += 1
        values = []
        i = 0
        while i < len(edges_to_break):
            index_of_vertex = edges_to_break[i]
            value_of_vertex = self.vertex[index_of_vertex].Value
            values.append(value_of_vertex)
            i += 1
        return values

    def create_subtree_recursive(self, vertex_index, tree, matrix):
        child_index = vertex_index + 1
        while child_index < self.max_vertex:
            e = matrix[vertex_index][child_index]
            if e == 1:
                tree.append(child_index)
                self.create_subtree_recursive(child_index, tree, matrix)
            child_index += 1





