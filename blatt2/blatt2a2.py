import matplotlib.pyplot as plt

uefaeuro = [35, 28, 29, 27, 32, 26, 22, 31, 28, 25, 25, 29, 28, 18, 25, 25, 24, 26, 25, 26, 30, 30, 27, 24, 31, 28]
uefawomen = [27, 22, 30, 22, 32, 20, 24, 22, 31, 24, 31, 31, 27, 22, 23, 27, 26, 25, 21, 27, 31, 19, 30]

plt.boxplot([uefaeuro, uefawomen], whis=[0, 100])
plt.xticks([1, 2], ['UEFA Euro 2020', 'UEFA Women\'s Euro 2022'])
plt.show()
