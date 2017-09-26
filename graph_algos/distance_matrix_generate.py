""" 
Updated: 2017
Author: Sergei Shliakhtin
Contact: xxx.serj@gmail.com
Parser: Python3
Notes:

Routines for distance (adjacency) matrices generation from other graph representations.
"""

import numpy as np

from graph_algos import INF, GraphAlgoException
from graph_algos.distance_matrix import unpack_edge

def generate_geometric_dist_mx(size):
    """ Create a distance matrix with distances in metric space

    size - vertices number
    return - numpy distance matrix
    """
    if size < 2:
        raise GraphAlgoException("Will generate at least 2 vertices")

    DIMENSIONS = 2
    xy = np.random.rand(size, DIMENSIONS)
    # .shape = (size, size, DIMENSIONS)
    distances = xy[:, None, :] - xy[None, :, :]
    dist_sqr = distances ** 2
    # (size, size)
    dist_sum = np.sum(dist_sqr, axis=-1)
    dist_mx = np.sqrt(dist_sum)
    np.place(dist_mx, dist_mx == 0, INF)
    return dist_mx

def triple_dist_zerob(triples, num_vx):                    
    """ Create a graph given edges and total vertex number.
    Take (from, to, weight) tuples and form distance matrix.
    from, to - vertex indices, zero-based
    
    triples - sequence of 3-tuples
    num_vx - int vertex count
    return - distance matrix, row N (zero-based) represents vertex N edges
    """
    dist_mx = np.full((num_vx, num_vx), INF)
    for edge in triples:
        from_v, to_v, weight = unpack_edge(edge)

        dist_mx[from_v][to_v] = weight
        dist_mx[to_v][from_v] = weight

    return dist_mx


def triple_dist_oneb(triples, num_vx):                    
    """Create a graph given edges and total vertex number.
    Take (from, to, weight) tuples and form distance matrix
    from, to - vertex indices, one-based
    
    triples - sequence of 3-tuples
    num_vx - int vertex count
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
    return - numpy distance matrix, row N represents vertex N edges
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
    
