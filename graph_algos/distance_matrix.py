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

def unpack_edge(edge):       
    """ For (from, to, weight) edge does nothing. For (from, to) adds weight 1. 
    Raises if length is not 2 or 3.

    return - (from, to, weight) tuple
    """
    if len(edge) < 2 or len(edge) > 3:
        raise GraphAlgosException("Malformed (vert, vert, weight) tuple")

    from_v, to_v = edge[:2]
    try:
        weight = edge[2] 
    except IndexError:
        weight = 1
        
    return (from_v, to_v, weight)


def add_edge(dist_mx, *, edge):
    """Add an edge to the graph in-place. Raise an exception if edge already exists

    edge - tuple (from, to) or (from, to, weight)
    """
    from_v, to_v, w = unpack_edge(edge)

    if dist_mx[from_v][to_v] != INF or dist_mx[to_v][from_v] != INF:
        raise GraphAlgoException("Edge already exists") 

    dist_mx[from_v][to_v] = w
    dist_mx[to_v][from_v] = w

def remove_edge(dist_mx, *, edge):
    """Removes an edge from the graph in-place. Raise an exception if doesn't exist

    edge - tuple (from, to) or (from, to, weight)
    """
    from_v, to_v, w = unpack_edge(edge)

    if dist_mx[from_v][to_v] == INF or dist_mx[to_v][from_v] == INF:
        raise GraphAlgoException("Edge doesn't exist") 

    dist_mx[from_v][to_v] = INF
    dist_mx[to_v][from_v] = INF 


def neighbours(dist_mx, *, vertex):
    """Get neighbouring nodes, given distance matrix of a graph

    dist_mx - distance matrix
    vertex - vertex N, whos neighbours
    return - neighbours set
    """    
    return set(np.nonzero(dist_mx[vertex] != INF)[0])

def odd_vertices(dist_mx):
    """Take odd degree vertices from a graph   

    dist_mx - distance matrix
    return - tuple of vertices
    """
    return np.where(
        [(np.sum(dist_mx[row] != INF) % 2 == 1) 
        for row in range(0, dist_mx.shape[0])]
        )[0] 


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


