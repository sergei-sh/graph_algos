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
from graph_algos.distance_matrix import verify_dist_mx, path_length, odd_vertices, neighbours, \
    add_edge, remove_edge


class TestDistmx(unittest.TestCase):

    def test_add_remove_edge(self):
        mx1 = np.array([
            [INF, 7, INF],
            [7, INF, 8],
            [INF, 8, INF],
            ])

        add_edge(mx1, edge=(0, 2, 5))
        check = np.array([
            [INF, 7, 5],
            [7, INF, 8],
            [5, 8, INF],
            ])
 
        self.assertEquals(np.ma.allequal(mx1, check), True)

        remove_edge(mx1, edge=(1, 2))
        check = np.array([
            [INF, 7, 5],
            [7, INF, INF],
            [5, INF, INF],
            ])
 
        self.assertEquals(np.ma.allequal(mx1, check), True)

    def test_neighbours(self):
        self.mx1 = np.array([ 
            [INF, 10, 15, 20], 
            [10, INF, 35, 25], 
            [15, 35, INF, 30], 
            [20, 25, 30, INF],
            ])

        neigh = neighbours(self.mx1, vertex=1)
        self.assertEqual(neigh, set([0, 2, 3]))


    def test_odd_vertices(self):
        mx1 = np.array([ 
                [INF, 1, 4, INF], 
                [1, INF, 3, 6], 
                [4, 3, INF, 7], 
                [INF, 6, 7, INF], ])

        odd_v = odd_vertices(mx1)
        self.assertEquals(np.ma.allequal(odd_v, np.array([1, 2])), True)


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

    def setUp(self):
        pass

    def tearDown(self):
        pass

suite = unittest.TestLoader().loadTestsFromTestCase(TestDistmx)
unittest.TextTestRunner(verbosity=2).run(suite)

