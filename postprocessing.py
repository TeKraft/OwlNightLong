from matplotlib import pyplot as plt
import numpy as np

def plotAverages(xyz, title):
    f, plotDist = plt.subplots(1) # Create plot

    # plotLabels = list(set(xyz[2]))
    # if (xyz[3]):
    #     plotLabels = xyz[3]
    # else:
    #     plotLabels = xyz[2]

    # plotDist.plot(xyz[0], xyz[1], label=plotLabels)
    # plotDist.plot(xyz[0], xyz[1], label=plotLabels)
    print()
    print(xyz[0])
    print(xyz[1])
    plotDist.scatter(xyz[0], xyz[1], label=xyz[1], cmap='gnuplot', s=20)
    # plotDist.scatter(xyz[0], xyz[1], c=coloring, label=plotLabels, cmap='gnuplot', s=20)
    # plotDist.plot(xyz[0], xyz[1])

    plotDist.legend(xyz[1])

    plt.title(title)
    plt.xlabel('time in hours')
    plt.ylabel('average distance in m')
    # plotDist.legend()
    # plt.axis('equal')
    plt.show()

def xyzPlotData(array):
    x = []
    y = []
    z = []
    idx = []

    for entry in array:
        x.append(entry[0])
        y.append(entry[1])
        z.append(entry[2])
        idx.append(entry[3])

    output = (x,y,z, idx)   
    return output

def xyzPlotDataAvg(array):
    x = []
    y = []

    for entry in array:
        x.append(entry[0])
        y.append(entry[1])
        # z.append(entry[3])

    output = (x,y)
    return output