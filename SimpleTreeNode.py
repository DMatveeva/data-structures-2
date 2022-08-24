def EvenTrees(self):
    indices_of_vertex = []
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
                indices_of_vertex.append(y)
                indices_of_vertex.append(x)
            else:
                matrix[y][x] = 1
                matrix[x][y] = 1
            x += 1
        y += 1
    vertex_to_break = []
    i = 0
    while i < len(indices_of_vertex):
        index_of_vertex = indices_of_vertex[i]
        vertex_to_break.append(self.vertex[index_of_vertex])
        i += 1
    return vertex_to_break


def create_subtree_recursive(self, vertex_index, tree, matrix):
    child_index = vertex_index + 1
    while child_index < self.max_vertex:
        e = matrix[vertex_index][child_index]
        if e == 1:
            tree.append(child_index)
            self.create_subtree_recursive(child_index, tree, matrix)
        child_index += 1