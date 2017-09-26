""" 
Updated: 2017
Author: Sergei Shliakhtin
Contact: xxx.serj@gmail.com
Parser: Python3
Notes:

Implementation of Fleurys algorithm to find an Eulerian path
http://www.geeksforgeeks.org/fleurys-algorithm-for-printing-eulerian-path/
"""

from collections import deque
import numpy as np

from graph_algos import odd_vertices, GraphAlgoException, INF
from graph_algos.distance_matrix import neighbours, add_edge, remove_edge

def eulerian_circuit(dist_mx): 
    """ Find an eulerian tour. Raise exception if none. Return path starting from 0 vertex.

    dist_mx - numpy distance matrix
    return - numpy array, eulerian path, starting and ending at 0
    """

    # need removing edges, so working with a copy 
    dist_mx = dist_mx.copy()

    print(dist_mx)
    if odd_vertices(dist_mx).size:
        raise GraphAlgoException("The graph is not Eulerian")

    def is_bridge(edge):
        reachable_with = bfs_count(dist_mx, start=edge[0])

        remove_edge(dist_mx, edge=edge)
        reachable_wo = bfs_count(dist_mx, start=edge[0])
        add_edge(dist_mx, edge=edge)

        assert not reachable_wo > reachable_with
        return reachable_with > reachable_wo

    def can_remove(edge):
        if 1 == len(neighbours(dist_mx, vertex=edge[0])):
            return True

        return not is_bridge(edge)

    vertex = 0            
    circuit = [0]
    while True:
        neigh = neighbours(dist_mx, vertex=vertex)
        if not neigh:
            break
        # print("vert", vertex)
        # print("N", neigh)
        for to in neigh:
            edge = (vertex, to)
            # print("edge:", edge)
            if can_remove(edge): 
                # print("e", edge, 1)
                circuit.append(to)
                remove_edge(dist_mx, edge=edge)
                vertex = to
                break
            # print("e", edge, 0)
        else:
            assert False, "Too many bridges"

    # all edges should have been removed so far
    assert np.ma.allequal(dist_mx, INF)        

    return circuit        


def bfs_count(dist_mx, *, start, return_path=False):
    """ Perform BFS traversal, starting from vertex, count acessible vertices

    dist_mx - numpmy distance matrix
    start - vertex to start from
    return_path - if true, return the traversal path
    return (int, array) - int, acessible vertices count
    """

    count = 0
    to_visit = deque([start])
    # N-th element indicates whether vertex N visited
    visited = [False] * dist_mx.shape[0]
    visited[start] = True

    if return_path:
        path = []

    while to_visit:
        vertex = to_visit.popleft()
        # mark visited
        count += 1
        
        # this is needed for DEBUG only
        if return_path:
            path.append(vertex)

        # assign children to be processed at the end of the queue
        for neighb in neighbours(dist_mx, vertex=vertex):
            if not visited[neighb]:
                # "roots" neighbours are pushed first. so, the level closest to the "root" will
                #  be popped earlier than the next layer (however, both layers co-exist in to_visit at some moment)
                visited[neighb] = True
                to_visit.append(neighb)

    if return_path:
        return (count, np.array(path))                
    else:
        return count
        


