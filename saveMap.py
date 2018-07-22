from matplotlib import pyplot as plt
import gdal
import numpy as np
import ogr        
import os

def openRaster(path):
    if os.path.exists(path):                
        data = gdal.Open(path)
        if data is None:
            print("Could not open %s" %(path))
            return None
        else:
            print("Opened %s" %(path))
            return data      
    else:
        print("Path does not exist %s" %(path))
        return None 
        


def saveMap(track, rasterData, outputPNG, trackClr, rasterClr):
    f, axarr = plt.subplots(1)

    #raster
    in_band = rasterData.GetRasterBand(1)
    data = in_band.ReadAsArray()

    geoTransform = rasterData.GetGeoTransform()
    minx = geoTransform[0]
    maxy = geoTransform[3]
    maxx = minx + geoTransform[1] * rasterData.RasterXSize
    miny = maxy + geoTransform[5] * rasterData.RasterYSize

    im = axarr.imshow(data, cmap=rasterClr, extent=(minx, maxx, miny, maxy))

    # track shp
    layer = track.GetLayer(0)
    
    x = []
    y = []
    owlID = []
    for feat in layer:
        pt = feat.geometry()
        x.append(pt.GetX())
        y.append(pt.GetY())
        owlID.append(feat.GetField('tag_ident'))

    
    scat = axarr.scatter(x, y, c=owlID, cmap=trackClr, s=6)
    axarr.set_xlabel('x coordinate')
    axarr.set_ylabel('y coordinate')
    axarr.set_aspect('equal')
    # Save the figure to disk
    
    plt.savefig(outputPNG, dpi=300, format='png')
    print ('finished save PNG at: ', outputPNG)