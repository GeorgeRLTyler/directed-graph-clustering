import numpy as np
from typing import Union

from directed_graph_generators.base_graph import BaseGraph

class DirectedTree(BaseGraph):
    def __init__(self, n:int , branching_factor: int, directions: Union[None, str] = None):
        super(DirectedTree, self).__init__(edges=None, adjacency_matrix=None)
        self.n = n
        self.branching_factor = branching_factor
        self._vertices = None
        self._edges = None
        self._adjacency_matrix = None
        self._directions = directions
        if type(self._directions) == str:
            assert self._directions in ['up', 'down', 'random'], ValueError('Invalid directions')
        if type(self._directions) == list:
            assert len(self._directions) == self.n, ValueError('Invalid directions')
        if self._directions is None:
            self._directions = 'up'
        self._generate_edges()
        self._generate_adjacency_matrix()

 
    def _generate_edges(self):
        self._vertices = list(range(self.n))
        self._edges = []
        if self._directions == 'up':
            for i in range(self.n):
                for j in range(self.branching_factor):
                    if i*self.branching_factor + j + 1 < self.n:
                            self._edges.append((i*self.branching_factor + j + 1, i))
                            
        elif self._directions == 'down':
            for i in range(self.n):
                for j in range(self.branching_factor):
                    if i*self.branching_factor + j + 1 < self.n:
                            self._edges.append((i, i*self.branching_factor + j + 1))

        elif self._directions == 'random':
            for i in range(self.n):
                for j in range(self.branching_factor):
                    if i*self.branching_factor + j + 1 < self.n:
                        if np.random.choice([True, False]):
                            self._edges.append((i*self.branching_factor + j + 1, i))
                        else:
                            self._edges.append((i, i*self.branching_factor + j + 1))


    def _generate_adjacency_matrix(self):
        self._adjacency_matrix = np.zeros((self.n, self.n))
        for edge in self._edges:
            self._adjacency_matrix[edge[0], edge[1]] = 1
        return self._adjacency_matrix