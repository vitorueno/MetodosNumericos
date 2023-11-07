import numpy as np
import matplotlib.pyplot as plt
import seaborn

seaborn.set(style='ticks')

x = np.linspace(0.2, 20, 100)
fig, ax = plt.subplots()
ax.plot(x, 1/x)
ax.plot(x, np.log(x))
ax.set_aspect('equal')
ax.grid(True, which='both')
seaborn.despine(ax=ax, offset=0)  # the important part here

plt.show()
