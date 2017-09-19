""" 
Updated: 2017
Author: Sergei Shliakhtin
Contact: xxx.serj@gmail.com
Notes: 

"""


import numpy as np
import unittest

from graph_algos import INF, GraphAlgoException 
from graph_algos.distance_matrix import triple_dist_oneb, half_mx_dist, verify_dist_mx
from graph_algos.prims_mst import prims_mst

class TestPrimMst(unittest.TestCase):

    def test_prim_mst(self):
        mx1 = np.array([ 
                [INF, 10, 15, 20], 
                [10, INF, 35, 25], 
                [15, 35, INF, 30], 
                [20, 25, 30, INF],
                ])

        mx1 = prims_mst(mx1)

        check = triple_dist_oneb(((1, 2, 10), (1, 4, 20), (1, 3, 15)), 4) 

        self.assertTrue(np.ma.allequal(check, mx1))

        mx2 = np.array([
            [7, INF, 4, 9, INF],
            [13, 5, 11, 8],
            [INF, 15, 6],
            [8, INF],
            [10]
            ])

        mx2 = half_mx_dist(mx2)
        verify_dist_mx(mx2)

        result = prims_mst(mx2)

        check = triple_dist_oneb(((1, 4, 4), (4, 5, 8), (2, 4, 5), (6, 2, 8), (6, 3, 6)), 6)

        self.assertTrue(np.ma.allequal(check, result))

    def setUp(self):
        pass

    def tearDown(self):
        pass

suite = unittest.TestLoader().loadTestsFromTestCase(TestPrimMst)
unittest.TextTestRunner(verbosity=2).run(suite)

