import pandas as pd
import numpy as np
from typing import Union

class BaseGraph:
    def __init__(self,vertices:Union[int,list,dict,pd.Series,None] = None,edges:Union[list,dict,pd.Series,None] = None, adjacency_matrix:Union[pd.DataFrame,np.array,None] = None):
        """A base class for all graph types. It is not meant to be used directly. It is meant to be inherited by other graph classes. If you want to create a graph, use one of the other classes.
        args:
            vertices: The vertices of the graph. Can be a list, a dictionary, a pandas series, or an integer. If it is an integer, it will be interpreted as the number of vertices in the graph.
                      If a list, the length of the list will be the number of vertices on the graph with the values of the list being the names/numbers of the vertices.
                      If a dictionary, the keys will be the names/numbers of the vertices and the values will be values that are stored on the vertices for whatever purpose.
                      If a pandas series, the index will be the names/numbers of the vertices and the values will be values that are stored on the vertices for whatever purpose.
                      If None, it is expected that the adjacency matrix will be provided and the vertices will be inferred from the adjacency matrix.
            edges: The edges of the graph. Can be a list, a dictionary, or a pandas series. If a list, it is expected to be a list of tuples and the the graph is assumed unweighted.
                    If a dictionary, the keys are the edges (also tuples) and the values are the weights of the edges.
                    If a pandas series, the index is the edges (also tuples) and the values are the weights of the edges.
                    If None, it is expected that the adjacency matrix will be provided and the edges will be inferred from the adjacency matrix.
            adjacency_matrix: The adjacency matrix of the graph. Can be a pandas dataframe or a numpy array. If a pandas dataframe, the index and columns are the names/numbers of the vertices.
                              It is expected that the index and columns match and the dataframe is square. If a numpy array, the rows and columns are the names/numbers of the vertices.
                              The entries in the dataframe/array are the weights of the edges. If None, it is expected that the vertices and edges will be provided."""

        self._vertices = vertices
        self._edges = edges
        self._adjacency_matrix = adjacency_matrix

    @property
    def vertices(self):
        return self._vertices
    
    @vertices.setter
    def vertices(self,vertices):
        self._vertices = vertices
    
    @property
    def edges(self):
        return self._edges
    
    @edges.setter
    def edges(self,edges):
        self._edges = edges
            
    @property
    def adjacency_matrix(self):
        return self._adjacency_matrix

    @adjacency_matrix.setter
    def adjacency_matrix(self,adjacency_matrix):
        self._adjacency_matrix = adjacency_matrix 
    
    @adjacency_matrix.deleter
    def adjacency_matrix(self):
        print('deleted adjacency matrix')
        del self._adjacency_matrix
