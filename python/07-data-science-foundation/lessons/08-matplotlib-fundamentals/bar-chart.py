import matplotlib.pyplot as plt

products = ["Laptop", "Mouse", "Keyboard", "Monitor"]
revenue = [110000, 3500, 2400, 8500]

plt.bar(products, revenue) #for horizontal change to barh then as per that change x and y label

plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue (₹)")

plt.tight_layout()



# plt.show()

# Save the graph
plt.savefig("bar-chart.png", dpi=300, bbox_inches="tight")

# Close the figure
plt.close()

print("Bar chart saved successfully: bar-chart.png")