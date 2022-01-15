from statistics import variance as variance
import numpy as np


def brute_force_segmentation(A):
    variance = np.var(A[0:2]) + np.var(A[2:4]) + np.var(A[4:6]) + np.var(A[6:8]) + np.var(A[8:len(A)])
    index = [2, 4, 6, 8]
    
    for h in range(2, len(A) - 8):
        for i in range(h + 2, len(A) - 6):
            for j in range(i + 2, len (A) - 4):
                for k in range(j + 2, len (A) - 2):
                    tempvar = np.var(A[0:h]) + np.var(A[h:i]) + np.var(A[i:j]) + np.var(A[j:k]) + np.var(A[k:len(A)])
                    if tempvar < variance:
                        variance = tempvar
                        index[0] = h
                        index[1] = i
                        index[2] = j
                        index[3] = k

    return(index)