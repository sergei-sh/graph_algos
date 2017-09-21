""" 
Updated: 2017
Author: Sergei Shliakhtin
Contact: xxx.serj@gmail.com
Parser: Python 3
Complexity: O(V^2) because of mask matrix multiplication
    Worth rewriting to be O(V * log(V)) (or == O(E * log(V))) otherwise
Notes: 

Prims Minimum Spanning Tree algorithm implementation 
http://www.geeksforgeeks.org/greedy-algorithms-set-5-prims-mst-for-adjacency-list-representation/
"""

import numpy as np
from heapq import heapify, heappush, heappop
from collections import namedtuple

from graph_algos import INF
from graph_algos.distance_matrix import verify_dist_mx

def prims_mst(dist_mx):
    """
    Prims MST. Uses distance matrix as input and heap for minimum vertex.

    dist_mx - numpy distance matrix. Diagonal elements and non-existent vertices should be INF.
    return - resulting tree as distance matrix
    """
    verify_dist_mx(dist_mx)

    MAX_V = range(dist_mx.shape[0]) 
    """ (comparison key,
        vertex not yet in MST,
        vertex the edge to which gives the comparison key)
    """
    class OutVert:
        def __init__(self, key, vx, vx_from):
            self.key = key
            self.vx = vx
            self.vx_from = vx_from

        def __lt__(self, rhv):
            return self.key < rhv.key

    out_of_mst = [OutVert(INF, v, INF) for v in MAX_V]
    """Make 0-th element root"""
    out_of_mst[0].key = 0
    heapify(out_of_mst)  # O(V*log(V))
    #resuting tree. the mask for edges remained from original graph.  
    # INF will discard dist_mx value in matrix element-wise product
    in_mst_mask = np.full(dist_mx.shape, INF)

    root = True
    while out_of_mst: # O(V)
        #take minimal, move to resulting tree
        cur_vx = heappop(out_of_mst) # O(1)
        vx = cur_vx.vx

        #root should be the first
        if not root:
            vx_from = cur_vx.vx_from
            # 1 will retain dist_mx value in matrix element-wise product
            in_mst_mask[vx][vx_from] = 1
            in_mst_mask[vx_from][vx] = 1

        root = False

        #modify neighbours
        for key_vx in out_of_mst: # O(V)
            weight = dist_mx[vx][key_vx.vx]
            if key_vx.key > weight:
                key_vx.key = weight 
                key_vx.vx_from = vx

        heapify(out_of_mst) # sifting a "looser" down O(log(V))

    return np.multiply(in_mst_mask, dist_mx) # O(V^2)



