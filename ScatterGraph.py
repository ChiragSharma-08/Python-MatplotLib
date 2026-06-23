import matplotlib.pyplot as plt
import numpy as np

# Scatter Graph = Shows the relationship between two variables
#                 Helps to identify a correlation (+, -, None)
#                 Example: Study hours vs Test scores

x1 = np.array([0,0,1,1,2,3,3,4,5,8,9])
y1 = np.array([15,10,40,14,20,43,24,41,55,20,53])
x2 = np.array([0,1,1,2,2,3,4,5,5,6,8])
y2 = np.array([5,15,30,18,19,46,22,41,50,47,51])

plt.scatter(x1,y1, color = "blue",
                   alpha= 0.5,
                   s = 200,
                   label = "Class A")
plt.scatter(x2,y2, color = "red",
                   alpha= 0.4,
                   s = 200,
                   label = "Class B")

plt.title("Test Scores")
plt.xlabel("Hours Studied")
plt.ylabel("Marks")

plt.legend()
plt.show()