import ogr
import os
import numpy as np
import sys
from math import sin, cos, atan2, radians, sqrt, acos

def openFile(path,driverTitle):
    if os.path.exists(path):
        driver = ogr.GetDriverByName(driverTitle) 
        data = driver.Open(path,0)
        if data is None:
            print("Could not open %s" %(path))
            return None
        else:
            print("Opened %s" %(path))
            return data      
    else:
        print("Path does not exist %s" %(path))
        return None 


def getOwlIDs(data):
    owlLayer = data.GetLayer(0)
    feature = owlLayer.GetNextFeature()
    IDvalues = []
    while feature:
        IDvalues.append(feature.GetFieldAsString("tag_ident"))
        feature = owlLayer.GetNextFeature()
    

    return list(set(IDvalues))


def owlDistanceAndTime(owlID, data):
    owlLayer = data.GetLayer(0)
    owlLayer.SetAttributeFilter("tag_ident = '" + owlID + "'")
    feature = owlLayer.GetNextFeature()
    timeValues = []
    timeValuesALL = []
    counter = 0

    while feature:
        timestamp = feature.GetFieldAsString("timestamp")
        owlTableId = feature.GetFieldAsString('tag_ident')

        distance = 0
        if (counter > 0):
             # previous feature
            lat1 = oldFeature.GetFieldAsDouble('lat')
            lon1 = oldFeature.GetFieldAsDouble('long')
            # current feature
            lat2 = feature.GetFieldAsDouble('lat')
            lon2 = feature.GetFieldAsDouble('long')

            distance = calcDistance((lat1, lon1), (lat2, lon2))

        timeValues.append((timestamp, distance))

        # if (owlTableId == owlID):
        counter += 1
        oldFeature = feature
        feature = owlLayer.GetNextFeature()

    return timeValues
    
# calculate distance of two points in m
def calcDistance(latlng1, latlng2):
    lat1 = radians(latlng1[0])
    lat2 = radians(latlng2[0])
    lon1 = radians(latlng1[1])
    lon2 = radians(latlng2[1])
    # distance calculation:
    cosG = sin(lat1)*sin(lat2) + cos(lat1) * cos(lat2) * cos(lon2 - lon1)
    # print(cosG)
    dist = 6378.388 * acos(cosG)
    return dist * 1000


    

