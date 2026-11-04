import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
revenue = [45000, 52000, 48000, 61000, 70000, 68000]

plt.plot(
    months,
    revenue,
    marker="^",
    linestyle="-.",
    label="Revenue",
)

plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue (₹)")
plt.legend()
plt.grid(True)

plt.tight_layout()
# plt.show()

# Save the graph
plt.savefig("line-chart.png", dpi=300, bbox_inches="tight")

# Close the figure
plt.close()

print("Line chart saved successfully: line-chart.png")