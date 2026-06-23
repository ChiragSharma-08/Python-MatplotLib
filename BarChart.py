import matplotlib.pyplot as plt
import numpy as np

# Bar Chart = compare categories of data by representing each category with a bar

categories = np.array(["Grains", "Stationary", "Vegetables", "Grooming", "Dairy", "Sweets"])
values = np.array([20,30,25,60,15,30])

plt.title("Profit")
plt.xlabel("Item")
plt.ylabel("Margin%")


plt.bar(categories,values,color="blue")
# plt.barh(categories,values,color="blue") # Creates horizontal bar charts 

plt.show()