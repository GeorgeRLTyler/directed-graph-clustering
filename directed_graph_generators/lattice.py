import numpy as np
from typing import Union

from directed_graph_generators.base_graph import BaseGraph
from helpers.edge_list_matrix_converter import Converter

class DirectedLattice(BaseGraph):
    def __init__(self, width: Union[int,None] = None, length: Union[int,None] = None, directions: Union[str,None] = None):
        """class generates a lattice of width and length with directed edges. The directions will flow 'left and down' unless
        directions is set to random in which case they are chosen at random."""
        super().__init__()
        self._directions = directions 
        self._width = width
        if self._width == None:
            self._width = 10
        self._length = length
        if self._length == None:
            self._length = 10
        self._vertices = list(range(self._width*self._length))
        self._edges = self._generate_edge_list()#
        self.adjacency_matrix = Converter.convert_from_edge_list_to_adjacency_matrix(N = len(self._vertices),edge_list=self._edges)
    
    def _generate_edge_list(self):
        self._edges = []
        if self._directions == None:
            for l in range(self._length -1):
                for w in range(self._width -1):
                    vertex_number = l*self._width + w
                    self._edges.append((vertex_number,vertex_number+1))
                    self._edges.append((vertex_number,vertex_number+self._width))
        return self._edges
