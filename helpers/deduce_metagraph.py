### Function to deduce the metagraph of a graph from its adjacency matrix and the clusters given
import numpy as np

def deduce_metagraph(adjacency_matrix: np.array, clusters: list, normalize: bool) -> np.array:
    """ Returns the metagraph of a graph given its adjacency matrix and the clusters of the graph.
    INPUTS: np.array, adjacency_matrix --- A[i,j] = 1 if i -> j else 0.
            list, clusters --- list of lists of vertices in each cluster.
    """
    adjacency_sym = adjacency_matrix + adjacency_matrix.T
    k = len(clusters)
    M = np.zeros((k,k))
    meta_D = np.zeros((k,k))

    for i in range(k):
        meta_D[i,i] = np.sum(adjacency_sym[clusters[i],:])
        for j in range(k):
            M[i,j] = np.sum(adjacency_matrix[np.ix_(clusters[i],clusters[j])])
            
    if normalize:
        # normalize adjacency matrix
        D_inv_sqrt = np.zeros(M.shape)
        np.fill_diagonal(D_inv_sqrt,[1/np.sqrt(d) for d in np.diag(meta_D) if d != 0])
        M = D_inv_sqrt @ M @ D_inv_sqrt
    
    return M

