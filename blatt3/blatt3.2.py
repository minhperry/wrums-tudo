import matplotlib.pyplot as plt
import numpy as np

dataX = np.array([9, 6, 12, 10, 8, 9])
dataY = np.array([130, 125, 145, 140, 130, 140])

N = len(dataX)

# Aufgabe a
plt.scatter(dataX, dataY)
# plt.show() # -> zeigt die Grafik an. Entferne das erste #, um die Grafik anzuzeigen.
print("--------------------")

# Aufgabe b
# Kovarianz berechnen

def covariance(x, y):
    x_mean = np.mean(x)
    y_mean = np.mean(y)
    cov = 0
    for i in range(len(x)):
        cov += (x[i] - x_mean) * (y[i] - y_mean)
    return cov / (len(x) - 1)

# print(np.mean(dataX), np.mean(dataY))
print("Kovarianz: ", covariance(dataX, dataY))

# Mit eingebaute Funktion von numpy
print("Kovarianz mit numpy: ", np.cov(dataX, dataY)[0][1])
print("--------------------")

# Aufgabe c
# Kovarianzkoeffizient nach Bravais-Pearson berechnen, mit numpy.std()
def unbkstd(x):
    # ddof=1 für unbekannte Varianz
    return np.std(x, ddof=1)

def cov_coeff(x, y):
    return covariance(x, y) / (unbkstd(x) * unbkstd(y))

# manuell berechnen
def cov_coeff_manual(x, y):
    return covariance(x, y) / (np.sqrt(covariance(x, x)) * np.sqrt(covariance(y, y)))


print("Kovarianzkoeffizient: ", cov_coeff_manual(dataX, dataY))
print(f"Kovarianzkoeffizient mit numpy: ", cov_coeff(dataX, dataY))
print("--------------------")

# Aufgabe d
# Lineare Regression
def lin_reg(x, y):
    a = covariance(x, y) / covariance(x, x)
    b = np.mean(y) - a * np.mean(x)
    return a, b

# Lineare Regression mit numpy
def lin_reg_np(x, y):
    a, b = np.polyfit(x, y, 1)
    return a, b

d, c = lin_reg(dataX, dataY)
d2, c2 = lin_reg_np(dataX, dataY)
print(f"Lineare Regression: y = {d}x + {c}")
print(f"Lineare Regression mit numpy: y = {d2}x + {c2}")

# lineare Regression mit matplotlib anzeigen
plt.scatter(dataX, dataY)
plt.plot(dataX, d * dataX + c, color="red")
# plt.show() # -> zeigt die Grafik an. Entferne das erste #, um die Grafik anzuzeigen.
print("--------------------")

# Aufgabe e
# Spearmans Rangkorrelation berechnen,
# mit eingebaute Funktion von scipy.stats.spearmanr()
from scipy.stats import spearmanr

print("Spearmans Rangkorrelation: ", spearmanr(dataX, dataY)[0])
print("--------------------")