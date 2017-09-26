""" 
Updated: 2017
Author: Sergei Shliakhtin
Contact: xxx.serj@gmail.com
Notes: 

"""


import numpy as np
import unittest

from graph_algos import INF, GraphAlgoException 
from graph_algos.distance_matrix import triple_dist_zerob, half_mx_dist, verify_dist_mx
from graph_algos.color_tree import tree_2coloring

class TestColor(unittest.TestCase):

    def setUp(self):
        pass

    def test_color(self):        
        mx1 = triple_dist_zerob(((0, 1, 0), (1, 2, 0), (1, 3, 0), (2, 4, 0), (2, 5, 0)), 6)
        check = tree_2coloring(mx1)

        self.assertEqual(check, ((0, 2, 3), (1, 4, 5)))

        mx1 = triple_dist_zerob(((0, 1, 0), (1, 7, 0), (7, 13, 0), (0, 4, 0), (4, 6, 0), (4, 5, 0), (0, 3, 0),
            (0, 2, 0), (2, 8, 0), (2, 9, 0), (2, 10, 0), (10, 11, 0), (10, 12, 0)),
            14)
        check = tree_2coloring(mx1)

        self.assertEqual(check, ((0, 5, 6, 7, 8, 9, 10), (1, 2, 3, 4, 11, 12, 13)))

    def tearDown(self):
        pass

suite = unittest.TestLoader().loadTestsFromTestCase(TestColor)
unittest.TextTestRunner(verbosity=2).run(suite)

