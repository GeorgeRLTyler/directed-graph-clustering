import numpy as np
from directed_graph_generators.base_graph import BaseGraph

class DirectedStochasticBlockModel(BaseGraph):

    def __init__(self,k,N,p,q,F):
        super(DirectedStochasticBlockModel,self).__init__(vertices=N,edges=None,adjacency_matrix=None)
        self.N = int(N)
        self.k = int(k)
        self.F = np.array(F)
        self.p = float(p)
        self.q = float(q)
        self.n = int(self.N/self.k)
        self.correct_clusters = [j for j in range(self.k) for i in range(self.n)]

    @property
    def adjacency_matrix(self):
        return self.adjacency_matrix_dbsm()
    
    def adjacency_matrix_dbsm(self):
        if self._adjacency_matrix is None:
            nodes = [i for i in range(self.N)]
            self._adjacency_matrix = self.F.tolist()
            for cluster_index1 in range(self.k):
                for cluster_index2 in range(cluster_index1,self.k):
                    direction_prob = self.F[cluster_index1,cluster_index2]
                    if cluster_index1 == cluster_index2:
                        connections = np.random.binomial(1, self.p, int((self.n)*(self.n)))
                        connections = connections.reshape((self.n,self.n))
                        np.fill_diagonal(connections,0)
                        #removing duplicated edges
                        dup_i, dup_j = np.nonzero(np.triu((connections + connections.T) == 2))
                        dup_tuples = list(zip(dup_i,dup_j))
                        tuples_to_keep = np.random.binomial(1, 1/2, len(dup_tuples))
                        for index, (i,j) in enumerate(dup_tuples):
                            if tuples_to_keep[index] == 1:
                                connections[i,j] = 1
                                connections[j,i] = 0
                            else:
                                connections[i,j] = 0
                                connections[j,i] = 1
                        
                    #set block equal to connections at correct position
                        self._adjacency_matrix[cluster_index1][cluster_index2] = connections
                    else:
                        connections = np.random.binomial(1, self.q, int((self.n)*(self.n)))
                        connections = connections.reshape(self.n,self.n)
                        #get positions of nonzero entries.
                        i,j = np.nonzero(connections)
                        #select with probability == direction_prob
                        ix = np.random.choice(len(i), int(np.floor(direction_prob * len(i))), replace=False)
                    
                        connections_upper = np.zeros(connections.shape)
                        connections_upper[i[ix],j[ix]] = connections[i[ix],j[ix]]
                        connections_lower = connections - connections_upper

                        self._adjacency_matrix[cluster_index1][cluster_index2] = connections_upper
                        self._adjacency_matrix[cluster_index2][cluster_index1] = connections_lower
            #convert list of list of arrays to block matrix 
            self._adjacency_matrix = np.block(self._adjacency_matrix)
        return self._adjacency_matrix
    
