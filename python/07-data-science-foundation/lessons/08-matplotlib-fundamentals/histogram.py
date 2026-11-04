import matplotlib.pyplot as plt

prices = [
    300, 450, 500, 650, 800,
    1200, 1500, 2200, 2500,
    5000, 8500, 12000, 25000, 55000,
]

plt.hist(prices, bins=5, edgecolor="black")

plt.title("Distribution of Product Prices")
plt.xlabel("Price Range (₹)")
plt.ylabel("Number of Values")

plt.tight_layout()
plt.savefig("histograms-chart.png", dpi=300, bbox_inches="tight")

# Close the figure
plt.close()

print("Histograms chart saved successfully: histograms-chart.png")