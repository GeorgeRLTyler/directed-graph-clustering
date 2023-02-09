import numpy as np
from sklearn.cluster import KMeans


def DSBM_Clustering_Zanetti(adjacency_matrix,K,l,method='adjacency',normalize=False):
# input: np.array, adjacency_matrix --- A[i,j] = 1 if i -> j else 0.
#        int, K --- number of blocks/communities.
#        int, l --- number of eigenvectors to consider.
# output: clusters

    # construct Hermitian adjacency matrix
    A_hat = adjacency_matrix
    #A = (A + A.T)
    A = (A_hat - A_hat.T)*1j

    if method == 'laplacian':
        # construct Laplacian matrix
        D = np.diag(np.sum(np.abs(A),axis=0))
        A = D - A
        # calculating eigenvectors 
        eig_vals, eig_vecs = np.linalg.eig(A)
        #sorting according to largest in magnitude
        idx = np.abs(eig_vals).argsort()
    else:
        if normalize:
            # normalize adjacency matrix
            D = np.diag(np.sum(np.abs(A),axis=0))
            D = np.sqrt(np.linalg.inv(D))
            A = D @ A @ D
        eig_vals, eig_vecs = np.linalg.eig(A)
        #sorting according to largest in magnitude
        idx = np.abs(eig_vals).argsort()[::-1]
    
    eig_vecs = eig_vecs[:,idx][:,0:l]
    eig_vecs_projected = np.zeros((len(A),len(A)))
    for k in range(l):
        eig_vecs_projected = eig_vecs_projected + np.outer(eig_vecs[:,k],eig_vecs[:,k].conj()) 
    
    eig_vecs_projected  = np.real(eig_vecs_projected)

    kmeans = KMeans(n_clusters = K,n_init=25, random_state = 42).fit(eig_vecs_projected)
    clusters = kmeans.labels_

    return clusters, eig_vecs_projected