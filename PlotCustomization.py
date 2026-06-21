import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023, 2024, 2025, 2026])
y1 = np.array([15, 25, 30, 20])
y2 = np.array([15, 30, 42, 10])
y3 = np.array([15, 10, 18, 37])

line_style = dict(marker=".",# You can also take different symbols from the matplotlib documentation
                   markersize=30,
                   markerfacecolor="blue",# We can also pick rgb and hexadecimal values
                   markeredgecolor="black",
                   linestyle="solid",
                   linewidth=4,
)

plt.plot(x, y1,marker="v",
               markersize=30,
               markerfacecolor="blue",
               markeredgecolor="black",
               linestyle="dashdot",
               linewidth=4,
               color="yellow"
)

plt.plot(x, y2, **line_style, color="pink") #You can also set color in our dictionary
plt.plot(x, y3, **line_style, color = "orange")

plt.show()