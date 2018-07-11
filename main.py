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
averageDistanceAllOwlsMonth = []

counter = 0
for owl in owlIds:
    # owl = owlIds[0]
    print()
    print('new owl')
    if (owl != "3897"): # and counter < 1): (owl == "1750" or owl == "4846"): # 
        print(owl)
        singleOwl = owlDistanceAndTime(owl,shpData)
        #interval = 3600000 # 60 min => 1000 * 60 * 60 // 1000 = 1 sec
        month = 0
        while(month < 13):
            distancePerHour = timebasedAvg(singleOwl, month)
            xyzHour = distHour(distancePerHour)
            # plotAverages(xyz, owl)

            if (month == 0):
                averageDistanceAllOwls.append((owl, xyzHour))
            else:
                # print(month)
                if ( len(averageDistanceAllOwlsMonth) < month ):
                    # print('add')
                    averageDistanceAllOwlsMonth.append([])
                # print(averageDistanceAllOwlsMonth)
                averageDistanceAllOwlsMonth[month-1].append((owl, xyzHour))
                # print(averageDistanceAllOwlsMonth)
            
            month += 1

    else:
        print('nix')
    counter += 1

# print(averageDistanceAllOwls)
"""
averageDistanceAllOwls
[
    ('id', [(avg, hour), (avg, hour), ...]),
    ('id', [(avg, hour), (avg, hour), ...])
]
"""

avgDistances = timebasedAvgAllOwls(averageDistanceAllOwls)# average for each owl
# xyzAll = xyzPlotData(avgDistances)
# plotAverages(xyzAll, 'OwlNightLong')
hourBased = hourBasedAverageAllOwls(avgDistances)
data = xyzPlotDataAvg(hourBased)
plotAverages(data, 'All Averages')

for idx, monthData in enumerate(averageDistanceAllOwlsMonth):
    avgDistancesMonth = timebasedAvgAllOwls(monthData)# average for each owl
    # xyzAll = xyzPlotData(avgDistances)
    # plotAverages(xyzAll, 'OwlNightLong')
    hourBasedMonth = hourBasedAverageAllOwls(avgDistancesMonth)
    dataMonth = xyzPlotDataAvg(hourBasedMonth)
    plotAverages(dataMonth, idx)

