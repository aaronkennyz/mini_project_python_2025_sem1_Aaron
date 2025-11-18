import matplotlib.pyplot as plt

months = ["jan", "feb", "march", "april", "may"]

sales = [100, 2003, 300, 4000, 500]
plt.plot(months, sales, marker="o", linestyle="-", linewidth=5)
plt.show()
