from matplotlib import pyplot as plt
import numpy as np

def plotAverages(xyz, title):
    plotTitle = getMonth(title)

    # check if data is available for plotting
    if (len(xyz[0]) > 0 and len(xyz[1]) > 0):
        f, plotDist = plt.subplots(1) # Create plot

        plotDist.scatter(xyz[0], xyz[1], label=xyz[1], cmap='gnuplot', s=20)
        # plotDist.scatter(xyz[0], xyz[1], c=coloring, label=plotLabels, cmap='gnuplot', s=20)
        plt.title(plotTitle)
        plt.xlabel('time in hours')
        plt.ylabel('average distance in m')
        plt.ylim(0, 1750)

        # save plot as .png and show
        plt.savefig('./plots/' + plotTitle + '.png')
        print('Saved ' + plotTitle + ' as .png to plots-folder.')
        # plt.show()
    else:
        print('No data available')

def saveAsCSV(data, title):
    fileTitle = getMonth(title)
    np.savetxt('./csv/' + fileTitle + '.csv', data, delimiter=',', header="Hour,# Average Distance")
    print('Saved ' + fileTitle + ' as .csv to csv-folder.')

def getMonth(title):
    month = ['All Owls', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    return month[title]

#unused
def prepareXYZDataForPlotting(array):
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

def prepareXYDataForPlotting(array):
    x = []
    y = []

    for entry in array:
        x.append(entry[0])
        y.append(entry[1])
        # z.append(entry[3])

    output = (x,y)
    return output