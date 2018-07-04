from preprocessing import openFile, getOwlIDs, owlDistanceAndTime
from processing import timebasedAvg

import os

# dataPath = os.path.join('C:\\','Users','s_slim01','Downloads','movebank','movebank','eagle_owl','Eagle owl Reinhard Vohwinkel MPIO','points.shp')
dataPath = os.path.join('/home','torben','Documents','uni','Master','SS_2018','PyGIS','final_submission','movebank','eagle_owl','Eagle owl Reinhard Vohwinkel MPIO','points.shp')

shpData = openFile(dataPath,'ESRI Shapefile')
owlIds = getOwlIDs(shpData)

for owl in owlIds:
    singleOwl = owlDistanceAndTime(owlIds[0],shpData)
    print()
    print(singleOwl)
    interval = 3600000 # 60 min => 1000 * 60 * 60 // 1000 = 1 sec
    timebasedAvg(singleOwl, interval)