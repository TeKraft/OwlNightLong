from preprocessing import *
from processingData import *
from postprocessing import *

import os

# dataPath = os.path.join('C:\\','Users','s_slim01','Downloads','movebank','movebank','eagle_owl','Eagle owl Reinhard Vohwinkel MPIO','points.shp')
dataPath = os.path.join('/home','torben','Documents','uni','Master','SS_2018','PyGIS','final_submission','movebank','eagle_owl','Eagle owl Reinhard Vohwinkel MPIO','points.shp')
# dataPath = os.path.join('C:\\', 'Users', 'hans-', \
# 'Documents', 'Master', '2.Semester', 'PythonInGIS', \
# 'FinalAssignment', 'data', 'movebank', 'movebank', 'eagle_owl', 'Eagle owl Reinhard Vohwinkel MPIO', 'points.shp')

shpData = openFile(dataPath,'ESRI Shapefile')
owlIds = getOwlIDs(shpData)

averageDistanceAllOwls = []

counter = 0
for owl in owlIds:
    # owl = owlIds[0]
    print()
    print('new owl')
    if (owl != "3897"): # and counter < 1):
        print(owl)
        singleOwl = owlDistanceAndTime(owl,shpData)
        #interval = 3600000 # 60 min => 1000 * 60 * 60 // 1000 = 1 sec
        distancePerHour = timebasedAvg(singleOwl)
        xyz = xyPlot(distancePerHour)
        # plotAverages(xyz, owl)
        averageDistanceAllOwls.append((owl, xyz[3]))
    else:
        print('nix')
    counter += 1

# print(averageDistanceAllOwls)
"""
averageDistanceAllOwls
[
    ('id', [(avg, hour), (acg, hour), ...]),
    ('id', [(avg, hour), (acg, hour), ...])
]
"""

avgDistances = timebasedAvgAllOwls(averageDistanceAllOwls)# average for each owl
xyzAll = xyzPlotData(avgDistances)
plotAverages(xyzAll, 'OwlNightLong')

hourBased = hourBasedAverageAllOwls(avgDistances)
data = xyzPlotDataAvg(hourBased)
plotAverages(data, 'All Averages')

