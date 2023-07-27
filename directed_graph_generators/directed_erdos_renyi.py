import numpy as np
from directed_graph_generators.base_graph import BaseGraph

class DirectedErdosRenyi(BaseGraph):

    def __init__(self,N,p):
        super(DirectedErdosRenyi,self).__init__(vertices=N,edges=None,adjacency_matrix=None)
        self.N = int(N)
        self.p = float(p)

    @property
    def adjacency_matrix(self):
        return self.adjacency_matrix_er()

    def adjacency_matrix_er(self):
        if self._adjacency_matrix is None:
            self._adjacency_matrix = np.random.binomial(1, self.p, int((self.N)*(self.N)))
            self._adjacency_matrix = self._adjacency_matrix.reshape((self.N,self.N))
            np.fill_diagonal(self._adjacency_matrix,0)
        return self._adjacency_matrix