import numpy as np
import numpy.random as rndg
import sys
Energy_H, Sigma_Total_H, Sigma_Elastic_H, Sigma_Absorption_H = np.loadtxt('./1-H.csv', delimiter=';', unpack=True)
Energy_O, Sigma_Total_O, Sigma_Elastic_O, Sigma_Absorption_O = np.loadtxt('./16-O.csv', delimiter=';', unpack=True)
nb_H = len(Energy_H) 
nb_O = len(Energy_O) 
print("=== Number of cross-section data for isotope 1-H: ",nb_H)
print("=== Number of cross-section data for isotope 16-O: ",nb_O)

