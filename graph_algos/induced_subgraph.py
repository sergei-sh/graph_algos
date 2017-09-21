""" 
Updated: 2017
Author: Sergei Shliakhtin
Contact: xxx.serj@gmail.com
Notes: 

"""

import numpy as np

def induced_subgraph(dist_mx, *, vertices):
    """Extract an induced subgraph of dist_mx by vertices

    dist_mx - numpy distance matrix
    vertices - array of vertices, zero-based
    return (ind_dist_mx, tgt_src_converter) - numpy distance matrix, function converting 
        a target dist mx vertex index to source vertex index
    """
    def tgt_src_converter(tgt_vertex):
        assert np.isscalar(tgt_vertex)
        return vertices[tgt_vertex]
    
    return \
      dist_mx[np.ix_(vertices, vertices)], \
      tgt_src_converter




