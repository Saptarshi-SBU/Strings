#!/usr/bin/python

import unittest
from graph import Graph, Vertex, Edge

class graphTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_case_001(self):
        g = Graph()
        for i in range(10):
            g.add_vertex(Vertex(i))

        for i in range(1, 10):
            g.add_edge(Edge(g.vertex(i - 1), g.vertex(i)))
           
        g.print_graph()
        x = g.is_eulirean()
        print 'Graph eulirean  :{}'.format(x)
        if x:
            circuit = g.euler_path()
            path = ''
            for x in circuit:
                path = '{} {}'.format(path, x)
            print 'euler path : {}'.format(path)

    def test_case_002(self):
        g = Graph()
        cities = [ 'L.A', 'S.F', 'Chicago', 'N.Y', 'Phil', 'Washington' ]
        for i in cities:
            g.add_vertex(Vertex(cities.index(i)))
        
        g.add_edge(Edge(g.vertex(2), g.vertex(0)))
        g.add_edge(Edge(g.vertex(0), g.vertex(3)))
        g.add_edge(Edge(g.vertex(3), g.vertex(4)))
        g.add_edge(Edge(g.vertex(4), g.vertex(0)))
        g.add_edge(Edge(g.vertex(0), g.vertex(1)))
        g.add_edge(Edge(g.vertex(1), g.vertex(2)))

        g.print_graph()
        x = g.is_eulirean()
        print 'Graph eulirean  :{}'.format(x)
        if x:
            circuit = g.euler_path()
            path = ''
            for x in circuit:
                path = '{} {}'.format(path, x)
            print 'euler path : {}'.format(path)

    def test_case_003(self):
        g = Graph()

        g.add_vertex(Vertex(0))
        g.add_vertex(Vertex(1))
        g.add_vertex(Vertex(2))
        g.add_vertex(Vertex(3))
        g.add_vertex(Vertex(4))
        g.add_vertex(Vertex(5))

        g.add_edge(Edge(g.vertex(0), g.vertex(1)))
        g.add_edge(Edge(g.vertex(1), g.vertex(2)))
        g.add_edge(Edge(g.vertex(2), g.vertex(0)))
        g.add_edge(Edge(g.vertex(0), g.vertex(3)))
        g.add_edge(Edge(g.vertex(3), g.vertex(4)))
        g.add_edge(Edge(g.vertex(4), g.vertex(5)))
        g.add_edge(Edge(g.vertex(5), g.vertex(3)))

        g.print_graph()
        #g.reverse_graph()
        #g.print_reverse_graph();
        x = g.is_eulirean()
        print 'Graph eulirean  :{}'.format(x)
        if x:
            circuit = g.euler_path()
            path = ''
            for x in circuit:
                path = '{} {}'.format(path, x)
            print 'euler path : {}'.format(path)

    def tearDown(self):
        pass

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    suite = unittest.TestSuite()
    suite.addTest(graphTestCase('test_case_001'))
    suite.addTest(graphTestCase('test_case_002'))
    suite.addTest(graphTestCase('test_case_003'))
    runner.run(suite)
