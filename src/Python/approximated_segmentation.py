import matplotlib.pyplot as plt
import numpy as np
from statistics import variance as var

def approximated_segmentation(A, var_segments):
    thresh = 0
    while thresh < 3:
        for i in range(0, len(var_segments)):
            print(var_segments)
            if i == 0:
                tempvar = np.var(A[0:var_segments[i]])*(var_segments[i])/len(A) + np.var(A[var_segments[i]:var_segments[i + 1]])*(var_segments[i + 1] - var_segments[i])/len(A)
                index = var_segments[i]
                for j in range(2, var_segments[i + 1] - 2):
                    tempvar2 = np.var(A[0:j])*(j + 1)/len(A) + np.var(A[j:var_segments[i + 1]])*(var_segments[i + 1] - j)/len(A)
                    if tempvar2 < tempvar:
                        tempvar = tempvar2
                        index = j
                        thresh = 0
            elif i == len(var_segments) - 1:
                tempvar = np.var(A[var_segments[i - 1]:var_segments[i]])*(var_segments[i] - var_segments[i - 1])/len(A) + np.var(A[var_segments[i]:len(A)])*(len(A) - var_segments[i])/len(A)
                index = var_segments[i]
                for j in range(var_segments[i - 1] + 2, len(A) - 2):
                    tempvar2 = np.var(A[var_segments[i - 1]:j])*(j - var_segments[i - 1])/len(A) + np.var(A[j:len(A)])*(len(A) - j)/len(A)
                    if tempvar2 < tempvar:
                        tempvar = tempvar2
                        index = j
                        thresh = 0
            else:
                tempvar = np.var(A[var_segments[i - 1]:var_segments[i]])*(var_segments[i] - var_segments[i - 1])/len(A) + np.var(A[var_segments[i]:var_segments[i + 1]])*(var_segments[i + 1] - var_segments[i])/len(A)
                index = var_segments[i]
                for j in range(var_segments[i - 1] + 2, var_segments[i + 1] - 2):
                    tempvar2 = np.var(A[var_segments[i - 1]:j])*(j - var_segments[i - 1])/len(A) + np.var(A[j:var_segments[i + 1]])*(var_segments[i + 1] - j)/len(A)
                    if tempvar2 < tempvar:
                        tempvar = tempvar2
                        index = j
                        thresh = 0
            
            var_segments[i] = index
                                  
        thresh += 1
    
    return(var_segments)