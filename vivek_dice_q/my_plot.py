"""Plot the results of the experiments."""

import matplotlib.pyplot as plt
from collections import defaultdict

def draw_bar(title, results):
    """Plot the bar graph from 1.0 to 6.0 with 1 decimal."""
    hist = defaultdict(int)
    for i in range(len(results)):
        # Round to 1 decimal 
        key = results[i]
        hist[key] += 1

    x = 1.0
    x_values = []
    y_values = []
    while x <= 6.0:
        x = round(x, 1)
        x_values.append(str(x))
        y_values.append(hist[x])
        x += 0.1
    plt.figure(figsize=(15,5))
    plt.bar(x_values, y_values, align='center', width=0.3)
    plt.xlabel("Return in dollars")
    plt.ylabel("Number of times")
    plt.title(title)
    plt.show()

    
