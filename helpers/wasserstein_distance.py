import taichi as ti
import numpy as np

from scipy.optimize import linprog


def wasserstein_distance(X,Y,dist):
    """ Compute the wasserstein distance between two discrete distributions X and Y where dist is the distance matrix between the support points.
    """
    # first flatten dist matrix:
    d = dist.flatten()
    N = len(d)
    # to be used in minizing d.T @ J
    # matrix that is N_x by len(J) and sums each flattened on column of X.
    A = np.zeros((len(X),N)) 
    for i in range(len(X)):
        A[i,i*len(Y):(i+1)*len(Y)] = 1

    # matrix that is N_y by len(J) and sums each flattened on column of Y.
    B = np.zeros((len(Y),N))
    for i in range(len(Y)):
        B[i,i::len(Y)] = 1
    
    #concatenating A and B
    A_and_B = np.concatenate((A,B),axis=0)
    X_and_Y = np.concatenate((X,Y),axis=0)

    #linear programming problem
    res = linprog(d,A_eq=A_and_B,b_eq=X_and_Y,bounds=(0,None))
    return res.fun
