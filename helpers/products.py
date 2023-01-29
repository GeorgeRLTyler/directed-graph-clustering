import numpy as np

class Products:
    @staticmethod
    def tensor_product(A: np.array, B: np.array):
        """Method for calculating the tensor product of two matrices."""
        return np.kron(A, B)
    
    def cartesian_product(A: np.array, B: np.array):
        """Method for calculating the cartesian product of two matrices."""
        n_A = A.shape[0]
        n_B = B.shape[0]
        return Products.tensor_product(A, np.eye(n_B)) + Products.tensor_product(np.eye(n_A), B)