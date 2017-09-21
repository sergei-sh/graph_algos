""" 
Updated: 2017
Author: Sergei Shliakhtin
Contact: xxx.serj@gmail.com
Notes: 

"""


import numpy as np
import unittest

from graph_algos import INF
from graph_algos.induced_subgraph import induced_subgraph

class TestColor(unittest.TestCase):

    def setUp(self):
        pass

    def test_induced1(self):
        mx1 = np.array([
            [INF, 1, 2, 3],
            [1, INF, 4, 5],
            [2, 4, INF, 6],
            [3, 5, 6, INF],
            ])

        result, dst_src_conv = induced_subgraph(mx1, vertices=np.array((0, 2)))
        check = np.array([
            [INF, 2],
            [2, INF],
            ]) 

        self.assertEqual(np.ma.allequal(result, check), True)
        self.assertEqual(dst_src_conv(0), 0)
        self.assertEqual(dst_src_conv(1), 2)

    def test_induced1(self):
        mx1 = np.array([
                [INF, 1, 2, 3],
                [1, INF, 4, 5],
                [2, 4, INF, 6],
                [3, 5, 6, INF],
                ])

        result, dst_src_conv = induced_subgraph(mx1, vertices=(1, 2, 3))
        check = np.array([
            [INF, 4, 5],
            [4, INF, 6],
            [5, 6, INF]
            ]) 

        self.assertEqual(np.ma.allequal(result, check), True)
        self.assertEqual(dst_src_conv(0), 1)
        self.assertEqual(dst_src_conv(1), 2)
        self.assertEqual(dst_src_conv(2), 3)


    def tearDown(self):
        pass

suite = unittest.TestLoader().loadTestsFromTestCase(TestColor)
unittest.TextTestRunner(verbosity=2).run(suite)

