from datetime import datetime

"""
Function to calculate distance average for a given time interval.
params:
owl: array with tuples (timestamp, distance)
"""
def timebasedAvg(owl, month):

    measInHour = 0
    distance = 0
    distanceArray = []
    lastDate = -1

    # if (interval == 0) {
    #     return per all
    # } else {
    #     return per month
    # }

    if (month != 0):
        data = list(filter(lambda x: datetime.strptime(x[0], '%Y-%m-%d %H:%M:%S').month == month , owl))
    else:
        data = owl
        print('new dataset')

    for entry in data:
        # time string: '2014-09-04 23:50:16'
        currentDate = datetime.strptime(entry[0], '%Y-%m-%d %H:%M:%S')
        currentHour = currentDate.hour # return hour
        if(lastDate == -1):
            firstDate = currentDate
        else:
            if(currentHour != lastDate.hour):
                # average = distance # /measInHour
                if (distance > 10000):
                    print(distance)
                distanceArray.append((distance, measInHour, firstDate, lastDate))
                distance = 0
                measInHour = 0
                firstDate = currentDate
    
        measInHour += 1
        distance = distance + entry[1]
        lastDate = currentDate

    # print()
    # print('timebasedAvg')
    # print(distanceArray)
    return distanceArray

    # for each intervaltime tuple(avgOfDistance, amountOfValues)
    # return [(interval01, avg), (interval02, avg), ...]

def timebasedAvgAllOwls(owlArray):
    
    output = []

    # print('finish')
    for idx, owl in enumerate(owlArray):
        owlId = owl[0]
        for entry in owl[1]:
            eachEntry = (entry[1], entry[0], idx, owlId)
            output.append(eachEntry)
    
    # print()
    # print('timebasedAvgAllOwls')
    # print(output)
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

        if( (lastHour != -1 and currentHour != lastHour) or (idx == len(arraySorted)-1) ):
            # print(currentHour)
            average = distance/amountOwls
            distPerHour.append((lastHour, average))
            distance = 0
            amountOwls = 0
        
        amountOwls += 1
        distance = distance + entry[1]
        lastHour = currentHour

    return distPerHour
    # [ (hour, averageDistance), ... ]

# [ (y,z,x), (y,z,x), ... ]
def distHour(array):
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
            # x.append(entry[2].hour)
            # y.append(entry[0])
            # z.append(flightsOfHour)

            currentHour = entry[2].hour

            # sorted([('abc', 121),('abc', 231),('abc', 148), ('abc',221)], key=lambda x: x[1])

            if( (lastHour != -1 and currentHour != lastHour) or (idx == len(arraySorted)-1 ) ):
                average = distance/flightsOfHour
                distPerHour.append((average, lastHour, entry[2].month))
                distance = 0
                flightsOfHour = 0
            
            flightsOfHour += 1
            distance = distance + entry[0]
            lastHour = currentHour

    return (distPerHour)
    # return (x,y,z,distPerHour)
