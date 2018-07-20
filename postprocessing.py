from matplotlib import pyplot as plt
import numpy as np

datapath = './plots/'

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

        sunData = getSunData(title)

        if (title > 0):
            plt.axvspan( sunData[0]-0.5, sunData[0]+0.5, color='red', alpha=0.3)
            plt.axvspan( sunData[1]-0.5, sunData[1]+0.5, color='red', alpha=0.3)

        # save plot as .png and show
        plt.savefig(datapath + plotTitle + '.png')
        print('Saved ' + plotTitle + ' as .png to plots-folder.')
        # plt.show()
    else:
        print('No data available')

def saveAsCSV(data, title):
    fileTitle = getMonth(title)
    np.savetxt('./csv/' + fileTitle + '.csv', data, delimiter=',', header="Hour,# Average Distance")
    print('Saved ' + fileTitle + ' as .csv to csv-folder.')

def getMonth(idx):
    month = ['All Owls', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    return month[idx]

def getSunData(idx):
    # average sunrise/sunset from 2011 -> 2017
    # data from http://www.sunrise-and-sunset.com/de/sun/deutschland
    # http://www.sunrise-and-sunset.com/de/sun/deutschland/berlin/2011/april
    month = [ (8.03, 16.25), (7.225, 17.155), (6.495, 18.40), (6.165, 20.035), (5.145, 20.53), (4.275, 21.24), (5.06, 21.15), (5.505, 20.265), (6.41, 19.2), (7.035, 17.405), (7.275, 16.16), (8.055, 15.575) ]
    return month[idx-1]

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