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
