import numpy as np
import scipy as sp
from sklearn.cluster import KMeans

def Exponential_Clustering(adjacency_matrix,K,l,t):
    A = (adjacency_matrix - adjacency_matrix.T)*1j
    A_abs = np.abs(A)
    D_bar_inv = np.zeros(A.shape)
    np.fill_diagonal(D_bar_inv,[1/np.sqrt(d) for d in np.sum(A_abs, axis=1) if d != 0])
    exp_A = sp.linalg.expm(t*( D_bar_inv @ A  @ D_bar_inv))
    cos_A = np.real(exp_A)
    eig_vals, eig_vecs = np.linalg.eig(cos_A)
    #sorting according to largest in magnitude
    idx = np.abs(eig_vals).argsort()[::-1]
    eig_vecs = eig_vecs[:,idx][:,0:l]
    eig_vecs_projected = np.zeros((len(A),len(A)))
    for k in range(l):
        eig_vecs_projected = eig_vecs_projected + np.outer(eig_vecs[:,k],eig_vecs[:,k].conj()) 
    
    eig_vecs_projected  = np.real(eig_vecs_projected)
    kmeans = KMeans(n_clusters = K).fit(eig_vecs_projected)
    clusters = kmeans.labels_
    return clusters, eig_vecs_projected


def Exponential_Clustering_no_evecs(adjacency_matrix,K,t):
    A = (adjacency_matrix - adjacency_matrix.T)*1j
    A_abs = np.abs(A)
    D_bar_inv = np.zeros(A.shape)
    np.fill_diagonal(D_bar_inv,[1/np.sqrt(d) for d in np.sum(A_abs, axis=1) if d != 0])
    exp_A = sp.linalg.expm(t*(np.eye(len(A)) - D_bar_inv @ A @ D_bar_inv))
    cos_A = np.real(exp_A)
    
    kmeans = KMeans(n_clusters = K).fit(cos_A)
    clusters = kmeans.labels_
    return clusters, cos_A