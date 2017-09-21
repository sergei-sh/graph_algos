""" 
Updated: 2017
Author: Sergei Shliakhtin
Contact: xxx.serj@gmail.com
Notes: 

"""


import networkx as nx 
import numpy as np
import unittest

from graph_algos import INF, GraphAlgoException
from graph_algos.distance_matrix import verify_dist_mx, triple_dist_oneb, triple_dist_zerob, half_mx_dist, path_length, graph_dist_mx


class TestAux(unittest.TestCase):

    def test_graph_dist_mx(self):
        g = nx.Graph()
        g.add_edge(0, 1, weight=3)
        g.add_edge(0, 2, weight=4)
        g.add_edge(2, 3, weight=5)

        dist_mx = graph_dist_mx(graph=g) 
        check = np.array([
            [INF, 3, 4, INF],
            [3, INF, INF, INF],
            [4, INF, INF, 5],
            [INF, INF, 5, INF],
            ])

        print(dist_mx)
        self.assertEqual(np.ma.allequal(dist_mx, check), True)

    def test_path_length(self):
        mx1 = np.array([ 
                [INF, 1, 4, INF], 
                [1, INF, 3, 6], 
                [4, 3, INF, 7], 
                [INF, 6, 7, INF], ])

        verify_dist_mx(mx1); 

        # 0 - 1 - 2 - 3
        self.assertEqual(path_length(mx1, path=iter(range(4))), 11)

        self.assertRaises(GraphAlgoException, path_length, mx1, path=iter([]))
        self.assertRaises(GraphAlgoException, path_length, mx1, path=iter([0, 1, 3, 0]))

    def test_verify_dist_mx(self):
        mx1 = np.array([ [INF, 1, 2], 
                [1, INF, 3], 
                [2, 3, INF], ])

        verify_dist_mx(mx1); 

        mx1[0][2] = 0
        self.assertRaises(GraphAlgoException, verify_dist_mx, mx1)

    def test_triple_zerob(self):
        mx1 = np.array([(0, 1, 7), (1, 2, 8)])        
        mx1 = triple_dist_zerob(triples=mx1, num_vx=3)
        check = np.array([
            [INF, 7, INF],
            [7, INF, 8],
            [INF, 8, INF],
            ])

        self.assertEqual(np.ma.allequal(mx1, check), True)


    def test_triple_oneb(self):
        mx1 = np.array([(1, 2, 10), (1, 4, 20), (1, 3, 15)])        
        mx1 = triple_dist_oneb(triples=mx1, num_vx=4)
        check = np.array([[INF, 10, 15, 20],
            [10, INF, INF, INF],
            [15, INF, INF, INF],
            [20, INF, INF, INF],
            ])
        
        self.assertEqual(np.ma.allequal(mx1, check), True)

    def test_half_mx_dist(self):
        half_mx = np.array([
            [0, 1, 2],
            [3, 4],
            [5],
            ])
        mx1 = half_mx_dist(half_mx)

        check = np.array([
            [INF, 0, 1, 2],
            [0, INF, 3, 4],
            [1, 3, INF, 5],
            [2, 4, 5, INF],
            ] )

        self.assertTrue(np.ma.allequal(mx1, check))

    def setUp(self):
        pass

    def tearDown(self):
        pass

suite = unittest.TestLoader().loadTestsFromTestCase(TestAux)
unittest.TextTestRunner(verbosity=2).run(suite)

