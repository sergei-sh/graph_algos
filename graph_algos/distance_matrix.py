""" 
Updated: 2017
Author: Sergei Shliakhtin
Contact: xxx.serj@gmail.com
Parser: Python3
Notes:

Auxiliary routines on distance (adjacency) matrices
"""

import numpy as np

from graph_algos import INF, GraphAlgoException

"TODO: rewrite"
def graph_dist_mx(*, graph):
    """Convert NetworkX graph into distance matrix
    
    graph - networkx.Graph
    return - numpy distance matrix
    """
    size = len(graph.nodes())
    dist_mx = np.full((size, size), INF)
    for i in range(0, size):
        for j in range(0, size):
            if i != j:
                try:
                    dist_mx[i][j] = graph[i][j]["weight"] 
                except KeyError:
                    pass
    return dist_mx                

def path_length(dist_mx, *, path):
    """Count the cost (sum of weights) of a given path

    dist_mx - numpy distance matrix
    path - iterable with vertices
    """
    path = iter(path)
    length = 0

    try:
        vert = next(path)
    except StopIteration:
        raise GraphAlgoException("The path is empty")

    for vert_next in path:
        edge_len = dist_mx[vert][vert_next]
        if INF == edge_len:
            raise GraphAlgoException("No edge between these vertices {} {}".format(vert, vert_next))
        length += edge_len

        vert = vert_next

    return length        


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
    
    triples - sequence of 3-tuples
    num_vx - int vertex count
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
    
