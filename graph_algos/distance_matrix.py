""" 
Updated: 2017
Author: Sergei Shliakhtin
Contact: xxx.serj@gmail.com
Notes:

Auxiliary routines for graph algos 
"""

from graph_algos import INF, GraphAlgoException

import numpy as np

def verify_dist_mx(dist_mx):
    """Checks distance matrix is symmetric and has INF in the diagonal, assert if not OK
    
    dist_mx - numpy distance matrix, row N represents vertex N edges
    """

    if not dist_mx.shape[0] == dist_mx.shape[1]:
        raise GraphAlgoException
    for i in range(0, dist_mx.shape[0]):
        for j in range(0, dist_mx.shape[1]):
            if i == j:
                if not INF == dist_mx[i][j]:
                    raise GraphAlgoException
            else:
                if not dist_mx[i][j] == dist_mx[j][i]:
                    raise GraphAlgoException

def triple_dist_zerob(triples, num_vx):                    
    """ Create a graph given edges and total vertex number.
    Take (from, to, weight) tuples and form distance matrix.
    from, to - vertex indices, zero-based
    
    triples - seq of triples
    return - distance matrix, row N (zero-based) represents vertex N edges
    """
    dist_mx = np.full((num_vx, num_vx), INF)
    for from_v, to_v, weight in triples:
        dist_mx[from_v][to_v] = weight
        dist_mx[to_v][from_v] = weight

    return dist_mx


def triple_dist_oneb(triples, num_vx):                    
    """Create a graph given edges and total vertex number.
    Take (from, to, weight) tuples and form distance matrix
    from, to - vertex indices, one-based
    
    triples - seq of triples
    return - distance matrix, row N (zero-based) represents vertex N edges
    """

#make copy
    triples = np.array(triples)
    triples[:,:2] -= 1
    return triple_dist_zerob(triples, num_vx)

def half_mx_dist(half_mx):
    """Given the diagonal half of distance matrix, mirror it to get the complete distance
    matrix

    half_mx - right upper diagonal cut of distance matrix
    return - distance matrix, row N represents vertex N edges
    """    
    w = len(half_mx[0]) + 1
    dist_mx = np.full((w, w), INF)
    for y in range(0, w):
        for x in range(0, w):
            if x > y:
                dist_mx[y][x] = half_mx[y][x - 1 - y]
            elif x < y:
                dist_mx[y][x] = half_mx[x][y - 1 - x]
    return dist_mx 
    
