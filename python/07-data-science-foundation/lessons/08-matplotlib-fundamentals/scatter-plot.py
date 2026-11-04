import matplotlib.pyplot as plt

quantity = [1, 4, 2, 1, 3, 1, 2, 2]
revenue = [55000, 2000, 2400, 8500, 1500, 55000, 4400, 5000]

plt.scatter(quantity, revenue)

plt.title("Quantity vs Order Revenue")
plt.xlabel("Quantity")
plt.ylabel("Revenue (₹)")

plt.tight_layout()
plt.savefig("scatter-chart.png", dpi=300, bbox_inches="tight")

# Close the figure
plt.close()

print("Scatter chart saved successfully: scatter-chart.png")