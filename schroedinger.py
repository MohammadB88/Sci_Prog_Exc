# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 16:44:42 2019

@author: mb1988
"""

import numpy as np
import matplotlib.pyplot as plt

def load_data(data_dir):
    """This function reads three files inside the provided directory and assign them
    to their corresponding numpy arrays
    
    energies = stor the energies from energies.dat file
    
    coordinate_discrpot = stor the coordinates and potentials from discrpot.dat file

    wfuncs = stor the wave function coefficients from wfuncs.dat file  
    
    """
    energies = np.loadtxt('{}/energies.dat'.format(data_dir))
    
    coordinate_discrpot = np.loadtxt('{}/discrpot.dat'.format(data_dir))
    
    wfuncs = np.loadtxt('{}/wfuncs.dat'.format(data_dir))
    
    print('Here is the array of energies: \n {} \n'.format(energies[:]))
    
    print('Here is the array of coordinates: \n {} \n'.format(coordinate_discrpot[:,0]))
    
    print('Here is the array of potentials: \n {} \n'.format(coordinate_discrpot[:,1]))
    
    print('Here is the array of potentials: \n {} \n'.format(wfuncs[:,1:4]))
    
    return energies, coordinate_discrpot, wfuncs

# This asks for the directory containing the datas
#data_dir =input('Please enter the name of the directory containing the data: ')

#  *************************  Inf_well  *************************
data_dir_infwell = 'schroedinger/inf_well/'

# This loads and print the datas
energies, coordinate_discrpot, wfuncs =load_data(data_dir_infwell)

print(np.size(coordinate_discrpot[:,0]))
print(np.size(energies))

# Start plotting the datas
plt.figure(figsize = (13,8))

# create a vactor of ones with the dimension of the coordinates.
# I need it to plot the horizontal gray lines in the plots
vactor_zeros = np.zeros(np.size(coordinate_discrpot[:,0]), dtype = int) 
    
# Create a new subplot from a grid of 1x2  ***** subplot(1,2,11 *****
plt.subplot(1,2,1)
plt.title('Infinite well (wavefunctions)')

plt.plot(coordinate_discrpot[:,0], coordinate_discrpot[:,1], color = 'black')

for itr in range(0, int(np.size(energies)/2)):
    plt.plot(coordinate_discrpot[:,0], energies[2*itr]+vactor_zeros, color = 'gray')
    plt.plot(coordinate_discrpot[:,0], energies[2*itr+1]+vactor_zeros, color = 'gray')
    plt.plot(wfuncs[:,0], energies[2*itr]+wfuncs[:,2*itr+1]*16, color = 'red')
    plt.plot(wfuncs[:,0], energies[2*itr+1]+wfuncs[:,2*itr+1+1]*16, color = 'blue')

# Set the boundaries on X and Y axis
plt.xlim((coordinate_discrpot[:,0]).min(), (coordinate_discrpot[:,0]).max())
plt.ylim(-0.5,6.3)

plt.xlabel('x [Bohr]')
plt.ylabel('Energy [Hartree]')

# Create a new subplot from a grid of 1x2  ***** subplot(1,2,2) *****
plt.subplot(1,2,2)
plt.title('Infinite well (probabilities)')

plt.plot(coordinate_discrpot[:,0], coordinate_discrpot[:,1], color = 'black')
    
for itr in range(0, int(np.size(energies)/2)):
    plt.plot(coordinate_discrpot[:,0], energies[2*itr]+vactor_zeros, color = 'gray')
    plt.plot(coordinate_discrpot[:,0], energies[2*itr+1]+vactor_zeros, color = 'gray')
    plt.plot(wfuncs[:,0], energies[2*itr]+(wfuncs[:,2*itr+1]*wfuncs[:,2*itr+1].transpose())*16*16, color = 'red')
    plt.plot(wfuncs[:,0], energies[2*itr+1]+(wfuncs[:,2*itr+1+1]*wfuncs[:,2*itr+1+1].transpose())*16*16, color = 'blue')

# Set the boundaries on X and Y axis
plt.xlim((coordinate_discrpot[:,0]).min(), (coordinate_discrpot[:,0]).max())
plt.ylim(-0.5,6.3)

plt.xlabel('x [Bohr]')
plt.ylabel('Energy [Hartree]')

plt.show()

#  *************************  Double_well  *************************
data_dir_doublewell = 'schroedinger/double_well/'

# This loads and print the datas
energies, coordinate_discrpot, wfuncs =load_data(data_dir_doublewell)

print(np.size(coordinate_discrpot[:,0]))
print(np.size(energies))

# Start plotting the datas
plt.figure(figsize = (13,8))

# create a vactor of ones with the dimension of the coordinates.
# I need it to plot the horizontal gray lines in the plots
vactor_zeros = np.zeros(np.size(coordinate_discrpot[:,0]), dtype = int) 

# Create a new subplot from a grid of 1x2  ***** subplot(1,2,11 *****
plt.subplot(1,2,1)
plt.title('Double well (wavefunctions)')

plt.plot(coordinate_discrpot[:,0], coordinate_discrpot[:,1], color = 'black')
    
for itr in range(0, int(np.size(energies)/2)):
    plt.plot(coordinate_discrpot[:,0], energies[2*itr]+vactor_zeros, color = 'gray')
    plt.plot(coordinate_discrpot[:,0], energies[2*itr+1]+vactor_zeros, color = 'gray')
    plt.plot(wfuncs[:,0], energies[2*itr]+wfuncs[:,2*itr+1]*2, color = 'red')
    plt.plot(wfuncs[:,0], energies[2*itr+1]+wfuncs[:,2*itr+1+1]*2, color = 'blue')

# Set the boundaries on X and Y axis
#plt.xlim((coordinate_discrpot[:,0]).min(), (coordinate_discrpot[:,0]).max())
plt.xlim(-12, 12)
plt.ylim(-1.6,2.5)

plt.xlabel('x [Bohr]')
plt.ylabel('Energy [Hartree]')

# Create a new subplot from a grid of 1x2  ***** subplot(1,2,2) *****
plt.subplot(1,2,2)
plt.title('Double well (probabilities)')

plt.plot(coordinate_discrpot[:,0], coordinate_discrpot[:,1], color = 'black')
    
for itr in range(0, int(np.size(energies)/2)):
    plt.plot(coordinate_discrpot[:,0], energies[2*itr]+vactor_zeros, color = 'gray')
    plt.plot(coordinate_discrpot[:,0], energies[2*itr+1]+vactor_zeros, color = 'gray')
    plt.plot(wfuncs[:,0], energies[2*itr]+(wfuncs[:,2*itr+1]*wfuncs[:,2*itr+1].transpose())*5*5, color = 'red')
    plt.plot(wfuncs[:,0], energies[2*itr+1]+(wfuncs[:,2*itr+1+1]*wfuncs[:,2*itr+1+1].transpose())*5*5, color = 'blue')

# Set the boundaries on X and Y axis
#plt.xlim((coordinate_discrpot[:,0]).min(), (coordinate_discrpot[:,0]).max())
plt.xlim(-12, 12)
plt.ylim(-1.6,2.5)

plt.xlabel('x [Bohr]')
plt.ylabel('Energy [Hartree]')

plt.show()

#  *************************  Harmonic Oscillator  *************************
data_dir_harmonic = 'schroedinger/harmonic/'

# This loads and print the datas
energies, coordinate_discrpot, wfuncs =load_data(data_dir_harmonic)

print(np.size(coordinate_discrpot[:,0]))
print(np.size(energies))

# Start plotting the datas
plt.figure(figsize = (13,8))

# create a vactor of ones with the dimension of the coordinates.
# I need it to plot the horizontal gray lines in the plots
vactor_zeros = np.zeros(np.size(coordinate_discrpot[:,0]), dtype = int) 

# Create a new subplot from a grid of 1x2  ***** subplot(1,2,11 *****
plt.subplot(1,2,1)
plt.title('Harmonic oscillator  (wavefunctions)')

plt.plot(coordinate_discrpot[:,0], coordinate_discrpot[:,1], color = 'black')
    
for itr in range(0, int(np.size(energies)/2)):
    plt.plot(coordinate_discrpot[:,0], energies[2*itr]+vactor_zeros, color = 'gray')
    plt.plot(coordinate_discrpot[:,0], energies[2*itr+1]+vactor_zeros, color = 'gray')
    plt.plot(wfuncs[:,0], energies[2*itr]+wfuncs[:,2*itr+1]*3, color = 'red')
    plt.plot(wfuncs[:,0], energies[2*itr+1]+wfuncs[:,2*itr+1+1]*3, color = 'blue')

# Set the boundaries on X and Y axis
#plt.xlim((coordinate_discrpot[:,0]).min(), (coordinate_discrpot[:,0]).max())
plt.xlim(-3, 3)
plt.ylim(0.0,2.5)

plt.xlabel('x [Bohr]')
plt.ylabel('Energy [Hartree]')

# Create a new subplot from a grid of 1x2  ***** subplot(1,2,2) *****
plt.subplot(1,2,2)
plt.title('Harmonic oscillator  (probabilities)')

plt.plot(coordinate_discrpot[:,0], coordinate_discrpot[:,1], color = 'black')
    
for itr in range(0, int(np.size(energies)/2)):
    plt.plot(coordinate_discrpot[:,0], energies[2*itr]+vactor_zeros, color = 'gray')
    plt.plot(coordinate_discrpot[:,0], energies[2*itr+1]+vactor_zeros, color = 'gray')
    plt.plot(wfuncs[:,0], energies[2*itr]+(wfuncs[:,2*itr+1]*wfuncs[:,2*itr+1].transpose())*6*6, color = 'red')
    plt.plot(wfuncs[:,0], energies[2*itr+1]+(wfuncs[:,2*itr+1+1]*wfuncs[:,2*itr+1+1].transpose())*6*6, color = 'blue')

# Set the boundaries on X and Y axis
#plt.xlim((coordinate_discrpot[:,0]).min(), (coordinate_discrpot[:,0]).max())
plt.xlim(-3, 3)
plt.ylim(0.0,2.5)

plt.xlabel('x [Bohr]')
plt.ylabel('Energy [Hartree]')

plt.show()