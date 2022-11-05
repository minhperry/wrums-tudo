from matplotlib.patches import Rectangle
import matplotlib.pyplot as mpl

mpl.xlim([140, 200])
mpl.ylim([0, 0.05])

ax = mpl.gca()

rects = [(20, 0.01), (5, 0.032), (5, 0.048), (5, 0.02), (10, 0.028), (15, 0.0013)]
startX = [140, 160, 165, 170, 175, 185]

for i in range(6):
    ax.add_patch(Rectangle((startX[i], 0), rects[i][0], rects[i][1], linewidth=1, edgecolor='black', facecolor='none'))
mpl.show()
