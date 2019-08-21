# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 16:44:42 2019

@author: mb1988
"""

import numpy as np
import matplotlib.pyplot as plt

def load_data(data_dir):
    """Read in the data from a QM-calculation
    
    Args: 
        data_dir: The directory that contains the data.
        (energies, discrpot.dat, wfuncs.dat)
    
    return: 
        Tuples (coordinate, energies, potential, wavefunctions) with the coordinates,
        eigenenergies, potential and wavefunctions on the coordinates.
    """
    
    energies = np.loadtxt('{}/energies.dat'.format(data_dir))
    coordinate_discrpot = np.loadtxt('{}/discrpot.dat'.format(data_dir))
    wfuncs = np.loadtxt('{}/wfuncs.dat'.format(data_dir))
    
    coordinate = coordinate_discrpot[:,0]
    energies = energies[:]
    potential = coordinate_discrpot[:,1]
    wavefunctions = wfuncs[:,1:]
    print('Here is the array of energies: \n {} \n'.format(energies))
    print('Here is the array of coordinates: \n {} \n'.format(coordinate))
    print('Here is the array of potentials: \n {} \n'.format(potential))
    print('Here is the array of potentials: \n {} \n'.format(wavefunctions))
    
    return coordinate, energies, potential, wavefunctions

def plot_results(plot_title, coordinate, energies, potential, wavefunctions, prefactor=1.0, xlim=None, ylim=None):
    """Plot the results from a QM-calculation
    
    args: 
        plot_title: Title of the plot
        coordinate: The coordinate on which the potential and wavefunctions are represented.
        energiee: Eigenenergies from a QM-calculation
        potential: Potential values on the coordinates
        wavefunctions: Wave function values on the coordinates
        prefactor: Scaling factor for the wave functions (default: 1.0)
        xlim: Minimal and maximal x-values to show (default: actual plt.xlim values)
        ylim: Minimal and maximal y-values to show (default: actual plt.ylim values)
    
    return: ????
        Plot the provided data and indicating its title.
    """
    plt.title(plot_title, fontsize = 14)
    plt.xlabel('x [Bohr]', fontsize = 14)
    plt.ylabel('Energy [Hartree]', fontsize = 14)

    if xlim == None:
        xmin, xmax = plt.xlim()
    else:
        xmin, xmax = xlim
        plt.xlim(xmin, xmax)
        
    if ylim == None:
        ymin, ymax = plt.ylim()
    else:   
        ymin, ymax = ylim        
        plt.ylim(ymin, ymax)

    plt.plot(coordinate, potential, color = 'black')

    for itr in range(0, np.size(energies)):
        if itr%2 == 0:
            plt.plot([xmin, xmax], [energies[itr], energies[itr]], color = 'gray')
            plt.plot(coordinate, prefactor*wavefunctions[:,itr]+energies[itr], color = 'red')
        else:
            plt.plot([xmin, xmax], [energies[itr], energies[itr]], color = 'gray')
            plt.plot(coordinate, prefactor*wavefunctions[:,itr]+energies[itr], color = 'blue')

#    return???

#  *************************  Inf_well  *************************
# Call the function that reads the results
coordinate, energies, potential, wavefunctions = load_data('schroedinger/inf_well/')

print(np.size(coordinate))
print(np.size(energies))

# Start plotting the datas
plt.figure(figsize = (13,8))

# Set the boundaries on X and Y axis
xlim = -2.0, 2.0
ylim = -0.5, 6.5

# Create a new subplot from a grid of 1x2  ***** subplot(1,2,11 *****
plt.subplot(1,2,1)

# Call the plotting function
plot_results('Infinite well (wavefunctions)', coordinate, energies, potential, wavefunctions, prefactor=16, xlim=xlim, ylim=ylim)

# Create a new subplot from a grid of 1x2  ***** subplot(1,2,2) *****
plt.subplot(1,2,2)

# Call the plotting function
plot_results('Infinite well (probabilities)', coordinate, energies, potential, np.abs(wavefunctions)**2, prefactor=400, xlim=xlim, ylim=ylim)

plt.show()

#  *************************  Double_well  *************************
# Call the function that reads the results
coordinate, energies, potential, wavefunctions = load_data('schroedinger/double_well/')

print(np.size(coordinate))
print(np.size(energies))

# Start plotting the datas
plt.figure(figsize = (13,8))

# Set the boundaries on X and Y axis
xlim = -12.0, 12.0
ylim = -1.6, 2.5

# Create a new subplot from a grid of 1x2  ***** subplot(1,2,11) *****
plt.subplot(1,2,1)

# Call the plotting function
plot_results('Double well (wavefunctions)', coordinate, energies, potential, wavefunctions, prefactor=2.2, xlim=xlim, ylim=ylim)

# Create a new subplot from a grid of 1x2  ***** subplot(1,2,2) *****
plt.subplot(1,2,2)

# Call the plotting function
plot_results('Double well (probabilities)', coordinate, energies, potential, np.abs(wavefunctions)**2, prefactor=25, xlim=xlim, ylim=ylim)

plt.show()

#  *************************  Harmonic Oscillator  *************************
# Call the function that reads the results
coordinate, energies, potential, wavefunctions = load_data('schroedinger/harmonic/')

print(np.size(coordinate))
print(np.size(energies))

# Start plotting the datas
plt.figure(figsize = (13,8))

# Set the boundaries on X and Y axis
xlim = -3.0, 3.0
ylim = 0.0, 2.5

# Create a new subplot from a grid of 1x2  ***** subplot(1,2,11) *****
plt.subplot(1,2,1)

# Call the plotting function
plot_results('Harmonic oscillator (wavefunctions)', coordinate, energies, potential, wavefunctions, prefactor=2.5, xlim=xlim, ylim=ylim)

# Create a new subplot from a grid of 1x2  ***** subplot(1,2,2) *****
plt.subplot(1,2,2)

# Call the plotting function
plot_results('Harmonic oscillator (probabilities)', coordinate, energies, potential, np.abs(wavefunctions)**2, prefactor=50, xlim=xlim, ylim=ylim)

plt.show()