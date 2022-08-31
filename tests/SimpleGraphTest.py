import unittest

from SimpleGraph import SimpleGraph


class MyTestCase(unittest.TestCase):

    def test_1(self):
        graph = SimpleGraph(3)
        graph.AddVertex(0)
        expected_vertex = '0,n,n,'
        self.assertEqual(expected_vertex, self.vertex_to_str(graph))  # add assertion here
        expected_m = '[0, 0, 0]\n' \
                     '[0, 0, 0]\n' \
                     '[0, 0, 0]\n'
        self.assertEqual(expected_m, self.m_adjacency_to_str(graph))  # add assertion here


    def test_2(self):
        graph = SimpleGraph(3)
        graph.AddVertex(0)
        expected_vertex = '0,n,n,'
        self.assertEqual(expected_vertex, self.vertex_to_str(graph))  # add assertion here
        expected_m = '[0, 0, 0]\n' \
                     '[0, 0, 0]\n' \
                     '[0, 0, 0]\n'
        self.assertEqual(expected_m, self.m_adjacency_to_str(graph))  # add assertion here

    def get_graph(selfs):
        graph = SimpleGraph(10)
        graph.AddVertex(1)
        graph.AddVertex(2)
        graph.AddVertex(3)
        graph.AddVertex(4)
        graph.AddVertex(5)
        graph.AddVertex(6)
        graph.AddVertex(7)
        graph.AddVertex(8)
        graph.AddVertex(9)
        graph.AddVertex(10)
        graph.AddEdge(0, 1)
        graph.AddEdge(0, 2)
        graph.AddEdge(0, 5)
        graph.AddEdge(1, 4)
        graph.AddEdge(1, 6)
        graph.AddEdge(2, 3)
        graph.AddEdge(5, 7)
        graph.AddEdge(7, 8)
        graph.AddEdge(7, 9)

        graph.AddEdge(6, 3)
        return graph

    def test_depth_search(self):
        graph = self.get_graph()
        v0 = graph.vertex[0]
        v1 = graph.vertex[1]
        actual = graph.DepthFirstSearch(0, 1)
        expected = [v0, v1]
        self.assertEqual(expected, actual)

    def test_depth_search_1(self):
        graph = self.get_graph()
        v0 = graph.vertex[0]
        v1 = graph.vertex[1]
        v2 = graph.vertex[2]
        v3 = graph.vertex[3]
        v4 = graph.vertex[4]
        v5 = graph.vertex[5]
        v6 = graph.vertex[6]
        v7 = graph.vertex[7]
        v8 = graph.vertex[8]
        v9 = graph.vertex[9]

        actual = graph.DepthFirstSearch(0, 9)
        expected = [v0, v5, v7, v9]
        self.assertEqual(expected, actual)

        actual = graph.DepthFirstSearch(0, 1)
        expected = [v0, v1]
        self.assertEqual(expected, actual)

        actual = graph.DepthFirstSearch(0, 4)
        expected = [v0, v1, v4]
        self.assertEqual(expected, actual)

        actual = graph.DepthFirstSearch(0, 6)
        expected = [v0, v1, v6]
        self.assertEqual(expected, actual)

        actual = graph.DepthFirstSearch(0, 2)
        expected = [v0, v1, v6, v3, v2]
        self.assertEqual(expected, actual)

        actual = graph.DepthFirstSearch(0, 3)
        expected = [v0, v1, v6, v3]
        self.assertEqual(expected, actual)

        actual = graph.DepthFirstSearch(0, 5)
        expected = [v0, v5]
        self.assertEqual(expected, actual)

        actual = graph.DepthFirstSearch(0, 7)
        expected = [v0, v5, v7]
        self.assertEqual(expected, actual)

        actual = graph.DepthFirstSearch(0, 8)
        expected = [v0, v5, v7, v8]
        self.assertEqual(expected, actual)

        actual = graph.DepthFirstSearch(0, 9)
        expected = [v0, v5, v7, v9]
        self.assertEqual(expected, actual)


    def vertex_to_str(self, graph):
        s = ''
        for v in graph.vertex:
            value = str(v.Value) if v else 'n'
            s += value + ','
        return s

    def m_adjacency_to_str(self, graph):
        s = ''
        for line in graph.m_adjacency:
            s += str(line) + '\n'
        return s




if __name__ == '__main__':
    unittest.main()
