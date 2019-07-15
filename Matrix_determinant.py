# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 14:52:53 2019

@author: mb1988
"""

# ***** Using a function inside itself is the lesson I have learned in this example. *****

import numpy as np


print('Now let\'s check our code for a 2x2 matrix:')

mtx = np.array([[1.0, 2.0], [3.0, 4.0]])
print(mtx)

def determinant(mtx):
    """This calculates the determinant for a 2x2 matrix.
    
    Arg:
        mtx: the input matrix,
        
    return:
        determinant of a 2x2 matrix,
    """
    det_mtx = mtx[0,0]*mtx[1,1] - mtx[0,1]*mtx[1,0]
    return det_mtx


print('Determinant of the given matrix is equal to: ', determinant(mtx))
print('The determinant calculated by "Numpy" module is equal to: ', np.linalg.det(mtx))


print('\nNow let\'s check our code for a 3x3 matrix:')

mtx3x3 = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 10.0]])
print(mtx3x3)

def determinant(mtx3x3):
    """This calculates the determinant for a 3x3 matrix.
    
    Arg:
        mtx3x3: the input matrix,
        
    return:
        determinant of a 3x3 matrix,
    """
    det_mtx3x3 = mtx3x3[0,0]*mtx3x3[1,1]*mtx3x3[2,2] + mtx3x3[0,1]*mtx3x3[1,2]*mtx3x3[2,0] + mtx3x3[0,2]*mtx3x3[1,0]*mtx3x3[2,1] - mtx3x3[0,2]*mtx3x3[1,1]*mtx3x3[2,0] - mtx3x3[0,1]*mtx3x3[1,0]*mtx3x3[2,2] - mtx3x3[0,0]*mtx3x3[1,2]*mtx3x3[2,1]
    return det_mtx3x3


print('Determinant of the given matrix is equal to: ', determinant(mtx3x3))
print('The determinant calculated by "Numpy" module is equal to: ', np.linalg.det(mtx3x3))

def determinant(mtx):
    """Calculates the determinant of a matrix.,

    Note: this routines serves didactic purposes only, use numpy.linalg.det in production runs!,
    
    Args:
        mtx: Square matrix as numpy array.,
    Returns:,
        Determinant of the matrix.,
    """
    nn = mtx.shape[0]
#    print(nn)
    if nn == 1:
        return mtx[0, 0]
    submtx = np.empty((nn - 1, nn - 1), dtype=float)
    det = 0.0   
    for ii in range(nn):
#        print('ii: ', ii )
        submtx[:, :ii] = mtx[1:, 0:ii]
        submtx[:, ii:] = mtx[1:, ii + 1:]
#        print(submtx[:, :ii], '\n', submtx[:, ii:])
#        print(mtx[0, ii])        
        det += (-1)**ii * mtx[0, ii] * determinant(submtx)
#        print(det)
    return det

print('Here is the determinant of an arbitrary matrix using Balint\'s method: ', determinant(mtx3x3))
