""" 
Updated: 2017
Author: Sergei Shliakhtin
Contact: xxx.serj@gmail.com
Notes: 

"""


import numpy as np
import unittest

from graph_algos import INF
from graph_algos.distance_matrix_generate import triple_dist_oneb, triple_dist_zerob, half_mx_dist


class TestGenerate(unittest.TestCase):
    
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

    def test_triple_oneb_double(self):
        mx1 = np.array([(1, 2), (2, 3)])        
        mx1 = triple_dist_oneb(triples=mx1, num_vx=3)
        check = np.array([
            [INF, 1, INF],
            [1, INF, 1],
            [INF, 1, INF],
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

suite = unittest.TestLoader().loadTestsFromTestCase(TestGenerate)
unittest.TextTestRunner(verbosity=2).run(suite)

