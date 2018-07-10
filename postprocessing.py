import Tkinter
from matplotlib import pyplot as plt
import numpy as np

def plotAverages(distanceArray):
    f, plotDist = plt.subplots(1) # Create plot
    values = xyPlot(distanceArray)
    plotDist.scatter(values[0], values[1], c=values[2], cmap='autumn', s=5)

    plt.axis('equal')
    plt.show()

def xyPlot(array):
    x = []
    y = []
    z = []
    for entry in array:
        x.append(entry[2].hour)
        y.append(entry[0])
        z.append(entry[1])

    return (x,y,z)
'''    
# Create plot
# f, (plotRed, ScatterRed) = plt.subplots(2)
f, plotRed = plt.subplots(1)
# f, scatterRed = plt.subplots(1)

mycolor = []
xAx = []
yAx = []

# Access single features

# shplayer1 = shp_layer
print(mycolor)


for feat in shp_layer:
    pt = feat.geometry()
    x = pt.GetX()
    y = pt.GetY()
    z = feat['ele']

    # No indexing for axarr, beacuse only one subplot
    # plotRed.scatter(x, y, c=z, cmap='autumn', s=5)
    xAx.append(x)
    yAx.append(y)
    mycolor.append(z)


plotRed.scatter(xAx, yAx, c=mycolor, cmap='autumn', s=5)
'''
