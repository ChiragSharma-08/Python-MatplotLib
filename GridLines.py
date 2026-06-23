import matplotlib.pyplot as plt
import numpy as np

# grid = Helps make plots easier to read by adding refrence lines.

x = np.array([2023, 2024, 2025, 2026])
y = np.array([15, 25, 30, 20])

# plt.grid() #Creates grids on both x and y axis
plt.grid(axis = "both", # Specifies the grid axis
         linewidth = 2,
         color = "lightgray",
         linestyle = "dashed")
plt.plot(x,y)
plt.show() 