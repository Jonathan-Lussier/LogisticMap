import numpy as np
import matplotlib.pyplot as plt
import Sim
import json
print("Sim Start.")
#x[n+1] =  r*x*(1-x)

precision = 100000

R, X = Sim.simulate(precision)
np.savez("sim_data", R=R, X=X)

data = np.load("sim_data.npz")
fig, ax = plt.subplots()

ax.plot(data["R"], data["X"], 'k,', markersize=12)
plt.show()