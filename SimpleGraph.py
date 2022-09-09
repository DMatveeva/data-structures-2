class Vertex:

    def __init__(self, val):
        self.Value = val
        self.Hit = False


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.size() == 0:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)


class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if self.size() == 0:
            return None
        return self.stack.pop()

    def push(self, value):
        self.stack.append(value)

    def peek(self):
        if self.size() == 0:
            return None
        return self.stack[self.size() - 1]


class SimpleGraph:

    def __init__(self, size):
        self.max_vertex = size
        self.m_adjacency = [[0] * size for _ in range(size)]
        self.vertex = [None] * size

    def WeakVertices(self):
        strong_vertex_indices = set()
        i = 0
        while i < self.max_vertex:
            # get all neighbours of the vertex
            neighbours = []
            j = 0
            while j < self.max_vertex:
                if self.m_adjacency[i][j] == 1:
                    neighbours.append(j)
                j += 1
            # for every neighbour we check if its neighbours are the neighbours of the initial vertex
            # if so, the initial vertex is strong vertex
            for k in neighbours:
                for m in neighbours:
                    if self.m_adjacency[k][m] == 1:
                        strong_vertex_indices.add(i)
            i += 1

        all_vertex_indices = list(range(0, self.max_vertex))
        weak_vertex_indices = [node for node in all_vertex_indices if node not in strong_vertex_indices]
        weak_vertex = []
        for i in weak_vertex_indices:
            weak_vertex.append(self.vertex[i])
        return weak_vertex

    def DepthFirstSearch(self, VFrom, VTo):
        for v in self.vertex:
            v.Hit = False
        vertex_from = self.vertex[VFrom]
        vertex_from.Hit = True
        stack = Stack()
        stack.push(VFrom)
        self.depth_first_search_recursive(VFrom, VTo, stack)
        shortest_part = []
        for index in stack.stack:
            node = self.vertex[index]
            shortest_part.append(node)
        return shortest_part

    def depth_first_search_recursive(self, v_from, v_to, stack):
        i = 0
        while i < self.max_vertex:
            if self.m_adjacency[v_from][i] == 0:
                i += 1
                continue
            vertex = self.vertex[i]
            if vertex.Hit:
                i += 1
                continue
            vertex.Hit = True
            stack.push(i)
            if v_to == i:
                return stack
            return self.depth_first_search_recursive(i, v_to, stack)
        stack.pop()
        if stack.size() == 0:
            return stack
        else:
            next_index = stack.peek()
            next_vertex = self.vertex[next_index]
            next_vertex.Hit = True
            return self.depth_first_search_recursive(next_index, v_to, stack)

    def BreadthFirstSearch(self, VFrom, VTo):
        for v in self.vertex:
            v.Hit = False

        vertex_from = self.vertex[VFrom]
        vertex_from.Hit = True
        paths = {VFrom: [vertex_from]}
        queue = Queue()
        queue.enqueue(VFrom)

        while queue.size() > 0:
            vertex_index = queue.dequeue()
            i = 0
            while i < self.max_vertex:
                neighbour_vertex = self.vertex[i]
                if not neighbour_vertex:
                    i += 1
                    continue
                if neighbour_vertex.Hit:
                    i += 1
                    continue
                if self.m_adjacency[vertex_index][i] == 1:
                    new_path = paths[vertex_index].copy()
                    new_path.append(neighbour_vertex)
                    paths[i] = new_path
                    queue.enqueue(i)
                    neighbour_vertex.Hit = True
                if self.m_adjacency[vertex_index][i] == 1 and i == VTo:
                    return paths[i]
                i += 1
        return []

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






