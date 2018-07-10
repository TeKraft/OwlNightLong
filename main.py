from preprocessing import openFile, getOwlIDs, owlDistanceAndTime
from processing import timebasedAvg
from postprocessing import plotAverages, xyPlot

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
    if (counter < 2):
        print(owl)
        singleOwl = owlDistanceAndTime(owl,shpData)
        #interval = 3600000 # 60 min => 1000 * 60 * 60 // 1000 = 1 sec
        averageDistance = timebasedAvg(singleOwl)
        xyz = xyPlot(averageDistance)
        plotAverages(xyz, owl)
        averageDistanceAllOwls.append((owl, xyz[3]))
    else:
        print('nix')
    counter += 1

# print(averageDistanceAllOwls)

# avgDistances = timebasedAvgAllOwls(averageDistanceAllOwls[0], averageDistanceAllOwls[1])# average for each owl
# xyzAll = xyPlot(avgDistances) 

plotAverages(xyzAll, 'OwlNightLong')
