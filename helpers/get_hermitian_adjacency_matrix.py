# Function that when given the adjacency matrix of a directed graph
# returns the hermitian adjacency matrix of the graph, with the option to normalize
import numpy as np


def get_hermitian_adjacency_matrix(adjacency_matrix: np.array, normalize: bool = False, roots_of_unity: int =4) -> np.array:
    """ Returns the hermitian adjacency matrix of a directed graph.
    """
    #create kth root of unity
    w_k = np.exp(2*np.pi*1j/roots_of_unity)
    #construct adjacency matrix
    A = w_k*adjacency_matrix + np.conj(w_k)*(adjacency_matrix.T)

    if normalize:
        # normalize adjacency matrix
        D = np.zeros(A.shape)
        np.fill_diagonal(D,[1/np.sqrt(d) for d in np.sum(np.abs(A), axis=1) if d != 0])
        A = D @ A @ D
    
    #clean up real parts if roots_of_unity=4
    if roots_of_unity == 4:
        A = 1j*np.imag(A)
    
    return A