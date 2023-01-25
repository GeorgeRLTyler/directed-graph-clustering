from typing import Union, Dict, List, Tuple
import numpy as np

# Class for converting between edge list and adjacency matrix, regardless of the format.
class Converter:
    @staticmethod
    def convert_from_edge_list_to_adjacency_matrix(edge_list: Union[Dict[Tuple[int], Union[float,int]], List[Tuple[int]]]):
        """Method for converting from edge list to adjacency matrix. the edge list can be either a list of tuples or a dictionary of tuples where
        the values are weights."""

        N = len(edge_list)
        adjacency_matrix = np.zeros((N,N))
            
        if type(edge_list) == list:
            for edge in edge_list:
                adjacency_matrix[edge[0],edge[1]] = 1
        
        elif type(edge_list) == dict:
            for edge in edge_list.keys():
                adjacency_matrix[edge[0],edge[1]] = edge_list[edge]
        

    @staticmethod
    def convert_adjacency_matrix_to_list_of_edges(adjacency_matrix: np.array):
        """Method for converting from adjacency matrix to edge list. The edge list is a list of tuples if the adjacency matrix has
        1s and 0s as entries and is dictionary if it is weighted."""
        N = adjacency_matrix.shape[0]
        # check if matrix is weighted
        if np.all(adjacency_matrix == adjacency_matrix.astype(bool)):
            edge_list = []
            for i in range(N):
                for j in range(N):
                    if adjacency_matrix[i,j] == 1:
                        edge_list.append((i,j))
        else:
            edge_list = {}
            for i in range(N):
                for j in range(N):
                    if adjacency_matrix[i,j] != 0:
                        edge_list[(i,j)] = adjacency_matrix[i,j]
                        
        return edge_list