from matplotlib import pyplot as plt
import numpy as np

def plotAverages(xyz, owlId):
    f, plotDist = plt.subplots(1) # Create plot

    # plotLabels = list(set(xyz[2]))
    plotLabels = xyz[2]

    plotDist.scatter(xyz[0], xyz[1], c=xyz[2], label=plotLabels, cmap='autumn', s=5)

    plt.title('owl ID: ' + owlId)
    plt.xlabel('time in hours')
    plt.ylabel('average distance in m')
    plotDist.legend()
    # plt.axis('equal')
    plt.show()

def xyPlot(array):
    x = []
    y = []
    z = []

    averageArray = []
    distance = 0
    counter = 0
    lastHour = -1

    arraySorted = sorted(array, key=lambda x: x[2].hour)

    for entry in arraySorted:
        x.append(entry[2].hour)
        y.append(entry[0])
        z.append(entry[1])

        currentHour = entry[2].hour

        # sorted([('abc', 121),('abc', 231),('abc', 148), ('abc',221)], key=lambda x: x[1])

        if(lastHour != -1 and currentHour != lastHour):
            average = distance/counter
            averageArray.append((average, lastHour))
            distance = 0
            counter = 0
        
        counter += 1
        distance = distance + entry[0]
        lastHour = currentHour

    return (x,y,z,averageArray)
