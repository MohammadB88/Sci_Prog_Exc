# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 21:09:21 2019

@author: mb1988
"""

import numpy as np

m1 = np.array([[1, 2, 3], [4, 5, 6]])
m2 = np.array([[1, 2], [3, 4], [5, 6]])

m1_raw, m1_column = m1.shape[0], m1.shape[1]
m2_raw, m2_column = m2.shape[0], m2.shape[1]

print('Shape of the first matrix: {}x{}'.format(m1_raw,m1_column))
print('Shape of the second matrix: {}X{}'.format(m2_raw,m2_column))

def matrix_product(m1,m2,m1_raw,m1_column,m2_column):
    """ Calculate the product of two matrices
    
    Args:
        m1: first matrix
        m2: second matrix
        m1_raw: raw of the first matrix
        m1_column: column of the first matrix
        m2_column: column of the second matrix
        
    Returns:
        result of matrix multiplication
    """
    m1m2 = np.zeros((m1_raw,m1_raw), dtype=int)
    for i in range(m1_raw):
        for j in range(m2_column):
            for k in range(m1_column):
#                print(i, j, k)
#                print(m1[i,k],m2[k,j])
                m1m2[i,j] += m1[i,k]*m2[k,j]
#                print(m1m2[i,j])
    return m1m2

matrix_product(m1,m2,m1_raw,m1_column,m2_column)

print('\nHere is the product using the function I wrote:')
print(matrix_product(m1,m2,m1_raw,m1_column,m2_column))

m1m2 = np.dot(m1,m2)
print('\nHere is the product using the built-in function "np.dot()":')
print(m1m2)
