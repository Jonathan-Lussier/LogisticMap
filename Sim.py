import numpy as np
import matplotlib.pyplot as plt
print("Sim Start.")
#x[n+1] =  r*x*(1-x)

def simulate(precision):
    R = np.empty((1*precision,1))
    X = np.full((1*precision,1),0.5)

    for j in range(0,1*precision):
        R[j] = j*(4/precision)
        x = 0.1
        for i in range(0,100):
            x = R[j] * x * (1 - x)
        X[j] = x
    return(R,X)