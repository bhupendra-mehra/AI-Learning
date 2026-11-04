import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
actual = [45000, 52000, 48000, 61000, 70000, 68000]
target = [50000, 50000, 55000, 60000, 65000, 70000]

plt.figure(figsize=(10, 5)) #creates a new canvas/figure in Matplotlib with a width of 10 inches and a height of 5 inches

plt.plot(months, actual, marker="o", label="Actual Revenue")
# plots a line graph of revenue over time months on the x-axis, actual data on the y-axis, places circular markers ("o") on each data point, and labels the trend line as "Actual Revenue" for the chart's legend
plt.plot(months, target, marker="s", linestyle="--", label="Target Revenue")

plt.title("Actual vs Target Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue (₹)")
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("actual_vs_target.png", dpi=150, bbox_inches="tight")
# Close the figure
plt.close()

print("Actual Vs Targe chart saved successfully: actual_vs_target.png")