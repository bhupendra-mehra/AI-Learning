import matplotlib.pyplot as plt

# Example data
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

plt.plot(x, y, marker="o")
plt.title("My First Matplotlib Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)

# Save the graph
plt.savefig("lesson08_plot.png", dpi=300, bbox_inches="tight")

# Close the figure
plt.close()

print("Plot saved successfully: lesson08_plot.png")