import matplotlib.pyplot as plt

data = {1: 1/6, 2: 0, 3: 1/3, 4: 1/3, 5: 0, 6: 1/6}

points = list(data.keys())
probs = list(data.values())


plt.vlines(points, 0, probs, colors="black", linestyles="solid")
plt.scatter(points, probs, marker="o", s=50, color="black")

plt.xlabel("X")
plt.ylabel("P(X)")
plt.title("Zähldichte")

plt.show()
