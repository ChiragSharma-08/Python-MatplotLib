import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023, 2024, 2025, 2026])
y1 = np.array([15, 25, 30, 20])
y2 = np.array([15, 30, 42, 10])
y3 = np.array([15, 10, 18, 37])

plt.title("Class Size", fontsize = 25,
                        family = "Arial",
                        fontweight = "bold",
                        color = "blue")

plt.xlabel("Class Size", fontsize = 25,
                         family = "Arial",
                         fontweight = "bold",
                         color = "blue")
plt.ylabel("Students"  , fontsize = 20,
                         family = "Arial",
                         fontweight = "normal",
                         color = "blue")

plt.xticks(x)

plt.tick_params(
    axis="both",         # x, y or both
    color="yellow",      # tick marks
    labelcolor="red"     # tick labels
)

plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)

plt.show() 