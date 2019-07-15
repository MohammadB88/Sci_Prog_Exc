# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 21:09:21 2019

@author: mb1988
"""

import numpy as np

m1 = np.array([[1, 2, 3], [4, 5, 6]])
m2 = np.array([[1, 2], [3, 4], [5, 6]])

m1_dim_raw, m1_dim_column = len(m1), len(m1[0])
m2_dim_raw, m2_dim_column = len(m2), len(m2[0])

print('Shape of the first matrix: {}x{}'.format(m1_dim_raw,m1_dim_column))
print('Shape of the second matrix: {}X{}'.format(m2_dim_raw,m2_dim_column))

def matrix_product(m1,m2,m1_dim_raw,m1_dim_column,m2_dim_column):
    m1m2 = np.zeros((m1_dim_raw,m1_dim_raw), dtype=int)
    for i in range(m1_dim_raw):
        for j in range(m2_dim_column):
            for k in range(m1_dim_column):
#                print(i, j, k)
#                print(m1[i,k],m2[k,j])
                m1m2[i,j] += m1[i,k]*m2[k,j]
#                print(m1m2[i,j])
    return m1m2

matrix_product(m1,m2,m1_dim_raw,m1_dim_column,m2_dim_column)

print('\nHere is the product using the function I wrote:')
print(matrix_product(m1,m2,m1_dim_raw,m1_dim_column,m2_dim_column))

m1m2 = np.dot(m1,m2)
print('\nHere is the product using the built-in function "np.dot()":')
print(m1m2)