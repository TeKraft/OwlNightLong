import ogr
import os
import numpy as np
import sys


dataPath = os.path.join('C:\\','Users','s_slim01','Downloads','movebank','movebank','eagle_owl','Eagle owl Reinhard Vohwinkel MPIO','points.shp')

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

#TODO: Make it work (Set correct attribute filter OR use if...)
def owlDistanceAndTime(owlID, data):
    owlLayer = data.GetLayer(0)
    owlLayer.SetAttributeFilter("tag_ident == 4044") 
    feature = owlLayer.GetNextFeature()    
    while feature:
        timestamp = feature.GetFieldAsString("timestamp")
        print(timestamp)
        feature = owlLayer.GetNextFeature()
    


shpData = openFile(dataPath,'ESRI Shapefile')
owlIds = getOwlIDs(shpData)
owlDistanceAndTime(owlIds[0],shpData)
    


        
