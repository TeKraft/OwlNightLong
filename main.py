from preprocessing import *
from processingData import *
from postprocessing import *
from saveMap import *

import os

# dataPath = os.path.join('C:\\','Users','s_slim01','Downloads','movebank','movebank','eagle_owl','Eagle owl Reinhard Vohwinkel MPIO','points.shp')
#dataPath = os.path.join('/home','torben','Documents','uni','Master','SS_2018','PyGIS','final_submission','movebank','eagle_owl','Eagle owl Reinhard Vohwinkel MPIO','points.shp')
# dataPath = os.path.join('C:\\', 'Users', 'hans-', \
# 'Documents', 'Master', '2.Semester', 'PythonInGIS', \
# 'FinalAssignment', 'data', 'movebank', 'movebank', 'eagle_owl', 'Eagle owl Reinhard Vohwinkel MPIO', 'points.shp')
# dataPath = os.path.join('C:\\', 'Users', 'pglah', 'Documents', 'movebank', 'movebank', 'eagle_owl', 'Eagle owl Reinhard Vohwinkel MPIO', 'points.shp')

datadir = os.path.join('C:\\','Users','Tanja','Desktop','Master','PythonInGIS')
dataPath = os.path.join(datadir, 'data','points.shp')
rasterPath = os.path.join(datadir, 'OwlNightLong','raster','dtk_reprojected_clipped.tif')
outputPath = os.path.join(datadir, 'OwlNightLong','map.png')

rasterData = openRaster(rasterPath)
shpData = openFile(dataPath,'ESRI Shapefile')
owlIds = getOwlIDs(shpData)

saveMap(shpData,rasterData,outputPath,'Wistia','YlGn')


averageDistanceAllOwls = []
averageDistanceAllOwlsMonth = []


owlIdsSorted = sorted(owlIds, key=lambda x: x)

counter = 0
for owl in owlIdsSorted:
    print()
    print(owl + ' ' + str(counter+1) + '/' + str(len(owlIdsSorted)))
    if (owl != "3897"):
    # if (owl == "4046" or owl == "3894"): # use to reduce processing time
        singleOwl = owlDistanceAndTime(owl,shpData)
        #interval = 3600000 # 60 min => 1000 * 60 * 60 // 1000 = 1 sec
        month = 0
        while(month < 13):
            distancePerHour = calcDistPerHour(singleOwl, month)
            xyzHour = distHour(distancePerHour)
            # plotAverages(xyz, owl)
            if (month == 0):
                averageDistanceAllOwls.append((owl, xyzHour))
            else:
                if ( len(averageDistanceAllOwlsMonth) < month ):
                    averageDistanceAllOwlsMonth.append([])
                averageDistanceAllOwlsMonth[month-1].append((owl, xyzHour))
            month += 1
    else:
        print('no data')
    counter += 1

# print(averageDistanceAllOwls)
"""
averageDistanceAllOwls
[
    ('id', [(avg, hour), (avg, hour), ...]),
    ('id', [(avg, hour), (avg, hour), ...])
]
"""

avgDistances = adjustEntryPosition(averageDistanceAllOwls)# average for each owl
# xyzAll = prepareXYZDataForPlotting(avgDistances)
# plotAverages(xyzAll, 'OwlNightLong')
hourBased = hourBasedAverageAllOwls(avgDistances)
data = prepareXYDataForPlotting(hourBased)
plotAverages(data, 0)
saveAsCSV(hourBased, 0)

for idx, monthData in enumerate(averageDistanceAllOwlsMonth):
    avgDistancesMonth = adjustEntryPosition(monthData)# average for each owl
    # xyzAll = prepareXYZDataForPlotting(avgDistances)
    # plotAverages(xyzAll, 'OwlNightLong')
    hourBasedMonth = hourBasedAverageAllOwls(avgDistancesMonth)
    dataMonth = prepareXYDataForPlotting(hourBasedMonth)
    plotAverages(dataMonth, idx+1)
    saveAsCSV(hourBasedMonth, idx+1)