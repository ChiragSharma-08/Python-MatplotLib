import matplotlib.pyplot as plt
import numpy as np

# Pie Chart = Circular chart divided into slices to show percentage of the total.
#             Good for visualization distribution among categories

categories = ["First year", "Second year", "Third year", "Forth year"]
values = np.array([300,275,250,225])
colors = ["violet", "indigo", "blue", "green"]

plt.pie(values, labels = categories,
                autopct= "%1.1f%%",
                colors = colors,
                explode = [0,0,0,0.2],
                shadow= True,
                startangle=60)

plt.title("STUDENTS")

plt.show()