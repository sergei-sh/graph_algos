""" 
Updated: 2017
Author: Sergei Shliakhtin
Contact: xxx.serj@gmail.com
Notes: 

"""
import numpy as np

from graph_algos import INF

def tree_2coloring(dist_mx):
    """ Create a proper vertex 2-coloring of a tree.

    dist_mx - distance matrix of the tree
    return - a tuple consisting of 2 tuples with vertices. Each vertex is N in dist_mx
    """

    class coloured_storage():
        def __init__(self):
            self.red = []
            self.black = []
            self._current = False

        def next_colour(self):
            self._current = not self._current
            if self._current:
                return self.red
            else:
                return self.black

    cols = coloured_storage()
    current = {0}
    visited = set()
    while current:
#check for duplicates which mean there is a cycle
#        assert len(cols.red) + len(current)  == len(set(colors.red + current))
#        assert len(cols.black) + len(current)  == len(set(colors.black + current))

        col = cols.next_colour()
#colour current nodes
        col.extend(list(current))

        assert len(col) == len(set(col))

        current_new = set()
        for vertex in current:
            #find "parent" and "child" nodes
            current_new |= neighbours(dist_mx, vertex=vertex)

#check for cycles; not all cycles will be found, though
        assert not current_new & current, "A cycle is found"

#remove "parent" nodes, only "child" are left
        current_new -= visited
        visited |= current
        current = current_new

    
    return (tuple(cols.red), tuple(cols.black))        

def neighbours(dist_mx, *, vertex):
    """Get neighbouring nodes, given distance matrix of a graph

    dist_mx - distance matrix
    vertex - vertex N, whos neighbours
    return - neighbours set
    """    
    return set(np.nonzero(dist_mx[vertex] != INF)[0])
            






