import matplotlib.pyplot as plt

dep = ["cse", "aiml", "ise", "ece"]
prog = [
    12,
    1,
    4,
    5,
]

plt.pie(prog, labels=dep, autopct="1%.1f%%", startangle=99, shadow=True)
plt.title(" projects undertaken by depaartments")
plt.show()
