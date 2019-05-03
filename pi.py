import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.patches as patches

plt.xkcd()

n = 6

circle = plt.Circle((0, 0), 1, fc='b')

inPoly = patches.RegularPolygon(
    xy=(0, 0),
    numVertices=n,
    radius=1,
    fill=False      # remove background
)

b = 1 / math.cos(np.pi/n)
outPoly = patches.RegularPolygon(
    xy=(0, 0),
    numVertices=n,
    radius=b,
    fill=False      # remove background
)

plt.gca().add_patch(circle)
plt.gca().add_patch(inPoly)
plt.gca().add_patch(outPoly)


plt.axis('equal')
plt.show()
