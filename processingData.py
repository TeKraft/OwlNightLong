from datetime import datetime

"""
Function to calculate distance average for a given time interval.
params:
owl: array with tuples (timestamp, distance)
"""
def calcDistPerHour(owl, month):

    measInHour = 0
    distance = 0
    distanceArray = []
    lastDate = -1

    if (month != 0):
        data = list(filter(lambda x: datetime.strptime(x[0], '%Y-%m-%d %H:%M:%S').month == month , owl))
    else:
        data = owl

    for entry in data:
        # time string: '2014-09-04 23:50:16'
        currentDate = datetime.strptime(entry[0], '%Y-%m-%d %H:%M:%S')
        currentHour = currentDate.hour # return hour
        if(lastDate == -1):
            firstDate = currentDate
        else:
            if(currentHour != lastDate.hour):
                distanceArray.append((distance, measInHour, firstDate, lastDate))
                distance = 0
                measInHour = 0
                firstDate = currentDate
    
        measInHour += 1
        distance = distance + entry[1]
        lastDate = currentDate

    return distanceArray
    # return [(interval01, avg), (interval02, avg), ...]

def adjustEntryPosition(owlArray):
    
    output = []

    for idx, owl in enumerate(owlArray):
        owlId = owl[0]
        for entry in owl[1]:
            eachEntry = (entry[1], entry[0], idx, owlId)
            output.append(eachEntry)
    
    return output
    # [
    # (hour, avg, owlId),
    # (hour, avg, avg),
    # ...]

# calculate average of distance of all owls per hour
def hourBasedAverageAllOwls(array):
    """
    array = [
        (hour, distance, idx, owlId), ...
    ]
    """
    arraySorted = sorted(array, key=lambda x: x[0])

    lastHour = -1
    distance = 0
    amountOwls = 0
    distPerHour = []

    for idx, entry in enumerate(arraySorted):
        currentHour = entry[0]

        if( (lastHour != -1 and currentHour != lastHour) ):
            average = distance/amountOwls
            distPerHour.append((lastHour, average))
            distance = 0
            amountOwls = 0
        
        if ( (idx == len(arraySorted)-1) ):
            print('23 Uhr')
            print(idx, len(arraySorted))
            average = distance/amountOwls
            distPerHour.append((lastHour, average))
            distance = 0
            amountOwls = 0
        
        amountOwls += 1
        distance = distance + entry[1]
        lastHour = currentHour

    return distPerHour
    # [ (hour, averageDistance), ... ]

def distHour(array):
    # array => [ (y,z,x), (y,z,x), ... ]
    x = []
    y = []
    z = []

    distPerHour = []
    distance = 0
    flightsOfHour = 0
    lastHour = -1

    arraySorted = sorted(array, key=lambda x: x[2].hour)

    for idx, entry in enumerate(arraySorted):
        """
        entry = [
            (distance, measInHour, firstDate, lastdate), ...
        ]
        """
        # check if amount of measurements in an hour is
        if (entry[1] >= 2):
        
            currentHour = entry[2].hour

            if( (lastHour != -1 and currentHour != lastHour) or (idx == len(arraySorted)-1 ) ):
                average = distance/flightsOfHour
                distPerHour.append((average, lastHour, entry[2].month))
                distance = 0
                flightsOfHour = 0
            
            flightsOfHour += 1
            distance = distance + entry[0]
            lastHour = currentHour

    return (distPerHour)
    
