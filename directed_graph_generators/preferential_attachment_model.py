# import sys
# sys.path.append("/home/georg/directed-graph-clustering")
import numpy as np

from directed_graph_generators.base_graph import BaseGraph

class PreferentialAttachmentModel(BaseGraph):
    def __init__(self, N,m,k,t_0,t_max,community_affinities, initial_graph=None):
        super(PreferentialAttachmentModel, self).__init__(vertices=N, edges=None, adjacency_matrix=None)
        self.m = int(m) #number of edges to add at each step
        self.k = range(int(k)) #number of communities
        self._community_affinities = community_affinities #k x k matrix of community affinities
        self.t_0 = t_0 #Number of initial nodes
        self.t_max = t_max #Number of nodes at end of simulation
        self._vertices = None
        self._vertex_communities = [np.random.choice(self.k) for i in range(self.t_0)]

        if initial_graph is None:
            #generate initial graph with m edges per node with no self loops
            # make vertices from 0 up to t_0 - 1
            self._vertices = list(range(self.t_0))

            if self.m >= self.t_0:
                self._edges = [(i,j) for i in range(self.t_0) for j in range(self.t_0) if i != j]
            else:
                self._edges = []
                for i in range(self.t_0):
                    for j in range(self.m):
                        while True:
                            node = np.random.choice(self._vertices)
                            if node != i:
                                self._edges.append((i,node))
                                break

        elif isinstance(initial_graph, BaseGraph):
            self._edges = initial_graph.edges
            self._vertices = initial_graph.vertices

    @property
    def adjacency_matrix(self):
        return self.adjacency_matrix_pam()

    def adjacency_matrix_pam(self):
        if self._adjacency_matrix is None:
            for t in range(self.t_0,self.t_max):
                #add community chosen at random for new node
                self._vertex_communities.append(np.random.choice(self.k))
                for e in range(self.m):
                    #get probability of choosing each node
                    edge_starts, edge_ends = zip(*self._edges)
                    p = [(self._community_affinities[self._vertex_communities[t],self._vertex_communities[j]])*(edge_ends.count(j) + edge_starts.count(j)) for j in self._vertices]
                    p = [i/sum(p) for i in p]
                    #choose node
                    node = np.random.choice(self._vertices, p=p)
                    #add edge
                    self._edges.append((t,node))
                self._vertices.append(t)
            self.convert_list_of_edges_to_adjacency_matrix()
        return self._adjacency_matrix
    
    def convert_list_of_edges_to_adjacency_matrix(self):
        self._adjacency_matrix = np.zeros((len(self._vertices),len(self._vertices)))
        for edge in self._edges:
            self._adjacency_matrix[edge[0],edge[1]] = 1
    
    def convert_adjacency_matrix_to_list_of_edges(self):
        self._edges = []
        for i in range(self._adjacency_matrix.shape[0]):
            for j in range(self._adjacency_matrix.shape[1]):
                if self._adjacency_matrix[i,j] == 1:
                    self._edges.append((i,j))

# if __name__ == "__main__":
#     N = 100
#     m = 2
#     k = 2
#     t_0 = 10
#     t_max = 100
#     community_affinities = np.array([[0.5,0.5],[0.5,0.5]])
#     graph = PreferentialAttachmentModel(N,m,k,t_0,t_max,community_affinities)
#     print(graph.adjacency_matrix)