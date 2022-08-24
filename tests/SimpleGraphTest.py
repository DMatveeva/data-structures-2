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
        graph.RemoveVertex(0)
        expected_vertex = '0,n,n,'
        self.assertEqual(expected_vertex, self.vertex_to_str(graph))  # add assertion here
        expected_m = '[0, 0, 0]\n' \
                     '[0, 0, 0]\n' \
                     '[0, 0, 0]\n'
        self.assertEqual(expected_m, self.m_adjacency_to_str(graph))  # add assertion here

    def test_even_tree(self):
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

        actual = graph.EvenTrees()
        expected = [1, 3, 1, 6]
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
