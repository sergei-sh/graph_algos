""" 
Updated: 2017
Author: Sergei Shliakhtin
Contact: xxx.serj@gmail.com
Notes: 

"""

import numpy as np
import unittest

from graph_algos import INF, GraphAlgoException
from graph_algos.eulerian_circuit_fleurys import eulerian_circuit, bfs_count
from graph_algos.distance_matrix_generate import triple_dist_zerob


class TestFleurys(unittest.TestCase):
    
    def test_fleurys(self):
        graph = [(0, 1, 11), (1, 2, 12), (2, 3, 13), (3, 0, 14)]
        dist_mx = triple_dist_zerob(graph, 4)
        eul = eulerian_circuit(dist_mx)
        self.assertEquals(np.ma.allequal(eul, np.array([0, 1, 2, 3, 0])), True)

        graph = [(0, 2), (0, 3), (1, 2), (1, 3), (2, 3), (2, 4), (4, 5), (5, 3)]
        dist_mx = triple_dist_zerob(graph, 6)
        eul = eulerian_circuit(dist_mx)
        self.assertEquals(np.ma.allequal(eul, np.array([0, 2, 1, 3, 2, 4, 5, 3, 0])), True)


    def test_bfs_count(self):
        # connected graph with cycles
        graph = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 5), (3, 5), (3, 4), (5, 6), (5, 7)]
        dist_mx = triple_dist_zerob(graph, 8)

        count, path = bfs_count(dist_mx, start=0, return_path=True)
        
        self.assertEquals(count, 8)
        self.assertEquals(np.ma.allequal(path, np.array([0, 1, 2, 3, 5, 4, 6, 7])), True)

    def test_bfs_count_disconnected(self):
        # disconnected graph 
        graph = [(0, 1), (1, 3), (3, 2), (2,1),
            (4, 5)]
        dist_mx = triple_dist_zerob(graph, 6)

        count, path = bfs_count(dist_mx, start=0, return_path=True)
        self.assertEquals(count, 4)
        self.assertEquals(np.ma.allequal(path, np.array([0, 1, 2, 3])), True)

        count, path = bfs_count(dist_mx, start=4, return_path=True)
        self.assertEquals(count, 2)
        self.assertEquals(np.ma.allequal(path, np.array([4, 5])), True)



    def setUp(self):
        pass

    def tearDown(self):
        pass

suite = unittest.TestLoader().loadTestsFromTestCase(TestFleurys)
unittest.TextTestRunner(verbosity=2).run(suite)

