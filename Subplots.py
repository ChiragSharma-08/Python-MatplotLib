import matplotlib.pyplot as plt
import numpy as np

# Figure = THe entire canvas
# Ax = A single plot (subplot)

x = np.array([1,2,3,4,5])

# print(plt.subplot(2,2))
figure, axes = plt.subplots(2,2) # Creating 2X2 subplots 2 row, 2 column

axes[0,0].plot(x, x*2, color = "red")
axes[0,0].set_title("x*2")

axes[0,1].plot(x, x**2, color = "blue")
axes[0,1].set_title("x^2")

axes[1,0].plot(x, x**3, color = "green")
axes[1,0].set_title("x^3")

axes[1,1].plot(x, 2**x, color = "#948336")
axes[1,1].set_title("2^x")

plt.tight_layout()
plt.show()