import matplotlib.pyplot as plt

data = {(0, 1): 0, (1, 3): 1/6, (3, 4): 1/2, (4, 6): 5/6, (6, 7): 1}

# for each key (a, b) in data, draw a line from a to b horizontally at y = data[(a, b)]
# draw a dot at start of each line except first one
for (a, b), val in data.items():
    plt.hlines(val, a, b, colors="black", linestyles="solid")
    if a != 0:
        plt.scatter(a, val, marker="o", s=50, color="black")

plt.xlabel("X")
plt.ylabel("F(X)")
plt.title("Verteilungsfunktion")

# set x max to 6.5 to make sure last line is visible
plt.xlim(0, 6.5)

plt.show()
