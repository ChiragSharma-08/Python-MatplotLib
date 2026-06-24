import matplotlib.pyplot as plt
import numpy as np

# Histograms = A visual rapresentation of distribution of quantitative data.
#              They group values into bins (intervals)
#              and counts jhow many fall in each range.

scores = np.random.normal(loc=80,scale=10,size=100)
scores = np.clip(scores, 0, 100)

plt.hist(scores, bins=10, # No. of divison you want in your histogram
                 color = "lightgreen",
                 edgecolor = "brown")

plt.title("Exam Scores")
plt.xlabel("Scores")
plt.ylabel("No. of students")

plt.show()